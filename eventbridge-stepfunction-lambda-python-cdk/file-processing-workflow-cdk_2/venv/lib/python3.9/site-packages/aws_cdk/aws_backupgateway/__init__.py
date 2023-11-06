'''
# AWS::BackupGateway Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_backupgateway as backupgateway
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BackupGateway construct libraries](https://constructs.dev/search?q=backupgateway)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BackupGateway resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BackupGateway.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BackupGateway](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BackupGateway.html).

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
class CfnHypervisor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_backupgateway.CfnHypervisor",
):
    '''Represents the hypervisor's permissions to which the gateway will connect.

    A hypervisor is hardware, software, or firmware that creates and manages virtual machines, and allocates resources to them.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_backupgateway as backupgateway
        
        cfn_hypervisor = backupgateway.CfnHypervisor(self, "MyCfnHypervisor",
            host="host",
            kms_key_arn="kmsKeyArn",
            log_group_arn="logGroupArn",
            name="name",
            password="password",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            username="username"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        host: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param host: The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service used to encrypt the hypervisor.
        :param log_group_arn: The Amazon Resource Name (ARN) of the group of gateways within the requested log.
        :param name: The name of the hypervisor.
        :param password: The password for the hypervisor.
        :param tags: The tags of the hypervisor configuration to import.
        :param username: The username for the hypervisor.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3be02ddf56a7cf36e877cb5703e48b257066d0325551bfac15ae1763c276bd4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHypervisorProps(
            host=host,
            kms_key_arn=kms_key_arn,
            log_group_arn=log_group_arn,
            name=name,
            password=password,
            tags=tags,
            username=username,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73179679c0ac35989063a27b881b3a1e441a50ceca6ff4c112b4797117c4a78e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__51ef1c77102bdf1334b3191a61e3d0c21969caa7c60187e81c77249c53555860)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHypervisorArn")
    def attr_hypervisor_arn(self) -> builtins.str:
        '''Returns ``HypervisorArn`` , an Amazon Resource Name (ARN) that uniquely identifies a Hypervisor.

        For example: ``arn:aws:backup-gateway:us-east-1:123456789012:hypervisor/hype-1234D67D``

        :cloudformationAttribute: HypervisorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHypervisorArn"))

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
    @jsii.member(jsii_name="host")
    def host(self) -> typing.Optional[builtins.str]:
        '''The server host of the hypervisor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "host"))

    @host.setter
    def host(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234675d8ca91dba01c1c315060e69648fc33228f4d948219054c844c1a448278)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "host", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service used to encrypt the hypervisor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7a3fd728ca2a0e447ba4104f46d934d4ef2f36042f47c6c805ca7d2aef9e0c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="logGroupArn")
    def log_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the group of gateways within the requested log.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "logGroupArn"))

    @log_group_arn.setter
    def log_group_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb3a1f75ab544a4984880a35146647b1fbea41c82c952a898424f032faf628d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the hypervisor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__51f6b5d4a83eac793b06bc0d84230f8b875839fa833e3f5956b48c16cc7cf3df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the hypervisor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be7fefb32999b7ee6037c16d74b63fc90b2f8978a74f5952e3aa18ad16bedca1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the hypervisor configuration to import.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dde24d2859009b6347e276635d0a0359b4dcc8299b84c2afd330e475d26093c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        '''The username for the hypervisor.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01da04068d13529ca3507c1adc48f01d03eb0ade1021a50f92b12c74e46c8b5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_backupgateway.CfnHypervisorProps",
    jsii_struct_bases=[],
    name_mapping={
        "host": "host",
        "kms_key_arn": "kmsKeyArn",
        "log_group_arn": "logGroupArn",
        "name": "name",
        "password": "password",
        "tags": "tags",
        "username": "username",
    },
)
class CfnHypervisorProps:
    def __init__(
        self,
        *,
        host: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        log_group_arn: typing.Optional[builtins.str] = None,
        name: typing.Optional[builtins.str] = None,
        password: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnHypervisor``.

        :param host: The server host of the hypervisor. This can be either an IP address or a fully-qualified domain name (FQDN).
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS Key Management Service used to encrypt the hypervisor.
        :param log_group_arn: The Amazon Resource Name (ARN) of the group of gateways within the requested log.
        :param name: The name of the hypervisor.
        :param password: The password for the hypervisor.
        :param tags: The tags of the hypervisor configuration to import.
        :param username: The username for the hypervisor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_backupgateway as backupgateway
            
            cfn_hypervisor_props = backupgateway.CfnHypervisorProps(
                host="host",
                kms_key_arn="kmsKeyArn",
                log_group_arn="logGroupArn",
                name="name",
                password="password",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                username="username"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57cbe7a0ec27db32ffa455c7883d0f02a2f26f4795873d74444a3b2a3e35f5d6)
            check_type(argname="argument host", value=host, expected_type=type_hints["host"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if host is not None:
            self._values["host"] = host
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if log_group_arn is not None:
            self._values["log_group_arn"] = log_group_arn
        if name is not None:
            self._values["name"] = name
        if password is not None:
            self._values["password"] = password
        if tags is not None:
            self._values["tags"] = tags
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def host(self) -> typing.Optional[builtins.str]:
        '''The server host of the hypervisor.

        This can be either an IP address or a fully-qualified domain name (FQDN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-host
        '''
        result = self._values.get("host")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Key Management Service used to encrypt the hypervisor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def log_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the group of gateways within the requested log.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-loggrouparn
        '''
        result = self._values.get("log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the hypervisor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password for the hypervisor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags of the hypervisor configuration to import.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The username for the hypervisor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-backupgateway-hypervisor.html#cfn-backupgateway-hypervisor-username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHypervisorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnHypervisor",
    "CfnHypervisorProps",
]

publication.publish()

def _typecheckingstub__f3be02ddf56a7cf36e877cb5703e48b257066d0325551bfac15ae1763c276bd4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    host: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    log_group_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73179679c0ac35989063a27b881b3a1e441a50ceca6ff4c112b4797117c4a78e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51ef1c77102bdf1334b3191a61e3d0c21969caa7c60187e81c77249c53555860(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234675d8ca91dba01c1c315060e69648fc33228f4d948219054c844c1a448278(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7a3fd728ca2a0e447ba4104f46d934d4ef2f36042f47c6c805ca7d2aef9e0c9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb3a1f75ab544a4984880a35146647b1fbea41c82c952a898424f032faf628d7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51f6b5d4a83eac793b06bc0d84230f8b875839fa833e3f5956b48c16cc7cf3df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be7fefb32999b7ee6037c16d74b63fc90b2f8978a74f5952e3aa18ad16bedca1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dde24d2859009b6347e276635d0a0359b4dcc8299b84c2afd330e475d26093c1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01da04068d13529ca3507c1adc48f01d03eb0ade1021a50f92b12c74e46c8b5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57cbe7a0ec27db32ffa455c7883d0f02a2f26f4795873d74444a3b2a3e35f5d6(
    *,
    host: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    log_group_arn: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
