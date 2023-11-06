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
class CfnAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnAlias",
):
    '''The ``AWS::GameLift::Alias`` resource creates an alias for an Amazon GameLift (GameLift) fleet destination.

    There are two types of routing strategies for aliases: simple and terminal. A simple alias points to an active fleet. A terminal alias displays a message instead of routing players to an active fleet. For example, a terminal alias might display a URL link that directs players to an upgrade site. You can use aliases to define destinations in a game session queue or when requesting new game sessions.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-alias.html
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
        :param server_sdk_version: The Amazon GameLift Server SDK version used to develop your game server.
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
        '''A unique identifier for a build to be deployed on the new fleet.

        If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a READY status. This fleet setting cannot be changed once the fleet is created.

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
        '''The Amazon GameLift Server SDK version used to develop your game server.'''
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
            '''
            :param bucket: An Amazon S3 bucket identifier. This is the name of the S3 bucket.
            :param key: The name of the zip file that contains the build files or script files.
            :param role_arn: The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access the S3 bucket.
            :param object_version: The version of the file, if object versioning is turned on for the bucket. Amazon GameLift uses this information when retrieving files from your S3 bucket. To retrieve a specific version of the file, provide an object version. To retrieve the latest version of the file, do not set this parameter.

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
            '''An Amazon S3 bucket identifier.

            This is the name of the S3 bucket.

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
            '''The Amazon Resource Name (ARN) for an IAM role that allows Amazon GameLift to access the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-build-storagelocation.html#cfn-gamelift-build-storagelocation-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object_version(self) -> typing.Optional[builtins.str]:
            '''The version of the file, if object versioning is turned on for the bucket.

            Amazon GameLift uses this information when retrieving files from your S3 bucket. To retrieve a specific version of the file, provide an object version. To retrieve the latest version of the file, do not set this parameter.

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
        :param server_sdk_version: The Amazon GameLift Server SDK version used to develop your game server.
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
        '''The Amazon GameLift Server SDK version used to develop your game server.

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


@jsii.implements(_IInspectable_c2943556)
class CfnFleet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_gamelift.CfnFleet",
):
    '''The ``AWS::GameLift::Fleet`` resource creates an Amazon GameLift (GameLift) fleet to host custom game server or Realtime Servers.

    A fleet is a set of EC2 instances, configured with instructions to run game servers on each instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html
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
            build_id="buildId",
            certificate_configuration=gamelift.CfnFleet.CertificateConfigurationProperty(
                certificate_type="certificateType"
            ),
            compute_type="computeType",
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
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.CertificateConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        desired_ec2_instances: typing.Optional[jsii.Number] = None,
        ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFleet.IpPermissionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_instance_type: typing.Optional[builtins.str] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
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
        script_id: typing.Optional[builtins.str] = None,
        server_launch_parameters: typing.Optional[builtins.str] = None,
        server_launch_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        :param anywhere_configuration: Configuration for Anywhere fleet.
        :param build_id: A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        :param certificate_configuration: Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet. Amazon GameLift uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet. AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition. .. epigraph:: ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .
        :param compute_type: The type of compute resource used to host your game servers. You can use your own compute resources with Amazon GameLift Anywhere or use Amazon EC2 instances with managed Amazon GameLift.
        :param description: A description for the fleet.
        :param desired_ec2_instances: The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        :param ec2_inbound_permissions: The allowed IP address ranges and port settings that allow inbound traffic to access game sessions on this fleet. If the fleet is hosting a custom game build, this property must be set before players can connect to game sessions. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges.
        :param ec2_instance_type: The Amazon GameLift-supported Amazon EC2 instance type to use for all fleet instances. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.
        :param fleet_type: Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This property cannot be changed after the fleet is created.
        :param instance_role_arn: A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the `IAM dashboard <https://docs.aws.amazon.com/iam/>`_ in the AWS Management Console . Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This property cannot be changed after the fleet is created.
        :param locations: A set of remote locations to deploy additional instances to and manage as part of the fleet. This parameter can only be used when creating fleets in AWS Regions that support multiple locations. You can add any Amazon GameLift-supported AWS Region as a remote location, in the form of an AWS Region code such as ``us-west-2`` . To create a fleet with instances in the home Region only, don't use this parameter. To use this parameter, Amazon GameLift requires you to use your home location in the request.
        :param log_paths: (deprecated) This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
        :param max_size: The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
        :param min_size: The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.
        :param new_game_session_protection_policy: The status of termination protection for active game sessions on the fleet. By default, this property is set to ``NoProtection`` . - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event. - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.
        :param peer_vpc_aws_account_id: Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
        :param peer_vpc_id: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .
        :param resource_creation_limit_policy: A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
        :param runtime_configuration: Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently. .. epigraph:: The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.
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
            build_id=build_id,
            certificate_configuration=certificate_configuration,
            compute_type=compute_type,
            description=description,
            desired_ec2_instances=desired_ec2_instances,
            ec2_inbound_permissions=ec2_inbound_permissions,
            ec2_instance_type=ec2_instance_type,
            fleet_type=fleet_type,
            instance_role_arn=instance_role_arn,
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
        '''Configuration for Anywhere fleet.'''
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
        '''The allowed IP address ranges and port settings that allow inbound traffic to access game sessions on this fleet.'''
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
        '''The Amazon GameLift-supported Amazon EC2 instance type to use for all fleet instances.'''
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
        '''A unique identifier for an IAM role that manages access to your AWS services.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceRoleArn"))

    @instance_role_arn.setter
    def instance_role_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7947f4ea6b160028fb5bbf20fcbd0cc9eb46ba122d737f3c792a6be5043d8577)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceRoleArn", value)

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
            '''Amazon GameLift Anywhere configuration options for your Anywhere fleets.

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
            '''Current resource capacity settings in a specified fleet or location.

            The location value might refer to a fleet's remote location or its home Region.

            *Related actions*

            `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ | `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ | `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

            :param desired_ec2_instances: The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits.
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

            This value must fall between the minimum and maximum size limits.

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
            '''A remote location where a multi-location fleet can deploy game servers for game hosting.

            :param location: An AWS Region code, such as ``us-west-2`` .
            :param location_capacity: Current resource capacity settings in a specified fleet or location. The location value might refer to a fleet's remote location or its home Region. *Related actions* `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ | `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ | `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

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
            '''Current resource capacity settings in a specified fleet or location.

            The location value might refer to a fleet's remote location or its home Region.

            *Related actions*

            `DescribeFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html>`_ | `DescribeFleetLocationCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html>`_ | `UpdateFleetCapacity <https://docs.aws.amazon.com/gamelift/latest/apireference/API_UpdateFleetCapacity.html>`_

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
            :param max_concurrent_game_session_activations: The number of game sessions in status ``ACTIVATING`` to allow on an instance. This setting limits the instance resources that can be used for new game activations at any one time.
            :param server_processes: A collection of server process configurations that identify what server processes to run on each instance in a fleet.

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
            '''The number of game sessions in status ``ACTIVATING`` to allow on an instance.

            This setting limits the instance resources that can be used for new game activations at any one time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-runtimeconfiguration.html#cfn-gamelift-fleet-runtimeconfiguration-maxconcurrentgamesessionactivations
            '''
            result = self._values.get("max_concurrent_game_session_activations")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_processes(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFleet.ServerProcessProperty"]]]]:
            '''A collection of server process configurations that identify what server processes to run on each instance in a fleet.

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

            :param concurrent_executions: The number of server processes using this configuration that run concurrently on each instance.
            :param launch_path: The location of a game build executable or the Realtime script file that contains the ``Init()`` function. Game builds and Realtime scripts are installed on instances at the root: - Windows (custom game builds only): ``C:\\game`` . Example: " ``C:\\game\\MyGame\\server.exe`` " - Linux: ``/local/game`` . Examples: " ``/local/game/MyGame/server.exe`` " or " ``/local/game/MyRealtimeScript.js`` "
            :param parameters: An optional list of parameters to pass to the server executable or Realtime script on launch.

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
            '''The number of server processes using this configuration that run concurrently on each instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-concurrentexecutions
            '''
            result = self._values.get("concurrent_executions")
            assert result is not None, "Required property 'concurrent_executions' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def launch_path(self) -> builtins.str:
            '''The location of a game build executable or the Realtime script file that contains the ``Init()`` function.

            Game builds and Realtime scripts are installed on instances at the root:

            - Windows (custom game builds only): ``C:\\game`` . Example: " ``C:\\game\\MyGame\\server.exe`` "
            - Linux: ``/local/game`` . Examples: " ``/local/game/MyGame/server.exe`` " or " ``/local/game/MyRealtimeScript.js`` "

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-gamelift-fleet-serverprocess.html#cfn-gamelift-fleet-serverprocess-launchpath
            '''
            result = self._values.get("launch_path")
            assert result is not None, "Required property 'launch_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def parameters(self) -> typing.Optional[builtins.str]:
            '''An optional list of parameters to pass to the server executable or Realtime script on launch.

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
    jsii_type="aws-cdk-lib.aws_gamelift.CfnFleetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "anywhere_configuration": "anywhereConfiguration",
        "build_id": "buildId",
        "certificate_configuration": "certificateConfiguration",
        "compute_type": "computeType",
        "description": "description",
        "desired_ec2_instances": "desiredEc2Instances",
        "ec2_inbound_permissions": "ec2InboundPermissions",
        "ec2_instance_type": "ec2InstanceType",
        "fleet_type": "fleetType",
        "instance_role_arn": "instanceRoleArn",
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
        build_id: typing.Optional[builtins.str] = None,
        certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        compute_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        desired_ec2_instances: typing.Optional[jsii.Number] = None,
        ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ec2_instance_type: typing.Optional[builtins.str] = None,
        fleet_type: typing.Optional[builtins.str] = None,
        instance_role_arn: typing.Optional[builtins.str] = None,
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
        script_id: typing.Optional[builtins.str] = None,
        server_launch_parameters: typing.Optional[builtins.str] = None,
        server_launch_path: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFleet``.

        :param name: A descriptive label that is associated with a fleet. Fleet names do not need to be unique.
        :param anywhere_configuration: Configuration for Anywhere fleet.
        :param build_id: A unique identifier for a build to be deployed on the new fleet. If you are deploying the fleet with a custom game build, you must specify this property. The build must have been successfully uploaded to Amazon GameLift and be in a ``READY`` status. This fleet setting cannot be changed once the fleet is created.
        :param certificate_configuration: Prompts Amazon GameLift to generate a TLS/SSL certificate for the fleet. Amazon GameLift uses the certificates to encrypt traffic between game clients and the game servers running on Amazon GameLift. By default, the ``CertificateConfiguration`` is ``DISABLED`` . You can't change this property after you create the fleet. AWS Certificate Manager (ACM) certificates expire after 13 months. Certificate expiration can cause fleets to fail, preventing players from connecting to instances in the fleet. We recommend you replace fleets before 13 months, consider using fleet aliases for a smooth transition. .. epigraph:: ACM isn't available in all AWS regions. A fleet creation request with certificate generation enabled in an unsupported Region, fails with a 4xx error. For more information about the supported Regions, see `Supported Regions <https://docs.aws.amazon.com/acm/latest/userguide/acm-regions.html>`_ in the *AWS Certificate Manager User Guide* .
        :param compute_type: The type of compute resource used to host your game servers. You can use your own compute resources with Amazon GameLift Anywhere or use Amazon EC2 instances with managed Amazon GameLift.
        :param description: A description for the fleet.
        :param desired_ec2_instances: The number of EC2 instances that you want this fleet to host. When creating a new fleet, GameLift automatically sets this value to "1" and initiates a single instance. Once the fleet is active, update this value to trigger GameLift to add or remove instances from the fleet.
        :param ec2_inbound_permissions: The allowed IP address ranges and port settings that allow inbound traffic to access game sessions on this fleet. If the fleet is hosting a custom game build, this property must be set before players can connect to game sessions. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges.
        :param ec2_instance_type: The Amazon GameLift-supported Amazon EC2 instance type to use for all fleet instances. Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.
        :param fleet_type: Indicates whether to use On-Demand or Spot instances for this fleet. By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This property cannot be changed after the fleet is created.
        :param instance_role_arn: A unique identifier for an IAM role that manages access to your AWS services. With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the `IAM dashboard <https://docs.aws.amazon.com/iam/>`_ in the AWS Management Console . Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This property cannot be changed after the fleet is created.
        :param locations: A set of remote locations to deploy additional instances to and manage as part of the fleet. This parameter can only be used when creating fleets in AWS Regions that support multiple locations. You can add any Amazon GameLift-supported AWS Region as a remote location, in the form of an AWS Region code such as ``us-west-2`` . To create a fleet with instances in the home Region only, don't use this parameter. To use this parameter, Amazon GameLift requires you to use your home location in the request.
        :param log_paths: (deprecated) This parameter is no longer used. When hosting a custom game build, specify where Amazon GameLift should store log files using the Amazon GameLift server API call ProcessReady()
        :param max_size: The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.
        :param metric_groups: The name of an AWS CloudWatch metric group to add this fleet to. A metric group is used to aggregate the metrics for multiple fleets. You can specify an existing metric group name or set a new name to create a new metric group. A fleet can be included in only one metric group at a time.
        :param min_size: The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.
        :param new_game_session_protection_policy: The status of termination protection for active game sessions on the fleet. By default, this property is set to ``NoProtection`` . - *NoProtection* - Game sessions can be terminated during active gameplay as a result of a scale-down event. - *FullProtection* - Game sessions in ``ACTIVE`` status cannot be terminated during a scale-down event.
        :param peer_vpc_aws_account_id: Used when peering your Amazon GameLift fleet with a VPC, the unique identifier for the AWS account that owns the VPC. You can find your account ID in the AWS Management Console under account settings.
        :param peer_vpc_id: A unique identifier for a VPC with resources to be accessed by your Amazon GameLift fleet. The VPC must be in the same Region as your fleet. To look up a VPC ID, use the `VPC Dashboard <https://docs.aws.amazon.com/vpc/>`_ in the AWS Management Console . Learn more about VPC peering in `VPC Peering with Amazon GameLift Fleets <https://docs.aws.amazon.com/gamelift/latest/developerguide/vpc-peering.html>`_ .
        :param resource_creation_limit_policy: A policy that limits the number of game sessions that an individual player can create on instances in this fleet within a specified span of time.
        :param runtime_configuration: Instructions for how to launch and maintain server processes on instances in the fleet. The runtime configuration defines one or more server process configurations, each identifying a build executable or Realtime script file and the number of processes of that type to run concurrently. .. epigraph:: The ``RuntimeConfiguration`` parameter is required unless the fleet is being configured using the older parameters ``ServerLaunchPath`` and ``ServerLaunchParameters`` , which are still supported for backward compatibility.
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
                build_id="buildId",
                certificate_configuration=gamelift.CfnFleet.CertificateConfigurationProperty(
                    certificate_type="certificateType"
                ),
                compute_type="computeType",
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
                script_id="scriptId",
                server_launch_parameters="serverLaunchParameters",
                server_launch_path="serverLaunchPath"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a51a418ba5b606bdfc45dc50c3172e280a12e078a7392f3258d5d329e037a55)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument anywhere_configuration", value=anywhere_configuration, expected_type=type_hints["anywhere_configuration"])
            check_type(argname="argument build_id", value=build_id, expected_type=type_hints["build_id"])
            check_type(argname="argument certificate_configuration", value=certificate_configuration, expected_type=type_hints["certificate_configuration"])
            check_type(argname="argument compute_type", value=compute_type, expected_type=type_hints["compute_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument desired_ec2_instances", value=desired_ec2_instances, expected_type=type_hints["desired_ec2_instances"])
            check_type(argname="argument ec2_inbound_permissions", value=ec2_inbound_permissions, expected_type=type_hints["ec2_inbound_permissions"])
            check_type(argname="argument ec2_instance_type", value=ec2_instance_type, expected_type=type_hints["ec2_instance_type"])
            check_type(argname="argument fleet_type", value=fleet_type, expected_type=type_hints["fleet_type"])
            check_type(argname="argument instance_role_arn", value=instance_role_arn, expected_type=type_hints["instance_role_arn"])
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
            check_type(argname="argument script_id", value=script_id, expected_type=type_hints["script_id"])
            check_type(argname="argument server_launch_parameters", value=server_launch_parameters, expected_type=type_hints["server_launch_parameters"])
            check_type(argname="argument server_launch_path", value=server_launch_path, expected_type=type_hints["server_launch_path"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if anywhere_configuration is not None:
            self._values["anywhere_configuration"] = anywhere_configuration
        if build_id is not None:
            self._values["build_id"] = build_id
        if certificate_configuration is not None:
            self._values["certificate_configuration"] = certificate_configuration
        if compute_type is not None:
            self._values["compute_type"] = compute_type
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
        '''Configuration for Anywhere fleet.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-anywhereconfiguration
        '''
        result = self._values.get("anywhere_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFleet.AnywhereConfigurationProperty]], result)

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

        You can use your own compute resources with Amazon GameLift Anywhere or use Amazon EC2 instances with managed Amazon GameLift.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-computetype
        '''
        result = self._values.get("compute_type")
        return typing.cast(typing.Optional[builtins.str], result)

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
        '''The allowed IP address ranges and port settings that allow inbound traffic to access game sessions on this fleet.

        If the fleet is hosting a custom game build, this property must be set before players can connect to game sessions. For Realtime Servers fleets, Amazon GameLift automatically sets TCP and UDP ranges.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2inboundpermissions
        '''
        result = self._values.get("ec2_inbound_permissions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.IpPermissionProperty]]]], result)

    @builtins.property
    def ec2_instance_type(self) -> typing.Optional[builtins.str]:
        '''The Amazon GameLift-supported Amazon EC2 instance type to use for all fleet instances.

        Instance type determines the computing resources that will be used to host your game servers, including CPU, memory, storage, and networking capacity. See `Amazon Elastic Compute Cloud Instance Types <https://docs.aws.amazon.com/ec2/instance-types/>`_ for detailed descriptions of Amazon EC2 instance types.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-ec2instancetype
        '''
        result = self._values.get("ec2_instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def fleet_type(self) -> typing.Optional[builtins.str]:
        '''Indicates whether to use On-Demand or Spot instances for this fleet.

        By default, this property is set to ``ON_DEMAND`` . Learn more about when to use `On-Demand versus Spot Instances <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html#gamelift-ec2-instances-spot>`_ . This property cannot be changed after the fleet is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-fleettype
        '''
        result = self._values.get("fleet_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_role_arn(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for an IAM role that manages access to your AWS services.

        With an instance role ARN set, any application that runs on an instance in this fleet can assume the role, including install scripts, server processes, and daemons (background processes). Create a role or look up a role's ARN by using the `IAM dashboard <https://docs.aws.amazon.com/iam/>`_ in the AWS Management Console . Learn more about using on-box credentials for your game servers at `Access external resources from a game server <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-resources.html>`_ . This property cannot be changed after the fleet is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-fleet.html#cfn-gamelift-fleet-instancerolearn
        '''
        result = self._values.get("instance_role_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFleet.LocationConfigurationProperty]]]]:
        '''A set of remote locations to deploy additional instances to and manage as part of the fleet.

        This parameter can only be used when creating fleets in AWS Regions that support multiple locations. You can add any Amazon GameLift-supported AWS Region as a remote location, in the form of an AWS Region code such as ``us-west-2`` . To create a fleet with instances in the home Region only, don't use this parameter.

        To use this parameter, Amazon GameLift requires you to use your home location in the request.

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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
            '''A fleet or alias designated in a game session queue.

            Queues fulfill requests for new game sessions by placing a new game session on any of the queue's destinations.

            :param destination_arn: The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias. ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

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
            '''The Amazon Resource Name (ARN) that is assigned to fleet or fleet alias.

            ARNs, which include a fleet ID or alias ID and a Region name, provide a unique identifier across all Regions.

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
    '''Creates a custom location for use in an Anywhere fleet.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html
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
        :param location_name: The location's name.
        :param tags: An array of key-value pairs to apply to this resource.
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
        '''
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
        '''The location's name.'''
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
        '''An array of key-value pairs to apply to this resource.'''
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

        :param location_name: The location's name.
        :param tags: An array of key-value pairs to apply to this resource.

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
        '''The location's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-gamelift-location.html#cfn-gamelift-location-locationname
        '''
        result = self._values.get("location_name")
        assert result is not None, "Required property 'location_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

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
        custom_event_data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flex_match_mode: typing.Optional[builtins.str] = None,
        game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMatchmakingConfiguration.GamePropertyProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        game_session_data: typing.Optional[builtins.str] = None,
        game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_target: typing.Optional[builtins.str] = None,
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
        :param custom_event_data: Information to add to all events related to the matchmaking configuration.
        :param description: A description for the matchmaking configuration.
        :param flex_match_mode: Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution. - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event. - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift queue to start a game session for the match.
        :param game_properties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_data: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_queue_arns: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.
        :param notification_target: An SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.
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
            custom_event_data=custom_event_data,
            description=description,
            flex_match_mode=flex_match_mode,
            game_properties=game_properties,
            game_session_data=game_session_data,
            game_session_queue_arns=game_session_queue_arns,
            notification_target=notification_target,
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
            '''Set of key-value pairs that contain information about a game session.

            When included in a game session request, these properties communicate details to be used when setting up the new game session. For example, a game property might specify a game mode, level, or map. Game properties are passed to the game server process when initiating a new game session. For more information, see the `Amazon GameLift Developer Guide <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-client-api.html#gamelift-sdk-client-api-create>`_ .

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
        "custom_event_data": "customEventData",
        "description": "description",
        "flex_match_mode": "flexMatchMode",
        "game_properties": "gameProperties",
        "game_session_data": "gameSessionData",
        "game_session_queue_arns": "gameSessionQueueArns",
        "notification_target": "notificationTarget",
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
        custom_event_data: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        flex_match_mode: typing.Optional[builtins.str] = None,
        game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        game_session_data: typing.Optional[builtins.str] = None,
        game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        notification_target: typing.Optional[builtins.str] = None,
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
        :param custom_event_data: Information to add to all events related to the matchmaking configuration.
        :param description: A description for the matchmaking configuration.
        :param flex_match_mode: Indicates whether this matchmaking configuration is being used with Amazon GameLift hosting or as a standalone matchmaking solution. - *STANDALONE* - FlexMatch forms matches and returns match information, including players and team assignments, in a `MatchmakingSucceeded <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-events.html#match-events-matchmakingsucceeded>`_ event. - *WITH_QUEUE* - FlexMatch forms matches and uses the specified Amazon GameLift queue to start a game session for the match.
        :param game_properties: A set of custom properties for a game session, formatted as key-value pairs. These properties are passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_data: A set of custom game session properties, formatted as a single string value. This data is passed to a game server process with a request to start a new game session. See `Start a Game Session <https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-sdk-server-api.html#gamelift-sdk-server-startsession>`_ . This parameter is not used if ``FlexMatchMode`` is set to ``STANDALONE`` .
        :param game_session_queue_arns: The Amazon Resource Name ( `ARN <https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html>`_ ) that is assigned to a Amazon GameLift game session queue resource and uniquely identifies it. ARNs are unique across all Regions. Format is ``arn:aws:gamelift:<region>::gamesessionqueue/<queue name>`` . Queues can be located in any Region. Queues are used to start new Amazon GameLift-hosted game sessions for matches that are created with this matchmaking configuration. If ``FlexMatchMode`` is set to ``STANDALONE`` , do not set this parameter.
        :param notification_target: An SNS topic ARN that is set up to receive matchmaking notifications. See `Setting up notifications for matchmaking <https://docs.aws.amazon.com/gamelift/latest/flexmatchguide/match-notification.html>`_ for more information.
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
            check_type(argname="argument custom_event_data", value=custom_event_data, expected_type=type_hints["custom_event_data"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flex_match_mode", value=flex_match_mode, expected_type=type_hints["flex_match_mode"])
            check_type(argname="argument game_properties", value=game_properties, expected_type=type_hints["game_properties"])
            check_type(argname="argument game_session_data", value=game_session_data, expected_type=type_hints["game_session_data"])
            check_type(argname="argument game_session_queue_arns", value=game_session_queue_arns, expected_type=type_hints["game_session_queue_arns"])
            check_type(argname="argument notification_target", value=notification_target, expected_type=type_hints["notification_target"])
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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

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
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''A unique identifier for a Realtime script.

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

def _typecheckingstub__21fe09a90444788b3c862f454214d4e160757c9b02d0598d282f68b7f79d749f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    desired_ec2_instances: typing.Optional[jsii.Number] = None,
    ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_type: typing.Optional[builtins.str] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
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

def _typecheckingstub__fc845ade67d7aff6536f53651c26f049fc04883863968a83da759b79b0a6d035(
    *,
    concurrent_executions: jsii.Number,
    launch_path: builtins.str,
    parameters: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a51a418ba5b606bdfc45dc50c3172e280a12e078a7392f3258d5d329e037a55(
    *,
    name: builtins.str,
    anywhere_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.AnywhereConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    build_id: typing.Optional[builtins.str] = None,
    certificate_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.CertificateConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    compute_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    desired_ec2_instances: typing.Optional[jsii.Number] = None,
    ec2_inbound_permissions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFleet.IpPermissionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_type: typing.Optional[builtins.str] = None,
    fleet_type: typing.Optional[builtins.str] = None,
    instance_role_arn: typing.Optional[builtins.str] = None,
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
    custom_event_data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    flex_match_mode: typing.Optional[builtins.str] = None,
    game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    game_session_data: typing.Optional[builtins.str] = None,
    game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_target: typing.Optional[builtins.str] = None,
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
    custom_event_data: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    flex_match_mode: typing.Optional[builtins.str] = None,
    game_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMatchmakingConfiguration.GamePropertyProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    game_session_data: typing.Optional[builtins.str] = None,
    game_session_queue_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    notification_target: typing.Optional[builtins.str] = None,
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
