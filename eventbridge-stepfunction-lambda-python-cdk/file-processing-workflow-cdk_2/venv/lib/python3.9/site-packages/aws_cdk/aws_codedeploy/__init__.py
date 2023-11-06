'''
# AWS CodeDeploy Construct Library

## Table of Contents

* [Introduction](#introduction)
* Deploying to Amazon EC2 and on-premise instances

  * [EC2/on-premise Applications](#ec2on-premise-applications)
  * [EC2/on-premise Deployment Groups](#ec2on-premise-deployment-groups)
  * [EC2/on-premise Deployment Configurations](#ec2on-premise-deployment-configurations)
* Deploying to AWS Lambda functions

  * [Lambda Applications](#lambda-applications)
  * [Lambda Deployment Groups](#lambda-deployment-groups)
  * [Lambda Deployment Configurations](#lambda-deployment-configurations)
* Deploying to Amazon ECS services

  * [ECS Applications](#ecs-applications)
  * [ECS Deployment Groups](#ecs-deployment-groups)
  * [ECS Deployment Configurations](#ecs-deployment-configurations)
  * [ECS Deployments](#ecs-deployments)

## Introduction

AWS CodeDeploy is a deployment service that automates application deployments to
Amazon EC2 instances, on-premises instances, serverless Lambda functions, or
Amazon ECS services.

The CDK currently supports Amazon EC2, on-premise, AWS Lambda, and Amazon ECS applications.

## EC2/on-premise Applications

To create a new CodeDeploy Application that deploys to EC2/on-premise instances:

```python
application = codedeploy.ServerApplication(self, "CodeDeployApplication",
    application_name="MyApplication"
)
```

To import an already existing Application:

```python
application = codedeploy.ServerApplication.from_server_application_name(self, "ExistingCodeDeployApplication", "MyExistingApplication")
```

## EC2/on-premise Deployment Groups

To create a new CodeDeploy Deployment Group that deploys to EC2/on-premise instances:

```python
import aws_cdk.aws_autoscaling as autoscaling
import aws_cdk.aws_cloudwatch as cloudwatch

# application: codedeploy.ServerApplication
# asg: autoscaling.AutoScalingGroup
# alarm: cloudwatch.Alarm

deployment_group = codedeploy.ServerDeploymentGroup(self, "CodeDeployDeploymentGroup",
    application=application,
    deployment_group_name="MyDeploymentGroup",
    auto_scaling_groups=[asg],
    # adds User Data that installs the CodeDeploy agent on your auto-scaling groups hosts
    # default: true
    install_agent=True,
    # adds EC2 instances matching tags
    ec2_instance_tags=codedeploy.InstanceTagSet({
        # any instance with tags satisfying
        # key1=v1 or key1=v2 or key2 (any value) or value v3 (any key)
        # will match this group
        "key1": ["v1", "v2"],
        "key2": [],
        "": ["v3"]
    }),
    # adds on-premise instances matching tags
    on_premise_instance_tags=codedeploy.InstanceTagSet({
        "key1": ["v1", "v2"]
    }, {
        "key2": ["v3"]
    }),
    # CloudWatch alarms
    alarms=[alarm],
    # whether to ignore failure to fetch the status of alarms from CloudWatch
    # default: false
    ignore_poll_alarms_failure=False,
    # auto-rollback configuration
    auto_rollback=codedeploy.AutoRollbackConfig(
        failed_deployment=True,  # default: true
        stopped_deployment=True,  # default: false
        deployment_in_alarm=True
    )
)
```

All properties are optional - if you don't provide an Application,
one will be automatically created.

To import an already existing Deployment Group:

```python
# application: codedeploy.ServerApplication

deployment_group = codedeploy.ServerDeploymentGroup.from_server_deployment_group_attributes(self, "ExistingCodeDeployDeploymentGroup",
    application=application,
    deployment_group_name="MyExistingDeploymentGroup"
)
```

### Load balancers

You can [specify a load balancer](https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html)
with the `loadBalancer` property when creating a Deployment Group.

`LoadBalancer` is an abstract class with static factory methods that allow you to create instances of it from various sources.

With Classic Elastic Load Balancer, you provide it directly:

```python
import aws_cdk.aws_elasticloadbalancing as elb

# lb: elb.LoadBalancer

lb.add_listener(
    external_port=80
)

deployment_group = codedeploy.ServerDeploymentGroup(self, "DeploymentGroup",
    load_balancer=codedeploy.LoadBalancer.classic(lb)
)
```

With Application Load Balancer or Network Load Balancer,
you provide a Target Group as the load balancer:

```python
# alb: elbv2.ApplicationLoadBalancer

listener = alb.add_listener("Listener", port=80)
target_group = listener.add_targets("Fleet", port=80)

deployment_group = codedeploy.ServerDeploymentGroup(self, "DeploymentGroup",
    load_balancer=codedeploy.LoadBalancer.application(target_group)
)
```

## EC2/on-premise Deployment Configurations

You can also pass a Deployment Configuration when creating the Deployment Group:

```python
deployment_group = codedeploy.ServerDeploymentGroup(self, "CodeDeployDeploymentGroup",
    deployment_config=codedeploy.ServerDeploymentConfig.ALL_AT_ONCE
)
```

The default Deployment Configuration is `ServerDeploymentConfig.ONE_AT_A_TIME`.

You can also create a custom Deployment Configuration:

```python
deployment_config = codedeploy.ServerDeploymentConfig(self, "DeploymentConfiguration",
    deployment_config_name="MyDeploymentConfiguration",  # optional property
    # one of these is required, but both cannot be specified at the same time
    minimum_healthy_hosts=codedeploy.MinimumHealthyHosts.count(2)
)
```

Or import an existing one:

```python
deployment_config = codedeploy.ServerDeploymentConfig.from_server_deployment_config_name(self, "ExistingDeploymentConfiguration", "MyExistingDeploymentConfiguration")
```

## Lambda Applications

To create a new CodeDeploy Application that deploys to a Lambda function:

```python
application = codedeploy.LambdaApplication(self, "CodeDeployApplication",
    application_name="MyApplication"
)
```

To import an already existing Application:

```python
application = codedeploy.LambdaApplication.from_lambda_application_name(self, "ExistingCodeDeployApplication", "MyExistingApplication")
```

## Lambda Deployment Groups

To enable traffic shifting deployments for Lambda functions, CodeDeploy uses Lambda Aliases, which can balance incoming traffic between two different versions of your function.
Before deployment, the alias sends 100% of invokes to the version used in production.
When you publish a new version of the function to your stack, CodeDeploy will send a small percentage of traffic to the new version, monitor, and validate before shifting 100% of traffic to the new version.

To create a new CodeDeploy Deployment Group that deploys to a Lambda function:

```python
# my_application: codedeploy.LambdaApplication
# func: lambda.Function

version = func.current_version
version1_alias = lambda_.Alias(self, "alias",
    alias_name="prod",
    version=version
)

deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
    application=my_application,  # optional property: one will be created for you if not provided
    alias=version1_alias,
    deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE
)
```

In order to deploy a new version of this function:

1. Reference the version with the latest changes `const version = func.currentVersion`.
2. Re-deploy the stack (this will trigger a deployment).
3. Monitor the CodeDeploy deployment as traffic shifts between the versions.

### Lambda Deployment Rollbacks and Alarms

CodeDeploy will roll back if the deployment fails. You can optionally trigger a rollback when one or more alarms are in a failed state:

```python
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
```

### Pre and Post Hooks

CodeDeploy allows you to run an arbitrary Lambda function before traffic shifting actually starts (PreTraffic Hook) and after it completes (PostTraffic Hook).
With either hook, you have the opportunity to run logic that determines whether the deployment must succeed or fail.
For example, with PreTraffic hook you could run integration tests against the newly created Lambda version (but not serving traffic). With PostTraffic hook, you could run end-to-end validation checks.

```python
# warm_up_user_cache: lambda.Function
# end_to_end_validation: lambda.Function
# alias: lambda.Alias


# pass a hook whe creating the deployment group
deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
    alias=alias,
    deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE,
    pre_hook=warm_up_user_cache
)

# or configure one on an existing deployment group
deployment_group.add_post_hook(end_to_end_validation)
```

### Import an existing Lambda Deployment Group

To import an already existing Deployment Group:

```python
# application: codedeploy.LambdaApplication

deployment_group = codedeploy.LambdaDeploymentGroup.from_lambda_deployment_group_attributes(self, "ExistingCodeDeployDeploymentGroup",
    application=application,
    deployment_group_name="MyExistingDeploymentGroup"
)
```

## Lambda Deployment Configurations

CodeDeploy for Lambda comes with predefined configurations for traffic shifting.
The predefined configurations are available as LambdaDeploymentConfig constants.

```python
# application: codedeploy.LambdaApplication
# alias: lambda.Alias
config = codedeploy.LambdaDeploymentConfig.CANARY_10PERCENT_30MINUTES
deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
    application=application,
    alias=alias,
    deployment_config=config
)
```

If you want to specify your own strategy,
you can do so with the LambdaDeploymentConfig construct,
letting you specify precisely how fast a new function version is deployed.

```python
# application: codedeploy.LambdaApplication
# alias: lambda.Alias
config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
    traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
        interval=Duration.minutes(15),
        percentage=5
    )
)
deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
    application=application,
    alias=alias,
    deployment_config=config
)
```

You can specify a custom name for your deployment config, but if you do you will not be able to update the interval/percentage through CDK.

```python
config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
    traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
        interval=Duration.minutes(15),
        percentage=5
    ),
    deployment_config_name="MyDeploymentConfig"
)
```

To import an already existing Deployment Config:

```python
deployment_config = codedeploy.LambdaDeploymentConfig.from_lambda_deployment_config_name(self, "ExistingDeploymentConfiguration", "MyExistingDeploymentConfiguration")
```

## ECS Applications

To create a new CodeDeploy Application that deploys an ECS service:

```python
application = codedeploy.EcsApplication(self, "CodeDeployApplication",
    application_name="MyApplication"
)
```

To import an already existing Application:

```python
application = codedeploy.EcsApplication.from_ecs_application_name(self, "ExistingCodeDeployApplication", "MyExistingApplication")
```

## ECS Deployment Groups

CodeDeploy can be used to deploy to load-balanced ECS services.
CodeDeploy performs ECS blue-green deployments by managing ECS task sets and load balancer
target groups.  During a blue-green deployment, one task set and target group runs the
original version of your ECS task definition ('blue') and another task set and target group
runs the new version of your ECS task definition ('green').

CodeDeploy orchestrates traffic shifting during ECS blue-green deployments by using
a load balancer listener to balance incoming traffic between the 'blue' and 'green' task sets/target groups
running two different versions of your ECS task definition.
Before deployment, the load balancer listener sends 100% of requests to the 'blue' target group.
When you publish a new version of the task definition and start a CodeDeploy deployment,
CodeDeploy can send a small percentage of traffic to the new 'green' task set behind the 'green' target group,
monitor, and validate before shifting 100% of traffic to the new version.

To create a new CodeDeploy Deployment Group that deploys to an ECS service:

```python
# my_application: codedeploy.EcsApplication
# cluster: ecs.Cluster
# task_definition: ecs.FargateTaskDefinition
# blue_target_group: elbv2.ITargetGroup
# green_target_group: elbv2.ITargetGroup
# listener: elbv2.IApplicationListener


service = ecs.FargateService(self, "Service",
    cluster=cluster,
    task_definition=task_definition,
    deployment_controller=ecs.DeploymentController(
        type=ecs.DeploymentControllerType.CODE_DEPLOY
    )
)

codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
    service=service,
    blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
        blue_target_group=blue_target_group,
        green_target_group=green_target_group,
        listener=listener
    ),
    deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
)
```

In order to deploy a new task definition version to the ECS service,
deploy the changes directly through CodeDeploy using the CodeDeploy APIs or console.
When the `CODE_DEPLOY` deployment controller is used, the ECS service cannot be
deployed with a new task definition version through CloudFormation.

For more information on the behavior of CodeDeploy blue-green deployments for ECS, see
[What happens during an Amazon ECS deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps-ecs.html#deployment-steps-what-happens)
in the CodeDeploy user guide.

Note: If you wish to deploy updates to your ECS service through CDK and CloudFormation instead of directly through CodeDeploy,
using the [`CfnCodeDeployBlueGreenHook`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.CfnCodeDeployBlueGreenHook.html)
construct is the recommended approach instead of using the `EcsDeploymentGroup` construct.  For a comparison
of ECS blue-green deployments through CodeDeploy (using `EcsDeploymentGroup`) and through CloudFormation (using `CfnCodeDeployBlueGreenHook`),
see [Create an Amazon ECS blue/green deployment through AWS CloudFormation](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-create-ecs-cfn.html#differences-ecs-bg-cfn)
in the CloudFormation user guide.

### ECS Deployment Rollbacks and Alarms

CodeDeploy will automatically roll back if a deployment fails.
You can optionally trigger an automatic rollback when one or more alarms are in a failed state during a deployment, or if the deployment stops.

In this example, CodeDeploy will monitor and roll back on alarms set for the
number of unhealthy ECS tasks in each of the blue and green target groups,
as well as alarms set for the number HTTP 5xx responses seen in each of the blue
and green target groups.

```python
import aws_cdk.aws_cloudwatch as cloudwatch

# service: ecs.FargateService
# blue_target_group: elbv2.ApplicationTargetGroup
# green_target_group: elbv2.ApplicationTargetGroup
# listener: elbv2.IApplicationListener


# Alarm on the number of unhealthy ECS tasks in each target group
blue_unhealthy_hosts = cloudwatch.Alarm(self, "BlueUnhealthyHosts",
    alarm_name=Stack.of(self).stack_name + "-Unhealthy-Hosts-Blue",
    metric=blue_target_group.metric_unhealthy_host_count(),
    threshold=1,
    evaluation_periods=2
)

green_unhealthy_hosts = cloudwatch.Alarm(self, "GreenUnhealthyHosts",
    alarm_name=Stack.of(self).stack_name + "-Unhealthy-Hosts-Green",
    metric=green_target_group.metric_unhealthy_host_count(),
    threshold=1,
    evaluation_periods=2
)

# Alarm on the number of HTTP 5xx responses returned by each target group
blue_api_failure = cloudwatch.Alarm(self, "Blue5xx",
    alarm_name=Stack.of(self).stack_name + "-Http-5xx-Blue",
    metric=blue_target_group.metric_http_code_target(elbv2.HttpCodeTarget.TARGET_5XX_COUNT, period=Duration.minutes(1)),
    threshold=1,
    evaluation_periods=1
)

green_api_failure = cloudwatch.Alarm(self, "Green5xx",
    alarm_name=Stack.of(self).stack_name + "-Http-5xx-Green",
    metric=green_target_group.metric_http_code_target(elbv2.HttpCodeTarget.TARGET_5XX_COUNT, period=Duration.minutes(1)),
    threshold=1,
    evaluation_periods=1
)

codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
    # CodeDeploy will monitor these alarms during a deployment and automatically roll back
    alarms=[blue_unhealthy_hosts, green_unhealthy_hosts, blue_api_failure, green_api_failure],
    auto_rollback=codedeploy.AutoRollbackConfig(
        # CodeDeploy will automatically roll back if a deployment is stopped
        stopped_deployment=True
    ),
    service=service,
    blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
        blue_target_group=blue_target_group,
        green_target_group=green_target_group,
        listener=listener
    ),
    deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
)
```

### Deployment validation and manual deployment approval

CodeDeploy blue-green deployments provide an opportunity to validate the new task definition version running on
the 'green' ECS task set prior to shifting any production traffic to the new version.  A second 'test' listener
serving traffic on a different port be added to the load balancer. For example, the test listener can serve
test traffic on port 9001 while the main listener serves production traffic on port 443.
During a blue-green deployment, CodeDeploy can then shift 100% of test traffic over to the 'green'
task set/target group prior to shifting any production traffic during the deployment.

```python
# my_application: codedeploy.EcsApplication
# service: ecs.FargateService
# blue_target_group: elbv2.ITargetGroup
# green_target_group: elbv2.ITargetGroup
# listener: elbv2.IApplicationListener
# test_listener: elbv2.IApplicationListener


codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
    service=service,
    blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
        blue_target_group=blue_target_group,
        green_target_group=green_target_group,
        listener=listener,
        test_listener=test_listener
    ),
    deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
)
```

Automated validation steps can run during the CodeDeploy deployment after shifting test traffic and before
shifting production traffic.  CodeDeploy supports registering Lambda functions as lifecycle hooks for
an ECS deployment.  These Lambda functions can run automated validation steps against the test traffic
port, for example in response to the `AfterAllowTestTraffic` lifecycle hook.  For more information about
how to specify the Lambda functions to run for each CodeDeploy lifecycle hook in an ECS deployment, see the
[AppSpec 'hooks' for an Amazon ECS deployment](https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-ecs)
section in the CodeDeploy user guide.

After provisioning the 'green' ECS task set and re-routing test traffic during a blue-green deployment,
CodeDeploy can wait for approval before continuing the deployment and re-routing production traffic.
During this approval wait time, you can complete additional validation steps prior to exposing the new
'green' task set to production traffic, such as manual testing through the test listener port or
running automated integration test suites.

To approve the deployment, validation steps use the CodeDeploy
[ContinueDeployment API(https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html).
If the ContinueDeployment API is not called within the approval wait time period, CodeDeploy will stop the
deployment and can automatically roll back the deployment.

```python
# service: ecs.FargateService
# blue_target_group: elbv2.ITargetGroup
# green_target_group: elbv2.ITargetGroup
# listener: elbv2.IApplicationListener
# test_listener: elbv2.IApplicationListener


codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
    auto_rollback=codedeploy.AutoRollbackConfig(
        # CodeDeploy will automatically roll back if the 8-hour approval period times out and the deployment stops
        stopped_deployment=True
    ),
    service=service,
    blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
        # The deployment will wait for approval for up to 8 hours before stopping the deployment
        deployment_approval_wait_time=Duration.hours(8),
        blue_target_group=blue_target_group,
        green_target_group=green_target_group,
        listener=listener,
        test_listener=test_listener
    ),
    deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
)
```

### Deployment bake time

You can specify how long CodeDeploy waits before it terminates the original 'blue' ECS task set when a blue-green deployment
is complete in order to let the deployment "bake" a while. During this bake time, CodeDeploy will continue to monitor any
CloudWatch alarms specified for the deployment group and will automatically roll back if those alarms go into a failed state.

```python
from aws_cdk import aws_cloudwatch as cloudwatch

# service: ecs.FargateService
# blue_target_group: elbv2.ITargetGroup
# green_target_group: elbv2.ITargetGroup
# listener: elbv2.IApplicationListener
# blue_unhealthy_hosts: cloudwatch.Alarm
# green_unhealthy_hosts: cloudwatch.Alarm
# blue_api_failure: cloudwatch.Alarm
# green_api_failure: cloudwatch.Alarm


codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
    service=service,
    blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
        blue_target_group=blue_target_group,
        green_target_group=green_target_group,
        listener=listener,
        # CodeDeploy will wait for 30 minutes after completing the blue-green deployment before it terminates the blue tasks
        termination_wait_time=Duration.minutes(30)
    ),
    # CodeDeploy will continue to monitor these alarms during the 30-minute bake time and will automatically
    # roll back if they go into a failed state at any point during the deployment.
    alarms=[blue_unhealthy_hosts, green_unhealthy_hosts, blue_api_failure, green_api_failure],
    deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
)
```

### Import an existing ECS Deployment Group

To import an already existing Deployment Group:

```python
# application: codedeploy.EcsApplication

deployment_group = codedeploy.EcsDeploymentGroup.from_ecs_deployment_group_attributes(self, "ExistingCodeDeployDeploymentGroup",
    application=application,
    deployment_group_name="MyExistingDeploymentGroup"
)
```

## ECS Deployment Configurations

CodeDeploy for ECS comes with predefined configurations for traffic shifting.
The predefined configurations are available as LambdaDeploymentConfig constants.

```python
config = codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
```

If you want to specify your own strategy,
you can do so with the EcsDeploymentConfig construct,
letting you specify precisely how fast an ECS service is deployed.

```python
codedeploy.EcsDeploymentConfig(self, "CustomConfig",
    traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
        interval=Duration.minutes(15),
        percentage=5
    )
)
```

You can specify a custom name for your deployment config, but if you do you will not be able to update the interval/percentage through CDK.

```python
config = codedeploy.EcsDeploymentConfig(self, "CustomConfig",
    traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
        interval=Duration.minutes(15),
        percentage=5
    ),
    deployment_config_name="MyDeploymentConfig"
)
```

Or import an existing one:

```python
deployment_config = codedeploy.EcsDeploymentConfig.from_ecs_deployment_config_name(self, "ExistingDeploymentConfiguration", "MyExistingDeploymentConfiguration")
```

## ECS Deployments

[![cdk-constructs: Experimental](https://img.shields.io/badge/cdk--constructs-experimental-important.svg)](https://constructs.dev/packages/@cdklabs/cdk-ecs-codedeploy)

An experimental construct is available on the Construct Hub called [@cdklabs/cdk-ecs-codedeploy](https://constructs.dev/packages/@cdklabs/cdk-ecs-codedeploy) that manages ECS CodeDeploy deployments.

```python
# deployment_group: codedeploy.IEcsDeploymentGroup
# task_definition: ecs.ITaskDefinition


EcsDeployment({
    "deployment_group": deployment_group,
    "target_service": {
        "task_definition": task_definition,
        "container_name": "mycontainer",
        "container_port": 80
    }
})
```

The deployment will use the AutoRollbackConfig for the EcsDeploymentGroup unless it is overridden in the deployment:

```python
# deployment_group: codedeploy.IEcsDeploymentGroup
# task_definition: ecs.ITaskDefinition


EcsDeployment({
    "deployment_group": deployment_group,
    "target_service": {
        "task_definition": task_definition,
        "container_name": "mycontainer",
        "container_port": 80
    },
    "auto_rollback": {
        "failed_deployment": True,
        "deployment_in_alarm": True,
        "stopped_deployment": False
    }
})
```

By default, the CodeDeploy Deployment will timeout after 30 minutes. The timeout value can be overridden:

```python
# deployment_group: codedeploy.IEcsDeploymentGroup
# task_definition: ecs.ITaskDefinition


EcsDeployment({
    "deployment_group": deployment_group,
    "target_service": {
        "task_definition": task_definition,
        "container_name": "mycontainer",
        "container_port": 80
    },
    "timeout": Duration.minutes(60)
})
```
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
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_autoscaling import (
    AutoScalingGroup as _AutoScalingGroup_c547a7b9,
    IAutoScalingGroup as _IAutoScalingGroup_360f1cde,
)
from ..aws_cloudwatch import IAlarm as _IAlarm_ff3eabc0
from ..aws_ecs import IBaseService as _IBaseService_3fcdd913
from ..aws_elasticloadbalancing import LoadBalancer as _LoadBalancer_a894d40e
from ..aws_elasticloadbalancingv2 import (
    IApplicationTargetGroup as _IApplicationTargetGroup_57799827,
    IListener as _IListener_7f84e41f,
    INetworkTargetGroup as _INetworkTargetGroup_abca2df7,
    ITargetGroup as _ITargetGroup_83c6f8c4,
)
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IRole as _IRole_235f5d8e,
)
from ..aws_lambda import Alias as _Alias_55be8873, IFunction as _IFunction_6adb0ab8


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.AutoRollbackConfig",
    jsii_struct_bases=[],
    name_mapping={
        "deployment_in_alarm": "deploymentInAlarm",
        "failed_deployment": "failedDeployment",
        "stopped_deployment": "stoppedDeployment",
    },
)
class AutoRollbackConfig:
    def __init__(
        self,
        *,
        deployment_in_alarm: typing.Optional[builtins.bool] = None,
        failed_deployment: typing.Optional[builtins.bool] = None,
        stopped_deployment: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''The configuration for automatically rolling back deployments in a given Deployment Group.

        :param deployment_in_alarm: Whether to automatically roll back a deployment during which one of the configured CloudWatch alarms for this Deployment Group went off. Default: true if you've provided any Alarms with the ``alarms`` property, false otherwise
        :param failed_deployment: Whether to automatically roll back a deployment that fails. Default: true
        :param stopped_deployment: Whether to automatically roll back a deployment that was manually stopped. Default: false

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_autoscaling as autoscaling
            import aws_cdk.aws_cloudwatch as cloudwatch
            
            # application: codedeploy.ServerApplication
            # asg: autoscaling.AutoScalingGroup
            # alarm: cloudwatch.Alarm
            
            deployment_group = codedeploy.ServerDeploymentGroup(self, "CodeDeployDeploymentGroup",
                application=application,
                deployment_group_name="MyDeploymentGroup",
                auto_scaling_groups=[asg],
                # adds User Data that installs the CodeDeploy agent on your auto-scaling groups hosts
                # default: true
                install_agent=True,
                # adds EC2 instances matching tags
                ec2_instance_tags=codedeploy.InstanceTagSet({
                    # any instance with tags satisfying
                    # key1=v1 or key1=v2 or key2 (any value) or value v3 (any key)
                    # will match this group
                    "key1": ["v1", "v2"],
                    "key2": [],
                    "": ["v3"]
                }),
                # adds on-premise instances matching tags
                on_premise_instance_tags=codedeploy.InstanceTagSet({
                    "key1": ["v1", "v2"]
                }, {
                    "key2": ["v3"]
                }),
                # CloudWatch alarms
                alarms=[alarm],
                # whether to ignore failure to fetch the status of alarms from CloudWatch
                # default: false
                ignore_poll_alarms_failure=False,
                # auto-rollback configuration
                auto_rollback=codedeploy.AutoRollbackConfig(
                    failed_deployment=True,  # default: true
                    stopped_deployment=True,  # default: false
                    deployment_in_alarm=True
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__689450aae2d9ca9a482d433f9f5a1fc7e3667c388258352cecb6392405eed69a)
            check_type(argname="argument deployment_in_alarm", value=deployment_in_alarm, expected_type=type_hints["deployment_in_alarm"])
            check_type(argname="argument failed_deployment", value=failed_deployment, expected_type=type_hints["failed_deployment"])
            check_type(argname="argument stopped_deployment", value=stopped_deployment, expected_type=type_hints["stopped_deployment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_in_alarm is not None:
            self._values["deployment_in_alarm"] = deployment_in_alarm
        if failed_deployment is not None:
            self._values["failed_deployment"] = failed_deployment
        if stopped_deployment is not None:
            self._values["stopped_deployment"] = stopped_deployment

    @builtins.property
    def deployment_in_alarm(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically roll back a deployment during which one of the configured CloudWatch alarms for this Deployment Group went off.

        :default: true if you've provided any Alarms with the ``alarms`` property, false otherwise
        '''
        result = self._values.get("deployment_in_alarm")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def failed_deployment(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically roll back a deployment that fails.

        :default: true
        '''
        result = self._values.get("failed_deployment")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def stopped_deployment(self) -> typing.Optional[builtins.bool]:
        '''Whether to automatically roll back a deployment that was manually stopped.

        :default: false
        '''
        result = self._values.get("stopped_deployment")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AutoRollbackConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.BaseDeploymentConfigOptions",
    jsii_struct_bases=[],
    name_mapping={"deployment_config_name": "deploymentConfigName"},
)
class BaseDeploymentConfigOptions:
    def __init__(
        self,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties of ``BaseDeploymentConfig``.

        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            base_deployment_config_options = codedeploy.BaseDeploymentConfigOptions(
                deployment_config_name="deploymentConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05a78df220a94eafb19c1fb09bf8cd1183e1f0942b3041c0d3aed8a339fd8ada)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the Deployment Configuration.

        :default: - automatically generated name
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDeploymentConfigOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.BaseDeploymentConfigProps",
    jsii_struct_bases=[BaseDeploymentConfigOptions],
    name_mapping={
        "deployment_config_name": "deploymentConfigName",
        "compute_platform": "computePlatform",
        "minimum_healthy_hosts": "minimumHealthyHosts",
        "traffic_routing": "trafficRouting",
    },
)
class BaseDeploymentConfigProps(BaseDeploymentConfigOptions):
    def __init__(
        self,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
        compute_platform: typing.Optional["ComputePlatform"] = None,
        minimum_healthy_hosts: typing.Optional["MinimumHealthyHosts"] = None,
        traffic_routing: typing.Optional["TrafficRouting"] = None,
    ) -> None:
        '''Complete base deployment config properties that are required to be supplied by the implementation of the BaseDeploymentConfig class.

        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        :param compute_platform: The destination compute platform for the deployment. Default: ComputePlatform.Server
        :param minimum_healthy_hosts: Minimum number of healthy hosts. Default: None
        :param traffic_routing: The configuration that specifies how traffic is shifted during a deployment. Only applicable to ECS and Lambda deployments, and must not be specified for Server deployments. Default: None

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            # minimum_healthy_hosts: codedeploy.MinimumHealthyHosts
            # traffic_routing: codedeploy.TrafficRouting
            
            base_deployment_config_props = codedeploy.BaseDeploymentConfigProps(
                compute_platform=codedeploy.ComputePlatform.SERVER,
                deployment_config_name="deploymentConfigName",
                minimum_healthy_hosts=minimum_healthy_hosts,
                traffic_routing=traffic_routing
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d482592e3c5f65fb9559b3e230fe81eab72a36fdd6c5a5b3cad1b4206b327f9f)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument compute_platform", value=compute_platform, expected_type=type_hints["compute_platform"])
            check_type(argname="argument minimum_healthy_hosts", value=minimum_healthy_hosts, expected_type=type_hints["minimum_healthy_hosts"])
            check_type(argname="argument traffic_routing", value=traffic_routing, expected_type=type_hints["traffic_routing"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if compute_platform is not None:
            self._values["compute_platform"] = compute_platform
        if minimum_healthy_hosts is not None:
            self._values["minimum_healthy_hosts"] = minimum_healthy_hosts
        if traffic_routing is not None:
            self._values["traffic_routing"] = traffic_routing

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the Deployment Configuration.

        :default: - automatically generated name
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_platform(self) -> typing.Optional["ComputePlatform"]:
        '''The destination compute platform for the deployment.

        :default: ComputePlatform.Server
        '''
        result = self._values.get("compute_platform")
        return typing.cast(typing.Optional["ComputePlatform"], result)

    @builtins.property
    def minimum_healthy_hosts(self) -> typing.Optional["MinimumHealthyHosts"]:
        '''Minimum number of healthy hosts.

        :default: None
        '''
        result = self._values.get("minimum_healthy_hosts")
        return typing.cast(typing.Optional["MinimumHealthyHosts"], result)

    @builtins.property
    def traffic_routing(self) -> typing.Optional["TrafficRouting"]:
        '''The configuration that specifies how traffic is shifted during a deployment.

        Only applicable to ECS and Lambda deployments, and must not be specified for Server deployments.

        :default: None
        '''
        result = self._values.get("traffic_routing")
        return typing.cast(typing.Optional["TrafficRouting"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseDeploymentConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.BaseTrafficShiftingConfigProps",
    jsii_struct_bases=[],
    name_mapping={"interval": "interval", "percentage": "percentage"},
)
class BaseTrafficShiftingConfigProps:
    def __init__(
        self,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> None:
        '''Common properties of traffic shifting routing configurations.

        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_codedeploy as codedeploy
            
            base_traffic_shifting_config_props = codedeploy.BaseTrafficShiftingConfigProps(
                interval=cdk.Duration.minutes(30),
                percentage=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d5ec69046dd60e940973497323ace19e7ca99f17fbf8c276127a2f0ac4bce26)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "percentage": percentage,
        }

    @builtins.property
    def interval(self) -> _Duration_4839e8c3:
        '''The amount of time between traffic shifts.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage to increase traffic on each traffic shift.'''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BaseTrafficShiftingConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.CanaryTrafficRoutingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "canary_interval": "canaryInterval",
        "canary_percentage": "canaryPercentage",
    },
)
class CanaryTrafficRoutingConfig:
    def __init__(
        self,
        *,
        canary_interval: jsii.Number,
        canary_percentage: jsii.Number,
    ) -> None:
        '''Represents the configuration specific to canary traffic shifting.

        :param canary_interval: The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary`` deployment.
        :param canary_percentage: The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            canary_traffic_routing_config = codedeploy.CanaryTrafficRoutingConfig(
                canary_interval=123,
                canary_percentage=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b220d2e40da00bdd6575561fd7cdb02d36ddf0940793b63fdbd380655db12905)
            check_type(argname="argument canary_interval", value=canary_interval, expected_type=type_hints["canary_interval"])
            check_type(argname="argument canary_percentage", value=canary_percentage, expected_type=type_hints["canary_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "canary_interval": canary_interval,
            "canary_percentage": canary_percentage,
        }

    @builtins.property
    def canary_interval(self) -> jsii.Number:
        '''The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary`` deployment.'''
        result = self._values.get("canary_interval")
        assert result is not None, "Required property 'canary_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def canary_percentage(self) -> jsii.Number:
        '''The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.'''
        result = self._values.get("canary_percentage")
        assert result is not None, "Required property 'canary_percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CanaryTrafficRoutingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.CfnApplication",
):
    '''The ``AWS::CodeDeploy::Application`` resource creates an AWS CodeDeploy application.

    In CodeDeploy , an application is a name that functions as a container to ensure that the correct combination of revision, deployment configuration, and deployment group are referenced during a deployment. You can use the ``AWS::CodeDeploy::DeploymentGroup`` resource to associate the application with a CodeDeploy deployment group. For more information, see `CodeDeploy Deployments <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-steps.html>`_ in the *AWS CodeDeploy User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codedeploy as codedeploy
        
        cfn_application = codedeploy.CfnApplication(self, "MyCfnApplication",
            application_name="applicationName",
            compute_platform="computePlatform",
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
        application_name: typing.Optional[builtins.str] = None,
        compute_platform: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_name: A name for the application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: Updates to ``ApplicationName`` are not supported.
        :param compute_platform: The compute platform that CodeDeploy deploys the application to.
        :param tags: The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdb5a43a5eee290cb73c7a01531e1ffdf06d171c94caaa945bee8063be1b20cb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            application_name=application_name,
            compute_platform=compute_platform,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__472dad38d3229c543cd45d013c4792382a9a9ff72b6a1c296cd46ddee9866459)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9a41fadf993de0854abe41941db98e76215ad0ec2ffd27ae1223e12e06bacf4c)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> typing.Optional[builtins.str]:
        '''A name for the application.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__728dce9dc041502139649117dd6edec48c37d9c568f82ee3be92de1b22e2d700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''The compute platform that CodeDeploy deploys the application to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computePlatform"))

    @compute_platform.setter
    def compute_platform(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1915728b28efc5c1d28ee6eddc170806e157b6c8dea55af22c18fe4e3b4ac191)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computePlatform", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The metadata that you apply to CodeDeploy applications to help you organize and categorize them.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b760e30495233c290b05641b219df0417ec34a7cdcb66209b76925733db09c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "compute_platform": "computePlatform",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
        compute_platform: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param application_name: A name for the application. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: Updates to ``ApplicationName`` are not supported.
        :param compute_platform: The compute platform that CodeDeploy deploys the application to.
        :param tags: The metadata that you apply to CodeDeploy applications to help you organize and categorize them. Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            cfn_application_props = codedeploy.CfnApplicationProps(
                application_name="applicationName",
                compute_platform="computePlatform",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3aeaaf4451457e6e36767224eb97c6e700e8d8faacb23edf47d5dd4c18588590)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument compute_platform", value=compute_platform, expected_type=type_hints["compute_platform"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name
        if compute_platform is not None:
            self._values["compute_platform"] = compute_platform
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''A name for the application.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the application name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           Updates to ``ApplicationName`` are not supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-applicationname
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''The compute platform that CodeDeploy deploys the application to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-computeplatform
        '''
        result = self._values.get("compute_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The metadata that you apply to CodeDeploy applications to help you organize and categorize them.

        Each tag consists of a key and an optional value, both of which you define.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html#cfn-codedeploy-application-tags
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


@jsii.implements(_IInspectable_c2943556)
class CfnDeploymentConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentConfig",
):
    '''The ``AWS::CodeDeploy::DeploymentConfig`` resource creates a set of deployment rules, deployment success conditions, and deployment failure conditions that AWS CodeDeploy uses during a deployment.

    The deployment configuration specifies, through the use of a ``MinimumHealthyHosts`` value, the number or percentage of instances that must remain available at any time during a deployment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codedeploy as codedeploy
        
        cfn_deployment_config = codedeploy.CfnDeploymentConfig(self, "MyCfnDeploymentConfig",
            compute_platform="computePlatform",
            deployment_config_name="deploymentConfigName",
            minimum_healthy_hosts=codedeploy.CfnDeploymentConfig.MinimumHealthyHostsProperty(
                type="type",
                value=123
            ),
            traffic_routing_config=codedeploy.CfnDeploymentConfig.TrafficRoutingConfigProperty(
                type="type",
        
                # the properties below are optional
                time_based_canary=codedeploy.CfnDeploymentConfig.TimeBasedCanaryProperty(
                    canary_interval=123,
                    canary_percentage=123
                ),
                time_based_linear=codedeploy.CfnDeploymentConfig.TimeBasedLinearProperty(
                    linear_interval=123,
                    linear_percentage=123
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compute_platform: typing.Optional[builtins.str] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentConfig.MinimumHealthyHostsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        traffic_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentConfig.TrafficRoutingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param compute_platform: The destination platform type for the deployment ( ``Lambda`` , ``Server`` , or ``ECS`` ).
        :param deployment_config_name: A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param minimum_healthy_hosts: The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value. The type parameter takes either of the following values: - HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value. - FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances. The value parameter takes an integer. For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95. For more information about instance health, see `CodeDeploy Instance Health <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`_ in the AWS CodeDeploy User Guide.
        :param traffic_routing_config: The configuration that specifies how the deployment traffic is routed.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1601263a429a6a400738eca0c5abc3bd436649919830aa684054ba853d401c1f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentConfigProps(
            compute_platform=compute_platform,
            deployment_config_name=deployment_config_name,
            minimum_healthy_hosts=minimum_healthy_hosts,
            traffic_routing_config=traffic_routing_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de25cf19eea9e6556b0b2281a81290d8a5bf22139c91cc21523d85735c1acaa3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7f45dd75f7b342e01e5b93540f71f720aa8d7caaf6291470bbe12a5b6f3885e9)
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
    @jsii.member(jsii_name="computePlatform")
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''The destination platform type for the deployment ( ``Lambda`` , ``Server`` , or ``ECS`` ).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computePlatform"))

    @compute_platform.setter
    def compute_platform(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fccd76b57c8ae8e5170ce23818cd0a34ba59302c6ce3d4c180222152061e2922)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computePlatform", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''A name for the deployment configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentConfigName"))

    @deployment_config_name.setter
    def deployment_config_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2be2e5144bd03df4a4fa40048f27e95c3e5304df13985412b42828a3a74d0e4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="minimumHealthyHosts")
    def minimum_healthy_hosts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.MinimumHealthyHostsProperty"]]:
        '''The minimum number of healthy instances that should be available at any time during the deployment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.MinimumHealthyHostsProperty"]], jsii.get(self, "minimumHealthyHosts"))

    @minimum_healthy_hosts.setter
    def minimum_healthy_hosts(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.MinimumHealthyHostsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a51d4f90c94e060ed843233d31547707cbf9d10d3d4de60cd6205bda621edc94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumHealthyHosts", value)

    @builtins.property
    @jsii.member(jsii_name="trafficRoutingConfig")
    def traffic_routing_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TrafficRoutingConfigProperty"]]:
        '''The configuration that specifies how the deployment traffic is routed.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TrafficRoutingConfigProperty"]], jsii.get(self, "trafficRoutingConfig"))

    @traffic_routing_config.setter
    def traffic_routing_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TrafficRoutingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe1bae2a6b88ba41a47472dc8dc7bbf6f72bde54b89b4ed3b8f8e3fd35645ce4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trafficRoutingConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentConfig.MinimumHealthyHostsProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class MinimumHealthyHostsProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''``MinimumHealthyHosts`` is a property of the `DeploymentConfig <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html>`_ resource that defines how many instances must remain healthy during an AWS CodeDeploy deployment.

            :param type: The minimum healthy instance type:. - HOST_COUNT: The minimum number of healthy instance as an absolute value. - FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment. In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment is successful if four or more instance are deployed to successfully. Otherwise, the deployment fails. .. epigraph:: In a call to ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful. For more information, see `AWS CodeDeploy Instance Health <https://docs.aws.amazon.com//codedeploy/latest/userguide/instances-health.html>`_ in the *AWS CodeDeploy User Guide* .
            :param value: The minimum healthy instance value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                minimum_healthy_hosts_property = codedeploy.CfnDeploymentConfig.MinimumHealthyHostsProperty(
                    type="type",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__564f19ccdd0db2b16c3c238ca2a96b350c9884c519827c6fb91e0d1d234c91d7)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The minimum healthy instance type:.

            - HOST_COUNT: The minimum number of healthy instance as an absolute value.
            - FLEET_PERCENT: The minimum number of healthy instance as a percentage of the total number of instance in the deployment.

            In an example of nine instance, if a HOST_COUNT of six is specified, deploy to up to three instances at a time. The deployment is successful if six or more instances are deployed to successfully. Otherwise, the deployment fails. If a FLEET_PERCENT of 40 is specified, deploy to up to five instance at a time. The deployment is successful if four or more instance are deployed to successfully. Otherwise, the deployment fails.
            .. epigraph::

               In a call to ``GetDeploymentConfig`` , CodeDeployDefault.OneAtATime returns a minimum healthy instance type of MOST_CONCURRENCY and a value of 1. This means a deployment to only one instance at a time. (You cannot set the type to MOST_CONCURRENCY, only to HOST_COUNT or FLEET_PERCENT.) In addition, with CodeDeployDefault.OneAtATime, AWS CodeDeploy attempts to ensure that all instances but one are kept in a healthy state during the deployment. Although this allows one instance at a time to be taken offline for a new deployment, it also means that if the deployment to the last instance fails, the overall deployment is still successful.

            For more information, see `AWS CodeDeploy Instance Health <https://docs.aws.amazon.com//codedeploy/latest/userguide/instances-health.html>`_ in the *AWS CodeDeploy User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The minimum healthy instance value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-minimumhealthyhosts.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MinimumHealthyHostsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentConfig.TimeBasedCanaryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "canary_interval": "canaryInterval",
            "canary_percentage": "canaryPercentage",
        },
    )
    class TimeBasedCanaryProperty:
        def __init__(
            self,
            *,
            canary_interval: jsii.Number,
            canary_percentage: jsii.Number,
        ) -> None:
            '''A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in two increments.

            The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.

            :param canary_interval: The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary`` deployment.
            :param canary_percentage: The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                time_based_canary_property = codedeploy.CfnDeploymentConfig.TimeBasedCanaryProperty(
                    canary_interval=123,
                    canary_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c4bcdd7787167974941b5c2516ab391320979aae485b7c1b94a03555868b2102)
                check_type(argname="argument canary_interval", value=canary_interval, expected_type=type_hints["canary_interval"])
                check_type(argname="argument canary_percentage", value=canary_percentage, expected_type=type_hints["canary_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "canary_interval": canary_interval,
                "canary_percentage": canary_percentage,
            }

        @builtins.property
        def canary_interval(self) -> jsii.Number:
            '''The number of minutes between the first and second traffic shifts of a ``TimeBasedCanary`` deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html#cfn-codedeploy-deploymentconfig-timebasedcanary-canaryinterval
            '''
            result = self._values.get("canary_interval")
            assert result is not None, "Required property 'canary_interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def canary_percentage(self) -> jsii.Number:
            '''The percentage of traffic to shift in the first increment of a ``TimeBasedCanary`` deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedcanary.html#cfn-codedeploy-deploymentconfig-timebasedcanary-canarypercentage
            '''
            result = self._values.get("canary_percentage")
            assert result is not None, "Required property 'canary_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedCanaryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentConfig.TimeBasedLinearProperty",
        jsii_struct_bases=[],
        name_mapping={
            "linear_interval": "linearInterval",
            "linear_percentage": "linearPercentage",
        },
    )
    class TimeBasedLinearProperty:
        def __init__(
            self,
            *,
            linear_interval: jsii.Number,
            linear_percentage: jsii.Number,
        ) -> None:
            '''A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in equal increments, with an equal number of minutes between each increment.

            The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.

            :param linear_interval: The number of minutes between each incremental traffic shift of a ``TimeBasedLinear`` deployment.
            :param linear_percentage: The percentage of traffic that is shifted at the start of each increment of a ``TimeBasedLinear`` deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                time_based_linear_property = codedeploy.CfnDeploymentConfig.TimeBasedLinearProperty(
                    linear_interval=123,
                    linear_percentage=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e2df4e7a87402b186b362bc4d946424539c4a60d7802ac7dcc0731829bf567cb)
                check_type(argname="argument linear_interval", value=linear_interval, expected_type=type_hints["linear_interval"])
                check_type(argname="argument linear_percentage", value=linear_percentage, expected_type=type_hints["linear_percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "linear_interval": linear_interval,
                "linear_percentage": linear_percentage,
            }

        @builtins.property
        def linear_interval(self) -> jsii.Number:
            '''The number of minutes between each incremental traffic shift of a ``TimeBasedLinear`` deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html#cfn-codedeploy-deploymentconfig-timebasedlinear-linearinterval
            '''
            result = self._values.get("linear_interval")
            assert result is not None, "Required property 'linear_interval' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def linear_percentage(self) -> jsii.Number:
            '''The percentage of traffic that is shifted at the start of each increment of a ``TimeBasedLinear`` deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-timebasedlinear.html#cfn-codedeploy-deploymentconfig-timebasedlinear-linearpercentage
            '''
            result = self._values.get("linear_percentage")
            assert result is not None, "Required property 'linear_percentage' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeBasedLinearProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentConfig.TrafficRoutingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "time_based_canary": "timeBasedCanary",
            "time_based_linear": "timeBasedLinear",
        },
    )
    class TrafficRoutingConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            time_based_canary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentConfig.TimeBasedCanaryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            time_based_linear: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentConfig.TimeBasedLinearProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The configuration that specifies how traffic is shifted from one version of a Lambda function to another version during an AWS Lambda deployment, or from one Amazon ECS task set to another during an Amazon ECS deployment.

            :param type: The type of traffic shifting ( ``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment configuration.
            :param time_based_canary: A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments. The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.
            :param time_based_linear: A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in equal increments, with an equal number of minutes between each increment. The original and target Lambda function versions or Amazon ECS task sets are specified in the deployment's AppSpec file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                traffic_routing_config_property = codedeploy.CfnDeploymentConfig.TrafficRoutingConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    time_based_canary=codedeploy.CfnDeploymentConfig.TimeBasedCanaryProperty(
                        canary_interval=123,
                        canary_percentage=123
                    ),
                    time_based_linear=codedeploy.CfnDeploymentConfig.TimeBasedLinearProperty(
                        linear_interval=123,
                        linear_percentage=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b1a59608913355745ad3536a5af2b299b48dfb68b88ee15dd0c479874845c5a)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument time_based_canary", value=time_based_canary, expected_type=type_hints["time_based_canary"])
                check_type(argname="argument time_based_linear", value=time_based_linear, expected_type=type_hints["time_based_linear"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if time_based_canary is not None:
                self._values["time_based_canary"] = time_based_canary
            if time_based_linear is not None:
                self._values["time_based_linear"] = time_based_linear

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of traffic shifting ( ``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_based_canary(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TimeBasedCanaryProperty"]]:
            '''A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments.

            The original and target Lambda function versions or ECS task sets are specified in the deployment's AppSpec file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig-timebasedcanary
            '''
            result = self._values.get("time_based_canary")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TimeBasedCanaryProperty"]], result)

        @builtins.property
        def time_based_linear(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TimeBasedLinearProperty"]]:
            '''A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in equal increments, with an equal number of minutes between each increment.

            The original and target Lambda function versions or Amazon ECS task sets are specified in the deployment's AppSpec file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentconfig-trafficroutingconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig-timebasedlinear
            '''
            result = self._values.get("time_based_linear")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentConfig.TimeBasedLinearProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficRoutingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "compute_platform": "computePlatform",
        "deployment_config_name": "deploymentConfigName",
        "minimum_healthy_hosts": "minimumHealthyHosts",
        "traffic_routing_config": "trafficRoutingConfig",
    },
)
class CfnDeploymentConfigProps:
    def __init__(
        self,
        *,
        compute_platform: typing.Optional[builtins.str] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        traffic_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeploymentConfig``.

        :param compute_platform: The destination platform type for the deployment ( ``Lambda`` , ``Server`` , or ``ECS`` ).
        :param deployment_config_name: A name for the deployment configuration. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param minimum_healthy_hosts: The minimum number of healthy instances that should be available at any time during the deployment. There are two parameters expected in the input: type and value. The type parameter takes either of the following values: - HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value. - FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances. The value parameter takes an integer. For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95. For more information about instance health, see `CodeDeploy Instance Health <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`_ in the AWS CodeDeploy User Guide.
        :param traffic_routing_config: The configuration that specifies how the deployment traffic is routed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            cfn_deployment_config_props = codedeploy.CfnDeploymentConfigProps(
                compute_platform="computePlatform",
                deployment_config_name="deploymentConfigName",
                minimum_healthy_hosts=codedeploy.CfnDeploymentConfig.MinimumHealthyHostsProperty(
                    type="type",
                    value=123
                ),
                traffic_routing_config=codedeploy.CfnDeploymentConfig.TrafficRoutingConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    time_based_canary=codedeploy.CfnDeploymentConfig.TimeBasedCanaryProperty(
                        canary_interval=123,
                        canary_percentage=123
                    ),
                    time_based_linear=codedeploy.CfnDeploymentConfig.TimeBasedLinearProperty(
                        linear_interval=123,
                        linear_percentage=123
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d50cfbd3bc3fca6105506273e4e48e992de4fbb025dced2c525ba1da4bacaadb)
            check_type(argname="argument compute_platform", value=compute_platform, expected_type=type_hints["compute_platform"])
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument minimum_healthy_hosts", value=minimum_healthy_hosts, expected_type=type_hints["minimum_healthy_hosts"])
            check_type(argname="argument traffic_routing_config", value=traffic_routing_config, expected_type=type_hints["traffic_routing_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute_platform is not None:
            self._values["compute_platform"] = compute_platform
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if minimum_healthy_hosts is not None:
            self._values["minimum_healthy_hosts"] = minimum_healthy_hosts
        if traffic_routing_config is not None:
            self._values["traffic_routing_config"] = traffic_routing_config

    @builtins.property
    def compute_platform(self) -> typing.Optional[builtins.str]:
        '''The destination platform type for the deployment ( ``Lambda`` , ``Server`` , or ``ECS`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-computeplatform
        '''
        result = self._values.get("compute_platform")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''A name for the deployment configuration.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment configuration name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-deploymentconfigname
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_healthy_hosts(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentConfig.MinimumHealthyHostsProperty]]:
        '''The minimum number of healthy instances that should be available at any time during the deployment.

        There are two parameters expected in the input: type and value.

        The type parameter takes either of the following values:

        - HOST_COUNT: The value parameter represents the minimum number of healthy instances as an absolute value.
        - FLEET_PERCENT: The value parameter represents the minimum number of healthy instances as a percentage of the total number of instances in the deployment. If you specify FLEET_PERCENT, at the start of the deployment, AWS CodeDeploy converts the percentage to the equivalent number of instance and rounds up fractional instances.

        The value parameter takes an integer.

        For example, to set a minimum of 95% healthy instance, specify a type of FLEET_PERCENT and a value of 95.

        For more information about instance health, see `CodeDeploy Instance Health <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-health.html>`_ in the AWS CodeDeploy User Guide.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-minimumhealthyhosts
        '''
        result = self._values.get("minimum_healthy_hosts")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentConfig.MinimumHealthyHostsProperty]], result)

    @builtins.property
    def traffic_routing_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentConfig.TrafficRoutingConfigProperty]]:
        '''The configuration that specifies how the deployment traffic is routed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html#cfn-codedeploy-deploymentconfig-trafficroutingconfig
        '''
        result = self._values.get("traffic_routing_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentConfig.TrafficRoutingConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDeploymentGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup",
):
    '''The ``AWS::CodeDeploy::DeploymentGroup`` resource creates an AWS CodeDeploy deployment group that specifies which instances your application revisions are deployed to, along with other deployment options.

    For more information, see `CreateDeploymentGroup <https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_CreateDeploymentGroup.html>`_ in the *CodeDeploy API Reference* .
    .. epigraph::

       Amazon ECS blue/green deployments through CodeDeploy do not use the ``AWS::CodeDeploy::DeploymentGroup`` resource. To perform Amazon ECS blue/green deployments, use the ``AWS::CodeDeploy::BlueGreen`` hook. See `Perform Amazon ECS blue/green deployments through CodeDeploy using AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html>`_ for more information.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codedeploy as codedeploy
        
        cfn_deployment_group = codedeploy.CfnDeploymentGroup(self, "MyCfnDeploymentGroup",
            application_name="applicationName",
            service_role_arn="serviceRoleArn",
        
            # the properties below are optional
            alarm_configuration=codedeploy.CfnDeploymentGroup.AlarmConfigurationProperty(
                alarms=[codedeploy.CfnDeploymentGroup.AlarmProperty(
                    name="name"
                )],
                enabled=False,
                ignore_poll_alarm_failure=False
            ),
            auto_rollback_configuration=codedeploy.CfnDeploymentGroup.AutoRollbackConfigurationProperty(
                enabled=False,
                events=["events"]
            ),
            auto_scaling_groups=["autoScalingGroups"],
            blue_green_deployment_configuration=codedeploy.CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty(
                deployment_ready_option=codedeploy.CfnDeploymentGroup.DeploymentReadyOptionProperty(
                    action_on_timeout="actionOnTimeout",
                    wait_time_in_minutes=123
                ),
                green_fleet_provisioning_option=codedeploy.CfnDeploymentGroup.GreenFleetProvisioningOptionProperty(
                    action="action"
                ),
                terminate_blue_instances_on_deployment_success=codedeploy.CfnDeploymentGroup.BlueInstanceTerminationOptionProperty(
                    action="action",
                    termination_wait_time_in_minutes=123
                )
            ),
            deployment=codedeploy.CfnDeploymentGroup.DeploymentProperty(
                revision=codedeploy.CfnDeploymentGroup.RevisionLocationProperty(
                    git_hub_location=codedeploy.CfnDeploymentGroup.GitHubLocationProperty(
                        commit_id="commitId",
                        repository="repository"
                    ),
                    revision_type="revisionType",
                    s3_location=codedeploy.CfnDeploymentGroup.S3LocationProperty(
                        bucket="bucket",
                        key="key",
        
                        # the properties below are optional
                        bundle_type="bundleType",
                        e_tag="eTag",
                        version="version"
                    )
                ),
        
                # the properties below are optional
                description="description",
                ignore_application_stop_failures=False
            ),
            deployment_config_name="deploymentConfigName",
            deployment_group_name="deploymentGroupName",
            deployment_style=codedeploy.CfnDeploymentGroup.DeploymentStyleProperty(
                deployment_option="deploymentOption",
                deployment_type="deploymentType"
            ),
            ec2_tag_filters=[codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                key="key",
                type="type",
                value="value"
            )],
            ec2_tag_set=codedeploy.CfnDeploymentGroup.EC2TagSetProperty(
                ec2_tag_set_list=[codedeploy.CfnDeploymentGroup.EC2TagSetListObjectProperty(
                    ec2_tag_group=[codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                        key="key",
                        type="type",
                        value="value"
                    )]
                )]
            ),
            ecs_services=[codedeploy.CfnDeploymentGroup.ECSServiceProperty(
                cluster_name="clusterName",
                service_name="serviceName"
            )],
            load_balancer_info=codedeploy.CfnDeploymentGroup.LoadBalancerInfoProperty(
                elb_info_list=[codedeploy.CfnDeploymentGroup.ELBInfoProperty(
                    name="name"
                )],
                target_group_info_list=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                    name="name"
                )],
                target_group_pair_info_list=[codedeploy.CfnDeploymentGroup.TargetGroupPairInfoProperty(
                    prod_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                        listener_arns=["listenerArns"]
                    ),
                    target_groups=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                        name="name"
                    )],
                    test_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                        listener_arns=["listenerArns"]
                    )
                )]
            ),
            on_premises_instance_tag_filters=[codedeploy.CfnDeploymentGroup.TagFilterProperty(
                key="key",
                type="type",
                value="value"
            )],
            on_premises_tag_set=codedeploy.CfnDeploymentGroup.OnPremisesTagSetProperty(
                on_premises_tag_set_list=[codedeploy.CfnDeploymentGroup.OnPremisesTagSetListObjectProperty(
                    on_premises_tag_group=[codedeploy.CfnDeploymentGroup.TagFilterProperty(
                        key="key",
                        type="type",
                        value="value"
                    )]
                )]
            ),
            outdated_instances_strategy="outdatedInstancesStrategy",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trigger_configurations=[codedeploy.CfnDeploymentGroup.TriggerConfigProperty(
                trigger_events=["triggerEvents"],
                trigger_name="triggerName",
                trigger_target_arn="triggerTargetArn"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: builtins.str,
        service_role_arn: builtins.str,
        alarm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.AlarmConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_rollback_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.AutoRollbackConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_scaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        blue_green_deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.DeploymentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        deployment_style: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.DeploymentStyleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ec2_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.EC2TagFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.EC2TagSetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ecs_services: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.ECSServiceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        load_balancer_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.LoadBalancerInfoProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        on_premises_instance_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TagFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        on_premises_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.OnPremisesTagSetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        outdated_instances_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trigger_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TriggerConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_name: The name of an existing CodeDeploy application to associate this deployment group with.
        :param service_role_arn: A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf. For more information, see `Create a Service Role for AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`_ in the *AWS CodeDeploy User Guide* . .. epigraph:: In some cases, you might need to add a dependency on the service role's policy. For more information, see IAM role policy in `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .
        :param alarm_configuration: Information about the Amazon CloudWatch alarms that are associated with the deployment group.
        :param auto_rollback_configuration: Information about the automatic rollback configuration that is associated with the deployment group. If you specify this property, don't specify the ``Deployment`` property.
        :param auto_scaling_groups: A list of associated Auto Scaling groups that CodeDeploy automatically deploys revisions to when new instances are created. Duplicates are not allowed.
        :param blue_green_deployment_configuration: Information about blue/green deployment options for a deployment group.
        :param deployment: The application revision to deploy to this deployment group. If you specify this property, your target application revision is deployed as soon as the provisioning process is complete. If you specify this property, don't specify the ``AutoRollbackConfiguration`` property.
        :param deployment_config_name: A deployment configuration name or a predefined configuration name. With predefined configurations, you can deploy application revisions to one instance at a time ( ``CodeDeployDefault.OneAtATime`` ), half of the instances at a time ( ``CodeDeployDefault.HalfAtATime`` ), or all the instances at once ( ``CodeDeployDefault.AllAtOnce`` ). For more information and valid values, see `Working with Deployment Configurations <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html>`_ in the *AWS CodeDeploy User Guide* .
        :param deployment_group_name: A name for the deployment group. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment group name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param deployment_style: Attributes that determine the type of deployment to run and whether to route deployment traffic behind a load balancer. If you specify this property with a blue/green deployment type, don't specify the ``AutoScalingGroups`` , ``LoadBalancerInfo`` , or ``Deployment`` properties. .. epigraph:: For blue/green deployments, AWS CloudFormation supports deployments on Lambda compute platforms only. You can perform Amazon ECS blue/green deployments using ``AWS::CodeDeploy::BlueGreen`` hook. See `Perform Amazon ECS blue/green deployments through CodeDeploy using AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html>`_ for more information.
        :param ec2_tag_filters: The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group. CodeDeploy includes all Amazon EC2 instances identified by any of the tags you specify in this deployment group. Duplicates are not allowed. You can specify ``EC2TagFilters`` or ``Ec2TagSet`` , but not both.
        :param ec2_tag_set: Information about groups of tags applied to Amazon EC2 instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same call as ``ec2TagFilter`` .
        :param ecs_services: The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format ``<clustername>:<servicename>`` .
        :param load_balancer_info: Information about the load balancer to use in a deployment. For more information, see `Integrating CodeDeploy with Elastic Load Balancing <https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html>`_ in the *AWS CodeDeploy User Guide* .
        :param on_premises_instance_tag_filters: The on-premises instance tags already applied to on-premises instances that you want to include in the deployment group. CodeDeploy includes all on-premises instances identified by any of the tags you specify in this deployment group. To register on-premises instances with CodeDeploy , see `Working with On-Premises Instances for CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html>`_ in the *AWS CodeDeploy User Guide* . Duplicates are not allowed. You can specify ``OnPremisesInstanceTagFilters`` or ``OnPremisesInstanceTagSet`` , but not both.
        :param on_premises_tag_set: Information about groups of tags applied to on-premises instances. The deployment group includes only on-premises instances identified by all the tag groups. You can specify ``OnPremisesInstanceTagFilters`` or ``OnPremisesInstanceTagSet`` , but not both.
        :param outdated_instances_strategy: 
        :param tags: 
        :param trigger_configurations: Information about triggers associated with the deployment group. Duplicates are not allowed
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afc1bc74c13d6392d70ae9e55ed64b8ec6f2cfed100b230e370997efe94283fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentGroupProps(
            application_name=application_name,
            service_role_arn=service_role_arn,
            alarm_configuration=alarm_configuration,
            auto_rollback_configuration=auto_rollback_configuration,
            auto_scaling_groups=auto_scaling_groups,
            blue_green_deployment_configuration=blue_green_deployment_configuration,
            deployment=deployment,
            deployment_config_name=deployment_config_name,
            deployment_group_name=deployment_group_name,
            deployment_style=deployment_style,
            ec2_tag_filters=ec2_tag_filters,
            ec2_tag_set=ec2_tag_set,
            ecs_services=ecs_services,
            load_balancer_info=load_balancer_info,
            on_premises_instance_tag_filters=on_premises_instance_tag_filters,
            on_premises_tag_set=on_premises_tag_set,
            outdated_instances_strategy=outdated_instances_strategy,
            tags=tags,
            trigger_configurations=trigger_configurations,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3307a6c43ea08ab3400b7fc835536202e54b37286849aee24bbada2786dd74cf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1713bf55d2b8953310377b4afb89de903e08433197c638276d6cc30c5d16e48d)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''The name of an existing CodeDeploy application to associate this deployment group with.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

    @application_name.setter
    def application_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb70a956898eec48889a079260c8cc973bf43c5f7612ee24bff5dbbbf459fe5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationName", value)

    @builtins.property
    @jsii.member(jsii_name="serviceRoleArn")
    def service_role_arn(self) -> builtins.str:
        '''A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceRoleArn"))

    @service_role_arn.setter
    def service_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66b7f059438dd5722aa9d8f744a278bc5625386e8ce3d4fc1eb8a281e2f306c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="alarmConfiguration")
    def alarm_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AlarmConfigurationProperty"]]:
        '''Information about the Amazon CloudWatch alarms that are associated with the deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AlarmConfigurationProperty"]], jsii.get(self, "alarmConfiguration"))

    @alarm_configuration.setter
    def alarm_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AlarmConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e91a52d4fd08a0b9deb3baefb2ccf408f0cb24c44a56893da4cb20fc1d8c83c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alarmConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="autoRollbackConfiguration")
    def auto_rollback_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AutoRollbackConfigurationProperty"]]:
        '''Information about the automatic rollback configuration that is associated with the deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AutoRollbackConfigurationProperty"]], jsii.get(self, "autoRollbackConfiguration"))

    @auto_rollback_configuration.setter
    def auto_rollback_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AutoRollbackConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69accffcb10c8665244d6da2f6e58570690d0e957e337792a901cb7be04905b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoRollbackConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of associated Auto Scaling groups that CodeDeploy automatically deploys revisions to when new instances are created.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "autoScalingGroups"))

    @auto_scaling_groups.setter
    def auto_scaling_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e04b36b090b14ba34ad491347fe2aca8d51c1e1877ebf2c7e060f1741102a50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingGroups", value)

    @builtins.property
    @jsii.member(jsii_name="blueGreenDeploymentConfiguration")
    def blue_green_deployment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty"]]:
        '''Information about blue/green deployment options for a deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty"]], jsii.get(self, "blueGreenDeploymentConfiguration"))

    @blue_green_deployment_configuration.setter
    def blue_green_deployment_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e01bb8b0c5b5d341a669261e31783fa832409200e3eb8a634fe33223a72f7306)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "blueGreenDeploymentConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="deployment")
    def deployment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentProperty"]]:
        '''The application revision to deploy to this deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentProperty"]], jsii.get(self, "deployment"))

    @deployment.setter
    def deployment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08845fc7de26e5f1faa42234a437c12699ffe9eb475932cf303f7acd1c272595)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deployment", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''A deployment configuration name or a predefined configuration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentConfigName"))

    @deployment_config_name.setter
    def deployment_config_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a74c90812b52cdad890ecf4f6486df9ad8780f8c6a1c163cd9479e4971f08402)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentConfigName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''A name for the deployment group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentGroupName"))

    @deployment_group_name.setter
    def deployment_group_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e42dd2dab2a2d9e3bc41f1ad0d0e48a8811bc6c996da34cbbfacc9757b3286d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentStyle")
    def deployment_style(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentStyleProperty"]]:
        '''Attributes that determine the type of deployment to run and whether to route deployment traffic behind a load balancer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentStyleProperty"]], jsii.get(self, "deploymentStyle"))

    @deployment_style.setter
    def deployment_style(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentStyleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf1c6eb87ee1012ff4d9949ecda81e6dcac87415f749d230c6ee6752153ec80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentStyle", value)

    @builtins.property
    @jsii.member(jsii_name="ec2TagFilters")
    def ec2_tag_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagFilterProperty"]]]]:
        '''The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagFilterProperty"]]]], jsii.get(self, "ec2TagFilters"))

    @ec2_tag_filters.setter
    def ec2_tag_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagFilterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee79962691a5c39e41198cbe8d3feba8224218b0f0150b5f282db760c6c767ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2TagFilters", value)

    @builtins.property
    @jsii.member(jsii_name="ec2TagSet")
    def ec2_tag_set(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagSetProperty"]]:
        '''Information about groups of tags applied to Amazon EC2 instances.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagSetProperty"]], jsii.get(self, "ec2TagSet"))

    @ec2_tag_set.setter
    def ec2_tag_set(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagSetProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6196a4cb27800772b6bd881880397500b9e720f740bb7b6289f13d2f51e04863)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2TagSet", value)

    @builtins.property
    @jsii.member(jsii_name="ecsServices")
    def ecs_services(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.ECSServiceProperty"]]]]:
        '''The target Amazon ECS services in the deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.ECSServiceProperty"]]]], jsii.get(self, "ecsServices"))

    @ecs_services.setter
    def ecs_services(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.ECSServiceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e313b8ad9be6363e7a8552e9cf937d4c0cf7ff77b9f105105f6b3bab3b53c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ecsServices", value)

    @builtins.property
    @jsii.member(jsii_name="loadBalancerInfo")
    def load_balancer_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.LoadBalancerInfoProperty"]]:
        '''Information about the load balancer to use in a deployment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.LoadBalancerInfoProperty"]], jsii.get(self, "loadBalancerInfo"))

    @load_balancer_info.setter
    def load_balancer_info(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.LoadBalancerInfoProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f10ac10d280e8586e5bdb5699bdb0c53aab83965020339a2a5611d15d4061e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loadBalancerInfo", value)

    @builtins.property
    @jsii.member(jsii_name="onPremisesInstanceTagFilters")
    def on_premises_instance_tag_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TagFilterProperty"]]]]:
        '''The on-premises instance tags already applied to on-premises instances that you want to include in the deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TagFilterProperty"]]]], jsii.get(self, "onPremisesInstanceTagFilters"))

    @on_premises_instance_tag_filters.setter
    def on_premises_instance_tag_filters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TagFilterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f88440801309d20e368d659f0132d109e5c37cb01b5a5f894053f4f9081f75f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onPremisesInstanceTagFilters", value)

    @builtins.property
    @jsii.member(jsii_name="onPremisesTagSet")
    def on_premises_tag_set(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.OnPremisesTagSetProperty"]]:
        '''Information about groups of tags applied to on-premises instances.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.OnPremisesTagSetProperty"]], jsii.get(self, "onPremisesTagSet"))

    @on_premises_tag_set.setter
    def on_premises_tag_set(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.OnPremisesTagSetProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1da01bcd68da7d01c5ffa220e48c83cd4d65bd034d7416a79c12856e9a25fad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onPremisesTagSet", value)

    @builtins.property
    @jsii.member(jsii_name="outdatedInstancesStrategy")
    def outdated_instances_strategy(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outdatedInstancesStrategy"))

    @outdated_instances_strategy.setter
    def outdated_instances_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9af30b6e3ffc37ae09bbaa003b72063af09adae4e47a022a24f8e942d28ea799)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outdatedInstancesStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca51d486320d92369410ca709970091be367eabeebde41a60143404eeb1cc6a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="triggerConfigurations")
    def trigger_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TriggerConfigProperty"]]]]:
        '''Information about triggers associated with the deployment group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TriggerConfigProperty"]]]], jsii.get(self, "triggerConfigurations"))

    @trigger_configurations.setter
    def trigger_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TriggerConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19f14404bcc2f5c2897842d997eb29c01baf8bcd6619fdc09e6b87d0df1f7693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerConfigurations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.AlarmConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarms": "alarms",
            "enabled": "enabled",
            "ignore_poll_alarm_failure": "ignorePollAlarmFailure",
        },
    )
    class AlarmConfigurationProperty:
        def __init__(
            self,
            *,
            alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.AlarmProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The ``AlarmConfiguration`` property type configures CloudWatch alarms for an AWS CodeDeploy deployment group.

            ``AlarmConfiguration`` is a property of the `DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource.

            :param alarms: A list of alarms configured for the deployment or deployment group. A maximum of 10 alarms can be added.
            :param enabled: Indicates whether the alarm configuration is enabled.
            :param ignore_poll_alarm_failure: Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch . The default value is ``false`` . - ``true`` : The deployment proceeds even if alarm status information can't be retrieved from CloudWatch . - ``false`` : The deployment stops if alarm status information can't be retrieved from CloudWatch .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                alarm_configuration_property = codedeploy.CfnDeploymentGroup.AlarmConfigurationProperty(
                    alarms=[codedeploy.CfnDeploymentGroup.AlarmProperty(
                        name="name"
                    )],
                    enabled=False,
                    ignore_poll_alarm_failure=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4a9049a177037c3e8ef4e71b7faa8d7ccdc08bd8b6c11e4af29269d336bc4d6f)
                check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument ignore_poll_alarm_failure", value=ignore_poll_alarm_failure, expected_type=type_hints["ignore_poll_alarm_failure"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alarms is not None:
                self._values["alarms"] = alarms
            if enabled is not None:
                self._values["enabled"] = enabled
            if ignore_poll_alarm_failure is not None:
                self._values["ignore_poll_alarm_failure"] = ignore_poll_alarm_failure

        @builtins.property
        def alarms(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AlarmProperty"]]]]:
            '''A list of alarms configured for the deployment or deployment group.

            A maximum of 10 alarms can be added.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-alarms
            '''
            result = self._values.get("alarms")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.AlarmProperty"]]]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the alarm configuration is enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ignore_poll_alarm_failure(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether a deployment should continue if information about the current state of alarms cannot be retrieved from Amazon CloudWatch .

            The default value is ``false`` .

            - ``true`` : The deployment proceeds even if alarm status information can't be retrieved from CloudWatch .
            - ``false`` : The deployment stops if alarm status information can't be retrieved from CloudWatch .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html#cfn-codedeploy-deploymentgroup-alarmconfiguration-ignorepollalarmfailure
            '''
            result = self._values.get("ignore_poll_alarm_failure")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.AlarmProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class AlarmProperty:
        def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
            '''The ``Alarm`` property type specifies a CloudWatch alarm to use for an AWS CodeDeploy deployment group.

            The ``Alarm`` property of the `CodeDeploy DeploymentGroup AlarmConfiguration <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarmconfiguration.html>`_ property contains a list of ``Alarm`` property types.

            :param name: The name of the alarm. Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                alarm_property = codedeploy.CfnDeploymentGroup.AlarmProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03e2a9b2ed59c3404f1d3022f2f33080db793f19b46ee08a71091c574e4f91bf)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the alarm.

            Maximum length is 255 characters. Each alarm name can be used only once in a list of alarms.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-alarm.html#cfn-codedeploy-deploymentgroup-alarm-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.AutoRollbackConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled", "events": "events"},
    )
    class AutoRollbackConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            events: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The ``AutoRollbackConfiguration`` property type configures automatic rollback for an AWS CodeDeploy deployment group when a deployment is not completed successfully.

            For more information, see `Automatic Rollbacks <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html#deployments-rollback-and-redeploy-automatic-rollbacks>`_ in the *AWS CodeDeploy User Guide* .

            ``AutoRollbackConfiguration`` is a property of the `DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource.

            :param enabled: Indicates whether a defined automatic rollback configuration is currently enabled.
            :param events: The event type or types that trigger a rollback. Valid values are ``DEPLOYMENT_FAILURE`` , ``DEPLOYMENT_STOP_ON_ALARM`` , or ``DEPLOYMENT_STOP_ON_REQUEST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                auto_rollback_configuration_property = codedeploy.CfnDeploymentGroup.AutoRollbackConfigurationProperty(
                    enabled=False,
                    events=["events"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a36fa5e61b5cc5a6cdc586ebcdd6624cb49131a6f67b88c2c5bcf44e6a75371f)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled
            if events is not None:
                self._values["events"] = events

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether a defined automatic rollback configuration is currently enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The event type or types that trigger a rollback.

            Valid values are ``DEPLOYMENT_FAILURE`` , ``DEPLOYMENT_STOP_ON_ALARM`` , or ``DEPLOYMENT_STOP_ON_REQUEST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-autorollbackconfiguration.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration-events
            '''
            result = self._values.get("events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoRollbackConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_ready_option": "deploymentReadyOption",
            "green_fleet_provisioning_option": "greenFleetProvisioningOption",
            "terminate_blue_instances_on_deployment_success": "terminateBlueInstancesOnDeploymentSuccess",
        },
    )
    class BlueGreenDeploymentConfigurationProperty:
        def __init__(
            self,
            *,
            deployment_ready_option: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.DeploymentReadyOptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            green_fleet_provisioning_option: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.GreenFleetProvisioningOptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.BlueInstanceTerminationOptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Information about blue/green deployment options for a deployment group.

            :param deployment_ready_option: Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.
            :param green_fleet_provisioning_option: Information about how instances are provisioned for a replacement environment in a blue/green deployment.
            :param terminate_blue_instances_on_deployment_success: Information about whether to terminate instances in the original fleet during a blue/green deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                blue_green_deployment_configuration_property = codedeploy.CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty(
                    deployment_ready_option=codedeploy.CfnDeploymentGroup.DeploymentReadyOptionProperty(
                        action_on_timeout="actionOnTimeout",
                        wait_time_in_minutes=123
                    ),
                    green_fleet_provisioning_option=codedeploy.CfnDeploymentGroup.GreenFleetProvisioningOptionProperty(
                        action="action"
                    ),
                    terminate_blue_instances_on_deployment_success=codedeploy.CfnDeploymentGroup.BlueInstanceTerminationOptionProperty(
                        action="action",
                        termination_wait_time_in_minutes=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b7f7b94df2ec70381780abbf295dc60aec98ca6cee8249a44d4e591068ed620)
                check_type(argname="argument deployment_ready_option", value=deployment_ready_option, expected_type=type_hints["deployment_ready_option"])
                check_type(argname="argument green_fleet_provisioning_option", value=green_fleet_provisioning_option, expected_type=type_hints["green_fleet_provisioning_option"])
                check_type(argname="argument terminate_blue_instances_on_deployment_success", value=terminate_blue_instances_on_deployment_success, expected_type=type_hints["terminate_blue_instances_on_deployment_success"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if deployment_ready_option is not None:
                self._values["deployment_ready_option"] = deployment_ready_option
            if green_fleet_provisioning_option is not None:
                self._values["green_fleet_provisioning_option"] = green_fleet_provisioning_option
            if terminate_blue_instances_on_deployment_success is not None:
                self._values["terminate_blue_instances_on_deployment_success"] = terminate_blue_instances_on_deployment_success

        @builtins.property
        def deployment_ready_option(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentReadyOptionProperty"]]:
            '''Information about the action to take when newly provisioned instances are ready to receive traffic in a blue/green deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-deploymentreadyoption
            '''
            result = self._values.get("deployment_ready_option")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.DeploymentReadyOptionProperty"]], result)

        @builtins.property
        def green_fleet_provisioning_option(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.GreenFleetProvisioningOptionProperty"]]:
            '''Information about how instances are provisioned for a replacement environment in a blue/green deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-greenfleetprovisioningoption
            '''
            result = self._values.get("green_fleet_provisioning_option")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.GreenFleetProvisioningOptionProperty"]], result)

        @builtins.property
        def terminate_blue_instances_on_deployment_success(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.BlueInstanceTerminationOptionProperty"]]:
            '''Information about whether to terminate instances in the original fleet during a blue/green deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-bluegreendeploymentconfiguration.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration-terminateblueinstancesondeploymentsuccess
            '''
            result = self._values.get("terminate_blue_instances_on_deployment_success")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.BlueInstanceTerminationOptionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlueGreenDeploymentConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.BlueInstanceTerminationOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action": "action",
            "termination_wait_time_in_minutes": "terminationWaitTimeInMinutes",
        },
    )
    class BlueInstanceTerminationOptionProperty:
        def __init__(
            self,
            *,
            action: typing.Optional[builtins.str] = None,
            termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about whether instances in the original environment are terminated when a blue/green deployment is successful.

            ``BlueInstanceTerminationOption`` does not apply to Lambda deployments.

            :param action: The action to take on instances in the original environment after a successful blue/green deployment. - ``TERMINATE`` : Instances are terminated after a specified wait time. - ``KEEP_ALIVE`` : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.
            :param termination_wait_time_in_minutes: For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment. For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set. The maximum setting is 2880 minutes (2 days).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                blue_instance_termination_option_property = codedeploy.CfnDeploymentGroup.BlueInstanceTerminationOptionProperty(
                    action="action",
                    termination_wait_time_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ace1975d2c13f6a63616292118c632b714e3f1acc2008b3030af06cf79e1b5e0)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument termination_wait_time_in_minutes", value=termination_wait_time_in_minutes, expected_type=type_hints["termination_wait_time_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action
            if termination_wait_time_in_minutes is not None:
                self._values["termination_wait_time_in_minutes"] = termination_wait_time_in_minutes

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The action to take on instances in the original environment after a successful blue/green deployment.

            - ``TERMINATE`` : Instances are terminated after a specified wait time.
            - ``KEEP_ALIVE`` : Instances are left running after they are deregistered from the load balancer and removed from the deployment group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html#cfn-codedeploy-deploymentgroup-blueinstanceterminationoption-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def termination_wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''For an Amazon EC2 deployment, the number of minutes to wait after a successful blue/green deployment before terminating instances from the original environment.

            For an Amazon ECS deployment, the number of minutes before deleting the original (blue) task set. During an Amazon ECS deployment, CodeDeploy shifts traffic from the original (blue) task set to a replacement (green) task set.

            The maximum setting is 2880 minutes (2 days).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-blueinstanceterminationoption.html#cfn-codedeploy-deploymentgroup-blueinstanceterminationoption-terminationwaittimeinminutes
            '''
            result = self._values.get("termination_wait_time_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BlueInstanceTerminationOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.DeploymentProperty",
        jsii_struct_bases=[],
        name_mapping={
            "revision": "revision",
            "description": "description",
            "ignore_application_stop_failures": "ignoreApplicationStopFailures",
        },
    )
    class DeploymentProperty:
        def __init__(
            self,
            *,
            revision: typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.RevisionLocationProperty", typing.Dict[builtins.str, typing.Any]]],
            description: typing.Optional[builtins.str] = None,
            ignore_application_stop_failures: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''``Deployment`` is a property of the `DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource that specifies an AWS CodeDeploy application revision to be deployed to instances in the deployment group. If you specify an application revision, your target revision is deployed as soon as the provisioning process is complete.

            :param revision: Information about the location of stored application artifacts and the service from which to retrieve them.
            :param description: A comment about the deployment.
            :param ignore_application_stop_failures: If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or ``AfterBlockTraffic`` deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event. For example, if ``ApplicationStop`` fails, the deployment continues with DownloadBundle. If ``BeforeBlockTraffic`` fails, the deployment continues with ``BlockTraffic`` . If ``AfterBlockTraffic`` fails, the deployment continues with ``ApplicationStop`` . If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted. During a deployment, the AWS CodeDeploy agent runs the scripts specified for ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail. If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use ``ignoreApplicationStopFailures`` to specify that the ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` failures should be ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                deployment_property = codedeploy.CfnDeploymentGroup.DeploymentProperty(
                    revision=codedeploy.CfnDeploymentGroup.RevisionLocationProperty(
                        git_hub_location=codedeploy.CfnDeploymentGroup.GitHubLocationProperty(
                            commit_id="commitId",
                            repository="repository"
                        ),
                        revision_type="revisionType",
                        s3_location=codedeploy.CfnDeploymentGroup.S3LocationProperty(
                            bucket="bucket",
                            key="key",
                
                            # the properties below are optional
                            bundle_type="bundleType",
                            e_tag="eTag",
                            version="version"
                        )
                    ),
                
                    # the properties below are optional
                    description="description",
                    ignore_application_stop_failures=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d8d7106fc8a20bc76da89cc9e6f595c31863f43d9fa4324b6eb51a8bc1dada19)
                check_type(argname="argument revision", value=revision, expected_type=type_hints["revision"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument ignore_application_stop_failures", value=ignore_application_stop_failures, expected_type=type_hints["ignore_application_stop_failures"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "revision": revision,
            }
            if description is not None:
                self._values["description"] = description
            if ignore_application_stop_failures is not None:
                self._values["ignore_application_stop_failures"] = ignore_application_stop_failures

        @builtins.property
        def revision(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.RevisionLocationProperty"]:
            '''Information about the location of stored application artifacts and the service from which to retrieve them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-codedeploy-deploymentgroup-deployment-revision
            '''
            result = self._values.get("revision")
            assert result is not None, "Required property 'revision' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.RevisionLocationProperty"], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A comment about the deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-codedeploy-deploymentgroup-deployment-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ignore_application_stop_failures(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, then if an ``ApplicationStop`` , ``BeforeBlockTraffic`` , or ``AfterBlockTraffic`` deployment lifecycle event to an instance fails, then the deployment continues to the next deployment lifecycle event.

            For example, if ``ApplicationStop`` fails, the deployment continues with DownloadBundle. If ``BeforeBlockTraffic`` fails, the deployment continues with ``BlockTraffic`` . If ``AfterBlockTraffic`` fails, the deployment continues with ``ApplicationStop`` .

            If false or not specified, then if a lifecycle event fails during a deployment to an instance, that deployment fails. If deployment to that instance is part of an overall deployment and the number of healthy hosts is not less than the minimum number of healthy hosts, then a deployment to the next instance is attempted.

            During a deployment, the AWS CodeDeploy agent runs the scripts specified for ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` in the AppSpec file from the previous successful deployment. (All other scripts are run from the AppSpec file in the current deployment.) If one of these scripts contains an error and does not run successfully, the deployment can fail.

            If the cause of the failure is a script from the last successful deployment that will never run successfully, create a new deployment and use ``ignoreApplicationStopFailures`` to specify that the ``ApplicationStop`` , ``BeforeBlockTraffic`` , and ``AfterBlockTraffic`` failures should be ignored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment.html#cfn-codedeploy-deploymentgroup-deployment-ignoreapplicationstopfailures
            '''
            result = self._values.get("ignore_application_stop_failures")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.DeploymentReadyOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "action_on_timeout": "actionOnTimeout",
            "wait_time_in_minutes": "waitTimeInMinutes",
        },
    )
    class DeploymentReadyOptionProperty:
        def __init__(
            self,
            *,
            action_on_timeout: typing.Optional[builtins.str] = None,
            wait_time_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about how traffic is rerouted to instances in a replacement environment in a blue/green deployment.

            :param action_on_timeout: Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment. - CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment. - STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using `ContinueDeployment <https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html>`_ . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.
            :param wait_time_in_minutes: The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually. Applies only to the ``STOP_DEPLOYMENT`` option for ``actionOnTimeout`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                deployment_ready_option_property = codedeploy.CfnDeploymentGroup.DeploymentReadyOptionProperty(
                    action_on_timeout="actionOnTimeout",
                    wait_time_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9191e174499f04c901c65523928f85f4ae3a2b619e5821f1dcd040efd65da4d6)
                check_type(argname="argument action_on_timeout", value=action_on_timeout, expected_type=type_hints["action_on_timeout"])
                check_type(argname="argument wait_time_in_minutes", value=wait_time_in_minutes, expected_type=type_hints["wait_time_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action_on_timeout is not None:
                self._values["action_on_timeout"] = action_on_timeout
            if wait_time_in_minutes is not None:
                self._values["wait_time_in_minutes"] = wait_time_in_minutes

        @builtins.property
        def action_on_timeout(self) -> typing.Optional[builtins.str]:
            '''Information about when to reroute traffic from an original environment to a replacement environment in a blue/green deployment.

            - CONTINUE_DEPLOYMENT: Register new instances with the load balancer immediately after the new application revision is installed on the instances in the replacement environment.
            - STOP_DEPLOYMENT: Do not register new instances with a load balancer unless traffic rerouting is started using `ContinueDeployment <https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html>`_ . If traffic rerouting is not started before the end of the specified wait period, the deployment status is changed to Stopped.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html#cfn-codedeploy-deploymentgroup-deploymentreadyoption-actionontimeout
            '''
            result = self._values.get("action_on_timeout")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def wait_time_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The number of minutes to wait before the status of a blue/green deployment is changed to Stopped if rerouting is not started manually.

            Applies only to the ``STOP_DEPLOYMENT`` option for ``actionOnTimeout`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentreadyoption.html#cfn-codedeploy-deploymentgroup-deploymentreadyoption-waittimeinminutes
            '''
            result = self._values.get("wait_time_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentReadyOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.DeploymentStyleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_option": "deploymentOption",
            "deployment_type": "deploymentType",
        },
    )
    class DeploymentStyleProperty:
        def __init__(
            self,
            *,
            deployment_option: typing.Optional[builtins.str] = None,
            deployment_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the type of deployment, either in-place or blue/green, you want to run and whether to route deployment traffic behind a load balancer.

            :param deployment_option: Indicates whether to route deployment traffic behind a load balancer. .. epigraph:: An Amazon EC2 Application Load Balancer or Network Load Balancer is required for an Amazon ECS deployment.
            :param deployment_type: Indicates whether to run an in-place or blue/green deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                deployment_style_property = codedeploy.CfnDeploymentGroup.DeploymentStyleProperty(
                    deployment_option="deploymentOption",
                    deployment_type="deploymentType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6043290c4b631767b4c4d436c6262f5d79a876cdc721342d1ef120eda81d2060)
                check_type(argname="argument deployment_option", value=deployment_option, expected_type=type_hints["deployment_option"])
                check_type(argname="argument deployment_type", value=deployment_type, expected_type=type_hints["deployment_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if deployment_option is not None:
                self._values["deployment_option"] = deployment_option
            if deployment_type is not None:
                self._values["deployment_type"] = deployment_type

        @builtins.property
        def deployment_option(self) -> typing.Optional[builtins.str]:
            '''Indicates whether to route deployment traffic behind a load balancer.

            .. epigraph::

               An Amazon EC2 Application Load Balancer or Network Load Balancer is required for an Amazon ECS deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymentoption
            '''
            result = self._values.get("deployment_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def deployment_type(self) -> typing.Optional[builtins.str]:
            '''Indicates whether to run an in-place or blue/green deployment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deploymentstyle.html#cfn-codedeploy-deploymentgroup-deploymentstyle-deploymenttype
            '''
            result = self._values.get("deployment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentStyleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.EC2TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "type": "type", "value": "value"},
    )
    class EC2TagFilterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about an Amazon EC2 tag filter.

            For more information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see `Tagging Instances for Deployment Groups in AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html>`_ in the *AWS CodeDeploy User Guide* .

            :param key: The tag filter key.
            :param type: The tag filter type:. - ``KEY_ONLY`` : Key only. - ``VALUE_ONLY`` : Value only. - ``KEY_AND_VALUE`` : Key and value.
            :param value: The tag filter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                e_c2_tag_filter_property = codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                    key="key",
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b4123febfdeb60265474ec5b72d4ed596f0cc20f7693da9000b91cc6f3c79da)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The tag filter key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The tag filter type:.

            - ``KEY_ONLY`` : Key only.
            - ``VALUE_ONLY`` : Value only.
            - ``KEY_AND_VALUE`` : Key and value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag filter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagfilter.html#cfn-codedeploy-deploymentgroup-ec2tagfilter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EC2TagFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.EC2TagSetListObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"ec2_tag_group": "ec2TagGroup"},
    )
    class EC2TagSetListObjectProperty:
        def __init__(
            self,
            *,
            ec2_tag_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.EC2TagFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``EC2TagSet`` property type specifies information about groups of tags applied to Amazon EC2 instances.

            The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same template as EC2TagFilters.

            For more information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see `Tagging Instances for Deployment Groups in AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html>`_ in the *AWS CodeDeploy User Guide* .

            ``EC2TagSet`` is a property of the `DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource type.

            :param ec2_tag_group: A list that contains other lists of Amazon EC2 instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                e_c2_tag_set_list_object_property = codedeploy.CfnDeploymentGroup.EC2TagSetListObjectProperty(
                    ec2_tag_group=[codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                        key="key",
                        type="type",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fff319f820316a004ead743ff5c8ad36448e48325ee845cbff5fcfd512773f6c)
                check_type(argname="argument ec2_tag_group", value=ec2_tag_group, expected_type=type_hints["ec2_tag_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ec2_tag_group is not None:
                self._values["ec2_tag_group"] = ec2_tag_group

        @builtins.property
        def ec2_tag_group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagFilterProperty"]]]]:
            '''A list that contains other lists of Amazon EC2 instance tag groups.

            For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagsetlistobject.html#cfn-codedeploy-deploymentgroup-ec2tagsetlistobject-ec2taggroup
            '''
            result = self._values.get("ec2_tag_group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EC2TagSetListObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.EC2TagSetProperty",
        jsii_struct_bases=[],
        name_mapping={"ec2_tag_set_list": "ec2TagSetList"},
    )
    class EC2TagSetProperty:
        def __init__(
            self,
            *,
            ec2_tag_set_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.EC2TagSetListObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``EC2TagSet`` property type specifies information about groups of tags applied to Amazon EC2 instances.

            The deployment group includes only Amazon EC2 instances identified by all the tag groups. ``EC2TagSet`` cannot be used in the same template as ``EC2TagFilter`` .

            For information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see `Tagging Instances for Deployment Groups in AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html>`_ .

            :param ec2_tag_set_list: The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group. CodeDeploy includes all Amazon EC2 instances identified by any of the tags you specify in this deployment group. Duplicates are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                e_c2_tag_set_property = codedeploy.CfnDeploymentGroup.EC2TagSetProperty(
                    ec2_tag_set_list=[codedeploy.CfnDeploymentGroup.EC2TagSetListObjectProperty(
                        ec2_tag_group=[codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                            key="key",
                            type="type",
                            value="value"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a2ba29487a84183313e702cd8e61c88a4f0351eb6fd78f229d2580ae39e8e3e0)
                check_type(argname="argument ec2_tag_set_list", value=ec2_tag_set_list, expected_type=type_hints["ec2_tag_set_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ec2_tag_set_list is not None:
                self._values["ec2_tag_set_list"] = ec2_tag_set_list

        @builtins.property
        def ec2_tag_set_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagSetListObjectProperty"]]]]:
            '''The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group.

            CodeDeploy includes all Amazon EC2 instances identified by any of the tags you specify in this deployment group.

            Duplicates are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ec2tagset.html#cfn-codedeploy-deploymentgroup-ec2tagset-ec2tagsetlist
            '''
            result = self._values.get("ec2_tag_set_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.EC2TagSetListObjectProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EC2TagSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.ECSServiceProperty",
        jsii_struct_bases=[],
        name_mapping={"cluster_name": "clusterName", "service_name": "serviceName"},
    )
    class ECSServiceProperty:
        def __init__(
            self,
            *,
            cluster_name: builtins.str,
            service_name: builtins.str,
        ) -> None:
            '''Contains the service and cluster names used to identify an Amazon ECS deployment's target.

            :param cluster_name: The name of the cluster that the Amazon ECS service is associated with.
            :param service_name: The name of the target Amazon ECS service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                e_cSService_property = codedeploy.CfnDeploymentGroup.ECSServiceProperty(
                    cluster_name="clusterName",
                    service_name="serviceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c6525e95eaf4a440450af5d2e22a53ae3b16a83e28290e48e8aaeda963614fc)
                check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
                check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cluster_name": cluster_name,
                "service_name": service_name,
            }

        @builtins.property
        def cluster_name(self) -> builtins.str:
            '''The name of the cluster that the Amazon ECS service is associated with.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html#cfn-codedeploy-deploymentgroup-ecsservice-clustername
            '''
            result = self._values.get("cluster_name")
            assert result is not None, "Required property 'cluster_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def service_name(self) -> builtins.str:
            '''The name of the target Amazon ECS service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-ecsservice.html#cfn-codedeploy-deploymentgroup-ecsservice-servicename
            '''
            result = self._values.get("service_name")
            assert result is not None, "Required property 'service_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ECSServiceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.ELBInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class ELBInfoProperty:
        def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
            '''The ``ELBInfo`` property type specifies information about the Elastic Load Balancing load balancer used for an CodeDeploy deployment group.

            If you specify the ``ELBInfo`` property, the ``DeploymentStyle.DeploymentOption`` property must be set to ``WITH_TRAFFIC_CONTROL`` for AWS CodeDeploy to route your traffic using the specified load balancers.

            ``ELBInfo`` is a property of the `AWS CodeDeploy DeploymentGroup LoadBalancerInfo <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html>`_ property type.

            :param name: For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment. For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete. .. epigraph:: AWS CloudFormation supports blue/green deployments on AWS Lambda compute platforms only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                e_lBInfo_property = codedeploy.CfnDeploymentGroup.ELBInfoProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1e1b138b2ef18765e84f9ebeee5de46f0b1d44931eeb67199e9796e5085caa7f)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''For blue/green deployments, the name of the load balancer that is used to route traffic from original instances to replacement instances in a blue/green deployment.

            For in-place deployments, the name of the load balancer that instances are deregistered from so they are not serving traffic during a deployment, and then re-registered with after the deployment is complete.
            .. epigraph::

               AWS CloudFormation supports blue/green deployments on AWS Lambda compute platforms only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-elbinfo.html#cfn-codedeploy-deploymentgroup-elbinfo-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ELBInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.GitHubLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"commit_id": "commitId", "repository": "repository"},
    )
    class GitHubLocationProperty:
        def __init__(
            self,
            *,
            commit_id: builtins.str,
            repository: builtins.str,
        ) -> None:
            '''``GitHubLocation`` is a property of the `CodeDeploy DeploymentGroup Revision <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html>`_ property that specifies the location of an application revision that is stored in GitHub.

            :param commit_id: The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.
            :param repository: The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision. Specify the value as ``account/repository`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-githublocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                git_hub_location_property = codedeploy.CfnDeploymentGroup.GitHubLocationProperty(
                    commit_id="commitId",
                    repository="repository"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed147000e92beb1f04d3f0454dc3a873381abc78c1a6b36b05a6e71f1e816253)
                check_type(argname="argument commit_id", value=commit_id, expected_type=type_hints["commit_id"])
                check_type(argname="argument repository", value=repository, expected_type=type_hints["repository"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "commit_id": commit_id,
                "repository": repository,
            }

        @builtins.property
        def commit_id(self) -> builtins.str:
            '''The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-githublocation.html#cfn-codedeploy-deploymentgroup-githublocation-commitid
            '''
            result = self._values.get("commit_id")
            assert result is not None, "Required property 'commit_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def repository(self) -> builtins.str:
            '''The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.

            Specify the value as ``account/repository`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-githublocation.html#cfn-codedeploy-deploymentgroup-githublocation-repository
            '''
            result = self._values.get("repository")
            assert result is not None, "Required property 'repository' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GitHubLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.GreenFleetProvisioningOptionProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action"},
    )
    class GreenFleetProvisioningOptionProperty:
        def __init__(self, *, action: typing.Optional[builtins.str] = None) -> None:
            '''Information about the instances that belong to the replacement environment in a blue/green deployment.

            :param action: The method used to add instances to a replacement environment. - ``DISCOVER_EXISTING`` : Use instances that already exist or will be created manually. - ``COPY_AUTO_SCALING_GROUP`` : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                green_fleet_provisioning_option_property = codedeploy.CfnDeploymentGroup.GreenFleetProvisioningOptionProperty(
                    action="action"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e876af08ef6424feae19da396da079af3de5bc150f304e98d88f569bd98449dc)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if action is not None:
                self._values["action"] = action

        @builtins.property
        def action(self) -> typing.Optional[builtins.str]:
            '''The method used to add instances to a replacement environment.

            - ``DISCOVER_EXISTING`` : Use instances that already exist or will be created manually.
            - ``COPY_AUTO_SCALING_GROUP`` : Use settings from a specified Auto Scaling group to define and create instances in a new Auto Scaling group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-greenfleetprovisioningoption.html#cfn-codedeploy-deploymentgroup-greenfleetprovisioningoption-action
            '''
            result = self._values.get("action")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GreenFleetProvisioningOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.LoadBalancerInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "elb_info_list": "elbInfoList",
            "target_group_info_list": "targetGroupInfoList",
            "target_group_pair_info_list": "targetGroupPairInfoList",
        },
    )
    class LoadBalancerInfoProperty:
        def __init__(
            self,
            *,
            elb_info_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.ELBInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            target_group_info_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TargetGroupInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            target_group_pair_info_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TargetGroupPairInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``LoadBalancerInfo`` property type specifies information about the load balancer or target group used for an AWS CodeDeploy deployment group.

            For more information, see `Integrating CodeDeploy with Elastic Load Balancing <https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html>`_ in the *AWS CodeDeploy User Guide* .

            For AWS CloudFormation to use the properties specified in ``LoadBalancerInfo`` , the ``DeploymentStyle.DeploymentOption`` property must be set to ``WITH_TRAFFIC_CONTROL`` . If ``DeploymentStyle.DeploymentOption`` is not set to ``WITH_TRAFFIC_CONTROL`` , AWS CloudFormation ignores any settings specified in ``LoadBalancerInfo`` .
            .. epigraph::

               AWS CloudFormation supports blue/green deployments on the AWS Lambda compute platform only.

            ``LoadBalancerInfo`` is a property of the `DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource.

            :param elb_info_list: An array that contains information about the load balancer to use for load balancing in a deployment. In Elastic Load Balancing, load balancers are used with Classic Load Balancers. .. epigraph:: Adding more than one load balancer to the array is not supported.
            :param target_group_info_list: An array that contains information about the target group to use for load balancing in a deployment. In Elastic Load Balancing , target groups are used with Application Load Balancers . .. epigraph:: Adding more than one target group to the array is not supported.
            :param target_group_pair_info_list: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                load_balancer_info_property = codedeploy.CfnDeploymentGroup.LoadBalancerInfoProperty(
                    elb_info_list=[codedeploy.CfnDeploymentGroup.ELBInfoProperty(
                        name="name"
                    )],
                    target_group_info_list=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                        name="name"
                    )],
                    target_group_pair_info_list=[codedeploy.CfnDeploymentGroup.TargetGroupPairInfoProperty(
                        prod_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                            listener_arns=["listenerArns"]
                        ),
                        target_groups=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                            name="name"
                        )],
                        test_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                            listener_arns=["listenerArns"]
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3433798b0214903267b0b0c3d8bd53b5bf256f9e32a4864f4aa3e7de53a3e0d6)
                check_type(argname="argument elb_info_list", value=elb_info_list, expected_type=type_hints["elb_info_list"])
                check_type(argname="argument target_group_info_list", value=target_group_info_list, expected_type=type_hints["target_group_info_list"])
                check_type(argname="argument target_group_pair_info_list", value=target_group_pair_info_list, expected_type=type_hints["target_group_pair_info_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if elb_info_list is not None:
                self._values["elb_info_list"] = elb_info_list
            if target_group_info_list is not None:
                self._values["target_group_info_list"] = target_group_info_list
            if target_group_pair_info_list is not None:
                self._values["target_group_pair_info_list"] = target_group_pair_info_list

        @builtins.property
        def elb_info_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.ELBInfoProperty"]]]]:
            '''An array that contains information about the load balancer to use for load balancing in a deployment.

            In Elastic Load Balancing, load balancers are used with Classic Load Balancers.
            .. epigraph::

               Adding more than one load balancer to the array is not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-elbinfolist
            '''
            result = self._values.get("elb_info_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.ELBInfoProperty"]]]], result)

        @builtins.property
        def target_group_info_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TargetGroupInfoProperty"]]]]:
            '''An array that contains information about the target group to use for load balancing in a deployment.

            In Elastic Load Balancing , target groups are used with Application Load Balancers .
            .. epigraph::

               Adding more than one target group to the array is not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgroupinfolist
            '''
            result = self._values.get("target_group_info_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TargetGroupInfoProperty"]]]], result)

        @builtins.property
        def target_group_pair_info_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TargetGroupPairInfoProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo-targetgrouppairinfolist
            '''
            result = self._values.get("target_group_pair_info_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TargetGroupPairInfoProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoadBalancerInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.OnPremisesTagSetListObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"on_premises_tag_group": "onPremisesTagGroup"},
    )
    class OnPremisesTagSetListObjectProperty:
        def __init__(
            self,
            *,
            on_premises_tag_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TagFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``OnPremisesTagSetListObject`` property type specifies lists of on-premises instance tag groups.

            In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

            ``OnPremisesTagSetListObject`` is a property of the `CodeDeploy DeploymentGroup OnPremisesTagSet <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html>`_ property type.

            :param on_premises_tag_group: Information about groups of on-premises instance tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                on_premises_tag_set_list_object_property = codedeploy.CfnDeploymentGroup.OnPremisesTagSetListObjectProperty(
                    on_premises_tag_group=[codedeploy.CfnDeploymentGroup.TagFilterProperty(
                        key="key",
                        type="type",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4011b432f9b5ed3fcdaa688b15c75cc1850efecdc1b1a6c9b90e48052559ec5b)
                check_type(argname="argument on_premises_tag_group", value=on_premises_tag_group, expected_type=type_hints["on_premises_tag_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_premises_tag_group is not None:
                self._values["on_premises_tag_group"] = on_premises_tag_group

        @builtins.property
        def on_premises_tag_group(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TagFilterProperty"]]]]:
            '''Information about groups of on-premises instance tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagsetlistobject.html#cfn-codedeploy-deploymentgroup-onpremisestagsetlistobject-onpremisestaggroup
            '''
            result = self._values.get("on_premises_tag_group")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TagFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnPremisesTagSetListObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.OnPremisesTagSetProperty",
        jsii_struct_bases=[],
        name_mapping={"on_premises_tag_set_list": "onPremisesTagSetList"},
    )
    class OnPremisesTagSetProperty:
        def __init__(
            self,
            *,
            on_premises_tag_set_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.OnPremisesTagSetListObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The ``OnPremisesTagSet`` property type specifies a list containing other lists of on-premises instance tag groups.

            In order for an instance to be included in the deployment group, it must be identified by all the tag groups in the list.

            For more information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see `Tagging Instances for Deployment Groups in AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html>`_ in the *AWS CodeDeploy User Guide* .

            ``OnPremisesTagSet`` is a property of the `DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource.

            :param on_premises_tag_set_list: A list that contains other lists of on-premises instance tag groups. For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list. Duplicates are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                on_premises_tag_set_property = codedeploy.CfnDeploymentGroup.OnPremisesTagSetProperty(
                    on_premises_tag_set_list=[codedeploy.CfnDeploymentGroup.OnPremisesTagSetListObjectProperty(
                        on_premises_tag_group=[codedeploy.CfnDeploymentGroup.TagFilterProperty(
                            key="key",
                            type="type",
                            value="value"
                        )]
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36ece4f2e243605e790c8b3d869b089b200ff22c8a77da7ce3d7477f6504f697)
                check_type(argname="argument on_premises_tag_set_list", value=on_premises_tag_set_list, expected_type=type_hints["on_premises_tag_set_list"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_premises_tag_set_list is not None:
                self._values["on_premises_tag_set_list"] = on_premises_tag_set_list

        @builtins.property
        def on_premises_tag_set_list(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.OnPremisesTagSetListObjectProperty"]]]]:
            '''A list that contains other lists of on-premises instance tag groups.

            For an instance to be included in the deployment group, it must be identified by all of the tag groups in the list.

            Duplicates are not allowed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-onpremisestagset.html#cfn-codedeploy-deploymentgroup-onpremisestagset-onpremisestagsetlist
            '''
            result = self._values.get("on_premises_tag_set_list")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.OnPremisesTagSetListObjectProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OnPremisesTagSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.RevisionLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "git_hub_location": "gitHubLocation",
            "revision_type": "revisionType",
            "s3_location": "s3Location",
        },
    )
    class RevisionLocationProperty:
        def __init__(
            self,
            *,
            git_hub_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.GitHubLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            revision_type: typing.Optional[builtins.str] = None,
            s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''``RevisionLocation`` is a property that defines the location of the CodeDeploy application revision to deploy.

            :param git_hub_location: Information about the location of application artifacts stored in GitHub.
            :param revision_type: The type of application revision:. - S3: An application revision stored in Amazon S3. - GitHub: An application revision stored in GitHub (EC2/On-premises deployments only). - String: A YAML-formatted or JSON-formatted string ( AWS Lambda deployments only). - AppSpecContent: An ``AppSpecContent`` object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
            :param s3_location: Information about the location of a revision stored in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-revisionlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                revision_location_property = codedeploy.CfnDeploymentGroup.RevisionLocationProperty(
                    git_hub_location=codedeploy.CfnDeploymentGroup.GitHubLocationProperty(
                        commit_id="commitId",
                        repository="repository"
                    ),
                    revision_type="revisionType",
                    s3_location=codedeploy.CfnDeploymentGroup.S3LocationProperty(
                        bucket="bucket",
                        key="key",
                
                        # the properties below are optional
                        bundle_type="bundleType",
                        e_tag="eTag",
                        version="version"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f29088b2f9a724cb557a6d1896af99895cac8961456ede05c903a4cb938ff48d)
                check_type(argname="argument git_hub_location", value=git_hub_location, expected_type=type_hints["git_hub_location"])
                check_type(argname="argument revision_type", value=revision_type, expected_type=type_hints["revision_type"])
                check_type(argname="argument s3_location", value=s3_location, expected_type=type_hints["s3_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if git_hub_location is not None:
                self._values["git_hub_location"] = git_hub_location
            if revision_type is not None:
                self._values["revision_type"] = revision_type
            if s3_location is not None:
                self._values["s3_location"] = s3_location

        @builtins.property
        def git_hub_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.GitHubLocationProperty"]]:
            '''Information about the location of application artifacts stored in GitHub.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-revisionlocation.html#cfn-codedeploy-deploymentgroup-revisionlocation-githublocation
            '''
            result = self._values.get("git_hub_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.GitHubLocationProperty"]], result)

        @builtins.property
        def revision_type(self) -> typing.Optional[builtins.str]:
            '''The type of application revision:.

            - S3: An application revision stored in Amazon S3.
            - GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
            - String: A YAML-formatted or JSON-formatted string ( AWS Lambda deployments only).
            - AppSpecContent: An ``AppSpecContent`` object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-revisionlocation.html#cfn-codedeploy-deploymentgroup-revisionlocation-revisiontype
            '''
            result = self._values.get("revision_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.S3LocationProperty"]]:
            '''Information about the location of a revision stored in Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-revisionlocation.html#cfn-codedeploy-deploymentgroup-revisionlocation-s3location
            '''
            result = self._values.get("s3_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.S3LocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RevisionLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "bundle_type": "bundleType",
            "e_tag": "eTag",
            "version": "version",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            bundle_type: typing.Optional[builtins.str] = None,
            e_tag: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``S3Location`` is a property of the `CodeDeploy DeploymentGroup Revision <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision.html>`_ property that specifies the location of an application revision that is stored in Amazon Simple Storage Service ( Amazon S3 ).

            :param bucket: The name of the Amazon S3 bucket where the application revision is stored.
            :param key: The name of the Amazon S3 object that represents the bundled artifacts for the application revision.
            :param bundle_type: The file type of the application revision. Must be one of the following:. - JSON - tar: A tar archive file. - tgz: A compressed tar archive file. - YAML - zip: A zip archive file.
            :param e_tag: The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision. If the ETag is not specified as an input parameter, ETag validation of the object is skipped.
            :param version: A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision. If the version is not specified, the system uses the most recent version by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                s3_location_property = codedeploy.CfnDeploymentGroup.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                
                    # the properties below are optional
                    bundle_type="bundleType",
                    e_tag="eTag",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7c51f97a2e756174dd9b616cbc2cf2e3a30fc7670a54bc88414aabf5142992ec)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument bundle_type", value=bundle_type, expected_type=type_hints["bundle_type"])
                check_type(argname="argument e_tag", value=e_tag, expected_type=type_hints["e_tag"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if bundle_type is not None:
                self._values["bundle_type"] = bundle_type
            if e_tag is not None:
                self._values["e_tag"] = e_tag
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket where the application revision is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-s3location.html#cfn-codedeploy-deploymentgroup-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-s3location.html#cfn-codedeploy-deploymentgroup-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bundle_type(self) -> typing.Optional[builtins.str]:
            '''The file type of the application revision. Must be one of the following:.

            - JSON
            - tar: A tar archive file.
            - tgz: A compressed tar archive file.
            - YAML
            - zip: A zip archive file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-s3location.html#cfn-codedeploy-deploymentgroup-s3location-bundletype
            '''
            result = self._values.get("bundle_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def e_tag(self) -> typing.Optional[builtins.str]:
            '''The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

            If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-s3location.html#cfn-codedeploy-deploymentgroup-s3location-etag
            '''
            result = self._values.get("e_tag")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

            If the version is not specified, the system uses the most recent version by default.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-s3location.html#cfn-codedeploy-deploymentgroup-s3location-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.TagFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "type": "type", "value": "value"},
    )
    class TagFilterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``TagFilter`` is a property type of the `AWS::CodeDeploy::DeploymentGroup <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html>`_ resource that specifies which on-premises instances to associate with the deployment group. To register on-premise instances with AWS CodeDeploy , see `Configure Existing On-Premises Instances by Using AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html>`_ in the *AWS CodeDeploy User Guide* .

            For more information about using tags and tag groups to help manage your Amazon EC2 instances and on-premises instances, see `Tagging Instances for Deployment Groups in AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-tagging.html>`_ in the *AWS CodeDeploy User Guide* .

            :param key: The on-premises instance tag filter key.
            :param type: The on-premises instance tag filter type:. - KEY_ONLY: Key only. - VALUE_ONLY: Value only. - KEY_AND_VALUE: Key and value.
            :param value: The on-premises instance tag filter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                tag_filter_property = codedeploy.CfnDeploymentGroup.TagFilterProperty(
                    key="key",
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63f4128dda3c53a5291d286360b72c038c5228704c806b5dfffed5bf290d6317)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The on-premises instance tag filter key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The on-premises instance tag filter type:.

            - KEY_ONLY: Key only.
            - VALUE_ONLY: Value only.
            - KEY_AND_VALUE: Key and value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The on-premises instance tag filter value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-tagfilter.html#cfn-codedeploy-deploymentgroup-tagfilter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name"},
    )
    class TargetGroupInfoProperty:
        def __init__(self, *, name: typing.Optional[builtins.str] = None) -> None:
            '''The ``TargetGroupInfo`` property type specifies information about a target group in Elastic Load Balancing to use in a deployment.

            Instances are registered as targets in a target group, and traffic is routed to the target group. For more information, see `TargetGroupInfo <https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_TargetGroupInfo.html>`_ in the *AWS CodeDeploy API Reference*

            If you specify the ``TargetGroupInfo`` property, the ``DeploymentStyle.DeploymentOption`` property must be set to ``WITH_TRAFFIC_CONTROL`` for CodeDeploy to route your traffic using the specified target groups.

            ``TargetGroupInfo`` is a property of the `LoadBalancerInfo <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-loadbalancerinfo.html>`_ property type.

            :param name: For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with. For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. No duplicates allowed. .. epigraph:: AWS CloudFormation supports blue/green deployments on AWS Lambda compute platforms only. This value cannot exceed 32 characters, so you should use the ``Name`` property of the target group, or the ``TargetGroupName`` attribute with the ``Fn::GetAtt`` intrinsic function, as shown in the following example. Don't use the group's Amazon Resource Name (ARN) or ``TargetGroupFullName`` attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                target_group_info_property = codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__16465f8a39251aa9907267031575771f643f1897cd1cfea422dfafe3c33e4e92)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''For blue/green deployments, the name of the target group that instances in the original environment are deregistered from, and instances in the replacement environment registered with.

            For in-place deployments, the name of the target group that instances are deregistered from, so they are not serving traffic during a deployment, and then re-registered with after the deployment completes. No duplicates allowed.
            .. epigraph::

               AWS CloudFormation supports blue/green deployments on AWS Lambda compute platforms only.

            This value cannot exceed 32 characters, so you should use the ``Name`` property of the target group, or the ``TargetGroupName`` attribute with the ``Fn::GetAtt`` intrinsic function, as shown in the following example. Don't use the group's Amazon Resource Name (ARN) or ``TargetGroupFullName`` attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgroupinfo.html#cfn-codedeploy-deploymentgroup-targetgroupinfo-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetGroupInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.TargetGroupPairInfoProperty",
        jsii_struct_bases=[],
        name_mapping={
            "prod_traffic_route": "prodTrafficRoute",
            "target_groups": "targetGroups",
            "test_traffic_route": "testTrafficRoute",
        },
    )
    class TargetGroupPairInfoProperty:
        def __init__(
            self,
            *,
            prod_traffic_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TrafficRouteProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            target_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TargetGroupInfoProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            test_traffic_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDeploymentGroup.TrafficRouteProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param prod_traffic_route: 
            :param target_groups: 
            :param test_traffic_route: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                target_group_pair_info_property = codedeploy.CfnDeploymentGroup.TargetGroupPairInfoProperty(
                    prod_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                        listener_arns=["listenerArns"]
                    ),
                    target_groups=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                        name="name"
                    )],
                    test_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                        listener_arns=["listenerArns"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7e5e2e921fcbd8db2d985022ed2557366a9e03a443be17ad0a66dc2940dfe1f1)
                check_type(argname="argument prod_traffic_route", value=prod_traffic_route, expected_type=type_hints["prod_traffic_route"])
                check_type(argname="argument target_groups", value=target_groups, expected_type=type_hints["target_groups"])
                check_type(argname="argument test_traffic_route", value=test_traffic_route, expected_type=type_hints["test_traffic_route"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if prod_traffic_route is not None:
                self._values["prod_traffic_route"] = prod_traffic_route
            if target_groups is not None:
                self._values["target_groups"] = target_groups
            if test_traffic_route is not None:
                self._values["test_traffic_route"] = test_traffic_route

        @builtins.property
        def prod_traffic_route(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TrafficRouteProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html#cfn-codedeploy-deploymentgroup-targetgrouppairinfo-prodtrafficroute
            '''
            result = self._values.get("prod_traffic_route")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TrafficRouteProperty"]], result)

        @builtins.property
        def target_groups(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TargetGroupInfoProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html#cfn-codedeploy-deploymentgroup-targetgrouppairinfo-targetgroups
            '''
            result = self._values.get("target_groups")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TargetGroupInfoProperty"]]]], result)

        @builtins.property
        def test_traffic_route(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TrafficRouteProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-targetgrouppairinfo.html#cfn-codedeploy-deploymentgroup-targetgrouppairinfo-testtrafficroute
            '''
            result = self._values.get("test_traffic_route")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDeploymentGroup.TrafficRouteProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetGroupPairInfoProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.TrafficRouteProperty",
        jsii_struct_bases=[],
        name_mapping={"listener_arns": "listenerArns"},
    )
    class TrafficRouteProperty:
        def __init__(
            self,
            *,
            listener_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param listener_arns: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-trafficroute.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                traffic_route_property = codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                    listener_arns=["listenerArns"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__658bb64cfd11bd3a4440b0f5de1ea0cdd277919eeaddf444d9b6438282bad659)
                check_type(argname="argument listener_arns", value=listener_arns, expected_type=type_hints["listener_arns"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if listener_arns is not None:
                self._values["listener_arns"] = listener_arns

        @builtins.property
        def listener_arns(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-trafficroute.html#cfn-codedeploy-deploymentgroup-trafficroute-listenerarns
            '''
            result = self._values.get("listener_arns")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrafficRouteProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroup.TriggerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trigger_events": "triggerEvents",
            "trigger_name": "triggerName",
            "trigger_target_arn": "triggerTargetArn",
        },
    )
    class TriggerConfigProperty:
        def __init__(
            self,
            *,
            trigger_events: typing.Optional[typing.Sequence[builtins.str]] = None,
            trigger_name: typing.Optional[builtins.str] = None,
            trigger_target_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about notification triggers for the deployment group.

            :param trigger_events: The event type or types that trigger notifications.
            :param trigger_name: The name of the notification trigger.
            :param trigger_target_arn: The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_codedeploy as codedeploy
                
                trigger_config_property = codedeploy.CfnDeploymentGroup.TriggerConfigProperty(
                    trigger_events=["triggerEvents"],
                    trigger_name="triggerName",
                    trigger_target_arn="triggerTargetArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__08bf43d66fb9d8d74aceca78cf370506dcc65400910ba065753222415226e3c5)
                check_type(argname="argument trigger_events", value=trigger_events, expected_type=type_hints["trigger_events"])
                check_type(argname="argument trigger_name", value=trigger_name, expected_type=type_hints["trigger_name"])
                check_type(argname="argument trigger_target_arn", value=trigger_target_arn, expected_type=type_hints["trigger_target_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if trigger_events is not None:
                self._values["trigger_events"] = trigger_events
            if trigger_name is not None:
                self._values["trigger_name"] = trigger_name
            if trigger_target_arn is not None:
                self._values["trigger_target_arn"] = trigger_target_arn

        @builtins.property
        def trigger_events(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The event type or types that trigger notifications.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggerevents
            '''
            result = self._values.get("trigger_events")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def trigger_name(self) -> typing.Optional[builtins.str]:
            '''The name of the notification trigger.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggername
            '''
            result = self._values.get("trigger_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def trigger_target_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic through which notifications about deployment or instance events are sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-triggerconfig.html#cfn-codedeploy-deploymentgroup-triggerconfig-triggertargetarn
            '''
            result = self._values.get("trigger_target_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.CfnDeploymentGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_name": "applicationName",
        "service_role_arn": "serviceRoleArn",
        "alarm_configuration": "alarmConfiguration",
        "auto_rollback_configuration": "autoRollbackConfiguration",
        "auto_scaling_groups": "autoScalingGroups",
        "blue_green_deployment_configuration": "blueGreenDeploymentConfiguration",
        "deployment": "deployment",
        "deployment_config_name": "deploymentConfigName",
        "deployment_group_name": "deploymentGroupName",
        "deployment_style": "deploymentStyle",
        "ec2_tag_filters": "ec2TagFilters",
        "ec2_tag_set": "ec2TagSet",
        "ecs_services": "ecsServices",
        "load_balancer_info": "loadBalancerInfo",
        "on_premises_instance_tag_filters": "onPremisesInstanceTagFilters",
        "on_premises_tag_set": "onPremisesTagSet",
        "outdated_instances_strategy": "outdatedInstancesStrategy",
        "tags": "tags",
        "trigger_configurations": "triggerConfigurations",
    },
)
class CfnDeploymentGroupProps:
    def __init__(
        self,
        *,
        application_name: builtins.str,
        service_role_arn: builtins.str,
        alarm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AlarmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_rollback_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AutoRollbackConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        auto_scaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        blue_green_deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        deployment_style: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentStyleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ec2_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ecs_services: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.ECSServiceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        load_balancer_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.LoadBalancerInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        on_premises_instance_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        on_premises_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.OnPremisesTagSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        outdated_instances_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trigger_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeploymentGroup``.

        :param application_name: The name of an existing CodeDeploy application to associate this deployment group with.
        :param service_role_arn: A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf. For more information, see `Create a Service Role for AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`_ in the *AWS CodeDeploy User Guide* . .. epigraph:: In some cases, you might need to add a dependency on the service role's policy. For more information, see IAM role policy in `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .
        :param alarm_configuration: Information about the Amazon CloudWatch alarms that are associated with the deployment group.
        :param auto_rollback_configuration: Information about the automatic rollback configuration that is associated with the deployment group. If you specify this property, don't specify the ``Deployment`` property.
        :param auto_scaling_groups: A list of associated Auto Scaling groups that CodeDeploy automatically deploys revisions to when new instances are created. Duplicates are not allowed.
        :param blue_green_deployment_configuration: Information about blue/green deployment options for a deployment group.
        :param deployment: The application revision to deploy to this deployment group. If you specify this property, your target application revision is deployed as soon as the provisioning process is complete. If you specify this property, don't specify the ``AutoRollbackConfiguration`` property.
        :param deployment_config_name: A deployment configuration name or a predefined configuration name. With predefined configurations, you can deploy application revisions to one instance at a time ( ``CodeDeployDefault.OneAtATime`` ), half of the instances at a time ( ``CodeDeployDefault.HalfAtATime`` ), or all the instances at once ( ``CodeDeployDefault.AllAtOnce`` ). For more information and valid values, see `Working with Deployment Configurations <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html>`_ in the *AWS CodeDeploy User Guide* .
        :param deployment_group_name: A name for the deployment group. If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment group name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ . .. epigraph:: If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.
        :param deployment_style: Attributes that determine the type of deployment to run and whether to route deployment traffic behind a load balancer. If you specify this property with a blue/green deployment type, don't specify the ``AutoScalingGroups`` , ``LoadBalancerInfo`` , or ``Deployment`` properties. .. epigraph:: For blue/green deployments, AWS CloudFormation supports deployments on Lambda compute platforms only. You can perform Amazon ECS blue/green deployments using ``AWS::CodeDeploy::BlueGreen`` hook. See `Perform Amazon ECS blue/green deployments through CodeDeploy using AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html>`_ for more information.
        :param ec2_tag_filters: The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group. CodeDeploy includes all Amazon EC2 instances identified by any of the tags you specify in this deployment group. Duplicates are not allowed. You can specify ``EC2TagFilters`` or ``Ec2TagSet`` , but not both.
        :param ec2_tag_set: Information about groups of tags applied to Amazon EC2 instances. The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same call as ``ec2TagFilter`` .
        :param ecs_services: The target Amazon ECS services in the deployment group. This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format ``<clustername>:<servicename>`` .
        :param load_balancer_info: Information about the load balancer to use in a deployment. For more information, see `Integrating CodeDeploy with Elastic Load Balancing <https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html>`_ in the *AWS CodeDeploy User Guide* .
        :param on_premises_instance_tag_filters: The on-premises instance tags already applied to on-premises instances that you want to include in the deployment group. CodeDeploy includes all on-premises instances identified by any of the tags you specify in this deployment group. To register on-premises instances with CodeDeploy , see `Working with On-Premises Instances for CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html>`_ in the *AWS CodeDeploy User Guide* . Duplicates are not allowed. You can specify ``OnPremisesInstanceTagFilters`` or ``OnPremisesInstanceTagSet`` , but not both.
        :param on_premises_tag_set: Information about groups of tags applied to on-premises instances. The deployment group includes only on-premises instances identified by all the tag groups. You can specify ``OnPremisesInstanceTagFilters`` or ``OnPremisesInstanceTagSet`` , but not both.
        :param outdated_instances_strategy: 
        :param tags: 
        :param trigger_configurations: Information about triggers associated with the deployment group. Duplicates are not allowed

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            cfn_deployment_group_props = codedeploy.CfnDeploymentGroupProps(
                application_name="applicationName",
                service_role_arn="serviceRoleArn",
            
                # the properties below are optional
                alarm_configuration=codedeploy.CfnDeploymentGroup.AlarmConfigurationProperty(
                    alarms=[codedeploy.CfnDeploymentGroup.AlarmProperty(
                        name="name"
                    )],
                    enabled=False,
                    ignore_poll_alarm_failure=False
                ),
                auto_rollback_configuration=codedeploy.CfnDeploymentGroup.AutoRollbackConfigurationProperty(
                    enabled=False,
                    events=["events"]
                ),
                auto_scaling_groups=["autoScalingGroups"],
                blue_green_deployment_configuration=codedeploy.CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty(
                    deployment_ready_option=codedeploy.CfnDeploymentGroup.DeploymentReadyOptionProperty(
                        action_on_timeout="actionOnTimeout",
                        wait_time_in_minutes=123
                    ),
                    green_fleet_provisioning_option=codedeploy.CfnDeploymentGroup.GreenFleetProvisioningOptionProperty(
                        action="action"
                    ),
                    terminate_blue_instances_on_deployment_success=codedeploy.CfnDeploymentGroup.BlueInstanceTerminationOptionProperty(
                        action="action",
                        termination_wait_time_in_minutes=123
                    )
                ),
                deployment=codedeploy.CfnDeploymentGroup.DeploymentProperty(
                    revision=codedeploy.CfnDeploymentGroup.RevisionLocationProperty(
                        git_hub_location=codedeploy.CfnDeploymentGroup.GitHubLocationProperty(
                            commit_id="commitId",
                            repository="repository"
                        ),
                        revision_type="revisionType",
                        s3_location=codedeploy.CfnDeploymentGroup.S3LocationProperty(
                            bucket="bucket",
                            key="key",
            
                            # the properties below are optional
                            bundle_type="bundleType",
                            e_tag="eTag",
                            version="version"
                        )
                    ),
            
                    # the properties below are optional
                    description="description",
                    ignore_application_stop_failures=False
                ),
                deployment_config_name="deploymentConfigName",
                deployment_group_name="deploymentGroupName",
                deployment_style=codedeploy.CfnDeploymentGroup.DeploymentStyleProperty(
                    deployment_option="deploymentOption",
                    deployment_type="deploymentType"
                ),
                ec2_tag_filters=[codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                    key="key",
                    type="type",
                    value="value"
                )],
                ec2_tag_set=codedeploy.CfnDeploymentGroup.EC2TagSetProperty(
                    ec2_tag_set_list=[codedeploy.CfnDeploymentGroup.EC2TagSetListObjectProperty(
                        ec2_tag_group=[codedeploy.CfnDeploymentGroup.EC2TagFilterProperty(
                            key="key",
                            type="type",
                            value="value"
                        )]
                    )]
                ),
                ecs_services=[codedeploy.CfnDeploymentGroup.ECSServiceProperty(
                    cluster_name="clusterName",
                    service_name="serviceName"
                )],
                load_balancer_info=codedeploy.CfnDeploymentGroup.LoadBalancerInfoProperty(
                    elb_info_list=[codedeploy.CfnDeploymentGroup.ELBInfoProperty(
                        name="name"
                    )],
                    target_group_info_list=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                        name="name"
                    )],
                    target_group_pair_info_list=[codedeploy.CfnDeploymentGroup.TargetGroupPairInfoProperty(
                        prod_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                            listener_arns=["listenerArns"]
                        ),
                        target_groups=[codedeploy.CfnDeploymentGroup.TargetGroupInfoProperty(
                            name="name"
                        )],
                        test_traffic_route=codedeploy.CfnDeploymentGroup.TrafficRouteProperty(
                            listener_arns=["listenerArns"]
                        )
                    )]
                ),
                on_premises_instance_tag_filters=[codedeploy.CfnDeploymentGroup.TagFilterProperty(
                    key="key",
                    type="type",
                    value="value"
                )],
                on_premises_tag_set=codedeploy.CfnDeploymentGroup.OnPremisesTagSetProperty(
                    on_premises_tag_set_list=[codedeploy.CfnDeploymentGroup.OnPremisesTagSetListObjectProperty(
                        on_premises_tag_group=[codedeploy.CfnDeploymentGroup.TagFilterProperty(
                            key="key",
                            type="type",
                            value="value"
                        )]
                    )]
                ),
                outdated_instances_strategy="outdatedInstancesStrategy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trigger_configurations=[codedeploy.CfnDeploymentGroup.TriggerConfigProperty(
                    trigger_events=["triggerEvents"],
                    trigger_name="triggerName",
                    trigger_target_arn="triggerTargetArn"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6511a1a48658d7f16b747353194a86e2a15daf184e4957a0f2924cfee66716bc)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
            check_type(argname="argument service_role_arn", value=service_role_arn, expected_type=type_hints["service_role_arn"])
            check_type(argname="argument alarm_configuration", value=alarm_configuration, expected_type=type_hints["alarm_configuration"])
            check_type(argname="argument auto_rollback_configuration", value=auto_rollback_configuration, expected_type=type_hints["auto_rollback_configuration"])
            check_type(argname="argument auto_scaling_groups", value=auto_scaling_groups, expected_type=type_hints["auto_scaling_groups"])
            check_type(argname="argument blue_green_deployment_configuration", value=blue_green_deployment_configuration, expected_type=type_hints["blue_green_deployment_configuration"])
            check_type(argname="argument deployment", value=deployment, expected_type=type_hints["deployment"])
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument deployment_style", value=deployment_style, expected_type=type_hints["deployment_style"])
            check_type(argname="argument ec2_tag_filters", value=ec2_tag_filters, expected_type=type_hints["ec2_tag_filters"])
            check_type(argname="argument ec2_tag_set", value=ec2_tag_set, expected_type=type_hints["ec2_tag_set"])
            check_type(argname="argument ecs_services", value=ecs_services, expected_type=type_hints["ecs_services"])
            check_type(argname="argument load_balancer_info", value=load_balancer_info, expected_type=type_hints["load_balancer_info"])
            check_type(argname="argument on_premises_instance_tag_filters", value=on_premises_instance_tag_filters, expected_type=type_hints["on_premises_instance_tag_filters"])
            check_type(argname="argument on_premises_tag_set", value=on_premises_tag_set, expected_type=type_hints["on_premises_tag_set"])
            check_type(argname="argument outdated_instances_strategy", value=outdated_instances_strategy, expected_type=type_hints["outdated_instances_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trigger_configurations", value=trigger_configurations, expected_type=type_hints["trigger_configurations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_name": application_name,
            "service_role_arn": service_role_arn,
        }
        if alarm_configuration is not None:
            self._values["alarm_configuration"] = alarm_configuration
        if auto_rollback_configuration is not None:
            self._values["auto_rollback_configuration"] = auto_rollback_configuration
        if auto_scaling_groups is not None:
            self._values["auto_scaling_groups"] = auto_scaling_groups
        if blue_green_deployment_configuration is not None:
            self._values["blue_green_deployment_configuration"] = blue_green_deployment_configuration
        if deployment is not None:
            self._values["deployment"] = deployment
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if deployment_group_name is not None:
            self._values["deployment_group_name"] = deployment_group_name
        if deployment_style is not None:
            self._values["deployment_style"] = deployment_style
        if ec2_tag_filters is not None:
            self._values["ec2_tag_filters"] = ec2_tag_filters
        if ec2_tag_set is not None:
            self._values["ec2_tag_set"] = ec2_tag_set
        if ecs_services is not None:
            self._values["ecs_services"] = ecs_services
        if load_balancer_info is not None:
            self._values["load_balancer_info"] = load_balancer_info
        if on_premises_instance_tag_filters is not None:
            self._values["on_premises_instance_tag_filters"] = on_premises_instance_tag_filters
        if on_premises_tag_set is not None:
            self._values["on_premises_tag_set"] = on_premises_tag_set
        if outdated_instances_strategy is not None:
            self._values["outdated_instances_strategy"] = outdated_instances_strategy
        if tags is not None:
            self._values["tags"] = tags
        if trigger_configurations is not None:
            self._values["trigger_configurations"] = trigger_configurations

    @builtins.property
    def application_name(self) -> builtins.str:
        '''The name of an existing CodeDeploy application to associate this deployment group with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-applicationname
        '''
        result = self._values.get("application_name")
        assert result is not None, "Required property 'application_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_role_arn(self) -> builtins.str:
        '''A service role Amazon Resource Name (ARN) that grants CodeDeploy permission to make calls to AWS services on your behalf.

        For more information, see `Create a Service Role for AWS CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-create-service-role.html>`_ in the *AWS CodeDeploy User Guide* .
        .. epigraph::

           In some cases, you might need to add a dependency on the service role's policy. For more information, see IAM role policy in `DependsOn Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-servicerolearn
        '''
        result = self._values.get("service_role_arn")
        assert result is not None, "Required property 'service_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alarm_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.AlarmConfigurationProperty]]:
        '''Information about the Amazon CloudWatch alarms that are associated with the deployment group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-alarmconfiguration
        '''
        result = self._values.get("alarm_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.AlarmConfigurationProperty]], result)

    @builtins.property
    def auto_rollback_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.AutoRollbackConfigurationProperty]]:
        '''Information about the automatic rollback configuration that is associated with the deployment group.

        If you specify this property, don't specify the ``Deployment`` property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autorollbackconfiguration
        '''
        result = self._values.get("auto_rollback_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.AutoRollbackConfigurationProperty]], result)

    @builtins.property
    def auto_scaling_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of associated Auto Scaling groups that CodeDeploy automatically deploys revisions to when new instances are created.

        Duplicates are not allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-autoscalinggroups
        '''
        result = self._values.get("auto_scaling_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def blue_green_deployment_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty]]:
        '''Information about blue/green deployment options for a deployment group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-bluegreendeploymentconfiguration
        '''
        result = self._values.get("blue_green_deployment_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty]], result)

    @builtins.property
    def deployment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.DeploymentProperty]]:
        '''The application revision to deploy to this deployment group.

        If you specify this property, your target application revision is deployed as soon as the provisioning process is complete. If you specify this property, don't specify the ``AutoRollbackConfiguration`` property.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deployment
        '''
        result = self._values.get("deployment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.DeploymentProperty]], result)

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''A deployment configuration name or a predefined configuration name.

        With predefined configurations, you can deploy application revisions to one instance at a time ( ``CodeDeployDefault.OneAtATime`` ), half of the instances at a time ( ``CodeDeployDefault.HalfAtATime`` ), or all the instances at once ( ``CodeDeployDefault.AllAtOnce`` ). For more information and valid values, see `Working with Deployment Configurations <https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html>`_ in the *AWS CodeDeploy User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentconfigname
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''A name for the deployment group.

        If you don't specify a name, AWS CloudFormation generates a unique physical ID and uses that ID for the deployment group name. For more information, see `Name Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-name.html>`_ .
        .. epigraph::

           If you specify a name, you cannot perform updates that require replacement of this resource. You can perform updates that require no or some interruption. If you must replace the resource, specify a new name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentgroupname
        '''
        result = self._values.get("deployment_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def deployment_style(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.DeploymentStyleProperty]]:
        '''Attributes that determine the type of deployment to run and whether to route deployment traffic behind a load balancer.

        If you specify this property with a blue/green deployment type, don't specify the ``AutoScalingGroups`` , ``LoadBalancerInfo`` , or ``Deployment`` properties.
        .. epigraph::

           For blue/green deployments, AWS CloudFormation supports deployments on Lambda compute platforms only. You can perform Amazon ECS blue/green deployments using ``AWS::CodeDeploy::BlueGreen`` hook. See `Perform Amazon ECS blue/green deployments through CodeDeploy using AWS CloudFormation <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html>`_ for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-deploymentstyle
        '''
        result = self._values.get("deployment_style")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.DeploymentStyleProperty]], result)

    @builtins.property
    def ec2_tag_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.EC2TagFilterProperty]]]]:
        '''The Amazon EC2 tags that are already applied to Amazon EC2 instances that you want to include in the deployment group.

        CodeDeploy includes all Amazon EC2 instances identified by any of the tags you specify in this deployment group. Duplicates are not allowed.

        You can specify ``EC2TagFilters`` or ``Ec2TagSet`` , but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagfilters
        '''
        result = self._values.get("ec2_tag_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.EC2TagFilterProperty]]]], result)

    @builtins.property
    def ec2_tag_set(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.EC2TagSetProperty]]:
        '''Information about groups of tags applied to Amazon EC2 instances.

        The deployment group includes only Amazon EC2 instances identified by all the tag groups. Cannot be used in the same call as ``ec2TagFilter`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ec2tagset
        '''
        result = self._values.get("ec2_tag_set")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.EC2TagSetProperty]], result)

    @builtins.property
    def ecs_services(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.ECSServiceProperty]]]]:
        '''The target Amazon ECS services in the deployment group.

        This applies only to deployment groups that use the Amazon ECS compute platform. A target Amazon ECS service is specified as an Amazon ECS cluster and service name pair using the format ``<clustername>:<servicename>`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-ecsservices
        '''
        result = self._values.get("ecs_services")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.ECSServiceProperty]]]], result)

    @builtins.property
    def load_balancer_info(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.LoadBalancerInfoProperty]]:
        '''Information about the load balancer to use in a deployment.

        For more information, see `Integrating CodeDeploy with Elastic Load Balancing <https://docs.aws.amazon.com/codedeploy/latest/userguide/integrations-aws-elastic-load-balancing.html>`_ in the *AWS CodeDeploy User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-loadbalancerinfo
        '''
        result = self._values.get("load_balancer_info")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.LoadBalancerInfoProperty]], result)

    @builtins.property
    def on_premises_instance_tag_filters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.TagFilterProperty]]]]:
        '''The on-premises instance tags already applied to on-premises instances that you want to include in the deployment group.

        CodeDeploy includes all on-premises instances identified by any of the tags you specify in this deployment group. To register on-premises instances with CodeDeploy , see `Working with On-Premises Instances for CodeDeploy <https://docs.aws.amazon.com/codedeploy/latest/userguide/instances-on-premises.html>`_ in the *AWS CodeDeploy User Guide* . Duplicates are not allowed.

        You can specify ``OnPremisesInstanceTagFilters`` or ``OnPremisesInstanceTagSet`` , but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisesinstancetagfilters
        '''
        result = self._values.get("on_premises_instance_tag_filters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.TagFilterProperty]]]], result)

    @builtins.property
    def on_premises_tag_set(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.OnPremisesTagSetProperty]]:
        '''Information about groups of tags applied to on-premises instances.

        The deployment group includes only on-premises instances identified by all the tag groups.

        You can specify ``OnPremisesInstanceTagFilters`` or ``OnPremisesInstanceTagSet`` , but not both.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-onpremisestagset
        '''
        result = self._values.get("on_premises_tag_set")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.OnPremisesTagSetProperty]], result)

    @builtins.property
    def outdated_instances_strategy(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-outdatedinstancesstrategy
        '''
        result = self._values.get("outdated_instances_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trigger_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.TriggerConfigProperty]]]]:
        '''Information about triggers associated with the deployment group.

        Duplicates are not allowed

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html#cfn-codedeploy-deploymentgroup-triggerconfigurations
        '''
        result = self._values.get("trigger_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.TriggerConfigProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codedeploy.ComputePlatform")
class ComputePlatform(enum.Enum):
    '''The compute platform of a deployment configuration.'''

    SERVER = "SERVER"
    '''The deployment will target EC2 instances or on-premise servers.'''
    LAMBDA = "LAMBDA"
    '''The deployment will target a Lambda function.'''
    ECS = "ECS"
    '''The deployment will target an ECS server.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.CustomLambdaDeploymentConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "interval": "interval",
        "percentage": "percentage",
        "type": "type",
        "deployment_config_name": "deploymentConfigName",
    },
)
class CustomLambdaDeploymentConfigProps:
    def __init__(
        self,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
        type: "CustomLambdaDeploymentConfigType",
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(deprecated) Properties of a reference to a CodeDeploy Lambda Deployment Configuration.

        :param interval: (deprecated) The interval, in number of minutes: - For LINEAR, how frequently additional traffic is shifted - For CANARY, how long to shift traffic before the full deployment.
        :param percentage: (deprecated) The integer percentage of traffic to shift: - For LINEAR, the percentage to shift every interval - For CANARY, the percentage to shift until the interval passes, before the full deployment.
        :param type: (deprecated) The type of deployment config, either CANARY or LINEAR.
        :param deployment_config_name: (deprecated) The verbatim name of the deployment config. Must be unique per account/region. Other parameters cannot be updated if this name is provided. Default: - automatically generated name

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_codedeploy as codedeploy
            
            custom_lambda_deployment_config_props = codedeploy.CustomLambdaDeploymentConfigProps(
                interval=cdk.Duration.minutes(30),
                percentage=123,
                type=codedeploy.CustomLambdaDeploymentConfigType.CANARY,
            
                # the properties below are optional
                deployment_config_name="deploymentConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f8c53864749c97e11693362fedad7242c31fc477d04c6e3dede64774251fad3)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "percentage": percentage,
            "type": type,
        }
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name

    @builtins.property
    def interval(self) -> _Duration_4839e8c3:
        '''(deprecated) The interval, in number of minutes: - For LINEAR, how frequently additional traffic is shifted - For CANARY, how long to shift traffic before the full deployment.

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''(deprecated) The integer percentage of traffic to shift: - For LINEAR, the percentage to shift every interval - For CANARY, the percentage to shift until the interval passes, before the full deployment.

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        '''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def type(self) -> "CustomLambdaDeploymentConfigType":
        '''(deprecated) The type of deployment config, either CANARY or LINEAR.

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast("CustomLambdaDeploymentConfigType", result)

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The verbatim name of the deployment config.

        Must be unique per account/region.
        Other parameters cannot be updated if this name is provided.

        :default: - automatically generated name

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CustomLambdaDeploymentConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_codedeploy.CustomLambdaDeploymentConfigType")
class CustomLambdaDeploymentConfigType(enum.Enum):
    '''(deprecated) Lambda Deployment config type.

    :deprecated: Use ``LambdaDeploymentConfig``

    :stability: deprecated
    '''

    CANARY = "CANARY"
    '''(deprecated) Canary deployment type.

    :deprecated: Use ``LambdaDeploymentConfig``

    :stability: deprecated
    '''
    LINEAR = "LINEAR"
    '''(deprecated) Linear deployment type.

    :deprecated: Use ``LambdaDeploymentConfig``

    :stability: deprecated
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName"},
)
class EcsApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for ``EcsApplication``.

        :param application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used

        :exampleMetadata: infused

        Example::

            application = codedeploy.EcsApplication(self, "CodeDeployApplication",
                application_name="MyApplication"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31617a0bd5a72eae80bdaf60a12a3c49a0948473616c9a8e908f3d9bd671d2f5)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the CodeDeploy Application.

        :default: an auto-generated name will be used
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsBlueGreenDeploymentConfig",
    jsii_struct_bases=[],
    name_mapping={
        "blue_target_group": "blueTargetGroup",
        "green_target_group": "greenTargetGroup",
        "listener": "listener",
        "deployment_approval_wait_time": "deploymentApprovalWaitTime",
        "termination_wait_time": "terminationWaitTime",
        "test_listener": "testListener",
    },
)
class EcsBlueGreenDeploymentConfig:
    def __init__(
        self,
        *,
        blue_target_group: _ITargetGroup_83c6f8c4,
        green_target_group: _ITargetGroup_83c6f8c4,
        listener: _IListener_7f84e41f,
        deployment_approval_wait_time: typing.Optional[_Duration_4839e8c3] = None,
        termination_wait_time: typing.Optional[_Duration_4839e8c3] = None,
        test_listener: typing.Optional[_IListener_7f84e41f] = None,
    ) -> None:
        '''Specify how the deployment behaves and how traffic is routed to the ECS service during a blue-green ECS deployment.

        :param blue_target_group: The target group that will be associated with the 'blue' ECS task set during a blue-green deployment.
        :param green_target_group: The target group that will be associated with the 'green' ECS task set during a blue-green deployment.
        :param listener: The load balancer listener used to serve production traffic and to shift production traffic from the 'blue' ECS task set to the 'green' ECS task set during a blue-green deployment.
        :param deployment_approval_wait_time: Specify how long CodeDeploy waits for approval to continue a blue-green deployment before it stops the deployment. After provisioning the 'green' ECS task set and re-routing test traffic, CodeDeploy can wait for approval before continuing the deployment and re-routing production traffic. During this wait time, validation such as manual testing or running integration tests can occur using the test traffic port, prior to exposing the new 'green' task set to production traffic. To approve the deployment, validation steps use the CodeDeploy [ContinueDeployment API(https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html). If the ContinueDeployment API is not called within the wait time period, CodeDeploy will stop the deployment. By default, CodeDeploy will not wait for deployment approval. After re-routing test traffic to the 'green' ECS task set and running any 'AfterAllowTestTraffic' and 'BeforeAllowTraffic' lifecycle hooks, the deployment will immediately re-route production traffic to the 'green' ECS task set. Default: 0
        :param termination_wait_time: Specify how long CodeDeploy waits before it terminates the original 'blue' ECS task set when a blue-green deployment is complete. During this wait time, CodeDeploy will continue to monitor any CloudWatch alarms specified for the deployment group, and the deployment group can be configured to automatically roll back if those alarms fire. Once CodeDeploy begins to terminate the 'blue' ECS task set, the deployment can no longer be rolled back, manually or automatically. By default, the deployment will immediately terminate the 'blue' ECS task set after production traffic is successfully routed to the 'green' ECS task set. Default: 0
        :param test_listener: The load balancer listener used to route test traffic to the 'green' ECS task set during a blue-green deployment. During a blue-green deployment, validation can occur after test traffic has been re-routed and before production traffic has been re-routed to the 'green' ECS task set. You can specify one or more Lambda funtions in the deployment's AppSpec file that run during the AfterAllowTestTraffic hook. The functions can run validation tests. If a validation test fails, a deployment rollback is triggered. If the validation tests succeed, the next hook in the deployment lifecycle, BeforeAllowTraffic, is triggered. If a test listener is not specified, the deployment will proceed to routing the production listener to the 'green' ECS task set and will skip the AfterAllowTestTraffic hook. Default: No test listener will be added

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-appspec-file-structure-hooks.html#appspec-hooks-ecs
        :exampleMetadata: infused

        Example::

            # my_application: codedeploy.EcsApplication
            # cluster: ecs.Cluster
            # task_definition: ecs.FargateTaskDefinition
            # blue_target_group: elbv2.ITargetGroup
            # green_target_group: elbv2.ITargetGroup
            # listener: elbv2.IApplicationListener
            
            
            service = ecs.FargateService(self, "Service",
                cluster=cluster,
                task_definition=task_definition,
                deployment_controller=ecs.DeploymentController(
                    type=ecs.DeploymentControllerType.CODE_DEPLOY
                )
            )
            
            codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
                service=service,
                blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
                    blue_target_group=blue_target_group,
                    green_target_group=green_target_group,
                    listener=listener
                ),
                deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b251dc2bb3166b5b08fc4a016e350d50231d6a3f0a8566638996a295262e0269)
            check_type(argname="argument blue_target_group", value=blue_target_group, expected_type=type_hints["blue_target_group"])
            check_type(argname="argument green_target_group", value=green_target_group, expected_type=type_hints["green_target_group"])
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
            check_type(argname="argument deployment_approval_wait_time", value=deployment_approval_wait_time, expected_type=type_hints["deployment_approval_wait_time"])
            check_type(argname="argument termination_wait_time", value=termination_wait_time, expected_type=type_hints["termination_wait_time"])
            check_type(argname="argument test_listener", value=test_listener, expected_type=type_hints["test_listener"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "blue_target_group": blue_target_group,
            "green_target_group": green_target_group,
            "listener": listener,
        }
        if deployment_approval_wait_time is not None:
            self._values["deployment_approval_wait_time"] = deployment_approval_wait_time
        if termination_wait_time is not None:
            self._values["termination_wait_time"] = termination_wait_time
        if test_listener is not None:
            self._values["test_listener"] = test_listener

    @builtins.property
    def blue_target_group(self) -> _ITargetGroup_83c6f8c4:
        '''The target group that will be associated with the 'blue' ECS task set during a blue-green deployment.'''
        result = self._values.get("blue_target_group")
        assert result is not None, "Required property 'blue_target_group' is missing"
        return typing.cast(_ITargetGroup_83c6f8c4, result)

    @builtins.property
    def green_target_group(self) -> _ITargetGroup_83c6f8c4:
        '''The target group that will be associated with the 'green' ECS task set during a blue-green deployment.'''
        result = self._values.get("green_target_group")
        assert result is not None, "Required property 'green_target_group' is missing"
        return typing.cast(_ITargetGroup_83c6f8c4, result)

    @builtins.property
    def listener(self) -> _IListener_7f84e41f:
        '''The load balancer listener used to serve production traffic and to shift production traffic from the 'blue' ECS task set to the 'green' ECS task set during a blue-green deployment.'''
        result = self._values.get("listener")
        assert result is not None, "Required property 'listener' is missing"
        return typing.cast(_IListener_7f84e41f, result)

    @builtins.property
    def deployment_approval_wait_time(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specify how long CodeDeploy waits for approval to continue a blue-green deployment before it stops the deployment.

        After provisioning the 'green' ECS task set and re-routing test traffic, CodeDeploy can wait for approval before
        continuing the deployment and re-routing production traffic.  During this wait time, validation such as manual
        testing or running integration tests can occur using the test traffic port, prior to exposing the new 'green' task
        set to production traffic.  To approve the deployment, validation steps use the CodeDeploy
        [ContinueDeployment API(https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_ContinueDeployment.html).
        If the ContinueDeployment API is not called within the wait time period, CodeDeploy will stop the deployment.

        By default, CodeDeploy will not wait for deployment approval.  After re-routing test traffic to the 'green' ECS task set
        and running any 'AfterAllowTestTraffic' and 'BeforeAllowTraffic' lifecycle hooks, the deployment will immediately
        re-route production traffic to the 'green' ECS task set.

        :default: 0
        '''
        result = self._values.get("deployment_approval_wait_time")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def termination_wait_time(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specify how long CodeDeploy waits before it terminates the original 'blue' ECS task set when a blue-green deployment is complete.

        During this wait time, CodeDeploy will continue to monitor any CloudWatch alarms specified for the deployment group,
        and the deployment group can be configured to automatically roll back if those alarms fire.  Once CodeDeploy begins to
        terminate the 'blue' ECS task set, the deployment can no longer be rolled back, manually or automatically.

        By default, the deployment will immediately terminate the 'blue' ECS task set after production traffic is successfully
        routed to the 'green' ECS task set.

        :default: 0
        '''
        result = self._values.get("termination_wait_time")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def test_listener(self) -> typing.Optional[_IListener_7f84e41f]:
        '''The load balancer listener used to route test traffic to the 'green' ECS task set during a blue-green deployment.

        During a blue-green deployment, validation can occur after test traffic has been re-routed and before production
        traffic has been re-routed to the 'green' ECS task set.  You can specify one or more Lambda funtions in the
        deployment's AppSpec file that run during the AfterAllowTestTraffic hook. The functions can run validation tests.
        If a validation test fails, a deployment rollback is triggered. If the validation tests succeed, the next hook in
        the deployment lifecycle, BeforeAllowTraffic, is triggered.

        If a test listener is not specified, the deployment will proceed to routing the production listener to the 'green' ECS task set
        and will skip the AfterAllowTestTraffic hook.

        :default: No test listener will be added
        '''
        result = self._values.get("test_listener")
        return typing.cast(typing.Optional[_IListener_7f84e41f], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsBlueGreenDeploymentConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsDeploymentConfigProps",
    jsii_struct_bases=[BaseDeploymentConfigOptions],
    name_mapping={
        "deployment_config_name": "deploymentConfigName",
        "traffic_routing": "trafficRouting",
    },
)
class EcsDeploymentConfigProps(BaseDeploymentConfigOptions):
    def __init__(
        self,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
        traffic_routing: typing.Optional["TrafficRouting"] = None,
    ) -> None:
        '''Construction properties of ``EcsDeploymentConfig``.

        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        :param traffic_routing: The configuration that specifies how traffic is shifted from the 'blue' target group to the 'green' target group during a deployment. Default: AllAtOnce

        :exampleMetadata: infused

        Example::

            codedeploy.EcsDeploymentConfig(self, "CustomConfig",
                traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                    interval=Duration.minutes(15),
                    percentage=5
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82f77eb6fc251ed7746cecc68aaaaf5706c1f2831b79812175c6abd5ba12b754)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument traffic_routing", value=traffic_routing, expected_type=type_hints["traffic_routing"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if traffic_routing is not None:
            self._values["traffic_routing"] = traffic_routing

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the Deployment Configuration.

        :default: - automatically generated name
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_routing(self) -> typing.Optional["TrafficRouting"]:
        '''The configuration that specifies how traffic is shifted from the 'blue' target group to the 'green' target group during a deployment.

        :default: AllAtOnce
        '''
        result = self._values.get("traffic_routing")
        return typing.cast(typing.Optional["TrafficRouting"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsDeploymentConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsDeploymentGroupAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "application": "application",
        "deployment_group_name": "deploymentGroupName",
        "deployment_config": "deploymentConfig",
    },
)
class EcsDeploymentGroupAttributes:
    def __init__(
        self,
        *,
        application: "IEcsApplication",
        deployment_group_name: builtins.str,
        deployment_config: typing.Optional["IEcsDeploymentConfig"] = None,
    ) -> None:
        '''Properties of a reference to a CodeDeploy ECS Deployment Group.

        :param application: The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy ECS Deployment Group that we are referencing.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: EcsDeploymentConfig.ALL_AT_ONCE

        :see: EcsDeploymentGroup#fromEcsDeploymentGroupAttributes
        :exampleMetadata: infused

        Example::

            # application: codedeploy.EcsApplication
            
            deployment_group = codedeploy.EcsDeploymentGroup.from_ecs_deployment_group_attributes(self, "ExistingCodeDeployDeploymentGroup",
                application=application,
                deployment_group_name="MyExistingDeploymentGroup"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__171917799e985d16bcafd7fcbcf48ad64ae8bcb175f7e2b8f9fe1f74316e63df)
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
            "deployment_group_name": deployment_group_name,
        }
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config

    @builtins.property
    def application(self) -> "IEcsApplication":
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast("IEcsApplication", result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''The physical, human-readable name of the CodeDeploy ECS Deployment Group that we are referencing.'''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_config(self) -> typing.Optional["IEcsDeploymentConfig"]:
        '''The Deployment Configuration this Deployment Group uses.

        :default: EcsDeploymentConfig.ALL_AT_ONCE
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional["IEcsDeploymentConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsDeploymentGroupAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsDeploymentGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "blue_green_deployment_config": "blueGreenDeploymentConfig",
        "service": "service",
        "alarms": "alarms",
        "application": "application",
        "auto_rollback": "autoRollback",
        "deployment_config": "deploymentConfig",
        "deployment_group_name": "deploymentGroupName",
        "ignore_poll_alarms_failure": "ignorePollAlarmsFailure",
        "role": "role",
    },
)
class EcsDeploymentGroupProps:
    def __init__(
        self,
        *,
        blue_green_deployment_config: typing.Union[EcsBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]],
        service: _IBaseService_3fcdd913,
        alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
        application: typing.Optional["IEcsApplication"] = None,
        auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_config: typing.Optional["IEcsDeploymentConfig"] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Construction properties for ``EcsDeploymentGroup``.

        :param blue_green_deployment_config: The configuration options for blue-green ECS deployments.
        :param service: The ECS service to deploy with this Deployment Group.
        :param alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method. Default: []
        :param application: The reference to the CodeDeploy ECS Application that this Deployment Group belongs to. Default: One will be created for you.
        :param auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: EcsDeploymentConfig.ALL_AT_ONCE
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: An auto-generated name will be used.
        :param ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
        :param role: The service Role of this Deployment Group. Default: - A new Role will be created.

        :exampleMetadata: infused

        Example::

            # my_application: codedeploy.EcsApplication
            # cluster: ecs.Cluster
            # task_definition: ecs.FargateTaskDefinition
            # blue_target_group: elbv2.ITargetGroup
            # green_target_group: elbv2.ITargetGroup
            # listener: elbv2.IApplicationListener
            
            
            service = ecs.FargateService(self, "Service",
                cluster=cluster,
                task_definition=task_definition,
                deployment_controller=ecs.DeploymentController(
                    type=ecs.DeploymentControllerType.CODE_DEPLOY
                )
            )
            
            codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
                service=service,
                blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
                    blue_target_group=blue_target_group,
                    green_target_group=green_target_group,
                    listener=listener
                ),
                deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
            )
        '''
        if isinstance(blue_green_deployment_config, dict):
            blue_green_deployment_config = EcsBlueGreenDeploymentConfig(**blue_green_deployment_config)
        if isinstance(auto_rollback, dict):
            auto_rollback = AutoRollbackConfig(**auto_rollback)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7adf7c582969f2d223ca19321a889bd4195cc6c299e92558e985e0fdcdea2cd0)
            check_type(argname="argument blue_green_deployment_config", value=blue_green_deployment_config, expected_type=type_hints["blue_green_deployment_config"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument auto_rollback", value=auto_rollback, expected_type=type_hints["auto_rollback"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument ignore_poll_alarms_failure", value=ignore_poll_alarms_failure, expected_type=type_hints["ignore_poll_alarms_failure"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "blue_green_deployment_config": blue_green_deployment_config,
            "service": service,
        }
        if alarms is not None:
            self._values["alarms"] = alarms
        if application is not None:
            self._values["application"] = application
        if auto_rollback is not None:
            self._values["auto_rollback"] = auto_rollback
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if deployment_group_name is not None:
            self._values["deployment_group_name"] = deployment_group_name
        if ignore_poll_alarms_failure is not None:
            self._values["ignore_poll_alarms_failure"] = ignore_poll_alarms_failure
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def blue_green_deployment_config(self) -> EcsBlueGreenDeploymentConfig:
        '''The configuration options for blue-green ECS deployments.'''
        result = self._values.get("blue_green_deployment_config")
        assert result is not None, "Required property 'blue_green_deployment_config' is missing"
        return typing.cast(EcsBlueGreenDeploymentConfig, result)

    @builtins.property
    def service(self) -> _IBaseService_3fcdd913:
        '''The ECS service to deploy with this Deployment Group.'''
        result = self._values.get("service")
        assert result is not None, "Required property 'service' is missing"
        return typing.cast(_IBaseService_3fcdd913, result)

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[_IAlarm_ff3eabc0]]:
        '''The CloudWatch alarms associated with this Deployment Group.

        CodeDeploy will stop (and optionally roll back)
        a deployment if during it any of the alarms trigger.

        Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method.

        :default: []

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms.html
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[_IAlarm_ff3eabc0]], result)

    @builtins.property
    def application(self) -> typing.Optional["IEcsApplication"]:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.

        :default: One will be created for you.
        '''
        result = self._values.get("application")
        return typing.cast(typing.Optional["IEcsApplication"], result)

    @builtins.property
    def auto_rollback(self) -> typing.Optional[AutoRollbackConfig]:
        '''The auto-rollback configuration for this Deployment Group.

        :default: - default AutoRollbackConfig.
        '''
        result = self._values.get("auto_rollback")
        return typing.cast(typing.Optional[AutoRollbackConfig], result)

    @builtins.property
    def deployment_config(self) -> typing.Optional["IEcsDeploymentConfig"]:
        '''The Deployment Configuration this Deployment Group uses.

        :default: EcsDeploymentConfig.ALL_AT_ONCE
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional["IEcsDeploymentConfig"], result)

    @builtins.property
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the CodeDeploy Deployment Group.

        :default: An auto-generated name will be used.
        '''
        result = self._values.get("deployment_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_poll_alarms_failure(self) -> typing.Optional[builtins.bool]:
        '''Whether to continue a deployment even if fetching the alarm status from CloudWatch failed.

        :default: false
        '''
        result = self._values.get("ignore_poll_alarms_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The service Role of this Deployment Group.

        :default: - A new Role will be created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EcsDeploymentGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IBaseDeploymentConfig")
class IBaseDeploymentConfig(typing_extensions.Protocol):
    '''The base class for ServerDeploymentConfig, EcsDeploymentConfig, and LambdaDeploymentConfig deployment configurations.'''

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        '''The ARN of the Deployment Configuration.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        '''The physical, human-readable name of the Deployment Configuration.

        :attribute: true
        '''
        ...


class _IBaseDeploymentConfigProxy:
    '''The base class for ServerDeploymentConfig, EcsDeploymentConfig, and LambdaDeploymentConfig deployment configurations.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IBaseDeploymentConfig"

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        '''The ARN of the Deployment Configuration.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        '''The physical, human-readable name of the Deployment Configuration.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IBaseDeploymentConfig).__jsii_proxy_class__ = lambda : _IBaseDeploymentConfigProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IEcsApplication")
class IEcsApplication(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a reference to a CodeDeploy Application deploying to Amazon ECS.

    If you're managing the Application alongside the rest of your CDK resources,
    use the ``EcsApplication`` class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the ``EcsApplication#fromEcsApplicationName`` method.
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...


class _IEcsApplicationProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a reference to a CodeDeploy Application deploying to Amazon ECS.

    If you're managing the Application alongside the rest of your CDK resources,
    use the ``EcsApplication`` class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the ``EcsApplication#fromEcsApplicationName`` method.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IEcsApplication"

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEcsApplication).__jsii_proxy_class__ = lambda : _IEcsApplicationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IEcsDeploymentConfig")
class IEcsDeploymentConfig(IBaseDeploymentConfig, typing_extensions.Protocol):
    '''The Deployment Configuration of an ECS Deployment Group.

    If you're managing the Deployment Configuration alongside the rest of your CDK resources,
    use the ``EcsDeploymentConfig`` class.

    If you want to reference an already existing deployment configuration,
    or one defined in a different CDK Stack,
    use the ``EcsDeploymentConfig#fromEcsDeploymentConfigName`` method.

    The default, pre-defined Configurations are available as constants on the ``EcsDeploymentConfig`` class
    (for example, ``EcsDeploymentConfig.AllAtOnce``).
    '''

    pass


class _IEcsDeploymentConfigProxy(
    jsii.proxy_for(IBaseDeploymentConfig), # type: ignore[misc]
):
    '''The Deployment Configuration of an ECS Deployment Group.

    If you're managing the Deployment Configuration alongside the rest of your CDK resources,
    use the ``EcsDeploymentConfig`` class.

    If you want to reference an already existing deployment configuration,
    or one defined in a different CDK Stack,
    use the ``EcsDeploymentConfig#fromEcsDeploymentConfigName`` method.

    The default, pre-defined Configurations are available as constants on the ``EcsDeploymentConfig`` class
    (for example, ``EcsDeploymentConfig.AllAtOnce``).
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IEcsDeploymentConfig"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEcsDeploymentConfig).__jsii_proxy_class__ = lambda : _IEcsDeploymentConfigProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IEcsDeploymentGroup")
class IEcsDeploymentGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface for an ECS deployment group.'''

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IEcsApplication:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IEcsDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.

        :attribute: true
        '''
        ...


class _IEcsDeploymentGroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface for an ECS deployment group.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IEcsDeploymentGroup"

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IEcsApplication:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        return typing.cast(IEcsApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IEcsDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        return typing.cast(IEcsDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEcsDeploymentGroup).__jsii_proxy_class__ = lambda : _IEcsDeploymentGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.ILambdaApplication")
class ILambdaApplication(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a reference to a CodeDeploy Application deploying to AWS Lambda.

    If you're managing the Application alongside the rest of your CDK resources,
    use the ``LambdaApplication`` class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the ``LambdaApplication#fromLambdaApplicationName`` method.
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...


class _ILambdaApplicationProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a reference to a CodeDeploy Application deploying to AWS Lambda.

    If you're managing the Application alongside the rest of your CDK resources,
    use the ``LambdaApplication`` class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the ``LambdaApplication#fromLambdaApplicationName`` method.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.ILambdaApplication"

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILambdaApplication).__jsii_proxy_class__ = lambda : _ILambdaApplicationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.ILambdaDeploymentConfig")
class ILambdaDeploymentConfig(IBaseDeploymentConfig, typing_extensions.Protocol):
    '''The Deployment Configuration of a Lambda Deployment Group.

    If you're managing the Deployment Configuration alongside the rest of your CDK resources,
    use the ``LambdaDeploymentConfig`` class.

    If you want to reference an already existing deployment configuration,
    or one defined in a different CDK Stack,
    use the ``LambdaDeploymentConfig#fromLambdaDeploymentConfigName`` method.

    The default, pre-defined Configurations are available as constants on the ``LambdaDeploymentConfig`` class
    (``LambdaDeploymentConfig.AllAtOnce``, ``LambdaDeploymentConfig.Canary10Percent30Minutes``, etc.).
    '''

    pass


class _ILambdaDeploymentConfigProxy(
    jsii.proxy_for(IBaseDeploymentConfig), # type: ignore[misc]
):
    '''The Deployment Configuration of a Lambda Deployment Group.

    If you're managing the Deployment Configuration alongside the rest of your CDK resources,
    use the ``LambdaDeploymentConfig`` class.

    If you want to reference an already existing deployment configuration,
    or one defined in a different CDK Stack,
    use the ``LambdaDeploymentConfig#fromLambdaDeploymentConfigName`` method.

    The default, pre-defined Configurations are available as constants on the ``LambdaDeploymentConfig`` class
    (``LambdaDeploymentConfig.AllAtOnce``, ``LambdaDeploymentConfig.Canary10Percent30Minutes``, etc.).
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.ILambdaDeploymentConfig"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILambdaDeploymentConfig).__jsii_proxy_class__ = lambda : _ILambdaDeploymentConfigProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.ILambdaDeploymentGroup")
class ILambdaDeploymentGroup(_IResource_c80c4260, typing_extensions.Protocol):
    '''Interface for a Lambda deployment groups.'''

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> ILambdaApplication:
        '''The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> ILambdaDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.

        :attribute: true
        '''
        ...


class _ILambdaDeploymentGroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Interface for a Lambda deployment groups.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.ILambdaDeploymentGroup"

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> ILambdaApplication:
        '''The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.'''
        return typing.cast(ILambdaApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> ILambdaDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of this Deployment Group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The physical name of the CodeDeploy Deployment Group.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ILambdaDeploymentGroup).__jsii_proxy_class__ = lambda : _ILambdaDeploymentGroupProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IServerApplication")
class IServerApplication(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a reference to a CodeDeploy Application deploying to EC2/on-premise instances.

    If you're managing the Application alongside the rest of your CDK resources,
    use the ``ServerApplication`` class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the ``#fromServerApplicationName`` method.
    '''

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...


class _IServerApplicationProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a reference to a CodeDeploy Application deploying to EC2/on-premise instances.

    If you're managing the Application alongside the rest of your CDK resources,
    use the ``ServerApplication`` class.

    If you want to reference an already existing Application,
    or one defined in a different CDK Stack,
    use the ``#fromServerApplicationName`` method.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IServerApplication"

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerApplication).__jsii_proxy_class__ = lambda : _IServerApplicationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IServerDeploymentConfig")
class IServerDeploymentConfig(IBaseDeploymentConfig, typing_extensions.Protocol):
    '''The Deployment Configuration of an EC2/on-premise Deployment Group.

    The default, pre-defined Configurations are available as constants on the ``ServerDeploymentConfig`` class
    (``ServerDeploymentConfig.HALF_AT_A_TIME``, ``ServerDeploymentConfig.ALL_AT_ONCE``, etc.).
    To create a custom Deployment Configuration,
    instantiate the ``ServerDeploymentConfig`` Construct.
    '''

    pass


class _IServerDeploymentConfigProxy(
    jsii.proxy_for(IBaseDeploymentConfig), # type: ignore[misc]
):
    '''The Deployment Configuration of an EC2/on-premise Deployment Group.

    The default, pre-defined Configurations are available as constants on the ``ServerDeploymentConfig`` class
    (``ServerDeploymentConfig.HALF_AT_A_TIME``, ``ServerDeploymentConfig.ALL_AT_ONCE``, etc.).
    To create a custom Deployment Configuration,
    instantiate the ``ServerDeploymentConfig`` Construct.
    '''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IServerDeploymentConfig"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerDeploymentConfig).__jsii_proxy_class__ = lambda : _IServerDeploymentConfigProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_codedeploy.IServerDeploymentGroup")
class IServerDeploymentGroup(_IResource_c80c4260, typing_extensions.Protocol):
    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IServerApplication:
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IServerDeploymentConfig:
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(
        self,
    ) -> typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]]:
        ...

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        ...


class _IServerDeploymentGroupProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_codedeploy.IServerDeploymentGroup"

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IServerApplication:
        return typing.cast(IServerApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IServerDeploymentConfig:
        return typing.cast(IServerDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(
        self,
    ) -> typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]]:
        return typing.cast(typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]], jsii.get(self, "autoScalingGroups"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "role"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IServerDeploymentGroup).__jsii_proxy_class__ = lambda : _IServerDeploymentGroupProxy


class InstanceTagSet(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.InstanceTagSet",
):
    '''Represents a set of instance tag groups.

    An instance will match a set if it matches all of the groups in the set -
    in other words, sets follow 'and' semantics.
    You can have a maximum of 3 tag groups inside a set.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_autoscaling as autoscaling
        import aws_cdk.aws_cloudwatch as cloudwatch
        
        # application: codedeploy.ServerApplication
        # asg: autoscaling.AutoScalingGroup
        # alarm: cloudwatch.Alarm
        
        deployment_group = codedeploy.ServerDeploymentGroup(self, "CodeDeployDeploymentGroup",
            application=application,
            deployment_group_name="MyDeploymentGroup",
            auto_scaling_groups=[asg],
            # adds User Data that installs the CodeDeploy agent on your auto-scaling groups hosts
            # default: true
            install_agent=True,
            # adds EC2 instances matching tags
            ec2_instance_tags=codedeploy.InstanceTagSet({
                # any instance with tags satisfying
                # key1=v1 or key1=v2 or key2 (any value) or value v3 (any key)
                # will match this group
                "key1": ["v1", "v2"],
                "key2": [],
                "": ["v3"]
            }),
            # adds on-premise instances matching tags
            on_premise_instance_tags=codedeploy.InstanceTagSet({
                "key1": ["v1", "v2"]
            }, {
                "key2": ["v3"]
            }),
            # CloudWatch alarms
            alarms=[alarm],
            # whether to ignore failure to fetch the status of alarms from CloudWatch
            # default: false
            ignore_poll_alarms_failure=False,
            # auto-rollback configuration
            auto_rollback=codedeploy.AutoRollbackConfig(
                failed_deployment=True,  # default: true
                stopped_deployment=True,  # default: false
                deployment_in_alarm=True
            )
        )
    '''

    def __init__(
        self,
        *instance_tag_groups: typing.Mapping[builtins.str, typing.List[builtins.str]],
    ) -> None:
        '''
        :param instance_tag_groups: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64b9abb1b571fcb8018ddc7afe78c42eb103fc0f0e19660e4bb0469356dd1564)
            check_type(argname="argument instance_tag_groups", value=instance_tag_groups, expected_type=typing.Tuple[type_hints["instance_tag_groups"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        jsii.create(self.__class__, self, [*instance_tag_groups])

    @builtins.property
    @jsii.member(jsii_name="instanceTagGroups")
    def instance_tag_groups(
        self,
    ) -> typing.List[typing.Mapping[builtins.str, typing.List[builtins.str]]]:
        return typing.cast(typing.List[typing.Mapping[builtins.str, typing.List[builtins.str]]], jsii.get(self, "instanceTagGroups"))


@jsii.implements(ILambdaApplication)
class LambdaApplication(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaApplication",
):
    '''A CodeDeploy Application that deploys to an AWS Lambda function.

    :resource: AWS::CodeDeploy::Application
    :exampleMetadata: infused

    Example::

        application = codedeploy.LambdaApplication(self, "CodeDeployApplication",
            application_name="MyApplication"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e32e68c167bb11e7bc23a290f22241a7b484b9a93c7477bfc8c699fd61d487e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaApplicationProps(application_name=application_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLambdaApplicationArn")
    @builtins.classmethod
    def from_lambda_application_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        lambda_application_arn: builtins.str,
    ) -> ILambdaApplication:
        '''Import an Application defined either outside the CDK, or in a different CDK Stack, by ARN.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param lambda_application_arn: the ARN of the application to import.

        :return: a Construct representing a reference to an existing Application
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d61dd07d8a44ddb86bf93e059a6adddbf9f337ddc2950868f8521d6d384940a3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_application_arn", value=lambda_application_arn, expected_type=type_hints["lambda_application_arn"])
        return typing.cast(ILambdaApplication, jsii.sinvoke(cls, "fromLambdaApplicationArn", [scope, id, lambda_application_arn]))

    @jsii.member(jsii_name="fromLambdaApplicationName")
    @builtins.classmethod
    def from_lambda_application_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        lambda_application_name: builtins.str,
    ) -> ILambdaApplication:
        '''Import an Application defined either outside the CDK, or in a different CDK Stack.

        The Application's account and region are assumed to be the same as the stack it is being imported
        into. If not, use ``fromLambdaApplicationArn``.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param lambda_application_name: the name of the application to import.

        :return: a Construct representing a reference to an existing Application
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1450d2b1c6c573bfe2bedfa6cd62cfe0f9b692ed8c0d2be4332b4ad5579ec629)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_application_name", value=lambda_application_name, expected_type=type_hints["lambda_application_name"])
        return typing.cast(ILambdaApplication, jsii.sinvoke(cls, "fromLambdaApplicationName", [scope, id, lambda_application_name]))

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName"},
)
class LambdaApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for ``LambdaApplication``.

        :param application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used

        :exampleMetadata: infused

        Example::

            application = codedeploy.LambdaApplication(self, "CodeDeployApplication",
                application_name="MyApplication"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92ab1acbc62b972c13cc918ece32b4065ed5e2d1fd027313d6a8f70f0f7f7d7a)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the CodeDeploy Application.

        :default: an auto-generated name will be used
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaDeploymentConfigImportProps",
    jsii_struct_bases=[],
    name_mapping={"deployment_config_name": "deploymentConfigName"},
)
class LambdaDeploymentConfigImportProps:
    def __init__(self, *, deployment_config_name: builtins.str) -> None:
        '''Properties of a reference to a CodeDeploy Lambda Deployment Configuration.

        :param deployment_config_name: The physical, human-readable name of the custom CodeDeploy Lambda Deployment Configuration that we are referencing.

        :see: LambdaDeploymentConfig# import
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            lambda_deployment_config_import_props = codedeploy.LambdaDeploymentConfigImportProps(
                deployment_config_name="deploymentConfigName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87bb46cc3cd2b6f2e34d49e71d8065dcab36372a5cc7cbe2a6cb84bf8150c93a)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "deployment_config_name": deployment_config_name,
        }

    @builtins.property
    def deployment_config_name(self) -> builtins.str:
        '''The physical, human-readable name of the custom CodeDeploy Lambda Deployment Configuration that we are referencing.'''
        result = self._values.get("deployment_config_name")
        assert result is not None, "Required property 'deployment_config_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDeploymentConfigImportProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaDeploymentConfigProps",
    jsii_struct_bases=[BaseDeploymentConfigOptions],
    name_mapping={
        "deployment_config_name": "deploymentConfigName",
        "traffic_routing": "trafficRouting",
    },
)
class LambdaDeploymentConfigProps(BaseDeploymentConfigOptions):
    def __init__(
        self,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
        traffic_routing: typing.Optional["TrafficRouting"] = None,
    ) -> None:
        '''Construction properties of ``LambdaDeploymentConfig``.

        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        :param traffic_routing: The configuration that specifies how traffic is shifted from the 'blue' target group to the 'green' target group during a deployment. Default: AllAtOnce

        :exampleMetadata: infused

        Example::

            # application: codedeploy.LambdaApplication
            # alias: lambda.Alias
            config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
                traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                    interval=Duration.minutes(15),
                    percentage=5
                )
            )
            deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
                application=application,
                alias=alias,
                deployment_config=config
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc83553749492603e2a4699e478de4d29b9ccf880c156fb0da254af8ec807aee)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument traffic_routing", value=traffic_routing, expected_type=type_hints["traffic_routing"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name
        if traffic_routing is not None:
            self._values["traffic_routing"] = traffic_routing

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the Deployment Configuration.

        :default: - automatically generated name
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def traffic_routing(self) -> typing.Optional["TrafficRouting"]:
        '''The configuration that specifies how traffic is shifted from the 'blue' target group to the 'green' target group during a deployment.

        :default: AllAtOnce
        '''
        result = self._values.get("traffic_routing")
        return typing.cast(typing.Optional["TrafficRouting"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDeploymentConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(ILambdaDeploymentGroup)
class LambdaDeploymentGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaDeploymentGroup",
):
    '''
    :resource: AWS::CodeDeploy::DeploymentGroup
    :exampleMetadata: infused

    Example::

        # application: codedeploy.LambdaApplication
        # alias: lambda.Alias
        config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
            traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                interval=Duration.minutes(15),
                percentage=5
            )
        )
        deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
            application=application,
            alias=alias,
            deployment_config=config
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias: _Alias_55be8873,
        alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
        application: typing.Optional[ILambdaApplication] = None,
        auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
        post_hook: typing.Optional[_IFunction_6adb0ab8] = None,
        pre_hook: typing.Optional[_IFunction_6adb0ab8] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alias: Lambda Alias to shift traffic. Updating the version of the alias will trigger a CodeDeploy deployment. [disable-awslint:ref-via-interface] since we need to modify the alias CFN resource update policy
        :param alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method. Default: []
        :param application: The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to. Default: - One will be created for you.
        :param auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: - An auto-generated name will be used.
        :param ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
        :param post_hook: The Lambda function to run after traffic routing starts. Default: - None.
        :param pre_hook: The Lambda function to run before traffic routing starts. Default: - None.
        :param role: The service Role of this Deployment Group. Default: - A new Role will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c26416b16de08b4064de631244255b96e87828c1c22b3d5795282b4183224b2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaDeploymentGroupProps(
            alias=alias,
            alarms=alarms,
            application=application,
            auto_rollback=auto_rollback,
            deployment_config=deployment_config,
            deployment_group_name=deployment_group_name,
            ignore_poll_alarms_failure=ignore_poll_alarms_failure,
            post_hook=post_hook,
            pre_hook=pre_hook,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLambdaDeploymentGroupAttributes")
    @builtins.classmethod
    def from_lambda_deployment_group_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: ILambdaApplication,
        deployment_group_name: builtins.str,
        deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
    ) -> ILambdaDeploymentGroup:
        '''Import an Lambda Deployment Group defined either outside the CDK app, or in a different AWS region.

        Account and region for the DeploymentGroup are taken from the application.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param application: The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Lambda Deployment Group that we are referencing.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES

        :return: a Construct representing a reference to an existing Deployment Group
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fd4dfddfe47c0a8dd92426b46cd63260d58eb3379c02a54f9334570681da9bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = LambdaDeploymentGroupAttributes(
            application=application,
            deployment_group_name=deployment_group_name,
            deployment_config=deployment_config,
        )

        return typing.cast(ILambdaDeploymentGroup, jsii.sinvoke(cls, "fromLambdaDeploymentGroupAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: _IAlarm_ff3eabc0) -> None:
        '''Associates an additional alarm with this Deployment Group.

        :param alarm: the alarm to associate with this Deployment Group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b711b8130a1d80370d61b0db615c68c614d3077ac9c81be826135376059b97e)
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
        return typing.cast(None, jsii.invoke(self, "addAlarm", [alarm]))

    @jsii.member(jsii_name="addPostHook")
    def add_post_hook(self, post_hook: _IFunction_6adb0ab8) -> None:
        '''Associate a function to run after deployment completes.

        :param post_hook: function to run after deployment completes.

        :throws: an error if a post-hook function is already configured
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52088593799588d855f46763ba6983d5b95d7128d66002267869967f0a287d99)
            check_type(argname="argument post_hook", value=post_hook, expected_type=type_hints["post_hook"])
        return typing.cast(None, jsii.invoke(self, "addPostHook", [post_hook]))

    @jsii.member(jsii_name="addPreHook")
    def add_pre_hook(self, pre_hook: _IFunction_6adb0ab8) -> None:
        '''Associate a function to run before deployment begins.

        :param pre_hook: function to run before deployment beings.

        :throws: an error if a pre-hook function is already configured
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9479e7d155c760cd01795544331c610a1cab348cb04f2ac1aaa5373c713b9424)
            check_type(argname="argument pre_hook", value=pre_hook, expected_type=type_hints["pre_hook"])
        return typing.cast(None, jsii.invoke(self, "addPreHook", [pre_hook]))

    @jsii.member(jsii_name="grantPutLifecycleEventHookExecutionStatus")
    def grant_put_lifecycle_event_hook_execution_status(
        self,
        grantee: _IGrantable_71c4f5de,
    ) -> _Grant_a7ae64f8:
        '''Grant a principal permission to codedeploy:PutLifecycleEventHookExecutionStatus on this deployment group resource.

        :param grantee: to grant permission to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d8689c21818340ec688b7586fd416bd82b1e7011d11184910717b5859285cb4)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantPutLifecycleEventHookExecutionStatus", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> ILambdaApplication:
        '''The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.'''
        return typing.cast(ILambdaApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> ILambdaDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of the Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The name of the Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_235f5d8e:
        '''The service Role of this Deployment Group.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaDeploymentGroupAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "application": "application",
        "deployment_group_name": "deploymentGroupName",
        "deployment_config": "deploymentConfig",
    },
)
class LambdaDeploymentGroupAttributes:
    def __init__(
        self,
        *,
        application: ILambdaApplication,
        deployment_group_name: builtins.str,
        deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
    ) -> None:
        '''Properties of a reference to a CodeDeploy Lambda Deployment Group.

        :param application: The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Lambda Deployment Group that we are referencing.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES

        :see: LambdaDeploymentGroup#fromLambdaDeploymentGroupAttributes
        :exampleMetadata: infused

        Example::

            # application: codedeploy.LambdaApplication
            
            deployment_group = codedeploy.LambdaDeploymentGroup.from_lambda_deployment_group_attributes(self, "ExistingCodeDeployDeploymentGroup",
                application=application,
                deployment_group_name="MyExistingDeploymentGroup"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08bd7879a63053a6c7bc752ef445954728069ab3039a8ede60d6b4eeea401e64)
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
            "deployment_group_name": deployment_group_name,
        }
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config

    @builtins.property
    def application(self) -> ILambdaApplication:
        '''The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast(ILambdaApplication, result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''The physical, human-readable name of the CodeDeploy Lambda Deployment Group that we are referencing.'''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_config(self) -> typing.Optional[ILambdaDeploymentConfig]:
        '''The Deployment Configuration this Deployment Group uses.

        :default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional[ILambdaDeploymentConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDeploymentGroupAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaDeploymentGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "alias": "alias",
        "alarms": "alarms",
        "application": "application",
        "auto_rollback": "autoRollback",
        "deployment_config": "deploymentConfig",
        "deployment_group_name": "deploymentGroupName",
        "ignore_poll_alarms_failure": "ignorePollAlarmsFailure",
        "post_hook": "postHook",
        "pre_hook": "preHook",
        "role": "role",
    },
)
class LambdaDeploymentGroupProps:
    def __init__(
        self,
        *,
        alias: _Alias_55be8873,
        alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
        application: typing.Optional[ILambdaApplication] = None,
        auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
        post_hook: typing.Optional[_IFunction_6adb0ab8] = None,
        pre_hook: typing.Optional[_IFunction_6adb0ab8] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Construction properties for ``LambdaDeploymentGroup``.

        :param alias: Lambda Alias to shift traffic. Updating the version of the alias will trigger a CodeDeploy deployment. [disable-awslint:ref-via-interface] since we need to modify the alias CFN resource update policy
        :param alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method. Default: []
        :param application: The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to. Default: - One will be created for you.
        :param auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: - An auto-generated name will be used.
        :param ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
        :param post_hook: The Lambda function to run after traffic routing starts. Default: - None.
        :param pre_hook: The Lambda function to run before traffic routing starts. Default: - None.
        :param role: The service Role of this Deployment Group. Default: - A new Role will be created.

        :exampleMetadata: infused

        Example::

            # my_application: codedeploy.LambdaApplication
            # func: lambda.Function
            
            version = func.current_version
            version1_alias = lambda_.Alias(self, "alias",
                alias_name="prod",
                version=version
            )
            
            deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
                application=my_application,  # optional property: one will be created for you if not provided
                alias=version1_alias,
                deployment_config=codedeploy.LambdaDeploymentConfig.LINEAR_10PERCENT_EVERY_1MINUTE
            )
        '''
        if isinstance(auto_rollback, dict):
            auto_rollback = AutoRollbackConfig(**auto_rollback)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__874e757437525f2d71406c292cf5ac7fae66797609da322dac9063247a871238)
            check_type(argname="argument alias", value=alias, expected_type=type_hints["alias"])
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument auto_rollback", value=auto_rollback, expected_type=type_hints["auto_rollback"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument ignore_poll_alarms_failure", value=ignore_poll_alarms_failure, expected_type=type_hints["ignore_poll_alarms_failure"])
            check_type(argname="argument post_hook", value=post_hook, expected_type=type_hints["post_hook"])
            check_type(argname="argument pre_hook", value=pre_hook, expected_type=type_hints["pre_hook"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias": alias,
        }
        if alarms is not None:
            self._values["alarms"] = alarms
        if application is not None:
            self._values["application"] = application
        if auto_rollback is not None:
            self._values["auto_rollback"] = auto_rollback
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if deployment_group_name is not None:
            self._values["deployment_group_name"] = deployment_group_name
        if ignore_poll_alarms_failure is not None:
            self._values["ignore_poll_alarms_failure"] = ignore_poll_alarms_failure
        if post_hook is not None:
            self._values["post_hook"] = post_hook
        if pre_hook is not None:
            self._values["pre_hook"] = pre_hook
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def alias(self) -> _Alias_55be8873:
        '''Lambda Alias to shift traffic. Updating the version of the alias will trigger a CodeDeploy deployment.

        [disable-awslint:ref-via-interface] since we need to modify the alias CFN resource update policy
        '''
        result = self._values.get("alias")
        assert result is not None, "Required property 'alias' is missing"
        return typing.cast(_Alias_55be8873, result)

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[_IAlarm_ff3eabc0]]:
        '''The CloudWatch alarms associated with this Deployment Group.

        CodeDeploy will stop (and optionally roll back)
        a deployment if during it any of the alarms trigger.

        Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method.

        :default: []

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms.html
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[_IAlarm_ff3eabc0]], result)

    @builtins.property
    def application(self) -> typing.Optional[ILambdaApplication]:
        '''The reference to the CodeDeploy Lambda Application that this Deployment Group belongs to.

        :default: - One will be created for you.
        '''
        result = self._values.get("application")
        return typing.cast(typing.Optional[ILambdaApplication], result)

    @builtins.property
    def auto_rollback(self) -> typing.Optional[AutoRollbackConfig]:
        '''The auto-rollback configuration for this Deployment Group.

        :default: - default AutoRollbackConfig.
        '''
        result = self._values.get("auto_rollback")
        return typing.cast(typing.Optional[AutoRollbackConfig], result)

    @builtins.property
    def deployment_config(self) -> typing.Optional[ILambdaDeploymentConfig]:
        '''The Deployment Configuration this Deployment Group uses.

        :default: LambdaDeploymentConfig.CANARY_10PERCENT_5MINUTES
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional[ILambdaDeploymentConfig], result)

    @builtins.property
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the CodeDeploy Deployment Group.

        :default: - An auto-generated name will be used.
        '''
        result = self._values.get("deployment_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_poll_alarms_failure(self) -> typing.Optional[builtins.bool]:
        '''Whether to continue a deployment even if fetching the alarm status from CloudWatch failed.

        :default: false
        '''
        result = self._values.get("ignore_poll_alarms_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def post_hook(self) -> typing.Optional[_IFunction_6adb0ab8]:
        '''The Lambda function to run after traffic routing starts.

        :default: - None.
        '''
        result = self._values.get("post_hook")
        return typing.cast(typing.Optional[_IFunction_6adb0ab8], result)

    @builtins.property
    def pre_hook(self) -> typing.Optional[_IFunction_6adb0ab8]:
        '''The Lambda function to run before traffic routing starts.

        :default: - None.
        '''
        result = self._values.get("pre_hook")
        return typing.cast(typing.Optional[_IFunction_6adb0ab8], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The service Role of this Deployment Group.

        :default: - A new Role will be created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDeploymentGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.LinearTrafficRoutingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "linear_interval": "linearInterval",
        "linear_percentage": "linearPercentage",
    },
)
class LinearTrafficRoutingConfig:
    def __init__(
        self,
        *,
        linear_interval: jsii.Number,
        linear_percentage: jsii.Number,
    ) -> None:
        '''Represents the configuration specific to linear traffic shifting.

        :param linear_interval: The number of minutes between each incremental traffic shift of a ``TimeBasedLinear`` deployment.
        :param linear_percentage: The percentage of traffic that is shifted at the start of each increment of a ``TimeBasedLinear`` deployment.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            linear_traffic_routing_config = codedeploy.LinearTrafficRoutingConfig(
                linear_interval=123,
                linear_percentage=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__370bf2390e5c88cb8bbf9c66f599b85ef458396f8157823b987c090f4826d4ef)
            check_type(argname="argument linear_interval", value=linear_interval, expected_type=type_hints["linear_interval"])
            check_type(argname="argument linear_percentage", value=linear_percentage, expected_type=type_hints["linear_percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "linear_interval": linear_interval,
            "linear_percentage": linear_percentage,
        }

    @builtins.property
    def linear_interval(self) -> jsii.Number:
        '''The number of minutes between each incremental traffic shift of a ``TimeBasedLinear`` deployment.'''
        result = self._values.get("linear_interval")
        assert result is not None, "Required property 'linear_interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def linear_percentage(self) -> jsii.Number:
        '''The percentage of traffic that is shifted at the start of each increment of a ``TimeBasedLinear`` deployment.'''
        result = self._values.get("linear_percentage")
        assert result is not None, "Required property 'linear_percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LinearTrafficRoutingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancer(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_codedeploy.LoadBalancer",
):
    '''An interface of an abstract load balancer, as needed by CodeDeploy.

    Create instances using the static factory methods:
    ``#classic``, ``#application`` and ``#network``.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancing as elb
        
        # lb: elb.LoadBalancer
        
        lb.add_listener(
            external_port=80
        )
        
        deployment_group = codedeploy.ServerDeploymentGroup(self, "DeploymentGroup",
            load_balancer=codedeploy.LoadBalancer.classic(lb)
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="application")
    @builtins.classmethod
    def application(
        cls,
        alb_target_group: _IApplicationTargetGroup_57799827,
    ) -> "LoadBalancer":
        '''Creates a new CodeDeploy load balancer from an Application Load Balancer Target Group.

        :param alb_target_group: an ALB Target Group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c36a2f946c61769d76c913c28d5738063c97172f02aedd94b235d81679262630)
            check_type(argname="argument alb_target_group", value=alb_target_group, expected_type=type_hints["alb_target_group"])
        return typing.cast("LoadBalancer", jsii.sinvoke(cls, "application", [alb_target_group]))

    @jsii.member(jsii_name="classic")
    @builtins.classmethod
    def classic(cls, load_balancer: _LoadBalancer_a894d40e) -> "LoadBalancer":
        '''Creates a new CodeDeploy load balancer from a Classic ELB Load Balancer.

        :param load_balancer: a classic ELB Load Balancer.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8808efa456e0bde58915d9f2353dc69253ae06e9b202151c399da611d72dc3a7)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        return typing.cast("LoadBalancer", jsii.sinvoke(cls, "classic", [load_balancer]))

    @jsii.member(jsii_name="network")
    @builtins.classmethod
    def network(cls, nlb_target_group: _INetworkTargetGroup_abca2df7) -> "LoadBalancer":
        '''Creates a new CodeDeploy load balancer from a Network Load Balancer Target Group.

        :param nlb_target_group: an NLB Target Group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c09dbdbc45c1037d7977cfe1df1e715bec88560b2da64188007c9c48538f678)
            check_type(argname="argument nlb_target_group", value=nlb_target_group, expected_type=type_hints["nlb_target_group"])
        return typing.cast("LoadBalancer", jsii.sinvoke(cls, "network", [nlb_target_group]))

    @builtins.property
    @jsii.member(jsii_name="generation")
    @abc.abstractmethod
    def generation(self) -> "LoadBalancerGeneration":
        ...

    @builtins.property
    @jsii.member(jsii_name="name")
    @abc.abstractmethod
    def name(self) -> builtins.str:
        ...


class _LoadBalancerProxy(LoadBalancer):
    @builtins.property
    @jsii.member(jsii_name="generation")
    def generation(self) -> "LoadBalancerGeneration":
        return typing.cast("LoadBalancerGeneration", jsii.get(self, "generation"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "name"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, LoadBalancer).__jsii_proxy_class__ = lambda : _LoadBalancerProxy


@jsii.enum(jsii_type="aws-cdk-lib.aws_codedeploy.LoadBalancerGeneration")
class LoadBalancerGeneration(enum.Enum):
    '''The generations of AWS load balancing solutions.'''

    FIRST = "FIRST"
    '''The first generation (ELB Classic).'''
    SECOND = "SECOND"
    '''The second generation (ALB and NLB).'''


class MinimumHealthyHosts(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.MinimumHealthyHosts",
):
    '''Minimum number of healthy hosts for a server deployment.

    :exampleMetadata: infused

    Example::

        deployment_config = codedeploy.ServerDeploymentConfig(self, "DeploymentConfiguration",
            deployment_config_name="MyDeploymentConfiguration",  # optional property
            # one of these is required, but both cannot be specified at the same time
            minimum_healthy_hosts=codedeploy.MinimumHealthyHosts.count(2)
        )
    '''

    @jsii.member(jsii_name="count")
    @builtins.classmethod
    def count(cls, value: jsii.Number) -> "MinimumHealthyHosts":
        '''The minimum healhty hosts threshold expressed as an absolute number.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43a212ab251dfefee2c1b1ee5cee194431e2a0ddeec2d9373bc5962fcc70beac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("MinimumHealthyHosts", jsii.sinvoke(cls, "count", [value]))

    @jsii.member(jsii_name="percentage")
    @builtins.classmethod
    def percentage(cls, value: jsii.Number) -> "MinimumHealthyHosts":
        '''The minmum healhty hosts threshold expressed as a percentage of the fleet.

        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c2a97036f753857be857236ee3fb97ddf235514bd9c31466fb2e569196a8670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast("MinimumHealthyHosts", jsii.sinvoke(cls, "percentage", [value]))


@jsii.implements(IServerApplication)
class ServerApplication(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerApplication",
):
    '''A CodeDeploy Application that deploys to EC2/on-premise instances.

    :resource: AWS::CodeDeploy::Application
    :exampleMetadata: infused

    Example::

        application = codedeploy.ServerApplication(self, "CodeDeployApplication",
            application_name="MyApplication"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff491d45a3da21d4d70991ac332ef8f240b72138a59519fcf6c3da3a3a9cb970)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServerApplicationProps(application_name=application_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServerApplicationArn")
    @builtins.classmethod
    def from_server_application_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        server_application_arn: builtins.str,
    ) -> IServerApplication:
        '''Import an Application defined either outside the CDK, or in a different CDK Stack, by ARN.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param server_application_arn: the ARN of the application to import.

        :return: a Construct representing a reference to an existing Application
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf6f1cc9e06bced10736cddcc278aca232660b56bc0451a57cced62037ec8590)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument server_application_arn", value=server_application_arn, expected_type=type_hints["server_application_arn"])
        return typing.cast(IServerApplication, jsii.sinvoke(cls, "fromServerApplicationArn", [scope, id, server_application_arn]))

    @jsii.member(jsii_name="fromServerApplicationName")
    @builtins.classmethod
    def from_server_application_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        server_application_name: builtins.str,
    ) -> IServerApplication:
        '''Import an Application defined either outside the CDK app, or in a different region.

        The Application's account and region are assumed to be the same as the stack it is being imported
        into. If not, use ``fromServerApplicationArn``.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param server_application_name: the name of the application to import.

        :return: a Construct representing a reference to an existing Application
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__926add8da73c5c44e3476965c380244e6b8d904443a6d509c4211b7aeebc5804)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument server_application_name", value=server_application_name, expected_type=type_hints["server_application_name"])
        return typing.cast(IServerApplication, jsii.sinvoke(cls, "fromServerApplicationName", [scope, id, server_application_name]))

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerApplicationProps",
    jsii_struct_bases=[],
    name_mapping={"application_name": "applicationName"},
)
class ServerApplicationProps:
    def __init__(
        self,
        *,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for ``ServerApplication``.

        :param application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used

        :exampleMetadata: infused

        Example::

            application = codedeploy.ServerApplication(self, "CodeDeployApplication",
                application_name="MyApplication"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5712e790d967a85a2bf9b346a95ce6db55b781233d88b2df81a98394233a8fb)
            check_type(argname="argument application_name", value=application_name, expected_type=type_hints["application_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if application_name is not None:
            self._values["application_name"] = application_name

    @builtins.property
    def application_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the CodeDeploy Application.

        :default: an auto-generated name will be used
        '''
        result = self._values.get("application_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerDeploymentConfigProps",
    jsii_struct_bases=[BaseDeploymentConfigOptions],
    name_mapping={
        "deployment_config_name": "deploymentConfigName",
        "minimum_healthy_hosts": "minimumHealthyHosts",
    },
)
class ServerDeploymentConfigProps(BaseDeploymentConfigOptions):
    def __init__(
        self,
        *,
        deployment_config_name: typing.Optional[builtins.str] = None,
        minimum_healthy_hosts: MinimumHealthyHosts,
    ) -> None:
        '''Construction properties of ``ServerDeploymentConfig``.

        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        :param minimum_healthy_hosts: Minimum number of healthy hosts.

        :exampleMetadata: infused

        Example::

            deployment_config = codedeploy.ServerDeploymentConfig(self, "DeploymentConfiguration",
                deployment_config_name="MyDeploymentConfiguration",  # optional property
                # one of these is required, but both cannot be specified at the same time
                minimum_healthy_hosts=codedeploy.MinimumHealthyHosts.count(2)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46be421d00313823efbbb0072b871dc311f7d9fca8dee4c13562ddd078f8cd37)
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
            check_type(argname="argument minimum_healthy_hosts", value=minimum_healthy_hosts, expected_type=type_hints["minimum_healthy_hosts"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "minimum_healthy_hosts": minimum_healthy_hosts,
        }
        if deployment_config_name is not None:
            self._values["deployment_config_name"] = deployment_config_name

    @builtins.property
    def deployment_config_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the Deployment Configuration.

        :default: - automatically generated name
        '''
        result = self._values.get("deployment_config_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def minimum_healthy_hosts(self) -> MinimumHealthyHosts:
        '''Minimum number of healthy hosts.'''
        result = self._values.get("minimum_healthy_hosts")
        assert result is not None, "Required property 'minimum_healthy_hosts' is missing"
        return typing.cast(MinimumHealthyHosts, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerDeploymentConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IServerDeploymentGroup)
class ServerDeploymentGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerDeploymentGroup",
):
    '''A CodeDeploy Deployment Group that deploys to EC2/on-premise instances.

    :resource: AWS::CodeDeploy::DeploymentGroup
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancing as elb
        
        # lb: elb.LoadBalancer
        
        lb.add_listener(
            external_port=80
        )
        
        deployment_group = codedeploy.ServerDeploymentGroup(self, "DeploymentGroup",
            load_balancer=codedeploy.LoadBalancer.classic(lb)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
        application: typing.Optional[IServerApplication] = None,
        auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling_groups: typing.Optional[typing.Sequence[_IAutoScalingGroup_360f1cde]] = None,
        deployment_config: typing.Optional[IServerDeploymentConfig] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        ec2_instance_tags: typing.Optional[InstanceTagSet] = None,
        ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
        install_agent: typing.Optional[builtins.bool] = None,
        load_balancer: typing.Optional[LoadBalancer] = None,
        on_premise_instance_tags: typing.Optional[InstanceTagSet] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method. Default: []
        :param application: The CodeDeploy EC2/on-premise Application this Deployment Group belongs to. Default: - A new Application will be created.
        :param auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
        :param auto_scaling_groups: The auto-scaling groups belonging to this Deployment Group. Auto-scaling groups can also be added after the Deployment Group is created using the ``#addAutoScalingGroup`` method. [disable-awslint:ref-via-interface] is needed because we update userdata for ASGs to install the codedeploy agent. Default: []
        :param deployment_config: The EC2/on-premise Deployment Configuration to use for this Deployment Group. Default: ServerDeploymentConfig#OneAtATime
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: - An auto-generated name will be used.
        :param ec2_instance_tags: All EC2 instances matching the given set of tags when a deployment occurs will be added to this Deployment Group. Default: - No additional EC2 instances will be added to the Deployment Group.
        :param ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
        :param install_agent: If you've provided any auto-scaling groups with the ``#autoScalingGroups`` property, you can set this property to add User Data that installs the CodeDeploy agent on the instances. Default: true
        :param load_balancer: The load balancer to place in front of this Deployment Group. Can be created from either a classic Elastic Load Balancer, or an Application Load Balancer / Network Load Balancer Target Group. Default: - Deployment Group will not have a load balancer defined.
        :param on_premise_instance_tags: All on-premise instances matching the given set of tags when a deployment occurs will be added to this Deployment Group. Default: - No additional on-premise instances will be added to the Deployment Group.
        :param role: The service Role of this Deployment Group. Default: - A new Role will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0364d4b48c02675a1899e742e45b411f0e83905e634a84441d088a41fe25c8f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServerDeploymentGroupProps(
            alarms=alarms,
            application=application,
            auto_rollback=auto_rollback,
            auto_scaling_groups=auto_scaling_groups,
            deployment_config=deployment_config,
            deployment_group_name=deployment_group_name,
            ec2_instance_tags=ec2_instance_tags,
            ignore_poll_alarms_failure=ignore_poll_alarms_failure,
            install_agent=install_agent,
            load_balancer=load_balancer,
            on_premise_instance_tags=on_premise_instance_tags,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServerDeploymentGroupAttributes")
    @builtins.classmethod
    def from_server_deployment_group_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: IServerApplication,
        deployment_group_name: builtins.str,
        deployment_config: typing.Optional[IServerDeploymentConfig] = None,
    ) -> IServerDeploymentGroup:
        '''Import an EC2/on-premise Deployment Group defined either outside the CDK app, or in a different region.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param application: The reference to the CodeDeploy EC2/on-premise Application that this Deployment Group belongs to.
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy EC2/on-premise Deployment Group that we are referencing.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: ServerDeploymentConfig#OneAtATime

        :return: a Construct representing a reference to an existing Deployment Group
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8af8e520b8abc653e37c88dc9f6e51e7d52aa5f24d99a8bcc8765154067e55f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ServerDeploymentGroupAttributes(
            application=application,
            deployment_group_name=deployment_group_name,
            deployment_config=deployment_config,
        )

        return typing.cast(IServerDeploymentGroup, jsii.sinvoke(cls, "fromServerDeploymentGroupAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: _IAlarm_ff3eabc0) -> None:
        '''Associates an additional alarm with this Deployment Group.

        :param alarm: the alarm to associate with this Deployment Group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__356a323fcb86d198006a31f41e7e9d1c8a6892ac423e8cb69666cd1ddcb8e718)
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
        return typing.cast(None, jsii.invoke(self, "addAlarm", [alarm]))

    @jsii.member(jsii_name="addAutoScalingGroup")
    def add_auto_scaling_group(self, asg: _AutoScalingGroup_c547a7b9) -> None:
        '''Adds an additional auto-scaling group to this Deployment Group.

        :param asg: the auto-scaling group to add to this Deployment Group. [disable-awslint:ref-via-interface] is needed in order to install the code deploy agent by updating the ASGs user data.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8eb5bbbb7e095997fadbddebece8f587dfbebf76e4fba6c071f9def29db693c8)
            check_type(argname="argument asg", value=asg, expected_type=type_hints["asg"])
        return typing.cast(None, jsii.invoke(self, "addAutoScalingGroup", [asg]))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IServerApplication:
        return typing.cast(IServerApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IServerDeploymentConfig:
        return typing.cast(IServerDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of the Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The name of the Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingGroups")
    def auto_scaling_groups(
        self,
    ) -> typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]]:
        return typing.cast(typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]], jsii.get(self, "autoScalingGroups"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The service Role of this Deployment Group.'''
        return typing.cast(typing.Optional[_IRole_235f5d8e], jsii.get(self, "role"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerDeploymentGroupAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "application": "application",
        "deployment_group_name": "deploymentGroupName",
        "deployment_config": "deploymentConfig",
    },
)
class ServerDeploymentGroupAttributes:
    def __init__(
        self,
        *,
        application: IServerApplication,
        deployment_group_name: builtins.str,
        deployment_config: typing.Optional[IServerDeploymentConfig] = None,
    ) -> None:
        '''Properties of a reference to a CodeDeploy EC2/on-premise Deployment Group.

        :param application: The reference to the CodeDeploy EC2/on-premise Application that this Deployment Group belongs to.
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy EC2/on-premise Deployment Group that we are referencing.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: ServerDeploymentConfig#OneAtATime

        :see: ServerDeploymentGroup# import
        :exampleMetadata: infused

        Example::

            # application: codedeploy.ServerApplication
            
            deployment_group = codedeploy.ServerDeploymentGroup.from_server_deployment_group_attributes(self, "ExistingCodeDeployDeploymentGroup",
                application=application,
                deployment_group_name="MyExistingDeploymentGroup"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7c78d15fd80ffece3b49e232b4a29903107350aac8446220b8caea80c448a80)
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application": application,
            "deployment_group_name": deployment_group_name,
        }
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config

    @builtins.property
    def application(self) -> IServerApplication:
        '''The reference to the CodeDeploy EC2/on-premise Application that this Deployment Group belongs to.'''
        result = self._values.get("application")
        assert result is not None, "Required property 'application' is missing"
        return typing.cast(IServerApplication, result)

    @builtins.property
    def deployment_group_name(self) -> builtins.str:
        '''The physical, human-readable name of the CodeDeploy EC2/on-premise Deployment Group that we are referencing.'''
        result = self._values.get("deployment_group_name")
        assert result is not None, "Required property 'deployment_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def deployment_config(self) -> typing.Optional[IServerDeploymentConfig]:
        '''The Deployment Configuration this Deployment Group uses.

        :default: ServerDeploymentConfig#OneAtATime
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional[IServerDeploymentConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerDeploymentGroupAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerDeploymentGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "alarms": "alarms",
        "application": "application",
        "auto_rollback": "autoRollback",
        "auto_scaling_groups": "autoScalingGroups",
        "deployment_config": "deploymentConfig",
        "deployment_group_name": "deploymentGroupName",
        "ec2_instance_tags": "ec2InstanceTags",
        "ignore_poll_alarms_failure": "ignorePollAlarmsFailure",
        "install_agent": "installAgent",
        "load_balancer": "loadBalancer",
        "on_premise_instance_tags": "onPremiseInstanceTags",
        "role": "role",
    },
)
class ServerDeploymentGroupProps:
    def __init__(
        self,
        *,
        alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
        application: typing.Optional[IServerApplication] = None,
        auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        auto_scaling_groups: typing.Optional[typing.Sequence[_IAutoScalingGroup_360f1cde]] = None,
        deployment_config: typing.Optional[IServerDeploymentConfig] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        ec2_instance_tags: typing.Optional[InstanceTagSet] = None,
        ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
        install_agent: typing.Optional[builtins.bool] = None,
        load_balancer: typing.Optional[LoadBalancer] = None,
        on_premise_instance_tags: typing.Optional[InstanceTagSet] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''Construction properties for ``ServerDeploymentGroup``.

        :param alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method. Default: []
        :param application: The CodeDeploy EC2/on-premise Application this Deployment Group belongs to. Default: - A new Application will be created.
        :param auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
        :param auto_scaling_groups: The auto-scaling groups belonging to this Deployment Group. Auto-scaling groups can also be added after the Deployment Group is created using the ``#addAutoScalingGroup`` method. [disable-awslint:ref-via-interface] is needed because we update userdata for ASGs to install the codedeploy agent. Default: []
        :param deployment_config: The EC2/on-premise Deployment Configuration to use for this Deployment Group. Default: ServerDeploymentConfig#OneAtATime
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: - An auto-generated name will be used.
        :param ec2_instance_tags: All EC2 instances matching the given set of tags when a deployment occurs will be added to this Deployment Group. Default: - No additional EC2 instances will be added to the Deployment Group.
        :param ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
        :param install_agent: If you've provided any auto-scaling groups with the ``#autoScalingGroups`` property, you can set this property to add User Data that installs the CodeDeploy agent on the instances. Default: true
        :param load_balancer: The load balancer to place in front of this Deployment Group. Can be created from either a classic Elastic Load Balancer, or an Application Load Balancer / Network Load Balancer Target Group. Default: - Deployment Group will not have a load balancer defined.
        :param on_premise_instance_tags: All on-premise instances matching the given set of tags when a deployment occurs will be added to this Deployment Group. Default: - No additional on-premise instances will be added to the Deployment Group.
        :param role: The service Role of this Deployment Group. Default: - A new Role will be created.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_elasticloadbalancing as elb
            
            # lb: elb.LoadBalancer
            
            lb.add_listener(
                external_port=80
            )
            
            deployment_group = codedeploy.ServerDeploymentGroup(self, "DeploymentGroup",
                load_balancer=codedeploy.LoadBalancer.classic(lb)
            )
        '''
        if isinstance(auto_rollback, dict):
            auto_rollback = AutoRollbackConfig(**auto_rollback)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3ad41a581be1a234fd5722299d51aa77bd7beaf51e0511c95ee742d49944018)
            check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
            check_type(argname="argument application", value=application, expected_type=type_hints["application"])
            check_type(argname="argument auto_rollback", value=auto_rollback, expected_type=type_hints["auto_rollback"])
            check_type(argname="argument auto_scaling_groups", value=auto_scaling_groups, expected_type=type_hints["auto_scaling_groups"])
            check_type(argname="argument deployment_config", value=deployment_config, expected_type=type_hints["deployment_config"])
            check_type(argname="argument deployment_group_name", value=deployment_group_name, expected_type=type_hints["deployment_group_name"])
            check_type(argname="argument ec2_instance_tags", value=ec2_instance_tags, expected_type=type_hints["ec2_instance_tags"])
            check_type(argname="argument ignore_poll_alarms_failure", value=ignore_poll_alarms_failure, expected_type=type_hints["ignore_poll_alarms_failure"])
            check_type(argname="argument install_agent", value=install_agent, expected_type=type_hints["install_agent"])
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
            check_type(argname="argument on_premise_instance_tags", value=on_premise_instance_tags, expected_type=type_hints["on_premise_instance_tags"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if alarms is not None:
            self._values["alarms"] = alarms
        if application is not None:
            self._values["application"] = application
        if auto_rollback is not None:
            self._values["auto_rollback"] = auto_rollback
        if auto_scaling_groups is not None:
            self._values["auto_scaling_groups"] = auto_scaling_groups
        if deployment_config is not None:
            self._values["deployment_config"] = deployment_config
        if deployment_group_name is not None:
            self._values["deployment_group_name"] = deployment_group_name
        if ec2_instance_tags is not None:
            self._values["ec2_instance_tags"] = ec2_instance_tags
        if ignore_poll_alarms_failure is not None:
            self._values["ignore_poll_alarms_failure"] = ignore_poll_alarms_failure
        if install_agent is not None:
            self._values["install_agent"] = install_agent
        if load_balancer is not None:
            self._values["load_balancer"] = load_balancer
        if on_premise_instance_tags is not None:
            self._values["on_premise_instance_tags"] = on_premise_instance_tags
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def alarms(self) -> typing.Optional[typing.List[_IAlarm_ff3eabc0]]:
        '''The CloudWatch alarms associated with this Deployment Group.

        CodeDeploy will stop (and optionally roll back)
        a deployment if during it any of the alarms trigger.

        Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method.

        :default: []

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-create-alarms.html
        '''
        result = self._values.get("alarms")
        return typing.cast(typing.Optional[typing.List[_IAlarm_ff3eabc0]], result)

    @builtins.property
    def application(self) -> typing.Optional[IServerApplication]:
        '''The CodeDeploy EC2/on-premise Application this Deployment Group belongs to.

        :default: - A new Application will be created.
        '''
        result = self._values.get("application")
        return typing.cast(typing.Optional[IServerApplication], result)

    @builtins.property
    def auto_rollback(self) -> typing.Optional[AutoRollbackConfig]:
        '''The auto-rollback configuration for this Deployment Group.

        :default: - default AutoRollbackConfig.
        '''
        result = self._values.get("auto_rollback")
        return typing.cast(typing.Optional[AutoRollbackConfig], result)

    @builtins.property
    def auto_scaling_groups(
        self,
    ) -> typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]]:
        '''The auto-scaling groups belonging to this Deployment Group.

        Auto-scaling groups can also be added after the Deployment Group is created
        using the ``#addAutoScalingGroup`` method.

        [disable-awslint:ref-via-interface] is needed because we update userdata
        for ASGs to install the codedeploy agent.

        :default: []
        '''
        result = self._values.get("auto_scaling_groups")
        return typing.cast(typing.Optional[typing.List[_IAutoScalingGroup_360f1cde]], result)

    @builtins.property
    def deployment_config(self) -> typing.Optional[IServerDeploymentConfig]:
        '''The EC2/on-premise Deployment Configuration to use for this Deployment Group.

        :default: ServerDeploymentConfig#OneAtATime
        '''
        result = self._values.get("deployment_config")
        return typing.cast(typing.Optional[IServerDeploymentConfig], result)

    @builtins.property
    def deployment_group_name(self) -> typing.Optional[builtins.str]:
        '''The physical, human-readable name of the CodeDeploy Deployment Group.

        :default: - An auto-generated name will be used.
        '''
        result = self._values.get("deployment_group_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ec2_instance_tags(self) -> typing.Optional[InstanceTagSet]:
        '''All EC2 instances matching the given set of tags when a deployment occurs will be added to this Deployment Group.

        :default: - No additional EC2 instances will be added to the Deployment Group.
        '''
        result = self._values.get("ec2_instance_tags")
        return typing.cast(typing.Optional[InstanceTagSet], result)

    @builtins.property
    def ignore_poll_alarms_failure(self) -> typing.Optional[builtins.bool]:
        '''Whether to continue a deployment even if fetching the alarm status from CloudWatch failed.

        :default: false
        '''
        result = self._values.get("ignore_poll_alarms_failure")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def install_agent(self) -> typing.Optional[builtins.bool]:
        '''If you've provided any auto-scaling groups with the ``#autoScalingGroups`` property, you can set this property to add User Data that installs the CodeDeploy agent on the instances.

        :default: true

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/codedeploy-agent-operations-install.html
        '''
        result = self._values.get("install_agent")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def load_balancer(self) -> typing.Optional[LoadBalancer]:
        '''The load balancer to place in front of this Deployment Group.

        Can be created from either a classic Elastic Load Balancer,
        or an Application Load Balancer / Network Load Balancer Target Group.

        :default: - Deployment Group will not have a load balancer defined.
        '''
        result = self._values.get("load_balancer")
        return typing.cast(typing.Optional[LoadBalancer], result)

    @builtins.property
    def on_premise_instance_tags(self) -> typing.Optional[InstanceTagSet]:
        '''All on-premise instances matching the given set of tags when a deployment occurs will be added to this Deployment Group.

        :default: - No additional on-premise instances will be added to the Deployment Group.
        '''
        result = self._values.get("on_premise_instance_tags")
        return typing.cast(typing.Optional[InstanceTagSet], result)

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The service Role of this Deployment Group.

        :default: - A new Role will be created.
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerDeploymentGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.TimeBasedCanaryTrafficRoutingProps",
    jsii_struct_bases=[BaseTrafficShiftingConfigProps],
    name_mapping={"interval": "interval", "percentage": "percentage"},
)
class TimeBasedCanaryTrafficRoutingProps(BaseTrafficShiftingConfigProps):
    def __init__(
        self,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> None:
        '''Construction properties for ``TimeBasedCanaryTrafficRouting``.

        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.

        :exampleMetadata: infused

        Example::

            config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
                traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                    interval=Duration.minutes(15),
                    percentage=5
                ),
                deployment_config_name="MyDeploymentConfig"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06d16b3e96e0fa33fc82ea5d170af742eef9ed50a9cbf223cb2ed4b3a79e12b0)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "percentage": percentage,
        }

    @builtins.property
    def interval(self) -> _Duration_4839e8c3:
        '''The amount of time between traffic shifts.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage to increase traffic on each traffic shift.'''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeBasedCanaryTrafficRoutingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.TimeBasedLinearTrafficRoutingProps",
    jsii_struct_bases=[BaseTrafficShiftingConfigProps],
    name_mapping={"interval": "interval", "percentage": "percentage"},
)
class TimeBasedLinearTrafficRoutingProps(BaseTrafficShiftingConfigProps):
    def __init__(
        self,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> None:
        '''Construction properties for ``TimeBasedLinearTrafficRouting``.

        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_codedeploy as codedeploy
            
            time_based_linear_traffic_routing_props = codedeploy.TimeBasedLinearTrafficRoutingProps(
                interval=cdk.Duration.minutes(30),
                percentage=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3ae43dc71a0186139db7c80b7def0fee785a31717f8577d65e13a868d2b3817a)
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "interval": interval,
            "percentage": percentage,
        }

    @builtins.property
    def interval(self) -> _Duration_4839e8c3:
        '''The amount of time between traffic shifts.'''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(_Duration_4839e8c3, result)

    @builtins.property
    def percentage(self) -> jsii.Number:
        '''The percentage to increase traffic on each traffic shift.'''
        result = self._values.get("percentage")
        assert result is not None, "Required property 'percentage' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TimeBasedLinearTrafficRoutingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TrafficRouting(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_codedeploy.TrafficRouting",
):
    '''Represents how traffic is shifted during a CodeDeploy deployment.

    :exampleMetadata: infused

    Example::

        config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
            traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                interval=Duration.minutes(15),
                percentage=5
            ),
            deployment_config_name="MyDeploymentConfig"
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="allAtOnce")
    @builtins.classmethod
    def all_at_once(cls) -> "TrafficRouting":
        '''Shifts 100% of traffic in a single shift.'''
        return typing.cast("TrafficRouting", jsii.sinvoke(cls, "allAtOnce", []))

    @jsii.member(jsii_name="timeBasedCanary")
    @builtins.classmethod
    def time_based_canary(
        cls,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> "TrafficRouting":
        '''Shifts a specified percentage of traffic, waits for a specified amount of time, then shifts the rest of traffic.

        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.
        '''
        props = TimeBasedCanaryTrafficRoutingProps(
            interval=interval, percentage=percentage
        )

        return typing.cast("TrafficRouting", jsii.sinvoke(cls, "timeBasedCanary", [props]))

    @jsii.member(jsii_name="timeBasedLinear")
    @builtins.classmethod
    def time_based_linear(
        cls,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> "TrafficRouting":
        '''Keeps shifting a specified percentage of traffic until reaching 100%, waiting for a specified amount of time in between each traffic shift.

        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.
        '''
        props = TimeBasedLinearTrafficRoutingProps(
            interval=interval, percentage=percentage
        )

        return typing.cast("TrafficRouting", jsii.sinvoke(cls, "timeBasedLinear", [props]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "TrafficRoutingConfig":
        '''Returns the traffic routing configuration.

        :param scope: -
        '''
        ...


class _TrafficRoutingProxy(TrafficRouting):
    @jsii.member(jsii_name="bind")
    def bind(self, scope: _constructs_77d1e7e8.Construct) -> "TrafficRoutingConfig":
        '''Returns the traffic routing configuration.

        :param scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd12a268dfe455277ad66728e6406ae5106e0f7beedf165c115e8e39ace124f0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast("TrafficRoutingConfig", jsii.invoke(self, "bind", [scope]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, TrafficRouting).__jsii_proxy_class__ = lambda : _TrafficRoutingProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codedeploy.TrafficRoutingConfig",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "time_based_canary": "timeBasedCanary",
        "time_based_linear": "timeBasedLinear",
    },
)
class TrafficRoutingConfig:
    def __init__(
        self,
        *,
        type: builtins.str,
        time_based_canary: typing.Optional[typing.Union[CanaryTrafficRoutingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        time_based_linear: typing.Optional[typing.Union[LinearTrafficRoutingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Represents the structure to pass into the underlying CfnDeploymentConfig class.

        :param type: The type of traffic shifting ( ``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment configuration.
        :param time_based_canary: A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments. Default: none
        :param time_based_linear: A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in equal increments, with an equal number of minutes between each increment. Default: none

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codedeploy as codedeploy
            
            traffic_routing_config = codedeploy.TrafficRoutingConfig(
                type="type",
            
                # the properties below are optional
                time_based_canary=codedeploy.CanaryTrafficRoutingConfig(
                    canary_interval=123,
                    canary_percentage=123
                ),
                time_based_linear=codedeploy.LinearTrafficRoutingConfig(
                    linear_interval=123,
                    linear_percentage=123
                )
            )
        '''
        if isinstance(time_based_canary, dict):
            time_based_canary = CanaryTrafficRoutingConfig(**time_based_canary)
        if isinstance(time_based_linear, dict):
            time_based_linear = LinearTrafficRoutingConfig(**time_based_linear)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b845a8828051dc720d79c0332ea3470f754dd765be05c704a97b6582380610fb)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument time_based_canary", value=time_based_canary, expected_type=type_hints["time_based_canary"])
            check_type(argname="argument time_based_linear", value=time_based_linear, expected_type=type_hints["time_based_linear"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "type": type,
        }
        if time_based_canary is not None:
            self._values["time_based_canary"] = time_based_canary
        if time_based_linear is not None:
            self._values["time_based_linear"] = time_based_linear

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of traffic shifting ( ``TimeBasedCanary`` or ``TimeBasedLinear`` ) used by a deployment configuration.'''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def time_based_canary(self) -> typing.Optional[CanaryTrafficRoutingConfig]:
        '''A configuration that shifts traffic from one version of a Lambda function or ECS task set to another in two increments.

        :default: none
        '''
        result = self._values.get("time_based_canary")
        return typing.cast(typing.Optional[CanaryTrafficRoutingConfig], result)

    @builtins.property
    def time_based_linear(self) -> typing.Optional[LinearTrafficRoutingConfig]:
        '''A configuration that shifts traffic from one version of a Lambda function or Amazon ECS task set to another in equal increments, with an equal number of minutes between each increment.

        :default: none
        '''
        result = self._values.get("time_based_linear")
        return typing.cast(typing.Optional[LinearTrafficRoutingConfig], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TrafficRoutingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AllAtOnceTrafficRouting(
    TrafficRouting,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.AllAtOnceTrafficRouting",
):
    '''Define a traffic routing config of type 'AllAtOnce'.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codedeploy as codedeploy
        
        all_at_once_traffic_routing = codedeploy.AllAtOnceTrafficRouting.all_at_once()
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _constructs_77d1e7e8.Construct) -> TrafficRoutingConfig:
        '''Return a TrafficRoutingConfig of type ``AllAtOnce``.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f05ebc00e48366a13e2ad293e1822da6d979a050647a74d9f563aab403921d0d)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(TrafficRoutingConfig, jsii.invoke(self, "bind", [_scope]))


@jsii.implements(IBaseDeploymentConfig)
class BaseDeploymentConfig(
    _Resource_45bc6135,
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_codedeploy.BaseDeploymentConfig",
):
    '''The base class for ServerDeploymentConfig, EcsDeploymentConfig, and LambdaDeploymentConfig deployment configurations.

    :resource: AWS::CodeDeploy::DeploymentConfig
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compute_platform: typing.Optional[ComputePlatform] = None,
        minimum_healthy_hosts: typing.Optional[MinimumHealthyHosts] = None,
        traffic_routing: typing.Optional[TrafficRouting] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param compute_platform: The destination compute platform for the deployment. Default: ComputePlatform.Server
        :param minimum_healthy_hosts: Minimum number of healthy hosts. Default: None
        :param traffic_routing: The configuration that specifies how traffic is shifted during a deployment. Only applicable to ECS and Lambda deployments, and must not be specified for Server deployments. Default: None
        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7be4ac008b1dbe1f91bb986ac7bb32dd779f4962b7a7696d9064b17fa3e5e35)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = BaseDeploymentConfigProps(
            compute_platform=compute_platform,
            minimum_healthy_hosts=minimum_healthy_hosts,
            traffic_routing=traffic_routing,
            deployment_config_name=deployment_config_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDeploymentConfigName")
    @builtins.classmethod
    def from_deployment_config_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        deployment_config_name: builtins.str,
    ) -> IBaseDeploymentConfig:
        '''Import a custom Deployment Configuration for a Deployment Group defined outside the CDK.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param deployment_config_name: the name of the referenced custom Deployment Configuration.

        :return: a Construct representing a reference to an existing custom Deployment Configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f696afb42fc23d24c96d39b2254f0b625ecbfacca97da38df5ba1831b8c62a53)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument deployment_config_name", value=deployment_config_name, expected_type=type_hints["deployment_config_name"])
        return typing.cast(IBaseDeploymentConfig, jsii.sinvoke(cls, "fromDeploymentConfigName", [scope, id, deployment_config_name]))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        '''The arn of the deployment config.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        '''The name of the deployment config.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))


class _BaseDeploymentConfigProxy(
    BaseDeploymentConfig,
    jsii.proxy_for(_Resource_45bc6135), # type: ignore[misc]
):
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, BaseDeploymentConfig).__jsii_proxy_class__ = lambda : _BaseDeploymentConfigProxy


@jsii.implements(ILambdaDeploymentConfig)
class CustomLambdaDeploymentConfig(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.CustomLambdaDeploymentConfig",
):
    '''(deprecated) A custom Deployment Configuration for a Lambda Deployment Group.

    :deprecated: CloudFormation now supports Lambda deployment configurations without custom resources. Use ``LambdaDeploymentConfig``.

    :stability: deprecated
    :resource: AWS::CodeDeploy::DeploymentGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_codedeploy as codedeploy
        
        custom_lambda_deployment_config = codedeploy.CustomLambdaDeploymentConfig(self, "MyCustomLambdaDeploymentConfig",
            interval=cdk.Duration.minutes(30),
            percentage=123,
            type=codedeploy.CustomLambdaDeploymentConfigType.CANARY,
        
            # the properties below are optional
            deployment_config_name="deploymentConfigName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
        type: CustomLambdaDeploymentConfigType,
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param interval: (deprecated) The interval, in number of minutes: - For LINEAR, how frequently additional traffic is shifted - For CANARY, how long to shift traffic before the full deployment.
        :param percentage: (deprecated) The integer percentage of traffic to shift: - For LINEAR, the percentage to shift every interval - For CANARY, the percentage to shift until the interval passes, before the full deployment.
        :param type: (deprecated) The type of deployment config, either CANARY or LINEAR.
        :param deployment_config_name: (deprecated) The verbatim name of the deployment config. Must be unique per account/region. Other parameters cannot be updated if this name is provided. Default: - automatically generated name

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ac867d6e5022c0be7de76fadf84363729e8cfde59c1d36f19b324981b6e8053)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CustomLambdaDeploymentConfigProps(
            interval=interval,
            percentage=percentage,
            type=type,
            deployment_config_name=deployment_config_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigArn")
    def deployment_config_arn(self) -> builtins.str:
        '''(deprecated) The arn of the deployment config.

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfigName")
    def deployment_config_name(self) -> builtins.str:
        '''(deprecated) The name of the deployment config.

        :deprecated: Use ``LambdaDeploymentConfig``

        :stability: deprecated
        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "deploymentConfigName"))


@jsii.implements(IEcsApplication)
class EcsApplication(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsApplication",
):
    '''A CodeDeploy Application that deploys to an Amazon ECS service.

    :resource: AWS::CodeDeploy::Application
    :exampleMetadata: infused

    Example::

        application = codedeploy.EcsApplication(self, "CodeDeployApplication",
            application_name="MyApplication"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param application_name: The physical, human-readable name of the CodeDeploy Application. Default: an auto-generated name will be used
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4edf5fb61452170b1877882129fc1df2e63797e3a9f6b183813f1e20bf3b8854)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsApplicationProps(application_name=application_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEcsApplicationArn")
    @builtins.classmethod
    def from_ecs_application_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        ecs_application_arn: builtins.str,
    ) -> IEcsApplication:
        '''Import an Application defined either outside the CDK, or in a different CDK Stack, by ARN.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param ecs_application_arn: the ARN of the application to import.

        :return: a Construct representing a reference to an existing Application
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a15b4054e084bc53dcd5e21cbb4878436d9d1074cc50177d7007d7382b209c85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ecs_application_arn", value=ecs_application_arn, expected_type=type_hints["ecs_application_arn"])
        return typing.cast(IEcsApplication, jsii.sinvoke(cls, "fromEcsApplicationArn", [scope, id, ecs_application_arn]))

    @jsii.member(jsii_name="fromEcsApplicationName")
    @builtins.classmethod
    def from_ecs_application_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        ecs_application_name: builtins.str,
    ) -> IEcsApplication:
        '''Import an Application defined either outside the CDK, or in a different CDK Stack.

        The Application's account and region are assumed to be the same as the stack it is being imported
        into. If not, use ``fromEcsApplicationArn``.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param ecs_application_name: the name of the application to import.

        :return: a Construct representing a reference to an existing Application
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10762c159701d6da1d6d041f0ac41aba5c82b3d604e4bad2002ef52f91f66339)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ecs_application_name", value=ecs_application_name, expected_type=type_hints["ecs_application_name"])
        return typing.cast(IEcsApplication, jsii.sinvoke(cls, "fromEcsApplicationName", [scope, id, ecs_application_name]))

    @builtins.property
    @jsii.member(jsii_name="applicationArn")
    def application_arn(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationArn"))

    @builtins.property
    @jsii.member(jsii_name="applicationName")
    def application_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "applicationName"))


@jsii.implements(IEcsDeploymentConfig)
class EcsDeploymentConfig(
    BaseDeploymentConfig,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsDeploymentConfig",
):
    '''A custom Deployment Configuration for an ECS Deployment Group.

    :resource: AWS::CodeDeploy::DeploymentConfig
    :exampleMetadata: infused

    Example::

        # service: ecs.FargateService
        # blue_target_group: elbv2.ITargetGroup
        # green_target_group: elbv2.ITargetGroup
        # listener: elbv2.IApplicationListener
        # test_listener: elbv2.IApplicationListener
        
        
        codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
            auto_rollback=codedeploy.AutoRollbackConfig(
                # CodeDeploy will automatically roll back if the 8-hour approval period times out and the deployment stops
                stopped_deployment=True
            ),
            service=service,
            blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
                # The deployment will wait for approval for up to 8 hours before stopping the deployment
                deployment_approval_wait_time=Duration.hours(8),
                blue_target_group=blue_target_group,
                green_target_group=green_target_group,
                listener=listener,
                test_listener=test_listener
            ),
            deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        traffic_routing: typing.Optional[TrafficRouting] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param traffic_routing: The configuration that specifies how traffic is shifted from the 'blue' target group to the 'green' target group during a deployment. Default: AllAtOnce
        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2d7f681f3251c7de51922fccb03d9839dc0514700deb88855b4a1e3e089d308)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsDeploymentConfigProps(
            traffic_routing=traffic_routing,
            deployment_config_name=deployment_config_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEcsDeploymentConfigName")
    @builtins.classmethod
    def from_ecs_deployment_config_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        ecs_deployment_config_name: builtins.str,
    ) -> IEcsDeploymentConfig:
        '''Import a custom Deployment Configuration for an ECS Deployment Group defined outside the CDK.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param ecs_deployment_config_name: the name of the referenced custom Deployment Configuration.

        :return: a Construct representing a reference to an existing custom Deployment Configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99681a26417ad9494dc9331a9865e7f0cf7cb6ec84094cf3b3a4888af4a81b06)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument ecs_deployment_config_name", value=ecs_deployment_config_name, expected_type=type_hints["ecs_deployment_config_name"])
        return typing.cast(IEcsDeploymentConfig, jsii.sinvoke(cls, "fromEcsDeploymentConfigName", [scope, id, ecs_deployment_config_name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> IEcsDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts all traffic to the updated ECS task set at once.'''
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "ALL_AT_ONCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_15MINUTES")
    def CANARY_10_PERCENT_15_MINUTES(cls) -> IEcsDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic in the first increment.

        The remaining 90 percent is deployed 15 minutes later.
        '''
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_15MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_5MINUTES")
    def CANARY_10_PERCENT_5_MINUTES(cls) -> IEcsDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic in the first increment.

        The remaining 90 percent is deployed five minutes later.
        '''
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_5MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_1MINUTES")
    def LINEAR_10_PERCENT_EVERY_1_MINUTES(cls) -> IEcsDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic every minute until all traffic is shifted.'''
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_1MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_3MINUTES")
    def LINEAR_10_PERCENT_EVERY_3_MINUTES(cls) -> IEcsDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic every three minutes until all traffic is shifted.'''
        return typing.cast(IEcsDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_3MINUTES"))


@jsii.implements(IEcsDeploymentGroup)
class EcsDeploymentGroup(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.EcsDeploymentGroup",
):
    '''A CodeDeploy deployment group that orchestrates ECS blue-green deployments.

    :resource: AWS::CodeDeploy::DeploymentGroup
    :exampleMetadata: infused

    Example::

        # my_application: codedeploy.EcsApplication
        # cluster: ecs.Cluster
        # task_definition: ecs.FargateTaskDefinition
        # blue_target_group: elbv2.ITargetGroup
        # green_target_group: elbv2.ITargetGroup
        # listener: elbv2.IApplicationListener
        
        
        service = ecs.FargateService(self, "Service",
            cluster=cluster,
            task_definition=task_definition,
            deployment_controller=ecs.DeploymentController(
                type=ecs.DeploymentControllerType.CODE_DEPLOY
            )
        )
        
        codedeploy.EcsDeploymentGroup(self, "BlueGreenDG",
            service=service,
            blue_green_deployment_config=codedeploy.EcsBlueGreenDeploymentConfig(
                blue_target_group=blue_target_group,
                green_target_group=green_target_group,
                listener=listener
            ),
            deployment_config=codedeploy.EcsDeploymentConfig.CANARY_10PERCENT_5MINUTES
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        blue_green_deployment_config: typing.Union[EcsBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]],
        service: _IBaseService_3fcdd913,
        alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
        application: typing.Optional[IEcsApplication] = None,
        auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
        deployment_group_name: typing.Optional[builtins.str] = None,
        ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param blue_green_deployment_config: The configuration options for blue-green ECS deployments.
        :param service: The ECS service to deploy with this Deployment Group.
        :param alarms: The CloudWatch alarms associated with this Deployment Group. CodeDeploy will stop (and optionally roll back) a deployment if during it any of the alarms trigger. Alarms can also be added after the Deployment Group is created using the ``#addAlarm`` method. Default: []
        :param application: The reference to the CodeDeploy ECS Application that this Deployment Group belongs to. Default: One will be created for you.
        :param auto_rollback: The auto-rollback configuration for this Deployment Group. Default: - default AutoRollbackConfig.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: EcsDeploymentConfig.ALL_AT_ONCE
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy Deployment Group. Default: An auto-generated name will be used.
        :param ignore_poll_alarms_failure: Whether to continue a deployment even if fetching the alarm status from CloudWatch failed. Default: false
        :param role: The service Role of this Deployment Group. Default: - A new Role will be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d5a27f58faebed8ad465b39d408bd717722f646f6471896e02b8ea95b82bc49)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EcsDeploymentGroupProps(
            blue_green_deployment_config=blue_green_deployment_config,
            service=service,
            alarms=alarms,
            application=application,
            auto_rollback=auto_rollback,
            deployment_config=deployment_config,
            deployment_group_name=deployment_group_name,
            ignore_poll_alarms_failure=ignore_poll_alarms_failure,
            role=role,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEcsDeploymentGroupAttributes")
    @builtins.classmethod
    def from_ecs_deployment_group_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application: IEcsApplication,
        deployment_group_name: builtins.str,
        deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
    ) -> IEcsDeploymentGroup:
        '''Reference an ECS Deployment Group defined outside the CDK app.

        Account and region for the DeploymentGroup are taken from the application.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param application: The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.
        :param deployment_group_name: The physical, human-readable name of the CodeDeploy ECS Deployment Group that we are referencing.
        :param deployment_config: The Deployment Configuration this Deployment Group uses. Default: EcsDeploymentConfig.ALL_AT_ONCE

        :return: a Construct representing a reference to an existing Deployment Group
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21d5d2081ae62e02eb318efb6845c80afcd2a31d1f65949b88d5e28b3887b2f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = EcsDeploymentGroupAttributes(
            application=application,
            deployment_group_name=deployment_group_name,
            deployment_config=deployment_config,
        )

        return typing.cast(IEcsDeploymentGroup, jsii.sinvoke(cls, "fromEcsDeploymentGroupAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="addAlarm")
    def add_alarm(self, alarm: _IAlarm_ff3eabc0) -> None:
        '''Associates an additional alarm with this Deployment Group.

        :param alarm: the alarm to associate with this Deployment Group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecbfe2758d485b20b4d7753475293fc67c26edc4d904112e8a409df22ce5f06c)
            check_type(argname="argument alarm", value=alarm, expected_type=type_hints["alarm"])
        return typing.cast(None, jsii.invoke(self, "addAlarm", [alarm]))

    @builtins.property
    @jsii.member(jsii_name="application")
    def application(self) -> IEcsApplication:
        '''The reference to the CodeDeploy ECS Application that this Deployment Group belongs to.'''
        return typing.cast(IEcsApplication, jsii.get(self, "application"))

    @builtins.property
    @jsii.member(jsii_name="deploymentConfig")
    def deployment_config(self) -> IEcsDeploymentConfig:
        '''The Deployment Configuration this Group uses.'''
        return typing.cast(IEcsDeploymentConfig, jsii.get(self, "deploymentConfig"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupArn")
    def deployment_group_arn(self) -> builtins.str:
        '''The ARN of the Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="deploymentGroupName")
    def deployment_group_name(self) -> builtins.str:
        '''The name of the Deployment Group.'''
        return typing.cast(builtins.str, jsii.get(self, "deploymentGroupName"))

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> _IRole_235f5d8e:
        '''The service Role of this Deployment Group.'''
        return typing.cast(_IRole_235f5d8e, jsii.get(self, "role"))


@jsii.implements(ILambdaDeploymentConfig)
class LambdaDeploymentConfig(
    BaseDeploymentConfig,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.LambdaDeploymentConfig",
):
    '''A custom Deployment Configuration for a Lambda Deployment Group.

    :resource: AWS::CodeDeploy::DeploymentConfig
    :exampleMetadata: infused

    Example::

        # application: codedeploy.LambdaApplication
        # alias: lambda.Alias
        config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
            traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                interval=Duration.minutes(15),
                percentage=5
            )
        )
        deployment_group = codedeploy.LambdaDeploymentGroup(self, "BlueGreenDeployment",
            application=application,
            alias=alias,
            deployment_config=config
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        traffic_routing: typing.Optional[TrafficRouting] = None,
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param traffic_routing: The configuration that specifies how traffic is shifted from the 'blue' target group to the 'green' target group during a deployment. Default: AllAtOnce
        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5058ddee6c11563a4a133d87a712b18e3c1621329942e72104da625c5e6242b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = LambdaDeploymentConfigProps(
            traffic_routing=traffic_routing,
            deployment_config_name=deployment_config_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromLambdaDeploymentConfigName")
    @builtins.classmethod
    def from_lambda_deployment_config_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        lambda_deployment_config_name: builtins.str,
    ) -> ILambdaDeploymentConfig:
        '''Import a Deployment Configuration for a Lambda Deployment Group defined outside the CDK.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param lambda_deployment_config_name: the name of the Lambda Deployment Configuration to import.

        :return: a Construct representing a reference to an existing Lambda Deployment Configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98c000174f0f5fb89592424d7fb95552d79f3a850e96cfda07890bde08230908)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument lambda_deployment_config_name", value=lambda_deployment_config_name, expected_type=type_hints["lambda_deployment_config_name"])
        return typing.cast(ILambdaDeploymentConfig, jsii.sinvoke(cls, "fromLambdaDeploymentConfigName", [scope, id, lambda_deployment_config_name]))

    @jsii.member(jsii_name="import")
    @builtins.classmethod
    def import_(
        cls,
        _scope: _constructs_77d1e7e8.Construct,
        _id: builtins.str,
        *,
        deployment_config_name: builtins.str,
    ) -> ILambdaDeploymentConfig:
        '''(deprecated) Import a Deployment Configuration for a Lambda Deployment Group defined outside the CDK.

        :param _scope: the parent Construct for this new Construct.
        :param _id: the logical ID of this new Construct.
        :param deployment_config_name: The physical, human-readable name of the custom CodeDeploy Lambda Deployment Configuration that we are referencing.

        :return: a Construct representing a reference to an existing custom Deployment Configuration

        :deprecated: use ``fromLambdaDeploymentConfigName``

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1505251b6329a0bcb03ec5f5656f675b1c5236b529a51019e64f1fee9d98cdb6)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _id", value=_id, expected_type=type_hints["_id"])
        props = LambdaDeploymentConfigImportProps(
            deployment_config_name=deployment_config_name
        )

        return typing.cast(ILambdaDeploymentConfig, jsii.sinvoke(cls, "import", [_scope, _id, props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts all traffic to the updated Lambda function at once.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "ALL_AT_ONCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_10MINUTES")
    def CANARY_10_PERCENT_10_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic in the first increment.

        The remaining 90 percent is deployed 10 minutes later.
        '''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_10MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_15MINUTES")
    def CANARY_10_PERCENT_15_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic in the first increment.

        The remaining 90 percent is deployed 15 minutes later.
        '''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_15MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_30MINUTES")
    def CANARY_10_PERCENT_30_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic in the first increment.

        The remaining 90 percent is deployed 30 minutes later.
        '''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_30MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CANARY_10PERCENT_5MINUTES")
    def CANARY_10_PERCENT_5_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic in the first increment.

        The remaining 90 percent is deployed five minutes later.
        '''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "CANARY_10PERCENT_5MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_10MINUTES")
    def LINEAR_10_PERCENT_EVERY_10_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic every 10 minutes until all traffic is shifted.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_10MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_1MINUTE")
    def LINEAR_10_PERCENT_EVERY_1_MINUTE(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic every minute until all traffic is shifted.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_1MINUTE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_2MINUTES")
    def LINEAR_10_PERCENT_EVERY_2_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic every two minutes until all traffic is shifted.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_2MINUTES"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="LINEAR_10PERCENT_EVERY_3MINUTES")
    def LINEAR_10_PERCENT_EVERY_3_MINUTES(cls) -> ILambdaDeploymentConfig:
        '''CodeDeploy predefined deployment configuration that shifts 10 percent of traffic every three minutes until all traffic is shifted.'''
        return typing.cast(ILambdaDeploymentConfig, jsii.sget(cls, "LINEAR_10PERCENT_EVERY_3MINUTES"))


@jsii.implements(IServerDeploymentConfig)
class ServerDeploymentConfig(
    BaseDeploymentConfig,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.ServerDeploymentConfig",
):
    '''A custom Deployment Configuration for an EC2/on-premise Deployment Group.

    :resource: AWS::CodeDeploy::DeploymentConfig
    :exampleMetadata: infused

    Example::

        deployment_group = codedeploy.ServerDeploymentGroup(self, "CodeDeployDeploymentGroup",
            deployment_config=codedeploy.ServerDeploymentConfig.ALL_AT_ONCE
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        minimum_healthy_hosts: MinimumHealthyHosts,
        deployment_config_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param minimum_healthy_hosts: Minimum number of healthy hosts.
        :param deployment_config_name: The physical, human-readable name of the Deployment Configuration. Default: - automatically generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0188bedb6550f8f8ec5175aae5830d1c200a93e114c45fc9d6b3942b7d6123a7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ServerDeploymentConfigProps(
            minimum_healthy_hosts=minimum_healthy_hosts,
            deployment_config_name=deployment_config_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromServerDeploymentConfigName")
    @builtins.classmethod
    def from_server_deployment_config_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        server_deployment_config_name: builtins.str,
    ) -> IServerDeploymentConfig:
        '''Import a custom Deployment Configuration for an EC2/on-premise Deployment Group defined either outside the CDK app, or in a different region.

        :param scope: the parent Construct for this new Construct.
        :param id: the logical ID of this new Construct.
        :param server_deployment_config_name: the properties of the referenced custom Deployment Configuration.

        :return: a Construct representing a reference to an existing custom Deployment Configuration
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0ea4e0fbba82ec61d62008656825ba154d6ab7a16569e404ef56dd5d012b2d4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument server_deployment_config_name", value=server_deployment_config_name, expected_type=type_hints["server_deployment_config_name"])
        return typing.cast(IServerDeploymentConfig, jsii.sinvoke(cls, "fromServerDeploymentConfigName", [scope, id, server_deployment_config_name]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ALL_AT_ONCE")
    def ALL_AT_ONCE(cls) -> IServerDeploymentConfig:
        '''The CodeDeployDefault.AllAtOnce predefined deployment configuration for EC2/on-premises compute platform.

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html#deployment-configuration-server
        '''
        return typing.cast(IServerDeploymentConfig, jsii.sget(cls, "ALL_AT_ONCE"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="HALF_AT_A_TIME")
    def HALF_AT_A_TIME(cls) -> IServerDeploymentConfig:
        '''The CodeDeployDefault.HalfAtATime predefined deployment configuration for EC2/on-premises compute platform.

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html#deployment-configuration-server
        '''
        return typing.cast(IServerDeploymentConfig, jsii.sget(cls, "HALF_AT_A_TIME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="ONE_AT_A_TIME")
    def ONE_AT_A_TIME(cls) -> IServerDeploymentConfig:
        '''The CodeDeployDefault.OneAtATime predefined deployment configuration for EC2/on-premises compute platform.

        :see: https://docs.aws.amazon.com/codedeploy/latest/userguide/deployment-configurations.html#deployment-configuration-server
        '''
        return typing.cast(IServerDeploymentConfig, jsii.sget(cls, "ONE_AT_A_TIME"))


class TimeBasedCanaryTrafficRouting(
    TrafficRouting,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.TimeBasedCanaryTrafficRouting",
):
    '''Define a traffic routing config of type 'TimeBasedCanary'.

    :exampleMetadata: infused

    Example::

        config = codedeploy.LambdaDeploymentConfig(self, "CustomConfig",
            traffic_routing=codedeploy.TimeBasedCanaryTrafficRouting(
                interval=Duration.minutes(15),
                percentage=5
            ),
            deployment_config_name="MyDeploymentConfig"
        )
    '''

    def __init__(
        self,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> None:
        '''
        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.
        '''
        props = TimeBasedCanaryTrafficRoutingProps(
            interval=interval, percentage=percentage
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _constructs_77d1e7e8.Construct) -> TrafficRoutingConfig:
        '''Return a TrafficRoutingConfig of type ``TimeBasedCanary``.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f62d359f751a6aad86ee02e74d93fa8692f764928aa7fa26224cb9b7679affc8)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(TrafficRoutingConfig, jsii.invoke(self, "bind", [_scope]))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> _Duration_4839e8c3:
        '''The amount of time between additional traffic shifts.'''
        return typing.cast(_Duration_4839e8c3, jsii.get(self, "interval"))

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        '''The percentage to increase traffic on each traffic shift.'''
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))


class TimeBasedLinearTrafficRouting(
    TrafficRouting,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codedeploy.TimeBasedLinearTrafficRouting",
):
    '''Define a traffic routing config of type 'TimeBasedLinear'.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codedeploy as codedeploy
        
        time_based_linear_traffic_routing = codedeploy.TimeBasedLinearTrafficRouting.all_at_once()
    '''

    def __init__(
        self,
        *,
        interval: _Duration_4839e8c3,
        percentage: jsii.Number,
    ) -> None:
        '''
        :param interval: The amount of time between traffic shifts.
        :param percentage: The percentage to increase traffic on each traffic shift.
        '''
        props = TimeBasedLinearTrafficRoutingProps(
            interval=interval, percentage=percentage
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(self, _scope: _constructs_77d1e7e8.Construct) -> TrafficRoutingConfig:
        '''Return a TrafficRoutingConfig of type ``TimeBasedLinear``.

        :param _scope: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa5564b995bb046b6d26e38cc462ee09779219878f550d6e7a210ed2d50a5b84)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
        return typing.cast(TrafficRoutingConfig, jsii.invoke(self, "bind", [_scope]))

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> _Duration_4839e8c3:
        '''The amount of time between additional traffic shifts.'''
        return typing.cast(_Duration_4839e8c3, jsii.get(self, "interval"))

    @builtins.property
    @jsii.member(jsii_name="percentage")
    def percentage(self) -> jsii.Number:
        '''The percentage to increase traffic on each traffic shift.'''
        return typing.cast(jsii.Number, jsii.get(self, "percentage"))


__all__ = [
    "AllAtOnceTrafficRouting",
    "AutoRollbackConfig",
    "BaseDeploymentConfig",
    "BaseDeploymentConfigOptions",
    "BaseDeploymentConfigProps",
    "BaseTrafficShiftingConfigProps",
    "CanaryTrafficRoutingConfig",
    "CfnApplication",
    "CfnApplicationProps",
    "CfnDeploymentConfig",
    "CfnDeploymentConfigProps",
    "CfnDeploymentGroup",
    "CfnDeploymentGroupProps",
    "ComputePlatform",
    "CustomLambdaDeploymentConfig",
    "CustomLambdaDeploymentConfigProps",
    "CustomLambdaDeploymentConfigType",
    "EcsApplication",
    "EcsApplicationProps",
    "EcsBlueGreenDeploymentConfig",
    "EcsDeploymentConfig",
    "EcsDeploymentConfigProps",
    "EcsDeploymentGroup",
    "EcsDeploymentGroupAttributes",
    "EcsDeploymentGroupProps",
    "IBaseDeploymentConfig",
    "IEcsApplication",
    "IEcsDeploymentConfig",
    "IEcsDeploymentGroup",
    "ILambdaApplication",
    "ILambdaDeploymentConfig",
    "ILambdaDeploymentGroup",
    "IServerApplication",
    "IServerDeploymentConfig",
    "IServerDeploymentGroup",
    "InstanceTagSet",
    "LambdaApplication",
    "LambdaApplicationProps",
    "LambdaDeploymentConfig",
    "LambdaDeploymentConfigImportProps",
    "LambdaDeploymentConfigProps",
    "LambdaDeploymentGroup",
    "LambdaDeploymentGroupAttributes",
    "LambdaDeploymentGroupProps",
    "LinearTrafficRoutingConfig",
    "LoadBalancer",
    "LoadBalancerGeneration",
    "MinimumHealthyHosts",
    "ServerApplication",
    "ServerApplicationProps",
    "ServerDeploymentConfig",
    "ServerDeploymentConfigProps",
    "ServerDeploymentGroup",
    "ServerDeploymentGroupAttributes",
    "ServerDeploymentGroupProps",
    "TimeBasedCanaryTrafficRouting",
    "TimeBasedCanaryTrafficRoutingProps",
    "TimeBasedLinearTrafficRouting",
    "TimeBasedLinearTrafficRoutingProps",
    "TrafficRouting",
    "TrafficRoutingConfig",
]

publication.publish()

def _typecheckingstub__689450aae2d9ca9a482d433f9f5a1fc7e3667c388258352cecb6392405eed69a(
    *,
    deployment_in_alarm: typing.Optional[builtins.bool] = None,
    failed_deployment: typing.Optional[builtins.bool] = None,
    stopped_deployment: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05a78df220a94eafb19c1fb09bf8cd1183e1f0942b3041c0d3aed8a339fd8ada(
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d482592e3c5f65fb9559b3e230fe81eab72a36fdd6c5a5b3cad1b4206b327f9f(
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
    compute_platform: typing.Optional[ComputePlatform] = None,
    minimum_healthy_hosts: typing.Optional[MinimumHealthyHosts] = None,
    traffic_routing: typing.Optional[TrafficRouting] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d5ec69046dd60e940973497323ace19e7ca99f17fbf8c276127a2f0ac4bce26(
    *,
    interval: _Duration_4839e8c3,
    percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b220d2e40da00bdd6575561fd7cdb02d36ddf0940793b63fdbd380655db12905(
    *,
    canary_interval: jsii.Number,
    canary_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdb5a43a5eee290cb73c7a01531e1ffdf06d171c94caaa945bee8063be1b20cb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: typing.Optional[builtins.str] = None,
    compute_platform: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472dad38d3229c543cd45d013c4792382a9a9ff72b6a1c296cd46ddee9866459(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a41fadf993de0854abe41941db98e76215ad0ec2ffd27ae1223e12e06bacf4c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__728dce9dc041502139649117dd6edec48c37d9c568f82ee3be92de1b22e2d700(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1915728b28efc5c1d28ee6eddc170806e157b6c8dea55af22c18fe4e3b4ac191(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b760e30495233c290b05641b219df0417ec34a7cdcb66209b76925733db09c3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3aeaaf4451457e6e36767224eb97c6e700e8d8faacb23edf47d5dd4c18588590(
    *,
    application_name: typing.Optional[builtins.str] = None,
    compute_platform: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1601263a429a6a400738eca0c5abc3bd436649919830aa684054ba853d401c1f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compute_platform: typing.Optional[builtins.str] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
    minimum_healthy_hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de25cf19eea9e6556b0b2281a81290d8a5bf22139c91cc21523d85735c1acaa3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f45dd75f7b342e01e5b93540f71f720aa8d7caaf6291470bbe12a5b6f3885e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fccd76b57c8ae8e5170ce23818cd0a34ba59302c6ce3d4c180222152061e2922(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2be2e5144bd03df4a4fa40048f27e95c3e5304df13985412b42828a3a74d0e4d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a51d4f90c94e060ed843233d31547707cbf9d10d3d4de60cd6205bda621edc94(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentConfig.MinimumHealthyHostsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe1bae2a6b88ba41a47472dc8dc7bbf6f72bde54b89b4ed3b8f8e3fd35645ce4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentConfig.TrafficRoutingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__564f19ccdd0db2b16c3c238ca2a96b350c9884c519827c6fb91e0d1d234c91d7(
    *,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4bcdd7787167974941b5c2516ab391320979aae485b7c1b94a03555868b2102(
    *,
    canary_interval: jsii.Number,
    canary_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2df4e7a87402b186b362bc4d946424539c4a60d7802ac7dcc0731829bf567cb(
    *,
    linear_interval: jsii.Number,
    linear_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b1a59608913355745ad3536a5af2b299b48dfb68b88ee15dd0c479874845c5a(
    *,
    type: builtins.str,
    time_based_canary: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.TimeBasedCanaryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    time_based_linear: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.TimeBasedLinearProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50cfbd3bc3fca6105506273e4e48e992de4fbb025dced2c525ba1da4bacaadb(
    *,
    compute_platform: typing.Optional[builtins.str] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
    minimum_healthy_hosts: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.MinimumHealthyHostsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    traffic_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentConfig.TrafficRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afc1bc74c13d6392d70ae9e55ed64b8ec6f2cfed100b230e370997efe94283fc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: builtins.str,
    service_role_arn: builtins.str,
    alarm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AlarmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_rollback_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AutoRollbackConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_scaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    blue_green_deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    deployment_style: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentStyleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ec2_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ecs_services: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.ECSServiceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    load_balancer_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.LoadBalancerInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    on_premises_instance_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    on_premises_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.OnPremisesTagSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outdated_instances_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trigger_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3307a6c43ea08ab3400b7fc835536202e54b37286849aee24bbada2786dd74cf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1713bf55d2b8953310377b4afb89de903e08433197c638276d6cc30c5d16e48d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb70a956898eec48889a079260c8cc973bf43c5f7612ee24bff5dbbbf459fe5(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66b7f059438dd5722aa9d8f744a278bc5625386e8ce3d4fc1eb8a281e2f306c2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e91a52d4fd08a0b9deb3baefb2ccf408f0cb24c44a56893da4cb20fc1d8c83c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.AlarmConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69accffcb10c8665244d6da2f6e58570690d0e957e337792a901cb7be04905b7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.AutoRollbackConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e04b36b090b14ba34ad491347fe2aca8d51c1e1877ebf2c7e060f1741102a50(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e01bb8b0c5b5d341a669261e31783fa832409200e3eb8a634fe33223a72f7306(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08845fc7de26e5f1faa42234a437c12699ffe9eb475932cf303f7acd1c272595(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.DeploymentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a74c90812b52cdad890ecf4f6486df9ad8780f8c6a1c163cd9479e4971f08402(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e42dd2dab2a2d9e3bc41f1ad0d0e48a8811bc6c996da34cbbfacc9757b3286d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf1c6eb87ee1012ff4d9949ecda81e6dcac87415f749d230c6ee6752153ec80(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.DeploymentStyleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee79962691a5c39e41198cbe8d3feba8224218b0f0150b5f282db760c6c767ab(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.EC2TagFilterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6196a4cb27800772b6bd881880397500b9e720f740bb7b6289f13d2f51e04863(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.EC2TagSetProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e313b8ad9be6363e7a8552e9cf937d4c0cf7ff77b9f105105f6b3bab3b53c6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.ECSServiceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f10ac10d280e8586e5bdb5699bdb0c53aab83965020339a2a5611d15d4061e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.LoadBalancerInfoProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f88440801309d20e368d659f0132d109e5c37cb01b5a5f894053f4f9081f75f1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.TagFilterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1da01bcd68da7d01c5ffa220e48c83cd4d65bd034d7416a79c12856e9a25fad(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.OnPremisesTagSetProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9af30b6e3ffc37ae09bbaa003b72063af09adae4e47a022a24f8e942d28ea799(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca51d486320d92369410ca709970091be367eabeebde41a60143404eeb1cc6a8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19f14404bcc2f5c2897842d997eb29c01baf8bcd6619fdc09e6b87d0df1f7693(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDeploymentGroup.TriggerConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9049a177037c3e8ef4e71b7faa8d7ccdc08bd8b6c11e4af29269d336bc4d6f(
    *,
    alarms: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AlarmProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ignore_poll_alarm_failure: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03e2a9b2ed59c3404f1d3022f2f33080db793f19b46ee08a71091c574e4f91bf(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a36fa5e61b5cc5a6cdc586ebcdd6624cb49131a6f67b88c2c5bcf44e6a75371f(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    events: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7f7b94df2ec70381780abbf295dc60aec98ca6cee8249a44d4e591068ed620(
    *,
    deployment_ready_option: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentReadyOptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    green_fleet_provisioning_option: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.GreenFleetProvisioningOptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    terminate_blue_instances_on_deployment_success: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.BlueInstanceTerminationOptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace1975d2c13f6a63616292118c632b714e3f1acc2008b3030af06cf79e1b5e0(
    *,
    action: typing.Optional[builtins.str] = None,
    termination_wait_time_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8d7106fc8a20bc76da89cc9e6f595c31863f43d9fa4324b6eb51a8bc1dada19(
    *,
    revision: typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.RevisionLocationProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    ignore_application_stop_failures: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9191e174499f04c901c65523928f85f4ae3a2b619e5821f1dcd040efd65da4d6(
    *,
    action_on_timeout: typing.Optional[builtins.str] = None,
    wait_time_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6043290c4b631767b4c4d436c6262f5d79a876cdc721342d1ef120eda81d2060(
    *,
    deployment_option: typing.Optional[builtins.str] = None,
    deployment_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b4123febfdeb60265474ec5b72d4ed596f0cc20f7693da9000b91cc6f3c79da(
    *,
    key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fff319f820316a004ead743ff5c8ad36448e48325ee845cbff5fcfd512773f6c(
    *,
    ec2_tag_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2ba29487a84183313e702cd8e61c88a4f0351eb6fd78f229d2580ae39e8e3e0(
    *,
    ec2_tag_set_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagSetListObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c6525e95eaf4a440450af5d2e22a53ae3b16a83e28290e48e8aaeda963614fc(
    *,
    cluster_name: builtins.str,
    service_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e1b138b2ef18765e84f9ebeee5de46f0b1d44931eeb67199e9796e5085caa7f(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed147000e92beb1f04d3f0454dc3a873381abc78c1a6b36b05a6e71f1e816253(
    *,
    commit_id: builtins.str,
    repository: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e876af08ef6424feae19da396da079af3de5bc150f304e98d88f569bd98449dc(
    *,
    action: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3433798b0214903267b0b0c3d8bd53b5bf256f9e32a4864f4aa3e7de53a3e0d6(
    *,
    elb_info_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.ELBInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    target_group_info_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TargetGroupInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    target_group_pair_info_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TargetGroupPairInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4011b432f9b5ed3fcdaa688b15c75cc1850efecdc1b1a6c9b90e48052559ec5b(
    *,
    on_premises_tag_group: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36ece4f2e243605e790c8b3d869b089b200ff22c8a77da7ce3d7477f6504f697(
    *,
    on_premises_tag_set_list: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.OnPremisesTagSetListObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f29088b2f9a724cb557a6d1896af99895cac8961456ede05c903a4cb938ff48d(
    *,
    git_hub_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.GitHubLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    revision_type: typing.Optional[builtins.str] = None,
    s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c51f97a2e756174dd9b616cbc2cf2e3a30fc7670a54bc88414aabf5142992ec(
    *,
    bucket: builtins.str,
    key: builtins.str,
    bundle_type: typing.Optional[builtins.str] = None,
    e_tag: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63f4128dda3c53a5291d286360b72c038c5228704c806b5dfffed5bf290d6317(
    *,
    key: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16465f8a39251aa9907267031575771f643f1897cd1cfea422dfafe3c33e4e92(
    *,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e5e2e921fcbd8db2d985022ed2557366a9e03a443be17ad0a66dc2940dfe1f1(
    *,
    prod_traffic_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TrafficRouteProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_groups: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TargetGroupInfoProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    test_traffic_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TrafficRouteProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__658bb64cfd11bd3a4440b0f5de1ea0cdd277919eeaddf444d9b6438282bad659(
    *,
    listener_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bf43d66fb9d8d74aceca78cf370506dcc65400910ba065753222415226e3c5(
    *,
    trigger_events: typing.Optional[typing.Sequence[builtins.str]] = None,
    trigger_name: typing.Optional[builtins.str] = None,
    trigger_target_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6511a1a48658d7f16b747353194a86e2a15daf184e4957a0f2924cfee66716bc(
    *,
    application_name: builtins.str,
    service_role_arn: builtins.str,
    alarm_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AlarmConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_rollback_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.AutoRollbackConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_scaling_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    blue_green_deployment_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.BlueGreenDeploymentConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    deployment_style: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.DeploymentStyleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ec2_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.EC2TagSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ecs_services: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.ECSServiceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    load_balancer_info: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.LoadBalancerInfoProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    on_premises_instance_tag_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TagFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    on_premises_tag_set: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.OnPremisesTagSetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outdated_instances_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trigger_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDeploymentGroup.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f8c53864749c97e11693362fedad7242c31fc477d04c6e3dede64774251fad3(
    *,
    interval: _Duration_4839e8c3,
    percentage: jsii.Number,
    type: CustomLambdaDeploymentConfigType,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31617a0bd5a72eae80bdaf60a12a3c49a0948473616c9a8e908f3d9bd671d2f5(
    *,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b251dc2bb3166b5b08fc4a016e350d50231d6a3f0a8566638996a295262e0269(
    *,
    blue_target_group: _ITargetGroup_83c6f8c4,
    green_target_group: _ITargetGroup_83c6f8c4,
    listener: _IListener_7f84e41f,
    deployment_approval_wait_time: typing.Optional[_Duration_4839e8c3] = None,
    termination_wait_time: typing.Optional[_Duration_4839e8c3] = None,
    test_listener: typing.Optional[_IListener_7f84e41f] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f77eb6fc251ed7746cecc68aaaaf5706c1f2831b79812175c6abd5ba12b754(
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
    traffic_routing: typing.Optional[TrafficRouting] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__171917799e985d16bcafd7fcbcf48ad64ae8bcb175f7e2b8f9fe1f74316e63df(
    *,
    application: IEcsApplication,
    deployment_group_name: builtins.str,
    deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7adf7c582969f2d223ca19321a889bd4195cc6c299e92558e985e0fdcdea2cd0(
    *,
    blue_green_deployment_config: typing.Union[EcsBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]],
    service: _IBaseService_3fcdd913,
    alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
    application: typing.Optional[IEcsApplication] = None,
    auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64b9abb1b571fcb8018ddc7afe78c42eb103fc0f0e19660e4bb0469356dd1564(
    *instance_tag_groups: typing.Mapping[builtins.str, typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32e68c167bb11e7bc23a290f22241a7b484b9a93c7477bfc8c699fd61d487e2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d61dd07d8a44ddb86bf93e059a6adddbf9f337ddc2950868f8521d6d384940a3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    lambda_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1450d2b1c6c573bfe2bedfa6cd62cfe0f9b692ed8c0d2be4332b4ad5579ec629(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    lambda_application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92ab1acbc62b972c13cc918ece32b4065ed5e2d1fd027313d6a8f70f0f7f7d7a(
    *,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87bb46cc3cd2b6f2e34d49e71d8065dcab36372a5cc7cbe2a6cb84bf8150c93a(
    *,
    deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc83553749492603e2a4699e478de4d29b9ccf880c156fb0da254af8ec807aee(
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
    traffic_routing: typing.Optional[TrafficRouting] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c26416b16de08b4064de631244255b96e87828c1c22b3d5795282b4183224b2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias: _Alias_55be8873,
    alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
    application: typing.Optional[ILambdaApplication] = None,
    auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
    post_hook: typing.Optional[_IFunction_6adb0ab8] = None,
    pre_hook: typing.Optional[_IFunction_6adb0ab8] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fd4dfddfe47c0a8dd92426b46cd63260d58eb3379c02a54f9334570681da9bd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: ILambdaApplication,
    deployment_group_name: builtins.str,
    deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b711b8130a1d80370d61b0db615c68c614d3077ac9c81be826135376059b97e(
    alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52088593799588d855f46763ba6983d5b95d7128d66002267869967f0a287d99(
    post_hook: _IFunction_6adb0ab8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9479e7d155c760cd01795544331c610a1cab348cb04f2ac1aaa5373c713b9424(
    pre_hook: _IFunction_6adb0ab8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d8689c21818340ec688b7586fd416bd82b1e7011d11184910717b5859285cb4(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08bd7879a63053a6c7bc752ef445954728069ab3039a8ede60d6b4eeea401e64(
    *,
    application: ILambdaApplication,
    deployment_group_name: builtins.str,
    deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874e757437525f2d71406c292cf5ac7fae66797609da322dac9063247a871238(
    *,
    alias: _Alias_55be8873,
    alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
    application: typing.Optional[ILambdaApplication] = None,
    auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_config: typing.Optional[ILambdaDeploymentConfig] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
    post_hook: typing.Optional[_IFunction_6adb0ab8] = None,
    pre_hook: typing.Optional[_IFunction_6adb0ab8] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__370bf2390e5c88cb8bbf9c66f599b85ef458396f8157823b987c090f4826d4ef(
    *,
    linear_interval: jsii.Number,
    linear_percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c36a2f946c61769d76c913c28d5738063c97172f02aedd94b235d81679262630(
    alb_target_group: _IApplicationTargetGroup_57799827,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8808efa456e0bde58915d9f2353dc69253ae06e9b202151c399da611d72dc3a7(
    load_balancer: _LoadBalancer_a894d40e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c09dbdbc45c1037d7977cfe1df1e715bec88560b2da64188007c9c48538f678(
    nlb_target_group: _INetworkTargetGroup_abca2df7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43a212ab251dfefee2c1b1ee5cee194431e2a0ddeec2d9373bc5962fcc70beac(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c2a97036f753857be857236ee3fb97ddf235514bd9c31466fb2e569196a8670(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff491d45a3da21d4d70991ac332ef8f240b72138a59519fcf6c3da3a3a9cb970(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf6f1cc9e06bced10736cddcc278aca232660b56bc0451a57cced62037ec8590(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    server_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__926add8da73c5c44e3476965c380244e6b8d904443a6d509c4211b7aeebc5804(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    server_application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5712e790d967a85a2bf9b346a95ce6db55b781233d88b2df81a98394233a8fb(
    *,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46be421d00313823efbbb0072b871dc311f7d9fca8dee4c13562ddd078f8cd37(
    *,
    deployment_config_name: typing.Optional[builtins.str] = None,
    minimum_healthy_hosts: MinimumHealthyHosts,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0364d4b48c02675a1899e742e45b411f0e83905e634a84441d088a41fe25c8f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
    application: typing.Optional[IServerApplication] = None,
    auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling_groups: typing.Optional[typing.Sequence[_IAutoScalingGroup_360f1cde]] = None,
    deployment_config: typing.Optional[IServerDeploymentConfig] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    ec2_instance_tags: typing.Optional[InstanceTagSet] = None,
    ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
    install_agent: typing.Optional[builtins.bool] = None,
    load_balancer: typing.Optional[LoadBalancer] = None,
    on_premise_instance_tags: typing.Optional[InstanceTagSet] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8af8e520b8abc653e37c88dc9f6e51e7d52aa5f24d99a8bcc8765154067e55f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: IServerApplication,
    deployment_group_name: builtins.str,
    deployment_config: typing.Optional[IServerDeploymentConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__356a323fcb86d198006a31f41e7e9d1c8a6892ac423e8cb69666cd1ddcb8e718(
    alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8eb5bbbb7e095997fadbddebece8f587dfbebf76e4fba6c071f9def29db693c8(
    asg: _AutoScalingGroup_c547a7b9,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c78d15fd80ffece3b49e232b4a29903107350aac8446220b8caea80c448a80(
    *,
    application: IServerApplication,
    deployment_group_name: builtins.str,
    deployment_config: typing.Optional[IServerDeploymentConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3ad41a581be1a234fd5722299d51aa77bd7beaf51e0511c95ee742d49944018(
    *,
    alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
    application: typing.Optional[IServerApplication] = None,
    auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    auto_scaling_groups: typing.Optional[typing.Sequence[_IAutoScalingGroup_360f1cde]] = None,
    deployment_config: typing.Optional[IServerDeploymentConfig] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    ec2_instance_tags: typing.Optional[InstanceTagSet] = None,
    ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
    install_agent: typing.Optional[builtins.bool] = None,
    load_balancer: typing.Optional[LoadBalancer] = None,
    on_premise_instance_tags: typing.Optional[InstanceTagSet] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06d16b3e96e0fa33fc82ea5d170af742eef9ed50a9cbf223cb2ed4b3a79e12b0(
    *,
    interval: _Duration_4839e8c3,
    percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ae43dc71a0186139db7c80b7def0fee785a31717f8577d65e13a868d2b3817a(
    *,
    interval: _Duration_4839e8c3,
    percentage: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd12a268dfe455277ad66728e6406ae5106e0f7beedf165c115e8e39ace124f0(
    scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b845a8828051dc720d79c0332ea3470f754dd765be05c704a97b6582380610fb(
    *,
    type: builtins.str,
    time_based_canary: typing.Optional[typing.Union[CanaryTrafficRoutingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    time_based_linear: typing.Optional[typing.Union[LinearTrafficRoutingConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f05ebc00e48366a13e2ad293e1822da6d979a050647a74d9f563aab403921d0d(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7be4ac008b1dbe1f91bb986ac7bb32dd779f4962b7a7696d9064b17fa3e5e35(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compute_platform: typing.Optional[ComputePlatform] = None,
    minimum_healthy_hosts: typing.Optional[MinimumHealthyHosts] = None,
    traffic_routing: typing.Optional[TrafficRouting] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f696afb42fc23d24c96d39b2254f0b625ecbfacca97da38df5ba1831b8c62a53(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac867d6e5022c0be7de76fadf84363729e8cfde59c1d36f19b324981b6e8053(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    interval: _Duration_4839e8c3,
    percentage: jsii.Number,
    type: CustomLambdaDeploymentConfigType,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4edf5fb61452170b1877882129fc1df2e63797e3a9f6b183813f1e20bf3b8854(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a15b4054e084bc53dcd5e21cbb4878436d9d1074cc50177d7007d7382b209c85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    ecs_application_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10762c159701d6da1d6d041f0ac41aba5c82b3d604e4bad2002ef52f91f66339(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    ecs_application_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2d7f681f3251c7de51922fccb03d9839dc0514700deb88855b4a1e3e089d308(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    traffic_routing: typing.Optional[TrafficRouting] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99681a26417ad9494dc9331a9865e7f0cf7cb6ec84094cf3b3a4888af4a81b06(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    ecs_deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d5a27f58faebed8ad465b39d408bd717722f646f6471896e02b8ea95b82bc49(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    blue_green_deployment_config: typing.Union[EcsBlueGreenDeploymentConfig, typing.Dict[builtins.str, typing.Any]],
    service: _IBaseService_3fcdd913,
    alarms: typing.Optional[typing.Sequence[_IAlarm_ff3eabc0]] = None,
    application: typing.Optional[IEcsApplication] = None,
    auto_rollback: typing.Optional[typing.Union[AutoRollbackConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
    deployment_group_name: typing.Optional[builtins.str] = None,
    ignore_poll_alarms_failure: typing.Optional[builtins.bool] = None,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21d5d2081ae62e02eb318efb6845c80afcd2a31d1f65949b88d5e28b3887b2f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application: IEcsApplication,
    deployment_group_name: builtins.str,
    deployment_config: typing.Optional[IEcsDeploymentConfig] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecbfe2758d485b20b4d7753475293fc67c26edc4d904112e8a409df22ce5f06c(
    alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5058ddee6c11563a4a133d87a712b18e3c1621329942e72104da625c5e6242b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    traffic_routing: typing.Optional[TrafficRouting] = None,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c000174f0f5fb89592424d7fb95552d79f3a850e96cfda07890bde08230908(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    lambda_deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1505251b6329a0bcb03ec5f5656f675b1c5236b529a51019e64f1fee9d98cdb6(
    _scope: _constructs_77d1e7e8.Construct,
    _id: builtins.str,
    *,
    deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0188bedb6550f8f8ec5175aae5830d1c200a93e114c45fc9d6b3942b7d6123a7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    minimum_healthy_hosts: MinimumHealthyHosts,
    deployment_config_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0ea4e0fbba82ec61d62008656825ba154d6ab7a16569e404ef56dd5d012b2d4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    server_deployment_config_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f62d359f751a6aad86ee02e74d93fa8692f764928aa7fa26224cb9b7679affc8(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa5564b995bb046b6d26e38cc462ee09779219878f550d6e7a210ed2d50a5b84(
    _scope: _constructs_77d1e7e8.Construct,
) -> None:
    """Type checking stubs"""
    pass
