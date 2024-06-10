'''
# Amazon GameLift Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_gamelift as gamelift
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for GameLift construct libraries](https://constructs.dev/search?q=gamelift)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::GameLift resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLift.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-gamelift-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::GameLift](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_GameLift.html).

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
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnAlias",
):
    '''The ``AWS::GameLift::Alias`` resource creates an alias for an Amazon GameLift (GameLift) fleet destination.

    There are two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias displays a message instead of routing players to an active fleet. For example, a terminal alias might display a URL link that directs players to an upgrade site. You can use aliases to define destinations in a game session queue or when requesting new game sessions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
    :cloudformationResource: AWS::GameLift::Alias
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_alias = gamelift.CfnAlias(self, "MyCfnAlias",
            name="name",
            routing_strategy=gamelift.CfnAlias.RoutingStrategyProperty(
                type="type",
        
                # the properties below are optional
                fleet_id="fleetId",
                message="message"
            ),
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAlias.RoutingStrategyProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with an alias. Alias names do not need to be unique.
        :param routing_strategy: The routing configuration, including routing type and fleet target, for the alias.
        :param description: A human-readable description of the alias.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a91f3a4a7dfbcf1655ec6812682d7a8824bfb46a9ce2a65e3c859108e3633c8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAliasProps(
            name=name, routing_strategy=routing_strategy, description=description
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6c7223e714d0339897da2cbb4b67d9e03a5022aa12f568680b86e828460d501)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a1fbbe6ec42c9ed6d59226c8fe9df0391ca1a181a605b688f9e6267ea6f2a055)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAliasId")
    def attr_alias_id(self) -> builtins.str:
        '''A unique identifier for the alias. For example, ``arn:aws:gamelift:us-west-1::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912``.

        Alias IDs are unique within a Region.

        :cloudformationAttribute: AliasId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAliasId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with an alias.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8666b32153f5438f8d6ea2d03ad01cbf8c67bad1071d8e1cdc42963a8912ad3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="routingStrategy")
    def routing_strategy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAlias.RoutingStrategyProperty"]:
        '''The routing configuration, including routing type and fleet target, for the alias.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAlias.RoutingStrategyProperty"], jsii.get(self, "routingStrategy"))

    @routing_strategy.setter
    def routing_strategy(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAlias.RoutingStrategyProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__529d8fec4c06eafb4c38da47298670dd8132ede4d21975eafb43f51a366a3d82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d25b43c56fe6060dfb6e36792550c92a6a537d6d2e31b8c97947858787f55a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnAlias.RoutingStrategyProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "fleet_id": "fleetId", "message": "message"},
    )
    class RoutingStrategyProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            fleet_id: typing.Optional[builtins.str] = None,
            message: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The routing configuration for a fleet alias.

            :param type: A type of routing strategy. Possible routing types include the following: - *SIMPLE* - The alias resolves to one specific fleet. Use this type when routing to active fleets. - *TERMINAL* - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a ``TerminalRoutingStrategyException`` with the message that you specified in the ``Message`` property.
            :param fleet_id: A unique identifier for a fleet that the alias points to. If you specify ``SIMPLE`` for the ``Type`` property, you must specify this property.
            :param message: The message text to be used with a terminal routing strategy. If you specify ``TERMINAL`` for the ``Type`` property, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                routing_strategy_property = gamelift.CfnAlias.RoutingStrategyProperty(
                    type="type",
                
                    # the properties below are optional
                    fleet_id="fleetId",
                    message="message"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4057d890d9c2fba51db14d6885375c0c7263cd6b07fb4401e3fb51d7676734f9)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument fleet_id", value=fleet_id, expected_type=type_hints["fleet_id"])
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if fleet_id is not None:
                self._values["fleet_id"] = fleet_id
            if message is not None:
                self._values["message"] = message

        @builtins.property
        def type(self) -> builtins.str:
            '''A type of routing strategy.

            Possible routing types include the following:

            - *SIMPLE* - The alias resolves to one specific fleet. Use this type when routing to active fleets.
            - *TERMINAL* - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a ``TerminalRoutingStrategyException`` with the message that you specified in the ``Message`` property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fleet_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for a fleet that the alias points to.

            If you specify ``SIMPLE`` for the ``Type`` property, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-fleetid
            '''
            result = self._values.get("fleet_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message(self) -> typing.Optional[builtins.str]:
            '''The message text to be used with a terminal routing strategy.

            If you specify ``TERMINAL`` for the ``Type`` property, you must specify this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-alias-routingstrategy.html#cfn-gamelift-alias-routingstrategy-message
            '''
            result = self._values.get("message")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RoutingStrategyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnAliasProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "routing_strategy": "routingStrategy",
        "description": "description",
    },
)
class CfnAliasProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlias.RoutingStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlias``.

        :param name: A descriptive label that is associated with an alias. Alias names do not need to be unique.
        :param routing_strategy: The routing configuration, including routing type and fleet target, for the alias.
        :param description: A human-readable description of the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_alias_props = gamelift.CfnAliasProps(
                name="name",
                routing_strategy=gamelift.CfnAlias.RoutingStrategyProperty(
                    type="type",
            
                    # the properties below are optional
                    fleet_id="fleetId",
                    message="message"
                ),
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e74c18c4446e0f846baf63e2e707aa2ba663f37170623164846853f1176d7891)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument routing_strategy", value=routing_strategy, expected_type=type_hints["routing_strategy"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "routing_strategy": routing_strategy,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with an alias.

        Alias names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def routing_strategy(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAlias.RoutingStrategyProperty]:
        '''The routing configuration, including routing type and fleet target, for the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-routingstrategy
        '''
        result = self._values.get("routing_strategy")
        assert result is not None, "Required property 'routing_strategy' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAlias.RoutingStrategyProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A human-readable description of the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html#cfn-gamelift-alias-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnBuild(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnBuild",
):
    '''The ``AWS::GameLift::Build`` resource creates a game server build that is installed and run on instances in an Amazon GameLift fleet.

    This resource points to an Amazon S3 location that contains a zip file with all of the components of the game server build.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
    :cloudformationResource: AWS::GameLift::Build
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_build = gamelift.CfnBuild(self, "MyCfnBuild",
            name="name",
            operating_system="operatingSystem",
            server_sdk_version="serverSdkVersion",
            storage_location=gamelift.CfnBuild.StorageLocationProperty(
                bucket="bucket",
                key="key",
                role_arn="roleArn",
        
                # the properties below are optional
                object_version="objectVersion"
            ),
            version="version"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        server_sdk_version: typing.Optional[builtins.str] = None,
        storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBuild.StorageLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with a build. Build names do not need to be unique.
        :param operating_system: The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later. .. epigraph:: If you have active fleets using the Windows Server 2012 operating system, you can continue to create new builds using this OS until October 10, 2023, when Microsoft ends its support. All others must use Windows Server 2016 when creating new Windows-based builds.
        :param server_sdk_version: A server SDK version you used when integrating your game server build with Amazon GameLift. For more information see `Integrate games with custom game servers <https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html>`_ . By default Amazon GameLift sets this value to ``4.0.2`` .
        :param storage_location: Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region. If a ``StorageLocation`` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift will report a ``SizeOnDisk`` of 0.
        :param version: Version information that is associated with this build. Version strings do not need to be unique.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d2f3884df6574dd3d4e76d857acf05a15fdc616d818da1cebcfcce4084ca8ddc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBuildProps(
            name=name,
            operating_system=operating_system,
            server_sdk_version=server_sdk_version,
            storage_location=storage_location,
            version=version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dabd8e19951007a8e9f2bcb21f9e872c9fc5b6a638701939005bc4d813c12a3)
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
            type_hints = typing.get_type_hints(_typecheckingstub__52be0a2eff399965a7232bfe5d136a98b17426adc22dd0fe1be4ebd8de6c3b47)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBuildId")
    def attr_build_id(self) -> builtins.str:
        '''A unique identifier for the build.

        :cloudformationAttribute: BuildId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBuildId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a build.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a86d40dd79232f1b81dd44ba375e9a9432429c05c3444beaf1128ab336d19dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''The operating system that your game server binaries run on.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__086f4a5a0a253ca19c97937d0f25a8ade9bb623ef1c01cacdc76233a24f4ef0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="serverSdkVersion")
    def server_sdk_version(self) -> typing.Optional[builtins.str]:
        '''A server SDK version you used when integrating your game server build with Amazon GameLift.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverSdkVersion"))

    @server_sdk_version.setter
    def server_sdk_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb7f1e9548565a4821c004b0e86bae438a45b45de61043075555fb43127d349d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverSdkVersion", value)

    @builtins.property
    @jsii.member(jsii_name="storageLocation")
    def storage_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBuild.StorageLocationProperty"]]:
        '''Information indicating where your game build files are stored.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBuild.StorageLocationProperty"]], jsii.get(self, "storageLocation"))

    @storage_location.setter
    def storage_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBuild.StorageLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdd3e9ea10aa8547b05a398258efac5d3e786e68d7875c76104c89d2a3178e02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''Version information that is associated with this build.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f69e6e764a220fcdeac2ac30cce1d3fbf57e0ef02b497976b1bb0e8162a6a67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnBuild.StorageLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "role_arn": "roleArn",
            "object_version": "objectVersion",
        },
    )
    class StorageLocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location in Amazon S3 where build or script files are stored for access by Amazon GameLift.

            :param bucket: An Amazon S3 bucket identifier. The name of the S3 bucket. .. epigraph:: Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).
            :param key: The name of the zip file that contains the build files or script files.
            :param role_arn: The ARNfor an IAM role that allows Amazon GameLift to access the S3 bucket.
            :param object_version: A version of a stored file to retrieve, if the object versioning feature is turned on for the S3 bucket. Use this parameter to specify a specific version. If this parameter isn't set, Amazon GameLift retrieves the latest version of the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                storage_location_property = gamelift.CfnBuild.StorageLocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6d6726269ab0714348382710795aeac31efd3f1d29c3bac05a4aefa5c90bcba4)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "role_arn": role_arn,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''An Amazon S3 bucket identifier. The name of the S3 bucket.

            .. epigraph::

               Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the zip file that contains the build files or script files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The ARNfor an IAM role that allows Amazon GameLift to access the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''A version of a stored file to retrieve, if the object versioning feature is turned on for the S3 bucket.

            Use this parameter to specify a specific version. If this parameter isn't set, Amazon GameLift retrieves the latest version of the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-objectversion
            '''
            result = self._values.get("object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StorageLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnBuildProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "operating_system": "operatingSystem",
        "server_sdk_version": "serverSdkVersion",
        "storage_location": "storageLocation",
        "version": "version",
    },
)
class CfnBuildProps:
    def __init__(
        self,
        *,
        name: typing.Optional[builtins.str] = None,
        operating_system: typing.Optional[builtins.str] = None,
        server_sdk_version: typing.Optional[builtins.str] = None,
        storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBuild.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnBuild``.

        :param name: A descriptive label that is associated with a build. Build names do not need to be unique.
        :param operating_system: The operating system that your game server binaries run on. This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later. .. epigraph:: If you have active fleets using the Windows Server 2012 operating system, you can continue to create new builds using this OS until October 10, 2023, when Microsoft ends its support. All others must use Windows Server 2016 when creating new Windows-based builds.
        :param server_sdk_version: A server SDK version you used when integrating your game server build with Amazon GameLift. For more information see `Integrate games with custom game servers <https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html>`_ . By default Amazon GameLift sets this value to ``4.0.2`` .
        :param storage_location: Information indicating where your game build files are stored. Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region. If a ``StorageLocation`` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift will report a ``SizeOnDisk`` of 0.
        :param version: Version information that is associated with this build. Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_build_props = gamelift.CfnBuildProps(
                name="name",
                operating_system="operatingSystem",
                server_sdk_version="serverSdkVersion",
                storage_location=gamelift.CfnBuild.StorageLocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    object_version="objectVersion"
                ),
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ea486b468f726c96f63f78347aac31445ce3b0bd1ea282f6fce30ca4e8642d7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument server_sdk_version", value=server_sdk_version, expected_type=type_hints["server_sdk_version"])
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if name is not None:
            self._values["name"] = name
        if operating_system is not None:
            self._values["operating_system"] = operating_system
        if server_sdk_version is not None:
            self._values["server_sdk_version"] = server_sdk_version
        if storage_location is not None:
            self._values["storage_location"] = storage_location
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a build.

        Build names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operating_system(self) -> typing.Optional[builtins.str]:
        '''The operating system that your game server binaries run on.

        This value determines the type of fleet resources that you use for this build. If your game build contains multiple executables, they all must run on the same operating system. You must specify a valid operating system in this request. There is no default value. You can't change a build's operating system later.
        .. epigraph::

           If you have active fleets using the Windows Server 2012 operating system, you can continue to create new builds using this OS until October 10, 2023, when Microsoft ends its support. All others must use Windows Server 2016 when creating new Windows-based builds.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-operatingsystem
        '''
        result = self._values.get("operating_system")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_sdk_version(self) -> typing.Optional[builtins.str]:
        '''A server SDK version you used when integrating your game server build with Amazon GameLift.

        For more information see `Integrate games with custom game servers <https://docs.aws.amazon.com/gamelift/latest/developerguide/integration-custom-intro.html>`_ . By default Amazon GameLift sets this value to ``4.0.2`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-serversdkversion
        '''
        result = self._values.get("server_sdk_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def storage_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBuild.StorageLocationProperty]]:
        '''Information indicating where your game build files are stored.

        Use this parameter only when creating a build with files stored in an Amazon S3 bucket that you own. The storage location must specify an Amazon S3 bucket name and key. The location must also specify a role ARN that you set up to allow Amazon GameLift to access your Amazon S3 bucket. The S3 bucket and your new build must be in the same Region.

        If a ``StorageLocation`` is specified, the size of your file can be found in your Amazon S3 bucket. Amazon GameLift will report a ``SizeOnDisk`` of 0.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-storagelocation
        '''
        result = self._values.get("storage_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBuild.StorageLocationProperty]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''Version information that is associated with this build.

        Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-build.html#cfn-gamelift-build-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBuildProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnContainerGroupDefinition(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition",
):
    '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

    The properties that describe a container group resource. Container group definition properties can't be updated. To change a property, create a new container group definition.

    *Used with:* ``CreateContainerGroupDefinition``

    *Returned by:* ``DescribeContainerGroupDefinition`` , ``ListContainerGroupDefinitions``

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html
    :cloudformationResource: AWS::GameLift::ContainerGroupDefinition
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_container_group_definition = gamelift.CfnContainerGroupDefinition(self, "MyCfnContainerGroupDefinition",
            container_definitions=[gamelift.CfnContainerGroupDefinition.ContainerDefinitionProperty(
                container_name="containerName",
                image_uri="imageUri",
        
                # the properties below are optional
                command=["command"],
                cpu=123,
                depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                    condition="condition",
                    container_name="containerName"
                )],
                entry_point=["entryPoint"],
                environment=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                    name="name",
                    value="value"
                )],
                essential=False,
                health_check=gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                    command=["command"],
        
                    # the properties below are optional
                    interval=123,
                    retries=123,
                    start_period=123,
                    timeout=123
                ),
                memory_limits=gamelift.CfnContainerGroupDefinition.MemoryLimitsProperty(
                    hard_limit=123,
                    soft_limit=123
                ),
                port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                    container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                        from_port=123,
                        protocol="protocol",
                        to_port=123
                    )]
                ),
                resolved_image_digest="resolvedImageDigest",
                working_directory="workingDirectory"
            )],
            name="name",
            operating_system="operatingSystem",
            total_cpu_limit=123,
            total_memory_limit=123,
        
            # the properties below are optional
            scheduling_strategy="schedulingStrategy",
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
        container_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        operating_system: builtins.str,
        total_cpu_limit: jsii.Number,
        total_memory_limit: jsii.Number,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param container_definitions: The set of container definitions that are included in the container group.
        :param name: A descriptive identifier for the container group definition. The name value is unique in an AWS Region.
        :param operating_system: The platform required for all containers in the container group definition.
        :param total_cpu_limit: The amount of CPU units on a fleet instance to allocate for the container group. All containers in the group share these resources. This property is an integer value in CPU units (1 vCPU is equal to 1024 CPU units). You can set additional limits for each ``ContainerDefinition`` in the group. If individual containers have limits, this value must be equal to or greater than the sum of all container-specific CPU limits in the group. For more details on memory allocation, see the `Container fleet design guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-design-fleet>`_ .
        :param total_memory_limit: The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources. You can set additional limits for each ``ContainerDefinition`` in the group. If individual containers have limits, this value must meet the following requirements: - Equal to or greater than the sum of all container-specific soft memory limits in the group. - Equal to or greater than any container-specific hard limits in the group. For more details on memory allocation, see the `Container fleet design guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-design-fleet>`_ .
        :param scheduling_strategy: The method for deploying the container group across fleet instances. A replica container group might have multiple copies on each fleet instance. A daemon container group maintains only one copy per fleet instance.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d0ad3aeb1243549bc05c0346bb1e8303d21326ec9f1a17ec63327d7e3f29a1e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContainerGroupDefinitionProps(
            container_definitions=container_definitions,
            name=name,
            operating_system=operating_system,
            total_cpu_limit=total_cpu_limit,
            total_memory_limit=total_memory_limit,
            scheduling_strategy=scheduling_strategy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b07a706beb428681d6a41fe2a705cfe7e9f6f65c0df4708d633a856c73d6fa7b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__abcc96ad0c8f9f987fd719eb37179f12dda8829dbbc0b9fb28188a52044ec711)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContainerGroupDefinitionArn")
    def attr_container_group_definition_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to an Amazon GameLift ``ContainerGroupDefinition`` resource. It uniquely identifies the resource across all AWS Regions. Format is ``arn:aws:gamelift:<region>::containergroupdefinition/[container group definition name]`` .

        :cloudformationAttribute: ContainerGroupDefinitionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrContainerGroupDefinitionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

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
    @jsii.member(jsii_name="containerDefinitions")
    def container_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDefinitionProperty"]]]:
        '''The set of container definitions that are included in the container group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDefinitionProperty"]]], jsii.get(self, "containerDefinitions"))

    @container_definitions.setter
    def container_definitions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDefinitionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d575dc521c3da1f3682c88ce08e24b38977a41bef8807469e908a4fc94b8be0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerDefinitions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive identifier for the container group definition.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90e8a024d1021ae9b57dadc57167a55f375efa5756fd3358541d1bbca8f16cf0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="operatingSystem")
    def operating_system(self) -> builtins.str:
        '''The platform required for all containers in the container group definition.'''
        return typing.cast(builtins.str, jsii.get(self, "operatingSystem"))

    @operating_system.setter
    def operating_system(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f85c42319aa42e6c796369d8760bfb73c97a6305632fa1b86497b93a214a2ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operatingSystem", value)

    @builtins.property
    @jsii.member(jsii_name="totalCpuLimit")
    def total_cpu_limit(self) -> jsii.Number:
        '''The amount of CPU units on a fleet instance to allocate for the container group.'''
        return typing.cast(jsii.Number, jsii.get(self, "totalCpuLimit"))

    @total_cpu_limit.setter
    def total_cpu_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c70806f2091ef0e31ae18f95ca9388e13070bc234c9db0acb79308e3bb8064c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalCpuLimit", value)

    @builtins.property
    @jsii.member(jsii_name="totalMemoryLimit")
    def total_memory_limit(self) -> jsii.Number:
        '''The amount of memory (in MiB) on a fleet instance to allocate for the container group.'''
        return typing.cast(jsii.Number, jsii.get(self, "totalMemoryLimit"))

    @total_memory_limit.setter
    def total_memory_limit(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4cc7de67e0ef4b7a915c9522aa5d27817d4c88d3cc0d6cc3897ec44fe82624e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "totalMemoryLimit", value)

    @builtins.property
    @jsii.member(jsii_name="schedulingStrategy")
    def scheduling_strategy(self) -> typing.Optional[builtins.str]:
        '''The method for deploying the container group across fleet instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schedulingStrategy"))

    @scheduling_strategy.setter
    def scheduling_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4192c1232484aa6cb4b7a0ff2133a07c228af7fc593005174668d67f88e787)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedulingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39d9905e11429554186c96e0a5c07109b132519014161fc8e8d7aa9f4250218d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "container_name": "containerName",
            "image_uri": "imageUri",
            "command": "command",
            "cpu": "cpu",
            "depends_on": "dependsOn",
            "entry_point": "entryPoint",
            "environment": "environment",
            "essential": "essential",
            "health_check": "healthCheck",
            "memory_limits": "memoryLimits",
            "port_configuration": "portConfiguration",
            "resolved_image_digest": "resolvedImageDigest",
            "working_directory": "workingDirectory",
        },
    )
    class ContainerDefinitionProperty:
        def __init__(
            self,
            *,
            container_name: builtins.str,
            image_uri: builtins.str,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            cpu: typing.Optional[jsii.Number] = None,
            depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerDependencyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
            environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerEnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            essential: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            health_check: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerHealthCheckProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            memory_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.MemoryLimitsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            port_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.PortConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resolved_image_digest: typing.Optional[builtins.str] = None,
            working_directory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

            Describes a container in a container fleet, the resources available to the container, and the commands that are run when the container starts. Container properties can't be updated. To change a property, create a new container group definition. See also ``ContainerDefinitionInput`` .

            *Part of:* ``ContainerGroupDefinition``

            *Returned by:* ``DescribeContainerGroupDefinition`` , ``ListContainerGroupDefinitions``

            :param container_name: The container definition identifier. Container names are unique within a container group definition.
            :param image_uri: The URI to the image that $short; copied and deployed to a container fleet. For a more specific identifier, see ``ResolvedImageDigest`` .
            :param command: A command that's passed to the container on startup. Each argument for the command is an additional string in the array. See the `ContainerDefinition::command <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-command>`_ parameter in the *Amazon Elastic Container Service API reference.*
            :param cpu: The number of CPU units that are reserved for the container. Note: 1 vCPU unit equals 1024 CPU units. If no resources are reserved, the container shares the total CPU limit for the container group. *Related data type:* ``ContainerGroupDefinition$TotalCpuLimit``
            :param depends_on: Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences. A container might have dependencies on multiple containers.
            :param entry_point: The entry point that's passed to the container on startup. If there are multiple arguments, each argument is an additional string in the array. See the `ContainerDefinition::entryPoint <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-entryPoint>`_ parameter in the *Amazon Elastic Container Service API Reference* .
            :param environment: A set of environment variables that's passed to the container on startup. See the `ContainerDefinition::environment <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment>`_ parameter in the *Amazon Elastic Container Service API Reference* .
            :param essential: Indicates whether the container is vital to the container group. If an essential container fails, the entire container group is restarted.
            :param health_check: A configuration for a non-terminal health check. A container, which automatically restarts if it stops functioning, also restarts if it fails this health check. If an essential container in the daemon group fails a health check, the entire container group is restarted. The essential container in the replica group doesn't use this health check mechanism, because the Amazon GameLift Agent automatically handles the task.
            :param memory_limits: The amount of memory that Amazon GameLift makes available to the container. If memory limits aren't set for an individual container, the container shares the container group's total memory allocation. *Related data type:* ``ContainerGroupDefinition$TotalMemoryLimit``
            :param port_configuration: Defines the ports that are available to assign to processes in the container. For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's ``ConnectionPortRange`` .
            :param resolved_image_digest: A unique and immutable identifier for the container image that is deployed to a container fleet. The digest is a SHA 256 hash of the container image manifest.
            :param working_directory: The directory in the container where commands are run. See the `ContainerDefinition::workingDirectory <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-workingDirectory>`_ parameter in the *Amazon Elastic Container Service API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_definition_property = gamelift.CfnContainerGroupDefinition.ContainerDefinitionProperty(
                    container_name="containerName",
                    image_uri="imageUri",
                
                    # the properties below are optional
                    command=["command"],
                    cpu=123,
                    depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                        condition="condition",
                        container_name="containerName"
                    )],
                    entry_point=["entryPoint"],
                    environment=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    essential=False,
                    health_check=gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                        command=["command"],
                
                        # the properties below are optional
                        interval=123,
                        retries=123,
                        start_period=123,
                        timeout=123
                    ),
                    memory_limits=gamelift.CfnContainerGroupDefinition.MemoryLimitsProperty(
                        hard_limit=123,
                        soft_limit=123
                    ),
                    port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                        container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                            from_port=123,
                            protocol="protocol",
                            to_port=123
                        )]
                    ),
                    resolved_image_digest="resolvedImageDigest",
                    working_directory="workingDirectory"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d96474fb31ceec64a55f6a09274f19f2dde05387b5bdd5c76ce6f26d90d5eb7)
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
                check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument cpu", value=cpu, expected_type=type_hints["cpu"])
                check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
                check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
                check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
                check_type(argname="argument essential", value=essential, expected_type=type_hints["essential"])
                check_type(argname="argument health_check", value=health_check, expected_type=type_hints["health_check"])
                check_type(argname="argument memory_limits", value=memory_limits, expected_type=type_hints["memory_limits"])
                check_type(argname="argument port_configuration", value=port_configuration, expected_type=type_hints["port_configuration"])
                check_type(argname="argument resolved_image_digest", value=resolved_image_digest, expected_type=type_hints["resolved_image_digest"])
                check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_name": container_name,
                "image_uri": image_uri,
            }
            if command is not None:
                self._values["command"] = command
            if cpu is not None:
                self._values["cpu"] = cpu
            if depends_on is not None:
                self._values["depends_on"] = depends_on
            if entry_point is not None:
                self._values["entry_point"] = entry_point
            if environment is not None:
                self._values["environment"] = environment
            if essential is not None:
                self._values["essential"] = essential
            if health_check is not None:
                self._values["health_check"] = health_check
            if memory_limits is not None:
                self._values["memory_limits"] = memory_limits
            if port_configuration is not None:
                self._values["port_configuration"] = port_configuration
            if resolved_image_digest is not None:
                self._values["resolved_image_digest"] = resolved_image_digest
            if working_directory is not None:
                self._values["working_directory"] = working_directory

        @builtins.property
        def container_name(self) -> builtins.str:
            '''The container definition identifier.

            Container names are unique within a container group definition.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-containername
            '''
            result = self._values.get("container_name")
            assert result is not None, "Required property 'container_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def image_uri(self) -> builtins.str:
            '''The URI to the image that $short;

            copied and deployed to a container fleet. For a more specific identifier, see ``ResolvedImageDigest`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-imageuri
            '''
            result = self._values.get("image_uri")
            assert result is not None, "Required property 'image_uri' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A command that's passed to the container on startup.

            Each argument for the command is an additional string in the array. See the `ContainerDefinition::command <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-command>`_ parameter in the *Amazon Elastic Container Service API reference.*

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def cpu(self) -> typing.Optional[jsii.Number]:
            '''The number of CPU units that are reserved for the container.

            Note: 1 vCPU unit equals 1024 CPU units. If no resources are reserved, the container shares the total CPU limit for the container group.

            *Related data type:* ``ContainerGroupDefinition$TotalCpuLimit``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-cpu
            '''
            result = self._values.get("cpu")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def depends_on(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDependencyProperty"]]]]:
            '''Indicates that the container relies on the status of other containers in the same container group during its startup and shutdown sequences.

            A container might have dependencies on multiple containers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-dependson
            '''
            result = self._values.get("depends_on")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerDependencyProperty"]]]], result)

        @builtins.property
        def entry_point(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The entry point that's passed to the container on startup.

            If there are multiple arguments, each argument is an additional string in the array. See the `ContainerDefinition::entryPoint <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-entryPoint>`_ parameter in the *Amazon Elastic Container Service API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-entrypoint
            '''
            result = self._values.get("entry_point")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def environment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerEnvironmentProperty"]]]]:
            '''A set of environment variables that's passed to the container on startup.

            See the `ContainerDefinition::environment <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-environment>`_ parameter in the *Amazon Elastic Container Service API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-environment
            '''
            result = self._values.get("environment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerEnvironmentProperty"]]]], result)

        @builtins.property
        def essential(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the container is vital to the container group.

            If an essential container fails, the entire container group is restarted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-essential
            '''
            result = self._values.get("essential")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def health_check(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerHealthCheckProperty"]]:
            '''A configuration for a non-terminal health check.

            A container, which automatically restarts if it stops functioning, also restarts if it fails this health check. If an essential container in the daemon group fails a health check, the entire container group is restarted. The essential container in the replica group doesn't use this health check mechanism, because the Amazon GameLift Agent automatically handles the task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-healthcheck
            '''
            result = self._values.get("health_check")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerHealthCheckProperty"]], result)

        @builtins.property
        def memory_limits(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.MemoryLimitsProperty"]]:
            '''The amount of memory that Amazon GameLift makes available to the container.

            If memory limits aren't set for an individual container, the container shares the container group's total memory allocation.

            *Related data type:* ``ContainerGroupDefinition$TotalMemoryLimit``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-memorylimits
            '''
            result = self._values.get("memory_limits")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.MemoryLimitsProperty"]], result)

        @builtins.property
        def port_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.PortConfigurationProperty"]]:
            '''Defines the ports that are available to assign to processes in the container.

            For example, a game server process requires a container port to allow game clients to connect to it. Container ports aren't directly accessed by inbound traffic. Amazon GameLift maps these container ports to externally accessible connection ports, which are assigned as needed from the container fleet's ``ConnectionPortRange`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-portconfiguration
            '''
            result = self._values.get("port_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.PortConfigurationProperty"]], result)

        @builtins.property
        def resolved_image_digest(self) -> typing.Optional[builtins.str]:
            '''A unique and immutable identifier for the container image that is deployed to a container fleet.

            The digest is a SHA 256 hash of the container image manifest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-resolvedimagedigest
            '''
            result = self._values.get("resolved_image_digest")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def working_directory(self) -> typing.Optional[builtins.str]:
            '''The directory in the container where commands are run.

            See the `ContainerDefinition::workingDirectory <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_ContainerDefinition.html#ECS-Type-ContainerDefinition-workingDirectory>`_ parameter in the *Amazon Elastic Container Service API Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinition-workingdirectory
            '''
            result = self._values.get("working_directory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty",
        jsii_struct_bases=[],
        name_mapping={"condition": "condition", "container_name": "containerName"},
    )
    class ContainerDependencyProperty:
        def __init__(
            self,
            *,
            condition: builtins.str,
            container_name: builtins.str,
        ) -> None:
            '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

            A container's dependency on another container in the same container group. The dependency impacts how the dependent container is able to start or shut down based the status of the other container.

            For example, ContainerA is configured with the following dependency: a ``START`` dependency on ContainerB. This means that ContainerA can't start until ContainerB has started. It also means that ContainerA must shut down before ContainerB.

            *Part of:* ``ContainerDefinition``

            :param condition: The condition that the dependency container must reach before the dependent container can start. Valid conditions include:. - START - The dependency container must have started. - COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container. - SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container. - HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.
            :param container_name: A descriptive label for the container definition that this container depends on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdependency.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_dependency_property = gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                    condition="condition",
                    container_name="containerName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8424bed9ce9567d13ec372652e5d607735583e13219bd42143f538aee3feb1f)
                check_type(argname="argument condition", value=condition, expected_type=type_hints["condition"])
                check_type(argname="argument container_name", value=container_name, expected_type=type_hints["container_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "condition": condition,
                "container_name": container_name,
            }

        @builtins.property
        def condition(self) -> builtins.str:
            '''The condition that the dependency container must reach before the dependent container can start. Valid conditions include:.

            - START - The dependency container must have started.
            - COMPLETE - The dependency container has run to completion (exits). Use this condition with nonessential containers, such as those that run a script and then exit. The dependency container can't be an essential container.
            - SUCCESS - The dependency container has run to completion and exited with a zero status. The dependency container can't be an essential container.
            - HEALTHY - The dependency container has passed its Docker health check. Use this condition with dependency containers that have health checks configured. This condition is confirmed at container group startup only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdependency.html#cfn-gamelift-containergroupdefinition-containerdependency-condition
            '''
            result = self._values.get("condition")
            assert result is not None, "Required property 'condition' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def container_name(self) -> builtins.str:
            '''A descriptive label for the container definition that this container depends on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerdependency.html#cfn-gamelift-containergroupdefinition-containerdependency-containername
            '''
            result = self._values.get("container_name")
            assert result is not None, "Required property 'container_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerDependencyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class ContainerEnvironmentProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

            An environment variable to set inside a container, in the form of a key-value pair.

            *Related data type:* ``ContainerDefinition$Environment``

            :param name: The environment variable name.
            :param value: The environment variable value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerenvironment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_environment_property = gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8a971f77ef4383909669846d3e4ee4a8463f7353ec0c1aa4da152ea7ec43bb9)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The environment variable name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerenvironment.html#cfn-gamelift-containergroupdefinition-containerenvironment-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The environment variable value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerenvironment.html#cfn-gamelift-containergroupdefinition-containerenvironment-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerEnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "interval": "interval",
            "retries": "retries",
            "start_period": "startPeriod",
            "timeout": "timeout",
        },
    )
    class ContainerHealthCheckProperty:
        def __init__(
            self,
            *,
            command: typing.Sequence[builtins.str],
            interval: typing.Optional[jsii.Number] = None,
            retries: typing.Optional[jsii.Number] = None,
            start_period: typing.Optional[jsii.Number] = None,
            timeout: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Instructions on when and how to check the health of a container in a container fleet.

            When health check properties are set in a container definition, they override any Docker health checks in the container image. For more information on container health checks, see `HealthCheck command <https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_HealthCheck.html#ECS-Type-HealthCheck-command>`_ in the *Amazon Elastic Container Service API* .

            The following example instructions tell the container to wait 100 seconds after launch before counting failed health checks, then initiate the health check command every 60 seconds. After issuing the health check command, wait 10 seconds for it to succeed. If it fails, retry the command 3 times before considering the container to be unhealthy.

            ``{"Command": [ "CMD-SHELL", "ps cax | grep "processmanager" || exit 1" ], "Interval": 300, "Timeout": 30, "Retries": 5, "StartPeriod": 100 }``

            *Part of:* ``ContainerDefinition$HealthCheck``

            :param command: A string array that specifies the command that the container runs to determine if it's healthy.
            :param interval: The time period (in seconds) between each health check.
            :param retries: The number of times to retry a failed health check before the container is considered unhealthy. The first run of the command does not count as a retry.
            :param start_period: The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.
            :param timeout: The time period (in seconds) to wait for a health check to succeed before a failed health check is counted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_health_check_property = gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                    command=["command"],
                
                    # the properties below are optional
                    interval=123,
                    retries=123,
                    start_period=123,
                    timeout=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__95b1e7083ac6b3d39e0bc5926b3c9ee368385be498c61499a81f860b155d0a1d)
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
                check_type(argname="argument retries", value=retries, expected_type=type_hints["retries"])
                check_type(argname="argument start_period", value=start_period, expected_type=type_hints["start_period"])
                check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "command": command,
            }
            if interval is not None:
                self._values["interval"] = interval
            if retries is not None:
                self._values["retries"] = retries
            if start_period is not None:
                self._values["start_period"] = start_period
            if timeout is not None:
                self._values["timeout"] = timeout

        @builtins.property
        def command(self) -> typing.List[builtins.str]:
            '''A string array that specifies the command that the container runs to determine if it's healthy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-command
            '''
            result = self._values.get("command")
            assert result is not None, "Required property 'command' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def interval(self) -> typing.Optional[jsii.Number]:
            '''The time period (in seconds) between each health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-interval
            '''
            result = self._values.get("interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def retries(self) -> typing.Optional[jsii.Number]:
            '''The number of times to retry a failed health check before the container is considered unhealthy.

            The first run of the command does not count as a retry.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-retries
            '''
            result = self._values.get("retries")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_period(self) -> typing.Optional[jsii.Number]:
            '''The optional grace period (in seconds) to give a container time to bootstrap before the first failed health check counts toward the number of retries.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-startperiod
            '''
            result = self._values.get("start_period")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def timeout(self) -> typing.Optional[jsii.Number]:
            '''The time period (in seconds) to wait for a health check to succeed before a failed health check is counted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerhealthcheck.html#cfn-gamelift-containergroupdefinition-containerhealthcheck-timeout
            '''
            result = self._values.get("timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerHealthCheckProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "from_port": "fromPort",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class ContainerPortRangeProperty:
        def __init__(
            self,
            *,
            from_port: jsii.Number,
            protocol: builtins.str,
            to_port: jsii.Number,
        ) -> None:
            '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

            A set of one or more port numbers that can be opened on the container.

            *Part of:* ``ContainerPortConfiguration``

            :param from_port: A starting value for the range of allowed port numbers.
            :param protocol: The network protocol that these ports support.
            :param to_port: An ending value for the range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_port_range_property = gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                    from_port=123,
                    protocol="protocol",
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2d3e35cf8a42e8cbcdf12218e64e5ac29c19f0813f144c8d75e97d3e3313d396)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "protocol": protocol,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''A starting value for the range of allowed port numbers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html#cfn-gamelift-containergroupdefinition-containerportrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network protocol that these ports support.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html#cfn-gamelift-containergroupdefinition-containerportrange-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''An ending value for the range of allowed port numbers.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-containerportrange.html#cfn-gamelift-containergroupdefinition-containerportrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerPortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.MemoryLimitsProperty",
        jsii_struct_bases=[],
        name_mapping={"hard_limit": "hardLimit", "soft_limit": "softLimit"},
    )
    class MemoryLimitsProperty:
        def __init__(
            self,
            *,
            hard_limit: typing.Optional[jsii.Number] = None,
            soft_limit: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Specifies how much memory is available to the container.

            :param hard_limit: The hard limit of memory to reserve for the container.
            :param soft_limit: The amount of memory that is reserved for the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-memorylimits.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                memory_limits_property = gamelift.CfnContainerGroupDefinition.MemoryLimitsProperty(
                    hard_limit=123,
                    soft_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9ac03f75ba7cf3ff7267cf9e9544e940c9974e78a4d364eed01d2ebb6bc2d3fa)
                check_type(argname="argument hard_limit", value=hard_limit, expected_type=type_hints["hard_limit"])
                check_type(argname="argument soft_limit", value=soft_limit, expected_type=type_hints["soft_limit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if hard_limit is not None:
                self._values["hard_limit"] = hard_limit
            if soft_limit is not None:
                self._values["soft_limit"] = soft_limit

        @builtins.property
        def hard_limit(self) -> typing.Optional[jsii.Number]:
            '''The hard limit of memory to reserve for the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-memorylimits.html#cfn-gamelift-containergroupdefinition-memorylimits-hardlimit
            '''
            result = self._values.get("hard_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def soft_limit(self) -> typing.Optional[jsii.Number]:
            '''The amount of memory that is reserved for the container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-memorylimits.html#cfn-gamelift-containergroupdefinition-memorylimits-softlimit
            '''
            result = self._values.get("soft_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MemoryLimitsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinition.PortConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"container_port_ranges": "containerPortRanges"},
    )
    class PortConfigurationProperty:
        def __init__(
            self,
            *,
            container_port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContainerGroupDefinition.ContainerPortRangeProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''Defines the ports on a container.

            :param container_port_ranges: Specifies one or more ranges of ports on a container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-portconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                port_configuration_property = gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                    container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                        from_port=123,
                        protocol="protocol",
                        to_port=123
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__49796d7f2a6fb9a60e370fb5b8e88da33d84ca298d8833d8e64e3d80586cedf7)
                check_type(argname="argument container_port_ranges", value=container_port_ranges, expected_type=type_hints["container_port_ranges"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "container_port_ranges": container_port_ranges,
            }

        @builtins.property
        def container_port_ranges(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerPortRangeProperty"]]]:
            '''Specifies one or more ranges of ports on a container.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-containergroupdefinition-portconfiguration.html#cfn-gamelift-containergroupdefinition-portconfiguration-containerportranges
            '''
            result = self._values.get("container_port_ranges")
            assert result is not None, "Required property 'container_port_ranges' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContainerGroupDefinition.ContainerPortRangeProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnContainerGroupDefinitionProps",
    jsii_struct_bases=[],
    name_mapping={
        "container_definitions": "containerDefinitions",
        "name": "name",
        "operating_system": "operatingSystem",
        "total_cpu_limit": "totalCpuLimit",
        "total_memory_limit": "totalMemoryLimit",
        "scheduling_strategy": "schedulingStrategy",
        "tags": "tags",
    },
)
class CfnContainerGroupDefinitionProps:
    def __init__(
        self,
        *,
        container_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        name: builtins.str,
        operating_system: builtins.str,
        total_cpu_limit: jsii.Number,
        total_memory_limit: jsii.Number,
        scheduling_strategy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContainerGroupDefinition``.

        :param container_definitions: The set of container definitions that are included in the container group.
        :param name: A descriptive identifier for the container group definition. The name value is unique in an AWS Region.
        :param operating_system: The platform required for all containers in the container group definition.
        :param total_cpu_limit: The amount of CPU units on a fleet instance to allocate for the container group. All containers in the group share these resources. This property is an integer value in CPU units (1 vCPU is equal to 1024 CPU units). You can set additional limits for each ``ContainerDefinition`` in the group. If individual containers have limits, this value must be equal to or greater than the sum of all container-specific CPU limits in the group. For more details on memory allocation, see the `Container fleet design guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-design-fleet>`_ .
        :param total_memory_limit: The amount of memory (in MiB) on a fleet instance to allocate for the container group. All containers in the group share these resources. You can set additional limits for each ``ContainerDefinition`` in the group. If individual containers have limits, this value must meet the following requirements: - Equal to or greater than the sum of all container-specific soft memory limits in the group. - Equal to or greater than any container-specific hard limits in the group. For more details on memory allocation, see the `Container fleet design guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-design-fleet>`_ .
        :param scheduling_strategy: The method for deploying the container group across fleet instances. A replica container group might have multiple copies on each fleet instance. A daemon container group maintains only one copy per fleet instance.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_container_group_definition_props = gamelift.CfnContainerGroupDefinitionProps(
                container_definitions=[gamelift.CfnContainerGroupDefinition.ContainerDefinitionProperty(
                    container_name="containerName",
                    image_uri="imageUri",
            
                    # the properties below are optional
                    command=["command"],
                    cpu=123,
                    depends_on=[gamelift.CfnContainerGroupDefinition.ContainerDependencyProperty(
                        condition="condition",
                        container_name="containerName"
                    )],
                    entry_point=["entryPoint"],
                    environment=[gamelift.CfnContainerGroupDefinition.ContainerEnvironmentProperty(
                        name="name",
                        value="value"
                    )],
                    essential=False,
                    health_check=gamelift.CfnContainerGroupDefinition.ContainerHealthCheckProperty(
                        command=["command"],
            
                        # the properties below are optional
                        interval=123,
                        retries=123,
                        start_period=123,
                        timeout=123
                    ),
                    memory_limits=gamelift.CfnContainerGroupDefinition.MemoryLimitsProperty(
                        hard_limit=123,
                        soft_limit=123
                    ),
                    port_configuration=gamelift.CfnContainerGroupDefinition.PortConfigurationProperty(
                        container_port_ranges=[gamelift.CfnContainerGroupDefinition.ContainerPortRangeProperty(
                            from_port=123,
                            protocol="protocol",
                            to_port=123
                        )]
                    ),
                    resolved_image_digest="resolvedImageDigest",
                    working_directory="workingDirectory"
                )],
                name="name",
                operating_system="operatingSystem",
                total_cpu_limit=123,
                total_memory_limit=123,
            
                # the properties below are optional
                scheduling_strategy="schedulingStrategy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b760a12182b9da0a53204aa5510dae28c2cda4c4fba1ef77f0245093da04ea4)
            check_type(argname="argument container_definitions", value=container_definitions, expected_type=type_hints["container_definitions"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument operating_system", value=operating_system, expected_type=type_hints["operating_system"])
            check_type(argname="argument total_cpu_limit", value=total_cpu_limit, expected_type=type_hints["total_cpu_limit"])
            check_type(argname="argument total_memory_limit", value=total_memory_limit, expected_type=type_hints["total_memory_limit"])
            check_type(argname="argument scheduling_strategy", value=scheduling_strategy, expected_type=type_hints["scheduling_strategy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "container_definitions": container_definitions,
            "name": name,
            "operating_system": operating_system,
            "total_cpu_limit": total_cpu_limit,
            "total_memory_limit": total_memory_limit,
        }
        if scheduling_strategy is not None:
            self._values["scheduling_strategy"] = scheduling_strategy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def container_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.ContainerDefinitionProperty]]]:
        '''The set of container definitions that are included in the container group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-containerdefinitions
        '''
        result = self._values.get("container_definitions")
        assert result is not None, "Required property 'container_definitions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.ContainerDefinitionProperty]]], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive identifier for the container group definition.

        The name value is unique in an AWS Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def operating_system(self) -> builtins.str:
        '''The platform required for all containers in the container group definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-operatingsystem
        '''
        result = self._values.get("operating_system")
        assert result is not None, "Required property 'operating_system' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def total_cpu_limit(self) -> jsii.Number:
        '''The amount of CPU units on a fleet instance to allocate for the container group.

        All containers in the group share these resources. This property is an integer value in CPU units (1 vCPU is equal to 1024 CPU units).

        You can set additional limits for each ``ContainerDefinition`` in the group. If individual containers have limits, this value must be equal to or greater than the sum of all container-specific CPU limits in the group.

        For more details on memory allocation, see the `Container fleet design guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-design-fleet>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-totalcpulimit
        '''
        result = self._values.get("total_cpu_limit")
        assert result is not None, "Required property 'total_cpu_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def total_memory_limit(self) -> jsii.Number:
        '''The amount of memory (in MiB) on a fleet instance to allocate for the container group.

        All containers in the group share these resources.

        You can set additional limits for each ``ContainerDefinition`` in the group. If individual containers have limits, this value must meet the following requirements:

        - Equal to or greater than the sum of all container-specific soft memory limits in the group.
        - Equal to or greater than any container-specific hard limits in the group.

        For more details on memory allocation, see the `Container fleet design guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/containers-design-fleet>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-totalmemorylimit
        '''
        result = self._values.get("total_memory_limit")
        assert result is not None, "Required property 'total_memory_limit' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def scheduling_strategy(self) -> typing.Optional[builtins.str]:
        '''The method for deploying the container group across fleet instances.

        A replica container group might have multiple copies on each fleet instance. A daemon container group maintains only one copy per fleet instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-schedulingstrategy
        '''
        result = self._values.get("scheduling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-containergroupdefinition.html#cfn-gamelift-containergroupdefinition-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContainerGroupDefinitionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet",
):
    '''The ``AWS::GameLift::Fleet`` resource creates an Amazon GameLift (GameLift) fleet to host custom game server or Realtime Servers.

    A fleet is a set of EC2 instances, configured with instructions to run game servers on each instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
    :cloudformationResource: AWS::GameLift::Fleet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_fleet = gamelift.CfnFleet(self, "MyCfnFleet",
            name="name",
        
            # the properties below are optional
            anywhere_configuration=gamelift.CfnFleet.AnywhereConfigurationProperty(
                cost="cost"
            ),
            apply_capacity="applyCapacity",
            build_id="buildId",
            certificate_configuration=gamelift.CfnFleet.CertificateConfigurationProperty(
                certificate_type="certificateType"
            ),
            compute_type="computeType",
            container_groups_configuration=gamelift.CfnFleet.ContainerGroupsConfigurationProperty(
                connection_port_range=gamelift.CfnFleet.ConnectionPortRangeProperty(
                    from_port=123,
                    to_port=123
                ),
                container_group_definition_names=["containerGroupDefinitionNames"],
        
                # the properties below are optional
                container_groups_per_instance=gamelift.CfnFleet.ContainerGroupsPerInstanceProperty(
                    desired_replica_container_groups_per_instance=123,
                    max_replica_container_groups_per_instance=123
                )
            ),
            description="description",
            desired_ec2_instances=123,
            ec2_inbound_permissions=[gamelift.CfnFleet.IpPermissionProperty(
                from_port=123,
                ip_range="ipRange",
                protocol="protocol",
                to_port=123
            )],
            ec2_instance_type="ec2InstanceType",
            fleet_type="fleetType",
            instance_role_arn="instanceRoleArn",
            instance_role_credentials_provider="instanceRoleCredentialsProvider",
            locations=[gamelift.CfnFleet.LocationConfigurationProperty(
                location="location",
        
                # the properties below are optional
                location_capacity=gamelift.CfnFleet.LocationCapacityProperty(
                    desired_ec2_instances=123,
                    max_size=123,
                    min_size=123
                )
            )],
            log_paths=["logPaths"],
            max_size=123,
            metric_groups=["metricGroups"],
            min_size=123,
            new_game_session_protection_policy="newGameSessionProtectionPolicy",
            peer_vpc_aws_account_id="peerVpcAwsAccountId",
            peer_vpc_id="peerVpcId",
            resource_creation_limit_policy=gamelift.CfnFleet.ResourceCreationLimitPolicyProperty(
                new_game_sessions_per_creator=123,
                policy_period_in_minutes=123
            ),
            runtime_configuration=gamelift.CfnFleet.RuntimeConfigurationProperty(
                game_session_activation_timeout_seconds=123,
                max_concurrent_game_session_activations=123,
                server_processes=[gamelift.CfnFleet.ServerProcessProperty(
                    concurrent_executions=123,
                    launch_path="launchPath",
        
                    # the properties below are optional
                    parameters="parameters"
                )]
            ),
            scaling_policies=[gamelift.CfnFleet.ScalingPolicyProperty(
                metric_name="metricName",
                name="name",
        
                # the properties below are optional
                comparison_operator="comparisonOperator",
                evaluation_periods=123,
                location="location",
                policy_type="policyType",
                scaling_adjustment=123,
                scaling_adjustment_type="scalingAdjustmentType",
                status="status",
                target_configuration=gamelift.CfnFleet.TargetConfigurationProperty(
                    target_value=123
                ),
                threshold=123,
                update_status="updateStatus"
            )],
            script_id="scriptId",
            server_launch_parameters="serverLaunchParameters",
            server_launch_path="serverLaunchPath"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.AnywhereConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        apply_capacity: typing.Optional[builtins.str] = None,
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.CertificateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        container_groups_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ContainerGroupsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_ec2_instances: typing.Optional[jsii.Number] = None,
        ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.IpPermissionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_instance_type: typing.Optional[builtins.str] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        instance_role_credentials_provider: typing.Optional[builtins.str] = None,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.LocationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_size: typing.Optional[jsii.Number] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
        peer_vpc_id: typing.Optional[builtins.str] = None,
        resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ResourceCreationLimitPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.RuntimeConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        script_id: typing.Optional[builtins.str] = None,
        server_launch_parameters: typing.Optional[builtins.str] = None,
        server_launch_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        :param anywhere_configuration: Amazon GameLift Anywhere configuration options.
        :param apply_capacity: Current resource capacity settings for managed EC2 fleets and container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region. *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_
        :param build_id: A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        :param certificate_configuration: Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet. Amazon GameLift uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet. AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition. .. epigraph:: ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .
        :param compute_type: The type of compute resource used to host your game servers. - ``EC2`` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting. - ``CONTAINER`` – Container images with your game server build and supporting software are deployed to Amazon EC2 instances for cloud hosting. With this compute type, you must specify the ``ContainerGroupsConfiguration`` parameter. - ``ANYWHERE`` – Game servers or container images with your game server and supporting software are deployed to compute resources that are provided and managed by you. With this compute type, you can also set the ``AnywhereConfiguration`` parameter.
        :param container_groups_configuration: *This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*. Configuration details for a set of container groups, for use when creating a fleet with compute type ``CONTAINER`` . *Used with:* ``CreateFleet``
        :param description: A description for the fleet.
        :param desired_ec2_instances: The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        :param ec2_inbound_permissions: The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for EC2 and container fleets. You can leave this parameter empty when creating the fleet, but you must call ``UpdateFleetPortSettings`` to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges. To manage inbound access for a container fleet, set this parameter to the same port numbers that you set for the fleet's connection port range. During the life of the fleet, update this parameter to control which connection ports are open to inbound traffic.
        :param ec2_instance_type: The Amazon GameLift-supported Amazon EC2 instance type to use with EC2 and container fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.
        :param fleet_type: Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This fleet property can't be changed after the fleet is created.
        :param instance_role_arn: A unique identifier for an IAM role with access permissions to other AWS services. Any application that runs on an instance in the fleet--including install scripts, server processes, and other processes--can use these permissions to interact with AWS resources that you own or have access to. For more information about using the role with your game server builds, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is "EC2" or "Container".
        :param instance_role_credentials_provider: Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` . Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is "EC2" or "Container".
        :param locations: A set of remote locations to deploy additional instances to and manage as part of the fleet. This parameter can only be used when creating fleets in AWS Regions that support multiple locations. You can add any Amazon GameLift-supported AWS Region as a remote location, in the form of an AWS Region code, such as ``us-west-2`` or Local Zone code. To create a fleet with instances in the home Region only, don't set this parameter. When using this parameter, Amazon GameLift requires you to include your home location in the request.
        :param log_paths: (deprecated) This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
        :param max_size: The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
        :param min_size: The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.
        :param new_game_session_protection_policy: The status of termination protection for active game sessions on the fleet. By default, this property is set to ``NoProtection`` . - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event. - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.
        :param peer_vpc_aws_account_id: Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
        :param peer_vpc_id: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .
        :param resource_creation_limit_policy: A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
        :param runtime_configuration: Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently. .. epigraph:: The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.
        :param scaling_policies: Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
        :param script_id: The unique identifier for a Realtime configuration script to be deployed on fleet instances. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift prior to creating the fleet. This fleet property cannot be changed later. .. epigraph:: You can't use the ``!Ref`` command to reference a script created with a CloudFormation template for the fleet property ``ScriptId`` . Instead, use ``Fn::GetAtt Script.Arn`` or ``Fn::GetAtt Script.Id`` to retrieve either of these properties as input for ``ScriptId`` . Alternatively, enter a ``ScriptId`` string manually.
        :param server_launch_parameters: (deprecated) This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
        :param server_launch_path: (deprecated) This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21fe09a90444788b3c862f454214d4e160757c9b02d0598d282f68b7f79d749f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFleetProps(
            name=name,
            anywhere_configuration=anywhere_configuration,
            apply_capacity=apply_capacity,
            build_id=build_id,
            certificate_configuration=certificate_configuration,
            compute_type=compute_type,
            container_groups_configuration=container_groups_configuration,
            description=description,
            desired_ec2_instances=desired_ec2_instances,
            ec2_inbound_permissions=ec2_inbound_permissions,
            ec2_instance_type=ec2_instance_type,
            fleet_type=fleet_type,
            instance_role_arn=instance_role_arn,
            instance_role_credentials_provider=instance_role_credentials_provider,
            locations=locations,
            log_paths=log_paths,
            max_size=max_size,
            metric_groups=metric_groups,
            min_size=min_size,
            new_game_session_protection_policy=new_game_session_protection_policy,
            peer_vpc_aws_account_id=peer_vpc_aws_account_id,
            peer_vpc_id=peer_vpc_id,
            resource_creation_limit_policy=resource_creation_limit_policy,
            runtime_configuration=runtime_configuration,
            scaling_policies=scaling_policies,
            script_id=script_id,
            server_launch_parameters=server_launch_parameters,
            server_launch_path=server_launch_path,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__264e19b1dd38619175091751b1eec860e08c2225c7798789a29ec89ab8971593)
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
            type_hints = typing.get_type_hints(_typecheckingstub__905cca04e4d534db21b7356373856ed4d0fb9130ab18a34d31eb7127b3ecdbc1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrContainerGroupsConfigurationContainerGroupsPerInstanceMaxReplicaContainerGroupsPerInstance")
    def attr_container_groups_configuration_container_groups_per_instance_max_replica_container_groups_per_instance(
        self,
    ) -> jsii.Number:
        '''The maximum possible number of replica container groups that each fleet instance can have.

        :cloudformationAttribute: ContainerGroupsConfiguration.ContainerGroupsPerInstance.MaxReplicaContainerGroupsPerInstance
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrContainerGroupsConfigurationContainerGroupsPerInstanceMaxReplicaContainerGroupsPerInstance"))

    @builtins.property
    @jsii.member(jsii_name="attrFleetId")
    def attr_fleet_id(self) -> builtins.str:
        '''A unique identifier for the fleet.

        :cloudformationAttribute: FleetId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFleetId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with a fleet.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3e6bf68da3a08ee0a6dbdff6b571a1a9348dfd6d1f15864e1efd85595ae689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="anywhereConfiguration")
    def anywhere_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AnywhereConfigurationProperty"]]:
        '''Amazon GameLift Anywhere configuration options.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AnywhereConfigurationProperty"]], jsii.get(self, "anywhereConfiguration"))

    @anywhere_configuration.setter
    def anywhere_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.AnywhereConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc575abdd043760dd1cbe4178328d65df4b96ee18072484d24bd88d2e2d340ac)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "anywhereConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="applyCapacity")
    def apply_capacity(self) -> typing.Optional[builtins.str]:
        '''Current resource capacity settings for managed EC2 fleets and container fleets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "applyCapacity"))

    @apply_capacity.setter
    def apply_capacity(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e4da24e64fdcbb7830d9e09a27219d611e9c486d09dd2a970381192b5e97213)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applyCapacity", value)

    @builtins.property
    @jsii.member(jsii_name="buildId")
    def build_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a build to be deployed on the new fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "buildId"))

    @build_id.setter
    def build_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fecb16629d96a3f0b5b4acdf8ba4a4b1a44a9314ada24ee4bf29122c11df18e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "buildId", value)

    @builtins.property
    @jsii.member(jsii_name="certificateConfiguration")
    def certificate_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CertificateConfigurationProperty"]]:
        '''Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CertificateConfigurationProperty"]], jsii.get(self, "certificateConfiguration"))

    @certificate_configuration.setter
    def certificate_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.CertificateConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f46d27389fd45eb3384977842c4289c60e5795c4a4bd6e08002ec26643232bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="computeType")
    def compute_type(self) -> typing.Optional[builtins.str]:
        '''The type of compute resource used to host your game servers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "computeType"))

    @compute_type.setter
    def compute_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__022e8bf70858e61cedf1ac2f0bbe1af01706924dda3af7f4e655e78c1b5985db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeType", value)

    @builtins.property
    @jsii.member(jsii_name="containerGroupsConfiguration")
    def container_groups_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ContainerGroupsConfigurationProperty"]]:
        '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ContainerGroupsConfigurationProperty"]], jsii.get(self, "containerGroupsConfiguration"))

    @container_groups_configuration.setter
    def container_groups_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ContainerGroupsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12ab5ebb46adc7fe2bb2e1911285f98090170c29093f6e28b584096baafa36aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "containerGroupsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eec78595476346beb2b42a6ac89d6890fb357c8bc49fbafff985bc1417bca206)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="desiredEc2Instances")
    def desired_ec2_instances(self) -> typing.Optional[jsii.Number]:
        '''The number of EC2 instances that you want this fleet to host.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "desiredEc2Instances"))

    @desired_ec2_instances.setter
    def desired_ec2_instances(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4941614413c1e1554010809926c621b6030f9b38418b19c26a4dbbfc56fd9cfd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "desiredEc2Instances", value)

    @builtins.property
    @jsii.member(jsii_name="ec2InboundPermissions")
    def ec2_inbound_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.IpPermissionProperty"]]]]:
        '''The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.IpPermissionProperty"]]]], jsii.get(self, "ec2InboundPermissions"))

    @ec2_inbound_permissions.setter
    def ec2_inbound_permissions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.IpPermissionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84bfe64c88748026f1ea76b00a3c1eeeffe26c5a9e7df3f052f9069032249c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2InboundPermissions", value)

    @builtins.property
    @jsii.member(jsii_name="ec2InstanceType")
    def ec2_instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon GameLift-supported Amazon EC2 instance type to use with EC2 and container fleets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ec2InstanceType"))

    @ec2_instance_type.setter
    def ec2_instance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5edb81bb6e5f986aaa8654e60493e7ec0e42f57ed43a7481b48714433fb0b95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ec2InstanceType", value)

    @builtins.property
    @jsii.member(jsii_name="fleetType")
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use On-Demand or Spot instances for this fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fleetType"))

    @fleet_type.setter
    def fleet_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc9a52bd70aa79d8d459ba6e23d2020447c1f1d4faa157c8836aad4e87181d56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fleetType", value)

    @builtins.property
    @jsii.member(jsii_name="instanceRoleArn")
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for an IAM role with access permissions to other AWS services.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleArn"))

    @instance_role_arn.setter
    def instance_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7947f4ea6b160028fb5bbf20fcbd0cc9eb46ba122d737f3c792a6be5043d8577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="instanceRoleCredentialsProvider")
    def instance_role_credentials_provider(self) -> typing.Optional[builtins.str]:
        '''Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleCredentialsProvider"))

    @instance_role_credentials_provider.setter
    def instance_role_credentials_provider(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6765d7366d76df2864c4535568d1edf808ceec869046e302b0c842674b46c102)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRoleCredentialsProvider", value)

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationConfigurationProperty"]]]]:
        '''A set of remote locations to deploy additional instances to and manage as part of the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationConfigurationProperty"]]]], jsii.get(self, "locations"))

    @locations.setter
    def locations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1377dfdecc90d2457b2fe3e90aa35cecb44bf218eb1836fc28cbc15b7a4812f3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @builtins.property
    @jsii.member(jsii_name="logPaths")
    def log_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) This parameter is no longer used.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logPaths"))

    @log_paths.setter
    def log_paths(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35b29d2e11870cd4d0ea412c5de5d02fbb8bb765ed67873227f57868f234fe52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logPaths", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances that are allowed in the specified fleet location.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbc74cb38ce8a622308c22d16cb5fe99f9f601acdfd26460b9b33bd15037e42f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="metricGroups")
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of an AWS CloudWatch metric group to add this fleet to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "metricGroups"))

    @metric_groups.setter
    def metric_groups(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02facc74087efba3bcf2b21fc12cd9fae063e33440abacb0fdfdf65ecb3fe7ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metricGroups", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances that are allowed in the specified fleet location.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d460bc2f634afc1e2c222819f53ddf45b2647b9ccf197380a1419dfb4b91c61a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="newGameSessionProtectionPolicy")
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''The status of termination protection for active game sessions on the fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "newGameSessionProtectionPolicy"))

    @new_game_session_protection_policy.setter
    def new_game_session_protection_policy(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c8b79569fe310aaed26b6fa78159b7101d72974e478dd380ca0713aea1d9a9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "newGameSessionProtectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="peerVpcAwsAccountId")
    def peer_vpc_aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the AWS account that owns the VPC.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVpcAwsAccountId"))

    @peer_vpc_aws_account_id.setter
    def peer_vpc_aws_account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a648f419a89a6e5926858e8481241ede65ca343e3b797aecd480dec6c8b20939)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVpcAwsAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="peerVpcId")
    def peer_vpc_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "peerVpcId"))

    @peer_vpc_id.setter
    def peer_vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3fd0ab83e874e8110a1f4093ff1e48395bf94729c8f475c6e23b4d22971f3428)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "peerVpcId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceCreationLimitPolicy")
    def resource_creation_limit_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ResourceCreationLimitPolicyProperty"]]:
        '''A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ResourceCreationLimitPolicyProperty"]], jsii.get(self, "resourceCreationLimitPolicy"))

    @resource_creation_limit_policy.setter
    def resource_creation_limit_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ResourceCreationLimitPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ee8415ef994fb87ac2edf852ffd98a21384f9eccc26d3a0537563c2b00fbed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceCreationLimitPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="runtimeConfiguration")
    def runtime_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.RuntimeConfigurationProperty"]]:
        '''Instructions for how to launch and maintain server processes on instances in the fleet.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.RuntimeConfigurationProperty"]], jsii.get(self, "runtimeConfiguration"))

    @runtime_configuration.setter
    def runtime_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.RuntimeConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91bbc8eaa0f72d2032ef5cfd51906c5fc923f7ed24ede99b907cb24fe23da499)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtimeConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="scalingPolicies")
    def scaling_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ScalingPolicyProperty"]]]]:
        '''Rule that controls how a fleet is scaled.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ScalingPolicyProperty"]]]], jsii.get(self, "scalingPolicies"))

    @scaling_policies.setter
    def scaling_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ScalingPolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082c3456142a6049adc9dd4639e8b2ca94a21dbf9412cc70d0ea2e1babccf7c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="scriptId")
    def script_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for a Realtime configuration script to be deployed on fleet instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scriptId"))

    @script_id.setter
    def script_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d89c92d80f54ea7b8f3b7a14762b9c71a927d074d3727f05bc330349648ba92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptId", value)

    @builtins.property
    @jsii.member(jsii_name="serverLaunchParameters")
    def server_launch_parameters(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used but is retained for backward compatibility.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverLaunchParameters"))

    @server_launch_parameters.setter
    def server_launch_parameters(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b86e485f6c758ba0a09838614ee6f5e63a4ba69e6100fd77af039cc9f223b152)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverLaunchParameters", value)

    @builtins.property
    @jsii.member(jsii_name="serverLaunchPath")
    def server_launch_path(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverLaunchPath"))

    @server_launch_path.setter
    def server_launch_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63d5bf96be81c4a6b00ef1deb4d8846acf0053313fb89efd0ded1f0931c66844)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverLaunchPath", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.AnywhereConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"cost": "cost"},
    )
    class AnywhereConfigurationProperty:
        def __init__(self, *, cost: builtins.str) -> None:
            '''Amazon GameLift configuration options for your Anywhere fleets.

            :param cost: The cost to run your fleet per hour. Amazon GameLift uses the provided cost of your fleet to balance usage in queues. For more information about queues, see `Setting up queues <https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html>`_ in the *Amazon GameLift Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                anywhere_configuration_property = gamelift.CfnFleet.AnywhereConfigurationProperty(
                    cost="cost"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3897ffc82938e5bf4e6384b3a83b22f50c7189a71eb0fc30ea8f17642db5ef9)
                check_type(argname="argument cost", value=cost, expected_type=type_hints["cost"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cost": cost,
            }

        @builtins.property
        def cost(self) -> builtins.str:
            '''The cost to run your fleet per hour.

            Amazon GameLift uses the provided cost of your fleet to balance usage in queues. For more information about queues, see `Setting up queues <https://docs.aws.amazon.com/gamelift/latest/developerguide/queues-intro.html>`_ in the *Amazon GameLift Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-anywhereconfiguration.html#cfn-gamelift-fleet-anywhereconfiguration-cost
            '''
            result = self._values.get("cost")
            assert result is not None, "Required property 'cost' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AnywhereConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.CertificateConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"certificate_type": "certificateType"},
    )
    class CertificateConfigurationProperty:
        def __init__(self, *, certificate_type: builtins.str) -> None:
            '''Determines whether a TLS/SSL certificate is generated for a fleet.

            This feature must be enabled when creating the fleet. All instances in a fleet share the same certificate. The certificate can be retrieved by calling the `GameLift Server SDK <https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-serversdk.html>`_ operation ``GetInstanceCertificate`` .

            :param certificate_type: Indicates whether a TLS/SSL certificate is generated for a fleet. Valid values include: - *GENERATED* - Generate a TLS/SSL certificate for this fleet. - *DISABLED* - (default) Do not generate a TLS/SSL certificate for this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                certificate_configuration_property = gamelift.CfnFleet.CertificateConfigurationProperty(
                    certificate_type="certificateType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4c3cca5919f32f3e2cb6c385afda08bf3b194b8baf60b4d20e5f9f580659cc84)
                check_type(argname="argument certificate_type", value=certificate_type, expected_type=type_hints["certificate_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_type": certificate_type,
            }

        @builtins.property
        def certificate_type(self) -> builtins.str:
            '''Indicates whether a TLS/SSL certificate is generated for a fleet.

            Valid values include:

            - *GENERATED* - Generate a TLS/SSL certificate for this fleet.
            - *DISABLED* - (default) Do not generate a TLS/SSL certificate for this fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-certificateconfiguration.html#cfn-gamelift-fleet-certificateconfiguration-certificatetype
            '''
            result = self._values.get("certificate_type")
            assert result is not None, "Required property 'certificate_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CertificateConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ConnectionPortRangeProperty",
        jsii_struct_bases=[],
        name_mapping={"from_port": "fromPort", "to_port": "toPort"},
    )
    class ConnectionPortRangeProperty:
        def __init__(self, *, from_port: jsii.Number, to_port: jsii.Number) -> None:
            '''*This operation has been expanded to use with the Amazon GameLift containers feature, which is currently in public preview.*.

            The set of port numbers to open on each instance in a container fleet. Connection ports are used by inbound traffic to connect with processes that are running in containers on the fleet.

            *Part of:* ``ContainerGroupsConfiguration`` , ``ContainerGroupsAttributes``

            :param from_port: Starting value for the port range.
            :param to_port: Ending value for the port. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-connectionportrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                connection_port_range_property = gamelift.CfnFleet.ConnectionPortRangeProperty(
                    from_port=123,
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65c7b986d31ccdfa5d51331dd935bb4233bcf101bbfe90052f66eb229319a0a8)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''Starting value for the port range.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-connectionportrange.html#cfn-gamelift-fleet-connectionportrange-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''Ending value for the port.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-connectionportrange.html#cfn-gamelift-fleet-connectionportrange-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectionPortRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ContainerGroupsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connection_port_range": "connectionPortRange",
            "container_group_definition_names": "containerGroupDefinitionNames",
            "container_groups_per_instance": "containerGroupsPerInstance",
        },
    )
    class ContainerGroupsConfigurationProperty:
        def __init__(
            self,
            *,
            connection_port_range: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ConnectionPortRangeProperty", typing.Dict[builtins.str, typing.Any]]],
            container_group_definition_names: typing.Sequence[builtins.str],
            container_groups_per_instance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ContainerGroupsPerInstanceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

            Configuration details for a set of container groups, for use when creating a fleet with compute type ``CONTAINER`` .

            *Used with:* ``CreateFleet``

            :param connection_port_range: A set of ports to allow inbound traffic, including game clients, to connect to processes running in the container fleet. Connection ports are dynamically mapped to container ports, which are assigned to individual processes running in a container. The connection port range must have enough ports to map to all container ports across a fleet instance. To calculate the minimum connection ports needed, use the following formula: *[Total number of container ports as defined for containers in the replica container group] * [Desired or calculated number of replica container groups per instance] + [Total number of container ports as defined for containers in the daemon container group]* As a best practice, double the minimum number of connection ports. .. epigraph:: Use the fleet's ``EC2InboundPermissions`` property to control external access to connection ports. Set this property to the connection port numbers that you want to open access to. See ``IpPermission`` for more details.
            :param container_group_definition_names: The list of container group definition names to deploy to a new container fleet.
            :param container_groups_per_instance: The number of container groups per instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_groups_configuration_property = gamelift.CfnFleet.ContainerGroupsConfigurationProperty(
                    connection_port_range=gamelift.CfnFleet.ConnectionPortRangeProperty(
                        from_port=123,
                        to_port=123
                    ),
                    container_group_definition_names=["containerGroupDefinitionNames"],
                
                    # the properties below are optional
                    container_groups_per_instance=gamelift.CfnFleet.ContainerGroupsPerInstanceProperty(
                        desired_replica_container_groups_per_instance=123,
                        max_replica_container_groups_per_instance=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af8dbebebd0e2db6dda0806b67c6edeb6e2460f1c55d333b8c83a5380be41afd)
                check_type(argname="argument connection_port_range", value=connection_port_range, expected_type=type_hints["connection_port_range"])
                check_type(argname="argument container_group_definition_names", value=container_group_definition_names, expected_type=type_hints["container_group_definition_names"])
                check_type(argname="argument container_groups_per_instance", value=container_groups_per_instance, expected_type=type_hints["container_groups_per_instance"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connection_port_range": connection_port_range,
                "container_group_definition_names": container_group_definition_names,
            }
            if container_groups_per_instance is not None:
                self._values["container_groups_per_instance"] = container_groups_per_instance

        @builtins.property
        def connection_port_range(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFleet.ConnectionPortRangeProperty"]:
            '''A set of ports to allow inbound traffic, including game clients, to connect to processes running in the container fleet.

            Connection ports are dynamically mapped to container ports, which are assigned to individual processes running in a container. The connection port range must have enough ports to map to all container ports across a fleet instance. To calculate the minimum connection ports needed, use the following formula:

            *[Total number of container ports as defined for containers in the replica container group] * [Desired or calculated number of replica container groups per instance] + [Total number of container ports as defined for containers in the daemon container group]*

            As a best practice, double the minimum number of connection ports.
            .. epigraph::

               Use the fleet's ``EC2InboundPermissions`` property to control external access to connection ports. Set this property to the connection port numbers that you want to open access to. See ``IpPermission`` for more details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsconfiguration.html#cfn-gamelift-fleet-containergroupsconfiguration-connectionportrange
            '''
            result = self._values.get("connection_port_range")
            assert result is not None, "Required property 'connection_port_range' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFleet.ConnectionPortRangeProperty"], result)

        @builtins.property
        def container_group_definition_names(self) -> typing.List[builtins.str]:
            '''The list of container group definition names to deploy to a new container fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsconfiguration.html#cfn-gamelift-fleet-containergroupsconfiguration-containergroupdefinitionnames
            '''
            result = self._values.get("container_group_definition_names")
            assert result is not None, "Required property 'container_group_definition_names' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def container_groups_per_instance(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ContainerGroupsPerInstanceProperty"]]:
            '''The number of container groups per instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsconfiguration.html#cfn-gamelift-fleet-containergroupsconfiguration-containergroupsperinstance
            '''
            result = self._values.get("container_groups_per_instance")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.ContainerGroupsPerInstanceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerGroupsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ContainerGroupsPerInstanceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_replica_container_groups_per_instance": "desiredReplicaContainerGroupsPerInstance",
            "max_replica_container_groups_per_instance": "maxReplicaContainerGroupsPerInstance",
        },
    )
    class ContainerGroupsPerInstanceProperty:
        def __init__(
            self,
            *,
            desired_replica_container_groups_per_instance: typing.Optional[jsii.Number] = None,
            max_replica_container_groups_per_instance: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

            Determines how many replica container groups that Amazon GameLift deploys to each instance in a container fleet.

            Amazon GameLift calculates the maximum possible replica groups per instance based on the instance 's CPU and memory resources. When deploying a fleet, Amazon GameLift places replica container groups on each fleet instance based on the following:

            - If no desired value is set, Amazon GameLift places the calculated maximum.
            - If a desired number is set to a value higher than the calculated maximum, fleet creation fails..
            - If a desired number is set to a value lower than the calculated maximum, Amazon GameLift places the desired number.

            *Part of:* ``ContainerGroupsConfiguration`` , ``ContainerGroupsAttributes``

            *Returned by:* ``DescribeFleetAttributes`` , ``CreateFleet``

            :param desired_replica_container_groups_per_instance: The desired number of replica container groups to place on each fleet instance.
            :param max_replica_container_groups_per_instance: The maximum possible number of replica container groups that each fleet instance can have.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsperinstance.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                container_groups_per_instance_property = gamelift.CfnFleet.ContainerGroupsPerInstanceProperty(
                    desired_replica_container_groups_per_instance=123,
                    max_replica_container_groups_per_instance=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3473ac2106ce855ef7577b99df8d3e14e6085d02c7bf0c0fb919636a907449c1)
                check_type(argname="argument desired_replica_container_groups_per_instance", value=desired_replica_container_groups_per_instance, expected_type=type_hints["desired_replica_container_groups_per_instance"])
                check_type(argname="argument max_replica_container_groups_per_instance", value=max_replica_container_groups_per_instance, expected_type=type_hints["max_replica_container_groups_per_instance"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if desired_replica_container_groups_per_instance is not None:
                self._values["desired_replica_container_groups_per_instance"] = desired_replica_container_groups_per_instance
            if max_replica_container_groups_per_instance is not None:
                self._values["max_replica_container_groups_per_instance"] = max_replica_container_groups_per_instance

        @builtins.property
        def desired_replica_container_groups_per_instance(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The desired number of replica container groups to place on each fleet instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsperinstance.html#cfn-gamelift-fleet-containergroupsperinstance-desiredreplicacontainergroupsperinstance
            '''
            result = self._values.get("desired_replica_container_groups_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_replica_container_groups_per_instance(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum possible number of replica container groups that each fleet instance can have.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-containergroupsperinstance.html#cfn-gamelift-fleet-containergroupsperinstance-maxreplicacontainergroupsperinstance
            '''
            result = self._values.get("max_replica_container_groups_per_instance")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ContainerGroupsPerInstanceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.IpPermissionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "from_port": "fromPort",
            "ip_range": "ipRange",
            "protocol": "protocol",
            "to_port": "toPort",
        },
    )
    class IpPermissionProperty:
        def __init__(
            self,
            *,
            from_port: jsii.Number,
            ip_range: builtins.str,
            protocol: builtins.str,
            to_port: jsii.Number,
        ) -> None:
            '''A range of IP addresses and port settings that allow inbound traffic to connect to server processes on an instance in a fleet.

            New game sessions are assigned an IP address/port number combination, which must fall into the fleet's allowed ranges. Fleets with custom game builds must have permissions explicitly set. For Realtime Servers fleets, GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

            :param from_port: A starting value for a range of allowed port numbers. For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid. For fleets using Windows builds, only ports ``1026-60000`` are valid.
            :param ip_range: A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: " ``000.000.000.000/[subnet mask]`` " or optionally the shortened version " ``0.0.0.0/[subnet mask]`` ".
            :param protocol: The network communication protocol used by the fleet.
            :param to_port: An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` . For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid. For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                ip_permission_property = gamelift.CfnFleet.IpPermissionProperty(
                    from_port=123,
                    ip_range="ipRange",
                    protocol="protocol",
                    to_port=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__70f885be25c9084dbab3b02a36601be0e37c43ab741ea7dd646494423839333a)
                check_type(argname="argument from_port", value=from_port, expected_type=type_hints["from_port"])
                check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument to_port", value=to_port, expected_type=type_hints["to_port"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "from_port": from_port,
                "ip_range": ip_range,
                "protocol": protocol,
                "to_port": to_port,
            }

        @builtins.property
        def from_port(self) -> jsii.Number:
            '''A starting value for a range of allowed port numbers.

            For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid.

            For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-fromport
            '''
            result = self._values.get("from_port")
            assert result is not None, "Required property 'from_port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def ip_range(self) -> builtins.str:
            '''A range of allowed IP addresses.

            This value must be expressed in CIDR notation. Example: " ``000.000.000.000/[subnet mask]`` " or optionally the shortened version " ``0.0.0.0/[subnet mask]`` ".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-iprange
            '''
            result = self._values.get("ip_range")
            assert result is not None, "Required property 'ip_range' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network communication protocol used by the fleet.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def to_port(self) -> jsii.Number:
            '''An ending value for a range of allowed port numbers.

            Port numbers are end-inclusive. This value must be equal to or greater than ``FromPort`` .

            For fleets using Linux builds, only ports ``22`` and ``1026-60000`` are valid.

            For fleets using Windows builds, only ports ``1026-60000`` are valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-ippermission.html#cfn-gamelift-fleet-ippermission-toport
            '''
            result = self._values.get("to_port")
            assert result is not None, "Required property 'to_port' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpPermissionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.LocationCapacityProperty",
        jsii_struct_bases=[],
        name_mapping={
            "desired_ec2_instances": "desiredEc2Instances",
            "max_size": "maxSize",
            "min_size": "minSize",
        },
    )
    class LocationCapacityProperty:
        def __init__(
            self,
            *,
            desired_ec2_instances: jsii.Number,
            max_size: jsii.Number,
            min_size: jsii.Number,
        ) -> None:
            '''Current resource capacity settings for managed EC2 fleets and container fleets.

            For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

            *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :param desired_ec2_instances: The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.
            :param max_size: The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
            :param min_size: The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                location_capacity_property = gamelift.CfnFleet.LocationCapacityProperty(
                    desired_ec2_instances=123,
                    max_size=123,
                    min_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__76847ac983ab72ef92adc1b0579d769ca62af002ef71c76165cbd879da8645fc)
                check_type(argname="argument desired_ec2_instances", value=desired_ec2_instances, expected_type=type_hints["desired_ec2_instances"])
                check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
                check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "desired_ec2_instances": desired_ec2_instances,
                "max_size": max_size,
                "min_size": min_size,
            }

        @builtins.property
        def desired_ec2_instances(self) -> jsii.Number:
            '''The number of Amazon EC2 instances you want to maintain in the specified fleet location.

            This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleet's capacity settings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-desiredec2instances
            '''
            result = self._values.get("desired_ec2_instances")
            assert result is not None, "Required property 'desired_ec2_instances' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_size(self) -> jsii.Number:
            '''The maximum number of instances that are allowed in the specified fleet location.

            If this parameter is not set, the default is 1.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-maxsize
            '''
            result = self._values.get("max_size")
            assert result is not None, "Required property 'max_size' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def min_size(self) -> jsii.Number:
            '''The minimum number of instances that are allowed in the specified fleet location.

            If this parameter is not set, the default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationcapacity.html#cfn-gamelift-fleet-locationcapacity-minsize
            '''
            result = self._values.get("min_size")
            assert result is not None, "Required property 'min_size' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationCapacityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.LocationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"location": "location", "location_capacity": "locationCapacity"},
    )
    class LocationConfigurationProperty:
        def __init__(
            self,
            *,
            location: builtins.str,
            location_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.LocationCapacityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''*This data type has been expanded to use with the Amazon GameLift containers feature, which is currently in public preview.*.

            A remote location where a multi-location fleet can deploy game servers for game hosting.

            :param location: An AWS Region code, such as ``us-west-2`` .
            :param location_capacity: Current resource capacity settings for managed EC2 fleets and container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region. *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                location_configuration_property = gamelift.CfnFleet.LocationConfigurationProperty(
                    location="location",
                
                    # the properties below are optional
                    location_capacity=gamelift.CfnFleet.LocationCapacityProperty(
                        desired_ec2_instances=123,
                        max_size=123,
                        min_size=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__716ff23eda74da42620dc64832ed27ab5a267661bd90b16577ee48991436d14c)
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument location_capacity", value=location_capacity, expected_type=type_hints["location_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "location": location,
            }
            if location_capacity is not None:
                self._values["location_capacity"] = location_capacity

        @builtins.property
        def location(self) -> builtins.str:
            '''An AWS Region code, such as ``us-west-2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html#cfn-gamelift-fleet-locationconfiguration-location
            '''
            result = self._values.get("location")
            assert result is not None, "Required property 'location' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def location_capacity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationCapacityProperty"]]:
            '''Current resource capacity settings for managed EC2 fleets and container fleets.

            For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

            *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-locationconfiguration.html#cfn-gamelift-fleet-locationconfiguration-locationcapacity
            '''
            result = self._values.get("location_capacity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.LocationCapacityProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ResourceCreationLimitPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "new_game_sessions_per_creator": "newGameSessionsPerCreator",
            "policy_period_in_minutes": "policyPeriodInMinutes",
        },
    )
    class ResourceCreationLimitPolicyProperty:
        def __init__(
            self,
            *,
            new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
            policy_period_in_minutes: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''A policy that limits the number of game sessions a player can create on the same fleet.

            This optional policy gives game owners control over how players can consume available game server resources. A resource creation policy makes the following statement: "An individual player can create a maximum number of new game sessions within a specified time period".

            The policy is evaluated when a player tries to create a new game session. For example, assume you have a policy of 10 new game sessions and a time period of 60 minutes. On receiving a ``CreateGameSession`` request, Amazon GameLift checks that the player (identified by ``CreatorId`` ) has created fewer than 10 game sessions in the past 60 minutes.

            :param new_game_sessions_per_creator: A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources. The policy is evaluated when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.
            :param policy_period_in_minutes: The time span used in evaluating the resource creation limit policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                resource_creation_limit_policy_property = gamelift.CfnFleet.ResourceCreationLimitPolicyProperty(
                    new_game_sessions_per_creator=123,
                    policy_period_in_minutes=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1b5bf70d1fc5987b674dcb2717a733f347f6ff57d29689b7a2a12d07ccfab884)
                check_type(argname="argument new_game_sessions_per_creator", value=new_game_sessions_per_creator, expected_type=type_hints["new_game_sessions_per_creator"])
                check_type(argname="argument policy_period_in_minutes", value=policy_period_in_minutes, expected_type=type_hints["policy_period_in_minutes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if new_game_sessions_per_creator is not None:
                self._values["new_game_sessions_per_creator"] = new_game_sessions_per_creator
            if policy_period_in_minutes is not None:
                self._values["policy_period_in_minutes"] = policy_period_in_minutes

        @builtins.property
        def new_game_sessions_per_creator(self) -> typing.Optional[jsii.Number]:
            '''A policy that puts limits on the number of game sessions that a player can create within a specified span of time.

            With this policy, you can control players' ability to consume available resources.

            The policy is evaluated when a player tries to create a new game session. On receiving a ``CreateGameSession`` request, Amazon GameLift checks that the player (identified by ``CreatorId`` ) has created fewer than game session limit in the specified time period.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-newgamesessionspercreator
            '''
            result = self._values.get("new_game_sessions_per_creator")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def policy_period_in_minutes(self) -> typing.Optional[jsii.Number]:
            '''The time span used in evaluating the resource creation limit policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-resourcecreationlimitpolicy.html#cfn-gamelift-fleet-resourcecreationlimitpolicy-policyperiodinminutes
            '''
            result = self._values.get("policy_period_in_minutes")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResourceCreationLimitPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.RuntimeConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "game_session_activation_timeout_seconds": "gameSessionActivationTimeoutSeconds",
            "max_concurrent_game_session_activations": "maxConcurrentGameSessionActivations",
            "server_processes": "serverProcesses",
        },
    )
    class RuntimeConfigurationProperty:
        def __init__(
            self,
            *,
            game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
            max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
            server_processes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.ServerProcessProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A collection of server process configurations that describe the set of processes to run on each instance in a fleet.

            Server processes run either an executable in a custom game build or a Realtime Servers script. GameLift launches the configured processes, manages their life cycle, and replaces them as needed. Each instance checks regularly for an updated runtime configuration.

            A GameLift instance is limited to 50 processes running concurrently. To calculate the total number of processes in a runtime configuration, add the values of the ``ConcurrentExecutions`` parameter for each ServerProcess. Learn more about `Running Multiple Processes on a Fleet <https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-multiprocess.html>`_ .

            :param game_session_activation_timeout_seconds: The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players. During this time, the game session is in status ``ACTIVATING`` . If the game session does not become active before the timeout, it is ended and the game session status is changed to ``TERMINATED`` .
            :param max_concurrent_game_session_activations: The number of game sessions in status ``ACTIVATING`` to allow on an instance or container. This setting limits the instance resources that can be used for new game activations at any one time.
            :param server_processes: A collection of server process configurations that identify what server processes to run on fleet computes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                runtime_configuration_property = gamelift.CfnFleet.RuntimeConfigurationProperty(
                    game_session_activation_timeout_seconds=123,
                    max_concurrent_game_session_activations=123,
                    server_processes=[gamelift.CfnFleet.ServerProcessProperty(
                        concurrent_executions=123,
                        launch_path="launchPath",
                
                        # the properties below are optional
                        parameters="parameters"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ae990fc53511e6175c77d897f3a8a6bc35be77827bfc0f1be6b1f8d7967e54c3)
                check_type(argname="argument game_session_activation_timeout_seconds", value=game_session_activation_timeout_seconds, expected_type=type_hints["game_session_activation_timeout_seconds"])
                check_type(argname="argument max_concurrent_game_session_activations", value=max_concurrent_game_session_activations, expected_type=type_hints["max_concurrent_game_session_activations"])
                check_type(argname="argument server_processes", value=server_processes, expected_type=type_hints["server_processes"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if game_session_activation_timeout_seconds is not None:
                self._values["game_session_activation_timeout_seconds"] = game_session_activation_timeout_seconds
            if max_concurrent_game_session_activations is not None:
                self._values["max_concurrent_game_session_activations"] = max_concurrent_game_session_activations
            if server_processes is not None:
                self._values["server_processes"] = server_processes

        @builtins.property
        def game_session_activation_timeout_seconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum amount of time (in seconds) allowed to launch a new game session and have it report ready to host players.

            During this time, the game session is in status ``ACTIVATING`` . If the game session does not become active before the timeout, it is ended and the game session status is changed to ``TERMINATED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-gamesessionactivationtimeoutseconds
            '''
            result = self._values.get("game_session_activation_timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_concurrent_game_session_activations(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The number of game sessions in status ``ACTIVATING`` to allow on an instance or container.

            This setting limits the instance resources that can be used for new game activations at any one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-maxconcurrentgamesessionactivations
            '''
            result = self._values.get("max_concurrent_game_session_activations")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_processes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServerProcessProperty"]]]]:
            '''A collection of server process configurations that identify what server processes to run on fleet computes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-serverprocesses
            '''
            result = self._values.get("server_processes")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServerProcessProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuntimeConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "metric_name": "metricName",
            "name": "name",
            "comparison_operator": "comparisonOperator",
            "evaluation_periods": "evaluationPeriods",
            "location": "location",
            "policy_type": "policyType",
            "scaling_adjustment": "scalingAdjustment",
            "scaling_adjustment_type": "scalingAdjustmentType",
            "status": "status",
            "target_configuration": "targetConfiguration",
            "threshold": "threshold",
            "update_status": "updateStatus",
        },
    )
    class ScalingPolicyProperty:
        def __init__(
            self,
            *,
            metric_name: builtins.str,
            name: builtins.str,
            comparison_operator: typing.Optional[builtins.str] = None,
            evaluation_periods: typing.Optional[jsii.Number] = None,
            location: typing.Optional[builtins.str] = None,
            policy_type: typing.Optional[builtins.str] = None,
            scaling_adjustment: typing.Optional[jsii.Number] = None,
            scaling_adjustment_type: typing.Optional[builtins.str] = None,
            status: typing.Optional[builtins.str] = None,
            target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.TargetConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            threshold: typing.Optional[jsii.Number] = None,
            update_status: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Rule that controls how a fleet is scaled.

            Scaling policies are uniquely identified by the combination of name and fleet ID.

            :param metric_name: Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment. For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`_ . - *ActivatingGameSessions* -- Game sessions in the process of being created. - *ActiveGameSessions* -- Game sessions that are currently running. - *ActiveInstances* -- Fleet instances that are currently running at least one game session. - *AvailableGameSessions* -- Additional game sessions that fleet could host simultaneously, given current capacity. - *AvailablePlayerSessions* -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included. - *CurrentPlayerSessions* -- Player slots in active game sessions that are being used by a player or are reserved for a player. - *IdleInstances* -- Active instances that are currently hosting zero game sessions. - *PercentAvailableGameSessions* -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy. - *PercentIdleInstances* -- Percentage of the total number of active instances that are hosting zero game sessions. - *QueueDepth* -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination. - *WaitTime* -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
            :param name: A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
            :param comparison_operator: Comparison operator to use when measuring a metric against the threshold value.
            :param evaluation_periods: Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
            :param location: The fleet location.
            :param policy_type: The type of scaling policy to create. For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .
            :param scaling_adjustment: Amount of adjustment to make, based on the scaling adjustment type.
            :param scaling_adjustment_type: The type of adjustment to make to a fleet's instance count. - *ChangeInCapacity* -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down. - *ExactCapacity* -- set the instance count to the scaling adjustment value. - *PercentChangeInCapacity* -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.
            :param status: Current status of the scaling policy. The scaling policy can be in force only when in an ``ACTIVE`` status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change. - *ACTIVE* -- The scaling policy can be used for auto-scaling a fleet. - *UPDATE_REQUESTED* -- A request to update the scaling policy has been received. - *UPDATING* -- A change is being made to the scaling policy. - *DELETE_REQUESTED* -- A request to delete the scaling policy has been received. - *DELETING* -- The scaling policy is being deleted. - *DELETED* -- The scaling policy has been deleted. - *ERROR* -- An error occurred in creating the policy. It should be removed and recreated.
            :param target_configuration: An object that contains settings for a target-based scaling policy.
            :param threshold: Metric value used to trigger a scaling event.
            :param update_status: The current status of the fleet's scaling policies in a requested fleet location. The status ``PENDING_UPDATE`` indicates that an update was requested for the fleet but has not yet been completed for the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                scaling_policy_property = gamelift.CfnFleet.ScalingPolicyProperty(
                    metric_name="metricName",
                    name="name",
                
                    # the properties below are optional
                    comparison_operator="comparisonOperator",
                    evaluation_periods=123,
                    location="location",
                    policy_type="policyType",
                    scaling_adjustment=123,
                    scaling_adjustment_type="scalingAdjustmentType",
                    status="status",
                    target_configuration=gamelift.CfnFleet.TargetConfigurationProperty(
                        target_value=123
                    ),
                    threshold=123,
                    update_status="updateStatus"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8690870b8fddf2f2747a9a00d8f1a693d624b5f4f72283ed427b04667f02bd8)
                check_type(argname="argument metric_name", value=metric_name, expected_type=type_hints["metric_name"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument evaluation_periods", value=evaluation_periods, expected_type=type_hints["evaluation_periods"])
                check_type(argname="argument location", value=location, expected_type=type_hints["location"])
                check_type(argname="argument policy_type", value=policy_type, expected_type=type_hints["policy_type"])
                check_type(argname="argument scaling_adjustment", value=scaling_adjustment, expected_type=type_hints["scaling_adjustment"])
                check_type(argname="argument scaling_adjustment_type", value=scaling_adjustment_type, expected_type=type_hints["scaling_adjustment_type"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
                check_type(argname="argument target_configuration", value=target_configuration, expected_type=type_hints["target_configuration"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument update_status", value=update_status, expected_type=type_hints["update_status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "metric_name": metric_name,
                "name": name,
            }
            if comparison_operator is not None:
                self._values["comparison_operator"] = comparison_operator
            if evaluation_periods is not None:
                self._values["evaluation_periods"] = evaluation_periods
            if location is not None:
                self._values["location"] = location
            if policy_type is not None:
                self._values["policy_type"] = policy_type
            if scaling_adjustment is not None:
                self._values["scaling_adjustment"] = scaling_adjustment
            if scaling_adjustment_type is not None:
                self._values["scaling_adjustment_type"] = scaling_adjustment_type
            if status is not None:
                self._values["status"] = status
            if target_configuration is not None:
                self._values["target_configuration"] = target_configuration
            if threshold is not None:
                self._values["threshold"] = threshold
            if update_status is not None:
                self._values["update_status"] = update_status

        @builtins.property
        def metric_name(self) -> builtins.str:
            '''Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment.

            For detailed descriptions of fleet metrics, see `Monitor Amazon GameLift with Amazon CloudWatch <https://docs.aws.amazon.com/gamelift/latest/developerguide/monitoring-cloudwatch.html>`_ .

            - *ActivatingGameSessions* -- Game sessions in the process of being created.
            - *ActiveGameSessions* -- Game sessions that are currently running.
            - *ActiveInstances* -- Fleet instances that are currently running at least one game session.
            - *AvailableGameSessions* -- Additional game sessions that fleet could host simultaneously, given current capacity.
            - *AvailablePlayerSessions* -- Empty player slots in currently active game sessions. This includes game sessions that are not currently accepting players. Reserved player slots are not included.
            - *CurrentPlayerSessions* -- Player slots in active game sessions that are being used by a player or are reserved for a player.
            - *IdleInstances* -- Active instances that are currently hosting zero game sessions.
            - *PercentAvailableGameSessions* -- Unused percentage of the total number of game sessions that a fleet could host simultaneously, given current capacity. Use this metric for a target-based scaling policy.
            - *PercentIdleInstances* -- Percentage of the total number of active instances that are hosting zero game sessions.
            - *QueueDepth* -- Pending game session placement requests, in any queue, where the current fleet is the top-priority destination.
            - *WaitTime* -- Current wait time for pending game session placement requests, in any queue, where the current fleet is the top-priority destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-metricname
            '''
            result = self._values.get("metric_name")
            assert result is not None, "Required property 'metric_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''A descriptive label that is associated with a fleet's scaling policy.

            Policy names do not need to be unique.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def comparison_operator(self) -> typing.Optional[builtins.str]:
            '''Comparison operator to use when measuring a metric against the threshold value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def evaluation_periods(self) -> typing.Optional[jsii.Number]:
            '''Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-evaluationperiods
            '''
            result = self._values.get("evaluation_periods")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def location(self) -> typing.Optional[builtins.str]:
            '''The fleet location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-location
            '''
            result = self._values.get("location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def policy_type(self) -> typing.Optional[builtins.str]:
            '''The type of scaling policy to create.

            For a target-based policy, set the parameter *MetricName* to 'PercentAvailableGameSessions' and specify a *TargetConfiguration* . For a rule-based policy set the following parameters: *MetricName* , *ComparisonOperator* , *Threshold* , *EvaluationPeriods* , *ScalingAdjustmentType* , and *ScalingAdjustment* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-policytype
            '''
            result = self._values.get("policy_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def scaling_adjustment(self) -> typing.Optional[jsii.Number]:
            '''Amount of adjustment to make, based on the scaling adjustment type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-scalingadjustment
            '''
            result = self._values.get("scaling_adjustment")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def scaling_adjustment_type(self) -> typing.Optional[builtins.str]:
            '''The type of adjustment to make to a fleet's instance count.

            - *ChangeInCapacity* -- add (or subtract) the scaling adjustment value from the current instance count. Positive values scale up while negative values scale down.
            - *ExactCapacity* -- set the instance count to the scaling adjustment value.
            - *PercentChangeInCapacity* -- increase or reduce the current instance count by the scaling adjustment, read as a percentage. Positive values scale up while negative values scale down.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-scalingadjustmenttype
            '''
            result = self._values.get("scaling_adjustment_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def status(self) -> typing.Optional[builtins.str]:
            '''Current status of the scaling policy.

            The scaling policy can be in force only when in an ``ACTIVE`` status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change.

            - *ACTIVE* -- The scaling policy can be used for auto-scaling a fleet.
            - *UPDATE_REQUESTED* -- A request to update the scaling policy has been received.
            - *UPDATING* -- A change is being made to the scaling policy.
            - *DELETE_REQUESTED* -- A request to delete the scaling policy has been received.
            - *DELETING* -- The scaling policy is being deleted.
            - *DELETED* -- The scaling policy has been deleted.
            - *ERROR* -- An error occurred in creating the policy. It should be removed and recreated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-status
            '''
            result = self._values.get("status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_configuration(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.TargetConfigurationProperty"]]:
            '''An object that contains settings for a target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-targetconfiguration
            '''
            result = self._values.get("target_configuration")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFleet.TargetConfigurationProperty"]], result)

        @builtins.property
        def threshold(self) -> typing.Optional[jsii.Number]:
            '''Metric value used to trigger a scaling event.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-threshold
            '''
            result = self._values.get("threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def update_status(self) -> typing.Optional[builtins.str]:
            '''The current status of the fleet's scaling policies in a requested fleet location.

            The status ``PENDING_UPDATE`` indicates that an update was requested for the fleet but has not yet been completed for the location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-scalingpolicy.html#cfn-gamelift-fleet-scalingpolicy-updatestatus
            '''
            result = self._values.get("update_status")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.ServerProcessProperty",
        jsii_struct_bases=[],
        name_mapping={
            "concurrent_executions": "concurrentExecutions",
            "launch_path": "launchPath",
            "parameters": "parameters",
        },
    )
    class ServerProcessProperty:
        def __init__(
            self,
            *,
            concurrent_executions: jsii.Number,
            launch_path: builtins.str,
            parameters: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A set of instructions for launching server processes on each instance in a fleet.

            Server processes run either an executable in a custom game build or a Realtime Servers script.

            :param concurrent_executions: The number of server processes using this configuration that run concurrently on each instance or container..
            :param launch_path: The location of a game build executable or Realtime script. Game builds and Realtime scripts are installed on instances at the root: - Windows (custom game builds only): ``C:\\game`` . Example: " ``C:\\game\\MyGame\\server.exe`` " - Linux: ``/local/game`` . Examples: " ``/local/game/MyGame/server.exe`` " or " ``/local/game/MyRealtimeScript.js`` " .. epigraph:: Amazon GameLift doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations ``initSDK()`` and ``ProcessReady()`` .
            :param parameters: An optional list of parameters to pass to the server executable or Realtime script on launch. Length Constraints: Minimum length of 1. Maximum length of 1024. Pattern: [A-Za-z0-9_:.+/\\- =@{},?'[]"]+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                server_process_property = gamelift.CfnFleet.ServerProcessProperty(
                    concurrent_executions=123,
                    launch_path="launchPath",
                
                    # the properties below are optional
                    parameters="parameters"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc845ade67d7aff6536f53651c26f049fc04883863968a83da759b79b0a6d035)
                check_type(argname="argument concurrent_executions", value=concurrent_executions, expected_type=type_hints["concurrent_executions"])
                check_type(argname="argument launch_path", value=launch_path, expected_type=type_hints["launch_path"])
                check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "concurrent_executions": concurrent_executions,
                "launch_path": launch_path,
            }
            if parameters is not None:
                self._values["parameters"] = parameters

        @builtins.property
        def concurrent_executions(self) -> jsii.Number:
            '''The number of server processes using this configuration that run concurrently on each instance or container..

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-concurrentexecutions
            '''
            result = self._values.get("concurrent_executions")
            assert result is not None, "Required property 'concurrent_executions' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def launch_path(self) -> builtins.str:
            '''The location of a game build executable or Realtime script.

            Game builds and Realtime scripts are installed on instances at the root:

            - Windows (custom game builds only): ``C:\\game`` . Example: " ``C:\\game\\MyGame\\server.exe`` "
            - Linux: ``/local/game`` . Examples: " ``/local/game/MyGame/server.exe`` " or " ``/local/game/MyRealtimeScript.js`` "

            .. epigraph::

               Amazon GameLift doesn't support the use of setup scripts that launch the game executable. For custom game builds, this parameter must indicate the executable that calls the server SDK operations ``initSDK()`` and ``ProcessReady()`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-launchpath
            '''
            result = self._values.get("launch_path")
            assert result is not None, "Required property 'launch_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(self) -> typing.Optional[builtins.str]:
            '''An optional list of parameters to pass to the server executable or Realtime script on launch.

            Length Constraints: Minimum length of 1. Maximum length of 1024.

            Pattern: [A-Za-z0-9_:.+/- =@{},?'[]"]+

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-parameters
            '''
            result = self._values.get("parameters")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServerProcessProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet.TargetConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_value": "targetValue"},
    )
    class TargetConfigurationProperty:
        def __init__(self, *, target_value: jsii.Number) -> None:
            '''Settings for a target-based scaling policy.

            A target-based policy tracks a particular fleet metric specifies a target value for the metric. As player usage changes, the policy triggers Amazon GameLift to adjust capacity so that the metric returns to the target value. The target configuration specifies settings as needed for the target based policy, including the target value.

            :param target_value: Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-targetconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                target_configuration_property = gamelift.CfnFleet.TargetConfigurationProperty(
                    target_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__472ce4c72467f1a69fc974099623863890460564fbbe1e98eb694a9a4b1546b7)
                check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_value": target_value,
            }

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''Desired value to use with a target-based scaling policy.

            The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-targetconfiguration.html#cfn-gamelift-fleet-targetconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "anywhere_configuration": "anywhereConfiguration",
        "apply_capacity": "applyCapacity",
        "build_id": "buildId",
        "certificate_configuration": "certificateConfiguration",
        "compute_type": "computeType",
        "container_groups_configuration": "containerGroupsConfiguration",
        "description": "description",
        "desired_ec2_instances": "desiredEc2Instances",
        "ec2_inbound_permissions": "ec2InboundPermissions",
        "ec2_instance_type": "ec2InstanceType",
        "fleet_type": "fleetType",
        "instance_role_arn": "instanceRoleArn",
        "instance_role_credentials_provider": "instanceRoleCredentialsProvider",
        "locations": "locations",
        "log_paths": "logPaths",
        "max_size": "maxSize",
        "metric_groups": "metricGroups",
        "min_size": "minSize",
        "new_game_session_protection_policy": "newGameSessionProtectionPolicy",
        "peer_vpc_aws_account_id": "peerVpcAwsAccountId",
        "peer_vpc_id": "peerVpcId",
        "resource_creation_limit_policy": "resourceCreationLimitPolicy",
        "runtime_configuration": "runtimeConfiguration",
        "scaling_policies": "scalingPolicies",
        "script_id": "scriptId",
        "server_launch_parameters": "serverLaunchParameters",
        "server_launch_path": "serverLaunchPath",
    },
)
class CfnFleetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        apply_capacity: typing.Optional[builtins.str] = None,
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        container_groups_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ContainerGroupsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        desired_ec2_instances: typing.Optional[jsii.Number] = None,
        ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_instance_type: typing.Optional[builtins.str] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
        instance_role_credentials_provider: typing.Optional[builtins.str] = None,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
        min_size: typing.Optional[jsii.Number] = None,
        new_game_session_protection_policy: typing.Optional[builtins.str] = None,
        peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
        peer_vpc_id: typing.Optional[builtins.str] = None,
        resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ResourceCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.RuntimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        script_id: typing.Optional[builtins.str] = None,
        server_launch_parameters: typing.Optional[builtins.str] = None,
        server_launch_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        :param anywhere_configuration: Amazon GameLift Anywhere configuration options.
        :param apply_capacity: Current resource capacity settings for managed EC2 fleets and container fleets. For multi-location fleets, location values might refer to a fleet's remote location or its home Region. *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_
        :param build_id: A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        :param certificate_configuration: Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet. Amazon GameLift uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet. AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition. .. epigraph:: ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .
        :param compute_type: The type of compute resource used to host your game servers. - ``EC2`` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting. - ``CONTAINER`` – Container images with your game server build and supporting software are deployed to Amazon EC2 instances for cloud hosting. With this compute type, you must specify the ``ContainerGroupsConfiguration`` parameter. - ``ANYWHERE`` – Game servers or container images with your game server and supporting software are deployed to compute resources that are provided and managed by you. With this compute type, you can also set the ``AnywhereConfiguration`` parameter.
        :param container_groups_configuration: *This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*. Configuration details for a set of container groups, for use when creating a fleet with compute type ``CONTAINER`` . *Used with:* ``CreateFleet``
        :param description: A description for the fleet.
        :param desired_ec2_instances: The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        :param ec2_inbound_permissions: The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet. Set this parameter for EC2 and container fleets. You can leave this parameter empty when creating the fleet, but you must call ``UpdateFleetPortSettings`` to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges. To manage inbound access for a container fleet, set this parameter to the same port numbers that you set for the fleet's connection port range. During the life of the fleet, update this parameter to control which connection ports are open to inbound traffic.
        :param ec2_instance_type: The Amazon GameLift-supported Amazon EC2 instance type to use with EC2 and container fleets. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.
        :param fleet_type: Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This fleet property can't be changed after the fleet is created.
        :param instance_role_arn: A unique identifier for an IAM role with access permissions to other AWS services. Any application that runs on an instance in the fleet--including install scripts, server processes, and other processes--can use these permissions to interact with AWS resources that you own or have access to. For more information about using the role with your game server builds, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is "EC2" or "Container".
        :param instance_role_credentials_provider: Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` . Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is "EC2" or "Container".
        :param locations: A set of remote locations to deploy additional instances to and manage as part of the fleet. This parameter can only be used when creating fleets in AWS Regions that support multiple locations. You can add any Amazon GameLift-supported AWS Region as a remote location, in the form of an AWS Region code, such as ``us-west-2`` or Local Zone code. To create a fleet with instances in the home Region only, don't set this parameter. When using this parameter, Amazon GameLift requires you to include your home location in the request.
        :param log_paths: (deprecated) This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
        :param max_size: The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
        :param min_size: The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.
        :param new_game_session_protection_policy: The status of termination protection for active game sessions on the fleet. By default, this property is set to ``NoProtection`` . - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event. - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.
        :param peer_vpc_aws_account_id: Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
        :param peer_vpc_id: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .
        :param resource_creation_limit_policy: A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
        :param runtime_configuration: Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently. .. epigraph:: The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.
        :param scaling_policies: Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
        :param script_id: The unique identifier for a Realtime configuration script to be deployed on fleet instances. You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift prior to creating the fleet. This fleet property cannot be changed later. .. epigraph:: You can't use the ``!Ref`` command to reference a script created with a CloudFormation template for the fleet property ``ScriptId`` . Instead, use ``Fn::GetAtt Script.Arn`` or ``Fn::GetAtt Script.Id`` to retrieve either of these properties as input for ``ScriptId`` . Alternatively, enter a ``ScriptId`` string manually.
        :param server_launch_parameters: (deprecated) This parameter is no longer used but is retained for backward compatibility. Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.
        :param server_launch_path: (deprecated) This parameter is no longer used. Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_fleet_props = gamelift.CfnFleetProps(
                name="name",
            
                # the properties below are optional
                anywhere_configuration=gamelift.CfnFleet.AnywhereConfigurationProperty(
                    cost="cost"
                ),
                apply_capacity="applyCapacity",
                build_id="buildId",
                certificate_configuration=gamelift.CfnFleet.CertificateConfigurationProperty(
                    certificate_type="certificateType"
                ),
                compute_type="computeType",
                container_groups_configuration=gamelift.CfnFleet.ContainerGroupsConfigurationProperty(
                    connection_port_range=gamelift.CfnFleet.ConnectionPortRangeProperty(
                        from_port=123,
                        to_port=123
                    ),
                    container_group_definition_names=["containerGroupDefinitionNames"],
            
                    # the properties below are optional
                    container_groups_per_instance=gamelift.CfnFleet.ContainerGroupsPerInstanceProperty(
                        desired_replica_container_groups_per_instance=123,
                        max_replica_container_groups_per_instance=123
                    )
                ),
                description="description",
                desired_ec2_instances=123,
                ec2_inbound_permissions=[gamelift.CfnFleet.IpPermissionProperty(
                    from_port=123,
                    ip_range="ipRange",
                    protocol="protocol",
                    to_port=123
                )],
                ec2_instance_type="ec2InstanceType",
                fleet_type="fleetType",
                instance_role_arn="instanceRoleArn",
                instance_role_credentials_provider="instanceRoleCredentialsProvider",
                locations=[gamelift.CfnFleet.LocationConfigurationProperty(
                    location="location",
            
                    # the properties below are optional
                    location_capacity=gamelift.CfnFleet.LocationCapacityProperty(
                        desired_ec2_instances=123,
                        max_size=123,
                        min_size=123
                    )
                )],
                log_paths=["logPaths"],
                max_size=123,
                metric_groups=["metricGroups"],
                min_size=123,
                new_game_session_protection_policy="newGameSessionProtectionPolicy",
                peer_vpc_aws_account_id="peerVpcAwsAccountId",
                peer_vpc_id="peerVpcId",
                resource_creation_limit_policy=gamelift.CfnFleet.ResourceCreationLimitPolicyProperty(
                    new_game_sessions_per_creator=123,
                    policy_period_in_minutes=123
                ),
                runtime_configuration=gamelift.CfnFleet.RuntimeConfigurationProperty(
                    game_session_activation_timeout_seconds=123,
                    max_concurrent_game_session_activations=123,
                    server_processes=[gamelift.CfnFleet.ServerProcessProperty(
                        concurrent_executions=123,
                        launch_path="launchPath",
            
                        # the properties below are optional
                        parameters="parameters"
                    )]
                ),
                scaling_policies=[gamelift.CfnFleet.ScalingPolicyProperty(
                    metric_name="metricName",
                    name="name",
            
                    # the properties below are optional
                    comparison_operator="comparisonOperator",
                    evaluation_periods=123,
                    location="location",
                    policy_type="policyType",
                    scaling_adjustment=123,
                    scaling_adjustment_type="scalingAdjustmentType",
                    status="status",
                    target_configuration=gamelift.CfnFleet.TargetConfigurationProperty(
                        target_value=123
                    ),
                    threshold=123,
                    update_status="updateStatus"
                )],
                script_id="scriptId",
                server_launch_parameters="serverLaunchParameters",
                server_launch_path="serverLaunchPath"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a51a418ba5b606bdfc45dc50c3172e280a12e078a7392f3258d5d329e037a55)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument anywhere_configuration", value=anywhere_configuration, expected_type=type_hints["anywhere_configuration"])
            check_type(argname="argument apply_capacity", value=apply_capacity, expected_type=type_hints["apply_capacity"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
            check_type(argname="argument certificate_configuration", value=certificate_configuration, expected_type=type_hints["certificate_configuration"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument container_groups_configuration", value=container_groups_configuration, expected_type=type_hints["container_groups_configuration"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_ec2_instances", value=desired_ec2_instances, expected_type=type_hints["desired_ec2_instances"])
            check_type(argname="argument ec2_inbound_permissions", value=ec2_inbound_permissions, expected_type=type_hints["ec2_inbound_permissions"])
            check_type(argname="argument ec2_instance_type", value=ec2_instance_type, expected_type=type_hints["ec2_instance_type"])
            check_type(argname="argument fleet_type", value=fleet_type, expected_type=type_hints["fleet_type"])
            check_type(argname="argument instance_role_arn", value=instance_role_arn, expected_type=type_hints["instance_role_arn"])
            check_type(argname="argument instance_role_credentials_provider", value=instance_role_credentials_provider, expected_type=type_hints["instance_role_credentials_provider"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
            check_type(argname="argument log_paths", value=log_paths, expected_type=type_hints["log_paths"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument metric_groups", value=metric_groups, expected_type=type_hints["metric_groups"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument new_game_session_protection_policy", value=new_game_session_protection_policy, expected_type=type_hints["new_game_session_protection_policy"])
            check_type(argname="argument peer_vpc_aws_account_id", value=peer_vpc_aws_account_id, expected_type=type_hints["peer_vpc_aws_account_id"])
            check_type(argname="argument peer_vpc_id", value=peer_vpc_id, expected_type=type_hints["peer_vpc_id"])
            check_type(argname="argument resource_creation_limit_policy", value=resource_creation_limit_policy, expected_type=type_hints["resource_creation_limit_policy"])
            check_type(argname="argument runtime_configuration", value=runtime_configuration, expected_type=type_hints["runtime_configuration"])
            check_type(argname="argument scaling_policies", value=scaling_policies, expected_type=type_hints["scaling_policies"])
            check_type(argname="argument script_id", value=script_id, expected_type=type_hints["script_id"])
            check_type(argname="argument server_launch_parameters", value=server_launch_parameters, expected_type=type_hints["server_launch_parameters"])
            check_type(argname="argument server_launch_path", value=server_launch_path, expected_type=type_hints["server_launch_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if anywhere_configuration is not None:
            self._values["anywhere_configuration"] = anywhere_configuration
        if apply_capacity is not None:
            self._values["apply_capacity"] = apply_capacity
        if build_id is not None:
            self._values["build_id"] = build_id
        if certificate_configuration is not None:
            self._values["certificate_configuration"] = certificate_configuration
        if compute_type is not None:
            self._values["compute_type"] = compute_type
        if container_groups_configuration is not None:
            self._values["container_groups_configuration"] = container_groups_configuration
        if description is not None:
            self._values["description"] = description
        if desired_ec2_instances is not None:
            self._values["desired_ec2_instances"] = desired_ec2_instances
        if ec2_inbound_permissions is not None:
            self._values["ec2_inbound_permissions"] = ec2_inbound_permissions
        if ec2_instance_type is not None:
            self._values["ec2_instance_type"] = ec2_instance_type
        if fleet_type is not None:
            self._values["fleet_type"] = fleet_type
        if instance_role_arn is not None:
            self._values["instance_role_arn"] = instance_role_arn
        if instance_role_credentials_provider is not None:
            self._values["instance_role_credentials_provider"] = instance_role_credentials_provider
        if locations is not None:
            self._values["locations"] = locations
        if log_paths is not None:
            self._values["log_paths"] = log_paths
        if max_size is not None:
            self._values["max_size"] = max_size
        if metric_groups is not None:
            self._values["metric_groups"] = metric_groups
        if min_size is not None:
            self._values["min_size"] = min_size
        if new_game_session_protection_policy is not None:
            self._values["new_game_session_protection_policy"] = new_game_session_protection_policy
        if peer_vpc_aws_account_id is not None:
            self._values["peer_vpc_aws_account_id"] = peer_vpc_aws_account_id
        if peer_vpc_id is not None:
            self._values["peer_vpc_id"] = peer_vpc_id
        if resource_creation_limit_policy is not None:
            self._values["resource_creation_limit_policy"] = resource_creation_limit_policy
        if runtime_configuration is not None:
            self._values["runtime_configuration"] = runtime_configuration
        if scaling_policies is not None:
            self._values["scaling_policies"] = scaling_policies
        if script_id is not None:
            self._values["script_id"] = script_id
        if server_launch_parameters is not None:
            self._values["server_launch_parameters"] = server_launch_parameters
        if server_launch_path is not None:
            self._values["server_launch_path"] = server_launch_path

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with a fleet.

        Fleet names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def anywhere_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]]:
        '''Amazon GameLift Anywhere configuration options.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-anywhereconfiguration
        '''
        result = self._values.get("anywhere_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]], result)

    @builtins.property
    def apply_capacity(self) -> typing.Optional[builtins.str]:
        '''Current resource capacity settings for managed EC2 fleets and container fleets.

        For multi-location fleets, location values might refer to a fleet's remote location or its home Region.

        *Returned by:* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ , `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ , `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-applycapacity
        '''
        result = self._values.get("apply_capacity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def build_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a build to be deployed on the new fleet.

        If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-buildid
        '''
        result = self._values.get("build_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.CertificateConfigurationProperty]]:
        '''Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet.

        Amazon GameLift uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet.

        AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition.
        .. epigraph::

           ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-certificateconfiguration
        '''
        result = self._values.get("certificate_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.CertificateConfigurationProperty]], result)

    @builtins.property
    def compute_type(self) -> typing.Optional[builtins.str]:
        '''The type of compute resource used to host your game servers.

        - ``EC2`` – The game server build is deployed to Amazon EC2 instances for cloud hosting. This is the default setting.
        - ``CONTAINER`` – Container images with your game server build and supporting software are deployed to Amazon EC2 instances for cloud hosting. With this compute type, you must specify the ``ContainerGroupsConfiguration`` parameter.
        - ``ANYWHERE`` – Game servers or container images with your game server and supporting software are deployed to compute resources that are provided and managed by you. With this compute type, you can also set the ``AnywhereConfiguration`` parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-computetype
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def container_groups_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ContainerGroupsConfigurationProperty]]:
        '''*This data type is used with the Amazon GameLift containers feature, which is currently in public preview.*.

        Configuration details for a set of container groups, for use when creating a fleet with compute type ``CONTAINER`` .

        *Used with:* ``CreateFleet``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-containergroupsconfiguration
        '''
        result = self._values.get("container_groups_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ContainerGroupsConfigurationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def desired_ec2_instances(self) -> typing.Optional[jsii.Number]:
        '''The number of EC2 instances that you want this fleet to host.

        When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-desiredec2instances
        '''
        result = self._values.get("desired_ec2_instances")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def ec2_inbound_permissions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]]:
        '''The IP address ranges and port settings that allow inbound traffic to access game server processes and other processes on this fleet.

        Set this parameter for EC2 and container fleets. You can leave this parameter empty when creating the fleet, but you must call ``UpdateFleetPortSettings`` to set it before players can connect to game sessions. As a best practice, we recommend opening ports for remote access only when you need them and closing them when you're finished. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges.

        To manage inbound access for a container fleet, set this parameter to the same port numbers that you set for the fleet's connection port range. During the life of the fleet, update this parameter to control which connection ports are open to inbound traffic.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2inboundpermissions
        '''
        result = self._values.get("ec2_inbound_permissions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]], result)

    @builtins.property
    def ec2_instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon GameLift-supported Amazon EC2 instance type to use with EC2 and container fleets.

        Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2instancetype
        '''
        result = self._values.get("ec2_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use On-Demand or Spot instances for this fleet.

        By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This fleet property can't be changed after the fleet is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-fleettype
        '''
        result = self._values.get("fleet_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for an IAM role with access permissions to other AWS services.

        Any application that runs on an instance in the fleet--including install scripts, server processes, and other processes--can use these permissions to interact with AWS resources that you own or have access to. For more information about using the role with your game server builds, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is "EC2" or "Container".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolearn
        '''
        result = self._values.get("instance_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_credentials_provider(self) -> typing.Optional[builtins.str]:
        '''Indicates that fleet instances maintain a shared credentials file for the IAM role defined in ``InstanceRoleArn`` .

        Shared credentials allow applications that are deployed with the game server executable to communicate with other AWS resources. This property is used only when the game server is integrated with the server SDK version 5.x. For more information about using shared credentials, see `Communicate with other AWS resources from your fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This attribute is used with fleets where ``ComputeType`` is "EC2" or "Container".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolecredentialsprovider
        '''
        result = self._values.get("instance_role_credentials_provider")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]]:
        '''A set of remote locations to deploy additional instances to and manage as part of the fleet.

        This parameter can only be used when creating fleets in AWS Regions that support multiple locations. You can add any Amazon GameLift-supported AWS Region as a remote location, in the form of an AWS Region code, such as ``us-west-2`` or Local Zone code. To create a fleet with instances in the home Region only, don't set this parameter.

        When using this parameter, Amazon GameLift requires you to include your home location in the request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-locations
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]], result)

    @builtins.property
    def log_paths(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) This parameter is no longer used.

        When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-logpaths
        :stability: deprecated
        '''
        result = self._values.get("log_paths")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances that are allowed in the specified fleet location.

        If this parameter is not set, the default is 1.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-maxsize
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def metric_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The name of an AWS CloudWatch metric group to add this fleet to.

        A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-metricgroups
        '''
        result = self._values.get("metric_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances that are allowed in the specified fleet location.

        If this parameter is not set, the default is 0.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-minsize
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def new_game_session_protection_policy(self) -> typing.Optional[builtins.str]:
        '''The status of termination protection for active game sessions on the fleet.

        By default, this property is set to ``NoProtection`` .

        - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event.
        - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-newgamesessionprotectionpolicy
        '''
        result = self._values.get("new_game_session_protection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_vpc_aws_account_id(self) -> typing.Optional[builtins.str]:
        '''Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the AWS account that owns the VPC.

        You can find your account ID in the AWS Management Console under account settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcawsaccountid
        '''
        result = self._values.get("peer_vpc_aws_account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def peer_vpc_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet.

        The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-peervpcid
        '''
        result = self._values.get("peer_vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_creation_limit_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ResourceCreationLimitPolicyProperty]]:
        '''A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-resourcecreationlimitpolicy
        '''
        result = self._values.get("resource_creation_limit_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ResourceCreationLimitPolicyProperty]], result)

    @builtins.property
    def runtime_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.RuntimeConfigurationProperty]]:
        '''Instructions for how to launch and maintain server processes on instances in the fleet.

        The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently.
        .. epigraph::

           The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-runtimeconfiguration
        '''
        result = self._values.get("runtime_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.RuntimeConfigurationProperty]], result)

    @builtins.property
    def scaling_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.ScalingPolicyProperty]]]]:
        '''Rule that controls how a fleet is scaled.

        Scaling policies are uniquely identified by the combination of name and fleet ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scalingpolicies
        '''
        result = self._values.get("scaling_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.ScalingPolicyProperty]]]], result)

    @builtins.property
    def script_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier for a Realtime configuration script to be deployed on fleet instances.

        You can use either the script ID or ARN. Scripts must be uploaded to Amazon GameLift prior to creating the fleet. This fleet property cannot be changed later.
        .. epigraph::

           You can't use the ``!Ref`` command to reference a script created with a CloudFormation template for the fleet property ``ScriptId`` . Instead, use ``Fn::GetAtt Script.Arn`` or ``Fn::GetAtt Script.Id`` to retrieve either of these properties as input for ``ScriptId`` . Alternatively, enter a ``ScriptId`` string manually.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-scriptid
        '''
        result = self._values.get("script_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_launch_parameters(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used but is retained for backward compatibility.

        Instead, specify server launch parameters in the RuntimeConfiguration parameter. A request must specify either a runtime configuration or values for both ServerLaunchParameters and ServerLaunchPath.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchparameters
        :stability: deprecated
        '''
        result = self._values.get("server_launch_parameters")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def server_launch_path(self) -> typing.Optional[builtins.str]:
        '''(deprecated) This parameter is no longer used.

        Instead, specify a server launch path using the RuntimeConfiguration parameter. Requests that specify a server launch path and launch parameters instead of a runtime configuration will continue to work.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-serverlaunchpath
        :stability: deprecated
        '''
        result = self._values.get("server_launch_path")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFleetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGameServerGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup",
):
    '''*This operation is used with the Amazon GameLift FleetIQ solution and game server groups.*.

    Creates a GameLift FleetIQ game server group for managing game hosting on a collection of Amazon EC2 instances for game hosting. This operation creates the game server group, creates an Auto Scaling group in your AWS account , and establishes a link between the two groups. You can view the status of your game server groups in the GameLift console. Game server group metrics and events are emitted to Amazon CloudWatch.

    Before creating a new game server group, you must have the following:

    - An Amazon EC2 launch template that specifies how to launch Amazon EC2 instances with your game server build. For more information, see `Launching an Instance from a Launch Template <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html>`_ in the *Amazon EC2 User Guide* .
    - An IAM role that extends limited access to your AWS account to allow GameLift FleetIQ to create and interact with the Auto Scaling group. For more information, see `Create IAM roles for cross-service interaction <https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-iam-permissions-roles.html>`_ in the *GameLift FleetIQ Developer Guide* .

    To create a new game server group, specify a unique group name, IAM role and Amazon EC2 launch template, and provide a list of instance types that can be used in the group. You must also set initial maximum and minimum limits on the group's instance count. You can optionally set an Auto Scaling policy with target tracking based on a GameLift FleetIQ metric.

    Once the game server group and corresponding Auto Scaling group are created, you have full access to change the Auto Scaling group's configuration as needed. Several properties that are set when creating a game server group, including maximum/minimum size and auto-scaling policy settings, must be updated directly in the Auto Scaling group. Keep in mind that some Auto Scaling group properties are periodically updated by GameLift FleetIQ as part of its balancing activities to optimize for availability and cost.

    *Learn more*

    `GameLift FleetIQ Guide <https://docs.aws.amazon.com/gamelift/latest/fleetiqguide/gsg-intro.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html
    :cloudformationResource: AWS::GameLift::GameServerGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_game_server_group = gamelift.CfnGameServerGroup(self, "MyCfnGameServerGroup",
            game_server_group_name="gameServerGroupName",
            instance_definitions=[gamelift.CfnGameServerGroup.InstanceDefinitionProperty(
                instance_type="instanceType",
        
                # the properties below are optional
                weighted_capacity="weightedCapacity"
            )],
            role_arn="roleArn",
        
            # the properties below are optional
            auto_scaling_policy=gamelift.CfnGameServerGroup.AutoScalingPolicyProperty(
                target_tracking_configuration=gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                    target_value=123
                ),
        
                # the properties below are optional
                estimated_instance_warmup=123
            ),
            balancing_strategy="balancingStrategy",
            delete_option="deleteOption",
            game_server_protection_policy="gameServerProtectionPolicy",
            launch_template=gamelift.CfnGameServerGroup.LaunchTemplateProperty(
                launch_template_id="launchTemplateId",
                launch_template_name="launchTemplateName",
                version="version"
            ),
            max_size=123,
            min_size=123,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_subnets=["vpcSubnets"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        game_server_group_name: builtins.str,
        instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.InstanceDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]]],
        role_arn: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.AutoScalingPolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        balancing_strategy: typing.Optional[builtins.str] = None,
        delete_option: typing.Optional[builtins.str] = None,
        game_server_protection_policy: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.LaunchTemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param game_server_group_name: A developer-defined identifier for the game server group. The name is unique for each Region in each AWS account.
        :param instance_definitions: The set of Amazon EC2 instance types that Amazon GameLift FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.
        :param role_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift to access your Amazon EC2 Auto Scaling groups.
        :param auto_scaling_policy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric ``"PercentUtilizedGameServers"`` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param balancing_strategy: Indicates how Amazon GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following: - ``SPOT_ONLY`` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced. - ``SPOT_PREFERRED`` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances. - ``ON_DEMAND_ONLY`` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
        :param delete_option: The type of delete to perform. To delete a game server group, specify the ``DeleteOption`` . Options include the following: - ``SAFE_DELETE`` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in ``UTILIZED`` status. - ``FORCE_DELETE`` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group. - ``RETAIN`` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.
        :param game_server_protection_policy: A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.
        :param launch_template: The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see `Creating a Launch Template for an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs. .. epigraph:: If you specify network interfaces in your launch template, you must explicitly set the property ``AssociatePublicIpAddress`` to "true". If no network interface is specified in the launch template, Amazon GameLift FleetIQ uses your account's default VPC.
        :param max_size: The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param min_size: The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param tags: A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags, respectively. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param vpc_subnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39a0d4e260fba686f866a885f9a542286a05d085037e114d8febabfdd92cfd24)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGameServerGroupProps(
            game_server_group_name=game_server_group_name,
            instance_definitions=instance_definitions,
            role_arn=role_arn,
            auto_scaling_policy=auto_scaling_policy,
            balancing_strategy=balancing_strategy,
            delete_option=delete_option,
            game_server_protection_policy=game_server_protection_policy,
            launch_template=launch_template,
            max_size=max_size,
            min_size=min_size,
            tags=tags,
            vpc_subnets=vpc_subnets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32ac0616025cd3de739c7101cea4baa4d9d85d9755bd18a18599fd247f47e000)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3a77b5aa43581e64c5c91459806a51ceb403900395eac9fb9f2cdec42c5c7fad)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAutoScalingGroupArn")
    def attr_auto_scaling_group_arn(self) -> builtins.str:
        '''A unique identifier for the auto scaling group.

        :cloudformationAttribute: AutoScalingGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAutoScalingGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGameServerGroupArn")
    def attr_game_server_group_arn(self) -> builtins.str:
        '''A unique identifier for the game server group.

        :cloudformationAttribute: GameServerGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGameServerGroupArn"))

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
    @jsii.member(jsii_name="gameServerGroupName")
    def game_server_group_name(self) -> builtins.str:
        '''A developer-defined identifier for the game server group.'''
        return typing.cast(builtins.str, jsii.get(self, "gameServerGroupName"))

    @game_server_group_name.setter
    def game_server_group_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89556427a3cb2e1aa05738182ce0459e80e576c3c25bd0cc1d7dc630a122bd67)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerGroupName", value)

    @builtins.property
    @jsii.member(jsii_name="instanceDefinitions")
    def instance_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.InstanceDefinitionProperty"]]]:
        '''The set of Amazon EC2 instance types that Amazon GameLift FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.InstanceDefinitionProperty"]]], jsii.get(self, "instanceDefinitions"))

    @instance_definitions.setter
    def instance_definitions(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.InstanceDefinitionProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__868421ea021122381c2075a524c1d4785b63637a5ae0e28ee1747043ceaf14fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceDefinitions", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift to access your Amazon EC2 Auto Scaling groups.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76aa84abc5cd589d0abb99434e1ecea33850fb0ccbb6eee11380bfa754fc482)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="autoScalingPolicy")
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.AutoScalingPolicyProperty"]]:
        '''Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.AutoScalingPolicyProperty"]], jsii.get(self, "autoScalingPolicy"))

    @auto_scaling_policy.setter
    def auto_scaling_policy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.AutoScalingPolicyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5ee0eb377684162644f965e1106f08af9e4431bca94796da59b89abc7ffd998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoScalingPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="balancingStrategy")
    def balancing_strategy(self) -> typing.Optional[builtins.str]:
        '''Indicates how Amazon GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "balancingStrategy"))

    @balancing_strategy.setter
    def balancing_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a5fc25560f0a78783f5ed8bb510e2e86e267d9629bd271a2403e866afa14e22e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "balancingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="deleteOption")
    def delete_option(self) -> typing.Optional[builtins.str]:
        '''The type of delete to perform.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteOption"))

    @delete_option.setter
    def delete_option(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a84355ef62b2fd37a277a26c39b2735a06cf204ad010f5de3744a8280e5be056)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deleteOption", value)

    @builtins.property
    @jsii.member(jsii_name="gameServerProtectionPolicy")
    def game_server_protection_policy(self) -> typing.Optional[builtins.str]:
        '''A flag that indicates whether instances in the game server group are protected from early termination.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gameServerProtectionPolicy"))

    @game_server_protection_policy.setter
    def game_server_protection_policy(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29b538c5660178a7532c29be9d3acb184e85dfbac80460c002d5f219fa429d79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameServerProtectionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="launchTemplate")
    def launch_template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.LaunchTemplateProperty"]]:
        '''The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.LaunchTemplateProperty"]], jsii.get(self, "launchTemplate"))

    @launch_template.setter
    def launch_template(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.LaunchTemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e1b30118131dd3fcdd29554603028109f41bf9f28d638ff1f26fc0de989e8b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "launchTemplate", value)

    @builtins.property
    @jsii.member(jsii_name="maxSize")
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances allowed in the Amazon EC2 Auto Scaling group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxSize"))

    @max_size.setter
    def max_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c07d732b195687bb610c12d0db39761316bbb61e6416116d630f224124000c66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxSize", value)

    @builtins.property
    @jsii.member(jsii_name="minSize")
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances allowed in the Amazon EC2 Auto Scaling group.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minSize"))

    @min_size.setter
    def min_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b7e884c21390c0adc461578e34ea9d201ce75716ffda1892218e4f39b5f6ae3e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minSize", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game server group resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0dba0594bea5d13fc9125228769f878f9679d696d511472809787acd5605b3e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSubnets")
    def vpc_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of virtual private cloud (VPC) subnets to use with instances in the game server group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSubnets"))

    @vpc_subnets.setter
    def vpc_subnets(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b4d5326a42c1fdc1afa97e1f31ad389e2aac7fbe1c4f2c6a3f614b0d23761c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSubnets", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.AutoScalingPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "target_tracking_configuration": "targetTrackingConfiguration",
            "estimated_instance_warmup": "estimatedInstanceWarmup",
        },
    )
    class AutoScalingPolicyProperty:
        def __init__(
            self,
            *,
            target_tracking_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameServerGroup.TargetTrackingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
            estimated_instance_warmup: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''*This data type is used with the GameLift FleetIQ and game server groups.*.

            Configuration settings for intelligent automatic scaling that uses target tracking. After the Auto Scaling group is created, all updates to Auto Scaling policies, including changing this policy and adding or removing other policies, is done directly on the Auto Scaling group.

            :param target_tracking_configuration: Settings for a target-based scaling policy applied to Auto Scaling group. These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric ``PercentUtilizedGameServers`` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.
            :param estimated_instance_warmup: Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift FleetIQ. Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                auto_scaling_policy_property = gamelift.CfnGameServerGroup.AutoScalingPolicyProperty(
                    target_tracking_configuration=gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                        target_value=123
                    ),
                
                    # the properties below are optional
                    estimated_instance_warmup=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e3ca9dc4f6076efea7dd9c18ae3d0d4e330ecd050951dbb0b731443e8b262e56)
                check_type(argname="argument target_tracking_configuration", value=target_tracking_configuration, expected_type=type_hints["target_tracking_configuration"])
                check_type(argname="argument estimated_instance_warmup", value=estimated_instance_warmup, expected_type=type_hints["estimated_instance_warmup"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_tracking_configuration": target_tracking_configuration,
            }
            if estimated_instance_warmup is not None:
                self._values["estimated_instance_warmup"] = estimated_instance_warmup

        @builtins.property
        def target_tracking_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.TargetTrackingConfigurationProperty"]:
            '''Settings for a target-based scaling policy applied to Auto Scaling group.

            These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric ``PercentUtilizedGameServers`` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html#cfn-gamelift-gameservergroup-autoscalingpolicy-targettrackingconfiguration
            '''
            result = self._values.get("target_tracking_configuration")
            assert result is not None, "Required property 'target_tracking_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnGameServerGroup.TargetTrackingConfigurationProperty"], result)

        @builtins.property
        def estimated_instance_warmup(self) -> typing.Optional[jsii.Number]:
            '''Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift FleetIQ.

            Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-autoscalingpolicy.html#cfn-gamelift-gameservergroup-autoscalingpolicy-estimatedinstancewarmup
            '''
            result = self._values.get("estimated_instance_warmup")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoScalingPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.InstanceDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_type": "instanceType",
            "weighted_capacity": "weightedCapacity",
        },
    )
    class InstanceDefinitionProperty:
        def __init__(
            self,
            *,
            instance_type: builtins.str,
            weighted_capacity: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*This data type is used with the Amazon GameLift FleetIQ and game server groups.*.

            An allowed instance type for a ``GameServerGroup`` . All game server groups must have at least two instance types defined for it. GameLift FleetIQ periodically evaluates each defined instance type for viability. It then updates the Auto Scaling group with the list of viable instance types.

            :param instance_type: An Amazon EC2 instance type designation.
            :param weighted_capacity: Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group. Instance weights are used by Amazon GameLift FleetIQ to calculate the instance type's cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see `Instance Weighting <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . Default value is "1".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                instance_definition_property = gamelift.CfnGameServerGroup.InstanceDefinitionProperty(
                    instance_type="instanceType",
                
                    # the properties below are optional
                    weighted_capacity="weightedCapacity"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b295ebcaf7cae28b09dfaf0a8c5a7fe40fd9a1dfa65423b6093711f0f56e28fc)
                check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
                check_type(argname="argument weighted_capacity", value=weighted_capacity, expected_type=type_hints["weighted_capacity"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_type": instance_type,
            }
            if weighted_capacity is not None:
                self._values["weighted_capacity"] = weighted_capacity

        @builtins.property
        def instance_type(self) -> builtins.str:
            '''An Amazon EC2 instance type designation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html#cfn-gamelift-gameservergroup-instancedefinition-instancetype
            '''
            result = self._values.get("instance_type")
            assert result is not None, "Required property 'instance_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def weighted_capacity(self) -> typing.Optional[builtins.str]:
            '''Instance weighting that indicates how much this instance type contributes to the total capacity of a game server group.

            Instance weights are used by Amazon GameLift FleetIQ to calculate the instance type's cost per unit hour and better identify the most cost-effective options. For detailed information on weighting instance capacity, see `Instance Weighting <https://docs.aws.amazon.com/autoscaling/ec2/userguide/asg-instance-weighting.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . Default value is "1".

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-instancedefinition.html#cfn-gamelift-gameservergroup-instancedefinition-weightedcapacity
            '''
            result = self._values.get("weighted_capacity")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InstanceDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.LaunchTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "launch_template_id": "launchTemplateId",
            "launch_template_name": "launchTemplateName",
            "version": "version",
        },
    )
    class LaunchTemplateProperty:
        def __init__(
            self,
            *,
            launch_template_id: typing.Optional[builtins.str] = None,
            launch_template_name: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''*This data type is used with the GameLift FleetIQ and game server groups.*.

            An Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in a game server group. The launch template is specified when creating a new game server group with ``GameServerGroup`` .

            :param launch_template_id: A unique identifier for an existing Amazon EC2 launch template.
            :param launch_template_name: A readable identifier for an existing Amazon EC2 launch template.
            :param version: The version of the Amazon EC2 launch template to use. If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                launch_template_property = gamelift.CfnGameServerGroup.LaunchTemplateProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__25060a9b2c2773d45ef64eabb5fbdc70d6c95644145351fecb4e3d70bd06f5e2)
                check_type(argname="argument launch_template_id", value=launch_template_id, expected_type=type_hints["launch_template_id"])
                check_type(argname="argument launch_template_name", value=launch_template_name, expected_type=type_hints["launch_template_name"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if launch_template_id is not None:
                self._values["launch_template_id"] = launch_template_id
            if launch_template_name is not None:
                self._values["launch_template_name"] = launch_template_name
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def launch_template_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for an existing Amazon EC2 launch template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-launchtemplateid
            '''
            result = self._values.get("launch_template_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def launch_template_name(self) -> typing.Optional[builtins.str]:
            '''A readable identifier for an existing Amazon EC2 launch template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-launchtemplatename
            '''
            result = self._values.get("launch_template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the Amazon EC2 launch template to use.

            If no version is specified, the default version will be used. With Amazon EC2, you can specify a default version for a launch template. If none is set, the default is the first version created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-launchtemplate.html#cfn-gamelift-gameservergroup-launchtemplate-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LaunchTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"target_value": "targetValue"},
    )
    class TargetTrackingConfigurationProperty:
        def __init__(self, *, target_value: jsii.Number) -> None:
            '''*This data type is used with the Amazon GameLift FleetIQ and game server groups.*.

            Settings for a target-based scaling policy as part of a ``GameServerGroupAutoScalingPolicy`` . These settings are used to create a target-based policy that tracks the GameLift FleetIQ metric ``"PercentUtilizedGameServers"`` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

            :param target_value: Desired value to use with a game server group target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                target_tracking_configuration_property = gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                    target_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef13423f0408e9300989065f2e1f7a323aeaaef1367e95591fe66bbfc152a818)
                check_type(argname="argument target_value", value=target_value, expected_type=type_hints["target_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_value": target_value,
            }

        @builtins.property
        def target_value(self) -> jsii.Number:
            '''Desired value to use with a game server group target-based scaling policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gameservergroup-targettrackingconfiguration.html#cfn-gamelift-gameservergroup-targettrackingconfiguration-targetvalue
            '''
            result = self._values.get("target_value")
            assert result is not None, "Required property 'target_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TargetTrackingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameServerGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "game_server_group_name": "gameServerGroupName",
        "instance_definitions": "instanceDefinitions",
        "role_arn": "roleArn",
        "auto_scaling_policy": "autoScalingPolicy",
        "balancing_strategy": "balancingStrategy",
        "delete_option": "deleteOption",
        "game_server_protection_policy": "gameServerProtectionPolicy",
        "launch_template": "launchTemplate",
        "max_size": "maxSize",
        "min_size": "minSize",
        "tags": "tags",
        "vpc_subnets": "vpcSubnets",
    },
)
class CfnGameServerGroupProps:
    def __init__(
        self,
        *,
        game_server_group_name: builtins.str,
        instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.InstanceDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
        role_arn: builtins.str,
        auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        balancing_strategy: typing.Optional[builtins.str] = None,
        delete_option: typing.Optional[builtins.str] = None,
        game_server_protection_policy: typing.Optional[builtins.str] = None,
        launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.LaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_size: typing.Optional[jsii.Number] = None,
        min_size: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnGameServerGroup``.

        :param game_server_group_name: A developer-defined identifier for the game server group. The name is unique for each Region in each AWS account.
        :param instance_definitions: The set of Amazon EC2 instance types that Amazon GameLift FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.
        :param role_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift to access your Amazon EC2 Auto Scaling groups.
        :param auto_scaling_policy: Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting. The scaling policy uses the metric ``"PercentUtilizedGameServers"`` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param balancing_strategy: Indicates how Amazon GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group. Method options include the following: - ``SPOT_ONLY`` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced. - ``SPOT_PREFERRED`` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances. - ``ON_DEMAND_ONLY`` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.
        :param delete_option: The type of delete to perform. To delete a game server group, specify the ``DeleteOption`` . Options include the following: - ``SAFE_DELETE`` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in ``UTILIZED`` status. - ``FORCE_DELETE`` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group. - ``RETAIN`` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.
        :param game_server_protection_policy: A flag that indicates whether instances in the game server group are protected from early termination. Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.
        :param launch_template: The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group. You can specify the template using either the template name or ID. For help with creating a launch template, see `Creating a Launch Template for an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs. .. epigraph:: If you specify network interfaces in your launch template, you must explicitly set the property ``AssociatePublicIpAddress`` to "true". If no network interface is specified in the launch template, Amazon GameLift FleetIQ uses your account's default VPC.
        :param max_size: The maximum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param min_size: The minimum number of instances allowed in the Amazon EC2 Auto Scaling group. During automatic scaling events, Amazon GameLift FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        :param tags: A list of labels to assign to the new game server group resource. Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags, respectively. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param vpc_subnets: A list of virtual private cloud (VPC) subnets to use with instances in the game server group. By default, all Amazon GameLift FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_game_server_group_props = gamelift.CfnGameServerGroupProps(
                game_server_group_name="gameServerGroupName",
                instance_definitions=[gamelift.CfnGameServerGroup.InstanceDefinitionProperty(
                    instance_type="instanceType",
            
                    # the properties below are optional
                    weighted_capacity="weightedCapacity"
                )],
                role_arn="roleArn",
            
                # the properties below are optional
                auto_scaling_policy=gamelift.CfnGameServerGroup.AutoScalingPolicyProperty(
                    target_tracking_configuration=gamelift.CfnGameServerGroup.TargetTrackingConfigurationProperty(
                        target_value=123
                    ),
            
                    # the properties below are optional
                    estimated_instance_warmup=123
                ),
                balancing_strategy="balancingStrategy",
                delete_option="deleteOption",
                game_server_protection_policy="gameServerProtectionPolicy",
                launch_template=gamelift.CfnGameServerGroup.LaunchTemplateProperty(
                    launch_template_id="launchTemplateId",
                    launch_template_name="launchTemplateName",
                    version="version"
                ),
                max_size=123,
                min_size=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_subnets=["vpcSubnets"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb2b330cbc0b2bd24b542707e03f7de3d6d3afa7d8fa0efaac64771d13b95db1)
            check_type(argname="argument game_server_group_name", value=game_server_group_name, expected_type=type_hints["game_server_group_name"])
            check_type(argname="argument instance_definitions", value=instance_definitions, expected_type=type_hints["instance_definitions"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument auto_scaling_policy", value=auto_scaling_policy, expected_type=type_hints["auto_scaling_policy"])
            check_type(argname="argument balancing_strategy", value=balancing_strategy, expected_type=type_hints["balancing_strategy"])
            check_type(argname="argument delete_option", value=delete_option, expected_type=type_hints["delete_option"])
            check_type(argname="argument game_server_protection_policy", value=game_server_protection_policy, expected_type=type_hints["game_server_protection_policy"])
            check_type(argname="argument launch_template", value=launch_template, expected_type=type_hints["launch_template"])
            check_type(argname="argument max_size", value=max_size, expected_type=type_hints["max_size"])
            check_type(argname="argument min_size", value=min_size, expected_type=type_hints["min_size"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_subnets", value=vpc_subnets, expected_type=type_hints["vpc_subnets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "game_server_group_name": game_server_group_name,
            "instance_definitions": instance_definitions,
            "role_arn": role_arn,
        }
        if auto_scaling_policy is not None:
            self._values["auto_scaling_policy"] = auto_scaling_policy
        if balancing_strategy is not None:
            self._values["balancing_strategy"] = balancing_strategy
        if delete_option is not None:
            self._values["delete_option"] = delete_option
        if game_server_protection_policy is not None:
            self._values["game_server_protection_policy"] = game_server_protection_policy
        if launch_template is not None:
            self._values["launch_template"] = launch_template
        if max_size is not None:
            self._values["max_size"] = max_size
        if min_size is not None:
            self._values["min_size"] = min_size
        if tags is not None:
            self._values["tags"] = tags
        if vpc_subnets is not None:
            self._values["vpc_subnets"] = vpc_subnets

    @builtins.property
    def game_server_group_name(self) -> builtins.str:
        '''A developer-defined identifier for the game server group.

        The name is unique for each Region in each AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameservergroupname
        '''
        result = self._values.get("game_server_group_name")
        assert result is not None, "Required property 'game_server_group_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def instance_definitions(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.InstanceDefinitionProperty]]]:
        '''The set of Amazon EC2 instance types that Amazon GameLift FleetIQ can use when balancing and automatically scaling instances in the corresponding Auto Scaling group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-instancedefinitions
        '''
        result = self._values.get("instance_definitions")
        assert result is not None, "Required property 'instance_definitions' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.InstanceDefinitionProperty]]], result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift to access your Amazon EC2 Auto Scaling groups.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def auto_scaling_policy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.AutoScalingPolicyProperty]]:
        '''Configuration settings to define a scaling policy for the Auto Scaling group that is optimized for game hosting.

        The scaling policy uses the metric ``"PercentUtilizedGameServers"`` to maintain a buffer of idle game servers that can immediately accommodate new games and players. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-autoscalingpolicy
        '''
        result = self._values.get("auto_scaling_policy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.AutoScalingPolicyProperty]], result)

    @builtins.property
    def balancing_strategy(self) -> typing.Optional[builtins.str]:
        '''Indicates how Amazon GameLift FleetIQ balances the use of Spot Instances and On-Demand Instances in the game server group.

        Method options include the following:

        - ``SPOT_ONLY`` - Only Spot Instances are used in the game server group. If Spot Instances are unavailable or not viable for game hosting, the game server group provides no hosting capacity until Spot Instances can again be used. Until then, no new instances are started, and the existing nonviable Spot Instances are terminated (after current gameplay ends) and are not replaced.
        - ``SPOT_PREFERRED`` - (default value) Spot Instances are used whenever available in the game server group. If Spot Instances are unavailable, the game server group continues to provide hosting capacity by falling back to On-Demand Instances. Existing nonviable Spot Instances are terminated (after current gameplay ends) and are replaced with new On-Demand Instances.
        - ``ON_DEMAND_ONLY`` - Only On-Demand Instances are used in the game server group. No Spot Instances are used, even when available, while this balancing strategy is in force.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-balancingstrategy
        '''
        result = self._values.get("balancing_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_option(self) -> typing.Optional[builtins.str]:
        '''The type of delete to perform.

        To delete a game server group, specify the ``DeleteOption`` . Options include the following:

        - ``SAFE_DELETE`` – (default) Terminates the game server group and Amazon EC2 Auto Scaling group only when it has no game servers that are in ``UTILIZED`` status.
        - ``FORCE_DELETE`` – Terminates the game server group, including all active game servers regardless of their utilization status, and the Amazon EC2 Auto Scaling group.
        - ``RETAIN`` – Does a safe delete of the game server group but retains the Amazon EC2 Auto Scaling group as is.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-deleteoption
        '''
        result = self._values.get("delete_option")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_server_protection_policy(self) -> typing.Optional[builtins.str]:
        '''A flag that indicates whether instances in the game server group are protected from early termination.

        Unprotected instances that have active game servers running might be terminated during a scale-down event, causing players to be dropped from the game. Protected instances cannot be terminated while there are active game servers running except in the event of a forced game server group deletion (see ). An exception to this is with Spot Instances, which can be terminated by AWS regardless of protection status.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-gameserverprotectionpolicy
        '''
        result = self._values.get("game_server_protection_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def launch_template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.LaunchTemplateProperty]]:
        '''The Amazon EC2 launch template that contains configuration settings and game server code to be deployed to all instances in the game server group.

        You can specify the template using either the template name or ID. For help with creating a launch template, see `Creating a Launch Template for an Auto Scaling Group <https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-launch-template.html>`_ in the *Amazon Elastic Compute Cloud Auto Scaling User Guide* . After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.
        .. epigraph::

           If you specify network interfaces in your launch template, you must explicitly set the property ``AssociatePublicIpAddress`` to "true". If no network interface is specified in the launch template, Amazon GameLift FleetIQ uses your account's default VPC.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-launchtemplate
        '''
        result = self._values.get("launch_template")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.LaunchTemplateProperty]], result)

    @builtins.property
    def max_size(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of instances allowed in the Amazon EC2 Auto Scaling group.

        During automatic scaling events, Amazon GameLift FleetIQ and EC2 do not scale up the group above this maximum. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-maxsize
        '''
        result = self._values.get("max_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_size(self) -> typing.Optional[jsii.Number]:
        '''The minimum number of instances allowed in the Amazon EC2 Auto Scaling group.

        During automatic scaling events, Amazon GameLift FleetIQ and Amazon EC2 do not scale down the group below this minimum. In production, this value should be set to at least 1. After the Auto Scaling group is created, update this value directly in the Auto Scaling group using the AWS console or APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-minsize
        '''
        result = self._values.get("min_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game server group resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources is useful for resource management, access management, and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags, respectively. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_subnets(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of virtual private cloud (VPC) subnets to use with instances in the game server group.

        By default, all Amazon GameLift FleetIQ-supported Availability Zones are used. You can use this parameter to specify VPCs that you've set up. This property cannot be updated after the game server group is created, and the corresponding Auto Scaling group will always use the property value that is set with this request, even if the Auto Scaling group is updated directly.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gameservergroup.html#cfn-gamelift-gameservergroup-vpcsubnets
        '''
        result = self._values.get("vpc_subnets")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGameServerGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnGameSessionQueue(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue",
):
    '''The ``AWS::GameLift::GameSessionQueue`` resource creates a placement queue that processes requests for new game sessions.

    A queue uses FleetIQ algorithms to determine the best placement locations and find an available game server, then prompts the game server to start a new game session. Queues can have destinations (GameLift fleets or aliases), which determine where the queue can place new game sessions. A queue can have destinations with varied fleet type (Spot and On-Demand), instance type, and AWS Region .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
    :cloudformationResource: AWS::GameLift::GameSessionQueue
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_game_session_queue = gamelift.CfnGameSessionQueue(self, "MyCfnGameSessionQueue",
            name="name",
        
            # the properties below are optional
            custom_event_data="customEventData",
            destinations=[gamelift.CfnGameSessionQueue.DestinationProperty(
                destination_arn="destinationArn"
            )],
            filter_configuration=gamelift.CfnGameSessionQueue.FilterConfigurationProperty(
                allowed_locations=["allowedLocations"]
            ),
            notification_target="notificationTarget",
            player_latency_policies=[gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty(
                maximum_individual_player_latency_milliseconds=123,
                policy_duration_seconds=123
            )],
            priority_configuration=gamelift.CfnGameSessionQueue.PriorityConfigurationProperty(
                location_order=["locationOrder"],
                priority_order=["priorityOrder"]
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            timeout_in_seconds=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        custom_event_data: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.DestinationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.FilterConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.PlayerLatencyPolicyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGameSessionQueue.PriorityConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
        :param custom_event_data: Information to be added to all events that are related to this game session queue.
        :param destinations: A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.
        :param filter_configuration: A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as ``us-west-2`` . If this parameter is not set, game sessions can be placed in any queue location.
        :param notification_target: An SNS topic ARN that is set up to receive game session placement notifications. See `Setting up notifications for game session placement <https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html>`_ .
        :param player_latency_policies: A set of policies that act as a sliding cap on player latency. FleetIQ works to deliver low latency for most players in a game session. These policies ensure that no individual player can be placed into a game with unreasonably high latency. Use multiple policies to gradually relax latency requirements a step at a time. Multiple policies are applied based on their maximum allowed latency, starting with the lowest value.
        :param priority_configuration: Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.
        :param tags: A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param timeout_in_seconds: The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status. By default, this property is set to ``600`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2435e37790a5987d49478948c0c1ac36c9e463fa29441c46ba0aa4d567f2c585)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGameSessionQueueProps(
            name=name,
            custom_event_data=custom_event_data,
            destinations=destinations,
            filter_configuration=filter_configuration,
            notification_target=notification_target,
            player_latency_policies=player_latency_policies,
            priority_configuration=priority_configuration,
            tags=tags,
            timeout_in_seconds=timeout_in_seconds,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cc05027a8472775374b6846f6c9ab499cc41f64fa8ed31ccbfd79e142b8b76d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b257e875617af0371cc9d2c1574fb2ba9c0e4ecbacf958d56eabd8a77d1fa023)
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
        '''The unique Amazon Resource Name (ARN) for the ``GameSessionQueue`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''A descriptive label that is associated with a game session queue.

        Names are unique within each Region.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with game session queue.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac381d2dd8ded0682b62f79246a99597b2aca0600afaa30c9f48b5f1411bbfa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="customEventData")
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to be added to all events that are related to this game session queue.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEventData"))

    @custom_event_data.setter
    def custom_event_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d8260843224b7180260627c762aaa0ae5afbcd912f5da71a3c576430e069f9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEventData", value)

    @builtins.property
    @jsii.member(jsii_name="destinations")
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.DestinationProperty"]]]]:
        '''A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.DestinationProperty"]]]], jsii.get(self, "destinations"))

    @destinations.setter
    def destinations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.DestinationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f656db0c32504c821ba5c5d5067bac317db7def96a39500c5847a853576e95ec)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinations", value)

    @builtins.property
    @jsii.member(jsii_name="filterConfiguration")
    def filter_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.FilterConfigurationProperty"]]:
        '''A list of locations where a queue is allowed to place new game sessions.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.FilterConfigurationProperty"]], jsii.get(self, "filterConfiguration"))

    @filter_configuration.setter
    def filter_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.FilterConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e5b9b16ae8732de19b82da87c71cb00a9d06d7a37c8d217314158c063bf0f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTarget")
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive game session placement notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTarget"))

    @notification_target.setter
    def notification_target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f838580d46a0a1a08c09d8b8b17de066bfb74896289f61432e755d32429e2a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTarget", value)

    @builtins.property
    @jsii.member(jsii_name="playerLatencyPolicies")
    def player_latency_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]]:
        '''A set of policies that act as a sliding cap on player latency.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]], jsii.get(self, "playerLatencyPolicies"))

    @player_latency_policies.setter
    def player_latency_policies(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PlayerLatencyPolicyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3da0f541db3f4dba488790dc678e2dd0872a5271bf05bb0ddcb181884f5dfb80)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "playerLatencyPolicies", value)

    @builtins.property
    @jsii.member(jsii_name="priorityConfiguration")
    def priority_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PriorityConfigurationProperty"]]:
        '''Custom settings to use when prioritizing destinations and locations for game session placements.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PriorityConfigurationProperty"]], jsii.get(self, "priorityConfiguration"))

    @priority_configuration.setter
    def priority_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnGameSessionQueue.PriorityConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__622dc07e672d46f719db763d6bf2dec499f84a17b72186d593df03f3fcb1ae7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priorityConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game session queue resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3a8c431c366d3fa711cfb42cebf2d1647b8f2a1a5e129b5536c91cdf0135eb8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInSeconds")
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The maximum time, in seconds, that a new game session placement request remains in the queue.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInSeconds"))

    @timeout_in_seconds.setter
    def timeout_in_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ad24ec0156a0a24d8fe08ecf8470df28f9f1501a3ab442e887e2d1c5ef03df4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInSeconds", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                destination_property = gamelift.CfnGameSessionQueue.DestinationProperty(
                    destination_arn="destinationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9d1ad7f562ade1312178a63d9196a21119d0e6500b9d651931481a59d709d462)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-destination.html#cfn-gamelift-gamesessionqueue-destination-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.FilterConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allowed_locations": "allowedLocations"},
    )
    class FilterConfigurationProperty:
        def __init__(
            self,
            *,
            allowed_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A list of fleet locations where a game session queue can place new game sessions.

            You can use a filter to temporarily turn off placements for specific locations. For queues that have multi-location fleets, you can use a filter configuration allow placement with some, but not all of these locations.

            :param allowed_locations: A list of locations to allow game session placement in, in the form of AWS Region codes such as ``us-west-2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                filter_configuration_property = gamelift.CfnGameSessionQueue.FilterConfigurationProperty(
                    allowed_locations=["allowedLocations"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a18c067b373a2989add73f26fd5a7da221d485dae82bf0842dcedf8017b6ad5f)
                check_type(argname="argument allowed_locations", value=allowed_locations, expected_type=type_hints["allowed_locations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allowed_locations is not None:
                self._values["allowed_locations"] = allowed_locations

        @builtins.property
        def allowed_locations(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of locations to allow game session placement in, in the form of AWS Region codes such as ``us-west-2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-filterconfiguration.html#cfn-gamelift-gamesessionqueue-filterconfiguration-allowedlocations
            '''
            result = self._values.get("allowed_locations")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.GameSessionQueueDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn"},
    )
    class GameSessionQueueDestinationProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A fleet or alias designated in a game session queue.

            Queues fulfill requests for new game sessions by placing a new game session on any of the queue's destinations.

            :param destination_arn: The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                game_session_queue_destination_property = gamelift.CfnGameSessionQueue.GameSessionQueueDestinationProperty(
                    destination_arn="destinationArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__682a2ca85600f7cf3e8fc279fa7f5c2ecab05f65cc96301b5afab09b2da5c684)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias.

            ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-gamesessionqueuedestination.html#cfn-gamelift-gamesessionqueue-gamesessionqueuedestination-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GameSessionQueueDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "maximum_individual_player_latency_milliseconds": "maximumIndividualPlayerLatencyMilliseconds",
            "policy_duration_seconds": "policyDurationSeconds",
        },
    )
    class PlayerLatencyPolicyProperty:
        def __init__(
            self,
            *,
            maximum_individual_player_latency_milliseconds: typing.Optional[jsii.Number] = None,
            policy_duration_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The queue setting that determines the highest latency allowed for individual players when placing a game session.

            When a latency policy is in force, a game session cannot be placed with any fleet in a Region where a player reports latency higher than the cap. Latency policies are only enforced when the placement request contains player latency information.

            :param maximum_individual_player_latency_milliseconds: The maximum latency value that is allowed for any player, in milliseconds. All policies must have a value set for this property.
            :param policy_duration_seconds: The length of time, in seconds, that the policy is enforced while placing a new game session. A null value for this property means that the policy is enforced until the queue times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                player_latency_policy_property = gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty(
                    maximum_individual_player_latency_milliseconds=123,
                    policy_duration_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7a9bd74ee679564c60f66c08f4f2d7739a8abfa4c61e93feedbd8457081f585)
                check_type(argname="argument maximum_individual_player_latency_milliseconds", value=maximum_individual_player_latency_milliseconds, expected_type=type_hints["maximum_individual_player_latency_milliseconds"])
                check_type(argname="argument policy_duration_seconds", value=policy_duration_seconds, expected_type=type_hints["policy_duration_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if maximum_individual_player_latency_milliseconds is not None:
                self._values["maximum_individual_player_latency_milliseconds"] = maximum_individual_player_latency_milliseconds
            if policy_duration_seconds is not None:
                self._values["policy_duration_seconds"] = policy_duration_seconds

        @builtins.property
        def maximum_individual_player_latency_milliseconds(
            self,
        ) -> typing.Optional[jsii.Number]:
            '''The maximum latency value that is allowed for any player, in milliseconds.

            All policies must have a value set for this property.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-maximumindividualplayerlatencymilliseconds
            '''
            result = self._values.get("maximum_individual_player_latency_milliseconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def policy_duration_seconds(self) -> typing.Optional[jsii.Number]:
            '''The length of time, in seconds, that the policy is enforced while placing a new game session.

            A null value for this property means that the policy is enforced until the queue times out.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-playerlatencypolicy.html#cfn-gamelift-gamesessionqueue-playerlatencypolicy-policydurationseconds
            '''
            result = self._values.get("policy_duration_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PlayerLatencyPolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueue.PriorityConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "location_order": "locationOrder",
            "priority_order": "priorityOrder",
        },
    )
    class PriorityConfigurationProperty:
        def __init__(
            self,
            *,
            location_order: typing.Optional[typing.Sequence[builtins.str]] = None,
            priority_order: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Custom prioritization settings for use by a game session queue when placing new game sessions with available game servers.

            When defined, this configuration replaces the default FleetIQ prioritization process, which is as follows:

            - If player latency data is included in a game session request, destinations and locations are prioritized first based on lowest average latency (1), then on lowest hosting cost (2), then on destination list order (3), and finally on location (alphabetical) (4). This approach ensures that the queue's top priority is to place game sessions where average player latency is lowest, and--if latency is the same--where the hosting cost is less, etc.
            - If player latency data is not included, destinations and locations are prioritized first on destination list order (1), and then on location (alphabetical) (2). This approach ensures that the queue's top priority is to place game sessions on the first destination fleet listed. If that fleet has multiple locations, the game session is placed on the first location (when listed alphabetically).

            Changing the priority order will affect how game sessions are placed.

            :param location_order: The prioritization order to use for fleet locations, when the ``PriorityOrder`` property includes ``LOCATION`` . Locations are identified by AWS Region codes such as ``us-west-2`` . Each location can only be listed once.
            :param priority_order: The recommended sequence to use when prioritizing where to place new game sessions. Each type can only be listed once. - ``LATENCY`` -- FleetIQ prioritizes locations where the average player latency (provided in each game session request) is lowest. - ``COST`` -- FleetIQ prioritizes destinations with the lowest current hosting costs. Cost is evaluated based on the location, instance type, and fleet type (Spot or On-Demand) for each destination in the queue. - ``DESTINATION`` -- FleetIQ prioritizes based on the order that destinations are listed in the queue configuration. - ``LOCATION`` -- FleetIQ prioritizes based on the provided order of locations, as defined in ``LocationOrder`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                priority_configuration_property = gamelift.CfnGameSessionQueue.PriorityConfigurationProperty(
                    location_order=["locationOrder"],
                    priority_order=["priorityOrder"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bffce6e10d5ec1968a817a7df177891e44b6ec986ec424c92d4e71dd599b36ac)
                check_type(argname="argument location_order", value=location_order, expected_type=type_hints["location_order"])
                check_type(argname="argument priority_order", value=priority_order, expected_type=type_hints["priority_order"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if location_order is not None:
                self._values["location_order"] = location_order
            if priority_order is not None:
                self._values["priority_order"] = priority_order

        @builtins.property
        def location_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The prioritization order to use for fleet locations, when the ``PriorityOrder`` property includes ``LOCATION`` .

            Locations are identified by AWS Region codes such as ``us-west-2`` . Each location can only be listed once.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html#cfn-gamelift-gamesessionqueue-priorityconfiguration-locationorder
            '''
            result = self._values.get("location_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def priority_order(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The recommended sequence to use when prioritizing where to place new game sessions.

            Each type can only be listed once.

            - ``LATENCY`` -- FleetIQ prioritizes locations where the average player latency (provided in each game session request) is lowest.
            - ``COST`` -- FleetIQ prioritizes destinations with the lowest current hosting costs. Cost is evaluated based on the location, instance type, and fleet type (Spot or On-Demand) for each destination in the queue.
            - ``DESTINATION`` -- FleetIQ prioritizes based on the order that destinations are listed in the queue configuration.
            - ``LOCATION`` -- FleetIQ prioritizes based on the provided order of locations, as defined in ``LocationOrder`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-gamesessionqueue-priorityconfiguration.html#cfn-gamelift-gamesessionqueue-priorityconfiguration-priorityorder
            '''
            result = self._values.get("priority_order")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PriorityConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnGameSessionQueueProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "custom_event_data": "customEventData",
        "destinations": "destinations",
        "filter_configuration": "filterConfiguration",
        "notification_target": "notificationTarget",
        "player_latency_policies": "playerLatencyPolicies",
        "priority_configuration": "priorityConfiguration",
        "tags": "tags",
        "timeout_in_seconds": "timeoutInSeconds",
    },
)
class CfnGameSessionQueueProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        custom_event_data: typing.Optional[builtins.str] = None,
        destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PlayerLatencyPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PriorityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        timeout_in_seconds: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnGameSessionQueue``.

        :param name: A descriptive label that is associated with game session queue. Queue names must be unique within each Region.
        :param custom_event_data: Information to be added to all events that are related to this game session queue.
        :param destinations: A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue. Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.
        :param filter_configuration: A list of locations where a queue is allowed to place new game sessions. Locations are specified in the form of AWS Region codes, such as ``us-west-2`` . If this parameter is not set, game sessions can be placed in any queue location.
        :param notification_target: An SNS topic ARN that is set up to receive game session placement notifications. See `Setting up notifications for game session placement <https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html>`_ .
        :param player_latency_policies: A set of policies that act as a sliding cap on player latency. FleetIQ works to deliver low latency for most players in a game session. These policies ensure that no individual player can be placed into a game with unreasonably high latency. Use multiple policies to gradually relax latency requirements a step at a time. Multiple policies are applied based on their maximum allowed latency, starting with the lowest value.
        :param priority_configuration: Custom settings to use when prioritizing destinations and locations for game session placements. This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.
        :param tags: A list of labels to assign to the new game session queue resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param timeout_in_seconds: The maximum time, in seconds, that a new game session placement request remains in the queue. When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status. By default, this property is set to ``600`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_game_session_queue_props = gamelift.CfnGameSessionQueueProps(
                name="name",
            
                # the properties below are optional
                custom_event_data="customEventData",
                destinations=[gamelift.CfnGameSessionQueue.DestinationProperty(
                    destination_arn="destinationArn"
                )],
                filter_configuration=gamelift.CfnGameSessionQueue.FilterConfigurationProperty(
                    allowed_locations=["allowedLocations"]
                ),
                notification_target="notificationTarget",
                player_latency_policies=[gamelift.CfnGameSessionQueue.PlayerLatencyPolicyProperty(
                    maximum_individual_player_latency_milliseconds=123,
                    policy_duration_seconds=123
                )],
                priority_configuration=gamelift.CfnGameSessionQueue.PriorityConfigurationProperty(
                    location_order=["locationOrder"],
                    priority_order=["priorityOrder"]
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                timeout_in_seconds=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b18cdd98f5e3e7424d6d930e416c9690c2e3cdcc56ac70f4688a8984ea0e8b7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument custom_event_data", value=custom_event_data, expected_type=type_hints["custom_event_data"])
            check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
            check_type(argname="argument filter_configuration", value=filter_configuration, expected_type=type_hints["filter_configuration"])
            check_type(argname="argument notification_target", value=notification_target, expected_type=type_hints["notification_target"])
            check_type(argname="argument player_latency_policies", value=player_latency_policies, expected_type=type_hints["player_latency_policies"])
            check_type(argname="argument priority_configuration", value=priority_configuration, expected_type=type_hints["priority_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_in_seconds", value=timeout_in_seconds, expected_type=type_hints["timeout_in_seconds"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if custom_event_data is not None:
            self._values["custom_event_data"] = custom_event_data
        if destinations is not None:
            self._values["destinations"] = destinations
        if filter_configuration is not None:
            self._values["filter_configuration"] = filter_configuration
        if notification_target is not None:
            self._values["notification_target"] = notification_target
        if player_latency_policies is not None:
            self._values["player_latency_policies"] = player_latency_policies
        if priority_configuration is not None:
            self._values["priority_configuration"] = priority_configuration
        if tags is not None:
            self._values["tags"] = tags
        if timeout_in_seconds is not None:
            self._values["timeout_in_seconds"] = timeout_in_seconds

    @builtins.property
    def name(self) -> builtins.str:
        '''A descriptive label that is associated with game session queue.

        Queue names must be unique within each Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to be added to all events that are related to this game session queue.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-customeventdata
        '''
        result = self._values.get("custom_event_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destinations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.DestinationProperty]]]]:
        '''A list of fleets and/or fleet aliases that can be used to fulfill game session placement requests in the queue.

        Destinations are identified by either a fleet ARN or a fleet alias ARN, and are listed in order of placement preference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-destinations
        '''
        result = self._values.get("destinations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.DestinationProperty]]]], result)

    @builtins.property
    def filter_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.FilterConfigurationProperty]]:
        '''A list of locations where a queue is allowed to place new game sessions.

        Locations are specified in the form of AWS Region codes, such as ``us-west-2`` . If this parameter is not set, game sessions can be placed in any queue location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-filterconfiguration
        '''
        result = self._values.get("filter_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.FilterConfigurationProperty]], result)

    @builtins.property
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive game session placement notifications.

        See `Setting up notifications for game session placement <https://docs.aws.amazon.com/gamelift/latest/developerguide/queue-notification.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-notificationtarget
        '''
        result = self._values.get("notification_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def player_latency_policies(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PlayerLatencyPolicyProperty]]]]:
        '''A set of policies that act as a sliding cap on player latency.

        FleetIQ works to deliver low latency for most players in a game session. These policies ensure that no individual player can be placed into a game with unreasonably high latency. Use multiple policies to gradually relax latency requirements a step at a time. Multiple policies are applied based on their maximum allowed latency, starting with the lowest value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-playerlatencypolicies
        '''
        result = self._values.get("player_latency_policies")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PlayerLatencyPolicyProperty]]]], result)

    @builtins.property
    def priority_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PriorityConfigurationProperty]]:
        '''Custom settings to use when prioritizing destinations and locations for game session placements.

        This configuration replaces the FleetIQ default prioritization process. Priority types that are not explicitly named will be automatically applied at the end of the prioritization process.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-priorityconfiguration
        '''
        result = self._values.get("priority_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PriorityConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new game session queue resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def timeout_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The maximum time, in seconds, that a new game session placement request remains in the queue.

        When a request exceeds this time, the game session placement changes to a ``TIMED_OUT`` status. By default, this property is set to ``600`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-gamesessionqueue.html#cfn-gamelift-gamesessionqueue-timeoutinseconds
        '''
        result = self._values.get("timeout_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGameSessionQueueProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnLocation(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnLocation",
):
    '''The AWS::GameLift::Location resource creates a custom location for use in an Anywhere fleet.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html
    :cloudformationResource: AWS::GameLift::Location
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_location = gamelift.CfnLocation(self, "MyCfnLocation",
            location_name="locationName",
        
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
        location_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param location_name: A descriptive name for the custom location.
        :param tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Rareference* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__404fc5857cf63bdcf757784b5c810e73ce1c99d8d82c264eec7a145724580816)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLocationProps(location_name=location_name, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d95943640733fe4e543a0c2a9e0a647a118d84274c6945f59f0598a9585e4a4b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__a18532e89ee9aa9c91c15cc19d2c9f2345325702005b9a2708e43204329266ae)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrLocationArn")
    def attr_location_arn(self) -> builtins.str:
        '''A unique identifier for the custom location.

        For example, ``arn:aws:gamelift:[region]::location/location-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`` .

        :cloudformationAttribute: LocationArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrLocationArn"))

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
    @jsii.member(jsii_name="locationName")
    def location_name(self) -> builtins.str:
        '''A descriptive name for the custom location.'''
        return typing.cast(builtins.str, jsii.get(self, "locationName"))

    @location_name.setter
    def location_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f9bf4f89ef7693448c9209f894d6900bab55884642fc136222c211e82f3015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locationName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking configuration resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db22dc038d314307a9d7182d88d8959bd024bf2feff9aee7f03deba1df46ca5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnLocationProps",
    jsii_struct_bases=[],
    name_mapping={"location_name": "locationName", "tags": "tags"},
)
class CfnLocationProps:
    def __init__(
        self,
        *,
        location_name: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnLocation``.

        :param location_name: A descriptive name for the custom location.
        :param tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Rareference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_location_props = gamelift.CfnLocationProps(
                location_name="locationName",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ffffd954dd9a648cdd22ea8069e64a916e69b5690bde3de5bb865f1a555e5d)
            check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location_name": location_name,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def location_name(self) -> builtins.str:
        '''A descriptive name for the custom location.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-locationname
        '''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking configuration resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Rareference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLocationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMatchmakingConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingConfiguration",
):
    '''The ``AWS::GameLift::MatchmakingConfiguration`` resource defines a new matchmaking configuration for use with FlexMatch.

    Whether you're using FlexMatch with GameLift hosting or as a standalone matchmaking service, the matchmaking configuration sets out rules for matching players and forming teams. If you're using GameLift hosting, it also defines how to start game sessions for each match. Your matchmaking system can use multiple configurations to handle different game scenarios. All matchmaking requests identify the matchmaking configuration to use and provide player attributes that are consistent with that configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
    :cloudformationResource: AWS::GameLift::MatchmakingConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_matchmaking_configuration = gamelift.CfnMatchmakingConfiguration(self, "MyCfnMatchmakingConfiguration",
            acceptance_required=False,
            name="name",
            request_timeout_seconds=123,
            rule_set_name="ruleSetName",
        
            # the properties below are optional
            acceptance_timeout_seconds=123,
            additional_player_count=123,
            backfill_mode="backfillMode",
            creation_time="creationTime",
            custom_event_data="customEventData",
            description="description",
            flex_match_mode="flexMatchMode",
            game_properties=[gamelift.CfnMatchmakingConfiguration.GamePropertyProperty(
                key="key",
                value="value"
            )],
            game_session_data="gameSessionData",
            game_session_queue_arns=["gameSessionQueueArns"],
            notification_target="notificationTarget",
            rule_set_arn="ruleSetArn",
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
        acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
        name: builtins.str,
        request_timeout_seconds: jsii.Number,
        rule_set_name: builtins.str,
        acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
        additional_player_count: typing.Optional[jsii.Number] = None,
        backfill_mode: typing.Optional[builtins.str] = None,
        creation_time: typing.Optional[builtins.str] = None,
        custom_event_data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flex_match_mode: typing.Optional[builtins.str] = None,
        game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchmakingConfiguration.GamePropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        game_session_data: typing.Optional[builtins.str] = None,
        game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        rule_set_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param acceptance_required: A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to ``TRUE`` . With this option enabled, matchmaking tickets use the status ``REQUIRES_ACCEPTANCE`` to indicate when a completed potential match is waiting for player acceptance.
        :param name: A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        :param request_timeout_seconds: The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
        :param rule_set_name: A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
        :param acceptance_timeout_seconds: The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.
        :param additional_player_count: The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 10-person team, and the additional player count is set to 2, 10 players will be selected for the match and 2 more player slots will be open for future players. This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param backfill_mode: The method used to backfill game sessions that are created with this matchmaking configuration. Specify ``MANUAL`` when your game manages backfill requests manually or does not use the match backfill feature. Specify ``AUTOMATIC`` to have GameLift create a ``StartMatchBackfill`` request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in `Backfill Existing Games with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html>`_ . Automatic backfill is not available when ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param creation_time: A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).
        :param custom_event_data: Information to add to all events related to the matchmaking configuration.
        :param description: A description for the matchmaking configuration.
        :param flex_match_mode: Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution. - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event. - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift queue to start a game session for the match.
        :param game_properties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_data: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_queue_arns: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.
        :param notification_target: An SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.
        :param rule_set_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.
        :param tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5991dfcf120df852e2fd4ce6291a275a648645c817c923b70181ea8f56e61574)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMatchmakingConfigurationProps(
            acceptance_required=acceptance_required,
            name=name,
            request_timeout_seconds=request_timeout_seconds,
            rule_set_name=rule_set_name,
            acceptance_timeout_seconds=acceptance_timeout_seconds,
            additional_player_count=additional_player_count,
            backfill_mode=backfill_mode,
            creation_time=creation_time,
            custom_event_data=custom_event_data,
            description=description,
            flex_match_mode=flex_match_mode,
            game_properties=game_properties,
            game_session_data=game_session_data,
            game_session_queue_arns=game_session_queue_arns,
            notification_target=notification_target,
            rule_set_arn=rule_set_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ef86c5f161a3f7e4debb1e365142a6bed6fcfa0560f9575501529b34dee619)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f090e32e05cfaeb363b1750dd5ec26197130f385a7f9bddfe37da83c98c9462c)
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
        '''The unique Amazon Resource Name (ARN) for the ``MatchmakingConfiguration`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The ``MatchmakingConfiguration`` name, which is unique.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="acceptanceRequired")
    def acceptance_required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A flag that determines whether a match that was created with this configuration must be accepted by the matched players.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "acceptanceRequired"))

    @acceptance_required.setter
    def acceptance_required(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22e4fb0874509d31426b22f3ffefc8f7d3c205a887689be775fe8344351315b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptanceRequired", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50207e3d686076a987e377c81a96125dab3ab3f1620c58f788384cb08b17f088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="requestTimeoutSeconds")
    def request_timeout_seconds(self) -> jsii.Number:
        '''The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out.'''
        return typing.cast(jsii.Number, jsii.get(self, "requestTimeoutSeconds"))

    @request_timeout_seconds.setter
    def request_timeout_seconds(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a26beba0933992ac93ce4a627f18fa7a10ad26da6a35a99b1e377d5afa493b78)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set to use with this configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e22642273b822aeccc60cfa3d9595fa6bc154a168c63626eefb68d6a746ffad0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetName", value)

    @builtins.property
    @jsii.member(jsii_name="acceptanceTimeoutSeconds")
    def acceptance_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "acceptanceTimeoutSeconds"))

    @acceptance_timeout_seconds.setter
    def acceptance_timeout_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c28ab17b4e7b606d702229a14a7e46b7f9e86cb64d8dc6e0585fbcb058d0b242)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "acceptanceTimeoutSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="additionalPlayerCount")
    def additional_player_count(self) -> typing.Optional[jsii.Number]:
        '''The number of player slots in a match to keep open for future players.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "additionalPlayerCount"))

    @additional_player_count.setter
    def additional_player_count(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92699d7bd325a7ad10bdb62647176ac995f2c17688efde0d91661c8f0815eda7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalPlayerCount", value)

    @builtins.property
    @jsii.member(jsii_name="backfillMode")
    def backfill_mode(self) -> typing.Optional[builtins.str]:
        '''The method used to backfill game sessions that are created with this matchmaking configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "backfillMode"))

    @backfill_mode.setter
    def backfill_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b63753d38be440877984c0aa86a81bd07b6d2ce3aec33c9d8dd34c0ccde356c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "backfillMode", value)

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> typing.Optional[builtins.str]:
        '''A time stamp indicating when this data object was created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "creationTime"))

    @creation_time.setter
    def creation_time(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31d3fbc33faadd8b20143f6719f4142fc516a089f7e572e974783578c57954d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "creationTime", value)

    @builtins.property
    @jsii.member(jsii_name="customEventData")
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to add to all events related to the matchmaking configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customEventData"))

    @custom_event_data.setter
    def custom_event_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fac8d8c2d6825f23811aeea9f440bf664e97a02184ef417460a8d92056b2fb27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customEventData", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the matchmaking configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a956b02b663049817a64e32bfd1f09f9857feedac28f4eca2d36141c326cc5e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="flexMatchMode")
    def flex_match_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flexMatchMode"))

    @flex_match_mode.setter
    def flex_match_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a047908ff094a894704a6965c30654d87bb94e2aff3bd57abb16673fd6e98318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flexMatchMode", value)

    @builtins.property
    @jsii.member(jsii_name="gameProperties")
    def game_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]]:
        '''A set of custom properties for a game session, formatted as key-value pairs.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]], jsii.get(self, "gameProperties"))

    @game_properties.setter
    def game_properties(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMatchmakingConfiguration.GamePropertyProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0086331ec6c1fe164de53253519ecf95f522026cd3c4b9b2c0b16c300b99ceb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameProperties", value)

    @builtins.property
    @jsii.member(jsii_name="gameSessionData")
    def game_session_data(self) -> typing.Optional[builtins.str]:
        '''A set of custom game session properties, formatted as a single string value.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "gameSessionData"))

    @game_session_data.setter
    def game_session_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad31d919af9b1fb2de550bd5b00fcb306185a91f87127b6250e135a48937df4d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameSessionData", value)

    @builtins.property
    @jsii.member(jsii_name="gameSessionQueueArns")
    def game_session_queue_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "gameSessionQueueArns"))

    @game_session_queue_arns.setter
    def game_session_queue_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beae0e02206ffef8c392d9dd656f3a5ac2476b679628f1884cf15a4e8092c49d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gameSessionQueueArns", value)

    @builtins.property
    @jsii.member(jsii_name="notificationTarget")
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive matchmaking notifications.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "notificationTarget"))

    @notification_target.setter
    def notification_target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__83e843d11896164f9fbc52e89ade017c17b6cce0da297e20b5f554281c6c8e7e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationTarget", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetArn")
    def rule_set_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetArn"))

    @rule_set_arn.setter
    def rule_set_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b47741240f35249cfb706757b5199576646836e89e8f9fcd9e6bb884d238a3c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetArn", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking configuration resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9777adaa1c91123290fcf69dfad3f29c9d5affe68344eb61a6147f7c78954b2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingConfiguration.GamePropertyProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class GamePropertyProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''This key-value pair can store custom data about a game session.

            For example, you might use a ``GameProperty`` to track a game session's map, level of difficulty, or remaining time. The difficulty level could be specified like this: ``{"Key": "difficulty", "Value":"Novice"}`` .

            You can set game properties when creating a game session. You can also modify game properties of an active game session. When searching for game sessions, you can filter on game property keys and values. You can't delete game properties from a game session.

            For examples of working with game properties, see `Create a game session with properties <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#game-properties>`_ .

            :param key: The game property identifier.
            :param value: The game property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                game_property_property = gamelift.CfnMatchmakingConfiguration.GamePropertyProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2a4ff02870ac5c61154789061383399d6e97942338fe5b3af997be3c7938c3f)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The game property identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The game property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-matchmakingconfiguration-gameproperty.html#cfn-gamelift-matchmakingconfiguration-gameproperty-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GamePropertyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "acceptance_required": "acceptanceRequired",
        "name": "name",
        "request_timeout_seconds": "requestTimeoutSeconds",
        "rule_set_name": "ruleSetName",
        "acceptance_timeout_seconds": "acceptanceTimeoutSeconds",
        "additional_player_count": "additionalPlayerCount",
        "backfill_mode": "backfillMode",
        "creation_time": "creationTime",
        "custom_event_data": "customEventData",
        "description": "description",
        "flex_match_mode": "flexMatchMode",
        "game_properties": "gameProperties",
        "game_session_data": "gameSessionData",
        "game_session_queue_arns": "gameSessionQueueArns",
        "notification_target": "notificationTarget",
        "rule_set_arn": "ruleSetArn",
        "tags": "tags",
    },
)
class CfnMatchmakingConfigurationProps:
    def __init__(
        self,
        *,
        acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
        name: builtins.str,
        request_timeout_seconds: jsii.Number,
        rule_set_name: builtins.str,
        acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
        additional_player_count: typing.Optional[jsii.Number] = None,
        backfill_mode: typing.Optional[builtins.str] = None,
        creation_time: typing.Optional[builtins.str] = None,
        custom_event_data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flex_match_mode: typing.Optional[builtins.str] = None,
        game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        game_session_data: typing.Optional[builtins.str] = None,
        game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_target: typing.Optional[builtins.str] = None,
        rule_set_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMatchmakingConfiguration``.

        :param acceptance_required: A flag that determines whether a match that was created with this configuration must be accepted by the matched players. To require acceptance, set to ``TRUE`` . With this option enabled, matchmaking tickets use the status ``REQUIRES_ACCEPTANCE`` to indicate when a completed potential match is waiting for player acceptance.
        :param name: A unique identifier for the matchmaking configuration. This name is used to identify the configuration associated with a matchmaking request or ticket.
        :param request_timeout_seconds: The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out. Requests that fail due to timing out can be resubmitted as needed.
        :param rule_set_name: A unique identifier for the matchmaking rule set to use with this configuration. You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.
        :param acceptance_timeout_seconds: The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.
        :param additional_player_count: The number of player slots in a match to keep open for future players. For example, if the configuration's rule set specifies a match for a single 10-person team, and the additional player count is set to 2, 10 players will be selected for the match and 2 more player slots will be open for future players. This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param backfill_mode: The method used to backfill game sessions that are created with this matchmaking configuration. Specify ``MANUAL`` when your game manages backfill requests manually or does not use the match backfill feature. Specify ``AUTOMATIC`` to have GameLift create a ``StartMatchBackfill`` request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in `Backfill Existing Games with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html>`_ . Automatic backfill is not available when ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param creation_time: A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).
        :param custom_event_data: Information to add to all events related to the matchmaking configuration.
        :param description: A description for the matchmaking configuration.
        :param flex_match_mode: Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution. - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event. - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift queue to start a game session for the match.
        :param game_properties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_data: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_queue_arns: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.
        :param notification_target: An SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.
        :param rule_set_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.
        :param tags: A list of labels to assign to the new matchmaking configuration resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_matchmaking_configuration_props = gamelift.CfnMatchmakingConfigurationProps(
                acceptance_required=False,
                name="name",
                request_timeout_seconds=123,
                rule_set_name="ruleSetName",
            
                # the properties below are optional
                acceptance_timeout_seconds=123,
                additional_player_count=123,
                backfill_mode="backfillMode",
                creation_time="creationTime",
                custom_event_data="customEventData",
                description="description",
                flex_match_mode="flexMatchMode",
                game_properties=[gamelift.CfnMatchmakingConfiguration.GamePropertyProperty(
                    key="key",
                    value="value"
                )],
                game_session_data="gameSessionData",
                game_session_queue_arns=["gameSessionQueueArns"],
                notification_target="notificationTarget",
                rule_set_arn="ruleSetArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db0695f9efae852f4e3e7ce492e734297825efd4ac43986ef67506d40163a838)
            check_type(argname="argument acceptance_required", value=acceptance_required, expected_type=type_hints["acceptance_required"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument request_timeout_seconds", value=request_timeout_seconds, expected_type=type_hints["request_timeout_seconds"])
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
            check_type(argname="argument acceptance_timeout_seconds", value=acceptance_timeout_seconds, expected_type=type_hints["acceptance_timeout_seconds"])
            check_type(argname="argument additional_player_count", value=additional_player_count, expected_type=type_hints["additional_player_count"])
            check_type(argname="argument backfill_mode", value=backfill_mode, expected_type=type_hints["backfill_mode"])
            check_type(argname="argument creation_time", value=creation_time, expected_type=type_hints["creation_time"])
            check_type(argname="argument custom_event_data", value=custom_event_data, expected_type=type_hints["custom_event_data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flex_match_mode", value=flex_match_mode, expected_type=type_hints["flex_match_mode"])
            check_type(argname="argument game_properties", value=game_properties, expected_type=type_hints["game_properties"])
            check_type(argname="argument game_session_data", value=game_session_data, expected_type=type_hints["game_session_data"])
            check_type(argname="argument game_session_queue_arns", value=game_session_queue_arns, expected_type=type_hints["game_session_queue_arns"])
            check_type(argname="argument notification_target", value=notification_target, expected_type=type_hints["notification_target"])
            check_type(argname="argument rule_set_arn", value=rule_set_arn, expected_type=type_hints["rule_set_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "acceptance_required": acceptance_required,
            "name": name,
            "request_timeout_seconds": request_timeout_seconds,
            "rule_set_name": rule_set_name,
        }
        if acceptance_timeout_seconds is not None:
            self._values["acceptance_timeout_seconds"] = acceptance_timeout_seconds
        if additional_player_count is not None:
            self._values["additional_player_count"] = additional_player_count
        if backfill_mode is not None:
            self._values["backfill_mode"] = backfill_mode
        if creation_time is not None:
            self._values["creation_time"] = creation_time
        if custom_event_data is not None:
            self._values["custom_event_data"] = custom_event_data
        if description is not None:
            self._values["description"] = description
        if flex_match_mode is not None:
            self._values["flex_match_mode"] = flex_match_mode
        if game_properties is not None:
            self._values["game_properties"] = game_properties
        if game_session_data is not None:
            self._values["game_session_data"] = game_session_data
        if game_session_queue_arns is not None:
            self._values["game_session_queue_arns"] = game_session_queue_arns
        if notification_target is not None:
            self._values["notification_target"] = notification_target
        if rule_set_arn is not None:
            self._values["rule_set_arn"] = rule_set_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def acceptance_required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''A flag that determines whether a match that was created with this configuration must be accepted by the matched players.

        To require acceptance, set to ``TRUE`` . With this option enabled, matchmaking tickets use the status ``REQUIRES_ACCEPTANCE`` to indicate when a completed potential match is waiting for player acceptance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancerequired
        '''
        result = self._values.get("acceptance_required")
        assert result is not None, "Required property 'acceptance_required' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking configuration.

        This name is used to identify the configuration associated with a matchmaking request or ticket.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def request_timeout_seconds(self) -> jsii.Number:
        '''The maximum duration, in seconds, that a matchmaking ticket can remain in process before timing out.

        Requests that fail due to timing out can be resubmitted as needed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-requesttimeoutseconds
        '''
        result = self._values.get("request_timeout_seconds")
        assert result is not None, "Required property 'request_timeout_seconds' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def rule_set_name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set to use with this configuration.

        You can use either the rule set name or ARN value. A matchmaking configuration can only use rule sets that are defined in the same Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetname
        '''
        result = self._values.get("rule_set_name")
        assert result is not None, "Required property 'rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def acceptance_timeout_seconds(self) -> typing.Optional[jsii.Number]:
        '''The length of time (in seconds) to wait for players to accept a proposed match, if acceptance is required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-acceptancetimeoutseconds
        '''
        result = self._values.get("acceptance_timeout_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def additional_player_count(self) -> typing.Optional[jsii.Number]:
        '''The number of player slots in a match to keep open for future players.

        For example, if the configuration's rule set specifies a match for a single 10-person team, and the additional player count is set to 2, 10 players will be selected for the match and 2 more player slots will be open for future players. This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-additionalplayercount
        '''
        result = self._values.get("additional_player_count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def backfill_mode(self) -> typing.Optional[builtins.str]:
        '''The method used to backfill game sessions that are created with this matchmaking configuration.

        Specify ``MANUAL`` when your game manages backfill requests manually or does not use the match backfill feature. Specify ``AUTOMATIC`` to have GameLift create a ``StartMatchBackfill`` request whenever a game session has one or more open slots. Learn more about manual and automatic backfill in `Backfill Existing Games with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-backfill.html>`_ . Automatic backfill is not available when ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-backfillmode
        '''
        result = self._values.get("backfill_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def creation_time(self) -> typing.Optional[builtins.str]:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-creationtime
        '''
        result = self._values.get("creation_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_event_data(self) -> typing.Optional[builtins.str]:
        '''Information to add to all events related to the matchmaking configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-customeventdata
        '''
        result = self._values.get("custom_event_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description for the matchmaking configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flex_match_mode(self) -> typing.Optional[builtins.str]:
        '''Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution.

        - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event.
        - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift queue to start a game session for the match.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-flexmatchmode
        '''
        result = self._values.get("flex_match_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_properties(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchmakingConfiguration.GamePropertyProperty]]]]:
        '''A set of custom properties for a game session, formatted as key-value pairs.

        These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gameproperties
        '''
        result = self._values.get("game_properties")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchmakingConfiguration.GamePropertyProperty]]]], result)

    @builtins.property
    def game_session_data(self) -> typing.Optional[builtins.str]:
        '''A set of custom game session properties, formatted as a single string value.

        This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessiondata
        '''
        result = self._values.get("game_session_data")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def game_session_queue_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-gamesessionqueuearns
        '''
        result = self._values.get("game_session_queue_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def notification_target(self) -> typing.Optional[builtins.str]:
        '''An SNS topic ARN that is set up to receive matchmaking notifications.

        See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-notificationtarget
        '''
        result = self._values.get("notification_target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rule_set_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) associated with the GameLift matchmaking rule set resource that this configuration uses.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-rulesetarn
        '''
        result = self._values.get("rule_set_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking configuration resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingconfiguration.html#cfn-gamelift-matchmakingconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMatchmakingConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnMatchmakingRuleSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingRuleSet",
):
    '''Creates a new rule set for FlexMatch matchmaking.

    A rule set describes the type of match to create, such as the number and size of teams. It also sets the parameters for acceptable player matches, such as minimum skill level or character type.

    To create a matchmaking rule set, provide unique rule set name and the rule set body in JSON format. Rule sets must be defined in the same Region as the matchmaking configuration they are used with.

    Since matchmaking rule sets cannot be edited, it is a good idea to check the rule set syntax.

    *Learn more*

    - `Build a rule set <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-rulesets.html>`_
    - `Design a matchmaker <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-configuration.html>`_
    - `Matchmaking with FlexMatch <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-intro.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
    :cloudformationResource: AWS::GameLift::MatchmakingRuleSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_matchmaking_rule_set = gamelift.CfnMatchmakingRuleSet(self, "MyCfnMatchmakingRuleSet",
            name="name",
            rule_set_body="ruleSetBody",
        
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
        name: builtins.str,
        rule_set_body: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A unique identifier for the matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional ``name`` field in the rule set body.
        :param rule_set_body: A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.
        :param tags: A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ad8102fb28f35f09c9f78c601c99b706ee4e13284fddfd4e85f0e7b2b9cf57)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMatchmakingRuleSetProps(
            name=name, rule_set_body=rule_set_body, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d61a78aff0b1528ed82cb81e325639d2c75504b437ae15a2e7aac55347f0a30)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0d30b78f916dd39df63fb4f2b2f869f31a7016f89e96d8e5620551a28085c667)
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
        '''The unique Amazon Resource Name (ARN) assigned to the rule set.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrName")
    def attr_name(self) -> builtins.str:
        '''The unique name of the rule set.

        :cloudformationAttribute: Name
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrName"))

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e140482b102c49c4f1893c669d34c3cb70704179735bb2d142748745913c03a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetBody")
    def rule_set_body(self) -> builtins.str:
        '''A collection of matchmaking rules, formatted as a JSON string.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetBody"))

    @rule_set_body.setter
    def rule_set_body(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2901f58b94659dc1e7b989a5220ec6f85b0fd07e208ae745469d1ed13b3ecb5e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetBody", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking rule set resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0b8486d81489f869526b41e6ebf2b191599f06a6370135adbf247ac933792cd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_gamelift.CfnMatchmakingRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "rule_set_body": "ruleSetBody", "tags": "tags"},
)
class CfnMatchmakingRuleSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        rule_set_body: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnMatchmakingRuleSet``.

        :param name: A unique identifier for the matchmaking rule set. A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional ``name`` field in the rule set body.
        :param rule_set_body: A collection of matchmaking rules, formatted as a JSON string. Comments are not allowed in JSON, but most elements support a description field.
        :param tags: A list of labels to assign to the new matchmaking rule set resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_matchmaking_rule_set_props = gamelift.CfnMatchmakingRuleSetProps(
                name="name",
                rule_set_body="ruleSetBody",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7bc1d10bdb780b0aa1af65a9211c041b6a3e7bb4893d0bfc3a61136195a863d6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument rule_set_body", value=rule_set_body, expected_type=type_hints["rule_set_body"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "rule_set_body": rule_set_body,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''A unique identifier for the matchmaking rule set.

        A matchmaking configuration identifies the rule set it uses by this name value. Note that the rule set name is different from the optional ``name`` field in the rule set body.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def rule_set_body(self) -> builtins.str:
        '''A collection of matchmaking rules, formatted as a JSON string.

        Comments are not allowed in JSON, but most elements support a description field.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-rulesetbody
        '''
        result = self._values.get("rule_set_body")
        assert result is not None, "Required property 'rule_set_body' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new matchmaking rule set resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-matchmakingruleset.html#cfn-gamelift-matchmakingruleset-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMatchmakingRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnScript(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnScript",
):
    '''The ``AWS::GameLift::Script`` resource creates a new script record for your Realtime Servers script.

    Realtime scripts are JavaScript that provide configuration settings and optional custom game logic for your game. The script is deployed when you create a Realtime Servers fleet to host your game sessions. Script logic is executed during an active game session.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
    :cloudformationResource: AWS::GameLift::Script
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_gamelift as gamelift
        
        cfn_script = gamelift.CfnScript(self, "MyCfnScript",
            storage_location=gamelift.CfnScript.S3LocationProperty(
                bucket="bucket",
                key="key",
                role_arn="roleArn",
        
                # the properties below are optional
                object_version="objectVersion"
            ),
        
            # the properties below are optional
            name="name",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            version="version"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        storage_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnScript.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param storage_location: The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ``ObjectVersion`` parameter to specify an earlier version.
        :param name: A descriptive label that is associated with a script. Script names do not need to be unique.
        :param tags: A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param version: The version that is associated with a build or script. Version strings do not need to be unique.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a610f7d9791794a98e26c23e6a2c7f57a2aceb363ba1a205d32cc00112745595)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnScriptProps(
            storage_location=storage_location, name=name, tags=tags, version=version
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e467306a2b7b42d3bd4d40de8ebac0e5dbae11f33d3c54e42eae339fc88bc56b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bc786feeaa63a2566413adc42f5f2b3c38ba00daa4986115963a8d6d6c1a1f30)
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
        '''The unique Amazon Resource Name (ARN) for the script.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> builtins.str:
        '''A time stamp indicating when this data object was created.

        Format is a number expressed in Unix time as milliseconds (for example ``"1469498468.057"`` ).

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for a Realtime script.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrSizeOnDisk")
    def attr_size_on_disk(self) -> jsii.Number:
        '''The file size of the uploaded Realtime script, expressed in bytes.

        When files are uploaded from an S3 location, this value remains at "0".

        :cloudformationAttribute: SizeOnDisk
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSizeOnDisk"))

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
    @jsii.member(jsii_name="storageLocation")
    def storage_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnScript.S3LocationProperty"]:
        '''The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnScript.S3LocationProperty"], jsii.get(self, "storageLocation"))

    @storage_location.setter
    def storage_location(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnScript.S3LocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67239519d512a22693f642bf29d26d0bffc0cf4f5f242e2295be3b8cf8bc1f30)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "storageLocation", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a script.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df6266bf40e8b346c6a57c12d46137c3fe4f29ca8b9c37ef0dfb5715f82fbbf1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new script resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59fee6448a284bb6932305c7159828353c13832415292cceb7a74453dd8177cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''The version that is associated with a build or script.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22d619527b7b1b8b21c8e5ffa7ab4abbd6f2c76a23e5179dd879485530ec9e39)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_gamelift.CfnScript.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "key": "key",
            "role_arn": "roleArn",
            "object_version": "objectVersion",
        },
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            role_arn: builtins.str,
            object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The location in Amazon S3 where build or script files can be stored for access by Amazon GameLift.

            :param bucket: An Amazon S3 bucket identifier. Thename of the S3 bucket. .. epigraph:: Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).
            :param key: The name of the zip file that contains the build files or script files.
            :param role_arn: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift to access the S3 bucket.
            :param object_version: The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_gamelift as gamelift
                
                s3_location_property = gamelift.CfnScript.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    object_version="objectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1bc9de7e6777aff8308976cae56a2f5dd2d0e14f8555821f0396e5b81605502e)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument object_version", value=object_version, expected_type=type_hints["object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "role_arn": role_arn,
            }
            if object_version is not None:
                self._values["object_version"] = object_version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''An Amazon S3 bucket identifier. Thename of the S3 bucket.

            .. epigraph::

               Amazon GameLift doesn't support uploading from Amazon S3 buckets with names that contain a dot (.).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''The name of the zip file that contains the build files or script files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) for an IAM role that allows Amazon GameLift to access the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The version of the file, if object versioning is turned on for the bucket.

            Amazon GameLift uses this information when retrieving files from an S3 bucket that you own. Use this parameter to specify a specific version of the file. If not set, the latest version of the file is retrieved.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-script-s3location.html#cfn-gamelift-script-s3location-objectversion
            '''
            result = self._values.get("object_version")
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
    jsii_type="aws-cdk-lib.aws_gamelift.CfnScriptProps",
    jsii_struct_bases=[],
    name_mapping={
        "storage_location": "storageLocation",
        "name": "name",
        "tags": "tags",
        "version": "version",
    },
)
class CfnScriptProps:
    def __init__(
        self,
        *,
        storage_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScript.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
        name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnScript``.

        :param storage_location: The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored. The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ``ObjectVersion`` parameter to specify an earlier version.
        :param name: A descriptive label that is associated with a script. Script names do not need to be unique.
        :param tags: A list of labels to assign to the new script resource. Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.
        :param version: The version that is associated with a build or script. Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_gamelift as gamelift
            
            cfn_script_props = gamelift.CfnScriptProps(
                storage_location=gamelift.CfnScript.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    object_version="objectVersion"
                ),
            
                # the properties below are optional
                name="name",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a56c9731d882f4e0af0b136c973132c594cdb2f6c8607aa9bd92978d6d80b5)
            check_type(argname="argument storage_location", value=storage_location, expected_type=type_hints["storage_location"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "storage_location": storage_location,
        }
        if name is not None:
            self._values["name"] = name
        if tags is not None:
            self._values["tags"] = tags
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def storage_location(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnScript.S3LocationProperty]:
        '''The location of the Amazon S3 bucket where a zipped file containing your Realtime scripts is stored.

        The storage location must specify the Amazon S3 bucket name, the zip file name (the "key"), and a role ARN that allows Amazon GameLift to access the Amazon S3 storage location. The S3 bucket must be in the same Region where you want to create a new script. By default, Amazon GameLift uploads the latest version of the zip file; if you have S3 object versioning turned on, you can use the ``ObjectVersion`` parameter to specify an earlier version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-storagelocation
        '''
        result = self._values.get("storage_location")
        assert result is not None, "Required property 'storage_location' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnScript.S3LocationProperty], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''A descriptive label that is associated with a script.

        Script names do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of labels to assign to the new script resource.

        Tags are developer-defined key-value pairs. Tagging AWS resources are useful for resource management, access management and cost allocation. For more information, see `Tagging AWS Resources <https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html>`_ in the *AWS General Reference* . Once the resource is created, you can use TagResource, UntagResource, and ListTagsForResource to add, remove, and view tags. The maximum tag limit may be lower than stated. See the AWS General Reference for actual tagging limits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''The version that is associated with a build or script.

        Version strings do not need to be unique.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-script.html#cfn-gamelift-script-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnScriptProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlias",
    "CfnAliasProps",
    "CfnBuild",
    "CfnBuildProps",
    "CfnContainerGroupDefinition",
    "CfnContainerGroupDefinitionProps",
    "CfnFleet",
    "CfnFleetProps",
    "CfnGameServerGroup",
    "CfnGameServerGroupProps",
    "CfnGameSessionQueue",
    "CfnGameSessionQueueProps",
    "CfnLocation",
    "CfnLocationProps",
    "CfnMatchmakingConfiguration",
    "CfnMatchmakingConfigurationProps",
    "CfnMatchmakingRuleSet",
    "CfnMatchmakingRuleSetProps",
    "CfnScript",
    "CfnScriptProps",
]

publication.publish()

def _typecheckingstub__6a91f3a4a7dfbcf1655ec6812682d7a8824bfb46a9ce2a65e3c859108e3633c8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlias.RoutingStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6c7223e714d0339897da2cbb4b67d9e03a5022aa12f568680b86e828460d501(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1fbbe6ec42c9ed6d59226c8fe9df0391ca1a181a605b688f9e6267ea6f2a055(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8666b32153f5438f8d6ea2d03ad01cbf8c67bad1071d8e1cdc42963a8912ad3c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__529d8fec4c06eafb4c38da47298670dd8132ede4d21975eafb43f51a366a3d82(
    value: typing.Union[_IResolvable_da3f097b, CfnAlias.RoutingStrategyProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d25b43c56fe6060dfb6e36792550c92a6a537d6d2e31b8c97947858787f55a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4057d890d9c2fba51db14d6885375c0c7263cd6b07fb4401e3fb51d7676734f9(
    *,
    type: builtins.str,
    fleet_id: typing.Optional[builtins.str] = None,
    message: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74c18c4446e0f846baf63e2e707aa2ba663f37170623164846853f1176d7891(
    *,
    name: builtins.str,
    routing_strategy: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAlias.RoutingStrategyProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2f3884df6574dd3d4e76d857acf05a15fdc616d818da1cebcfcce4084ca8ddc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: typing.Optional[builtins.str] = None,
    operating_system: typing.Optional[builtins.str] = None,
    server_sdk_version: typing.Optional[builtins.str] = None,
    storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBuild.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dabd8e19951007a8e9f2bcb21f9e872c9fc5b6a638701939005bc4d813c12a3(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52be0a2eff399965a7232bfe5d136a98b17426adc22dd0fe1be4ebd8de6c3b47(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a86d40dd79232f1b81dd44ba375e9a9432429c05c3444beaf1128ab336d19dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086f4a5a0a253ca19c97937d0f25a8ade9bb623ef1c01cacdc76233a24f4ef0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7f1e9548565a4821c004b0e86bae438a45b45de61043075555fb43127d349d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdd3e9ea10aa8547b05a398258efac5d3e786e68d7875c76104c89d2a3178e02(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBuild.StorageLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f69e6e764a220fcdeac2ac30cce1d3fbf57e0ef02b497976b1bb0e8162a6a67(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d6726269ab0714348382710795aeac31efd3f1d29c3bac05a4aefa5c90bcba4(
    *,
    bucket: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ea486b468f726c96f63f78347aac31445ce3b0bd1ea282f6fce30ca4e8642d7(
    *,
    name: typing.Optional[builtins.str] = None,
    operating_system: typing.Optional[builtins.str] = None,
    server_sdk_version: typing.Optional[builtins.str] = None,
    storage_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBuild.StorageLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d0ad3aeb1243549bc05c0346bb1e8303d21326ec9f1a17ec63327d7e3f29a1e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    container_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    operating_system: builtins.str,
    total_cpu_limit: jsii.Number,
    total_memory_limit: jsii.Number,
    scheduling_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b07a706beb428681d6a41fe2a705cfe7e9f6f65c0df4708d633a856c73d6fa7b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abcc96ad0c8f9f987fd719eb37179f12dda8829dbbc0b9fb28188a52044ec711(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d575dc521c3da1f3682c88ce08e24b38977a41bef8807469e908a4fc94b8be0(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContainerGroupDefinition.ContainerDefinitionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90e8a024d1021ae9b57dadc57167a55f375efa5756fd3358541d1bbca8f16cf0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f85c42319aa42e6c796369d8760bfb73c97a6305632fa1b86497b93a214a2ec(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c70806f2091ef0e31ae18f95ca9388e13070bc234c9db0acb79308e3bb8064c8(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4cc7de67e0ef4b7a915c9522aa5d27817d4c88d3cc0d6cc3897ec44fe82624e(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4192c1232484aa6cb4b7a0ff2133a07c228af7fc593005174668d67f88e787(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d9905e11429554186c96e0a5c07109b132519014161fc8e8d7aa9f4250218d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d96474fb31ceec64a55f6a09274f19f2dde05387b5bdd5c76ce6f26d90d5eb7(
    *,
    container_name: builtins.str,
    image_uri: builtins.str,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    cpu: typing.Optional[jsii.Number] = None,
    depends_on: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerDependencyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    essential: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    health_check: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerHealthCheckProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    memory_limits: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.MemoryLimitsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    port_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.PortConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resolved_image_digest: typing.Optional[builtins.str] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8424bed9ce9567d13ec372652e5d607735583e13219bd42143f538aee3feb1f(
    *,
    condition: builtins.str,
    container_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8a971f77ef4383909669846d3e4ee4a8463f7353ec0c1aa4da152ea7ec43bb9(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95b1e7083ac6b3d39e0bc5926b3c9ee368385be498c61499a81f860b155d0a1d(
    *,
    command: typing.Sequence[builtins.str],
    interval: typing.Optional[jsii.Number] = None,
    retries: typing.Optional[jsii.Number] = None,
    start_period: typing.Optional[jsii.Number] = None,
    timeout: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3e35cf8a42e8cbcdf12218e64e5ac29c19f0813f144c8d75e97d3e3313d396(
    *,
    from_port: jsii.Number,
    protocol: builtins.str,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ac03f75ba7cf3ff7267cf9e9544e940c9974e78a4d364eed01d2ebb6bc2d3fa(
    *,
    hard_limit: typing.Optional[jsii.Number] = None,
    soft_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49796d7f2a6fb9a60e370fb5b8e88da33d84ca298d8833d8e64e3d80586cedf7(
    *,
    container_port_ranges: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerPortRangeProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b760a12182b9da0a53204aa5510dae28c2cda4c4fba1ef77f0245093da04ea4(
    *,
    container_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContainerGroupDefinition.ContainerDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    name: builtins.str,
    operating_system: builtins.str,
    total_cpu_limit: jsii.Number,
    total_memory_limit: jsii.Number,
    scheduling_strategy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21fe09a90444788b3c862f454214d4e160757c9b02d0598d282f68b7f79d749f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apply_capacity: typing.Optional[builtins.str] = None,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_type: typing.Optional[builtins.str] = None,
    container_groups_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ContainerGroupsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    desired_ec2_instances: typing.Optional[jsii.Number] = None,
    ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_type: typing.Optional[builtins.str] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    instance_role_credentials_provider: typing.Optional[builtins.str] = None,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    min_size: typing.Optional[jsii.Number] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
    peer_vpc_id: typing.Optional[builtins.str] = None,
    resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ResourceCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.RuntimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    script_id: typing.Optional[builtins.str] = None,
    server_launch_parameters: typing.Optional[builtins.str] = None,
    server_launch_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__264e19b1dd38619175091751b1eec860e08c2225c7798789a29ec89ab8971593(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__905cca04e4d534db21b7356373856ed4d0fb9130ab18a34d31eb7127b3ecdbc1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3e6bf68da3a08ee0a6dbdff6b571a1a9348dfd6d1f15864e1efd85595ae689(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc575abdd043760dd1cbe4178328d65df4b96ee18072484d24bd88d2e2d340ac(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e4da24e64fdcbb7830d9e09a27219d611e9c486d09dd2a970381192b5e97213(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fecb16629d96a3f0b5b4acdf8ba4a4b1a44a9314ada24ee4bf29122c11df18e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f46d27389fd45eb3384977842c4289c60e5795c4a4bd6e08002ec26643232bc(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.CertificateConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__022e8bf70858e61cedf1ac2f0bbe1af01706924dda3af7f4e655e78c1b5985db(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ab5ebb46adc7fe2bb2e1911285f98090170c29093f6e28b584096baafa36aa(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ContainerGroupsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eec78595476346beb2b42a6ac89d6890fb357c8bc49fbafff985bc1417bca206(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4941614413c1e1554010809926c621b6030f9b38418b19c26a4dbbfc56fd9cfd(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84bfe64c88748026f1ea76b00a3c1eeeffe26c5a9e7df3f052f9069032249c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5edb81bb6e5f986aaa8654e60493e7ec0e42f57ed43a7481b48714433fb0b95(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc9a52bd70aa79d8d459ba6e23d2020447c1f1d4faa157c8836aad4e87181d56(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7947f4ea6b160028fb5bbf20fcbd0cc9eb46ba122d737f3c792a6be5043d8577(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6765d7366d76df2864c4535568d1edf808ceec869046e302b0c842674b46c102(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1377dfdecc90d2457b2fe3e90aa35cecb44bf218eb1836fc28cbc15b7a4812f3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35b29d2e11870cd4d0ea412c5de5d02fbb8bb765ed67873227f57868f234fe52(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbc74cb38ce8a622308c22d16cb5fe99f9f601acdfd26460b9b33bd15037e42f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02facc74087efba3bcf2b21fc12cd9fae063e33440abacb0fdfdf65ecb3fe7ad(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d460bc2f634afc1e2c222819f53ddf45b2647b9ccf197380a1419dfb4b91c61a(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c8b79569fe310aaed26b6fa78159b7101d72974e478dd380ca0713aea1d9a9f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a648f419a89a6e5926858e8481241ede65ca343e3b797aecd480dec6c8b20939(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fd0ab83e874e8110a1f4093ff1e48395bf94729c8f475c6e23b4d22971f3428(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ee8415ef994fb87ac2edf852ffd98a21384f9eccc26d3a0537563c2b00fbed(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.ResourceCreationLimitPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91bbc8eaa0f72d2032ef5cfd51906c5fc923f7ed24ede99b907cb24fe23da499(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.RuntimeConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082c3456142a6049adc9dd4639e8b2ca94a21dbf9412cc70d0ea2e1babccf7c3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.ScalingPolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d89c92d80f54ea7b8f3b7a14762b9c71a927d074d3727f05bc330349648ba92(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b86e485f6c758ba0a09838614ee6f5e63a4ba69e6100fd77af039cc9f223b152(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63d5bf96be81c4a6b00ef1deb4d8846acf0053313fb89efd0ded1f0931c66844(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3897ffc82938e5bf4e6384b3a83b22f50c7189a71eb0fc30ea8f17642db5ef9(
    *,
    cost: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3cca5919f32f3e2cb6c385afda08bf3b194b8baf60b4d20e5f9f580659cc84(
    *,
    certificate_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65c7b986d31ccdfa5d51331dd935bb4233bcf101bbfe90052f66eb229319a0a8(
    *,
    from_port: jsii.Number,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af8dbebebd0e2db6dda0806b67c6edeb6e2460f1c55d333b8c83a5380be41afd(
    *,
    connection_port_range: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ConnectionPortRangeProperty, typing.Dict[builtins.str, typing.Any]]],
    container_group_definition_names: typing.Sequence[builtins.str],
    container_groups_per_instance: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ContainerGroupsPerInstanceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3473ac2106ce855ef7577b99df8d3e14e6085d02c7bf0c0fb919636a907449c1(
    *,
    desired_replica_container_groups_per_instance: typing.Optional[jsii.Number] = None,
    max_replica_container_groups_per_instance: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70f885be25c9084dbab3b02a36601be0e37c43ab741ea7dd646494423839333a(
    *,
    from_port: jsii.Number,
    ip_range: builtins.str,
    protocol: builtins.str,
    to_port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76847ac983ab72ef92adc1b0579d769ca62af002ef71c76165cbd879da8645fc(
    *,
    desired_ec2_instances: jsii.Number,
    max_size: jsii.Number,
    min_size: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__716ff23eda74da42620dc64832ed27ab5a267661bd90b16577ee48991436d14c(
    *,
    location: builtins.str,
    location_capacity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationCapacityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b5bf70d1fc5987b674dcb2717a733f347f6ff57d29689b7a2a12d07ccfab884(
    *,
    new_game_sessions_per_creator: typing.Optional[jsii.Number] = None,
    policy_period_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae990fc53511e6175c77d897f3a8a6bc35be77827bfc0f1be6b1f8d7967e54c3(
    *,
    game_session_activation_timeout_seconds: typing.Optional[jsii.Number] = None,
    max_concurrent_game_session_activations: typing.Optional[jsii.Number] = None,
    server_processes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ServerProcessProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8690870b8fddf2f2747a9a00d8f1a693d624b5f4f72283ed427b04667f02bd8(
    *,
    metric_name: builtins.str,
    name: builtins.str,
    comparison_operator: typing.Optional[builtins.str] = None,
    evaluation_periods: typing.Optional[jsii.Number] = None,
    location: typing.Optional[builtins.str] = None,
    policy_type: typing.Optional[builtins.str] = None,
    scaling_adjustment: typing.Optional[jsii.Number] = None,
    scaling_adjustment_type: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    target_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.TargetConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    threshold: typing.Optional[jsii.Number] = None,
    update_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc845ade67d7aff6536f53651c26f049fc04883863968a83da759b79b0a6d035(
    *,
    concurrent_executions: jsii.Number,
    launch_path: builtins.str,
    parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__472ce4c72467f1a69fc974099623863890460564fbbe1e98eb694a9a4b1546b7(
    *,
    target_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a51a418ba5b606bdfc45dc50c3172e280a12e078a7392f3258d5d329e037a55(
    *,
    name: builtins.str,
    anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    apply_capacity: typing.Optional[builtins.str] = None,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_type: typing.Optional[builtins.str] = None,
    container_groups_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ContainerGroupsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    desired_ec2_instances: typing.Optional[jsii.Number] = None,
    ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_type: typing.Optional[builtins.str] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
    instance_role_credentials_provider: typing.Optional[builtins.str] = None,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.LocationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    log_paths: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    metric_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    min_size: typing.Optional[jsii.Number] = None,
    new_game_session_protection_policy: typing.Optional[builtins.str] = None,
    peer_vpc_aws_account_id: typing.Optional[builtins.str] = None,
    peer_vpc_id: typing.Optional[builtins.str] = None,
    resource_creation_limit_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ResourceCreationLimitPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    runtime_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.RuntimeConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scaling_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.ScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    script_id: typing.Optional[builtins.str] = None,
    server_launch_parameters: typing.Optional[builtins.str] = None,
    server_launch_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a0d4e260fba686f866a885f9a542286a05d085037e114d8febabfdd92cfd24(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    game_server_group_name: builtins.str,
    instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.InstanceDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    role_arn: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    balancing_strategy: typing.Optional[builtins.str] = None,
    delete_option: typing.Optional[builtins.str] = None,
    game_server_protection_policy: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.LaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32ac0616025cd3de739c7101cea4baa4d9d85d9755bd18a18599fd247f47e000(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a77b5aa43581e64c5c91459806a51ceb403900395eac9fb9f2cdec42c5c7fad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89556427a3cb2e1aa05738182ce0459e80e576c3c25bd0cc1d7dc630a122bd67(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__868421ea021122381c2075a524c1d4785b63637a5ae0e28ee1747043ceaf14fc(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.InstanceDefinitionProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76aa84abc5cd589d0abb99434e1ecea33850fb0ccbb6eee11380bfa754fc482(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5ee0eb377684162644f965e1106f08af9e4431bca94796da59b89abc7ffd998(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.AutoScalingPolicyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5fc25560f0a78783f5ed8bb510e2e86e267d9629bd271a2403e866afa14e22e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a84355ef62b2fd37a277a26c39b2735a06cf204ad010f5de3744a8280e5be056(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29b538c5660178a7532c29be9d3acb184e85dfbac80460c002d5f219fa429d79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e1b30118131dd3fcdd29554603028109f41bf9f28d638ff1f26fc0de989e8b6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameServerGroup.LaunchTemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c07d732b195687bb610c12d0db39761316bbb61e6416116d630f224124000c66(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e884c21390c0adc461578e34ea9d201ce75716ffda1892218e4f39b5f6ae3e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0dba0594bea5d13fc9125228769f878f9679d696d511472809787acd5605b3e6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b4d5326a42c1fdc1afa97e1f31ad389e2aac7fbe1c4f2c6a3f614b0d23761c7(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3ca9dc4f6076efea7dd9c18ae3d0d4e330ecd050951dbb0b731443e8b262e56(
    *,
    target_tracking_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.TargetTrackingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    estimated_instance_warmup: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b295ebcaf7cae28b09dfaf0a8c5a7fe40fd9a1dfa65423b6093711f0f56e28fc(
    *,
    instance_type: builtins.str,
    weighted_capacity: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25060a9b2c2773d45ef64eabb5fbdc70d6c95644145351fecb4e3d70bd06f5e2(
    *,
    launch_template_id: typing.Optional[builtins.str] = None,
    launch_template_name: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef13423f0408e9300989065f2e1f7a323aeaaef1367e95591fe66bbfc152a818(
    *,
    target_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb2b330cbc0b2bd24b542707e03f7de3d6d3afa7d8fa0efaac64771d13b95db1(
    *,
    game_server_group_name: builtins.str,
    instance_definitions: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.InstanceDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]]],
    role_arn: builtins.str,
    auto_scaling_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.AutoScalingPolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    balancing_strategy: typing.Optional[builtins.str] = None,
    delete_option: typing.Optional[builtins.str] = None,
    game_server_protection_policy: typing.Optional[builtins.str] = None,
    launch_template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameServerGroup.LaunchTemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_size: typing.Optional[jsii.Number] = None,
    min_size: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_subnets: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2435e37790a5987d49478948c0c1ac36c9e463fa29441c46ba0aa4d567f2c585(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    custom_event_data: typing.Optional[builtins.str] = None,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PlayerLatencyPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PriorityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cc05027a8472775374b6846f6c9ab499cc41f64fa8ed31ccbfd79e142b8b76d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b257e875617af0371cc9d2c1574fb2ba9c0e4ecbacf958d56eabd8a77d1fa023(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac381d2dd8ded0682b62f79246a99597b2aca0600afaa30c9f48b5f1411bbfa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8260843224b7180260627c762aaa0ae5afbcd912f5da71a3c576430e069f9e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f656db0c32504c821ba5c5d5067bac317db7def96a39500c5847a853576e95ec(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.DestinationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e5b9b16ae8732de19b82da87c71cb00a9d06d7a37c8d217314158c063bf0f7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.FilterConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f838580d46a0a1a08c09d8b8b17de066bfb74896289f61432e755d32429e2a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3da0f541db3f4dba488790dc678e2dd0872a5271bf05bb0ddcb181884f5dfb80(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PlayerLatencyPolicyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__622dc07e672d46f719db763d6bf2dec499f84a17b72186d593df03f3fcb1ae7f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnGameSessionQueue.PriorityConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3a8c431c366d3fa711cfb42cebf2d1647b8f2a1a5e129b5536c91cdf0135eb8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ad24ec0156a0a24d8fe08ecf8470df28f9f1501a3ab442e887e2d1c5ef03df4(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d1ad7f562ade1312178a63d9196a21119d0e6500b9d651931481a59d709d462(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18c067b373a2989add73f26fd5a7da221d485dae82bf0842dcedf8017b6ad5f(
    *,
    allowed_locations: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__682a2ca85600f7cf3e8fc279fa7f5c2ecab05f65cc96301b5afab09b2da5c684(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7a9bd74ee679564c60f66c08f4f2d7739a8abfa4c61e93feedbd8457081f585(
    *,
    maximum_individual_player_latency_milliseconds: typing.Optional[jsii.Number] = None,
    policy_duration_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bffce6e10d5ec1968a817a7df177891e44b6ec986ec424c92d4e71dd599b36ac(
    *,
    location_order: typing.Optional[typing.Sequence[builtins.str]] = None,
    priority_order: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b18cdd98f5e3e7424d6d930e416c9690c2e3cdcc56ac70f4688a8984ea0e8b7(
    *,
    name: builtins.str,
    custom_event_data: typing.Optional[builtins.str] = None,
    destinations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.DestinationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    filter_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.FilterConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    player_latency_policies: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PlayerLatencyPolicyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    priority_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGameSessionQueue.PriorityConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_in_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__404fc5857cf63bdcf757784b5c810e73ce1c99d8d82c264eec7a145724580816(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    location_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d95943640733fe4e543a0c2a9e0a647a118d84274c6945f59f0598a9585e4a4b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a18532e89ee9aa9c91c15cc19d2c9f2345325702005b9a2708e43204329266ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f9bf4f89ef7693448c9209f894d6900bab55884642fc136222c211e82f3015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db22dc038d314307a9d7182d88d8959bd024bf2feff9aee7f03deba1df46ca5c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ffffd954dd9a648cdd22ea8069e64a916e69b5690bde3de5bb865f1a555e5d(
    *,
    location_name: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5991dfcf120df852e2fd4ce6291a275a648645c817c923b70181ea8f56e61574(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
    name: builtins.str,
    request_timeout_seconds: jsii.Number,
    rule_set_name: builtins.str,
    acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
    additional_player_count: typing.Optional[jsii.Number] = None,
    backfill_mode: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[builtins.str] = None,
    custom_event_data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    flex_match_mode: typing.Optional[builtins.str] = None,
    game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    game_session_data: typing.Optional[builtins.str] = None,
    game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    rule_set_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ef86c5f161a3f7e4debb1e365142a6bed6fcfa0560f9575501529b34dee619(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f090e32e05cfaeb363b1750dd5ec26197130f385a7f9bddfe37da83c98c9462c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22e4fb0874509d31426b22f3ffefc8f7d3c205a887689be775fe8344351315b4(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50207e3d686076a987e377c81a96125dab3ab3f1620c58f788384cb08b17f088(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a26beba0933992ac93ce4a627f18fa7a10ad26da6a35a99b1e377d5afa493b78(
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e22642273b822aeccc60cfa3d9595fa6bc154a168c63626eefb68d6a746ffad0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c28ab17b4e7b606d702229a14a7e46b7f9e86cb64d8dc6e0585fbcb058d0b242(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92699d7bd325a7ad10bdb62647176ac995f2c17688efde0d91661c8f0815eda7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b63753d38be440877984c0aa86a81bd07b6d2ce3aec33c9d8dd34c0ccde356c3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31d3fbc33faadd8b20143f6719f4142fc516a089f7e572e974783578c57954d8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fac8d8c2d6825f23811aeea9f440bf664e97a02184ef417460a8d92056b2fb27(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a956b02b663049817a64e32bfd1f09f9857feedac28f4eca2d36141c326cc5e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a047908ff094a894704a6965c30654d87bb94e2aff3bd57abb16673fd6e98318(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0086331ec6c1fe164de53253519ecf95f522026cd3c4b9b2c0b16c300b99ceb2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMatchmakingConfiguration.GamePropertyProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad31d919af9b1fb2de550bd5b00fcb306185a91f87127b6250e135a48937df4d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beae0e02206ffef8c392d9dd656f3a5ac2476b679628f1884cf15a4e8092c49d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__83e843d11896164f9fbc52e89ade017c17b6cce0da297e20b5f554281c6c8e7e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b47741240f35249cfb706757b5199576646836e89e8f9fcd9e6bb884d238a3c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9777adaa1c91123290fcf69dfad3f29c9d5affe68344eb61a6147f7c78954b2c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2a4ff02870ac5c61154789061383399d6e97942338fe5b3af997be3c7938c3f(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db0695f9efae852f4e3e7ce492e734297825efd4ac43986ef67506d40163a838(
    *,
    acceptance_required: typing.Union[builtins.bool, _IResolvable_da3f097b],
    name: builtins.str,
    request_timeout_seconds: jsii.Number,
    rule_set_name: builtins.str,
    acceptance_timeout_seconds: typing.Optional[jsii.Number] = None,
    additional_player_count: typing.Optional[jsii.Number] = None,
    backfill_mode: typing.Optional[builtins.str] = None,
    creation_time: typing.Optional[builtins.str] = None,
    custom_event_data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    flex_match_mode: typing.Optional[builtins.str] = None,
    game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    game_session_data: typing.Optional[builtins.str] = None,
    game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_target: typing.Optional[builtins.str] = None,
    rule_set_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ad8102fb28f35f09c9f78c601c99b706ee4e13284fddfd4e85f0e7b2b9cf57(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    rule_set_body: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d61a78aff0b1528ed82cb81e325639d2c75504b437ae15a2e7aac55347f0a30(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d30b78f916dd39df63fb4f2b2f869f31a7016f89e96d8e5620551a28085c667(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e140482b102c49c4f1893c669d34c3cb70704179735bb2d142748745913c03a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2901f58b94659dc1e7b989a5220ec6f85b0fd07e208ae745469d1ed13b3ecb5e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b8486d81489f869526b41e6ebf2b191599f06a6370135adbf247ac933792cd6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bc1d10bdb780b0aa1af65a9211c041b6a3e7bb4893d0bfc3a61136195a863d6(
    *,
    name: builtins.str,
    rule_set_body: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a610f7d9791794a98e26c23e6a2c7f57a2aceb363ba1a205d32cc00112745595(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    storage_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScript.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e467306a2b7b42d3bd4d40de8ebac0e5dbae11f33d3c54e42eae339fc88bc56b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc786feeaa63a2566413adc42f5f2b3c38ba00daa4986115963a8d6d6c1a1f30(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67239519d512a22693f642bf29d26d0bffc0cf4f5f242e2295be3b8cf8bc1f30(
    value: typing.Union[_IResolvable_da3f097b, CfnScript.S3LocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df6266bf40e8b346c6a57c12d46137c3fe4f29ca8b9c37ef0dfb5715f82fbbf1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59fee6448a284bb6932305c7159828353c13832415292cceb7a74453dd8177cc(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22d619527b7b1b8b21c8e5ffa7ab4abbd6f2c76a23e5179dd879485530ec9e39(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bc9de7e6777aff8308976cae56a2f5dd2d0e14f8555821f0396e5b81605502e(
    *,
    bucket: builtins.str,
    key: builtins.str,
    role_arn: builtins.str,
    object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a56c9731d882f4e0af0b136c973132c594cdb2f6c8607aa9bd92978d6d80b5(
    *,
    storage_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnScript.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
