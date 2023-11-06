'''
# CloudWatch Alarm Actions library

This library contains a set of classes which can be used as CloudWatch Alarm actions.

The currently implemented actions are: EC2 Actions, SNS Actions, SSM OpsCenter Actions, Autoscaling Actions and Application Autoscaling Actions

## EC2 Action Example

```python
# Alarm must be configured with an EC2 per-instance metric
# alarm: cloudwatch.Alarm

# Attach a reboot when alarm triggers
alarm.add_alarm_action(
    actions.Ec2Action(actions.Ec2InstanceAction.REBOOT))
```

## SSM OpsCenter Action Example

```python
# alarm: cloudwatch.Alarm

# Create an OpsItem with specific severity and category when alarm triggers
alarm.add_alarm_action(
    actions.SsmAction(actions.OpsItemSeverity.CRITICAL, actions.OpsItemCategory.PERFORMANCE))
```

## SSM Incident Manager Action Example

```python
# alarm: cloudwatch.Alarm

# Create an Incident Manager incident based on a specific response plan
alarm.add_alarm_action(
    actions.SsmIncidentAction("ResponsePlanName"))
```

See `aws-cdk-lib/aws-cloudwatch` for more information.
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
from ..aws_applicationautoscaling import (
    StepScalingAction as _StepScalingAction_d79ca2c9
)
from ..aws_autoscaling import StepScalingAction as _StepScalingAction_24d17483
from ..aws_cloudwatch import (
    AlarmActionConfig as _AlarmActionConfig_f831c655,
    IAlarm as _IAlarm_ff3eabc0,
    IAlarmAction as _IAlarmAction_922c5aa8,
)
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.implements(_IAlarmAction_922c5aa8)
class ApplicationScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.ApplicationScalingAction",
):
    '''Use an ApplicationAutoScaling StepScalingAction as an Alarm Action.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_applicationautoscaling as appscaling
        from aws_cdk import aws_cloudwatch_actions as cloudwatch_actions
        
        # step_scaling_action: appscaling.StepScalingAction
        
        application_scaling_action = cloudwatch_actions.ApplicationScalingAction(step_scaling_action)
    '''

    def __init__(self, step_scaling_action: _StepScalingAction_d79ca2c9) -> None:
        '''
        :param step_scaling_action: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b916236e2043981349e2841d1ec98b11cee63ab17d5362ab2a6d58f02a514d7d)
            check_type(argname="argument step_scaling_action", value=step_scaling_action, expected_type=type_hints["step_scaling_action"])
        jsii.create(self.__class__, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an ApplicationScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74bb72262ab3b2a9141f8b8f1171cf0d9a0ba7d5f865b123acffaec5bfef51fd)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _alarm", value=_alarm, expected_type=type_hints["_alarm"])
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(_IAlarmAction_922c5aa8)
class AutoScalingAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.AutoScalingAction",
):
    '''Use an AutoScaling StepScalingAction as an Alarm Action.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_autoscaling as autoscaling
        from aws_cdk import aws_cloudwatch_actions as cloudwatch_actions
        
        # step_scaling_action: autoscaling.StepScalingAction
        
        auto_scaling_action = cloudwatch_actions.AutoScalingAction(step_scaling_action)
    '''

    def __init__(self, step_scaling_action: _StepScalingAction_24d17483) -> None:
        '''
        :param step_scaling_action: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96afe5a98488b1418c68f6530257948e9ea29d3656df0b68c83d1defaf09dd60)
            check_type(argname="argument step_scaling_action", value=step_scaling_action, expected_type=type_hints["step_scaling_action"])
        jsii.create(self.__class__, self, [step_scaling_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an AutoScaling StepScalingAction as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd3adde7a8331a2b783351a5b794ad83f7245f085799ed1b7e3d9deedcd8d03)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _alarm", value=_alarm, expected_type=type_hints["_alarm"])
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(_IAlarmAction_922c5aa8)
class Ec2Action(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.Ec2Action",
):
    '''Use an EC2 action as an Alarm action.

    :exampleMetadata: infused

    Example::

        # Alarm must be configured with an EC2 per-instance metric
        # alarm: cloudwatch.Alarm
        
        # Attach a reboot when alarm triggers
        alarm.add_alarm_action(
            actions.Ec2Action(actions.Ec2InstanceAction.REBOOT))
    '''

    def __init__(self, instance_action: "Ec2InstanceAction") -> None:
        '''
        :param instance_action: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aeaedd2203e210d309c17277a5c904dcbc459891e662493aaf75e344e40174f4)
            check_type(argname="argument instance_action", value=instance_action, expected_type=type_hints["instance_action"])
        jsii.create(self.__class__, self, [instance_action])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an EC2 action as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__617684dcf0b429d0176779c30669a734e5e356a2d0dbb98bf321e897c2cbdcd3)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _alarm", value=_alarm, expected_type=type_hints["_alarm"])
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch_actions.Ec2InstanceAction")
class Ec2InstanceAction(enum.Enum):
    '''Types of EC2 actions available.

    :exampleMetadata: infused

    Example::

        # Alarm must be configured with an EC2 per-instance metric
        # alarm: cloudwatch.Alarm
        
        # Attach a reboot when alarm triggers
        alarm.add_alarm_action(
            actions.Ec2Action(actions.Ec2InstanceAction.REBOOT))
    '''

    STOP = "STOP"
    '''Stop the instance.'''
    TERMINATE = "TERMINATE"
    '''Terminatethe instance.'''
    RECOVER = "RECOVER"
    '''Recover the instance.'''
    REBOOT = "REBOOT"
    '''Reboot the instance.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch_actions.OpsItemCategory")
class OpsItemCategory(enum.Enum):
    '''Types of OpsItem category available.

    :exampleMetadata: infused

    Example::

        # alarm: cloudwatch.Alarm
        
        # Create an OpsItem with specific severity and category when alarm triggers
        alarm.add_alarm_action(
            actions.SsmAction(actions.OpsItemSeverity.CRITICAL, actions.OpsItemCategory.PERFORMANCE))
    '''

    AVAILABILITY = "AVAILABILITY"
    '''Set the category to availability.'''
    COST = "COST"
    '''Set the category to cost.'''
    PERFORMANCE = "PERFORMANCE"
    '''Set the category to performance.'''
    RECOVERY = "RECOVERY"
    '''Set the category to recovery.'''
    SECURITY = "SECURITY"
    '''Set the category to security.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_cloudwatch_actions.OpsItemSeverity")
class OpsItemSeverity(enum.Enum):
    '''Types of OpsItem severity available.

    :exampleMetadata: infused

    Example::

        # alarm: cloudwatch.Alarm
        
        # Create an OpsItem with specific severity and category when alarm triggers
        alarm.add_alarm_action(
            actions.SsmAction(actions.OpsItemSeverity.CRITICAL, actions.OpsItemCategory.PERFORMANCE))
    '''

    CRITICAL = "CRITICAL"
    '''Set the severity to critical.'''
    HIGH = "HIGH"
    '''Set the severity to high.'''
    MEDIUM = "MEDIUM"
    '''Set the severity to medium.'''
    LOW = "LOW"
    '''Set the severity to low.'''


@jsii.implements(_IAlarmAction_922c5aa8)
class SnsAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.SnsAction",
):
    '''Use an SNS topic as an alarm action.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudwatch_actions as cw_actions
        # alarm: cloudwatch.Alarm
        
        
        topic = sns.Topic(self, "Topic")
        alarm.add_alarm_action(cw_actions.SnsAction(topic))
    '''

    def __init__(self, topic: _ITopic_9eca4852) -> None:
        '''
        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d45c9fa069d1e0b882f975c29c8eb30315e60025b85741889c42ee16c1f229ca)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        jsii.create(self.__class__, self, [topic])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an SNS topic as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02204ab9dd4d2adf853c731232a8cb824c41fb62dc79eae79e4e69b7e0e748eb)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _alarm", value=_alarm, expected_type=type_hints["_alarm"])
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(_IAlarmAction_922c5aa8)
class SsmAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.SsmAction",
):
    '''Use an SSM OpsItem action as an Alarm action.

    :exampleMetadata: infused

    Example::

        # alarm: cloudwatch.Alarm
        
        # Create an OpsItem with specific severity and category when alarm triggers
        alarm.add_alarm_action(
            actions.SsmAction(actions.OpsItemSeverity.CRITICAL, actions.OpsItemCategory.PERFORMANCE))
    '''

    def __init__(
        self,
        severity: OpsItemSeverity,
        category: typing.Optional[OpsItemCategory] = None,
    ) -> None:
        '''
        :param severity: -
        :param category: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec3a9c97b1f6b9b5d3d6db7a3eb09cb5990e4d0201ddb6c37b8ccf6864b794a1)
            check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
            check_type(argname="argument category", value=category, expected_type=type_hints["category"])
        jsii.create(self.__class__, self, [severity, category])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an SSM OpsItem action as an alarm action.

        :param _scope: -
        :param _alarm: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01d8a7f674b7236375000e24e89aa7de87b7b73e1540d7b7a75318b36ba526fa)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _alarm", value=_alarm, expected_type=type_hints["_alarm"])
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


@jsii.implements(_IAlarmAction_922c5aa8)
class SsmIncidentAction(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudwatch_actions.SsmIncidentAction",
):
    '''Use an SSM Incident Response Plan as an Alarm action.

    :exampleMetadata: infused

    Example::

        # alarm: cloudwatch.Alarm
        
        # Create an Incident Manager incident based on a specific response plan
        alarm.add_alarm_action(
            actions.SsmIncidentAction("ResponsePlanName"))
    '''

    def __init__(self, response_plan_name: builtins.str) -> None:
        '''
        :param response_plan_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be00ac2bf80144c7f66d1276bfef345e7613075b15116cbf4a62b8fa42044c98)
            check_type(argname="argument response_plan_name", value=response_plan_name, expected_type=type_hints["response_plan_name"])
        jsii.create(self.__class__, self, [response_plan_name])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _scope: _constructs_77d1e7e8.Construct,
        _alarm: _IAlarm_ff3eabc0,
    ) -> _AlarmActionConfig_f831c655:
        '''Returns an alarm action configuration to use an SSM Incident as an alarm action based on an Incident Manager Response Plan.

        :param _scope: -
        :param _alarm: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__27baa9de2ba955e7124c3e624eb53ed6f9be430c6d188be64d2ef483e56fabf5)
            check_type(argname="argument _scope", value=_scope, expected_type=type_hints["_scope"])
            check_type(argname="argument _alarm", value=_alarm, expected_type=type_hints["_alarm"])
        return typing.cast(_AlarmActionConfig_f831c655, jsii.invoke(self, "bind", [_scope, _alarm]))


__all__ = [
    "ApplicationScalingAction",
    "AutoScalingAction",
    "Ec2Action",
    "Ec2InstanceAction",
    "OpsItemCategory",
    "OpsItemSeverity",
    "SnsAction",
    "SsmAction",
    "SsmIncidentAction",
]

publication.publish()

def _typecheckingstub__b916236e2043981349e2841d1ec98b11cee63ab17d5362ab2a6d58f02a514d7d(
    step_scaling_action: _StepScalingAction_d79ca2c9,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74bb72262ab3b2a9141f8b8f1171cf0d9a0ba7d5f865b123acffaec5bfef51fd(
    _scope: _constructs_77d1e7e8.Construct,
    _alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96afe5a98488b1418c68f6530257948e9ea29d3656df0b68c83d1defaf09dd60(
    step_scaling_action: _StepScalingAction_24d17483,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd3adde7a8331a2b783351a5b794ad83f7245f085799ed1b7e3d9deedcd8d03(
    _scope: _constructs_77d1e7e8.Construct,
    _alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aeaedd2203e210d309c17277a5c904dcbc459891e662493aaf75e344e40174f4(
    instance_action: Ec2InstanceAction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__617684dcf0b429d0176779c30669a734e5e356a2d0dbb98bf321e897c2cbdcd3(
    _scope: _constructs_77d1e7e8.Construct,
    _alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d45c9fa069d1e0b882f975c29c8eb30315e60025b85741889c42ee16c1f229ca(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02204ab9dd4d2adf853c731232a8cb824c41fb62dc79eae79e4e69b7e0e748eb(
    _scope: _constructs_77d1e7e8.Construct,
    _alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec3a9c97b1f6b9b5d3d6db7a3eb09cb5990e4d0201ddb6c37b8ccf6864b794a1(
    severity: OpsItemSeverity,
    category: typing.Optional[OpsItemCategory] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d8a7f674b7236375000e24e89aa7de87b7b73e1540d7b7a75318b36ba526fa(
    _scope: _constructs_77d1e7e8.Construct,
    _alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be00ac2bf80144c7f66d1276bfef345e7613075b15116cbf4a62b8fa42044c98(
    response_plan_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__27baa9de2ba955e7124c3e624eb53ed6f9be430c6d188be64d2ef483e56fabf5(
    _scope: _constructs_77d1e7e8.Construct,
    _alarm: _IAlarm_ff3eabc0,
) -> None:
    """Type checking stubs"""
    pass
