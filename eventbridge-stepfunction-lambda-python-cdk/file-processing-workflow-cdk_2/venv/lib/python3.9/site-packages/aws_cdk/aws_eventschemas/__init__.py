'''
# AWS::EventSchemas Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_eventschemas as eventschemas
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for EventSchemas construct libraries](https://constructs.dev/search?q=eventschemas)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::EventSchemas resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EventSchemas.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::EventSchemas](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_EventSchemas.html).

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
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDiscoverer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnDiscoverer",
):
    '''Use the ``AWS::EventSchemas::Discoverer`` resource to specify a *discoverer* that is associated with an event bus.

    A discoverer allows the Amazon EventBridge Schema Registry to automatically generate schemas based on events on an event bus.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventschemas as eventschemas
        
        cfn_discoverer = eventschemas.CfnDiscoverer(self, "MyCfnDiscoverer",
            source_arn="sourceArn",
        
            # the properties below are optional
            cross_account=False,
            description="description",
            tags=[eventschemas.CfnDiscoverer.TagsEntryProperty(
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
        source_arn: builtins.str,
        cross_account: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnDiscoverer.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param source_arn: The ARN of the event bus.
        :param cross_account: Allows for the discovery of the event schemas that are sent to the event bus from another account.
        :param description: A description for the discoverer.
        :param tags: Tags associated with the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6de86d5a427a463ae500f08a01bbbbb1a7e5c02fcfcd3f1f306367587ea104b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDiscovererProps(
            source_arn=source_arn,
            cross_account=cross_account,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5aed120cd74fca6fbf78a33d62495d891cbe2c2122e7ee9aac1ad880b563510c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e89fa30181b946d0bba0e9220d943a0e33377704225394b1f9d3d14fe912c54b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCrossAccount")
    def attr_cross_account(self) -> _IResolvable_da3f097b:
        '''Defines whether event schemas from other accounts are discovered.

        Default is True.

        :cloudformationAttribute: CrossAccount
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCrossAccount"))

    @builtins.property
    @jsii.member(jsii_name="attrDiscovererArn")
    def attr_discoverer_arn(self) -> builtins.str:
        '''The ARN of the discoverer.

        :cloudformationAttribute: DiscovererArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiscovererArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDiscovererId")
    def attr_discoverer_id(self) -> builtins.str:
        '''The ID of the discoverer.

        :cloudformationAttribute: DiscovererId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDiscovererId"))

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
    @jsii.member(jsii_name="sourceArn")
    def source_arn(self) -> builtins.str:
        '''The ARN of the event bus.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceArn"))

    @source_arn.setter
    def source_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5676db42d7839b4e31ffff3ed613305ba8b0b32d7a6e2629d38eee2586e717fa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="crossAccount")
    def cross_account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Allows for the discovery of the event schemas that are sent to the event bus from another account.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "crossAccount"))

    @cross_account.setter
    def cross_account(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecb4a06e541deb6c8dda40cd09befd814af0290af78146808d35ff87851560c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crossAccount", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the discoverer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7463e2b4b05eced21b83e3338eb22af5c46afefaac9f880d439ba9a57d2eef9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(
        self,
    ) -> typing.Optional[typing.List["CfnDiscoverer.TagsEntryProperty"]]:
        '''Tags associated with the resource.'''
        return typing.cast(typing.Optional[typing.List["CfnDiscoverer.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnDiscoverer.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca041b8aa73b6324baa5d76e21ca40251767aae80510f933254a18d21bdd512b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventschemas.CfnDiscoverer.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Tags to associate with the discoverer.

            :param key: They key of a key-value pair.
            :param value: They value of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventschemas as eventschemas
                
                tags_entry_property = eventschemas.CfnDiscoverer.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8474d9c87ec86399a0d85d3b5386ddc8baf06ba1964693f15122f050ab2c3ea0)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''They key of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''They value of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-discoverer-tagsentry.html#cfn-eventschemas-discoverer-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnDiscovererProps",
    jsii_struct_bases=[],
    name_mapping={
        "source_arn": "sourceArn",
        "cross_account": "crossAccount",
        "description": "description",
        "tags": "tags",
    },
)
class CfnDiscovererProps:
    def __init__(
        self,
        *,
        source_arn: builtins.str,
        cross_account: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnDiscoverer.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDiscoverer``.

        :param source_arn: The ARN of the event bus.
        :param cross_account: Allows for the discovery of the event schemas that are sent to the event bus from another account.
        :param description: A description for the discoverer.
        :param tags: Tags associated with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventschemas as eventschemas
            
            cfn_discoverer_props = eventschemas.CfnDiscovererProps(
                source_arn="sourceArn",
            
                # the properties below are optional
                cross_account=False,
                description="description",
                tags=[eventschemas.CfnDiscoverer.TagsEntryProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__add35f90727b55854c3eefb472afcafa74b28a09aa410e1c3aa8a3128fa89a68)
            check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
            check_type(argname="argument cross_account", value=cross_account, expected_type=type_hints["cross_account"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "source_arn": source_arn,
        }
        if cross_account is not None:
            self._values["cross_account"] = cross_account
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def source_arn(self) -> builtins.str:
        '''The ARN of the event bus.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-sourcearn
        '''
        result = self._values.get("source_arn")
        assert result is not None, "Required property 'source_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cross_account(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Allows for the discovery of the event schemas that are sent to the event bus from another account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-crossaccount
        '''
        result = self._values.get("cross_account")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the discoverer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnDiscoverer.TagsEntryProperty]]:
        '''Tags associated with the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-discoverer.html#cfn-eventschemas-discoverer-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnDiscoverer.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDiscovererProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRegistry(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnRegistry",
):
    '''Use the ``AWS::EventSchemas::Registry`` to specify a schema registry.

    Schema registries are containers for Schemas. Registries collect and organize schemas so that your schemas are in logical groups.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventschemas as eventschemas
        
        cfn_registry = eventschemas.CfnRegistry(self, "MyCfnRegistry",
            description="description",
            registry_name="registryName",
            tags=[eventschemas.CfnRegistry.TagsEntryProperty(
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
        description: typing.Optional[builtins.str] = None,
        registry_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnRegistry.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the registry to be created.
        :param registry_name: The name of the schema registry.
        :param tags: Tags to associate with the registry.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afa8b8787bb752aaa6ea6c7d930a60af4b640432a5163a02767bd01c6998d811)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegistryProps(
            description=description, registry_name=registry_name, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f3a33248bf046934f50b3053f727578e1528e051189d185d58c716421f60590)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a7c11136544dd1e24d8b718272168cff2cded43a5d89859a4521b899c77fd6df)
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
    @jsii.member(jsii_name="attrRegistryArn")
    def attr_registry_arn(self) -> builtins.str:
        '''The ARN of the registry.

        :cloudformationAttribute: RegistryArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRegistryName")
    def attr_registry_name(self) -> builtins.str:
        '''The name of the registry.

        :cloudformationAttribute: RegistryName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegistryName"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the registry to be created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bce4f7f7e8c5a687a7fbdf9c4f2b0cd152aed97c129a84f29d1e92c997b8ce99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schema registry.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03b858e4024a2d1d4fa69d9add1f3648a6097e703c3b1d88c7273988233bd91b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["CfnRegistry.TagsEntryProperty"]]:
        '''Tags to associate with the registry.'''
        return typing.cast(typing.Optional[typing.List["CfnRegistry.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnRegistry.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4a5acf9b60d1d99c19efc9051601a320243d772d72bfe9c99d7bef8fe5e6703)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventschemas.CfnRegistry.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Tags to associate with the schema registry.

            :param key: They key of a key-value pair.
            :param value: They value of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventschemas as eventschemas
                
                tags_entry_property = eventschemas.CfnRegistry.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__434a165e1c5dfe37a102494f5df09787d58fee40ecc8ab422d5fca90ce8040d7)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''They key of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''They value of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-registry-tagsentry.html#cfn-eventschemas-registry-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnRegistryPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnRegistryPolicy",
):
    '''Use the ``AWS::EventSchemas::RegistryPolicy`` resource to specify resource-based policies for an EventBridge Schema Registry.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventschemas as eventschemas
        
        # policy: Any
        
        cfn_registry_policy = eventschemas.CfnRegistryPolicy(self, "MyCfnRegistryPolicy",
            policy=policy,
            registry_name="registryName",
        
            # the properties below are optional
            revision_id="revisionId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        policy: typing.Any,
        registry_name: builtins.str,
        revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param policy: A resource-based policy.
        :param registry_name: The name of the registry.
        :param revision_id: The revision ID of the policy.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad540eb68722cc10f4390e174c8e5220a2044dd1bc749c9d97dce9d05dc109b0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRegistryPolicyProps(
            policy=policy, registry_name=registry_name, revision_id=revision_id
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02a0b235686021baf044f24458acbcb50ff177d86100af36ba8109eb640f4ebc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4a4bec0d7bf3b7fc3674cf3e9fa5ea7ee730f6261b7292bc21c8d3a1e0921ab)
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
        '''The ID of the policy.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Any:
        '''A resource-based policy.'''
        return typing.cast(typing.Any, jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45e4a373a0302fe2e435472748d76b293c581b493372610b3c508f9ba14da520)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> builtins.str:
        '''The name of the registry.'''
        return typing.cast(builtins.str, jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4e5d3263c610305f4f20d2099d36fbf2bcc864fb0ea06c0e1a9a9bd79d60eba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryName", value)

    @builtins.property
    @jsii.member(jsii_name="revisionId")
    def revision_id(self) -> typing.Optional[builtins.str]:
        '''The revision ID of the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "revisionId"))

    @revision_id.setter
    def revision_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31f144d1732dcb92e464a7650dd5d31b9d139132ce00d366faf674bc51981ce2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "revisionId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnRegistryPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "policy": "policy",
        "registry_name": "registryName",
        "revision_id": "revisionId",
    },
)
class CfnRegistryPolicyProps:
    def __init__(
        self,
        *,
        policy: typing.Any,
        registry_name: builtins.str,
        revision_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnRegistryPolicy``.

        :param policy: A resource-based policy.
        :param registry_name: The name of the registry.
        :param revision_id: The revision ID of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventschemas as eventschemas
            
            # policy: Any
            
            cfn_registry_policy_props = eventschemas.CfnRegistryPolicyProps(
                policy=policy,
                registry_name="registryName",
            
                # the properties below are optional
                revision_id="revisionId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4135569dfec488bd5fc791f6abd204e6685e6f0164234565f9892897a9e86712)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
            check_type(argname="argument revision_id", value=revision_id, expected_type=type_hints["revision_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "policy": policy,
            "registry_name": registry_name,
        }
        if revision_id is not None:
            self._values["revision_id"] = revision_id

    @builtins.property
    def policy(self) -> typing.Any:
        '''A resource-based policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-policy
        '''
        result = self._values.get("policy")
        assert result is not None, "Required property 'policy' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def registry_name(self) -> builtins.str:
        '''The name of the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-registryname
        '''
        result = self._values.get("registry_name")
        assert result is not None, "Required property 'registry_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def revision_id(self) -> typing.Optional[builtins.str]:
        '''The revision ID of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registrypolicy.html#cfn-eventschemas-registrypolicy-revisionid
        '''
        result = self._values.get("revision_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnRegistryProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "registry_name": "registryName",
        "tags": "tags",
    },
)
class CfnRegistryProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        registry_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnRegistry.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRegistry``.

        :param description: A description of the registry to be created.
        :param registry_name: The name of the schema registry.
        :param tags: Tags to associate with the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventschemas as eventschemas
            
            cfn_registry_props = eventschemas.CfnRegistryProps(
                description="description",
                registry_name="registryName",
                tags=[eventschemas.CfnRegistry.TagsEntryProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98dc1608c2765effd97dc8e5664e8320916290dab365bc424710db12203fb1d2)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if registry_name is not None:
            self._values["registry_name"] = registry_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the registry to be created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def registry_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schema registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-registryname
        '''
        result = self._values.get("registry_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnRegistry.TagsEntryProperty]]:
        '''Tags to associate with the registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-registry.html#cfn-eventschemas-registry-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnRegistry.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRegistryProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSchema(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnSchema",
):
    '''Use the ``AWS::EventSchemas::Schema`` resource to specify an event schema.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_eventschemas as eventschemas
        
        cfn_schema = eventschemas.CfnSchema(self, "MyCfnSchema",
            content="content",
            registry_name="registryName",
            type="type",
        
            # the properties below are optional
            description="description",
            schema_name="schemaName",
            tags=[eventschemas.CfnSchema.TagsEntryProperty(
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
        content: builtins.str,
        registry_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union["CfnSchema.TagsEntryProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The source of the schema definition.
        :param registry_name: The name of the schema registry.
        :param type: The type of schema. Valid types include ``OpenApi3`` and ``JSONSchemaDraft4`` .
        :param description: A description of the schema.
        :param schema_name: The name of the schema.
        :param tags: Tags associated with the schema.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932c87e95b88ceabe68e304bed1c0517a1d9d901885f0e20ecd498449a6ceb5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSchemaProps(
            content=content,
            registry_name=registry_name,
            type=type,
            description=description,
            schema_name=schema_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11c3446e0c3190c26437e17664c824be87ad934d8243da4641672f66afadca7f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6f2224950a07cafb374f4a0e4dc54be3b520ba594f655ea88cfa238dc567dc00)
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
    @jsii.member(jsii_name="attrSchemaArn")
    def attr_schema_arn(self) -> builtins.str:
        '''The ARN of the schema.

        :cloudformationAttribute: SchemaArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSchemaName")
    def attr_schema_name(self) -> builtins.str:
        '''The name of the schema.

        :cloudformationAttribute: SchemaName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaName"))

    @builtins.property
    @jsii.member(jsii_name="attrSchemaVersion")
    def attr_schema_version(self) -> builtins.str:
        '''The version number of the schema.

        :cloudformationAttribute: SchemaVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSchemaVersion"))

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
    @jsii.member(jsii_name="content")
    def content(self) -> builtins.str:
        '''The source of the schema definition.'''
        return typing.cast(builtins.str, jsii.get(self, "content"))

    @content.setter
    def content(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e02d625cb742e61d0be744006f3c5bf11fbb499e14b421515752b5c3fa0756)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="registryName")
    def registry_name(self) -> builtins.str:
        '''The name of the schema registry.'''
        return typing.cast(builtins.str, jsii.get(self, "registryName"))

    @registry_name.setter
    def registry_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acc689ddbd2b2a99878cac557f72fa063db9c10fddb26006cde8c99dc8f47c4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "registryName", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of schema.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20994186b4e8a47c5f0da09570ff31daa342ccdb0faad6c3315fda6d333ac74e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the schema.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ac622a701dd4b78af42b037fd6d2d8a8f0df09268073b3b3e6ec9e89760deb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="schemaName")
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schema.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaName"))

    @schema_name.setter
    def schema_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0dc9f39d1407d9c42e73f09f44f4f3418c538613dd3f113ee845da29afc7450)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List["CfnSchema.TagsEntryProperty"]]:
        '''Tags associated with the schema.'''
        return typing.cast(typing.Optional[typing.List["CfnSchema.TagsEntryProperty"]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.List["CfnSchema.TagsEntryProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a12028f764e3ef6195835093bbd0f923b75cab1508a3629f92ff2d2ff121ba73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_eventschemas.CfnSchema.TagsEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TagsEntryProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Tags to associate with the schema.

            :param key: They key of a key-value pair.
            :param value: They value of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_eventschemas as eventschemas
                
                tags_entry_property = eventschemas.CfnSchema.TagsEntryProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3c0c8417e202ecdfe0d59ad69ea4376812f4a41c7f0620db5a4177794242134b)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''They key of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''They value of a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-eventschemas-schema-tagsentry.html#cfn-eventschemas-schema-tagsentry-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagsEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_eventschemas.CfnSchemaProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "registry_name": "registryName",
        "type": "type",
        "description": "description",
        "schema_name": "schemaName",
        "tags": "tags",
    },
)
class CfnSchemaProps:
    def __init__(
        self,
        *,
        content: builtins.str,
        registry_name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        schema_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[CfnSchema.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSchema``.

        :param content: The source of the schema definition.
        :param registry_name: The name of the schema registry.
        :param type: The type of schema. Valid types include ``OpenApi3`` and ``JSONSchemaDraft4`` .
        :param description: A description of the schema.
        :param schema_name: The name of the schema.
        :param tags: Tags associated with the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_eventschemas as eventschemas
            
            cfn_schema_props = eventschemas.CfnSchemaProps(
                content="content",
                registry_name="registryName",
                type="type",
            
                # the properties below are optional
                description="description",
                schema_name="schemaName",
                tags=[eventschemas.CfnSchema.TagsEntryProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb00ff21937e458a5e190860af6b381fcf6f0ab59d0849bcf094f0fc2c44c2c9)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument registry_name", value=registry_name, expected_type=type_hints["registry_name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument schema_name", value=schema_name, expected_type=type_hints["schema_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "registry_name": registry_name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if schema_name is not None:
            self._values["schema_name"] = schema_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> builtins.str:
        '''The source of the schema definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def registry_name(self) -> builtins.str:
        '''The name of the schema registry.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-registryname
        '''
        result = self._values.get("registry_name")
        assert result is not None, "Required property 'registry_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of schema.

        Valid types include ``OpenApi3`` and ``JSONSchemaDraft4`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_name(self) -> typing.Optional[builtins.str]:
        '''The name of the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-schemaname
        '''
        result = self._values.get("schema_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[CfnSchema.TagsEntryProperty]]:
        '''Tags associated with the schema.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-eventschemas-schema.html#cfn-eventschemas-schema-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[CfnSchema.TagsEntryProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSchemaProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDiscoverer",
    "CfnDiscovererProps",
    "CfnRegistry",
    "CfnRegistryPolicy",
    "CfnRegistryPolicyProps",
    "CfnRegistryProps",
    "CfnSchema",
    "CfnSchemaProps",
]

publication.publish()

def _typecheckingstub__c6de86d5a427a463ae500f08a01bbbbb1a7e5c02fcfcd3f1f306367587ea104b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    source_arn: builtins.str,
    cross_account: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDiscoverer.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5aed120cd74fca6fbf78a33d62495d891cbe2c2122e7ee9aac1ad880b563510c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e89fa30181b946d0bba0e9220d943a0e33377704225394b1f9d3d14fe912c54b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5676db42d7839b4e31ffff3ed613305ba8b0b32d7a6e2629d38eee2586e717fa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecb4a06e541deb6c8dda40cd09befd814af0290af78146808d35ff87851560c3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7463e2b4b05eced21b83e3338eb22af5c46afefaac9f880d439ba9a57d2eef9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca041b8aa73b6324baa5d76e21ca40251767aae80510f933254a18d21bdd512b(
    value: typing.Optional[typing.List[CfnDiscoverer.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8474d9c87ec86399a0d85d3b5386ddc8baf06ba1964693f15122f050ab2c3ea0(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__add35f90727b55854c3eefb472afcafa74b28a09aa410e1c3aa8a3128fa89a68(
    *,
    source_arn: builtins.str,
    cross_account: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnDiscoverer.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afa8b8787bb752aaa6ea6c7d930a60af4b640432a5163a02767bd01c6998d811(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    registry_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnRegistry.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f3a33248bf046934f50b3053f727578e1528e051189d185d58c716421f60590(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7c11136544dd1e24d8b718272168cff2cded43a5d89859a4521b899c77fd6df(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bce4f7f7e8c5a687a7fbdf9c4f2b0cd152aed97c129a84f29d1e92c997b8ce99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03b858e4024a2d1d4fa69d9add1f3648a6097e703c3b1d88c7273988233bd91b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4a5acf9b60d1d99c19efc9051601a320243d772d72bfe9c99d7bef8fe5e6703(
    value: typing.Optional[typing.List[CfnRegistry.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434a165e1c5dfe37a102494f5df09787d58fee40ecc8ab422d5fca90ce8040d7(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad540eb68722cc10f4390e174c8e5220a2044dd1bc749c9d97dce9d05dc109b0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    policy: typing.Any,
    registry_name: builtins.str,
    revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02a0b235686021baf044f24458acbcb50ff177d86100af36ba8109eb640f4ebc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4a4bec0d7bf3b7fc3674cf3e9fa5ea7ee730f6261b7292bc21c8d3a1e0921ab(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45e4a373a0302fe2e435472748d76b293c581b493372610b3c508f9ba14da520(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4e5d3263c610305f4f20d2099d36fbf2bcc864fb0ea06c0e1a9a9bd79d60eba(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31f144d1732dcb92e464a7650dd5d31b9d139132ce00d366faf674bc51981ce2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4135569dfec488bd5fc791f6abd204e6685e6f0164234565f9892897a9e86712(
    *,
    policy: typing.Any,
    registry_name: builtins.str,
    revision_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98dc1608c2765effd97dc8e5664e8320916290dab365bc424710db12203fb1d2(
    *,
    description: typing.Optional[builtins.str] = None,
    registry_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnRegistry.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932c87e95b88ceabe68e304bed1c0517a1d9d901885f0e20ecd498449a6ceb5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: builtins.str,
    registry_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnSchema.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11c3446e0c3190c26437e17664c824be87ad934d8243da4641672f66afadca7f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f2224950a07cafb374f4a0e4dc54be3b520ba594f655ea88cfa238dc567dc00(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e02d625cb742e61d0be744006f3c5bf11fbb499e14b421515752b5c3fa0756(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acc689ddbd2b2a99878cac557f72fa063db9c10fddb26006cde8c99dc8f47c4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20994186b4e8a47c5f0da09570ff31daa342ccdb0faad6c3315fda6d333ac74e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac622a701dd4b78af42b037fd6d2d8a8f0df09268073b3b3e6ec9e89760deb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0dc9f39d1407d9c42e73f09f44f4f3418c538613dd3f113ee845da29afc7450(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a12028f764e3ef6195835093bbd0f923b75cab1508a3629f92ff2d2ff121ba73(
    value: typing.Optional[typing.List[CfnSchema.TagsEntryProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c0c8417e202ecdfe0d59ad69ea4376812f4a41c7f0620db5a4177794242134b(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb00ff21937e458a5e190860af6b381fcf6f0ab59d0849bcf094f0fc2c44c2c9(
    *,
    content: builtins.str,
    registry_name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    schema_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnSchema.TagsEntryProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
