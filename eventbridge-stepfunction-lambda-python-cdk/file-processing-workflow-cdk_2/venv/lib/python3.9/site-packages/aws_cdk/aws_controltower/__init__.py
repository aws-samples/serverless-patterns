'''
# AWS::ControlTower Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_controltower as controltower
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ControlTower construct libraries](https://constructs.dev/search?q=controltower)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ControlTower resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ControlTower.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ControlTower](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ControlTower.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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
    IInspectable as _IInspectable_c2943556,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnEnabledControl(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControl",
):
    '''The resource represents an enabled control.

    It specifies an asynchronous operation that creates AWS resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_controltower as controltower
        
        cfn_enabled_control = controltower.CfnEnabledControl(self, "MyCfnEnabledControl",
            control_identifier="controlIdentifier",
            target_identifier="targetIdentifier"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        control_identifier: builtins.str,
        target_identifier: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param control_identifier: The ARN of the control. Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* guardrail.
        :param target_identifier: The ARN of the organizational unit.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f147c3cf3aed5100105feba92fb41fa040a90e250e566c4f852830a75cfc586)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnabledControlProps(
            control_identifier=control_identifier, target_identifier=target_identifier
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f48fb910d3eecb04d51dd6fcc7cb9241b6efe5d9c5090dd7e2fd56008e8b927d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__261484f697e7db6197c5dc87066a21bee7f59b77e85daa6773dbaf62c8d80eea)
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
    @jsii.member(jsii_name="controlIdentifier")
    def control_identifier(self) -> builtins.str:
        '''The ARN of the control.'''
        return typing.cast(builtins.str, jsii.get(self, "controlIdentifier"))

    @control_identifier.setter
    def control_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8a36ed174761f649221cc9963f7efb537dbfdcc36152637e5c027b145c88fbe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "controlIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="targetIdentifier")
    def target_identifier(self) -> builtins.str:
        '''The ARN of the organizational unit.'''
        return typing.cast(builtins.str, jsii.get(self, "targetIdentifier"))

    @target_identifier.setter
    def target_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9224f8582867a991a7807db81df627cf779770c76fc707cfecf8fd568b7998a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIdentifier", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "control_identifier": "controlIdentifier",
        "target_identifier": "targetIdentifier",
    },
)
class CfnEnabledControlProps:
    def __init__(
        self,
        *,
        control_identifier: builtins.str,
        target_identifier: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnEnabledControl``.

        :param control_identifier: The ARN of the control. Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* guardrail.
        :param target_identifier: The ARN of the organizational unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_controltower as controltower
            
            cfn_enabled_control_props = controltower.CfnEnabledControlProps(
                control_identifier="controlIdentifier",
                target_identifier="targetIdentifier"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e0009029d159859294a7c6bf2b14974d61fd34884bdb5a993abbb2d14cff4f)
            check_type(argname="argument control_identifier", value=control_identifier, expected_type=type_hints["control_identifier"])
            check_type(argname="argument target_identifier", value=target_identifier, expected_type=type_hints["target_identifier"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }

    @builtins.property
    def control_identifier(self) -> builtins.str:
        '''The ARN of the control.

        Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* guardrail.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-controlidentifier
        '''
        result = self._values.get("control_identifier")
        assert result is not None, "Required property 'control_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_identifier(self) -> builtins.str:
        '''The ARN of the organizational unit.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-targetidentifier
        '''
        result = self._values.get("target_identifier")
        assert result is not None, "Required property 'target_identifier' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnabledControlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnabledControl",
    "CfnEnabledControlProps",
]

publication.publish()

def _typecheckingstub__1f147c3cf3aed5100105feba92fb41fa040a90e250e566c4f852830a75cfc586(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f48fb910d3eecb04d51dd6fcc7cb9241b6efe5d9c5090dd7e2fd56008e8b927d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__261484f697e7db6197c5dc87066a21bee7f59b77e85daa6773dbaf62c8d80eea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8a36ed174761f649221cc9963f7efb537dbfdcc36152637e5c027b145c88fbe(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9224f8582867a991a7807db81df627cf779770c76fc707cfecf8fd568b7998a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e0009029d159859294a7c6bf2b14974d61fd34884bdb5a993abbb2d14cff4f(
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
