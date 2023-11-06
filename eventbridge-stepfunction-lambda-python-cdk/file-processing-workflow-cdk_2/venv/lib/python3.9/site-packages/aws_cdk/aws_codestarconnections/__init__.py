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
        :param connection_name: The name of the connection. Connection names must be unique in an AWS user account.
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

        :param connection_name: The name of the connection. Connection names must be unique in an AWS user account.
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

        Connection names must be unique in an AWS user account.

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


__all__ = [
    "CfnConnection",
    "CfnConnectionProps",
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
