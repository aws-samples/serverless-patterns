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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEnabledBaseline(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledBaseline",
):
    '''This resource represents a ``Baseline`` that has been applied to a target.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html
    :cloudformationResource: AWS::ControlTower::EnabledBaseline
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_controltower as controltower
        
        # value: Any
        
        cfn_enabled_baseline = controltower.CfnEnabledBaseline(self, "MyCfnEnabledBaseline",
            baseline_identifier="baselineIdentifier",
            baseline_version="baselineVersion",
            target_identifier="targetIdentifier",
        
            # the properties below are optional
            parameters=[controltower.CfnEnabledBaseline.ParameterProperty(
                key="key",
                value=value
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
        baseline_identifier: builtins.str,
        baseline_version: builtins.str,
        target_identifier: builtins.str,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnabledBaseline.ParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param baseline_identifier: The specific ``Baseline`` enabled as part of the ``EnabledBaseline`` resource.
        :param baseline_version: The enabled version of the ``Baseline`` .
        :param target_identifier: The target on which to enable the ``Baseline`` .
        :param parameters: Parameters that are applied when enabling this ``Baseline`` . These parameters configure the behavior of the baseline.
        :param tags: Tags associated with input to ``EnableBaseline`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ea8761029fec1b3c1fb5fb985be9ac741a889e29fe3445cfb5a962436cab528)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnabledBaselineProps(
            baseline_identifier=baseline_identifier,
            baseline_version=baseline_version,
            target_identifier=target_identifier,
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
            type_hints = typing.get_type_hints(_typecheckingstub__5abe9c6604e1de27a08b948cef7b25d1d00ac0fd4f37eae3c69039eafa98f1eb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d058552bbbb5c0f63483ccf116562ca76df6186349bcfda930d4858b8ec89a17)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEnabledBaselineIdentifier")
    def attr_enabled_baseline_identifier(self) -> builtins.str:
        '''The ARN of the ``EnabledBaseline`` resource.

        :cloudformationAttribute: EnabledBaselineIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnabledBaselineIdentifier"))

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
    @jsii.member(jsii_name="baselineIdentifier")
    def baseline_identifier(self) -> builtins.str:
        '''The specific ``Baseline`` enabled as part of the ``EnabledBaseline`` resource.'''
        return typing.cast(builtins.str, jsii.get(self, "baselineIdentifier"))

    @baseline_identifier.setter
    def baseline_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57b2e3563053c046f1ff16bb1039bd1ef2a8fe88dfa1d7e2f7597f4728b4e655)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baselineIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="baselineVersion")
    def baseline_version(self) -> builtins.str:
        '''The enabled version of the ``Baseline`` .'''
        return typing.cast(builtins.str, jsii.get(self, "baselineVersion"))

    @baseline_version.setter
    def baseline_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52d8aafe8b718b522d97264d203dd2054ded5b9659a63bd9d0e8ba81ad6988d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baselineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="targetIdentifier")
    def target_identifier(self) -> builtins.str:
        '''The target on which to enable the ``Baseline`` .'''
        return typing.cast(builtins.str, jsii.get(self, "targetIdentifier"))

    @target_identifier.setter
    def target_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33691a19619ca8f1a07bbce396790320cab38048162971280b54976d64d10b18)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnabledBaseline.ParameterProperty"]]]]:
        '''Parameters that are applied when enabling this ``Baseline`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnabledBaseline.ParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnabledBaseline.ParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85aec378e74e2e896fd36d14071fb0792f36ba92c5c2dbed45d60aed4145fb66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags associated with input to ``EnableBaseline`` .'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a9dd44360aa5f3a328dba2dbcea76058e61fb30293a75243bec51585249eacf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledBaseline.ParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class ParameterProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Any = None,
        ) -> None:
            '''A key-value parameter to an ``EnabledBaseline`` resource.

            :param key: A string denoting the parameter key.
            :param value: A low-level ``Document`` object of any type (for example, a Java Object).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledbaseline-parameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_controltower as controltower
                
                # value: Any
                
                parameter_property = controltower.CfnEnabledBaseline.ParameterProperty(
                    key="key",
                    value=value
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29cd4b6989b5df874eedae62a39653d1a63188dc5b54322534381839629e6b4c)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''A string denoting the parameter key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledbaseline-parameter.html#cfn-controltower-enabledbaseline-parameter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Any:
            '''A low-level ``Document`` object of any type (for example, a Java Object).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledbaseline-parameter.html#cfn-controltower-enabledbaseline-parameter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledBaselineProps",
    jsii_struct_bases=[],
    name_mapping={
        "baseline_identifier": "baselineIdentifier",
        "baseline_version": "baselineVersion",
        "target_identifier": "targetIdentifier",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnEnabledBaselineProps:
    def __init__(
        self,
        *,
        baseline_identifier: builtins.str,
        baseline_version: builtins.str,
        target_identifier: builtins.str,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnabledBaseline.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnabledBaseline``.

        :param baseline_identifier: The specific ``Baseline`` enabled as part of the ``EnabledBaseline`` resource.
        :param baseline_version: The enabled version of the ``Baseline`` .
        :param target_identifier: The target on which to enable the ``Baseline`` .
        :param parameters: Parameters that are applied when enabling this ``Baseline`` . These parameters configure the behavior of the baseline.
        :param tags: Tags associated with input to ``EnableBaseline`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_controltower as controltower
            
            # value: Any
            
            cfn_enabled_baseline_props = controltower.CfnEnabledBaselineProps(
                baseline_identifier="baselineIdentifier",
                baseline_version="baselineVersion",
                target_identifier="targetIdentifier",
            
                # the properties below are optional
                parameters=[controltower.CfnEnabledBaseline.ParameterProperty(
                    key="key",
                    value=value
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cee7d036bdad40a28b228f1094b7badfc14178a44cd291977e709bfab8981cec)
            check_type(argname="argument baseline_identifier", value=baseline_identifier, expected_type=type_hints["baseline_identifier"])
            check_type(argname="argument baseline_version", value=baseline_version, expected_type=type_hints["baseline_version"])
            check_type(argname="argument target_identifier", value=target_identifier, expected_type=type_hints["target_identifier"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "baseline_identifier": baseline_identifier,
            "baseline_version": baseline_version,
            "target_identifier": target_identifier,
        }
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def baseline_identifier(self) -> builtins.str:
        '''The specific ``Baseline`` enabled as part of the ``EnabledBaseline`` resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html#cfn-controltower-enabledbaseline-baselineidentifier
        '''
        result = self._values.get("baseline_identifier")
        assert result is not None, "Required property 'baseline_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def baseline_version(self) -> builtins.str:
        '''The enabled version of the ``Baseline`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html#cfn-controltower-enabledbaseline-baselineversion
        '''
        result = self._values.get("baseline_version")
        assert result is not None, "Required property 'baseline_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_identifier(self) -> builtins.str:
        '''The target on which to enable the ``Baseline`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html#cfn-controltower-enabledbaseline-targetidentifier
        '''
        result = self._values.get("target_identifier")
        assert result is not None, "Required property 'target_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnabledBaseline.ParameterProperty]]]]:
        '''Parameters that are applied when enabling this ``Baseline`` .

        These parameters configure the behavior of the baseline.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html#cfn-controltower-enabledbaseline-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnabledBaseline.ParameterProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags associated with input to ``EnableBaseline`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledbaseline.html#cfn-controltower-enabledbaseline-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnabledBaselineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnEnabledControl(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControl",
):
    '''The resource represents an enabled control.

    It specifies an asynchronous operation that creates AWS resources on the specified organizational unit and the accounts it contains. The resources created will vary according to the control that you specify.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
    :cloudformationResource: AWS::ControlTower::EnabledControl
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_controltower as controltower
        
        # value: Any
        
        cfn_enabled_control = controltower.CfnEnabledControl(self, "MyCfnEnabledControl",
            control_identifier="controlIdentifier",
            target_identifier="targetIdentifier",
        
            # the properties below are optional
            parameters=[controltower.CfnEnabledControl.EnabledControlParameterProperty(
                key="key",
                value=value
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
        control_identifier: builtins.str,
        target_identifier: builtins.str,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnabledControl.EnabledControlParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param control_identifier: The ARN of the control. Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* control. For information on how to find the ``controlIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        :param target_identifier: The ARN of the organizational unit. For information on how to find the ``targetIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        :param parameters: Array of ``EnabledControlParameter`` objects.
        :param tags: Tags to be applied to the enabled control.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f147c3cf3aed5100105feba92fb41fa040a90e250e566c4f852830a75cfc586)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnabledControlProps(
            control_identifier=control_identifier,
            target_identifier=target_identifier,
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
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

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

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnabledControl.EnabledControlParameterProperty"]]]]:
        '''Array of ``EnabledControlParameter`` objects.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnabledControl.EnabledControlParameterProperty"]]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnabledControl.EnabledControlParameterProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d515a7308c280d71a9dde323de4153a28a8fd50c1d63b3e432f221eb67cc226)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to be applied to the enabled control.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbb8154bebca6a968563b4cbc9e3dac6895358c7f3c169f15f270de236454f6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControl.EnabledControlParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class EnabledControlParameterProperty:
        def __init__(self, *, key: builtins.str, value: typing.Any) -> None:
            '''A set of parameters that configure the behavior of the enabled control.

            Expressed as a key/value pair, where ``Key`` is of type ``String`` and ``Value`` is of type ``Document`` .

            :param key: The key of a key/value pair. It is of type ``string`` .
            :param value: The value of a key/value pair. It can be of type ``array`` , ``string`` , ``number`` , ``object`` , or ``boolean`` . [Note: The *Type* field that follows may show a single type such as Number, which is only one possible type.]

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_controltower as controltower
                
                # value: Any
                
                enabled_control_parameter_property = controltower.CfnEnabledControl.EnabledControlParameterProperty(
                    key="key",
                    value=value
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4fcf81607a6c1e1854e0f8d566886b58dcc76d98bca786eda233fcfda5f007e4)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The key of a key/value pair.

            It is of type ``string`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html#cfn-controltower-enabledcontrol-enabledcontrolparameter-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> typing.Any:
            '''The value of a key/value pair.

            It can be of type ``array`` , ``string`` , ``number`` , ``object`` , or ``boolean`` . [Note: The *Type* field that follows may show a single type such as Number, which is only one possible type.]

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-controltower-enabledcontrol-enabledcontrolparameter.html#cfn-controltower-enabledcontrol-enabledcontrolparameter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EnabledControlParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_controltower.CfnEnabledControlProps",
    jsii_struct_bases=[],
    name_mapping={
        "control_identifier": "controlIdentifier",
        "target_identifier": "targetIdentifier",
        "parameters": "parameters",
        "tags": "tags",
    },
)
class CfnEnabledControlProps:
    def __init__(
        self,
        *,
        control_identifier: builtins.str,
        target_identifier: builtins.str,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnabledControl.EnabledControlParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnabledControl``.

        :param control_identifier: The ARN of the control. Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* control. For information on how to find the ``controlIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        :param target_identifier: The ARN of the organizational unit. For information on how to find the ``targetIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .
        :param parameters: Array of ``EnabledControlParameter`` objects.
        :param tags: Tags to be applied to the enabled control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_controltower as controltower
            
            # value: Any
            
            cfn_enabled_control_props = controltower.CfnEnabledControlProps(
                control_identifier="controlIdentifier",
                target_identifier="targetIdentifier",
            
                # the properties below are optional
                parameters=[controltower.CfnEnabledControl.EnabledControlParameterProperty(
                    key="key",
                    value=value
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23e0009029d159859294a7c6bf2b14974d61fd34884bdb5a993abbb2d14cff4f)
            check_type(argname="argument control_identifier", value=control_identifier, expected_type=type_hints["control_identifier"])
            check_type(argname="argument target_identifier", value=target_identifier, expected_type=type_hints["target_identifier"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "control_identifier": control_identifier,
            "target_identifier": target_identifier,
        }
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def control_identifier(self) -> builtins.str:
        '''The ARN of the control.

        Only *Strongly recommended* and *Elective* controls are permitted, with the exception of the *Region deny* control. For information on how to find the ``controlIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-controlidentifier
        '''
        result = self._values.get("control_identifier")
        assert result is not None, "Required property 'control_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_identifier(self) -> builtins.str:
        '''The ARN of the organizational unit.

        For information on how to find the ``targetIdentifier`` , see `the overview page <https://docs.aws.amazon.com//controltower/latest/APIReference/Welcome.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-targetidentifier
        '''
        result = self._values.get("target_identifier")
        assert result is not None, "Required property 'target_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnabledControl.EnabledControlParameterProperty]]]]:
        '''Array of ``EnabledControlParameter`` objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnabledControl.EnabledControlParameterProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to be applied to the enabled control.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-enabledcontrol.html#cfn-controltower-enabledcontrol-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnabledControlProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnLandingZone(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_controltower.CfnLandingZone",
):
    '''Creates a new landing zone.

    This API call starts an asynchronous operation that creates and configures a landing zone, based on the parameters specified in the manifest JSON file.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html
    :cloudformationResource: AWS::ControlTower::LandingZone
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_controltower as controltower
        
        # manifest: Any
        
        cfn_landing_zone = controltower.CfnLandingZone(self, "MyCfnLandingZone",
            manifest=manifest,
            version="version",
        
            # the properties below are optional
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
        manifest: typing.Any,
        version: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param manifest: The landing zone manifest JSON text file that specifies the landing zone configurations.
        :param version: The landing zone's current deployed version.
        :param tags: Tags to be applied to the landing zone.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af3c2c6625c6aae1afd50bbbd83dafe3289d77c3e128938fa7a5e5c8c7ddf150)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLandingZoneProps(manifest=manifest, version=version, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0d56a7dc8ba80b56dd66a841e7e3da6e2e5ff196ed627e202ce0b501f32afe2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bdedd2a6b11698e1ddadd84cf4edea18986d77eb329c8e69790ef015dc016ac0)
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
        '''The ARN of the landing zone.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDriftStatus")
    def attr_drift_status(self) -> builtins.str:
        '''The drift status of the landing zone.

        :cloudformationAttribute: DriftStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDriftStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrLandingZoneIdentifier")
    def attr_landing_zone_identifier(self) -> builtins.str:
        '''The unique identifier of the landing zone.

        :cloudformationAttribute: LandingZoneIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLandingZoneIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrLatestAvailableVersion")
    def attr_latest_available_version(self) -> builtins.str:
        '''The latest available version of the landing zone.

        :cloudformationAttribute: LatestAvailableVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLatestAvailableVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The landing zone deployment status.

        One of ``ACTIVE`` , ``PROCESSING`` , ``FAILED`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="manifest")
    def manifest(self) -> typing.Any:
        '''The landing zone manifest JSON text file that specifies the landing zone configurations.'''
        return typing.cast(typing.Any, jsii.get(self, "manifest"))

    @manifest.setter
    def manifest(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a92b83913378997bcb3264bef174ae6f2a1a9003e0c9e506f3ea364329334ad2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "manifest", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> builtins.str:
        '''The landing zone's current deployed version.'''
        return typing.cast(builtins.str, jsii.get(self, "version"))

    @version.setter
    def version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e32b3e7b64f2950f24c12755b01848b9ebe791c11c2152b740f8f62257157e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to be applied to the landing zone.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74f7c6529f7d31ad5ed3d98ad190f8c0fed87380c25f04fc3e960c88ff73bdaf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_controltower.CfnLandingZoneProps",
    jsii_struct_bases=[],
    name_mapping={"manifest": "manifest", "version": "version", "tags": "tags"},
)
class CfnLandingZoneProps:
    def __init__(
        self,
        *,
        manifest: typing.Any,
        version: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLandingZone``.

        :param manifest: The landing zone manifest JSON text file that specifies the landing zone configurations.
        :param version: The landing zone's current deployed version.
        :param tags: Tags to be applied to the landing zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_controltower as controltower
            
            # manifest: Any
            
            cfn_landing_zone_props = controltower.CfnLandingZoneProps(
                manifest=manifest,
                version="version",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19c72c4436a305fc4b4dfd189564d877d145ce92e0c75f37eafddc778100f13e)
            check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "manifest": manifest,
            "version": version,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def manifest(self) -> typing.Any:
        '''The landing zone manifest JSON text file that specifies the landing zone configurations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-manifest
        '''
        result = self._values.get("manifest")
        assert result is not None, "Required property 'manifest' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def version(self) -> builtins.str:
        '''The landing zone's current deployed version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-version
        '''
        result = self._values.get("version")
        assert result is not None, "Required property 'version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Tags to be applied to the landing zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-controltower-landingzone.html#cfn-controltower-landingzone-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLandingZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnabledBaseline",
    "CfnEnabledBaselineProps",
    "CfnEnabledControl",
    "CfnEnabledControlProps",
    "CfnLandingZone",
    "CfnLandingZoneProps",
]

publication.publish()

def _typecheckingstub__1ea8761029fec1b3c1fb5fb985be9ac741a889e29fe3445cfb5a962436cab528(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    baseline_identifier: builtins.str,
    baseline_version: builtins.str,
    target_identifier: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnabledBaseline.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5abe9c6604e1de27a08b948cef7b25d1d00ac0fd4f37eae3c69039eafa98f1eb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d058552bbbb5c0f63483ccf116562ca76df6186349bcfda930d4858b8ec89a17(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57b2e3563053c046f1ff16bb1039bd1ef2a8fe88dfa1d7e2f7597f4728b4e655(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52d8aafe8b718b522d97264d203dd2054ded5b9659a63bd9d0e8ba81ad6988d2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33691a19619ca8f1a07bbce396790320cab38048162971280b54976d64d10b18(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85aec378e74e2e896fd36d14071fb0792f36ba92c5c2dbed45d60aed4145fb66(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnabledBaseline.ParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9dd44360aa5f3a328dba2dbcea76058e61fb30293a75243bec51585249eacf(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29cd4b6989b5df874eedae62a39653d1a63188dc5b54322534381839629e6b4c(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cee7d036bdad40a28b228f1094b7badfc14178a44cd291977e709bfab8981cec(
    *,
    baseline_identifier: builtins.str,
    baseline_version: builtins.str,
    target_identifier: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnabledBaseline.ParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f147c3cf3aed5100105feba92fb41fa040a90e250e566c4f852830a75cfc586(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnabledControl.EnabledControlParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
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

def _typecheckingstub__4d515a7308c280d71a9dde323de4153a28a8fd50c1d63b3e432f221eb67cc226(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnEnabledControl.EnabledControlParameterProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbb8154bebca6a968563b4cbc9e3dac6895358c7f3c169f15f270de236454f6a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fcf81607a6c1e1854e0f8d566886b58dcc76d98bca786eda233fcfda5f007e4(
    *,
    key: builtins.str,
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23e0009029d159859294a7c6bf2b14974d61fd34884bdb5a993abbb2d14cff4f(
    *,
    control_identifier: builtins.str,
    target_identifier: builtins.str,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnabledControl.EnabledControlParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af3c2c6625c6aae1afd50bbbd83dafe3289d77c3e128938fa7a5e5c8c7ddf150(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    manifest: typing.Any,
    version: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0d56a7dc8ba80b56dd66a841e7e3da6e2e5ff196ed627e202ce0b501f32afe2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdedd2a6b11698e1ddadd84cf4edea18986d77eb329c8e69790ef015dc016ac0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a92b83913378997bcb3264bef174ae6f2a1a9003e0c9e506f3ea364329334ad2(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e32b3e7b64f2950f24c12755b01848b9ebe791c11c2152b740f8f62257157e39(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74f7c6529f7d31ad5ed3d98ad190f8c0fed87380c25f04fc3e960c88ff73bdaf(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19c72c4436a305fc4b4dfd189564d877d145ce92e0c75f37eafddc778100f13e(
    *,
    manifest: typing.Any,
    version: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
