'''
# AWS::CodeStarConnections Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_codestarconnections as codestarconnections
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for CodeStarConnections construct libraries](https://constructs.dev/search?q=codestarconnections)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::CodeStarConnections resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeStarConnections.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::CodeStarConnections](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_CodeStarConnections.html).

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
    ITaggable as _ITaggable_36806126,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnConnection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codestarconnections.CfnConnection",
):
    '''The AWS::CodeStarConnections::Connection resource can be used to connect external source providers with services like AWS CodePipeline .

    *Note:* A connection created through AWS CloudFormation is in ``PENDING`` status by default. You can make its status ``AVAILABLE`` by updating the connection in the console.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html
    :cloudformationResource: AWS::CodeStarConnections::Connection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codestarconnections as codestarconnections
        
        cfn_connection = codestarconnections.CfnConnection(self, "MyCfnConnection",
            connection_name="connectionName",
        
            # the properties below are optional
            host_arn="hostArn",
            provider_type="providerType",
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
        connection_name: builtins.str,
        host_arn: typing.Optional[builtins.str] = None,
        provider_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connection_name: The name of the connection. Connection names must be unique in an AWS account .
        :param host_arn: The Amazon Resource Name (ARN) of the host associated with the connection.
        :param provider_type: The name of the external provider where your third-party code repository is configured.
        :param tags: Specifies the tags applied to the resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b31f55bcd270757c56f65f68558594d1908e1956199257e40b61ad1328525c3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectionProps(
            connection_name=connection_name,
            host_arn=host_arn,
            provider_type=provider_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35ee59ed14cc3a52d66e46db3ccc3d36ea0c6b5133b23c09d6f13279a0159048)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7439e44f0496a9ba58cb0741afc532422c7c595d46da2e7f6cc4e0b67c3387e9)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionArn")
    def attr_connection_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connection.

        The ARN is used as the connection reference when the connection is shared between AWS services. For example: ``arn:aws:codestar-connections:us-west-2:123456789012:connection/39e4c34d-e13a-4e94-a886-ea67651bf042`` .

        :cloudformationAttribute: ConnectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectionStatus")
    def attr_connection_status(self) -> builtins.str:
        '''The current status of the connection.

        For example: ``PENDING`` , ``AVAILABLE`` , or ``ERROR`` .

        :cloudformationAttribute: ConnectionStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectionStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerAccountId")
    def attr_owner_account_id(self) -> builtins.str:
        '''The AWS account ID of the owner of the connection.

        For Bitbucket, this is the account ID of the owner of the Bitbucket repository. For example: ``123456789012`` .

        :cloudformationAttribute: OwnerAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerAccountId"))

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
    @jsii.member(jsii_name="connectionName")
    def connection_name(self) -> builtins.str:
        '''The name of the connection.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionName"))

    @connection_name.setter
    def connection_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c74ec66d28c8d03c7f48d90efa65701a9b502cde3cf8e62b1f7d4b30a589a83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionName", value)

    @builtins.property
    @jsii.member(jsii_name="hostArn")
    def host_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the host associated with the connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostArn"))

    @host_arn.setter
    def host_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06a35f319001e96b6f2b20bfbe5dae6f255ba9622170543150326f886683e443)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostArn", value)

    @builtins.property
    @jsii.member(jsii_name="providerType")
    def provider_type(self) -> typing.Optional[builtins.str]:
        '''The name of the external provider where your third-party code repository is configured.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "providerType"))

    @provider_type.setter
    def provider_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1aca832648768d4bedc95e0dd9eb0553af2e55cd113046f9922f476f7c18ddd7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "providerType", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the tags applied to the resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4559e698887f8e503dde8843ff791284d6d9949c323e9ac7625231409f77297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarconnections.CfnConnectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_name": "connectionName",
        "host_arn": "hostArn",
        "provider_type": "providerType",
        "tags": "tags",
    },
)
class CfnConnectionProps:
    def __init__(
        self,
        *,
        connection_name: builtins.str,
        host_arn: typing.Optional[builtins.str] = None,
        provider_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnection``.

        :param connection_name: The name of the connection. Connection names must be unique in an AWS account .
        :param host_arn: The Amazon Resource Name (ARN) of the host associated with the connection.
        :param provider_type: The name of the external provider where your third-party code repository is configured.
        :param tags: Specifies the tags applied to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarconnections as codestarconnections
            
            cfn_connection_props = codestarconnections.CfnConnectionProps(
                connection_name="connectionName",
            
                # the properties below are optional
                host_arn="hostArn",
                provider_type="providerType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c17bc8ee185245b98d73051c96c32d31990b026c92635744b3a690aba461026)
            check_type(argname="argument connection_name", value=connection_name, expected_type=type_hints["connection_name"])
            check_type(argname="argument host_arn", value=host_arn, expected_type=type_hints["host_arn"])
            check_type(argname="argument provider_type", value=provider_type, expected_type=type_hints["provider_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_name": connection_name,
        }
        if host_arn is not None:
            self._values["host_arn"] = host_arn
        if provider_type is not None:
            self._values["provider_type"] = provider_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connection_name(self) -> builtins.str:
        '''The name of the connection.

        Connection names must be unique in an AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-connectionname
        '''
        result = self._values.get("connection_name")
        assert result is not None, "Required property 'connection_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def host_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the host associated with the connection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-hostarn
        '''
        result = self._values.get("host_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def provider_type(self) -> typing.Optional[builtins.str]:
        '''The name of the external provider where your third-party code repository is configured.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-providertype
        '''
        result = self._values.get("provider_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Specifies the tags applied to the resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-connection.html#cfn-codestarconnections-connection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnRepositoryLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codestarconnections.CfnRepositoryLink",
):
    '''Information about the repository link resource, such as the repository link ARN, the associated connection ARN, encryption key ARN, and owner ID.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html
    :cloudformationResource: AWS::CodeStarConnections::RepositoryLink
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codestarconnections as codestarconnections
        
        cfn_repository_link = codestarconnections.CfnRepositoryLink(self, "MyCfnRepositoryLink",
            connection_arn="connectionArn",
            owner_id="ownerId",
            repository_name="repositoryName",
        
            # the properties below are optional
            encryption_key_arn="encryptionKeyArn",
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
        connection_arn: builtins.str,
        owner_id: builtins.str,
        repository_name: builtins.str,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connection_arn: The Amazon Resource Name (ARN) of the connection associated with the repository link.
        :param owner_id: The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.
        :param repository_name: The name of the repository associated with the repository link.
        :param encryption_key_arn: The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.
        :param tags: The tags for the repository to be associated with the repository link.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdf48b0dfdec692a05fb0520b1d1c224a8c2e2c7f2613c7a1e42179efa8707cc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRepositoryLinkProps(
            connection_arn=connection_arn,
            owner_id=owner_id,
            repository_name=repository_name,
            encryption_key_arn=encryption_key_arn,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c12cbe13f83fd7ed50821e79d7ce9f67351ce7923283498bb237f85641899258)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b12f3011d520668189d58b24e4e9f8e0f5155af7ad40e14f399a0462ecebb0d4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProviderType")
    def attr_provider_type(self) -> builtins.str:
        '''The name of the external provider where your third-party code repository is configured.

        :cloudformationAttribute: ProviderType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProviderType"))

    @builtins.property
    @jsii.member(jsii_name="attrRepositoryLinkArn")
    def attr_repository_link_arn(self) -> builtins.str:
        '''A unique Amazon Resource Name (ARN) to designate the repository link.

        :cloudformationAttribute: RepositoryLinkArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRepositoryLinkArn"))

    @builtins.property
    @jsii.member(jsii_name="attrRepositoryLinkId")
    def attr_repository_link_id(self) -> builtins.str:
        '''A UUID that uniquely identifies the RepositoryLink.

        :cloudformationAttribute: RepositoryLinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRepositoryLinkId"))

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
    @jsii.member(jsii_name="connectionArn")
    def connection_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connection associated with the repository link.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionArn"))

    @connection_arn.setter
    def connection_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8876457702f59ff1032085cd26b110c8d6e7fae6bbd6adee023301843b8dd66)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionArn", value)

    @builtins.property
    @jsii.member(jsii_name="ownerId")
    def owner_id(self) -> builtins.str:
        '''The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.'''
        return typing.cast(builtins.str, jsii.get(self, "ownerId"))

    @owner_id.setter
    def owner_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__663677d537f429830084c0b8c2eb0fb3120802794afada996d2845193413d150)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ownerId", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryName")
    def repository_name(self) -> builtins.str:
        '''The name of the repository associated with the repository link.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryName"))

    @repository_name.setter
    def repository_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ada27515939c416886b3726d8504ee6351dee56bf23a317efce0cbf60225bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryName", value)

    @builtins.property
    @jsii.member(jsii_name="encryptionKeyArn")
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encryptionKeyArn"))

    @encryption_key_arn.setter
    def encryption_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72d6898194f3a2786d5d0888d37cfcf4f3c06554c8dcab6f23c16f81ff241b9c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryptionKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the repository to be associated with the repository link.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3169870757b800cdac6097cbe92bb05d72aa36383fc08c2d273a2ef98bdfb961)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarconnections.CfnRepositoryLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_arn": "connectionArn",
        "owner_id": "ownerId",
        "repository_name": "repositoryName",
        "encryption_key_arn": "encryptionKeyArn",
        "tags": "tags",
    },
)
class CfnRepositoryLinkProps:
    def __init__(
        self,
        *,
        connection_arn: builtins.str,
        owner_id: builtins.str,
        repository_name: builtins.str,
        encryption_key_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRepositoryLink``.

        :param connection_arn: The Amazon Resource Name (ARN) of the connection associated with the repository link.
        :param owner_id: The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.
        :param repository_name: The name of the repository associated with the repository link.
        :param encryption_key_arn: The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.
        :param tags: The tags for the repository to be associated with the repository link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarconnections as codestarconnections
            
            cfn_repository_link_props = codestarconnections.CfnRepositoryLinkProps(
                connection_arn="connectionArn",
                owner_id="ownerId",
                repository_name="repositoryName",
            
                # the properties below are optional
                encryption_key_arn="encryptionKeyArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a059e8a38cb53db73841fe9a927fc29f036c7d50538d54c9a91ff9cb6d714763)
            check_type(argname="argument connection_arn", value=connection_arn, expected_type=type_hints["connection_arn"])
            check_type(argname="argument owner_id", value=owner_id, expected_type=type_hints["owner_id"])
            check_type(argname="argument repository_name", value=repository_name, expected_type=type_hints["repository_name"])
            check_type(argname="argument encryption_key_arn", value=encryption_key_arn, expected_type=type_hints["encryption_key_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_arn": connection_arn,
            "owner_id": owner_id,
            "repository_name": repository_name,
        }
        if encryption_key_arn is not None:
            self._values["encryption_key_arn"] = encryption_key_arn
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def connection_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connection associated with the repository link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-connectionarn
        '''
        result = self._values.get("connection_arn")
        assert result is not None, "Required property 'connection_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def owner_id(self) -> builtins.str:
        '''The owner ID for the repository associated with the repository link, such as the owner ID in GitHub.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-ownerid
        '''
        result = self._values.get("owner_id")
        assert result is not None, "Required property 'owner_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_name(self) -> builtins.str:
        '''The name of the repository associated with the repository link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-repositoryname
        '''
        result = self._values.get("repository_name")
        assert result is not None, "Required property 'repository_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def encryption_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the encryption key for the repository associated with the repository link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-encryptionkeyarn
        '''
        result = self._values.get("encryption_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags for the repository to be associated with the repository link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-repositorylink.html#cfn-codestarconnections-repositorylink-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRepositoryLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnSyncConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_codestarconnections.CfnSyncConfiguration",
):
    '''Information, such as repository, branch, provider, and resource names for a specific sync configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html
    :cloudformationResource: AWS::CodeStarConnections::SyncConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_codestarconnections as codestarconnections
        
        cfn_sync_configuration = codestarconnections.CfnSyncConfiguration(self, "MyCfnSyncConfiguration",
            branch="branch",
            config_file="configFile",
            repository_link_id="repositoryLinkId",
            resource_name="resourceName",
            role_arn="roleArn",
            sync_type="syncType",
        
            # the properties below are optional
            publish_deployment_status="publishDeploymentStatus",
            trigger_resource_update_on="triggerResourceUpdateOn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        branch: builtins.str,
        config_file: builtins.str,
        repository_link_id: builtins.str,
        resource_name: builtins.str,
        role_arn: builtins.str,
        sync_type: builtins.str,
        publish_deployment_status: typing.Optional[builtins.str] = None,
        trigger_resource_update_on: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param branch: The branch associated with a specific sync configuration.
        :param config_file: The file path to the configuration file associated with a specific sync configuration. The path should point to an actual file in the sync configurations linked repository.
        :param repository_link_id: The ID of the repository link associated with a specific sync configuration.
        :param resource_name: The name of the connection resource associated with a specific sync configuration.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.
        :param sync_type: The type of sync for a specific sync configuration.
        :param publish_deployment_status: Whether to enable or disable publishing of deployment status to source providers.
        :param trigger_resource_update_on: When to trigger Git sync to begin the stack update.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c8a904149088ca3c954aba811ae03db6bb18a34b324a10bedb2331c6f876b12)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSyncConfigurationProps(
            branch=branch,
            config_file=config_file,
            repository_link_id=repository_link_id,
            resource_name=resource_name,
            role_arn=role_arn,
            sync_type=sync_type,
            publish_deployment_status=publish_deployment_status,
            trigger_resource_update_on=trigger_resource_update_on,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba0212b5f34dcefde1cc911722704bbe375f7da6cc5664daf19a6b30de041172)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c4c5e0bde34dbb71b2c1dca1aa91236c78ce6f4f9cce380b40392d95f60f5436)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrOwnerId")
    def attr_owner_id(self) -> builtins.str:
        '''The owner ID for the repository associated with a specific sync configuration, such as the owner ID in GitHub.

        :cloudformationAttribute: OwnerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOwnerId"))

    @builtins.property
    @jsii.member(jsii_name="attrProviderType")
    def attr_provider_type(self) -> builtins.str:
        '''The name of the external provider where your third-party code repository is configured.

        :cloudformationAttribute: ProviderType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProviderType"))

    @builtins.property
    @jsii.member(jsii_name="attrRepositoryName")
    def attr_repository_name(self) -> builtins.str:
        '''The name of the repository that is being synced to.

        :cloudformationAttribute: RepositoryName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRepositoryName"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="branch")
    def branch(self) -> builtins.str:
        '''The branch associated with a specific sync configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "branch"))

    @branch.setter
    def branch(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41b151b4d5881562900d975603bfc5389d4bab87c50dc36536cd3003bc4d791b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "branch", value)

    @builtins.property
    @jsii.member(jsii_name="configFile")
    def config_file(self) -> builtins.str:
        '''The file path to the configuration file associated with a specific sync configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "configFile"))

    @config_file.setter
    def config_file(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f0211209d25f8536c8c1167936be2d2cebd2bf3ae3224a101371fea54254429)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configFile", value)

    @builtins.property
    @jsii.member(jsii_name="repositoryLinkId")
    def repository_link_id(self) -> builtins.str:
        '''The ID of the repository link associated with a specific sync configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "repositoryLinkId"))

    @repository_link_id.setter
    def repository_link_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d960d0547e481ad4fe89040e67311dc4f418ffe323ada1ffc6b3f130569e8b86)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "repositoryLinkId", value)

    @builtins.property
    @jsii.member(jsii_name="resourceName")
    def resource_name(self) -> builtins.str:
        '''The name of the connection resource associated with a specific sync configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceName"))

    @resource_name.setter
    def resource_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c6a186f209425b22ba86b10b6714304808f4cb3f878507a70f06e8d9378dac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceName", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c33417a47e49bf925d46ca39cc6ac66fa3d450e28ab0ba781d48878d680eb99b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="syncType")
    def sync_type(self) -> builtins.str:
        '''The type of sync for a specific sync configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "syncType"))

    @sync_type.setter
    def sync_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a7aa9e776fee9e7c2ac12a6821ca735b73efe0013da11eacba140d600678d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "syncType", value)

    @builtins.property
    @jsii.member(jsii_name="publishDeploymentStatus")
    def publish_deployment_status(self) -> typing.Optional[builtins.str]:
        '''Whether to enable or disable publishing of deployment status to source providers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "publishDeploymentStatus"))

    @publish_deployment_status.setter
    def publish_deployment_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ee8fea36d4094e0ac90eb20686a90d517ffcde16742313ecf04785324f10c50)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publishDeploymentStatus", value)

    @builtins.property
    @jsii.member(jsii_name="triggerResourceUpdateOn")
    def trigger_resource_update_on(self) -> typing.Optional[builtins.str]:
        '''When to trigger Git sync to begin the stack update.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "triggerResourceUpdateOn"))

    @trigger_resource_update_on.setter
    def trigger_resource_update_on(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3019909980645630665fb7da740e906ba748d5a370476cef6024471869dea97b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerResourceUpdateOn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_codestarconnections.CfnSyncConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "branch": "branch",
        "config_file": "configFile",
        "repository_link_id": "repositoryLinkId",
        "resource_name": "resourceName",
        "role_arn": "roleArn",
        "sync_type": "syncType",
        "publish_deployment_status": "publishDeploymentStatus",
        "trigger_resource_update_on": "triggerResourceUpdateOn",
    },
)
class CfnSyncConfigurationProps:
    def __init__(
        self,
        *,
        branch: builtins.str,
        config_file: builtins.str,
        repository_link_id: builtins.str,
        resource_name: builtins.str,
        role_arn: builtins.str,
        sync_type: builtins.str,
        publish_deployment_status: typing.Optional[builtins.str] = None,
        trigger_resource_update_on: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnSyncConfiguration``.

        :param branch: The branch associated with a specific sync configuration.
        :param config_file: The file path to the configuration file associated with a specific sync configuration. The path should point to an actual file in the sync configurations linked repository.
        :param repository_link_id: The ID of the repository link associated with a specific sync configuration.
        :param resource_name: The name of the connection resource associated with a specific sync configuration.
        :param role_arn: The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.
        :param sync_type: The type of sync for a specific sync configuration.
        :param publish_deployment_status: Whether to enable or disable publishing of deployment status to source providers.
        :param trigger_resource_update_on: When to trigger Git sync to begin the stack update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_codestarconnections as codestarconnections
            
            cfn_sync_configuration_props = codestarconnections.CfnSyncConfigurationProps(
                branch="branch",
                config_file="configFile",
                repository_link_id="repositoryLinkId",
                resource_name="resourceName",
                role_arn="roleArn",
                sync_type="syncType",
            
                # the properties below are optional
                publish_deployment_status="publishDeploymentStatus",
                trigger_resource_update_on="triggerResourceUpdateOn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea619fc4ca98271e7e2c90f35350d4af5c1f35168a8e4cdc7191c86cfcfff5ce)
            check_type(argname="argument branch", value=branch, expected_type=type_hints["branch"])
            check_type(argname="argument config_file", value=config_file, expected_type=type_hints["config_file"])
            check_type(argname="argument repository_link_id", value=repository_link_id, expected_type=type_hints["repository_link_id"])
            check_type(argname="argument resource_name", value=resource_name, expected_type=type_hints["resource_name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument sync_type", value=sync_type, expected_type=type_hints["sync_type"])
            check_type(argname="argument publish_deployment_status", value=publish_deployment_status, expected_type=type_hints["publish_deployment_status"])
            check_type(argname="argument trigger_resource_update_on", value=trigger_resource_update_on, expected_type=type_hints["trigger_resource_update_on"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "branch": branch,
            "config_file": config_file,
            "repository_link_id": repository_link_id,
            "resource_name": resource_name,
            "role_arn": role_arn,
            "sync_type": sync_type,
        }
        if publish_deployment_status is not None:
            self._values["publish_deployment_status"] = publish_deployment_status
        if trigger_resource_update_on is not None:
            self._values["trigger_resource_update_on"] = trigger_resource_update_on

    @builtins.property
    def branch(self) -> builtins.str:
        '''The branch associated with a specific sync configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-branch
        '''
        result = self._values.get("branch")
        assert result is not None, "Required property 'branch' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def config_file(self) -> builtins.str:
        '''The file path to the configuration file associated with a specific sync configuration.

        The path should point to an actual file in the sync configurations linked repository.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-configfile
        '''
        result = self._values.get("config_file")
        assert result is not None, "Required property 'config_file' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def repository_link_id(self) -> builtins.str:
        '''The ID of the repository link associated with a specific sync configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-repositorylinkid
        '''
        result = self._values.get("repository_link_id")
        assert result is not None, "Required property 'repository_link_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_name(self) -> builtins.str:
        '''The name of the connection resource associated with a specific sync configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-resourcename
        '''
        result = self._values.get("resource_name")
        assert result is not None, "Required property 'resource_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the IAM role associated with a specific sync configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sync_type(self) -> builtins.str:
        '''The type of sync for a specific sync configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-synctype
        '''
        result = self._values.get("sync_type")
        assert result is not None, "Required property 'sync_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def publish_deployment_status(self) -> typing.Optional[builtins.str]:
        '''Whether to enable or disable publishing of deployment status to source providers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-publishdeploymentstatus
        '''
        result = self._values.get("publish_deployment_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def trigger_resource_update_on(self) -> typing.Optional[builtins.str]:
        '''When to trigger Git sync to begin the stack update.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codestarconnections-syncconfiguration.html#cfn-codestarconnections-syncconfiguration-triggerresourceupdateon
        '''
        result = self._values.get("trigger_resource_update_on")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSyncConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnection",
    "CfnConnectionProps",
    "CfnRepositoryLink",
    "CfnRepositoryLinkProps",
    "CfnSyncConfiguration",
    "CfnSyncConfigurationProps",
]

publication.publish()

def _typecheckingstub__1b31f55bcd270757c56f65f68558594d1908e1956199257e40b61ad1328525c3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_name: builtins.str,
    host_arn: typing.Optional[builtins.str] = None,
    provider_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35ee59ed14cc3a52d66e46db3ccc3d36ea0c6b5133b23c09d6f13279a0159048(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7439e44f0496a9ba58cb0741afc532422c7c595d46da2e7f6cc4e0b67c3387e9(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c74ec66d28c8d03c7f48d90efa65701a9b502cde3cf8e62b1f7d4b30a589a83(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06a35f319001e96b6f2b20bfbe5dae6f255ba9622170543150326f886683e443(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1aca832648768d4bedc95e0dd9eb0553af2e55cd113046f9922f476f7c18ddd7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4559e698887f8e503dde8843ff791284d6d9949c323e9ac7625231409f77297(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c17bc8ee185245b98d73051c96c32d31990b026c92635744b3a690aba461026(
    *,
    connection_name: builtins.str,
    host_arn: typing.Optional[builtins.str] = None,
    provider_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdf48b0dfdec692a05fb0520b1d1c224a8c2e2c7f2613c7a1e42179efa8707cc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_arn: builtins.str,
    owner_id: builtins.str,
    repository_name: builtins.str,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c12cbe13f83fd7ed50821e79d7ce9f67351ce7923283498bb237f85641899258(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b12f3011d520668189d58b24e4e9f8e0f5155af7ad40e14f399a0462ecebb0d4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8876457702f59ff1032085cd26b110c8d6e7fae6bbd6adee023301843b8dd66(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__663677d537f429830084c0b8c2eb0fb3120802794afada996d2845193413d150(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ada27515939c416886b3726d8504ee6351dee56bf23a317efce0cbf60225bce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72d6898194f3a2786d5d0888d37cfcf4f3c06554c8dcab6f23c16f81ff241b9c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3169870757b800cdac6097cbe92bb05d72aa36383fc08c2d273a2ef98bdfb961(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a059e8a38cb53db73841fe9a927fc29f036c7d50538d54c9a91ff9cb6d714763(
    *,
    connection_arn: builtins.str,
    owner_id: builtins.str,
    repository_name: builtins.str,
    encryption_key_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c8a904149088ca3c954aba811ae03db6bb18a34b324a10bedb2331c6f876b12(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    branch: builtins.str,
    config_file: builtins.str,
    repository_link_id: builtins.str,
    resource_name: builtins.str,
    role_arn: builtins.str,
    sync_type: builtins.str,
    publish_deployment_status: typing.Optional[builtins.str] = None,
    trigger_resource_update_on: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba0212b5f34dcefde1cc911722704bbe375f7da6cc5664daf19a6b30de041172(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c5e0bde34dbb71b2c1dca1aa91236c78ce6f4f9cce380b40392d95f60f5436(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41b151b4d5881562900d975603bfc5389d4bab87c50dc36536cd3003bc4d791b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f0211209d25f8536c8c1167936be2d2cebd2bf3ae3224a101371fea54254429(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d960d0547e481ad4fe89040e67311dc4f418ffe323ada1ffc6b3f130569e8b86(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6a186f209425b22ba86b10b6714304808f4cb3f878507a70f06e8d9378dac4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c33417a47e49bf925d46ca39cc6ac66fa3d450e28ab0ba781d48878d680eb99b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7aa9e776fee9e7c2ac12a6821ca735b73efe0013da11eacba140d600678d98(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ee8fea36d4094e0ac90eb20686a90d517ffcde16742313ecf04785324f10c50(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3019909980645630665fb7da740e906ba748d5a370476cef6024471869dea97b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea619fc4ca98271e7e2c90f35350d4af5c1f35168a8e4cdc7191c86cfcfff5ce(
    *,
    branch: builtins.str,
    config_file: builtins.str,
    repository_link_id: builtins.str,
    resource_name: builtins.str,
    role_arn: builtins.str,
    sync_type: builtins.str,
    publish_deployment_status: typing.Optional[builtins.str] = None,
    trigger_resource_update_on: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
