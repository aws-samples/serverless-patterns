'''
# AWS::AppRunner Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_apprunner as apprunner
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppRunner construct libraries](https://constructs.dev/search?q=apprunner)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppRunner resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppRunner.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-apprunner-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppRunner](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppRunner.html).

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
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnAutoScalingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnAutoScalingConfiguration",
):
    '''Specify an AWS App Runner Automatic Scaling configuration by using the ``AWS::AppRunner::AutoScalingConfiguration`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::AutoScalingConfiguration`` resource is an AWS App Runner resource type that specifies an App Runner automatic scaling configuration.

    App Runner requires this resource to set non-default auto scaling settings for instances used to process the web requests. You can share an auto scaling configuration across multiple services.

    Create multiple revisions of a configuration by calling this action multiple times using the same ``AutoScalingConfigurationName`` . The call returns incremental ``AutoScalingConfigurationRevision`` values. When you create a service and configure an auto scaling configuration resource, the service uses the latest active revision of the auto scaling configuration by default. You can optionally configure the service to use a specific revision.

    Configure a higher ``MinSize`` to increase the spread of your App Runner service over more Availability Zones in the AWS Region . The tradeoff is a higher minimal cost.

    Configure a lower ``MaxSize`` to control your cost. The tradeoff is lower responsiveness during peak demand.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_auto_scaling_configuration = apprunner.CfnAutoScalingConfiguration(self, "MyCfnAutoScalingConfiguration",
            auto_scaling_configuration_name="autoScalingConfigurationName",
            max_concurrency=123,
            max_size=123,
            min_size=123,
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
        auto_scaling_configuration_name: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param auto_scaling_configuration_name: The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.
        :param max_concurrency: The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up.
        :param max_size: The maximum number of instances that a service scales up to. At most ``MaxSize`` instances actively serve traffic for your service.
        :param min_size: The minimum number of instances that App Runner provisions for a service. The service always has at least ``MinSize`` provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset. App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.
        :param tags: A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a097973cb063319e04b0f6e6c21b4cfd5c92b8418d4ae98fd7a13b5ef4bed0e8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAutoScalingConfigurationProps(
            auto_scaling_configuration_name=auto_scaling_configuration_name,
            max_concurrency=max_concurrency,
            max_size=max_size,
            min_size=min_size,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543708ceb6604b166bc6eed37718011031e49891f6312bd156560547d85091a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5274d724f0f7ae4be497d58f3e9e326d502d1ea6864cfb94650b4339848ad179)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAutoScalingConfigurationArn")
    def attr_auto_scaling_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this auto scaling configuration.

        :cloudformationAttribute: AutoScalingConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAutoScalingConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAutoScalingConfigurationRevision")
    def attr_auto_scaling_configuration_revision(self) -> jsii.Number:
        '''The revision of this auto scaling configuration.

        It's unique among all the active configurations that share the same ``AutoScalingConfigurationName`` .

        :cloudformationAttribute: AutoScalingConfigurationRevision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAutoScalingConfigurationRevision"))

    @builtins.property
    @jsii.member(jsii_name="attrLatest")
    def attr_latest(self) -> _IResolvable_da3f097b:
        '''It's set to true for the configuration with the highest ``Revision`` among all configurations that share the same ``AutoScalingConfigurationName`` .

        It's set to false otherwise. App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.

        :cloudformationAttribute: Latest
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLatest"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="autoScalingConfigurationName")
    def auto_scaling_configuration_name(self) -> typing.Optional[builtins.str]:
        '''The customer-provided auto scaling configuration name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationName"))

    @auto_scaling_configuration_name.setter
    def auto_scaling_configuration_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e356312a777bbadb57bd63f0dfc33fb70c5d8e557376009f249840b11d66bd5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrency")
    def max_concurrency(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of concurrent requests that an instance processes.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrency"))

    @max_concurrency.setter
    def max_concurrency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__283d39757b13fe904a4b3d64120221a2d431ba2ec1d757638e1c345e78c3f7cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrency", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances that a service scales up to.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b95fc2bf6f77f9647d9a90116b7d9f7e048c77120c45dd9da79cf0fac82b8f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances that App Runner provisions for a service.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__804986513a4dd9744a0afef975cf1e8a6c7345cb309f071e4ff0a913123c0fcf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your auto scaling configuration resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb90876342a230c9991099f852e8e245b9b8c860b209c3ebdfa443bf9af5660a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnAutoScalingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "auto_scaling_configuration_name": "autoScalingConfigurationName",
        "max_concurrency": "maxConcurrency",
        "max_size": "maxSize",
        "min_size": "minSize",
        "tags": "tags",
    },
)
class CfnAutoScalingConfigurationProps:
    def __init__(
        self,
        *,
        auto_scaling_configuration_name: typing.Optional[builtins.str] = None,
        max_concurrency: typing.Optional[jsii.Number] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAutoScalingConfiguration``.

        :param auto_scaling_configuration_name: The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.
        :param max_concurrency: The maximum number of concurrent requests that an instance processes. If the number of concurrent requests exceeds this limit, App Runner scales the service up.
        :param max_size: The maximum number of instances that a service scales up to. At most ``MaxSize`` instances actively serve traffic for your service.
        :param min_size: The minimum number of instances that App Runner provisions for a service. The service always has at least ``MinSize`` provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset. App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.
        :param tags: A list of metadata items that you can associate with your auto scaling configuration resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_auto_scaling_configuration_props = apprunner.CfnAutoScalingConfigurationProps(
                auto_scaling_configuration_name="autoScalingConfigurationName",
                max_concurrency=123,
                max_size=123,
                min_size=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d64ff92813f3f968746f4f41c6f17d2e277154809c684b9c520b7ab47bbcdfb7)
            check_type(argname="argument auto_scaling_configuration_name", value=auto_scaling_configuration_name, expected_type=type_hints["auto_scaling_configuration_name"])
            check_type(argname="argument max_concurrency", value=max_concurrency, expected_type=type_hints["max_concurrency"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if auto_scaling_configuration_name is not None:
            self._values["auto_scaling_configuration_name"] = auto_scaling_configuration_name
        if max_concurrency is not None:
            self._values["max_concurrency"] = max_concurrency
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def auto_scaling_configuration_name(self) -> typing.Optional[builtins.str]:
        '''The customer-provided auto scaling configuration name.

        It can be used in multiple revisions of a configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-autoscalingconfigurationname
        '''
        result = self._values.get("auto_scaling_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrency(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of concurrent requests that an instance processes.

        If the number of concurrent requests exceeds this limit, App Runner scales the service up.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-maxconcurrency
        '''
        result = self._values.get("max_concurrency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances that a service scales up to.

        At most ``MaxSize`` instances actively serve traffic for your service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-maxsize
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances that App Runner provisions for a service.

        The service always has at least ``MinSize`` provisioned instances. Some of them actively serve traffic. The rest of them (provisioned and inactive instances) are a cost-effective compute capacity reserve and are ready to be quickly activated. You pay for memory usage of all the provisioned instances. You pay for CPU usage of only the active subset.

        App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-minsize
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your auto scaling configuration resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-autoscalingconfiguration.html#cfn-apprunner-autoscalingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAutoScalingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnObservabilityConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnObservabilityConfiguration",
):
    '''Specify an AWS App Runner observability configuration by using the ``AWS::AppRunner::ObservabilityConfiguration`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::ObservabilityConfiguration`` resource is an AWS App Runner resource type that specifies an App Runner observability configuration.

    App Runner requires this resource when you specify App Runner services and you want to enable non-default observability features. You can share an observability configuration across multiple services.

    Create multiple revisions of a configuration by specifying this resource multiple times using the same ``ObservabilityConfigurationName`` . App Runner creates multiple resources with incremental ``ObservabilityConfigurationRevision`` values. When you specify a service and configure an observability configuration resource, the service uses the latest active revision of the observability configuration by default. You can optionally configure the service to use a specific revision.

    The observability configuration resource is designed to configure multiple features (currently one feature, tracing). This resource takes optional parameters that describe the configuration of these features (currently one parameter, ``TraceConfiguration`` ). If you don't specify a feature parameter, App Runner doesn't enable the feature.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_observability_configuration = apprunner.CfnObservabilityConfiguration(self, "MyCfnObservabilityConfiguration",
            observability_configuration_name="observabilityConfigurationName",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trace_configuration=apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty(
                vendor="vendor"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        observability_configuration_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnObservabilityConfiguration.TraceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param observability_configuration_name: A name for the observability configuration. When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. .. epigraph:: The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it. When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service. If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.
        :param tags: A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        :param trace_configuration: The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b238f814243acf19fa88af79842810e60380a88ae9065727ec71a1f3e03c1798)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnObservabilityConfigurationProps(
            observability_configuration_name=observability_configuration_name,
            tags=tags,
            trace_configuration=trace_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7573b8057d1f727c6f989a8a051a5419de5cb4e5bfba9e84827ba331b857930b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__85d3e6ee4fc274cb1c65005b12130712ef169b4fb6b51f4a4df5ba7ba8373c53)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLatest")
    def attr_latest(self) -> _IResolvable_da3f097b:
        '''It's set to ``true`` for the configuration with the highest ``Revision`` among all configurations that share the same ``ObservabilityConfigurationName`` .

        It's set to ``false`` otherwise.

        :cloudformationAttribute: Latest
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrLatest"))

    @builtins.property
    @jsii.member(jsii_name="attrObservabilityConfigurationArn")
    def attr_observability_configuration_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this observability configuration.

        :cloudformationAttribute: ObservabilityConfigurationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrObservabilityConfigurationArn"))

    @builtins.property
    @jsii.member(jsii_name="attrObservabilityConfigurationRevision")
    def attr_observability_configuration_revision(self) -> jsii.Number:
        '''The revision of this observability configuration.

        It's unique among all the active configurations ( ``"Status": "ACTIVE"`` ) that share the same ``ObservabilityConfigurationName`` .

        :cloudformationAttribute: ObservabilityConfigurationRevision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrObservabilityConfigurationRevision"))

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
    @jsii.member(jsii_name="observabilityConfigurationName")
    def observability_configuration_name(self) -> typing.Optional[builtins.str]:
        '''A name for the observability configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "observabilityConfigurationName"))

    @observability_configuration_name.setter
    def observability_configuration_name(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c26a7cba97d979e2a8926b0558d823516db0c33215fa2d3d69c31dbda532dc09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "observabilityConfigurationName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your observability configuration resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce47e83931668ff51ac71d820c33d01c438549553e61f61b5004c469dc989b24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="traceConfiguration")
    def trace_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObservabilityConfiguration.TraceConfigurationProperty"]]:
        '''The configuration of the tracing feature within this observability configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObservabilityConfiguration.TraceConfigurationProperty"]], jsii.get(self, "traceConfiguration"))

    @trace_configuration.setter
    def trace_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnObservabilityConfiguration.TraceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bd55266808c4e55e36644c988b23fab8e1251933cfea55aef9c05afb1e4df38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "traceConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vendor": "vendor"},
    )
    class TraceConfigurationProperty:
        def __init__(self, *, vendor: builtins.str) -> None:
            '''Describes the configuration of the tracing feature within an AWS App Runner observability configuration.

            :param vendor: The implementation provider chosen for tracing App Runner services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                trace_configuration_property = apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty(
                    vendor="vendor"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e60603c83c7c60d6c57801b50c84000528fb34ca799fc3840032663efef1221a)
                check_type(argname="argument vendor", value=vendor, expected_type=type_hints["vendor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "vendor": vendor,
            }

        @builtins.property
        def vendor(self) -> builtins.str:
            '''The implementation provider chosen for tracing App Runner services.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-observabilityconfiguration-traceconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration-vendor
            '''
            result = self._values.get("vendor")
            assert result is not None, "Required property 'vendor' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TraceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnObservabilityConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "observability_configuration_name": "observabilityConfigurationName",
        "tags": "tags",
        "trace_configuration": "traceConfiguration",
    },
)
class CfnObservabilityConfigurationProps:
    def __init__(
        self,
        *,
        observability_configuration_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObservabilityConfiguration.TraceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnObservabilityConfiguration``.

        :param observability_configuration_name: A name for the observability configuration. When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration. .. epigraph:: The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it. When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service. If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.
        :param tags: A list of metadata items that you can associate with your observability configuration resource. A tag is a key-value pair.
        :param trace_configuration: The configuration of the tracing feature within this observability configuration. If you don't specify it, App Runner doesn't enable tracing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_observability_configuration_props = apprunner.CfnObservabilityConfigurationProps(
                observability_configuration_name="observabilityConfigurationName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trace_configuration=apprunner.CfnObservabilityConfiguration.TraceConfigurationProperty(
                    vendor="vendor"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1debdf716fbe9ec809b1573ccbd25ac6c6aa5901a77a6b6c323eb8445dd9cc2)
            check_type(argname="argument observability_configuration_name", value=observability_configuration_name, expected_type=type_hints["observability_configuration_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trace_configuration", value=trace_configuration, expected_type=type_hints["trace_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if observability_configuration_name is not None:
            self._values["observability_configuration_name"] = observability_configuration_name
        if tags is not None:
            self._values["tags"] = tags
        if trace_configuration is not None:
            self._values["trace_configuration"] = trace_configuration

    @builtins.property
    def observability_configuration_name(self) -> typing.Optional[builtins.str]:
        '''A name for the observability configuration.

        When you use it for the first time in an AWS Region , App Runner creates revision number ``1`` of this name. When you use the same name in subsequent calls, App Runner creates incremental revisions of the configuration.
        .. epigraph::

           The name ``DefaultConfiguration`` is reserved. You can't use it to create a new observability configuration, and you can't create a revision of it.

           When you want to use your own observability configuration for your App Runner service, *create a configuration with a different name* , and then provide it when you create or update your service.

        If you don't specify a name, AWS CloudFormation generates a name for your observability configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-observabilityconfigurationname
        '''
        result = self._values.get("observability_configuration_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your observability configuration resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trace_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnObservabilityConfiguration.TraceConfigurationProperty]]:
        '''The configuration of the tracing feature within this observability configuration.

        If you don't specify it, App Runner doesn't enable tracing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-observabilityconfiguration.html#cfn-apprunner-observabilityconfiguration-traceconfiguration
        '''
        result = self._values.get("trace_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnObservabilityConfiguration.TraceConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnObservabilityConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnService(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnService",
):
    '''Specify an AWS App Runner service by using the ``AWS::AppRunner::Service`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::Service`` resource is an AWS App Runner resource type that specifies an App Runner service.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_service = apprunner.CfnService(self, "MyCfnService",
            source_configuration=apprunner.CfnService.SourceConfigurationProperty(
                authentication_configuration=apprunner.CfnService.AuthenticationConfigurationProperty(
                    access_role_arn="accessRoleArn",
                    connection_arn="connectionArn"
                ),
                auto_deployments_enabled=False,
                code_repository=apprunner.CfnService.CodeRepositoryProperty(
                    repository_url="repositoryUrl",
                    source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                        type="type",
                        value="value"
                    ),
        
                    # the properties below are optional
                    code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                        configuration_source="configurationSource",
        
                        # the properties below are optional
                        code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                            runtime="runtime",
        
                            # the properties below are optional
                            build_command="buildCommand",
                            port="port",
                            runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                ),
                image_repository=apprunner.CfnService.ImageRepositoryProperty(
                    image_identifier="imageIdentifier",
                    image_repository_type="imageRepositoryType",
        
                    # the properties below are optional
                    image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                        port="port",
                        runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        start_command="startCommand"
                    )
                )
            ),
        
            # the properties below are optional
            auto_scaling_configuration_arn="autoScalingConfigurationArn",
            encryption_configuration=apprunner.CfnService.EncryptionConfigurationProperty(
                kms_key="kmsKey"
            ),
            health_check_configuration=apprunner.CfnService.HealthCheckConfigurationProperty(
                healthy_threshold=123,
                interval=123,
                path="path",
                protocol="protocol",
                timeout=123,
                unhealthy_threshold=123
            ),
            instance_configuration=apprunner.CfnService.InstanceConfigurationProperty(
                cpu="cpu",
                instance_role_arn="instanceRoleArn",
                memory="memory"
            ),
            network_configuration=apprunner.CfnService.NetworkConfigurationProperty(
                egress_configuration=apprunner.CfnService.EgressConfigurationProperty(
                    egress_type="egressType",
        
                    # the properties below are optional
                    vpc_connector_arn="vpcConnectorArn"
                ),
                ingress_configuration=apprunner.CfnService.IngressConfigurationProperty(
                    is_publicly_accessible=False
                )
            ),
            observability_configuration=apprunner.CfnService.ServiceObservabilityConfigurationProperty(
                observability_enabled=False,
        
                # the properties below are optional
                observability_configuration_arn="observabilityConfigurationArn"
            ),
            service_name="serviceName",
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
        source_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.SourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.EncryptionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        health_check_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.HealthCheckConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.InstanceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.NetworkConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        observability_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.ServiceObservabilityConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param source_configuration: The source to deploy to the App Runner service. It can be a code or an image repository.
        :param auto_scaling_configuration_arn: The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration. Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3`` Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``
        :param encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed key .
        :param health_check_configuration: The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.
        :param instance_configuration: The runtime configuration of instances (scaling units) of your service.
        :param network_configuration: Configuration settings related to network traffic of the web application that the App Runner service runs.
        :param observability_configuration: The observability configuration of your service.
        :param service_name: A name for the App Runner service. It must be unique across all the running App Runner services in your AWS account in the AWS Region . If you don't specify a name, AWS CloudFormation generates a name for your service.
        :param tags: An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f3344ac8fb704588f823f8fe3348e96180ce7161e948774f8ff0039717ac7d1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            source_configuration=source_configuration,
            auto_scaling_configuration_arn=auto_scaling_configuration_arn,
            encryption_configuration=encryption_configuration,
            health_check_configuration=health_check_configuration,
            instance_configuration=instance_configuration,
            network_configuration=network_configuration,
            observability_configuration=observability_configuration,
            service_name=service_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3cf8e51d4eccb32ee3ef3461167841e06a93d9694b1e83f5dc77dbb74162e65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__19aa03b24cc6712dedc0bf27c1e5234ddbcc99a0e361aaca63670154b108f203)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceArn")
    def attr_service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this service.

        :cloudformationAttribute: ServiceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceId")
    def attr_service_id(self) -> builtins.str:
        '''An ID that App Runner generated for this service.

        It's unique within the AWS Region .

        :cloudformationAttribute: ServiceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceUrl")
    def attr_service_url(self) -> builtins.str:
        '''A subdomain URL that App Runner generated for this service.

        You can use this URL to access your service web application.

        :cloudformationAttribute: ServiceUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current state of the App Runner service. These particular values mean the following.

        - ``CREATE_FAILED`` – The service failed to create. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and retry the call to create the service.

        The failed service isn't usable, and still counts towards your service quota. When you're done analyzing the failure, delete the service.

        - ``DELETE_FAILED`` – The service failed to delete and can't be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="sourceConfiguration")
    def source_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnService.SourceConfigurationProperty"]:
        '''The source to deploy to the App Runner service.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnService.SourceConfigurationProperty"], jsii.get(self, "sourceConfiguration"))

    @source_configuration.setter
    def source_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnService.SourceConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f906f3589e623c80d2665ec2f81b5b46a9bfd75fc62158280dc192dc67e9080a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="autoScalingConfigurationArn")
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoScalingConfigurationArn"))

    @auto_scaling_configuration_arn.setter
    def auto_scaling_configuration_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__830032968a02bd9d8caa04a33e010b953e99500f74dbb0205d3bf7810e095356)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingConfigurationArn", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.EncryptionConfigurationProperty"]]:
        '''An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.EncryptionConfigurationProperty"]], jsii.get(self, "encryptionConfiguration"))

    @encryption_configuration.setter
    def encryption_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.EncryptionConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01e3a7e233a752aeff40d77129499d66848c13059c089f87f3bb99c5c1252ec2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckConfiguration")
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.HealthCheckConfigurationProperty"]]:
        '''The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.HealthCheckConfigurationProperty"]], jsii.get(self, "healthCheckConfiguration"))

    @health_check_configuration.setter
    def health_check_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.HealthCheckConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2852aa3e1fcf08cbe02de00601e5be10bd2bac5a7477e1953199f545c46795cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="instanceConfiguration")
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.InstanceConfigurationProperty"]]:
        '''The runtime configuration of instances (scaling units) of your service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.InstanceConfigurationProperty"]], jsii.get(self, "instanceConfiguration"))

    @instance_configuration.setter
    def instance_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.InstanceConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8ee1f12a50b167c1a9699060f4057c41f5a075862c428087001b8d07a6413b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="networkConfiguration")
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.NetworkConfigurationProperty"]]:
        '''Configuration settings related to network traffic of the web application that the App Runner service runs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.NetworkConfigurationProperty"]], jsii.get(self, "networkConfiguration"))

    @network_configuration.setter
    def network_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.NetworkConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af223adf09794f1f0c996dedbd19dd70289a9751ee54ff8b7d4b84ca0192e8a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="observabilityConfiguration")
    def observability_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ServiceObservabilityConfigurationProperty"]]:
        '''The observability configuration of your service.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ServiceObservabilityConfigurationProperty"]], jsii.get(self, "observabilityConfiguration"))

    @observability_configuration.setter
    def observability_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ServiceObservabilityConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d5c2cafccb24b7204e32b739f13c908a8446a7a9ff65741a742b58db4fef347)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "observabilityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="serviceName")
    def service_name(self) -> typing.Optional[builtins.str]:
        '''A name for the App Runner service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serviceName"))

    @service_name.setter
    def service_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76c8ce698d6dc1e05d9ea8ec49310addce6b06b6e33ed66d51296ca06479eb5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the App Runner service resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6597cd10121d1839d04290eed34b55273823d79529be0202ecac53c9024d8b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_role_arn": "accessRoleArn",
            "connection_arn": "connectionArn",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            access_role_arn: typing.Optional[builtins.str] = None,
            connection_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes resources needed to authenticate access to some source repositories.

            The specific resource depends on the repository provider.

            :param access_role_arn: The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories).
            :param connection_arn: The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. It's required for GitHub code repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                authentication_configuration_property = apprunner.CfnService.AuthenticationConfigurationProperty(
                    access_role_arn="accessRoleArn",
                    connection_arn="connectionArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30b5454bc76bfa3acad5b8180bd5d14cae0f0cef45569b007bdd5780adb8b08a)
                check_type(argname="argument access_role_arn", value=access_role_arn, expected_type=type_hints["access_role_arn"])
                check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_role_arn is not None:
                self._values["access_role_arn"] = access_role_arn
            if connection_arn is not None:
                self._values["connection_arn"] = connection_arn

        @builtins.property
        def access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository.

            It's required for ECR image repositories (but not for ECR Public repositories).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-accessrolearn
            '''
            result = self._values.get("access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connection_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository.

            It's required for GitHub code repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-authenticationconfiguration.html#cfn-apprunner-service-authenticationconfiguration-connectionarn
            '''
            result = self._values.get("connection_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.CodeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "configuration_source": "configurationSource",
            "code_configuration_values": "codeConfigurationValues",
        },
    )
    class CodeConfigurationProperty:
        def __init__(
            self,
            *,
            configuration_source: builtins.str,
            code_configuration_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.CodeConfigurationValuesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the configuration that AWS App Runner uses to build and run an App Runner service from a source code repository.

            :param configuration_source: The source of the App Runner configuration. Values are interpreted as follows:. - ``REPOSITORY`` – App Runner reads configuration values from the ``apprunner.yaml`` file in the source code repository and ignores ``CodeConfigurationValues`` . - ``API`` – App Runner uses configuration values provided in ``CodeConfigurationValues`` and ignores the ``apprunner.yaml`` file in the source code repository.
            :param code_configuration_values: The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a ``apprunner.yaml`` file in the source code repository (or ignoring the file if it exists).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                code_configuration_property = apprunner.CfnService.CodeConfigurationProperty(
                    configuration_source="configurationSource",
                
                    # the properties below are optional
                    code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                        runtime="runtime",
                
                        # the properties below are optional
                        build_command="buildCommand",
                        port="port",
                        runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        start_command="startCommand"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bdc80c8b1b9fde246d05e948f871c86f580cb4c5a42e76d87cac13d2da0f0d88)
                check_type(argname="argument configuration_source", value=configuration_source, expected_type=type_hints["configuration_source"])
                check_type(argname="argument code_configuration_values", value=code_configuration_values, expected_type=type_hints["code_configuration_values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "configuration_source": configuration_source,
            }
            if code_configuration_values is not None:
                self._values["code_configuration_values"] = code_configuration_values

        @builtins.property
        def configuration_source(self) -> builtins.str:
            '''The source of the App Runner configuration. Values are interpreted as follows:.

            - ``REPOSITORY`` – App Runner reads configuration values from the ``apprunner.yaml`` file in the source code repository and ignores ``CodeConfigurationValues`` .
            - ``API`` – App Runner uses configuration values provided in ``CodeConfigurationValues`` and ignores the ``apprunner.yaml`` file in the source code repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-configurationsource
            '''
            result = self._values.get("configuration_source")
            assert result is not None, "Required property 'configuration_source' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def code_configuration_values(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.CodeConfigurationValuesProperty"]]:
            '''The basic configuration for building and running the App Runner service.

            Use it to quickly launch an App Runner service without providing a ``apprunner.yaml`` file in the source code repository (or ignoring the file if it exists).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfiguration.html#cfn-apprunner-service-codeconfiguration-codeconfigurationvalues
            '''
            result = self._values.get("code_configuration_values")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.CodeConfigurationValuesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.CodeConfigurationValuesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "runtime": "runtime",
            "build_command": "buildCommand",
            "port": "port",
            "runtime_environment_secrets": "runtimeEnvironmentSecrets",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class CodeConfigurationValuesProperty:
        def __init__(
            self,
            *,
            runtime: builtins.str,
            build_command: typing.Optional[builtins.str] = None,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.KeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            runtime_environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.KeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the basic configuration needed for building and running an AWS App Runner service.

            This type doesn't support the full set of possible configuration options. Fur full configuration capabilities, use a ``apprunner.yaml`` file in the source code repository.

            :param runtime: A runtime environment type for building and running an App Runner service. It represents a programming language runtime.
            :param build_command: The command App Runner runs to build your application.
            :param port: The port that your application listens to in the container. Default: ``8080``
            :param runtime_environment_secrets: An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store. .. epigraph:: - If the AWS Systems Manager Parameter Store parameter exists in the same AWS Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified. - Currently, cross account referencing of AWS Systems Manager Parameter Store parameter is not supported.
            :param runtime_environment_variables: The environment variables that are available to your running AWS App Runner service. An array of key-value pairs.
            :param start_command: The command App Runner runs to start your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                code_configuration_values_property = apprunner.CfnService.CodeConfigurationValuesProperty(
                    runtime="runtime",
                
                    # the properties below are optional
                    build_command="buildCommand",
                    port="port",
                    runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                        name="name",
                        value="value"
                    )],
                    runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                        name="name",
                        value="value"
                    )],
                    start_command="startCommand"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ff281e24562ce64ca7e6650ff7d53db9017e2cd96873b1811de38a0d9e93f8d)
                check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
                check_type(argname="argument build_command", value=build_command, expected_type=type_hints["build_command"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument runtime_environment_secrets", value=runtime_environment_secrets, expected_type=type_hints["runtime_environment_secrets"])
                check_type(argname="argument runtime_environment_variables", value=runtime_environment_variables, expected_type=type_hints["runtime_environment_variables"])
                check_type(argname="argument start_command", value=start_command, expected_type=type_hints["start_command"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "runtime": runtime,
            }
            if build_command is not None:
                self._values["build_command"] = build_command
            if port is not None:
                self._values["port"] = port
            if runtime_environment_secrets is not None:
                self._values["runtime_environment_secrets"] = runtime_environment_secrets
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def runtime(self) -> builtins.str:
            '''A runtime environment type for building and running an App Runner service.

            It represents a programming language runtime.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtime
            '''
            result = self._values.get("runtime")
            assert result is not None, "Required property 'runtime' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def build_command(self) -> typing.Optional[builtins.str]:
            '''The command App Runner runs to build your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-buildcommand
            '''
            result = self._values.get("build_command")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port that your application listens to in the container.

            Default: ``8080``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_secrets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]]:
            '''An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable.

            The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
            .. epigraph::

               - If the AWS Systems Manager Parameter Store parameter exists in the same AWS Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
               - Currently, cross account referencing of AWS Systems Manager Parameter Store parameter is not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentsecrets
            '''
            result = self._values.get("runtime_environment_secrets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]]:
            '''The environment variables that are available to your running AWS App Runner service.

            An array of key-value pairs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''The command App Runner runs to start your application.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-codeconfigurationvalues.html#cfn-apprunner-service-codeconfigurationvalues-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeConfigurationValuesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.CodeRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "repository_url": "repositoryUrl",
            "source_code_version": "sourceCodeVersion",
            "code_configuration": "codeConfiguration",
        },
    )
    class CodeRepositoryProperty:
        def __init__(
            self,
            *,
            repository_url: builtins.str,
            source_code_version: typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.SourceCodeVersionProperty", typing.Dict[builtins.str, typing.Any]]],
            code_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.CodeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a source code repository.

            :param repository_url: The location of the repository that contains the source code.
            :param source_code_version: The version that should be used within the source code repository.
            :param code_configuration: Configuration for building and running the service from a source code repository. .. epigraph:: ``CodeConfiguration`` is required only for ``CreateService`` request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                code_repository_property = apprunner.CfnService.CodeRepositoryProperty(
                    repository_url="repositoryUrl",
                    source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                        type="type",
                        value="value"
                    ),
                
                    # the properties below are optional
                    code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                        configuration_source="configurationSource",
                
                        # the properties below are optional
                        code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                            runtime="runtime",
                
                            # the properties below are optional
                            build_command="buildCommand",
                            port="port",
                            runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e57d98a975d0c8c64544e6ebe1f5749961d6621131b9650e9c5c571fb374136)
                check_type(argname="argument repository_url", value=repository_url, expected_type=type_hints["repository_url"])
                check_type(argname="argument source_code_version", value=source_code_version, expected_type=type_hints["source_code_version"])
                check_type(argname="argument code_configuration", value=code_configuration, expected_type=type_hints["code_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "repository_url": repository_url,
                "source_code_version": source_code_version,
            }
            if code_configuration is not None:
                self._values["code_configuration"] = code_configuration

        @builtins.property
        def repository_url(self) -> builtins.str:
            '''The location of the repository that contains the source code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-repositoryurl
            '''
            result = self._values.get("repository_url")
            assert result is not None, "Required property 'repository_url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_code_version(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnService.SourceCodeVersionProperty"]:
            '''The version that should be used within the source code repository.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-sourcecodeversion
            '''
            result = self._values.get("source_code_version")
            assert result is not None, "Required property 'source_code_version' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnService.SourceCodeVersionProperty"], result)

        @builtins.property
        def code_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.CodeConfigurationProperty"]]:
            '''Configuration for building and running the service from a source code repository.

            .. epigraph::

               ``CodeConfiguration`` is required only for ``CreateService`` request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-coderepository.html#cfn-apprunner-service-coderepository-codeconfiguration
            '''
            result = self._values.get("code_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.CodeConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CodeRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.EgressConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "egress_type": "egressType",
            "vpc_connector_arn": "vpcConnectorArn",
        },
    )
    class EgressConfigurationProperty:
        def __init__(
            self,
            *,
            egress_type: builtins.str,
            vpc_connector_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes configuration settings related to outbound network traffic of an AWS App Runner service.

            :param egress_type: The type of egress configuration. Set to ``DEFAULT`` for access to resources hosted on public networks. Set to ``VPC`` to associate your service to a custom VPC specified by ``VpcConnectorArn`` .
            :param vpc_connector_arn: The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service. Only valid when ``EgressType = VPC`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                egress_configuration_property = apprunner.CfnService.EgressConfigurationProperty(
                    egress_type="egressType",
                
                    # the properties below are optional
                    vpc_connector_arn="vpcConnectorArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9aa7300a0ca2f45d7ad8f456f3e12ff6d2c58968cda0f6bff5cf32d86beb0a0e)
                check_type(argname="argument egress_type", value=egress_type, expected_type=type_hints["egress_type"])
                check_type(argname="argument vpc_connector_arn", value=vpc_connector_arn, expected_type=type_hints["vpc_connector_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "egress_type": egress_type,
            }
            if vpc_connector_arn is not None:
                self._values["vpc_connector_arn"] = vpc_connector_arn

        @builtins.property
        def egress_type(self) -> builtins.str:
            '''The type of egress configuration.

            Set to ``DEFAULT`` for access to resources hosted on public networks.

            Set to ``VPC`` to associate your service to a custom VPC specified by ``VpcConnectorArn`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-egresstype
            '''
            result = self._values.get("egress_type")
            assert result is not None, "Required property 'egress_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_connector_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service.

            Only valid when ``EgressType = VPC`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-egressconfiguration.html#cfn-apprunner-service-egressconfiguration-vpcconnectorarn
            '''
            result = self._values.get("vpc_connector_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.EncryptionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_key": "kmsKey"},
    )
    class EncryptionConfigurationProperty:
        def __init__(self, *, kms_key: builtins.str) -> None:
            '''Describes a custom encryption key that AWS App Runner uses to encrypt copies of the source repository and service logs.

            :param kms_key: The ARN of the KMS key that's used for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                encryption_configuration_property = apprunner.CfnService.EncryptionConfigurationProperty(
                    kms_key="kmsKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dcf4b087c55d0f65d04bce2a56335fb14d4f38cc947dfe30e76df078b84dd053)
                check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_key": kms_key,
            }

        @builtins.property
        def kms_key(self) -> builtins.str:
            '''The ARN of the KMS key that's used for encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-encryptionconfiguration.html#cfn-apprunner-service-encryptionconfiguration-kmskey
            '''
            result = self._values.get("kms_key")
            assert result is not None, "Required property 'kms_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.HealthCheckConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "healthy_threshold": "healthyThreshold",
            "interval": "interval",
            "path": "path",
            "protocol": "protocol",
            "timeout": "timeout",
            "unhealthy_threshold": "unhealthyThreshold",
        },
    )
    class HealthCheckConfigurationProperty:
        def __init__(
            self,
            *,
            healthy_threshold: typing.Optional[jsii.Number] = None,
            interval: typing.Optional[jsii.Number] = None,
            path: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            timeout: typing.Optional[jsii.Number] = None,
            unhealthy_threshold: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Describes the settings for the health check that AWS App Runner performs to monitor the health of a service.

            :param healthy_threshold: The number of consecutive checks that must succeed before App Runner decides that the service is healthy. Default: ``1``
            :param interval: The time interval, in seconds, between health checks. Default: ``5``
            :param path: The URL that health check requests are sent to. ``Path`` is only applicable when you set ``Protocol`` to ``HTTP`` . Default: ``"/"``
            :param protocol: The IP protocol that App Runner uses to perform health checks for your service. If you set ``Protocol`` to ``HTTP`` , App Runner sends health check requests to the HTTP path specified by ``Path`` . Default: ``TCP``
            :param timeout: The time, in seconds, to wait for a health check response before deciding it failed. Default: ``2``
            :param unhealthy_threshold: The number of consecutive checks that must fail before App Runner decides that the service is unhealthy. Default: ``5``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                health_check_configuration_property = apprunner.CfnService.HealthCheckConfigurationProperty(
                    healthy_threshold=123,
                    interval=123,
                    path="path",
                    protocol="protocol",
                    timeout=123,
                    unhealthy_threshold=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f6c511197949231301c5b4f96bfc5acfeeb4efc21990365c703df50783e284fe)
                check_type(argname="argument healthy_threshold", value=healthy_threshold, expected_type=type_hints["healthy_threshold"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
                check_type(argname="argument unhealthy_threshold", value=unhealthy_threshold, expected_type=type_hints["unhealthy_threshold"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if healthy_threshold is not None:
                self._values["healthy_threshold"] = healthy_threshold
            if interval is not None:
                self._values["interval"] = interval
            if path is not None:
                self._values["path"] = path
            if protocol is not None:
                self._values["protocol"] = protocol
            if timeout is not None:
                self._values["timeout"] = timeout
            if unhealthy_threshold is not None:
                self._values["unhealthy_threshold"] = unhealthy_threshold

        @builtins.property
        def healthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive checks that must succeed before App Runner decides that the service is healthy.

            Default: ``1``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-healthythreshold
            '''
            result = self._values.get("healthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The time interval, in seconds, between health checks.

            Default: ``5``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The URL that health check requests are sent to.

            ``Path`` is only applicable when you set ``Protocol`` to ``HTTP`` .

            Default: ``"/"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The IP protocol that App Runner uses to perform health checks for your service.

            If you set ``Protocol`` to ``HTTP`` , App Runner sends health check requests to the HTTP path specified by ``Path`` .

            Default: ``TCP``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The time, in seconds, to wait for a health check response before deciding it failed.

            Default: ``2``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def unhealthy_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.

            Default: ``5``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-healthcheckconfiguration.html#cfn-apprunner-service-healthcheckconfiguration-unhealthythreshold
            '''
            result = self._values.get("unhealthy_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.ImageConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "port": "port",
            "runtime_environment_secrets": "runtimeEnvironmentSecrets",
            "runtime_environment_variables": "runtimeEnvironmentVariables",
            "start_command": "startCommand",
        },
    )
    class ImageConfigurationProperty:
        def __init__(
            self,
            *,
            port: typing.Optional[builtins.str] = None,
            runtime_environment_secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.KeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            runtime_environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.KeyValuePairProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            start_command: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the configuration that AWS App Runner uses to run an App Runner service using an image pulled from a source image repository.

            :param port: The port that your application listens to in the container. Default: ``8080``
            :param runtime_environment_secrets: An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store. .. epigraph:: - If the AWS Systems Manager Parameter Store parameter exists in the same AWS Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified. - Currently, cross account referencing of AWS Systems Manager Parameter Store parameter is not supported.
            :param runtime_environment_variables: Environment variables that are available to your running App Runner service. An array of key-value pairs.
            :param start_command: An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker image’s default start command.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                image_configuration_property = apprunner.CfnService.ImageConfigurationProperty(
                    port="port",
                    runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                        name="name",
                        value="value"
                    )],
                    runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                        name="name",
                        value="value"
                    )],
                    start_command="startCommand"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b462e731657fa3a312801448c4742df6463407a2dcd5ce1c4ae46c5f7a9db6f3)
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument runtime_environment_secrets", value=runtime_environment_secrets, expected_type=type_hints["runtime_environment_secrets"])
                check_type(argname="argument runtime_environment_variables", value=runtime_environment_variables, expected_type=type_hints["runtime_environment_variables"])
                check_type(argname="argument start_command", value=start_command, expected_type=type_hints["start_command"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if port is not None:
                self._values["port"] = port
            if runtime_environment_secrets is not None:
                self._values["runtime_environment_secrets"] = runtime_environment_secrets
            if runtime_environment_variables is not None:
                self._values["runtime_environment_variables"] = runtime_environment_variables
            if start_command is not None:
                self._values["start_command"] = start_command

        @builtins.property
        def port(self) -> typing.Optional[builtins.str]:
            '''The port that your application listens to in the container.

            Default: ``8080``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def runtime_environment_secrets(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]]:
            '''An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable.

            The supported values are either the full Amazon Resource Name (ARN) of the AWS Secrets Manager secret or the full ARN of the parameter in the AWS Systems Manager Parameter Store.
            .. epigraph::

               - If the AWS Systems Manager Parameter Store parameter exists in the same AWS Region as the service that you're launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
               - Currently, cross account referencing of AWS Systems Manager Parameter Store parameter is not supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentsecrets
            '''
            result = self._values.get("runtime_environment_secrets")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def runtime_environment_variables(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]]:
            '''Environment variables that are available to your running App Runner service.

            An array of key-value pairs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-runtimeenvironmentvariables
            '''
            result = self._values.get("runtime_environment_variables")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnService.KeyValuePairProperty"]]]], result)

        @builtins.property
        def start_command(self) -> typing.Optional[builtins.str]:
            '''An optional command that App Runner runs to start the application in the source image.

            If specified, this command overrides the Docker image’s default start command.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imageconfiguration.html#cfn-apprunner-service-imageconfiguration-startcommand
            '''
            result = self._values.get("start_command")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.ImageRepositoryProperty",
        jsii_struct_bases=[],
        name_mapping={
            "image_identifier": "imageIdentifier",
            "image_repository_type": "imageRepositoryType",
            "image_configuration": "imageConfiguration",
        },
    )
    class ImageRepositoryProperty:
        def __init__(
            self,
            *,
            image_identifier: builtins.str,
            image_repository_type: builtins.str,
            image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.ImageConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes a source image repository.

            :param image_identifier: The identifier of an image. For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see `Pulling an image <https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html>`_ in the *Amazon ECR User Guide* .
            :param image_repository_type: The type of the image repository. This reflects the repository provider and whether the repository is private or public.
            :param image_configuration: Configuration for running the identified image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                image_repository_property = apprunner.CfnService.ImageRepositoryProperty(
                    image_identifier="imageIdentifier",
                    image_repository_type="imageRepositoryType",
                
                    # the properties below are optional
                    image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                        port="port",
                        runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                            name="name",
                            value="value"
                        )],
                        start_command="startCommand"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39e14e61edb5acbf99056085513b11e8b9db8f919d2e4ada418733b25d52b7c4)
                check_type(argname="argument image_identifier", value=image_identifier, expected_type=type_hints["image_identifier"])
                check_type(argname="argument image_repository_type", value=image_repository_type, expected_type=type_hints["image_repository_type"])
                check_type(argname="argument image_configuration", value=image_configuration, expected_type=type_hints["image_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "image_identifier": image_identifier,
                "image_repository_type": image_repository_type,
            }
            if image_configuration is not None:
                self._values["image_configuration"] = image_configuration

        @builtins.property
        def image_identifier(self) -> builtins.str:
            '''The identifier of an image.

            For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see `Pulling an image <https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html>`_ in the *Amazon ECR User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageidentifier
            '''
            result = self._values.get("image_identifier")
            assert result is not None, "Required property 'image_identifier' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_repository_type(self) -> builtins.str:
            '''The type of the image repository.

            This reflects the repository provider and whether the repository is private or public.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imagerepositorytype
            '''
            result = self._values.get("image_repository_type")
            assert result is not None, "Required property 'image_repository_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ImageConfigurationProperty"]]:
            '''Configuration for running the identified image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-imagerepository.html#cfn-apprunner-service-imagerepository-imageconfiguration
            '''
            result = self._values.get("image_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ImageConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageRepositoryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.IngressConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"is_publicly_accessible": "isPubliclyAccessible"},
    )
    class IngressConfigurationProperty:
        def __init__(
            self,
            *,
            is_publicly_accessible: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Network configuration settings for inbound network traffic.

            :param is_publicly_accessible: Specifies whether your App Runner service is publicly accessible. To make the service publicly accessible set it to ``True`` . To make the service privately accessible, from only within an Amazon VPC set it to ``False`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                ingress_configuration_property = apprunner.CfnService.IngressConfigurationProperty(
                    is_publicly_accessible=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b531c1f1e02cf0fb643d9fc867b2df6e13a708713664c32fc4b9fc70f38c4b5e)
                check_type(argname="argument is_publicly_accessible", value=is_publicly_accessible, expected_type=type_hints["is_publicly_accessible"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "is_publicly_accessible": is_publicly_accessible,
            }

        @builtins.property
        def is_publicly_accessible(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether your App Runner service is publicly accessible.

            To make the service publicly accessible set it to ``True`` . To make the service privately accessible, from only within an Amazon VPC set it to ``False`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-ingressconfiguration.html#cfn-apprunner-service-ingressconfiguration-ispubliclyaccessible
            '''
            result = self._values.get("is_publicly_accessible")
            assert result is not None, "Required property 'is_publicly_accessible' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngressConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.InstanceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cpu": "cpu",
            "instance_role_arn": "instanceRoleArn",
            "memory": "memory",
        },
    )
    class InstanceConfigurationProperty:
        def __init__(
            self,
            *,
            cpu: typing.Optional[builtins.str] = None,
            instance_role_arn: typing.Optional[builtins.str] = None,
            memory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the runtime configuration of an AWS App Runner service instance (scaling unit).

            :param cpu: The number of CPU units reserved for each instance of your App Runner service. Default: ``1 vCPU``
            :param instance_role_arn: The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any AWS APIs.
            :param memory: The amount of memory, in MB or GB, reserved for each instance of your App Runner service. Default: ``2 GB``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                instance_configuration_property = apprunner.CfnService.InstanceConfigurationProperty(
                    cpu="cpu",
                    instance_role_arn="instanceRoleArn",
                    memory="memory"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c2ea788bc7a30c83814ed0cbcd539bdaba16e04ffd0e4142985e615d5563cd6)
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument instance_role_arn", value=instance_role_arn, expected_type=type_hints["instance_role_arn"])
                check_type(argname="argument memory", value=memory, expected_type=type_hints["memory"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cpu is not None:
                self._values["cpu"] = cpu
            if instance_role_arn is not None:
                self._values["instance_role_arn"] = instance_role_arn
            if memory is not None:
                self._values["memory"] = memory

        @builtins.property
        def cpu(self) -> typing.Optional[builtins.str]:
            '''The number of CPU units reserved for each instance of your App Runner service.

            Default: ``1 vCPU``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def instance_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service.

            These are permissions that your code needs when it calls any AWS APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-instancerolearn
            '''
            result = self._values.get("instance_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def memory(self) -> typing.Optional[builtins.str]:
            '''The amount of memory, in MB or GB, reserved for each instance of your App Runner service.

            Default: ``2 GB``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-instanceconfiguration.html#cfn-apprunner-service-instanceconfiguration-memory
            '''
            result = self._values.get("memory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.KeyValuePairProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class KeyValuePairProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes a key-value pair, which is a string-to-string mapping.

            :param name: The key name string to map to a value.
            :param value: The value string to which the key name is mapped.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                key_value_pair_property = apprunner.CfnService.KeyValuePairProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad5b38a165675b32873604a58a5b6333391d6020c2ec2524d1a089109b36fa43)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The key name string to map to a value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value string to which the key name is mapped.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-keyvaluepair.html#cfn-apprunner-service-keyvaluepair-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyValuePairProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.NetworkConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "egress_configuration": "egressConfiguration",
            "ingress_configuration": "ingressConfiguration",
        },
    )
    class NetworkConfigurationProperty:
        def __init__(
            self,
            *,
            egress_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.EgressConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ingress_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.IngressConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes configuration settings related to network traffic of an AWS App Runner service.

            Consists of embedded objects for each configurable network feature.

            :param egress_configuration: Network configuration settings for outbound message traffic.
            :param ingress_configuration: Network configuration settings for inbound message traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                network_configuration_property = apprunner.CfnService.NetworkConfigurationProperty(
                    egress_configuration=apprunner.CfnService.EgressConfigurationProperty(
                        egress_type="egressType",
                
                        # the properties below are optional
                        vpc_connector_arn="vpcConnectorArn"
                    ),
                    ingress_configuration=apprunner.CfnService.IngressConfigurationProperty(
                        is_publicly_accessible=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d032584a280064bb60d87b518e3b84a91c70e15015ddb757b83c7545dcc84496)
                check_type(argname="argument egress_configuration", value=egress_configuration, expected_type=type_hints["egress_configuration"])
                check_type(argname="argument ingress_configuration", value=ingress_configuration, expected_type=type_hints["ingress_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if egress_configuration is not None:
                self._values["egress_configuration"] = egress_configuration
            if ingress_configuration is not None:
                self._values["ingress_configuration"] = ingress_configuration

        @builtins.property
        def egress_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.EgressConfigurationProperty"]]:
            '''Network configuration settings for outbound message traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-egressconfiguration
            '''
            result = self._values.get("egress_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.EgressConfigurationProperty"]], result)

        @builtins.property
        def ingress_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.IngressConfigurationProperty"]]:
            '''Network configuration settings for inbound message traffic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-networkconfiguration.html#cfn-apprunner-service-networkconfiguration-ingressconfiguration
            '''
            result = self._values.get("ingress_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.IngressConfigurationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NetworkConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.ServiceObservabilityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "observability_enabled": "observabilityEnabled",
            "observability_configuration_arn": "observabilityConfigurationArn",
        },
    )
    class ServiceObservabilityConfigurationProperty:
        def __init__(
            self,
            *,
            observability_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
            observability_configuration_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Describes the observability configuration of an AWS App Runner service.

            These are additional observability features, like tracing, that you choose to enable. They're configured in a separate resource that you associate with your service.

            :param observability_enabled: When ``true`` , an observability configuration resource is associated with the service, and an ``ObservabilityConfigurationArn`` is specified.
            :param observability_configuration_arn: The Amazon Resource Name (ARN) of the observability configuration that is associated with the service. Specified only when ``ObservabilityEnabled`` is ``true`` . Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3`` Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                service_observability_configuration_property = apprunner.CfnService.ServiceObservabilityConfigurationProperty(
                    observability_enabled=False,
                
                    # the properties below are optional
                    observability_configuration_arn="observabilityConfigurationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11747a926ba64608c74d8a6613e39dc7029d1347c5e88c4498dc163a5720084c)
                check_type(argname="argument observability_enabled", value=observability_enabled, expected_type=type_hints["observability_enabled"])
                check_type(argname="argument observability_configuration_arn", value=observability_configuration_arn, expected_type=type_hints["observability_configuration_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "observability_enabled": observability_enabled,
            }
            if observability_configuration_arn is not None:
                self._values["observability_configuration_arn"] = observability_configuration_arn

        @builtins.property
        def observability_enabled(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''When ``true`` , an observability configuration resource is associated with the service, and an ``ObservabilityConfigurationArn`` is specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityenabled
            '''
            result = self._values.get("observability_enabled")
            assert result is not None, "Required property 'observability_enabled' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def observability_configuration_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the observability configuration that is associated with the service.

            Specified only when ``ObservabilityEnabled`` is ``true`` .

            Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3``

            Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-serviceobservabilityconfiguration.html#cfn-apprunner-service-serviceobservabilityconfiguration-observabilityconfigurationarn
            '''
            result = self._values.get("observability_configuration_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceObservabilityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.SourceCodeVersionProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SourceCodeVersionProperty:
        def __init__(self, *, type: builtins.str, value: builtins.str) -> None:
            '''Identifies a version of code that AWS App Runner refers to within a source code repository.

            :param type: The type of version identifier. For a git-based repository, branches represent versions.
            :param value: A source code version. For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                source_code_version_property = apprunner.CfnService.SourceCodeVersionProperty(
                    type="type",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8e9142c1e1ff6b21306b8295ae86641c592a9ee7f4abb1584e1b81f4c14d228)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of version identifier.

            For a git-based repository, branches represent versions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''A source code version.

            For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourcecodeversion.html#cfn-apprunner-service-sourcecodeversion-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceCodeVersionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnService.SourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_configuration": "authenticationConfiguration",
            "auto_deployments_enabled": "autoDeploymentsEnabled",
            "code_repository": "codeRepository",
            "image_repository": "imageRepository",
        },
    )
    class SourceConfigurationProperty:
        def __init__(
            self,
            *,
            authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            code_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.CodeRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            image_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.ImageRepositoryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Describes the source deployed to an AWS App Runner service.

            It can be a code or an image repository.

            :param authentication_configuration: Describes the resources that are needed to authenticate access to some source repositories.
            :param auto_deployments_enabled: If ``true`` , continuous integration from the source repository is enabled for the App Runner service. Each repository change (including any source code commit or new image version) starts a deployment. Default: App Runner sets to ``false`` for a source image that uses an ECR Public repository or an ECR repository that's in an AWS account other than the one that the service is in. App Runner sets to ``true`` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).
            :param code_repository: The description of a source code repository. You must provide either this member or ``ImageRepository`` (but not both).
            :param image_repository: The description of a source image repository. You must provide either this member or ``CodeRepository`` (but not both).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                source_configuration_property = apprunner.CfnService.SourceConfigurationProperty(
                    authentication_configuration=apprunner.CfnService.AuthenticationConfigurationProperty(
                        access_role_arn="accessRoleArn",
                        connection_arn="connectionArn"
                    ),
                    auto_deployments_enabled=False,
                    code_repository=apprunner.CfnService.CodeRepositoryProperty(
                        repository_url="repositoryUrl",
                        source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                            type="type",
                            value="value"
                        ),
                
                        # the properties below are optional
                        code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                            configuration_source="configurationSource",
                
                            # the properties below are optional
                            code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                                runtime="runtime",
                
                                # the properties below are optional
                                build_command="buildCommand",
                                port="port",
                                runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                                    name="name",
                                    value="value"
                                )],
                                runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                    name="name",
                                    value="value"
                                )],
                                start_command="startCommand"
                            )
                        )
                    ),
                    image_repository=apprunner.CfnService.ImageRepositoryProperty(
                        image_identifier="imageIdentifier",
                        image_repository_type="imageRepositoryType",
                
                        # the properties below are optional
                        image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                            port="port",
                            runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba4fb6cc4d2a777620eb88ed6607040beb32a47eaf68f2d10e8187935bd51b4a)
                check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
                check_type(argname="argument auto_deployments_enabled", value=auto_deployments_enabled, expected_type=type_hints["auto_deployments_enabled"])
                check_type(argname="argument code_repository", value=code_repository, expected_type=type_hints["code_repository"])
                check_type(argname="argument image_repository", value=image_repository, expected_type=type_hints["image_repository"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authentication_configuration is not None:
                self._values["authentication_configuration"] = authentication_configuration
            if auto_deployments_enabled is not None:
                self._values["auto_deployments_enabled"] = auto_deployments_enabled
            if code_repository is not None:
                self._values["code_repository"] = code_repository
            if image_repository is not None:
                self._values["image_repository"] = image_repository

        @builtins.property
        def authentication_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.AuthenticationConfigurationProperty"]]:
            '''Describes the resources that are needed to authenticate access to some source repositories.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-authenticationconfiguration
            '''
            result = self._values.get("authentication_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.AuthenticationConfigurationProperty"]], result)

        @builtins.property
        def auto_deployments_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , continuous integration from the source repository is enabled for the App Runner service.

            Each repository change (including any source code commit or new image version) starts a deployment.

            Default: App Runner sets to ``false`` for a source image that uses an ECR Public repository or an ECR repository that's in an AWS account other than the one that the service is in. App Runner sets to ``true`` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-autodeploymentsenabled
            '''
            result = self._values.get("auto_deployments_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def code_repository(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.CodeRepositoryProperty"]]:
            '''The description of a source code repository.

            You must provide either this member or ``ImageRepository`` (but not both).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-coderepository
            '''
            result = self._values.get("code_repository")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.CodeRepositoryProperty"]], result)

        @builtins.property
        def image_repository(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ImageRepositoryProperty"]]:
            '''The description of a source image repository.

            You must provide either this member or ``CodeRepository`` (but not both).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-service-sourceconfiguration.html#cfn-apprunner-service-sourceconfiguration-imagerepository
            '''
            result = self._values.get("image_repository")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.ImageRepositoryProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "source_configuration": "sourceConfiguration",
        "auto_scaling_configuration_arn": "autoScalingConfigurationArn",
        "encryption_configuration": "encryptionConfiguration",
        "health_check_configuration": "healthCheckConfiguration",
        "instance_configuration": "instanceConfiguration",
        "network_configuration": "networkConfiguration",
        "observability_configuration": "observabilityConfiguration",
        "service_name": "serviceName",
        "tags": "tags",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        source_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        health_check_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.HealthCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        observability_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceObservabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        service_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnService``.

        :param source_configuration: The source to deploy to the App Runner service. It can be a code or an image repository.
        :param auto_scaling_configuration_arn: The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service. If not provided, App Runner associates the latest revision of a default auto scaling configuration. Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3`` Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``
        :param encryption_configuration: An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs. By default, App Runner uses an AWS managed key .
        :param health_check_configuration: The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.
        :param instance_configuration: The runtime configuration of instances (scaling units) of your service.
        :param network_configuration: Configuration settings related to network traffic of the web application that the App Runner service runs.
        :param observability_configuration: The observability configuration of your service.
        :param service_name: A name for the App Runner service. It must be unique across all the running App Runner services in your AWS account in the AWS Region . If you don't specify a name, AWS CloudFormation generates a name for your service.
        :param tags: An optional list of metadata items that you can associate with the App Runner service resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_service_props = apprunner.CfnServiceProps(
                source_configuration=apprunner.CfnService.SourceConfigurationProperty(
                    authentication_configuration=apprunner.CfnService.AuthenticationConfigurationProperty(
                        access_role_arn="accessRoleArn",
                        connection_arn="connectionArn"
                    ),
                    auto_deployments_enabled=False,
                    code_repository=apprunner.CfnService.CodeRepositoryProperty(
                        repository_url="repositoryUrl",
                        source_code_version=apprunner.CfnService.SourceCodeVersionProperty(
                            type="type",
                            value="value"
                        ),
            
                        # the properties below are optional
                        code_configuration=apprunner.CfnService.CodeConfigurationProperty(
                            configuration_source="configurationSource",
            
                            # the properties below are optional
                            code_configuration_values=apprunner.CfnService.CodeConfigurationValuesProperty(
                                runtime="runtime",
            
                                # the properties below are optional
                                build_command="buildCommand",
                                port="port",
                                runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                                    name="name",
                                    value="value"
                                )],
                                runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                    name="name",
                                    value="value"
                                )],
                                start_command="startCommand"
                            )
                        )
                    ),
                    image_repository=apprunner.CfnService.ImageRepositoryProperty(
                        image_identifier="imageIdentifier",
                        image_repository_type="imageRepositoryType",
            
                        # the properties below are optional
                        image_configuration=apprunner.CfnService.ImageConfigurationProperty(
                            port="port",
                            runtime_environment_secrets=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            runtime_environment_variables=[apprunner.CfnService.KeyValuePairProperty(
                                name="name",
                                value="value"
                            )],
                            start_command="startCommand"
                        )
                    )
                ),
            
                # the properties below are optional
                auto_scaling_configuration_arn="autoScalingConfigurationArn",
                encryption_configuration=apprunner.CfnService.EncryptionConfigurationProperty(
                    kms_key="kmsKey"
                ),
                health_check_configuration=apprunner.CfnService.HealthCheckConfigurationProperty(
                    healthy_threshold=123,
                    interval=123,
                    path="path",
                    protocol="protocol",
                    timeout=123,
                    unhealthy_threshold=123
                ),
                instance_configuration=apprunner.CfnService.InstanceConfigurationProperty(
                    cpu="cpu",
                    instance_role_arn="instanceRoleArn",
                    memory="memory"
                ),
                network_configuration=apprunner.CfnService.NetworkConfigurationProperty(
                    egress_configuration=apprunner.CfnService.EgressConfigurationProperty(
                        egress_type="egressType",
            
                        # the properties below are optional
                        vpc_connector_arn="vpcConnectorArn"
                    ),
                    ingress_configuration=apprunner.CfnService.IngressConfigurationProperty(
                        is_publicly_accessible=False
                    )
                ),
                observability_configuration=apprunner.CfnService.ServiceObservabilityConfigurationProperty(
                    observability_enabled=False,
            
                    # the properties below are optional
                    observability_configuration_arn="observabilityConfigurationArn"
                ),
                service_name="serviceName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37772da8e2081252d29ad212c4bce9ca489c11a77271153d93e81976b37d45aa)
            check_type(argname="argument source_configuration", value=source_configuration, expected_type=type_hints["source_configuration"])
            check_type(argname="argument auto_scaling_configuration_arn", value=auto_scaling_configuration_arn, expected_type=type_hints["auto_scaling_configuration_arn"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument health_check_configuration", value=health_check_configuration, expected_type=type_hints["health_check_configuration"])
            check_type(argname="argument instance_configuration", value=instance_configuration, expected_type=type_hints["instance_configuration"])
            check_type(argname="argument network_configuration", value=network_configuration, expected_type=type_hints["network_configuration"])
            check_type(argname="argument observability_configuration", value=observability_configuration, expected_type=type_hints["observability_configuration"])
            check_type(argname="argument service_name", value=service_name, expected_type=type_hints["service_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_configuration": source_configuration,
        }
        if auto_scaling_configuration_arn is not None:
            self._values["auto_scaling_configuration_arn"] = auto_scaling_configuration_arn
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if health_check_configuration is not None:
            self._values["health_check_configuration"] = health_check_configuration
        if instance_configuration is not None:
            self._values["instance_configuration"] = instance_configuration
        if network_configuration is not None:
            self._values["network_configuration"] = network_configuration
        if observability_configuration is not None:
            self._values["observability_configuration"] = observability_configuration
        if service_name is not None:
            self._values["service_name"] = service_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def source_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnService.SourceConfigurationProperty]:
        '''The source to deploy to the App Runner service.

        It can be a code or an image repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-sourceconfiguration
        '''
        result = self._values.get("source_configuration")
        assert result is not None, "Required property 'source_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnService.SourceConfigurationProperty], result)

    @builtins.property
    def auto_scaling_configuration_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with your service.

        If not provided, App Runner associates the latest revision of a default auto scaling configuration.

        Specify an ARN with a name and a revision number to associate that revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability/3``

        Specify just the name to associate the latest revision. For example: ``arn:aws:apprunner:us-east-1:123456789012:autoscalingconfiguration/high-availability``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-autoscalingconfigurationarn
        '''
        result = self._values.get("auto_scaling_configuration_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.EncryptionConfigurationProperty]]:
        '''An optional custom encryption key that App Runner uses to encrypt the copy of your source repository that it maintains and your service logs.

        By default, App Runner uses an AWS managed key .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-encryptionconfiguration
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.EncryptionConfigurationProperty]], result)

    @builtins.property
    def health_check_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.HealthCheckConfigurationProperty]]:
        '''The settings for the health check that AWS App Runner performs to monitor the health of the App Runner service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-healthcheckconfiguration
        '''
        result = self._values.get("health_check_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.HealthCheckConfigurationProperty]], result)

    @builtins.property
    def instance_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.InstanceConfigurationProperty]]:
        '''The runtime configuration of instances (scaling units) of your service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-instanceconfiguration
        '''
        result = self._values.get("instance_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.InstanceConfigurationProperty]], result)

    @builtins.property
    def network_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.NetworkConfigurationProperty]]:
        '''Configuration settings related to network traffic of the web application that the App Runner service runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-networkconfiguration
        '''
        result = self._values.get("network_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.NetworkConfigurationProperty]], result)

    @builtins.property
    def observability_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.ServiceObservabilityConfigurationProperty]]:
        '''The observability configuration of your service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-observabilityconfiguration
        '''
        result = self._values.get("observability_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.ServiceObservabilityConfigurationProperty]], result)

    @builtins.property
    def service_name(self) -> typing.Optional[builtins.str]:
        '''A name for the App Runner service.

        It must be unique across all the running App Runner services in your AWS account in the AWS Region .

        If you don't specify a name, AWS CloudFormation generates a name for your service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-servicename
        '''
        result = self._values.get("service_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the App Runner service resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-service.html#cfn-apprunner-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVpcConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcConnector",
):
    '''Specify an AWS App Runner VPC connector by using the ``AWS::AppRunner::VpcConnector`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::VpcConnector`` resource is an AWS App Runner resource type that specifies an App Runner VPC connector.

    App Runner requires this resource when you want to associate your App Runner service to a custom Amazon Virtual Private Cloud ( Amazon VPC ).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_vpc_connector = apprunner.CfnVpcConnector(self, "MyCfnVpcConnector",
            subnets=["subnets"],
        
            # the properties below are optional
            security_groups=["securityGroups"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_connector_name="vpcConnectorName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        subnets: typing.Sequence[builtins.str],
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_connector_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param subnets: A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify. .. epigraph:: App Runner currently only provides support for IPv4.
        :param security_groups: A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        :param tags: A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        :param vpc_connector_name: A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be589026c3fd7633e7cbbae6a2059ec8d285e62b05b7dce52a6d06b534940bf3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcConnectorProps(
            subnets=subnets,
            security_groups=security_groups,
            tags=tags,
            vpc_connector_name=vpc_connector_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b371f940488f7fa52b8c0a37052f1002b78c797329074722d8cd41d136966b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d1bf179d010e21327b912bc88a37f13c42e0b69b1a0ae11b8ccba53ac85ac73f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcConnectorArn")
    def attr_vpc_connector_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of this VPC connector.

        :cloudformationAttribute: VpcConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcConnectorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcConnectorRevision")
    def attr_vpc_connector_revision(self) -> jsii.Number:
        '''The revision of this VPC connector.

        It's unique among all the active connectors ( ``"Status": "ACTIVE"`` ) that share the same ``Name`` .
        .. epigraph::

           At this time, App Runner supports only one revision per name.

        :cloudformationAttribute: VpcConnectorRevision
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrVpcConnectorRevision"))

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
    @jsii.member(jsii_name="subnets")
    def subnets(self) -> typing.List[builtins.str]:
        '''A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnets"))

    @subnets.setter
    def subnets(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc85cb9354005c37a9ed05d8af5f08ab9efac90811d669fd89b15dfdc01f4e4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnets", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroups")
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroups"))

    @security_groups.setter
    def security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9179e71101f183e34524aa60ee5842981915b91fd8bd3763409dde35761ee21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroups", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your VPC connector resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e48b3594376ff2dc2aa341938ae9d299f6aac12ddb2a5b0aeb8fe1a0aff994a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConnectorName")
    def vpc_connector_name(self) -> typing.Optional[builtins.str]:
        '''A name for the VPC connector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcConnectorName"))

    @vpc_connector_name.setter
    def vpc_connector_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73ecdd2e55710876cadbdcb04b4c04bb7358741703d21df85a608b981ffd28f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConnectorName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "subnets": "subnets",
        "security_groups": "securityGroups",
        "tags": "tags",
        "vpc_connector_name": "vpcConnectorName",
    },
)
class CfnVpcConnectorProps:
    def __init__(
        self,
        *,
        subnets: typing.Sequence[builtins.str],
        security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_connector_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcConnector``.

        :param subnets: A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC. Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify. .. epigraph:: App Runner currently only provides support for IPv4.
        :param security_groups: A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets. If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.
        :param tags: A list of metadata items that you can associate with your VPC connector resource. A tag is a key-value pair.
        :param vpc_connector_name: A name for the VPC connector. If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_vpc_connector_props = apprunner.CfnVpcConnectorProps(
                subnets=["subnets"],
            
                # the properties below are optional
                security_groups=["securityGroups"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_connector_name="vpcConnectorName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3874001d469c9a53bc1ebacc92f127d716349bc989287cfb6de624b3a435282)
            check_type(argname="argument subnets", value=subnets, expected_type=type_hints["subnets"])
            check_type(argname="argument security_groups", value=security_groups, expected_type=type_hints["security_groups"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_connector_name", value=vpc_connector_name, expected_type=type_hints["vpc_connector_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "subnets": subnets,
        }
        if security_groups is not None:
            self._values["security_groups"] = security_groups
        if tags is not None:
            self._values["tags"] = tags
        if vpc_connector_name is not None:
            self._values["vpc_connector_name"] = vpc_connector_name

    @builtins.property
    def subnets(self) -> typing.List[builtins.str]:
        '''A list of IDs of subnets that App Runner should use when it associates your service with a custom Amazon VPC.

        Specify IDs of subnets of a single Amazon VPC. App Runner determines the Amazon VPC from the subnets you specify.
        .. epigraph::

           App Runner currently only provides support for IPv4.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-subnets
        '''
        result = self._values.get("subnets")
        assert result is not None, "Required property 'subnets' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of IDs of security groups that App Runner should use for access to AWS resources under the specified subnets.

        If not specified, App Runner uses the default security group of the Amazon VPC. The default security group allows all outbound traffic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-securitygroups
        '''
        result = self._values.get("security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of metadata items that you can associate with your VPC connector resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_connector_name(self) -> typing.Optional[builtins.str]:
        '''A name for the VPC connector.

        If you don't specify a name, AWS CloudFormation generates a name for your VPC connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcconnector.html#cfn-apprunner-vpcconnector-vpcconnectorname
        '''
        result = self._values.get("vpc_connector_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVpcIngressConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcIngressConnection",
):
    '''Specify an AWS App Runner VPC Ingress Connection by using the ``AWS::AppRunner::VpcIngressConnection`` resource in an AWS CloudFormation template.

    The ``AWS::AppRunner::VpcIngressConnection`` resource is an AWS App Runner resource type that specifies an App Runner VPC Ingress Connection.

    App Runner requires this resource when you want to associate your App Runner service to an Amazon VPC endpoint.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apprunner as apprunner
        
        cfn_vpc_ingress_connection = apprunner.CfnVpcIngressConnection(self, "MyCfnVpcIngressConnection",
            ingress_vpc_configuration=apprunner.CfnVpcIngressConnection.IngressVpcConfigurationProperty(
                vpc_endpoint_id="vpcEndpointId",
                vpc_id="vpcId"
            ),
            service_arn="serviceArn",
        
            # the properties below are optional
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_ingress_connection_name="vpcIngressConnectionName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ingress_vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnVpcIngressConnection.IngressVpcConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        service_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_ingress_connection_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ingress_vpc_configuration: Specifications for the customer’s Amazon VPC and the related AWS PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.
        :param service_arn: The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.
        :param tags: An optional list of metadata items that you can associate with the VPC Ingress Connection resource. A tag is a key-value pair.
        :param vpc_ingress_connection_name: The customer-provided VPC Ingress Connection name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbb5f9e033f465b7f8f245446cf2a67c499f7755bf4e573bb4e74c62012e3eb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcIngressConnectionProps(
            ingress_vpc_configuration=ingress_vpc_configuration,
            service_arn=service_arn,
            tags=tags,
            vpc_ingress_connection_name=vpc_ingress_connection_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f67f9fb8c3bc36500287f4f15ffe9e2aac73bd9264d825a1b8feca96b5ab9947)
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
            type_hints = typing.get_type_hints(_typecheckingstub__81a7c201018ce7d862062f57e76a1eba22f6f743e6df0d2d572da65e50cb8e0f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDomainName")
    def attr_domain_name(self) -> builtins.str:
        '''The domain name associated with the VPC Ingress Connection resource.

        :cloudformationAttribute: DomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of the VPC Ingress Connection.

        The VPC Ingress Connection displays one of the following statuses: ``AVAILABLE`` , ``PENDING_CREATION`` , ``PENDING_DELETION`` , ``FAILED_CREATION`` , ``FAILED_DELETION`` , ``PENDNG_UPDATE`` , ``FAILED_UPDATE`` , and ``DELETED`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcIngressConnectionArn")
    def attr_vpc_ingress_connection_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the VPC Ingress Connection.

        :cloudformationAttribute: VpcIngressConnectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcIngressConnectionArn"))

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
    @jsii.member(jsii_name="ingressVpcConfiguration")
    def ingress_vpc_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnVpcIngressConnection.IngressVpcConfigurationProperty"]:
        '''Specifications for the customer’s Amazon VPC and the related AWS PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnVpcIngressConnection.IngressVpcConfigurationProperty"], jsii.get(self, "ingressVpcConfiguration"))

    @ingress_vpc_configuration.setter
    def ingress_vpc_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnVpcIngressConnection.IngressVpcConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe73cbc5a7819f686471275cf17a497ef6a4bf8e5abc645677efae99b1c050b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressVpcConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="serviceArn")
    def service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceArn"))

    @service_arn.setter
    def service_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d22ffa367118e7d931a0e85912e911ee55aa08d47a290fa3c4ce8c7cb2bfd9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the VPC Ingress Connection resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a0945b23398d82cc256f9ca7475c53f36cd50e0a5efa6f3fba8bcb142420715)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcIngressConnectionName")
    def vpc_ingress_connection_name(self) -> typing.Optional[builtins.str]:
        '''The customer-provided VPC Ingress Connection name.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcIngressConnectionName"))

    @vpc_ingress_connection_name.setter
    def vpc_ingress_connection_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2254246359157fd8f5f145f18ba7aa688c879c038dd392722baf08dbca2caec5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcIngressConnectionName", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcIngressConnection.IngressVpcConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_endpoint_id": "vpcEndpointId", "vpc_id": "vpcId"},
    )
    class IngressVpcConfigurationProperty:
        def __init__(
            self,
            *,
            vpc_endpoint_id: builtins.str,
            vpc_id: builtins.str,
        ) -> None:
            '''Specifications for the customer’s VPC and related PrivateLink VPC endpoint that are used to associate with the VPC Ingress Connection resource.

            :param vpc_endpoint_id: The ID of the VPC endpoint that your App Runner service connects to.
            :param vpc_id: The ID of the VPC that is used for the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apprunner as apprunner
                
                ingress_vpc_configuration_property = apprunner.CfnVpcIngressConnection.IngressVpcConfigurationProperty(
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d93a874adc86f6dd70420bba4844973e5ec9219b31184c142b1e2f968d6b0e0)
                check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "vpc_endpoint_id": vpc_endpoint_id,
                "vpc_id": vpc_id,
            }

        @builtins.property
        def vpc_endpoint_id(self) -> builtins.str:
            '''The ID of the VPC endpoint that your App Runner service connects to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            assert result is not None, "Required property 'vpc_endpoint_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''The ID of the VPC that is used for the VPC endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apprunner-vpcingressconnection-ingressvpcconfiguration.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngressVpcConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apprunner.CfnVpcIngressConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "ingress_vpc_configuration": "ingressVpcConfiguration",
        "service_arn": "serviceArn",
        "tags": "tags",
        "vpc_ingress_connection_name": "vpcIngressConnectionName",
    },
)
class CfnVpcIngressConnectionProps:
    def __init__(
        self,
        *,
        ingress_vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcIngressConnection.IngressVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        service_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_ingress_connection_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcIngressConnection``.

        :param ingress_vpc_configuration: Specifications for the customer’s Amazon VPC and the related AWS PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.
        :param service_arn: The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.
        :param tags: An optional list of metadata items that you can associate with the VPC Ingress Connection resource. A tag is a key-value pair.
        :param vpc_ingress_connection_name: The customer-provided VPC Ingress Connection name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apprunner as apprunner
            
            cfn_vpc_ingress_connection_props = apprunner.CfnVpcIngressConnectionProps(
                ingress_vpc_configuration=apprunner.CfnVpcIngressConnection.IngressVpcConfigurationProperty(
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                ),
                service_arn="serviceArn",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_ingress_connection_name="vpcIngressConnectionName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf477654ff7633b979d8887848a90ba10d61fd01fb42e291521adefbd4d3706)
            check_type(argname="argument ingress_vpc_configuration", value=ingress_vpc_configuration, expected_type=type_hints["ingress_vpc_configuration"])
            check_type(argname="argument service_arn", value=service_arn, expected_type=type_hints["service_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_ingress_connection_name", value=vpc_ingress_connection_name, expected_type=type_hints["vpc_ingress_connection_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ingress_vpc_configuration": ingress_vpc_configuration,
            "service_arn": service_arn,
        }
        if tags is not None:
            self._values["tags"] = tags
        if vpc_ingress_connection_name is not None:
            self._values["vpc_ingress_connection_name"] = vpc_ingress_connection_name

    @builtins.property
    def ingress_vpc_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnVpcIngressConnection.IngressVpcConfigurationProperty]:
        '''Specifications for the customer’s Amazon VPC and the related AWS PrivateLink VPC endpoint that are used to create the VPC Ingress Connection resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-ingressvpcconfiguration
        '''
        result = self._values.get("ingress_vpc_configuration")
        assert result is not None, "Required property 'ingress_vpc_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnVpcIngressConnection.IngressVpcConfigurationProperty], result)

    @builtins.property
    def service_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) for this App Runner service that is used to create the VPC Ingress Connection resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-servicearn
        '''
        result = self._values.get("service_arn")
        assert result is not None, "Required property 'service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An optional list of metadata items that you can associate with the VPC Ingress Connection resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_ingress_connection_name(self) -> typing.Optional[builtins.str]:
        '''The customer-provided VPC Ingress Connection name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apprunner-vpcingressconnection.html#cfn-apprunner-vpcingressconnection-vpcingressconnectionname
        '''
        result = self._values.get("vpc_ingress_connection_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcIngressConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAutoScalingConfiguration",
    "CfnAutoScalingConfigurationProps",
    "CfnObservabilityConfiguration",
    "CfnObservabilityConfigurationProps",
    "CfnService",
    "CfnServiceProps",
    "CfnVpcConnector",
    "CfnVpcConnectorProps",
    "CfnVpcIngressConnection",
    "CfnVpcIngressConnectionProps",
]

publication.publish()

def _typecheckingstub__a097973cb063319e04b0f6e6c21b4cfd5c92b8418d4ae98fd7a13b5ef4bed0e8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    auto_scaling_configuration_name: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_size: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543708ceb6604b166bc6eed37718011031e49891f6312bd156560547d85091a3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5274d724f0f7ae4be497d58f3e9e326d502d1ea6864cfb94650b4339848ad179(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e356312a777bbadb57bd63f0dfc33fb70c5d8e557376009f249840b11d66bd5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__283d39757b13fe904a4b3d64120221a2d431ba2ec1d757638e1c345e78c3f7cf(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b95fc2bf6f77f9647d9a90116b7d9f7e048c77120c45dd9da79cf0fac82b8f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804986513a4dd9744a0afef975cf1e8a6c7345cb309f071e4ff0a913123c0fcf(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb90876342a230c9991099f852e8e245b9b8c860b209c3ebdfa443bf9af5660a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d64ff92813f3f968746f4f41c6f17d2e277154809c684b9c520b7ab47bbcdfb7(
    *,
    auto_scaling_configuration_name: typing.Optional[builtins.str] = None,
    max_concurrency: typing.Optional[jsii.Number] = None,
    max_size: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b238f814243acf19fa88af79842810e60380a88ae9065727ec71a1f3e03c1798(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    observability_configuration_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObservabilityConfiguration.TraceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7573b8057d1f727c6f989a8a051a5419de5cb4e5bfba9e84827ba331b857930b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85d3e6ee4fc274cb1c65005b12130712ef169b4fb6b51f4a4df5ba7ba8373c53(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c26a7cba97d979e2a8926b0558d823516db0c33215fa2d3d69c31dbda532dc09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce47e83931668ff51ac71d820c33d01c438549553e61f61b5004c469dc989b24(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd55266808c4e55e36644c988b23fab8e1251933cfea55aef9c05afb1e4df38(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnObservabilityConfiguration.TraceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60603c83c7c60d6c57801b50c84000528fb34ca799fc3840032663efef1221a(
    *,
    vendor: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1debdf716fbe9ec809b1573ccbd25ac6c6aa5901a77a6b6c323eb8445dd9cc2(
    *,
    observability_configuration_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trace_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnObservabilityConfiguration.TraceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f3344ac8fb704588f823f8fe3348e96180ce7161e948774f8ff0039717ac7d1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    source_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.HealthCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    observability_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceObservabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3cf8e51d4eccb32ee3ef3461167841e06a93d9694b1e83f5dc77dbb74162e65(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19aa03b24cc6712dedc0bf27c1e5234ddbcc99a0e361aaca63670154b108f203(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f906f3589e623c80d2665ec2f81b5b46a9bfd75fc62158280dc192dc67e9080a(
    value: typing.Union[_IResolvable_da3f097b, CfnService.SourceConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__830032968a02bd9d8caa04a33e010b953e99500f74dbb0205d3bf7810e095356(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01e3a7e233a752aeff40d77129499d66848c13059c089f87f3bb99c5c1252ec2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.EncryptionConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2852aa3e1fcf08cbe02de00601e5be10bd2bac5a7477e1953199f545c46795cc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.HealthCheckConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ee1f12a50b167c1a9699060f4057c41f5a075862c428087001b8d07a6413b5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.InstanceConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af223adf09794f1f0c996dedbd19dd70289a9751ee54ff8b7d4b84ca0192e8a9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.NetworkConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d5c2cafccb24b7204e32b739f13c908a8446a7a9ff65741a742b58db4fef347(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.ServiceObservabilityConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76c8ce698d6dc1e05d9ea8ec49310addce6b06b6e33ed66d51296ca06479eb5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6597cd10121d1839d04290eed34b55273823d79529be0202ecac53c9024d8b4(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30b5454bc76bfa3acad5b8180bd5d14cae0f0cef45569b007bdd5780adb8b08a(
    *,
    access_role_arn: typing.Optional[builtins.str] = None,
    connection_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdc80c8b1b9fde246d05e948f871c86f580cb4c5a42e76d87cac13d2da0f0d88(
    *,
    configuration_source: builtins.str,
    code_configuration_values: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.CodeConfigurationValuesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ff281e24562ce64ca7e6650ff7d53db9017e2cd96873b1811de38a0d9e93f8d(
    *,
    runtime: builtins.str,
    build_command: typing.Optional[builtins.str] = None,
    port: typing.Optional[builtins.str] = None,
    runtime_environment_secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.KeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    runtime_environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.KeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    start_command: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e57d98a975d0c8c64544e6ebe1f5749961d6621131b9650e9c5c571fb374136(
    *,
    repository_url: builtins.str,
    source_code_version: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.SourceCodeVersionProperty, typing.Dict[builtins.str, typing.Any]]],
    code_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.CodeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aa7300a0ca2f45d7ad8f456f3e12ff6d2c58968cda0f6bff5cf32d86beb0a0e(
    *,
    egress_type: builtins.str,
    vpc_connector_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcf4b087c55d0f65d04bce2a56335fb14d4f38cc947dfe30e76df078b84dd053(
    *,
    kms_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c511197949231301c5b4f96bfc5acfeeb4efc21990365c703df50783e284fe(
    *,
    healthy_threshold: typing.Optional[jsii.Number] = None,
    interval: typing.Optional[jsii.Number] = None,
    path: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[jsii.Number] = None,
    unhealthy_threshold: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b462e731657fa3a312801448c4742df6463407a2dcd5ce1c4ae46c5f7a9db6f3(
    *,
    port: typing.Optional[builtins.str] = None,
    runtime_environment_secrets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.KeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    runtime_environment_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.KeyValuePairProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    start_command: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39e14e61edb5acbf99056085513b11e8b9db8f919d2e4ada418733b25d52b7c4(
    *,
    image_identifier: builtins.str,
    image_repository_type: builtins.str,
    image_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ImageConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b531c1f1e02cf0fb643d9fc867b2df6e13a708713664c32fc4b9fc70f38c4b5e(
    *,
    is_publicly_accessible: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c2ea788bc7a30c83814ed0cbcd539bdaba16e04ffd0e4142985e615d5563cd6(
    *,
    cpu: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    memory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad5b38a165675b32873604a58a5b6333391d6020c2ec2524d1a089109b36fa43(
    *,
    name: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d032584a280064bb60d87b518e3b84a91c70e15015ddb757b83c7545dcc84496(
    *,
    egress_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.EgressConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.IngressConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11747a926ba64608c74d8a6613e39dc7029d1347c5e88c4498dc163a5720084c(
    *,
    observability_enabled: typing.Union[builtins.bool, _IResolvable_da3f097b],
    observability_configuration_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e9142c1e1ff6b21306b8295ae86641c592a9ee7f4abb1584e1b81f4c14d228(
    *,
    type: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba4fb6cc4d2a777620eb88ed6607040beb32a47eaf68f2d10e8187935bd51b4a(
    *,
    authentication_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_deployments_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    code_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.CodeRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_repository: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ImageRepositoryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37772da8e2081252d29ad212c4bce9ca489c11a77271153d93e81976b37d45aa(
    *,
    source_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.SourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    auto_scaling_configuration_arn: typing.Optional[builtins.str] = None,
    encryption_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.EncryptionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.HealthCheckConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    instance_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.InstanceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.NetworkConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    observability_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.ServiceObservabilityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be589026c3fd7633e7cbbae6a2059ec8d285e62b05b7dce52a6d06b534940bf3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    subnets: typing.Sequence[builtins.str],
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_connector_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b371f940488f7fa52b8c0a37052f1002b78c797329074722d8cd41d136966b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1bf179d010e21327b912bc88a37f13c42e0b69b1a0ae11b8ccba53ac85ac73f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc85cb9354005c37a9ed05d8af5f08ab9efac90811d669fd89b15dfdc01f4e4f(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9179e71101f183e34524aa60ee5842981915b91fd8bd3763409dde35761ee21(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e48b3594376ff2dc2aa341938ae9d299f6aac12ddb2a5b0aeb8fe1a0aff994a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73ecdd2e55710876cadbdcb04b4c04bb7358741703d21df85a608b981ffd28f4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3874001d469c9a53bc1ebacc92f127d716349bc989287cfb6de624b3a435282(
    *,
    subnets: typing.Sequence[builtins.str],
    security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_connector_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbb5f9e033f465b7f8f245446cf2a67c499f7755bf4e573bb4e74c62012e3eb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ingress_vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcIngressConnection.IngressVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    service_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_ingress_connection_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f67f9fb8c3bc36500287f4f15ffe9e2aac73bd9264d825a1b8feca96b5ab9947(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81a7c201018ce7d862062f57e76a1eba22f6f743e6df0d2d572da65e50cb8e0f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe73cbc5a7819f686471275cf17a497ef6a4bf8e5abc645677efae99b1c050b(
    value: typing.Union[_IResolvable_da3f097b, CfnVpcIngressConnection.IngressVpcConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d22ffa367118e7d931a0e85912e911ee55aa08d47a290fa3c4ce8c7cb2bfd9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a0945b23398d82cc256f9ca7475c53f36cd50e0a5efa6f3fba8bcb142420715(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2254246359157fd8f5f145f18ba7aa688c879c038dd392722baf08dbca2caec5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d93a874adc86f6dd70420bba4844973e5ec9219b31184c142b1e2f968d6b0e0(
    *,
    vpc_endpoint_id: builtins.str,
    vpc_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf477654ff7633b979d8887848a90ba10d61fd01fb42e291521adefbd4d3706(
    *,
    ingress_vpc_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnVpcIngressConnection.IngressVpcConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    service_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_ingress_connection_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
