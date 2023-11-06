'''
# AWS AutoScaling Common Library

This is a sister package to `aws-cdk-lib/aws-autoscaling` and
`aws-cdk-lib/aws-applicationautoscaling`. It contains shared implementation
details between them.

It does not need to be used directly.
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


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_autoscaling_common.Alarms",
    jsii_struct_bases=[],
    name_mapping={
        "lower_alarm_interval_index": "lowerAlarmIntervalIndex",
        "upper_alarm_interval_index": "upperAlarmIntervalIndex",
    },
)
class Alarms:
    def __init__(
        self,
        *,
        lower_alarm_interval_index: typing.Optional[jsii.Number] = None,
        upper_alarm_interval_index: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param lower_alarm_interval_index: 
        :param upper_alarm_interval_index: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_autoscaling_common as autoscaling_common
            
            alarms = autoscaling_common.Alarms(
                lower_alarm_interval_index=123,
                upper_alarm_interval_index=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abf78afeb9ac8e8462332fca79fe9b5fffea8d7bfa2ff758f5d7a5e7602ad7f6)
            check_type(argname="argument lower_alarm_interval_index", value=lower_alarm_interval_index, expected_type=type_hints["lower_alarm_interval_index"])
            check_type(argname="argument upper_alarm_interval_index", value=upper_alarm_interval_index, expected_type=type_hints["upper_alarm_interval_index"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if lower_alarm_interval_index is not None:
            self._values["lower_alarm_interval_index"] = lower_alarm_interval_index
        if upper_alarm_interval_index is not None:
            self._values["upper_alarm_interval_index"] = upper_alarm_interval_index

    @builtins.property
    def lower_alarm_interval_index(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("lower_alarm_interval_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upper_alarm_interval_index(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("upper_alarm_interval_index")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Alarms(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_autoscaling_common.ArbitraryIntervals",
    jsii_struct_bases=[],
    name_mapping={"absolute": "absolute", "intervals": "intervals"},
)
class ArbitraryIntervals:
    def __init__(
        self,
        *,
        absolute: builtins.bool,
        intervals: typing.Sequence[typing.Union["ScalingInterval", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param absolute: 
        :param intervals: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_autoscaling_common as autoscaling_common
            
            arbitrary_intervals = autoscaling_common.ArbitraryIntervals(
                absolute=False,
                intervals=[autoscaling_common.ScalingInterval(
                    change=123,
            
                    # the properties below are optional
                    lower=123,
                    upper=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57995ea3409b19529dee8383d66d29b069590c52cb741f0e8ae75b7bc40af361)
            check_type(argname="argument absolute", value=absolute, expected_type=type_hints["absolute"])
            check_type(argname="argument intervals", value=intervals, expected_type=type_hints["intervals"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "absolute": absolute,
            "intervals": intervals,
        }

    @builtins.property
    def absolute(self) -> builtins.bool:
        result = self._values.get("absolute")
        assert result is not None, "Required property 'absolute' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def intervals(self) -> typing.List["ScalingInterval"]:
        result = self._values.get("intervals")
        assert result is not None, "Required property 'intervals' is missing"
        return typing.cast(typing.List["ScalingInterval"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ArbitraryIntervals(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_autoscaling_common.CompleteScalingInterval",
    jsii_struct_bases=[],
    name_mapping={"lower": "lower", "upper": "upper", "change": "change"},
)
class CompleteScalingInterval:
    def __init__(
        self,
        *,
        lower: jsii.Number,
        upper: jsii.Number,
        change: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param lower: 
        :param upper: 
        :param change: 

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_autoscaling_common as autoscaling_common
            
            complete_scaling_interval = autoscaling_common.CompleteScalingInterval(
                lower=123,
                upper=123,
            
                # the properties below are optional
                change=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2dcfdc3d9397619d127fb623a33ade65cb15bfd29863b7d524d449180f466014)
            check_type(argname="argument lower", value=lower, expected_type=type_hints["lower"])
            check_type(argname="argument upper", value=upper, expected_type=type_hints["upper"])
            check_type(argname="argument change", value=change, expected_type=type_hints["change"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "lower": lower,
            "upper": upper,
        }
        if change is not None:
            self._values["change"] = change

    @builtins.property
    def lower(self) -> jsii.Number:
        result = self._values.get("lower")
        assert result is not None, "Required property 'lower' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def upper(self) -> jsii.Number:
        result = self._values.get("upper")
        assert result is not None, "Required property 'upper' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def change(self) -> typing.Optional[jsii.Number]:
        result = self._values.get("change")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CompleteScalingInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_autoscaling_common.IRandomGenerator")
class IRandomGenerator(typing_extensions.Protocol):
    @jsii.member(jsii_name="nextBoolean")
    def next_boolean(self) -> builtins.bool:
        ...

    @jsii.member(jsii_name="nextInt")
    def next_int(self, min: jsii.Number, max: jsii.Number) -> jsii.Number:
        '''
        :param min: -
        :param max: -
        '''
        ...


class _IRandomGeneratorProxy:
    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_autoscaling_common.IRandomGenerator"

    @jsii.member(jsii_name="nextBoolean")
    def next_boolean(self) -> builtins.bool:
        return typing.cast(builtins.bool, jsii.invoke(self, "nextBoolean", []))

    @jsii.member(jsii_name="nextInt")
    def next_int(self, min: jsii.Number, max: jsii.Number) -> jsii.Number:
        '''
        :param min: -
        :param max: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4f79c181fb4012fc3ec659257628da3b8d1a60516f0b95625926cb8a6b56f8b)
            check_type(argname="argument min", value=min, expected_type=type_hints["min"])
            check_type(argname="argument max", value=max, expected_type=type_hints["max"])
        return typing.cast(jsii.Number, jsii.invoke(self, "nextInt", [min, max]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRandomGenerator).__jsii_proxy_class__ = lambda : _IRandomGeneratorProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_autoscaling_common.ScalingInterval",
    jsii_struct_bases=[],
    name_mapping={"change": "change", "lower": "lower", "upper": "upper"},
)
class ScalingInterval:
    def __init__(
        self,
        *,
        change: jsii.Number,
        lower: typing.Optional[jsii.Number] = None,
        upper: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''A range of metric values in which to apply a certain scaling operation.

        :param change: The capacity adjustment to apply in this interval. The number is interpreted differently based on AdjustmentType: - ChangeInCapacity: add the adjustment to the current capacity. The number can be positive or negative. - PercentChangeInCapacity: add or remove the given percentage of the current capacity to itself. The number can be in the range [-100..100]. - ExactCapacity: set the capacity to this number. The number must be positive.
        :param lower: The lower bound of the interval. The scaling adjustment will be applied if the metric is higher than this value. Default: Threshold automatically derived from neighbouring intervals
        :param upper: The upper bound of the interval. The scaling adjustment will be applied if the metric is lower than this value. Default: Threshold automatically derived from neighbouring intervals

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_autoscaling_common as autoscaling_common
            
            scaling_interval = autoscaling_common.ScalingInterval(
                change=123,
            
                # the properties below are optional
                lower=123,
                upper=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1471419b50dcbf2a2d82cb0eaa8b1a900d152953019294ad8b7a326fdf03f2a)
            check_type(argname="argument change", value=change, expected_type=type_hints["change"])
            check_type(argname="argument lower", value=lower, expected_type=type_hints["lower"])
            check_type(argname="argument upper", value=upper, expected_type=type_hints["upper"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "change": change,
        }
        if lower is not None:
            self._values["lower"] = lower
        if upper is not None:
            self._values["upper"] = upper

    @builtins.property
    def change(self) -> jsii.Number:
        '''The capacity adjustment to apply in this interval.

        The number is interpreted differently based on AdjustmentType:

        - ChangeInCapacity: add the adjustment to the current capacity.
          The number can be positive or negative.
        - PercentChangeInCapacity: add or remove the given percentage of the current
          capacity to itself. The number can be in the range [-100..100].
        - ExactCapacity: set the capacity to this number. The number must
          be positive.
        '''
        result = self._values.get("change")
        assert result is not None, "Required property 'change' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def lower(self) -> typing.Optional[jsii.Number]:
        '''The lower bound of the interval.

        The scaling adjustment will be applied if the metric is higher than this value.

        :default: Threshold automatically derived from neighbouring intervals
        '''
        result = self._values.get("lower")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def upper(self) -> typing.Optional[jsii.Number]:
        '''The upper bound of the interval.

        The scaling adjustment will be applied if the metric is lower than this value.

        :default: Threshold automatically derived from neighbouring intervals
        '''
        result = self._values.get("upper")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ScalingInterval(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "Alarms",
    "ArbitraryIntervals",
    "CompleteScalingInterval",
    "IRandomGenerator",
    "ScalingInterval",
]

publication.publish()

def _typecheckingstub__abf78afeb9ac8e8462332fca79fe9b5fffea8d7bfa2ff758f5d7a5e7602ad7f6(
    *,
    lower_alarm_interval_index: typing.Optional[jsii.Number] = None,
    upper_alarm_interval_index: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57995ea3409b19529dee8383d66d29b069590c52cb741f0e8ae75b7bc40af361(
    *,
    absolute: builtins.bool,
    intervals: typing.Sequence[typing.Union[ScalingInterval, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dcfdc3d9397619d127fb623a33ade65cb15bfd29863b7d524d449180f466014(
    *,
    lower: jsii.Number,
    upper: jsii.Number,
    change: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f79c181fb4012fc3ec659257628da3b8d1a60516f0b95625926cb8a6b56f8b(
    min: jsii.Number,
    max: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1471419b50dcbf2a2d82cb0eaa8b1a900d152953019294ad8b7a326fdf03f2a(
    *,
    change: jsii.Number,
    lower: typing.Optional[jsii.Number] = None,
    upper: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
