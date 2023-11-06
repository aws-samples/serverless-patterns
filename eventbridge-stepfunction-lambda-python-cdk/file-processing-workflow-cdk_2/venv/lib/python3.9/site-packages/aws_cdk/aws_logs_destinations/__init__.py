'''
# AWS CloudWatch Logs Subscription Destination Library

This library contains destinations for AWS CloudWatch Logs SubscriptionFilters. You
can send log data to Kinesis Streams or Lambda Functions.

See the documentation of the `logs` module for more information.
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
from ..aws_iam import IRole as _IRole_235f5d8e
from ..aws_kinesis import IStream as _IStream_4e2457d2
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_logs import (
    ILogGroup as _ILogGroup_3c4fa718,
    ILogSubscriptionDestination as _ILogSubscriptionDestination_99a12804,
    LogSubscriptionDestinationConfig as _LogSubscriptionDestinationConfig_15877ced,
)


@jsii.implements(_ILogSubscriptionDestination_99a12804)
class KinesisDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs_destinations.KinesisDestination",
):
    '''Use a Kinesis stream as the destination for a log subscription.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_kinesis as kinesis
        from aws_cdk import aws_logs_destinations as logs_destinations
        
        # role: iam.Role
        # stream: kinesis.Stream
        
        kinesis_destination = logs_destinations.KinesisDestination(stream,
            role=role
        )
    '''

    def __init__(
        self,
        stream: _IStream_4e2457d2,
        *,
        role: typing.Optional[_IRole_235f5d8e] = None,
    ) -> None:
        '''
        :param stream: The Kinesis stream to use as destination.
        :param role: The role to assume to write log events to the destination. Default: - A new Role is created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f4422231f62d5490fdbb0217f4c6e73134c1c066522144d9488224a6ffe689b)
            check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
        props = KinesisDestinationProps(role=role)

        jsii.create(self.__class__, self, [stream, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        _source_log_group: _ILogGroup_3c4fa718,
    ) -> _LogSubscriptionDestinationConfig_15877ced:
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param _source_log_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a07b9b6b39b3253620357aaea5f2db6340db83e8acaeadc70a521c3ba7ff8bc8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument _source_log_group", value=_source_log_group, expected_type=type_hints["_source_log_group"])
        return typing.cast(_LogSubscriptionDestinationConfig_15877ced, jsii.invoke(self, "bind", [scope, _source_log_group]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs_destinations.KinesisDestinationProps",
    jsii_struct_bases=[],
    name_mapping={"role": "role"},
)
class KinesisDestinationProps:
    def __init__(self, *, role: typing.Optional[_IRole_235f5d8e] = None) -> None:
        '''Customize the Kinesis Logs Destination.

        :param role: The role to assume to write log events to the destination. Default: - A new Role is created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_logs_destinations as logs_destinations
            
            # role: iam.Role
            
            kinesis_destination_props = logs_destinations.KinesisDestinationProps(
                role=role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed9acb9b71ca684b5ebfbc3c135853e27907758f495b2be8f5c1b2c9f6ee2acb)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if role is not None:
            self._values["role"] = role

    @builtins.property
    def role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''The role to assume to write log events to the destination.

        :default: - A new Role is created
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KinesisDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_ILogSubscriptionDestination_99a12804)
class LambdaDestination(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_logs_destinations.LambdaDestination",
):
    '''Use a Lambda Function as the destination for a log subscription.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_logs_destinations as destinations
        
        # fn: lambda.Function
        # log_group: logs.LogGroup
        
        
        logs.SubscriptionFilter(self, "Subscription",
            log_group=log_group,
            destination=destinations.LambdaDestination(fn),
            filter_pattern=logs.FilterPattern.all_terms("ERROR", "MainThread"),
            filter_name="ErrorInMainThread"
        )
    '''

    def __init__(
        self,
        fn: _IFunction_6adb0ab8,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''LambdaDestinationOptions.

        :param fn: -
        :param add_permissions: Whether or not to add Lambda Permissions. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c47e3ce3069e1b69399c7a089486d831f48b9af53861d0ad449aab3b9864816c)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        options = LambdaDestinationOptions(add_permissions=add_permissions)

        jsii.create(self.__class__, self, [fn, options])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        log_group: _ILogGroup_3c4fa718,
    ) -> _LogSubscriptionDestinationConfig_15877ced:
        '''Return the properties required to send subscription events to this destination.

        If necessary, the destination can use the properties of the SubscriptionFilter
        object itself to configure its permissions to allow the subscription to write
        to it.

        The destination may reconfigure its own permissions in response to this
        function call.

        :param scope: -
        :param log_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a6c995782d33f0fc9c3b09e6ca3ad1d26c953c729ccc6f6ce6e0c48579dac67)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument log_group", value=log_group, expected_type=type_hints["log_group"])
        return typing.cast(_LogSubscriptionDestinationConfig_15877ced, jsii.invoke(self, "bind", [scope, log_group]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_logs_destinations.LambdaDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={"add_permissions": "addPermissions"},
)
class LambdaDestinationOptions:
    def __init__(
        self,
        *,
        add_permissions: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Options that may be provided to LambdaDestination.

        :param add_permissions: Whether or not to add Lambda Permissions. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_logs_destinations as logs_destinations
            
            lambda_destination_options = logs_destinations.LambdaDestinationOptions(
                add_permissions=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__259a49bfbf7d698b36353f61f932529b98ad6ca6911ab92efe40ed71c6d43bff)
            check_type(argname="argument add_permissions", value=add_permissions, expected_type=type_hints["add_permissions"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_permissions is not None:
            self._values["add_permissions"] = add_permissions

    @builtins.property
    def add_permissions(self) -> typing.Optional[builtins.bool]:
        '''Whether or not to add Lambda Permissions.

        :default: true
        '''
        result = self._values.get("add_permissions")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "KinesisDestination",
    "KinesisDestinationProps",
    "LambdaDestination",
    "LambdaDestinationOptions",
]

publication.publish()

def _typecheckingstub__6f4422231f62d5490fdbb0217f4c6e73134c1c066522144d9488224a6ffe689b(
    stream: _IStream_4e2457d2,
    *,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a07b9b6b39b3253620357aaea5f2db6340db83e8acaeadc70a521c3ba7ff8bc8(
    scope: _constructs_77d1e7e8.Construct,
    _source_log_group: _ILogGroup_3c4fa718,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed9acb9b71ca684b5ebfbc3c135853e27907758f495b2be8f5c1b2c9f6ee2acb(
    *,
    role: typing.Optional[_IRole_235f5d8e] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c47e3ce3069e1b69399c7a089486d831f48b9af53861d0ad449aab3b9864816c(
    fn: _IFunction_6adb0ab8,
    *,
    add_permissions: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a6c995782d33f0fc9c3b09e6ca3ad1d26c953c729ccc6f6ce6e0c48579dac67(
    scope: _constructs_77d1e7e8.Construct,
    log_group: _ILogGroup_3c4fa718,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__259a49bfbf7d698b36353f61f932529b98ad6ca6911ab92efe40ed71c6d43bff(
    *,
    add_permissions: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass
