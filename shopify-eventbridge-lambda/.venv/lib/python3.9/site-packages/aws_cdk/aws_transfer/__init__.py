'''
# AWS Transfer for SFTP Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_transfer as transfer
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Transfer construct libraries](https://constructs.dev/search?q=transfer)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Transfer resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transfer.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Transfer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Transfer.html).

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
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAgreement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnAgreement",
):
    '''Creates an agreement.

    An agreement is a bilateral trading partner agreement, or partnership, between an AWS Transfer Family server and an AS2 process. The agreement defines the file and message transfer relationship between the server and the AS2 process. To define an agreement, Transfer Family combines a server, local profile, partner profile, certificate, and other attributes.

    The partner is identified with the ``PartnerProfileId`` , and the AS2 process is identified with the ``LocalProfileId`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html
    :cloudformationResource: AWS::Transfer::Agreement
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        cfn_agreement = transfer.CfnAgreement(self, "MyCfnAgreement",
            access_role="accessRole",
            base_directory="baseDirectory",
            local_profile_id="localProfileId",
            partner_profile_id="partnerProfileId",
            server_id="serverId",
        
            # the properties below are optional
            description="description",
            status="status",
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
        access_role: builtins.str,
        base_directory: builtins.str,
        local_profile_id: builtins.str,
        partner_profile_id: builtins.str,
        server_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_role: Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use. *For AS2 connectors* With AS2, you can send files by calling ``StartFileTransfer`` and specifying the file paths in the request parameter, ``SendFilePaths`` . We use the file’s parent directory (for example, for ``--send-file-paths /bucket/dir/file.txt`` , parent directory is ``/bucket/dir/`` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the ``AccessRole`` needs to provide read and write access to the parent directory of the file location used in the ``StartFileTransfer`` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with ``StartFileTransfer`` . If you are using Basic authentication for your AS2 connector, the access role requires the ``secretsmanager:GetSecretValue`` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the ``kms:Decrypt`` permission for that key. *For SFTP connectors* Make sure that the access role provides read and write access to the parent directory of the file location that's used in the ``StartFileTransfer`` request. Additionally, make sure that the role provides ``secretsmanager:GetSecretValue`` permission to AWS Secrets Manager .
        :param base_directory: The landing directory (folder) for files that are transferred by using the AS2 protocol.
        :param local_profile_id: A unique identifier for the AS2 local profile.
        :param partner_profile_id: A unique identifier for the partner profile used in the agreement.
        :param server_id: A system-assigned unique identifier for a server instance. This identifier indicates the specific server that the agreement uses.
        :param description: The name or short description that's used to identify the agreement.
        :param status: The current status of the agreement, either ``ACTIVE`` or ``INACTIVE`` .
        :param tags: Key-value pairs that can be used to group and search for agreements.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f95ec07e6c4ee624e4f9374f7db0e66b46af64fa8c86e2e41aa290c72214e4ab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAgreementProps(
            access_role=access_role,
            base_directory=base_directory,
            local_profile_id=local_profile_id,
            partner_profile_id=partner_profile_id,
            server_id=server_id,
            description=description,
            status=status,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__228db9cea00437d476e4860ef1214693d948e861477e0b0435205c3df9bf79f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6401d5baaa894d0f43e7153a11e00450f84a7d2eae08481fba5d6eeece91aa77)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAgreementId")
    def attr_agreement_id(self) -> builtins.str:
        '''The unique identifier for the AS2 agreement, returned after the API call succeeds.

        :cloudformationAttribute: AgreementId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAgreementId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Specifies the unique Amazon Resource Name (ARN) for the agreement.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

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
    @jsii.member(jsii_name="accessRole")
    def access_role(self) -> builtins.str:
        '''Connectors are used to send files using either the AS2 or SFTP protocol.'''
        return typing.cast(builtins.str, jsii.get(self, "accessRole"))

    @access_role.setter
    def access_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6846ae06100d907ce47940f1c737179b266cb64b8ba5e2c4167475979e0e2716)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessRole", value)

    @builtins.property
    @jsii.member(jsii_name="baseDirectory")
    def base_directory(self) -> builtins.str:
        '''The landing directory (folder) for files that are transferred by using the AS2 protocol.'''
        return typing.cast(builtins.str, jsii.get(self, "baseDirectory"))

    @base_directory.setter
    def base_directory(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e95a046a6530138645bcc3d9ea79bf173c25ac44d2324af6ecc4137b705bfc28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "baseDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="localProfileId")
    def local_profile_id(self) -> builtins.str:
        '''A unique identifier for the AS2 local profile.'''
        return typing.cast(builtins.str, jsii.get(self, "localProfileId"))

    @local_profile_id.setter
    def local_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3167bad2c7efdb7b3e0dd7d0402156f8d6e14fae7c15dd40a5fccd0b81e057)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "localProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="partnerProfileId")
    def partner_profile_id(self) -> builtins.str:
        '''A unique identifier for the partner profile used in the agreement.'''
        return typing.cast(builtins.str, jsii.get(self, "partnerProfileId"))

    @partner_profile_id.setter
    def partner_profile_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd438983791db4dad3b3d480a6bf25cacd9537198e1ed06c6a676fa3b408f77a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "partnerProfileId", value)

    @builtins.property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        '''A system-assigned unique identifier for a server instance.'''
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14dc2bb42fd7d8e680f89ab4bbef23a05ad685bb8ba0ece9fc2d04ff9c7d508a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The name or short description that's used to identify the agreement.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53c57c4c1fcab40ff6fbf72d1b3a40161b6904921f0e56930629bce8dc6662fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> typing.Optional[builtins.str]:
        '''The current status of the agreement, either ``ACTIVE`` or ``INACTIVE`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "status"))

    @status.setter
    def status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78211aad1a50ad3834dcb7a48092349fa0f45f77997fe33f6e8cab4593032c48)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for agreements.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbeccb7f697f73180ad5ee02e1bc0a8b54212c0eb54c653977d2989de01ad6f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnAgreementProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_role": "accessRole",
        "base_directory": "baseDirectory",
        "local_profile_id": "localProfileId",
        "partner_profile_id": "partnerProfileId",
        "server_id": "serverId",
        "description": "description",
        "status": "status",
        "tags": "tags",
    },
)
class CfnAgreementProps:
    def __init__(
        self,
        *,
        access_role: builtins.str,
        base_directory: builtins.str,
        local_profile_id: builtins.str,
        partner_profile_id: builtins.str,
        server_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        status: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAgreement``.

        :param access_role: Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use. *For AS2 connectors* With AS2, you can send files by calling ``StartFileTransfer`` and specifying the file paths in the request parameter, ``SendFilePaths`` . We use the file’s parent directory (for example, for ``--send-file-paths /bucket/dir/file.txt`` , parent directory is ``/bucket/dir/`` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the ``AccessRole`` needs to provide read and write access to the parent directory of the file location used in the ``StartFileTransfer`` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with ``StartFileTransfer`` . If you are using Basic authentication for your AS2 connector, the access role requires the ``secretsmanager:GetSecretValue`` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the ``kms:Decrypt`` permission for that key. *For SFTP connectors* Make sure that the access role provides read and write access to the parent directory of the file location that's used in the ``StartFileTransfer`` request. Additionally, make sure that the role provides ``secretsmanager:GetSecretValue`` permission to AWS Secrets Manager .
        :param base_directory: The landing directory (folder) for files that are transferred by using the AS2 protocol.
        :param local_profile_id: A unique identifier for the AS2 local profile.
        :param partner_profile_id: A unique identifier for the partner profile used in the agreement.
        :param server_id: A system-assigned unique identifier for a server instance. This identifier indicates the specific server that the agreement uses.
        :param description: The name or short description that's used to identify the agreement.
        :param status: The current status of the agreement, either ``ACTIVE`` or ``INACTIVE`` .
        :param tags: Key-value pairs that can be used to group and search for agreements.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            cfn_agreement_props = transfer.CfnAgreementProps(
                access_role="accessRole",
                base_directory="baseDirectory",
                local_profile_id="localProfileId",
                partner_profile_id="partnerProfileId",
                server_id="serverId",
            
                # the properties below are optional
                description="description",
                status="status",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c92e8cdff7d6f57ae5fd00ef4190544d79a76c01e88d32b21b88588eeb47ba2e)
            check_type(argname="argument access_role", value=access_role, expected_type=type_hints["access_role"])
            check_type(argname="argument base_directory", value=base_directory, expected_type=type_hints["base_directory"])
            check_type(argname="argument local_profile_id", value=local_profile_id, expected_type=type_hints["local_profile_id"])
            check_type(argname="argument partner_profile_id", value=partner_profile_id, expected_type=type_hints["partner_profile_id"])
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_role": access_role,
            "base_directory": base_directory,
            "local_profile_id": local_profile_id,
            "partner_profile_id": partner_profile_id,
            "server_id": server_id,
        }
        if description is not None:
            self._values["description"] = description
        if status is not None:
            self._values["status"] = status
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def access_role(self) -> builtins.str:
        '''Connectors are used to send files using either the AS2 or SFTP protocol.

        For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.

        *For AS2 connectors*

        With AS2, you can send files by calling ``StartFileTransfer`` and specifying the file paths in the request parameter, ``SendFilePaths`` . We use the file’s parent directory (for example, for ``--send-file-paths /bucket/dir/file.txt`` , parent directory is ``/bucket/dir/`` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the ``AccessRole`` needs to provide read and write access to the parent directory of the file location used in the ``StartFileTransfer`` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with ``StartFileTransfer`` .

        If you are using Basic authentication for your AS2 connector, the access role requires the ``secretsmanager:GetSecretValue`` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the ``kms:Decrypt`` permission for that key.

        *For SFTP connectors*

        Make sure that the access role provides read and write access to the parent directory of the file location that's used in the ``StartFileTransfer`` request. Additionally, make sure that the role provides ``secretsmanager:GetSecretValue`` permission to AWS Secrets Manager .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-accessrole
        '''
        result = self._values.get("access_role")
        assert result is not None, "Required property 'access_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def base_directory(self) -> builtins.str:
        '''The landing directory (folder) for files that are transferred by using the AS2 protocol.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-basedirectory
        '''
        result = self._values.get("base_directory")
        assert result is not None, "Required property 'base_directory' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def local_profile_id(self) -> builtins.str:
        '''A unique identifier for the AS2 local profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-localprofileid
        '''
        result = self._values.get("local_profile_id")
        assert result is not None, "Required property 'local_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def partner_profile_id(self) -> builtins.str:
        '''A unique identifier for the partner profile used in the agreement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-partnerprofileid
        '''
        result = self._values.get("partner_profile_id")
        assert result is not None, "Required property 'partner_profile_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''A system-assigned unique identifier for a server instance.

        This identifier indicates the specific server that the agreement uses.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-serverid
        '''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The name or short description that's used to identify the agreement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional[builtins.str]:
        '''The current status of the agreement, either ``ACTIVE`` or ``INACTIVE`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-status
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for agreements.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-agreement.html#cfn-transfer-agreement-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAgreementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnCertificate",
):
    '''Imports the signing and encryption certificates that you need to create local (AS2) profiles and partner profiles.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html
    :cloudformationResource: AWS::Transfer::Certificate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        cfn_certificate = transfer.CfnCertificate(self, "MyCfnCertificate",
            certificate="certificate",
            usage="usage",
        
            # the properties below are optional
            active_date="activeDate",
            certificate_chain="certificateChain",
            description="description",
            inactive_date="inactiveDate",
            private_key="privateKey",
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
        certificate: builtins.str,
        usage: builtins.str,
        active_date: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        inactive_date: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate: The file name for the certificate.
        :param usage: Specifies how this certificate is used. It can be used in the following ways:. - ``SIGNING`` : For signing AS2 messages - ``ENCRYPTION`` : For encrypting AS2 messages - ``TLS`` : For securing AS2 communications sent over HTTPS
        :param active_date: An optional date that specifies when the certificate becomes active.
        :param certificate_chain: The list of certificates that make up the chain for the certificate.
        :param description: The name or description that's used to identity the certificate.
        :param inactive_date: An optional date that specifies when the certificate becomes inactive.
        :param private_key: The file that contains the private key for the certificate that's being imported.
        :param tags: Key-value pairs that can be used to group and search for certificates.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f95ee160137bed43b6b325f0de8dc95bc0d10db792e4492913f9d664df9a567)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            certificate=certificate,
            usage=usage,
            active_date=active_date,
            certificate_chain=certificate_chain,
            description=description,
            inactive_date=inactive_date,
            private_key=private_key,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1474a816abc465fbde815216c7dd03f20d910c99fb002aee78d0f01c8d4f55c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__277a102c432293cf858b418d7187668fb07e13095bca6276d8a05cc05818e185)
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
        '''The unique Amazon Resource Name (ARN) for the certificate.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCertificateId")
    def attr_certificate_id(self) -> builtins.str:
        '''An array of identifiers for the imported certificates.

        You use this identifier for working with profiles and partner profiles.

        :cloudformationAttribute: CertificateId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCertificateId"))

    @builtins.property
    @jsii.member(jsii_name="attrNotAfterDate")
    def attr_not_after_date(self) -> builtins.str:
        '''The final date that the certificate is valid.

        :cloudformationAttribute: NotAfterDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNotAfterDate"))

    @builtins.property
    @jsii.member(jsii_name="attrNotBeforeDate")
    def attr_not_before_date(self) -> builtins.str:
        '''The earliest date that the certificate is valid.

        :cloudformationAttribute: NotBeforeDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNotBeforeDate"))

    @builtins.property
    @jsii.member(jsii_name="attrSerial")
    def attr_serial(self) -> builtins.str:
        '''The serial number for the certificate.

        :cloudformationAttribute: Serial
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSerial"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The certificate can be either ``ACTIVE`` , ``PENDING_ROTATION`` , or ``INACTIVE`` .

        ``PENDING_ROTATION`` means that this certificate will replace the current certificate when it expires.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrType")
    def attr_type(self) -> builtins.str:
        '''If a private key has been specified for the certificate, its type is ``CERTIFICATE_WITH_PRIVATE_KEY`` .

        If there is no private key, the type is ``CERTIFICATE`` .

        :cloudformationAttribute: Type
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrType"))

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
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> builtins.str:
        '''The file name for the certificate.'''
        return typing.cast(builtins.str, jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fa83398b89b8d2e8d3148b42b343e817bfe6f78b80958b2d783b221499449d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="usage")
    def usage(self) -> builtins.str:
        '''Specifies how this certificate is used.

        It can be used in the following ways:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "usage"))

    @usage.setter
    def usage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17d42e7b31f98bf4936b925740b19e31175848292139c852b96ff6f0b4e1fe90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usage", value)

    @builtins.property
    @jsii.member(jsii_name="activeDate")
    def active_date(self) -> typing.Optional[builtins.str]:
        '''An optional date that specifies when the certificate becomes active.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "activeDate"))

    @active_date.setter
    def active_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e21cd62811200a42c14a35c21b39187a62f01e9ea383c2661f6e2554927157a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "activeDate", value)

    @builtins.property
    @jsii.member(jsii_name="certificateChain")
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''The list of certificates that make up the chain for the certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateChain"))

    @certificate_chain.setter
    def certificate_chain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2df481347ef056a66debc0e80f934287081532818a1ce5e1ba0d0537183f006)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateChain", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The name or description that's used to identity the certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__333e9a8ceb39861e44203fc455ed2ec68cd2d164b99b9114af865c90e44a7f2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="inactiveDate")
    def inactive_date(self) -> typing.Optional[builtins.str]:
        '''An optional date that specifies when the certificate becomes inactive.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inactiveDate"))

    @inactive_date.setter
    def inactive_date(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__154790047dfce512ca194065423dd7cea885f3c80210af5f1388990a82c42986)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inactiveDate", value)

    @builtins.property
    @jsii.member(jsii_name="privateKey")
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The file that contains the private key for the certificate that's being imported.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "privateKey"))

    @private_key.setter
    def private_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2850ba9bd4e8becb665faeed903ba33f4e9e56676cc1fa8d8a849f7bd65cd8df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "privateKey", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for certificates.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__112d41348367dd1df7b4520890e43a0633334e24689066a3866ad51862dc97c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "usage": "usage",
        "active_date": "activeDate",
        "certificate_chain": "certificateChain",
        "description": "description",
        "inactive_date": "inactiveDate",
        "private_key": "privateKey",
        "tags": "tags",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        certificate: builtins.str,
        usage: builtins.str,
        active_date: typing.Optional[builtins.str] = None,
        certificate_chain: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        inactive_date: typing.Optional[builtins.str] = None,
        private_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param certificate: The file name for the certificate.
        :param usage: Specifies how this certificate is used. It can be used in the following ways:. - ``SIGNING`` : For signing AS2 messages - ``ENCRYPTION`` : For encrypting AS2 messages - ``TLS`` : For securing AS2 communications sent over HTTPS
        :param active_date: An optional date that specifies when the certificate becomes active.
        :param certificate_chain: The list of certificates that make up the chain for the certificate.
        :param description: The name or description that's used to identity the certificate.
        :param inactive_date: An optional date that specifies when the certificate becomes inactive.
        :param private_key: The file that contains the private key for the certificate that's being imported.
        :param tags: Key-value pairs that can be used to group and search for certificates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            cfn_certificate_props = transfer.CfnCertificateProps(
                certificate="certificate",
                usage="usage",
            
                # the properties below are optional
                active_date="activeDate",
                certificate_chain="certificateChain",
                description="description",
                inactive_date="inactiveDate",
                private_key="privateKey",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9b7c390d04a925160e4d0a39429a22ee9641e79a668a3dcae449e157976c325)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument usage", value=usage, expected_type=type_hints["usage"])
            check_type(argname="argument active_date", value=active_date, expected_type=type_hints["active_date"])
            check_type(argname="argument certificate_chain", value=certificate_chain, expected_type=type_hints["certificate_chain"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument inactive_date", value=inactive_date, expected_type=type_hints["inactive_date"])
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate": certificate,
            "usage": usage,
        }
        if active_date is not None:
            self._values["active_date"] = active_date
        if certificate_chain is not None:
            self._values["certificate_chain"] = certificate_chain
        if description is not None:
            self._values["description"] = description
        if inactive_date is not None:
            self._values["inactive_date"] = inactive_date
        if private_key is not None:
            self._values["private_key"] = private_key
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def certificate(self) -> builtins.str:
        '''The file name for the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-certificate
        '''
        result = self._values.get("certificate")
        assert result is not None, "Required property 'certificate' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def usage(self) -> builtins.str:
        '''Specifies how this certificate is used. It can be used in the following ways:.

        - ``SIGNING`` : For signing AS2 messages
        - ``ENCRYPTION`` : For encrypting AS2 messages
        - ``TLS`` : For securing AS2 communications sent over HTTPS

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-usage
        '''
        result = self._values.get("usage")
        assert result is not None, "Required property 'usage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def active_date(self) -> typing.Optional[builtins.str]:
        '''An optional date that specifies when the certificate becomes active.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-activedate
        '''
        result = self._values.get("active_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_chain(self) -> typing.Optional[builtins.str]:
        '''The list of certificates that make up the chain for the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-certificatechain
        '''
        result = self._values.get("certificate_chain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The name or description that's used to identity the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inactive_date(self) -> typing.Optional[builtins.str]:
        '''An optional date that specifies when the certificate becomes inactive.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-inactivedate
        '''
        result = self._values.get("inactive_date")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def private_key(self) -> typing.Optional[builtins.str]:
        '''The file that contains the private key for the certificate that's being imported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-privatekey
        '''
        result = self._values.get("private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for certificates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-certificate.html#cfn-transfer-certificate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnConnector",
):
    '''Creates the connector, which captures the parameters for a connection for the AS2 or SFTP protocol.

    For AS2, the connector is required for sending files to an externally hosted AS2 server. For SFTP, the connector is required when sending files to an SFTP server or receiving files from an SFTP server. For more details about connectors, see `Configure AS2 connectors <https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-connector.html>`_ and `Create SFTP connectors <https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html>`_ .
    .. epigraph::

       You must specify exactly one configuration object: either for AS2 ( ``As2Config`` ) or SFTP ( ``SftpConfig`` ).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html
    :cloudformationResource: AWS::Transfer::Connector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        # as2_config: Any
        
        cfn_connector = transfer.CfnConnector(self, "MyCfnConnector",
            access_role="accessRole",
            url="url",
        
            # the properties below are optional
            as2_config=as2_config,
            logging_role="loggingRole",
            security_policy_name="securityPolicyName",
            sftp_config=transfer.CfnConnector.SftpConfigProperty(
                trusted_host_keys=["trustedHostKeys"],
                user_secret_id="userSecretId"
            ),
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
        access_role: builtins.str,
        url: builtins.str,
        as2_config: typing.Any = None,
        logging_role: typing.Optional[builtins.str] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        sftp_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.SftpConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_role: Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use. *For AS2 connectors* With AS2, you can send files by calling ``StartFileTransfer`` and specifying the file paths in the request parameter, ``SendFilePaths`` . We use the file’s parent directory (for example, for ``--send-file-paths /bucket/dir/file.txt`` , parent directory is ``/bucket/dir/`` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the ``AccessRole`` needs to provide read and write access to the parent directory of the file location used in the ``StartFileTransfer`` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with ``StartFileTransfer`` . If you are using Basic authentication for your AS2 connector, the access role requires the ``secretsmanager:GetSecretValue`` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the ``kms:Decrypt`` permission for that key. *For SFTP connectors* Make sure that the access role provides read and write access to the parent directory of the file location that's used in the ``StartFileTransfer`` request. Additionally, make sure that the role provides ``secretsmanager:GetSecretValue`` permission to AWS Secrets Manager .
        :param url: The URL of the partner's AS2 or SFTP endpoint.
        :param as2_config: A structure that contains the parameters for an AS2 connector object.
        :param logging_role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.
        :param security_policy_name: The text name of the security policy for the specified connector.
        :param sftp_config: A structure that contains the parameters for an SFTP connector object.
        :param tags: Key-value pairs that can be used to group and search for connectors.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a3d92be7ab611ebe6dbf531ad899c2a95b3655fb829aeffdf52fdb11aae9d07)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProps(
            access_role=access_role,
            url=url,
            as2_config=as2_config,
            logging_role=logging_role,
            security_policy_name=security_policy_name,
            sftp_config=sftp_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a4f5bff2b8dd506b9f1b6f0cd274f6a295704751fa097cd5e1cf149d089e94)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9aab4ede341c608327700d1830ce91ecccf256e71cd06e45d4bd1c9fe8e81f16)
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
        '''Specifies the unique Amazon Resource Name (ARN) for the connector.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectorId")
    def attr_connector_id(self) -> builtins.str:
        '''The service-assigned ID of the connector that is created.

        :cloudformationAttribute: ConnectorId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorId"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceManagedEgressIpAddresses")
    def attr_service_managed_egress_ip_addresses(self) -> typing.List[builtins.str]:
        '''The list of egress IP addresses of this connector.

        These IP addresses are assigned automatically when you create the connector.

        :cloudformationAttribute: ServiceManagedEgressIpAddresses
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrServiceManagedEgressIpAddresses"))

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
    @jsii.member(jsii_name="accessRole")
    def access_role(self) -> builtins.str:
        '''Connectors are used to send files using either the AS2 or SFTP protocol.'''
        return typing.cast(builtins.str, jsii.get(self, "accessRole"))

    @access_role.setter
    def access_role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f4bab9f1a3e47eaac0c429ed6125ef23e8b2d8f33fac6396c2ef4a60b8617a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessRole", value)

    @builtins.property
    @jsii.member(jsii_name="url")
    def url(self) -> builtins.str:
        '''The URL of the partner's AS2 or SFTP endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "url"))

    @url.setter
    def url(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f2f8d48aab925fcdb11fb86f8b12aeae11aa8b85048a7ded27a817b5864536d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "url", value)

    @builtins.property
    @jsii.member(jsii_name="as2Config")
    def as2_config(self) -> typing.Any:
        '''A structure that contains the parameters for an AS2 connector object.'''
        return typing.cast(typing.Any, jsii.get(self, "as2Config"))

    @as2_config.setter
    def as2_config(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b16726d88010ccba3b94afdf2e5c9f9c1e8e4dc3d9f7d56e2edf0140e687d75c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "as2Config", value)

    @builtins.property
    @jsii.member(jsii_name="loggingRole")
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingRole"))

    @logging_role.setter
    def logging_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6fd1718d368db980c8cf49c237a691317f958db670b242715c5440aaf081b1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingRole", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyName")
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''The text name of the security policy for the specified connector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyName"))

    @security_policy_name.setter
    def security_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c96b636b491e11ce074e40058c1620fda321bb7685ad3a5204502b6fdb4cc24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="sftpConfig")
    def sftp_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.SftpConfigProperty"]]:
        '''A structure that contains the parameters for an SFTP connector object.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.SftpConfigProperty"]], jsii.get(self, "sftpConfig"))

    @sftp_config.setter
    def sftp_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.SftpConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__391f4dfc56c4811c4c4aedb8ffcfac5c521d440de2f0de853365abcdec435568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sftpConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for connectors.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__207f7abcb769a2e1717d82ad1c8c7df0c05b8d8d3d89a23127362727dcd65473)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnConnector.As2ConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "basic_auth_secret_id": "basicAuthSecretId",
            "compression": "compression",
            "encryption_algorithm": "encryptionAlgorithm",
            "local_profile_id": "localProfileId",
            "mdn_response": "mdnResponse",
            "mdn_signing_algorithm": "mdnSigningAlgorithm",
            "message_subject": "messageSubject",
            "partner_profile_id": "partnerProfileId",
            "signing_algorithm": "signingAlgorithm",
        },
    )
    class As2ConfigProperty:
        def __init__(
            self,
            *,
            basic_auth_secret_id: typing.Optional[builtins.str] = None,
            compression: typing.Optional[builtins.str] = None,
            encryption_algorithm: typing.Optional[builtins.str] = None,
            local_profile_id: typing.Optional[builtins.str] = None,
            mdn_response: typing.Optional[builtins.str] = None,
            mdn_signing_algorithm: typing.Optional[builtins.str] = None,
            message_subject: typing.Optional[builtins.str] = None,
            partner_profile_id: typing.Optional[builtins.str] = None,
            signing_algorithm: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the parameters for an AS2 connector object.

            :param basic_auth_secret_id: Provides Basic authentication support to the AS2 Connectors API. To use Basic authentication, you must provide the name or Amazon Resource Name (ARN) of a secret in AWS Secrets Manager . The default value for this parameter is ``null`` , which indicates that Basic authentication is not enabled for the connector. If the connector should use Basic authentication, the secret needs to be in the following format: ``{ "Username": "user-name", "Password": "user-password" }`` Replace ``user-name`` and ``user-password`` with the credentials for the actual user that is being authenticated. Note the following: - You are storing these credentials in Secrets Manager, *not passing them directly* into this API. - If you are using the API, SDKs, or CloudFormation to configure your connector, then you must create the secret before you can enable Basic authentication. However, if you are using the AWS management console, you can have the system create the secret for you. If you have previously enabled Basic authentication for a connector, you can disable it by using the ``UpdateConnector`` API call. For example, if you are using the CLI, you can run the following command to remove Basic authentication: ``update-connector --connector-id my-connector-id --as2-config 'BasicAuthSecretId=""'``
            :param compression: Specifies whether the AS2 file is compressed.
            :param encryption_algorithm: The algorithm that is used to encrypt the file. Note the following: - Do not use the ``DES_EDE3_CBC`` algorithm unless you must support a legacy client that requires it, as it is a weak encryption algorithm. - You can only specify ``NONE`` if the URL for your connector uses HTTPS. Using HTTPS ensures that no traffic is sent in clear text.
            :param local_profile_id: A unique identifier for the AS2 local profile.
            :param mdn_response: Used for outbound requests (from an AWS Transfer Family server to a partner AS2 server) to determine whether the partner response for transfers is synchronous or asynchronous. Specify either of the following values: - ``SYNC`` : The system expects a synchronous MDN response, confirming that the file was transferred successfully (or not). - ``NONE`` : Specifies that no MDN response is required.
            :param mdn_signing_algorithm: The signing algorithm for the MDN response. .. epigraph:: If set to DEFAULT (or not set at all), the value for ``SigningAlgorithm`` is used.
            :param message_subject: Used as the ``Subject`` HTTP header attribute in AS2 messages that are being sent with the connector.
            :param partner_profile_id: A unique identifier for the partner profile for the connector.
            :param signing_algorithm: The algorithm that is used to sign the AS2 messages sent with the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                as2_config_property = transfer.CfnConnector.As2ConfigProperty(
                    basic_auth_secret_id="basicAuthSecretId",
                    compression="compression",
                    encryption_algorithm="encryptionAlgorithm",
                    local_profile_id="localProfileId",
                    mdn_response="mdnResponse",
                    mdn_signing_algorithm="mdnSigningAlgorithm",
                    message_subject="messageSubject",
                    partner_profile_id="partnerProfileId",
                    signing_algorithm="signingAlgorithm"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__328497a7bbb181a996e0747268f6105731221ad3f578e8a5ca68e405dcdd7e63)
                check_type(argname="argument basic_auth_secret_id", value=basic_auth_secret_id, expected_type=type_hints["basic_auth_secret_id"])
                check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
                check_type(argname="argument encryption_algorithm", value=encryption_algorithm, expected_type=type_hints["encryption_algorithm"])
                check_type(argname="argument local_profile_id", value=local_profile_id, expected_type=type_hints["local_profile_id"])
                check_type(argname="argument mdn_response", value=mdn_response, expected_type=type_hints["mdn_response"])
                check_type(argname="argument mdn_signing_algorithm", value=mdn_signing_algorithm, expected_type=type_hints["mdn_signing_algorithm"])
                check_type(argname="argument message_subject", value=message_subject, expected_type=type_hints["message_subject"])
                check_type(argname="argument partner_profile_id", value=partner_profile_id, expected_type=type_hints["partner_profile_id"])
                check_type(argname="argument signing_algorithm", value=signing_algorithm, expected_type=type_hints["signing_algorithm"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if basic_auth_secret_id is not None:
                self._values["basic_auth_secret_id"] = basic_auth_secret_id
            if compression is not None:
                self._values["compression"] = compression
            if encryption_algorithm is not None:
                self._values["encryption_algorithm"] = encryption_algorithm
            if local_profile_id is not None:
                self._values["local_profile_id"] = local_profile_id
            if mdn_response is not None:
                self._values["mdn_response"] = mdn_response
            if mdn_signing_algorithm is not None:
                self._values["mdn_signing_algorithm"] = mdn_signing_algorithm
            if message_subject is not None:
                self._values["message_subject"] = message_subject
            if partner_profile_id is not None:
                self._values["partner_profile_id"] = partner_profile_id
            if signing_algorithm is not None:
                self._values["signing_algorithm"] = signing_algorithm

        @builtins.property
        def basic_auth_secret_id(self) -> typing.Optional[builtins.str]:
            '''Provides Basic authentication support to the AS2 Connectors API.

            To use Basic authentication, you must provide the name or Amazon Resource Name (ARN) of a secret in AWS Secrets Manager .

            The default value for this parameter is ``null`` , which indicates that Basic authentication is not enabled for the connector.

            If the connector should use Basic authentication, the secret needs to be in the following format:

            ``{ "Username": "user-name", "Password": "user-password" }``

            Replace ``user-name`` and ``user-password`` with the credentials for the actual user that is being authenticated.

            Note the following:

            - You are storing these credentials in Secrets Manager, *not passing them directly* into this API.
            - If you are using the API, SDKs, or CloudFormation to configure your connector, then you must create the secret before you can enable Basic authentication. However, if you are using the AWS management console, you can have the system create the secret for you.

            If you have previously enabled Basic authentication for a connector, you can disable it by using the ``UpdateConnector`` API call. For example, if you are using the CLI, you can run the following command to remove Basic authentication:

            ``update-connector --connector-id my-connector-id --as2-config 'BasicAuthSecretId=""'``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-basicauthsecretid
            '''
            result = self._values.get("basic_auth_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compression(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the AS2 file is compressed.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-compression
            '''
            result = self._values.get("compression")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_algorithm(self) -> typing.Optional[builtins.str]:
            '''The algorithm that is used to encrypt the file.

            Note the following:

            - Do not use the ``DES_EDE3_CBC`` algorithm unless you must support a legacy client that requires it, as it is a weak encryption algorithm.
            - You can only specify ``NONE`` if the URL for your connector uses HTTPS. Using HTTPS ensures that no traffic is sent in clear text.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-encryptionalgorithm
            '''
            result = self._values.get("encryption_algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_profile_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for the AS2 local profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-localprofileid
            '''
            result = self._values.get("local_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mdn_response(self) -> typing.Optional[builtins.str]:
            '''Used for outbound requests (from an AWS Transfer Family server to a partner AS2 server) to determine whether the partner response for transfers is synchronous or asynchronous.

            Specify either of the following values:

            - ``SYNC`` : The system expects a synchronous MDN response, confirming that the file was transferred successfully (or not).
            - ``NONE`` : Specifies that no MDN response is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-mdnresponse
            '''
            result = self._values.get("mdn_response")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mdn_signing_algorithm(self) -> typing.Optional[builtins.str]:
            '''The signing algorithm for the MDN response.

            .. epigraph::

               If set to DEFAULT (or not set at all), the value for ``SigningAlgorithm`` is used.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-mdnsigningalgorithm
            '''
            result = self._values.get("mdn_signing_algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_subject(self) -> typing.Optional[builtins.str]:
            '''Used as the ``Subject`` HTTP header attribute in AS2 messages that are being sent with the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-messagesubject
            '''
            result = self._values.get("message_subject")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def partner_profile_id(self) -> typing.Optional[builtins.str]:
            '''A unique identifier for the partner profile for the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-partnerprofileid
            '''
            result = self._values.get("partner_profile_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def signing_algorithm(self) -> typing.Optional[builtins.str]:
            '''The algorithm that is used to sign the AS2 messages sent with the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-as2config.html#cfn-transfer-connector-as2config-signingalgorithm
            '''
            result = self._values.get("signing_algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "As2ConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnConnector.SftpConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trusted_host_keys": "trustedHostKeys",
            "user_secret_id": "userSecretId",
        },
    )
    class SftpConfigProperty:
        def __init__(
            self,
            *,
            trusted_host_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
            user_secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains the parameters for an SFTP connector object.

            :param trusted_host_keys: The public portion of the host key, or keys, that are used to identify the external server to which you are connecting. You can use the ``ssh-keyscan`` command against the SFTP server to retrieve the necessary key. The three standard SSH public key format elements are ``<key type>`` , ``<body base64>`` , and an optional ``<comment>`` , with spaces between each element. Specify only the ``<key type>`` and ``<body base64>`` : do not enter the ``<comment>`` portion of the key. For the trusted host key, AWS Transfer Family accepts RSA and ECDSA keys. - For RSA keys, the ``<key type>`` string is ``ssh-rsa`` . - For ECDSA keys, the ``<key type>`` string is either ``ecdsa-sha2-nistp256`` , ``ecdsa-sha2-nistp384`` , or ``ecdsa-sha2-nistp521`` , depending on the size of the key you generated. Run this command to retrieve the SFTP server host key, where your SFTP server name is ``ftp.host.com`` . ``ssh-keyscan ftp.host.com`` This prints the public host key to standard output. ``ftp.host.com ssh-rsa AAAAB3Nza...<long-string-for-public-key`` Copy and paste this string into the ``TrustedHostKeys`` field for the ``create-connector`` command or into the *Trusted host keys* field in the console.
            :param user_secret_id: The identifier for the secret (in AWS Secrets Manager) that contains the SFTP user's private key, password, or both. The identifier must be the Amazon Resource Name (ARN) of the secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-sftpconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                sftp_config_property = transfer.CfnConnector.SftpConfigProperty(
                    trusted_host_keys=["trustedHostKeys"],
                    user_secret_id="userSecretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f4f8d4be2ad63a06a458c41605c9c21318e1d9117d48f21b9ee2ea6bb109d2e8)
                check_type(argname="argument trusted_host_keys", value=trusted_host_keys, expected_type=type_hints["trusted_host_keys"])
                check_type(argname="argument user_secret_id", value=user_secret_id, expected_type=type_hints["user_secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if trusted_host_keys is not None:
                self._values["trusted_host_keys"] = trusted_host_keys
            if user_secret_id is not None:
                self._values["user_secret_id"] = user_secret_id

        @builtins.property
        def trusted_host_keys(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The public portion of the host key, or keys, that are used to identify the external server to which you are connecting.

            You can use the ``ssh-keyscan`` command against the SFTP server to retrieve the necessary key.

            The three standard SSH public key format elements are ``<key type>`` , ``<body base64>`` , and an optional ``<comment>`` , with spaces between each element. Specify only the ``<key type>`` and ``<body base64>`` : do not enter the ``<comment>`` portion of the key.

            For the trusted host key, AWS Transfer Family accepts RSA and ECDSA keys.

            - For RSA keys, the ``<key type>`` string is ``ssh-rsa`` .
            - For ECDSA keys, the ``<key type>`` string is either ``ecdsa-sha2-nistp256`` , ``ecdsa-sha2-nistp384`` , or ``ecdsa-sha2-nistp521`` , depending on the size of the key you generated.

            Run this command to retrieve the SFTP server host key, where your SFTP server name is ``ftp.host.com`` .

            ``ssh-keyscan ftp.host.com``

            This prints the public host key to standard output.

            ``ftp.host.com ssh-rsa AAAAB3Nza...<long-string-for-public-key``

            Copy and paste this string into the ``TrustedHostKeys`` field for the ``create-connector`` command or into the *Trusted host keys* field in the console.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-sftpconfig.html#cfn-transfer-connector-sftpconfig-trustedhostkeys
            '''
            result = self._values.get("trusted_host_keys")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def user_secret_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the secret (in AWS Secrets Manager) that contains the SFTP user's private key, password, or both.

            The identifier must be the Amazon Resource Name (ARN) of the secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-connector-sftpconfig.html#cfn-transfer-connector-sftpconfig-usersecretid
            '''
            result = self._values.get("user_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SftpConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_role": "accessRole",
        "url": "url",
        "as2_config": "as2Config",
        "logging_role": "loggingRole",
        "security_policy_name": "securityPolicyName",
        "sftp_config": "sftpConfig",
        "tags": "tags",
    },
)
class CfnConnectorProps:
    def __init__(
        self,
        *,
        access_role: builtins.str,
        url: builtins.str,
        as2_config: typing.Any = None,
        logging_role: typing.Optional[builtins.str] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        sftp_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.SftpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnector``.

        :param access_role: Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use. *For AS2 connectors* With AS2, you can send files by calling ``StartFileTransfer`` and specifying the file paths in the request parameter, ``SendFilePaths`` . We use the file’s parent directory (for example, for ``--send-file-paths /bucket/dir/file.txt`` , parent directory is ``/bucket/dir/`` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the ``AccessRole`` needs to provide read and write access to the parent directory of the file location used in the ``StartFileTransfer`` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with ``StartFileTransfer`` . If you are using Basic authentication for your AS2 connector, the access role requires the ``secretsmanager:GetSecretValue`` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the ``kms:Decrypt`` permission for that key. *For SFTP connectors* Make sure that the access role provides read and write access to the parent directory of the file location that's used in the ``StartFileTransfer`` request. Additionally, make sure that the role provides ``secretsmanager:GetSecretValue`` permission to AWS Secrets Manager .
        :param url: The URL of the partner's AS2 or SFTP endpoint.
        :param as2_config: A structure that contains the parameters for an AS2 connector object.
        :param logging_role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.
        :param security_policy_name: The text name of the security policy for the specified connector.
        :param sftp_config: A structure that contains the parameters for an SFTP connector object.
        :param tags: Key-value pairs that can be used to group and search for connectors.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            # as2_config: Any
            
            cfn_connector_props = transfer.CfnConnectorProps(
                access_role="accessRole",
                url="url",
            
                # the properties below are optional
                as2_config=as2_config,
                logging_role="loggingRole",
                security_policy_name="securityPolicyName",
                sftp_config=transfer.CfnConnector.SftpConfigProperty(
                    trusted_host_keys=["trustedHostKeys"],
                    user_secret_id="userSecretId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7675f9dcded8f51977cf70f499821100319fe5d62996cb917457f772cfcc9a2e)
            check_type(argname="argument access_role", value=access_role, expected_type=type_hints["access_role"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument as2_config", value=as2_config, expected_type=type_hints["as2_config"])
            check_type(argname="argument logging_role", value=logging_role, expected_type=type_hints["logging_role"])
            check_type(argname="argument security_policy_name", value=security_policy_name, expected_type=type_hints["security_policy_name"])
            check_type(argname="argument sftp_config", value=sftp_config, expected_type=type_hints["sftp_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "access_role": access_role,
            "url": url,
        }
        if as2_config is not None:
            self._values["as2_config"] = as2_config
        if logging_role is not None:
            self._values["logging_role"] = logging_role
        if security_policy_name is not None:
            self._values["security_policy_name"] = security_policy_name
        if sftp_config is not None:
            self._values["sftp_config"] = sftp_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def access_role(self) -> builtins.str:
        '''Connectors are used to send files using either the AS2 or SFTP protocol.

        For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.

        *For AS2 connectors*

        With AS2, you can send files by calling ``StartFileTransfer`` and specifying the file paths in the request parameter, ``SendFilePaths`` . We use the file’s parent directory (for example, for ``--send-file-paths /bucket/dir/file.txt`` , parent directory is ``/bucket/dir/`` ) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the ``AccessRole`` needs to provide read and write access to the parent directory of the file location used in the ``StartFileTransfer`` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with ``StartFileTransfer`` .

        If you are using Basic authentication for your AS2 connector, the access role requires the ``secretsmanager:GetSecretValue`` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the ``kms:Decrypt`` permission for that key.

        *For SFTP connectors*

        Make sure that the access role provides read and write access to the parent directory of the file location that's used in the ``StartFileTransfer`` request. Additionally, make sure that the role provides ``secretsmanager:GetSecretValue`` permission to AWS Secrets Manager .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-accessrole
        '''
        result = self._values.get("access_role")
        assert result is not None, "Required property 'access_role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def url(self) -> builtins.str:
        '''The URL of the partner's AS2 or SFTP endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-url
        '''
        result = self._values.get("url")
        assert result is not None, "Required property 'url' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def as2_config(self) -> typing.Any:
        '''A structure that contains the parameters for an AS2 connector object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-as2config
        '''
        result = self._values.get("as2_config")
        return typing.cast(typing.Any, result)

    @builtins.property
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events.

        When set, you can view connector activity in your CloudWatch logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-loggingrole
        '''
        result = self._values.get("logging_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''The text name of the security policy for the specified connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-securitypolicyname
        '''
        result = self._values.get("security_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sftp_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.SftpConfigProperty]]:
        '''A structure that contains the parameters for an SFTP connector object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-sftpconfig
        '''
        result = self._values.get("sftp_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.SftpConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for connectors.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-connector.html#cfn-transfer-connector-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnProfile",
):
    '''Creates the local or partner profile to use for AS2 transfers.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html
    :cloudformationResource: AWS::Transfer::Profile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        cfn_profile = transfer.CfnProfile(self, "MyCfnProfile",
            as2_id="as2Id",
            profile_type="profileType",
        
            # the properties below are optional
            certificate_ids=["certificateIds"],
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
        as2_id: builtins.str,
        profile_type: builtins.str,
        certificate_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param as2_id: The ``As2Id`` is the *AS2-name* , as defined in the `RFC 4130 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc4130>`_ . For inbound transfers, this is the ``AS2-From`` header for the AS2 messages sent from the partner. For outbound connectors, this is the ``AS2-To`` header for the AS2 messages sent to the partner using the ``StartFileTransfer`` API operation. This ID cannot include spaces.
        :param profile_type: Indicates whether to list only ``LOCAL`` type profiles or only ``PARTNER`` type profiles. If not supplied in the request, the command lists all types of profiles.
        :param certificate_ids: An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.
        :param tags: Key-value pairs that can be used to group and search for profiles.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5b82428b7fd1ac13f1a57b868694175d216c1f61c671da5b091d46d81a7fa5c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileProps(
            as2_id=as2_id,
            profile_type=profile_type,
            certificate_ids=certificate_ids,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56325834528256f6c2bd12b40bde80e132a645d3bffd84876d0f808ee64a8d81)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5bf2a5779da146ecf6baff4b026696b629a9454da25b91d74ddd76ab2d5e3b0c)
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
        '''The Amazon Resource Name associated with the profile, in the form ``arn:aws:transfer:region:account-id:profile/profile-id/`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileId")
    def attr_profile_id(self) -> builtins.str:
        '''The unique identifier for the AS2 profile, returned after the API call succeeds.

        :cloudformationAttribute: ProfileId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileId"))

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
    @jsii.member(jsii_name="as2Id")
    def as2_id(self) -> builtins.str:
        '''The ``As2Id`` is the *AS2-name* , as defined in the `RFC 4130 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc4130>`_ . For inbound transfers, this is the ``AS2-From`` header for the AS2 messages sent from the partner. For outbound connectors, this is the ``AS2-To`` header for the AS2 messages sent to the partner using the ``StartFileTransfer`` API operation. This ID cannot include spaces.'''
        return typing.cast(builtins.str, jsii.get(self, "as2Id"))

    @as2_id.setter
    def as2_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__874129323a36e45f11222542eec1aaa8f0c6a101af85c9157bd91e99153e1f4c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "as2Id", value)

    @builtins.property
    @jsii.member(jsii_name="profileType")
    def profile_type(self) -> builtins.str:
        '''Indicates whether to list only ``LOCAL`` type profiles or only ``PARTNER`` type profiles.'''
        return typing.cast(builtins.str, jsii.get(self, "profileType"))

    @profile_type.setter
    def profile_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0b0d24da9b7ec761d77dbb7a24743425517ee4b5e684246e4a4a66f364ecc89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileType", value)

    @builtins.property
    @jsii.member(jsii_name="certificateIds")
    def certificate_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of identifiers for the imported certificates.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "certificateIds"))

    @certificate_ids.setter
    def certificate_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9becc0cd340df21123a424e73d8ffeb9b49be520391d98ec1ecf3c32081ef00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for profiles.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c41001d8363b6450b3342fb333eb5b5d2a570b2a64b0911308cd8d2824ad0419)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "as2_id": "as2Id",
        "profile_type": "profileType",
        "certificate_ids": "certificateIds",
        "tags": "tags",
    },
)
class CfnProfileProps:
    def __init__(
        self,
        *,
        as2_id: builtins.str,
        profile_type: builtins.str,
        certificate_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfile``.

        :param as2_id: The ``As2Id`` is the *AS2-name* , as defined in the `RFC 4130 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc4130>`_ . For inbound transfers, this is the ``AS2-From`` header for the AS2 messages sent from the partner. For outbound connectors, this is the ``AS2-To`` header for the AS2 messages sent to the partner using the ``StartFileTransfer`` API operation. This ID cannot include spaces.
        :param profile_type: Indicates whether to list only ``LOCAL`` type profiles or only ``PARTNER`` type profiles. If not supplied in the request, the command lists all types of profiles.
        :param certificate_ids: An array of identifiers for the imported certificates. You use this identifier for working with profiles and partner profiles.
        :param tags: Key-value pairs that can be used to group and search for profiles.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            cfn_profile_props = transfer.CfnProfileProps(
                as2_id="as2Id",
                profile_type="profileType",
            
                # the properties below are optional
                certificate_ids=["certificateIds"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca248e37e97df6c091c4a5b1f174228ff41c93e4175048b0f4e76df0547f4cd7)
            check_type(argname="argument as2_id", value=as2_id, expected_type=type_hints["as2_id"])
            check_type(argname="argument profile_type", value=profile_type, expected_type=type_hints["profile_type"])
            check_type(argname="argument certificate_ids", value=certificate_ids, expected_type=type_hints["certificate_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "as2_id": as2_id,
            "profile_type": profile_type,
        }
        if certificate_ids is not None:
            self._values["certificate_ids"] = certificate_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def as2_id(self) -> builtins.str:
        '''The ``As2Id`` is the *AS2-name* , as defined in the `RFC 4130 <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc4130>`_ . For inbound transfers, this is the ``AS2-From`` header for the AS2 messages sent from the partner. For outbound connectors, this is the ``AS2-To`` header for the AS2 messages sent to the partner using the ``StartFileTransfer`` API operation. This ID cannot include spaces.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-as2id
        '''
        result = self._values.get("as2_id")
        assert result is not None, "Required property 'as2_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_type(self) -> builtins.str:
        '''Indicates whether to list only ``LOCAL`` type profiles or only ``PARTNER`` type profiles.

        If not supplied in the request, the command lists all types of profiles.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-profiletype
        '''
        result = self._values.get("profile_type")
        assert result is not None, "Required property 'profile_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''An array of identifiers for the imported certificates.

        You use this identifier for working with profiles and partner profiles.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-certificateids
        '''
        result = self._values.get("certificate_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for profiles.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-profile.html#cfn-transfer-profile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnServer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnServer",
):
    '''Instantiates an auto-scaling virtual server based on the selected file transfer protocol in AWS .

    When you make updates to your file transfer protocol-enabled server or when you work with users, use the service-generated ``ServerId`` property that is assigned to the newly created server.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
    :cloudformationResource: AWS::Transfer::Server
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        cfn_server = transfer.CfnServer(self, "MyCfnServer",
            certificate="certificate",
            domain="domain",
            endpoint_details=transfer.CfnServer.EndpointDetailsProperty(
                address_allocation_ids=["addressAllocationIds"],
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_endpoint_id="vpcEndpointId",
                vpc_id="vpcId"
            ),
            endpoint_type="endpointType",
            identity_provider_details=transfer.CfnServer.IdentityProviderDetailsProperty(
                directory_id="directoryId",
                function="function",
                invocation_role="invocationRole",
                sftp_authentication_methods="sftpAuthenticationMethods",
                url="url"
            ),
            identity_provider_type="identityProviderType",
            logging_role="loggingRole",
            post_authentication_login_banner="postAuthenticationLoginBanner",
            pre_authentication_login_banner="preAuthenticationLoginBanner",
            protocol_details=transfer.CfnServer.ProtocolDetailsProperty(
                as2_transports=["as2Transports"],
                passive_ip="passiveIp",
                set_stat_option="setStatOption",
                tls_session_resumption_mode="tlsSessionResumptionMode"
            ),
            protocols=["protocols"],
            s3_storage_options=transfer.CfnServer.S3StorageOptionsProperty(
                directory_listing_optimization="directoryListingOptimization"
            ),
            security_policy_name="securityPolicyName",
            structured_log_destinations=["structuredLogDestinations"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            workflow_details=transfer.CfnServer.WorkflowDetailsProperty(
                on_partial_upload=[transfer.CfnServer.WorkflowDetailProperty(
                    execution_role="executionRole",
                    workflow_id="workflowId"
                )],
                on_upload=[transfer.CfnServer.WorkflowDetailProperty(
                    execution_role="executionRole",
                    workflow_id="workflowId"
                )]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        endpoint_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.EndpointDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        identity_provider_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.IdentityProviderDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_provider_type: typing.Optional[builtins.str] = None,
        logging_role: typing.Optional[builtins.str] = None,
        post_authentication_login_banner: typing.Optional[builtins.str] = None,
        pre_authentication_login_banner: typing.Optional[builtins.str] = None,
        protocol_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.ProtocolDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.S3StorageOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        structured_log_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        workflow_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.WorkflowDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate: The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate. Required when ``Protocols`` is set to ``FTPS`` . To request a new public certificate, see `Request a public certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html>`_ in the *AWS Certificate Manager User Guide* . To import an existing certificate into ACM, see `Importing certificates into ACM <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`_ in the *AWS Certificate Manager User Guide* . To request a private certificate to use FTPS through private IP addresses, see `Request a private certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html>`_ in the *AWS Certificate Manager User Guide* . Certificates with the following cryptographic algorithms and key sizes are supported: - 2048-bit RSA (RSA_2048) - 4096-bit RSA (RSA_4096) - Elliptic Prime Curve 256 bit (EC_prime256v1) - Elliptic Prime Curve 384 bit (EC_secp384r1) - Elliptic Prime Curve 521 bit (EC_secp521r1) .. epigraph:: The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.
        :param domain: Specifies the domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.
        :param endpoint_details: The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.
        :param endpoint_type: The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it. .. epigraph:: After May 19, 2021, you won't be able to create a server using ``EndpointType=VPC_ENDPOINT`` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with ``EndpointType=VPC_ENDPOINT`` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use ``EndpointType`` = ``VPC`` . For more information, see `Discontinuing the use of VPC_ENDPOINT <https://docs.aws.amazon.com//transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint>`_ . It is recommended that you use ``VPC`` as the ``EndpointType`` . With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with ``EndpointType`` set to ``VPC_ENDPOINT`` .
        :param identity_provider_details: Required when ``IdentityProviderType`` is set to ``AWS_DIRECTORY_SERVICE`` , ``AWS _LAMBDA`` or ``API_GATEWAY`` . Accepts an array containing all of the information required to use a directory in ``AWS_DIRECTORY_SERVICE`` or invoke a customer-supplied authentication API, including the API Gateway URL. Not required when ``IdentityProviderType`` is set to ``SERVICE_MANAGED`` .
        :param identity_provider_type: The mode of authentication for a server. The default value is ``SERVICE_MANAGED`` , which allows you to store and access user credentials within the AWS Transfer Family service. Use ``AWS_DIRECTORY_SERVICE`` to provide access to Active Directory groups in AWS Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in AWS using AD Connector. This option also requires you to provide a Directory ID by using the ``IdentityProviderDetails`` parameter. Use the ``API_GATEWAY`` value to integrate with an identity provider of your choosing. The ``API_GATEWAY`` setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the ``IdentityProviderDetails`` parameter. Use the ``AWS_LAMBDA`` value to directly use an AWS Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the ``Function`` parameter for the ``IdentityProviderDetails`` data type.
        :param logging_role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFSevents. When set, you can view user activity in your CloudWatch logs.
        :param post_authentication_login_banner: Specifies a string to display when users connect to a server. This string is displayed after the user authenticates. .. epigraph:: The SFTP protocol does not support post-authentication display banners.
        :param pre_authentication_login_banner: Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system: ``This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.``
        :param protocol_details: The protocol settings that are configured for your server. - To indicate passive mode (for FTP and FTPS protocols), use the ``PassiveIp`` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. - To ignore the error that is generated when the client attempts to use the ``SETSTAT`` command on a file that you are uploading to an Amazon S3 bucket, use the ``SetStatOption`` parameter. To have the AWS Transfer Family server ignore the ``SETSTAT`` command and upload files without needing to make any changes to your SFTP client, set the value to ``ENABLE_NO_OP`` . If you set the ``SetStatOption`` parameter to ``ENABLE_NO_OP`` , Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a ``SETSTAT`` call. - To determine whether your AWS Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the ``TlsSessionResumptionMode`` parameter. - ``As2Transports`` indicates the transport method for the AS2 messages. Currently, only HTTP is supported. The ``Protocols`` parameter is an array of strings. *Allowed values* : One or more of ``SFTP`` , ``FTPS`` , ``FTP`` , ``AS2``
        :param protocols: Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are: - ``SFTP`` (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH - ``FTPS`` (File Transfer Protocol Secure): File transfer with TLS encryption - ``FTP`` (File Transfer Protocol): Unencrypted file transfer - ``AS2`` (Applicability Statement 2): used for transporting structured business-to-business data .. epigraph:: - If you select ``FTPS`` , you must choose a certificate stored in AWS Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS. - If ``Protocol`` includes either ``FTP`` or ``FTPS`` , then the ``EndpointType`` must be ``VPC`` and the ``IdentityProviderType`` must be either ``AWS_DIRECTORY_SERVICE`` , ``AWS_LAMBDA`` , or ``API_GATEWAY`` . - If ``Protocol`` includes ``FTP`` , then ``AddressAllocationIds`` cannot be associated. - If ``Protocol`` is set only to ``SFTP`` , the ``EndpointType`` can be set to ``PUBLIC`` and the ``IdentityProviderType`` can be set any of the supported identity types: ``SERVICE_MANAGED`` , ``AWS_DIRECTORY_SERVICE`` , ``AWS_LAMBDA`` , or ``API_GATEWAY`` . - If ``Protocol`` includes ``AS2`` , then the ``EndpointType`` must be ``VPC`` , and domain must be Amazon S3. The ``Protocols`` parameter is an array of strings. *Allowed values* : One or more of ``SFTP`` , ``FTPS`` , ``FTP`` , ``AS2``
        :param s3_storage_options: Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default. By default, home directory mappings have a ``TYPE`` of ``DIRECTORY`` . If you enable this option, you would then need to explicitly set the ``HomeDirectoryMapEntry`` ``Type`` to ``FILE`` if you want a mapping to have a file target.
        :param security_policy_name: Specifies the name of the security policy for the server.
        :param structured_log_destinations: Specifies the log groups to which your server logs are sent. To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows: ``arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*`` For example, ``arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*`` If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an ``update-server`` call. For example: ``update-server --server-id s-1234567890abcdef0 --structured-log-destinations``
        :param tags: Key-value pairs that can be used to group and search for servers.
        :param workflow_details: Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow. In addition to a workflow to execute when a file is uploaded completely, ``WorkflowDetails`` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when a file is open when the session disconnects.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf4192baa4fd5a52c9092a6bab5b78398f0e5f14bdad138f58e7990699f038ae)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServerProps(
            certificate=certificate,
            domain=domain,
            endpoint_details=endpoint_details,
            endpoint_type=endpoint_type,
            identity_provider_details=identity_provider_details,
            identity_provider_type=identity_provider_type,
            logging_role=logging_role,
            post_authentication_login_banner=post_authentication_login_banner,
            pre_authentication_login_banner=pre_authentication_login_banner,
            protocol_details=protocol_details,
            protocols=protocols,
            s3_storage_options=s3_storage_options,
            security_policy_name=security_policy_name,
            structured_log_destinations=structured_log_destinations,
            tags=tags,
            workflow_details=workflow_details,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a102be38a6d3ae9d49e28b8883914d07542c58d9491bf5753554a0113ffa87f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b97045b0c5fc436bbcfa181809dbf495470f670463751ef7893661923f939bd5)
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
        '''The Amazon Resource Name associated with the server, in the form ``arn:aws:transfer:region: *account-id* :server/ *server-id* /`` .

        An example of a server ARN is: ``arn:aws:transfer:us-east-1:123456789012:server/s-01234567890abcdef`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> builtins.str:
        '''The service-assigned ID of the server that is created.

        An example ``ServerId`` is ``s-01234567890abcdef`` .

        :cloudformationAttribute: ServerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerId"))

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
    @jsii.member(jsii_name="certificate")
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificate"))

    @certificate.setter
    def certificate(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d563df1c135ed9313e3dcb00bca6377542fc063b499e5019b63083d76d98d4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificate", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(self) -> typing.Optional[builtins.str]:
        '''Specifies the domain of the storage system that is used for file transfers.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "domain"))

    @domain.setter
    def domain(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fec79565f0dbe159eaa20c23eb0a3a83bd02830760cb60e52cacf1a4cb63a759)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="endpointDetails")
    def endpoint_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.EndpointDetailsProperty"]]:
        '''The virtual private cloud (VPC) endpoint settings that are configured for your server.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.EndpointDetailsProperty"]], jsii.get(self, "endpointDetails"))

    @endpoint_details.setter
    def endpoint_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.EndpointDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__823691982357b872378325dd203d71148265650854d8786177cbfe72d5cd1cef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointDetails", value)

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''The type of endpoint that you want your server to use.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__00ba0605ab69aa9a51bf216b956c181794abc5a526276ac4b9db623c6c0bf7b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderDetails")
    def identity_provider_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.IdentityProviderDetailsProperty"]]:
        '''Required when ``IdentityProviderType`` is set to ``AWS_DIRECTORY_SERVICE`` , ``AWS _LAMBDA`` or ``API_GATEWAY`` .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.IdentityProviderDetailsProperty"]], jsii.get(self, "identityProviderDetails"))

    @identity_provider_details.setter
    def identity_provider_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.IdentityProviderDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1216795787e100411fafd375b3cfc4b841d96cdfab5edb3bdaad0c4035f93113)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderDetails", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderType")
    def identity_provider_type(self) -> typing.Optional[builtins.str]:
        '''The mode of authentication for a server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityProviderType"))

    @identity_provider_type.setter
    def identity_provider_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a6cb2bcf7a55379e6b89fa02d0735271e11fc131bf9d9b0693cea393aa4401)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderType", value)

    @builtins.property
    @jsii.member(jsii_name="loggingRole")
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFSevents.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "loggingRole"))

    @logging_role.setter
    def logging_role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85db09859b7fcfcae20f45283fb5e74d7f731e8583b8055856472647123250d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "loggingRole", value)

    @builtins.property
    @jsii.member(jsii_name="postAuthenticationLoginBanner")
    def post_authentication_login_banner(self) -> typing.Optional[builtins.str]:
        '''Specifies a string to display when users connect to a server.

        This string is displayed after the user authenticates.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "postAuthenticationLoginBanner"))

    @post_authentication_login_banner.setter
    def post_authentication_login_banner(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1dfef6051ebbe7b359e51fbbccf44bdd359cd353801a4563eec263eef777c769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postAuthenticationLoginBanner", value)

    @builtins.property
    @jsii.member(jsii_name="preAuthenticationLoginBanner")
    def pre_authentication_login_banner(self) -> typing.Optional[builtins.str]:
        '''Specifies a string to display when users connect to a server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preAuthenticationLoginBanner"))

    @pre_authentication_login_banner.setter
    def pre_authentication_login_banner(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__285d90628b0741ae262fa6e66817df857f96385dc0d6e597c8117867ee84ced2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preAuthenticationLoginBanner", value)

    @builtins.property
    @jsii.member(jsii_name="protocolDetails")
    def protocol_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.ProtocolDetailsProperty"]]:
        '''The protocol settings that are configured for your server.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.ProtocolDetailsProperty"]], jsii.get(self, "protocolDetails"))

    @protocol_details.setter
    def protocol_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.ProtocolDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a9f48a90693f920a173d0269d8553ecc5b0e8d2f2d14cb94fe1075b3651a3d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolDetails", value)

    @builtins.property
    @jsii.member(jsii_name="protocols")
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "protocols"))

    @protocols.setter
    def protocols(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fd2c10237c6e32f4456347dbaa9e2a6133f24a85fbbc337ffc36e289abcbeae1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocols", value)

    @builtins.property
    @jsii.member(jsii_name="s3StorageOptions")
    def s3_storage_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.S3StorageOptionsProperty"]]:
        '''Specifies whether or not performance for your Amazon S3 directories is optimized.

        This is disabled by default.
        '''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.S3StorageOptionsProperty"]], jsii.get(self, "s3StorageOptions"))

    @s3_storage_options.setter
    def s3_storage_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.S3StorageOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__163a1c09687c961e3488fbf0c1737554423fa0fc38fcd229be5018973ec9bb51)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3StorageOptions", value)

    @builtins.property
    @jsii.member(jsii_name="securityPolicyName")
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the security policy for the server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityPolicyName"))

    @security_policy_name.setter
    def security_policy_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__61c01276e220c0838559c857ba2fd6565aeb281872677b4ec1a9cf3ef85100bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityPolicyName", value)

    @builtins.property
    @jsii.member(jsii_name="structuredLogDestinations")
    def structured_log_destinations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the log groups to which your server logs are sent.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "structuredLogDestinations"))

    @structured_log_destinations.setter
    def structured_log_destinations(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f11770f5eaa4f458a4acec04511188ac9b4a7a0177f6c2e8de622a00cd0a8700)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "structuredLogDestinations", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for servers.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6c88c4497661801373ac6dc027449a26f4bf736a03ee6cf692728004fb17b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="workflowDetails")
    def workflow_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailsProperty"]]:
        '''Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailsProperty"]], jsii.get(self, "workflowDetails"))

    @workflow_details.setter
    def workflow_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b4b59cf92c244a6a1f87cc398c2d4baeea212278bda328f2dd6f2c84abc67e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "workflowDetails", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnServer.EndpointDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "address_allocation_ids": "addressAllocationIds",
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
            "vpc_endpoint_id": "vpcEndpointId",
            "vpc_id": "vpcId",
        },
    )
    class EndpointDetailsProperty:
        def __init__(
            self,
            *,
            address_allocation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            vpc_endpoint_id: typing.Optional[builtins.str] = None,
            vpc_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The virtual private cloud (VPC) endpoint settings that are configured for your server.

            When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.

            :param address_allocation_ids: A list of address allocation IDs that are required to attach an Elastic IP address to your server's endpoint. An address allocation ID corresponds to the allocation ID of an Elastic IP address. This value can be retrieved from the ``allocationId`` field from the Amazon EC2 `Address <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html>`_ data type. One way to retrieve this value is by calling the EC2 `DescribeAddresses <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html>`_ API. This parameter is optional. Set this parameter if you want to make your VPC endpoint public-facing. For details, see `Create an internet-facing endpoint for your server <https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint>`_ . .. epigraph:: This property can only be set as follows: - ``EndpointType`` must be set to ``VPC`` - The Transfer Family server must be offline. - You cannot set this parameter for Transfer Family servers that use the FTP protocol. - The server must already have ``SubnetIds`` populated ( ``SubnetIds`` and ``AddressAllocationIds`` cannot be updated simultaneously). - ``AddressAllocationIds`` can't contain duplicates, and must be equal in length to ``SubnetIds`` . For example, if you have three subnet IDs, you must also specify three address allocation IDs. - Call the ``UpdateServer`` API to set or change this parameter.
            :param security_group_ids: A list of security groups IDs that are available to attach to your server's endpoint. .. epigraph:: This property can only be set when ``EndpointType`` is set to ``VPC`` . You can edit the ``SecurityGroupIds`` property in the `UpdateServer <https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html>`_ API only if you are changing the ``EndpointType`` from ``PUBLIC`` or ``VPC_ENDPOINT`` to ``VPC`` . To change security groups associated with your server's VPC endpoint after creation, use the Amazon EC2 `ModifyVpcEndpoint <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html>`_ API.
            :param subnet_ids: A list of subnet IDs that are required to host your server endpoint in your VPC. .. epigraph:: This property can only be set when ``EndpointType`` is set to ``VPC`` .
            :param vpc_endpoint_id: The ID of the VPC endpoint. .. epigraph:: This property can only be set when ``EndpointType`` is set to ``VPC_ENDPOINT`` .
            :param vpc_id: The VPC ID of the virtual private cloud in which the server's endpoint will be hosted. .. epigraph:: This property can only be set when ``EndpointType`` is set to ``VPC`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                endpoint_details_property = transfer.CfnServer.EndpointDetailsProperty(
                    address_allocation_ids=["addressAllocationIds"],
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e86c738b4725d61d9fcf1e57609114312f1194c719c25f07a2b6061397bb99d7)
                check_type(argname="argument address_allocation_ids", value=address_allocation_ids, expected_type=type_hints["address_allocation_ids"])
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
                check_type(argname="argument vpc_endpoint_id", value=vpc_endpoint_id, expected_type=type_hints["vpc_endpoint_id"])
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if address_allocation_ids is not None:
                self._values["address_allocation_ids"] = address_allocation_ids
            if security_group_ids is not None:
                self._values["security_group_ids"] = security_group_ids
            if subnet_ids is not None:
                self._values["subnet_ids"] = subnet_ids
            if vpc_endpoint_id is not None:
                self._values["vpc_endpoint_id"] = vpc_endpoint_id
            if vpc_id is not None:
                self._values["vpc_id"] = vpc_id

        @builtins.property
        def address_allocation_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of address allocation IDs that are required to attach an Elastic IP address to your server's endpoint.

            An address allocation ID corresponds to the allocation ID of an Elastic IP address. This value can be retrieved from the ``allocationId`` field from the Amazon EC2 `Address <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Address.html>`_ data type. One way to retrieve this value is by calling the EC2 `DescribeAddresses <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAddresses.html>`_ API.

            This parameter is optional. Set this parameter if you want to make your VPC endpoint public-facing. For details, see `Create an internet-facing endpoint for your server <https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#create-internet-facing-endpoint>`_ .
            .. epigraph::

               This property can only be set as follows:

               - ``EndpointType`` must be set to ``VPC``
               - The Transfer Family server must be offline.
               - You cannot set this parameter for Transfer Family servers that use the FTP protocol.
               - The server must already have ``SubnetIds`` populated ( ``SubnetIds`` and ``AddressAllocationIds`` cannot be updated simultaneously).
               - ``AddressAllocationIds`` can't contain duplicates, and must be equal in length to ``SubnetIds`` . For example, if you have three subnet IDs, you must also specify three address allocation IDs.
               - Call the ``UpdateServer`` API to set or change this parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-addressallocationids
            '''
            result = self._values.get("address_allocation_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of security groups IDs that are available to attach to your server's endpoint.

            .. epigraph::

               This property can only be set when ``EndpointType`` is set to ``VPC`` .

               You can edit the ``SecurityGroupIds`` property in the `UpdateServer <https://docs.aws.amazon.com/transfer/latest/userguide/API_UpdateServer.html>`_ API only if you are changing the ``EndpointType`` from ``PUBLIC`` or ``VPC_ENDPOINT`` to ``VPC`` . To change security groups associated with your server's VPC endpoint after creation, use the Amazon EC2 `ModifyVpcEndpoint <https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyVpcEndpoint.html>`_ API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def subnet_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of subnet IDs that are required to host your server endpoint in your VPC.

            .. epigraph::

               This property can only be set when ``EndpointType`` is set to ``VPC`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-subnetids
            '''
            result = self._values.get("subnet_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def vpc_endpoint_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the VPC endpoint.

            .. epigraph::

               This property can only be set when ``EndpointType`` is set to ``VPC_ENDPOINT`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcendpointid
            '''
            result = self._values.get("vpc_endpoint_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_id(self) -> typing.Optional[builtins.str]:
            '''The VPC ID of the virtual private cloud in which the server's endpoint will be hosted.

            .. epigraph::

               This property can only be set when ``EndpointType`` is set to ``VPC`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-endpointdetails.html#cfn-transfer-server-endpointdetails-vpcid
            '''
            result = self._values.get("vpc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnServer.IdentityProviderDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_id": "directoryId",
            "function": "function",
            "invocation_role": "invocationRole",
            "sftp_authentication_methods": "sftpAuthenticationMethods",
            "url": "url",
        },
    )
    class IdentityProviderDetailsProperty:
        def __init__(
            self,
            *,
            directory_id: typing.Optional[builtins.str] = None,
            function: typing.Optional[builtins.str] = None,
            invocation_role: typing.Optional[builtins.str] = None,
            sftp_authentication_methods: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Required when ``IdentityProviderType`` is set to ``AWS_DIRECTORY_SERVICE`` , ``AWS _LAMBDA`` or ``API_GATEWAY`` .

            Accepts an array containing all of the information required to use a directory in ``AWS_DIRECTORY_SERVICE`` or invoke a customer-supplied authentication API, including the API Gateway URL. Not required when ``IdentityProviderType`` is set to ``SERVICE_MANAGED`` .

            :param directory_id: The identifier of the AWS Directory Service directory that you want to use as your identity provider.
            :param function: The ARN for a Lambda function to use for the Identity provider.
            :param invocation_role: This parameter is only applicable if your ``IdentityProviderType`` is ``API_GATEWAY`` . Provides the type of ``InvocationRole`` used to authenticate the user account.
            :param sftp_authentication_methods: For SFTP-enabled servers, and for custom identity providers *only* , you can specify whether to authenticate using a password, SSH key pair, or both. - ``PASSWORD`` - users must provide their password to connect. - ``PUBLIC_KEY`` - users must provide their private key to connect. - ``PUBLIC_KEY_OR_PASSWORD`` - users can authenticate with either their password or their key. This is the default value. - ``PUBLIC_KEY_AND_PASSWORD`` - users must provide both their private key and their password to connect. The server checks the key first, and then if the key is valid, the system prompts for a password. If the private key provided does not match the public key that is stored, authentication fails.
            :param url: Provides the location of the service endpoint used to authenticate users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                identity_provider_details_property = transfer.CfnServer.IdentityProviderDetailsProperty(
                    directory_id="directoryId",
                    function="function",
                    invocation_role="invocationRole",
                    sftp_authentication_methods="sftpAuthenticationMethods",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8252699fb02969aa8fc67db81cc180b0bb34e8f04f1c627cb561c7fe4f3bb85f)
                check_type(argname="argument directory_id", value=directory_id, expected_type=type_hints["directory_id"])
                check_type(argname="argument function", value=function, expected_type=type_hints["function"])
                check_type(argname="argument invocation_role", value=invocation_role, expected_type=type_hints["invocation_role"])
                check_type(argname="argument sftp_authentication_methods", value=sftp_authentication_methods, expected_type=type_hints["sftp_authentication_methods"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if directory_id is not None:
                self._values["directory_id"] = directory_id
            if function is not None:
                self._values["function"] = function
            if invocation_role is not None:
                self._values["invocation_role"] = invocation_role
            if sftp_authentication_methods is not None:
                self._values["sftp_authentication_methods"] = sftp_authentication_methods
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def directory_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the AWS Directory Service directory that you want to use as your identity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-directoryid
            '''
            result = self._values.get("directory_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def function(self) -> typing.Optional[builtins.str]:
            '''The ARN for a Lambda function to use for the Identity provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-function
            '''
            result = self._values.get("function")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def invocation_role(self) -> typing.Optional[builtins.str]:
            '''This parameter is only applicable if your ``IdentityProviderType`` is ``API_GATEWAY`` .

            Provides the type of ``InvocationRole`` used to authenticate the user account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-invocationrole
            '''
            result = self._values.get("invocation_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sftp_authentication_methods(self) -> typing.Optional[builtins.str]:
            '''For SFTP-enabled servers, and for custom identity providers *only* , you can specify whether to authenticate using a password, SSH key pair, or both.

            - ``PASSWORD`` - users must provide their password to connect.
            - ``PUBLIC_KEY`` - users must provide their private key to connect.
            - ``PUBLIC_KEY_OR_PASSWORD`` - users can authenticate with either their password or their key. This is the default value.
            - ``PUBLIC_KEY_AND_PASSWORD`` - users must provide both their private key and their password to connect. The server checks the key first, and then if the key is valid, the system prompts for a password. If the private key provided does not match the public key that is stored, authentication fails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-sftpauthenticationmethods
            '''
            result = self._values.get("sftp_authentication_methods")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''Provides the location of the service endpoint used to authenticate users.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-identityproviderdetails.html#cfn-transfer-server-identityproviderdetails-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProviderDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnServer.ProtocolDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "as2_transports": "as2Transports",
            "passive_ip": "passiveIp",
            "set_stat_option": "setStatOption",
            "tls_session_resumption_mode": "tlsSessionResumptionMode",
        },
    )
    class ProtocolDetailsProperty:
        def __init__(
            self,
            *,
            as2_transports: typing.Optional[typing.Sequence[builtins.str]] = None,
            passive_ip: typing.Optional[builtins.str] = None,
            set_stat_option: typing.Optional[builtins.str] = None,
            tls_session_resumption_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The protocol settings that are configured for your server.

            - To indicate passive mode (for FTP and FTPS protocols), use the ``PassiveIp`` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer.
            - To ignore the error that is generated when the client attempts to use the ``SETSTAT`` command on a file that you are uploading to an Amazon S3 bucket, use the ``SetStatOption`` parameter. To have the AWS Transfer Family server ignore the ``SETSTAT`` command and upload files without needing to make any changes to your SFTP client, set the value to ``ENABLE_NO_OP`` . If you set the ``SetStatOption`` parameter to ``ENABLE_NO_OP`` , Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a ``SETSTAT`` call.
            - To determine whether your AWS Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the ``TlsSessionResumptionMode`` parameter.
            - ``As2Transports`` indicates the transport method for the AS2 messages. Currently, only HTTP is supported.

            :param as2_transports: List of ``As2Transport`` objects.
            :param passive_ip: Indicates passive mode, for FTP and FTPS protocols. Enter a single IPv4 address, such as the public IP address of a firewall, router, or load balancer. For example: ``aws transfer update-server --protocol-details PassiveIp=0.0.0.0`` Replace ``0.0.0.0`` in the example above with the actual IP address you want to use. .. epigraph:: If you change the ``PassiveIp`` value, you must stop and then restart your Transfer Family server for the change to take effect. For details on using passive mode (PASV) in a NAT environment, see `Configuring your FTPS server behind a firewall or NAT with AWS Transfer Family <https://docs.aws.amazon.com/storage/configuring-your-ftps-server-behind-a-firewall-or-nat-with-aws-transfer-family/>`_ . *Special values* The ``AUTO`` and ``0.0.0.0`` are special values for the ``PassiveIp`` parameter. The value ``PassiveIp=AUTO`` is assigned by default to FTP and FTPS type servers. In this case, the server automatically responds with one of the endpoint IPs within the PASV response. ``PassiveIp=0.0.0.0`` has a more unique application for its usage. For example, if you have a High Availability (HA) Network Load Balancer (NLB) environment, where you have 3 subnets, you can only specify a single IP address using the ``PassiveIp`` parameter. This reduces the effectiveness of having High Availability. In this case, you can specify ``PassiveIp=0.0.0.0`` . This tells the client to use the same IP address as the Control connection and utilize all AZs for their connections. Note, however, that not all FTP clients support the ``PassiveIp=0.0.0.0`` response. FileZilla and WinSCP do support it. If you are using other clients, check to see if your client supports the ``PassiveIp=0.0.0.0`` response.
            :param set_stat_option: Use the ``SetStatOption`` to ignore the error that is generated when the client attempts to use ``SETSTAT`` on a file you are uploading to an S3 bucket. Some SFTP file transfer clients can attempt to change the attributes of remote files, including timestamp and permissions, using commands, such as ``SETSTAT`` when uploading the file. However, these commands are not compatible with object storage systems, such as Amazon S3. Due to this incompatibility, file uploads from these clients can result in errors even when the file is otherwise successfully uploaded. Set the value to ``ENABLE_NO_OP`` to have the Transfer Family server ignore the ``SETSTAT`` command, and upload files without needing to make any changes to your SFTP client. While the ``SetStatOption`` ``ENABLE_NO_OP`` setting ignores the error, it does generate a log entry in Amazon CloudWatch Logs, so you can determine when the client is making a ``SETSTAT`` call. .. epigraph:: If you want to preserve the original timestamp for your file, and modify other file attributes using ``SETSTAT`` , you can use Amazon EFS as backend storage with Transfer Family.
            :param tls_session_resumption_mode: A property used with Transfer Family servers that use the FTPS protocol. TLS Session Resumption provides a mechanism to resume or share a negotiated secret key between the control and data connection for an FTPS session. ``TlsSessionResumptionMode`` determines whether or not the server resumes recent, negotiated sessions through a unique session ID. This property is available during ``CreateServer`` and ``UpdateServer`` calls. If a ``TlsSessionResumptionMode`` value is not specified during ``CreateServer`` , it is set to ``ENFORCED`` by default. - ``DISABLED`` : the server does not process TLS session resumption client requests and creates a new TLS session for each request. - ``ENABLED`` : the server processes and accepts clients that are performing TLS session resumption. The server doesn't reject client data connections that do not perform the TLS session resumption client processing. - ``ENFORCED`` : the server processes and accepts clients that are performing TLS session resumption. The server rejects client data connections that do not perform the TLS session resumption client processing. Before you set the value to ``ENFORCED`` , test your clients. .. epigraph:: Not all FTPS clients perform TLS session resumption. So, if you choose to enforce TLS session resumption, you prevent any connections from FTPS clients that don't perform the protocol negotiation. To determine whether or not you can use the ``ENFORCED`` value, you need to test your clients.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                protocol_details_property = transfer.CfnServer.ProtocolDetailsProperty(
                    as2_transports=["as2Transports"],
                    passive_ip="passiveIp",
                    set_stat_option="setStatOption",
                    tls_session_resumption_mode="tlsSessionResumptionMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b1af46c3c18a62e5483e3be74497e66aaecc076ccfe0d473686a4e4b38255cc)
                check_type(argname="argument as2_transports", value=as2_transports, expected_type=type_hints["as2_transports"])
                check_type(argname="argument passive_ip", value=passive_ip, expected_type=type_hints["passive_ip"])
                check_type(argname="argument set_stat_option", value=set_stat_option, expected_type=type_hints["set_stat_option"])
                check_type(argname="argument tls_session_resumption_mode", value=tls_session_resumption_mode, expected_type=type_hints["tls_session_resumption_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if as2_transports is not None:
                self._values["as2_transports"] = as2_transports
            if passive_ip is not None:
                self._values["passive_ip"] = passive_ip
            if set_stat_option is not None:
                self._values["set_stat_option"] = set_stat_option
            if tls_session_resumption_mode is not None:
                self._values["tls_session_resumption_mode"] = tls_session_resumption_mode

        @builtins.property
        def as2_transports(self) -> typing.Optional[typing.List[builtins.str]]:
            '''List of ``As2Transport`` objects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-as2transports
            '''
            result = self._values.get("as2_transports")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def passive_ip(self) -> typing.Optional[builtins.str]:
            '''Indicates passive mode, for FTP and FTPS protocols.

            Enter a single IPv4 address, such as the public IP address of a firewall, router, or load balancer. For example:

            ``aws transfer update-server --protocol-details PassiveIp=0.0.0.0``

            Replace ``0.0.0.0`` in the example above with the actual IP address you want to use.
            .. epigraph::

               If you change the ``PassiveIp`` value, you must stop and then restart your Transfer Family server for the change to take effect. For details on using passive mode (PASV) in a NAT environment, see `Configuring your FTPS server behind a firewall or NAT with AWS Transfer Family <https://docs.aws.amazon.com/storage/configuring-your-ftps-server-behind-a-firewall-or-nat-with-aws-transfer-family/>`_ .

            *Special values*

            The ``AUTO`` and ``0.0.0.0`` are special values for the ``PassiveIp`` parameter. The value ``PassiveIp=AUTO`` is assigned by default to FTP and FTPS type servers. In this case, the server automatically responds with one of the endpoint IPs within the PASV response. ``PassiveIp=0.0.0.0`` has a more unique application for its usage. For example, if you have a High Availability (HA) Network Load Balancer (NLB) environment, where you have 3 subnets, you can only specify a single IP address using the ``PassiveIp`` parameter. This reduces the effectiveness of having High Availability. In this case, you can specify ``PassiveIp=0.0.0.0`` . This tells the client to use the same IP address as the Control connection and utilize all AZs for their connections. Note, however, that not all FTP clients support the ``PassiveIp=0.0.0.0`` response. FileZilla and WinSCP do support it. If you are using other clients, check to see if your client supports the ``PassiveIp=0.0.0.0`` response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-passiveip
            '''
            result = self._values.get("passive_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def set_stat_option(self) -> typing.Optional[builtins.str]:
            '''Use the ``SetStatOption`` to ignore the error that is generated when the client attempts to use ``SETSTAT`` on a file you are uploading to an S3 bucket.

            Some SFTP file transfer clients can attempt to change the attributes of remote files, including timestamp and permissions, using commands, such as ``SETSTAT`` when uploading the file. However, these commands are not compatible with object storage systems, such as Amazon S3. Due to this incompatibility, file uploads from these clients can result in errors even when the file is otherwise successfully uploaded.

            Set the value to ``ENABLE_NO_OP`` to have the Transfer Family server ignore the ``SETSTAT`` command, and upload files without needing to make any changes to your SFTP client. While the ``SetStatOption`` ``ENABLE_NO_OP`` setting ignores the error, it does generate a log entry in Amazon CloudWatch Logs, so you can determine when the client is making a ``SETSTAT`` call.
            .. epigraph::

               If you want to preserve the original timestamp for your file, and modify other file attributes using ``SETSTAT`` , you can use Amazon EFS as backend storage with Transfer Family.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-setstatoption
            '''
            result = self._values.get("set_stat_option")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tls_session_resumption_mode(self) -> typing.Optional[builtins.str]:
            '''A property used with Transfer Family servers that use the FTPS protocol.

            TLS Session Resumption provides a mechanism to resume or share a negotiated secret key between the control and data connection for an FTPS session. ``TlsSessionResumptionMode`` determines whether or not the server resumes recent, negotiated sessions through a unique session ID. This property is available during ``CreateServer`` and ``UpdateServer`` calls. If a ``TlsSessionResumptionMode`` value is not specified during ``CreateServer`` , it is set to ``ENFORCED`` by default.

            - ``DISABLED`` : the server does not process TLS session resumption client requests and creates a new TLS session for each request.
            - ``ENABLED`` : the server processes and accepts clients that are performing TLS session resumption. The server doesn't reject client data connections that do not perform the TLS session resumption client processing.
            - ``ENFORCED`` : the server processes and accepts clients that are performing TLS session resumption. The server rejects client data connections that do not perform the TLS session resumption client processing. Before you set the value to ``ENFORCED`` , test your clients.

            .. epigraph::

               Not all FTPS clients perform TLS session resumption. So, if you choose to enforce TLS session resumption, you prevent any connections from FTPS clients that don't perform the protocol negotiation. To determine whether or not you can use the ``ENFORCED`` value, you need to test your clients.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-protocoldetails.html#cfn-transfer-server-protocoldetails-tlssessionresumptionmode
            '''
            result = self._values.get("tls_session_resumption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProtocolDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnServer.S3StorageOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "directory_listing_optimization": "directoryListingOptimization",
        },
    )
    class S3StorageOptionsProperty:
        def __init__(
            self,
            *,
            directory_listing_optimization: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The Amazon S3 storage options that are configured for your server.

            :param directory_listing_optimization: Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default. By default, home directory mappings have a ``TYPE`` of ``DIRECTORY`` . If you enable this option, you would then need to explicitly set the ``HomeDirectoryMapEntry`` ``Type`` to ``FILE`` if you want a mapping to have a file target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-s3storageoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                s3_storage_options_property = transfer.CfnServer.S3StorageOptionsProperty(
                    directory_listing_optimization="directoryListingOptimization"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7f2be4894cf62db2547a5d072c4de8c6e51d04c741195403ed629be98852110)
                check_type(argname="argument directory_listing_optimization", value=directory_listing_optimization, expected_type=type_hints["directory_listing_optimization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if directory_listing_optimization is not None:
                self._values["directory_listing_optimization"] = directory_listing_optimization

        @builtins.property
        def directory_listing_optimization(self) -> typing.Optional[builtins.str]:
            '''Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default.

            By default, home directory mappings have a ``TYPE`` of ``DIRECTORY`` . If you enable this option, you would then need to explicitly set the ``HomeDirectoryMapEntry`` ``Type`` to ``FILE`` if you want a mapping to have a file target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-s3storageoptions.html#cfn-transfer-server-s3storageoptions-directorylistingoptimization
            '''
            result = self._values.get("directory_listing_optimization")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3StorageOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnServer.WorkflowDetailProperty",
        jsii_struct_bases=[],
        name_mapping={"execution_role": "executionRole", "workflow_id": "workflowId"},
    )
    class WorkflowDetailProperty:
        def __init__(
            self,
            *,
            execution_role: builtins.str,
            workflow_id: builtins.str,
        ) -> None:
            '''Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.

            In addition to a workflow to execute when a file is uploaded completely, ``WorkflowDetails`` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when a file is open when the session disconnects.

            :param execution_role: Includes the necessary permissions for S3, EFS, and Lambda operations that Transfer can assume, so that all workflow steps can operate on the required resources.
            :param workflow_id: A unique identifier for the workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                workflow_detail_property = transfer.CfnServer.WorkflowDetailProperty(
                    execution_role="executionRole",
                    workflow_id="workflowId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03eaccaa8c41960eed5ac1d533ff7d5c2d5b8fb55954177db820e8382860df05)
                check_type(argname="argument execution_role", value=execution_role, expected_type=type_hints["execution_role"])
                check_type(argname="argument workflow_id", value=workflow_id, expected_type=type_hints["workflow_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "execution_role": execution_role,
                "workflow_id": workflow_id,
            }

        @builtins.property
        def execution_role(self) -> builtins.str:
            '''Includes the necessary permissions for S3, EFS, and Lambda operations that Transfer can assume, so that all workflow steps can operate on the required resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-executionrole
            '''
            result = self._values.get("execution_role")
            assert result is not None, "Required property 'execution_role' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def workflow_id(self) -> builtins.str:
            '''A unique identifier for the workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetail.html#cfn-transfer-server-workflowdetail-workflowid
            '''
            result = self._values.get("workflow_id")
            assert result is not None, "Required property 'workflow_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowDetailProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnServer.WorkflowDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"on_partial_upload": "onPartialUpload", "on_upload": "onUpload"},
    )
    class WorkflowDetailsProperty:
        def __init__(
            self,
            *,
            on_partial_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.WorkflowDetailProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            on_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnServer.WorkflowDetailProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Container for the ``WorkflowDetail`` data type.

            It is used by actions that trigger a workflow to begin execution.

            :param on_partial_upload: A trigger that starts a workflow if a file is only partially uploaded. You can attach a workflow to a server that executes whenever there is a partial upload. A *partial upload* occurs when a file is open when the session disconnects.
            :param on_upload: A trigger that starts a workflow: the workflow begins to execute after a file is uploaded. To remove an associated workflow from a server, you can provide an empty ``OnUpload`` object, as in the following example. ``aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                workflow_details_property = transfer.CfnServer.WorkflowDetailsProperty(
                    on_partial_upload=[transfer.CfnServer.WorkflowDetailProperty(
                        execution_role="executionRole",
                        workflow_id="workflowId"
                    )],
                    on_upload=[transfer.CfnServer.WorkflowDetailProperty(
                        execution_role="executionRole",
                        workflow_id="workflowId"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0511d1dd99e09b5726ca7209160f14134b7339c966fe43485d5e7f3ee614892)
                check_type(argname="argument on_partial_upload", value=on_partial_upload, expected_type=type_hints["on_partial_upload"])
                check_type(argname="argument on_upload", value=on_upload, expected_type=type_hints["on_upload"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if on_partial_upload is not None:
                self._values["on_partial_upload"] = on_partial_upload
            if on_upload is not None:
                self._values["on_upload"] = on_upload

        @builtins.property
        def on_partial_upload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailProperty"]]]]:
            '''A trigger that starts a workflow if a file is only partially uploaded.

            You can attach a workflow to a server that executes whenever there is a partial upload.

            A *partial upload* occurs when a file is open when the session disconnects.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html#cfn-transfer-server-workflowdetails-onpartialupload
            '''
            result = self._values.get("on_partial_upload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailProperty"]]]], result)

        @builtins.property
        def on_upload(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailProperty"]]]]:
            '''A trigger that starts a workflow: the workflow begins to execute after a file is uploaded.

            To remove an associated workflow from a server, you can provide an empty ``OnUpload`` object, as in the following example.

            ``aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-server-workflowdetails.html#cfn-transfer-server-workflowdetails-onupload
            '''
            result = self._values.get("on_upload")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnServer.WorkflowDetailProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnServerProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate": "certificate",
        "domain": "domain",
        "endpoint_details": "endpointDetails",
        "endpoint_type": "endpointType",
        "identity_provider_details": "identityProviderDetails",
        "identity_provider_type": "identityProviderType",
        "logging_role": "loggingRole",
        "post_authentication_login_banner": "postAuthenticationLoginBanner",
        "pre_authentication_login_banner": "preAuthenticationLoginBanner",
        "protocol_details": "protocolDetails",
        "protocols": "protocols",
        "s3_storage_options": "s3StorageOptions",
        "security_policy_name": "securityPolicyName",
        "structured_log_destinations": "structuredLogDestinations",
        "tags": "tags",
        "workflow_details": "workflowDetails",
    },
)
class CfnServerProps:
    def __init__(
        self,
        *,
        certificate: typing.Optional[builtins.str] = None,
        domain: typing.Optional[builtins.str] = None,
        endpoint_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        endpoint_type: typing.Optional[builtins.str] = None,
        identity_provider_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.IdentityProviderDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        identity_provider_type: typing.Optional[builtins.str] = None,
        logging_role: typing.Optional[builtins.str] = None,
        post_authentication_login_banner: typing.Optional[builtins.str] = None,
        pre_authentication_login_banner: typing.Optional[builtins.str] = None,
        protocol_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.ProtocolDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
        s3_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.S3StorageOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        security_policy_name: typing.Optional[builtins.str] = None,
        structured_log_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        workflow_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.WorkflowDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnServer``.

        :param certificate: The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate. Required when ``Protocols`` is set to ``FTPS`` . To request a new public certificate, see `Request a public certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html>`_ in the *AWS Certificate Manager User Guide* . To import an existing certificate into ACM, see `Importing certificates into ACM <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`_ in the *AWS Certificate Manager User Guide* . To request a private certificate to use FTPS through private IP addresses, see `Request a private certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html>`_ in the *AWS Certificate Manager User Guide* . Certificates with the following cryptographic algorithms and key sizes are supported: - 2048-bit RSA (RSA_2048) - 4096-bit RSA (RSA_4096) - Elliptic Prime Curve 256 bit (EC_prime256v1) - Elliptic Prime Curve 384 bit (EC_secp384r1) - Elliptic Prime Curve 521 bit (EC_secp521r1) .. epigraph:: The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.
        :param domain: Specifies the domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.
        :param endpoint_details: The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.
        :param endpoint_type: The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it. .. epigraph:: After May 19, 2021, you won't be able to create a server using ``EndpointType=VPC_ENDPOINT`` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with ``EndpointType=VPC_ENDPOINT`` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use ``EndpointType`` = ``VPC`` . For more information, see `Discontinuing the use of VPC_ENDPOINT <https://docs.aws.amazon.com//transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint>`_ . It is recommended that you use ``VPC`` as the ``EndpointType`` . With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with ``EndpointType`` set to ``VPC_ENDPOINT`` .
        :param identity_provider_details: Required when ``IdentityProviderType`` is set to ``AWS_DIRECTORY_SERVICE`` , ``AWS _LAMBDA`` or ``API_GATEWAY`` . Accepts an array containing all of the information required to use a directory in ``AWS_DIRECTORY_SERVICE`` or invoke a customer-supplied authentication API, including the API Gateway URL. Not required when ``IdentityProviderType`` is set to ``SERVICE_MANAGED`` .
        :param identity_provider_type: The mode of authentication for a server. The default value is ``SERVICE_MANAGED`` , which allows you to store and access user credentials within the AWS Transfer Family service. Use ``AWS_DIRECTORY_SERVICE`` to provide access to Active Directory groups in AWS Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in AWS using AD Connector. This option also requires you to provide a Directory ID by using the ``IdentityProviderDetails`` parameter. Use the ``API_GATEWAY`` value to integrate with an identity provider of your choosing. The ``API_GATEWAY`` setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the ``IdentityProviderDetails`` parameter. Use the ``AWS_LAMBDA`` value to directly use an AWS Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the ``Function`` parameter for the ``IdentityProviderDetails`` data type.
        :param logging_role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFSevents. When set, you can view user activity in your CloudWatch logs.
        :param post_authentication_login_banner: Specifies a string to display when users connect to a server. This string is displayed after the user authenticates. .. epigraph:: The SFTP protocol does not support post-authentication display banners.
        :param pre_authentication_login_banner: Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system: ``This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.``
        :param protocol_details: The protocol settings that are configured for your server. - To indicate passive mode (for FTP and FTPS protocols), use the ``PassiveIp`` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer. - To ignore the error that is generated when the client attempts to use the ``SETSTAT`` command on a file that you are uploading to an Amazon S3 bucket, use the ``SetStatOption`` parameter. To have the AWS Transfer Family server ignore the ``SETSTAT`` command and upload files without needing to make any changes to your SFTP client, set the value to ``ENABLE_NO_OP`` . If you set the ``SetStatOption`` parameter to ``ENABLE_NO_OP`` , Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a ``SETSTAT`` call. - To determine whether your AWS Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the ``TlsSessionResumptionMode`` parameter. - ``As2Transports`` indicates the transport method for the AS2 messages. Currently, only HTTP is supported. The ``Protocols`` parameter is an array of strings. *Allowed values* : One or more of ``SFTP`` , ``FTPS`` , ``FTP`` , ``AS2``
        :param protocols: Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are: - ``SFTP`` (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH - ``FTPS`` (File Transfer Protocol Secure): File transfer with TLS encryption - ``FTP`` (File Transfer Protocol): Unencrypted file transfer - ``AS2`` (Applicability Statement 2): used for transporting structured business-to-business data .. epigraph:: - If you select ``FTPS`` , you must choose a certificate stored in AWS Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS. - If ``Protocol`` includes either ``FTP`` or ``FTPS`` , then the ``EndpointType`` must be ``VPC`` and the ``IdentityProviderType`` must be either ``AWS_DIRECTORY_SERVICE`` , ``AWS_LAMBDA`` , or ``API_GATEWAY`` . - If ``Protocol`` includes ``FTP`` , then ``AddressAllocationIds`` cannot be associated. - If ``Protocol`` is set only to ``SFTP`` , the ``EndpointType`` can be set to ``PUBLIC`` and the ``IdentityProviderType`` can be set any of the supported identity types: ``SERVICE_MANAGED`` , ``AWS_DIRECTORY_SERVICE`` , ``AWS_LAMBDA`` , or ``API_GATEWAY`` . - If ``Protocol`` includes ``AS2`` , then the ``EndpointType`` must be ``VPC`` , and domain must be Amazon S3. The ``Protocols`` parameter is an array of strings. *Allowed values* : One or more of ``SFTP`` , ``FTPS`` , ``FTP`` , ``AS2``
        :param s3_storage_options: Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default. By default, home directory mappings have a ``TYPE`` of ``DIRECTORY`` . If you enable this option, you would then need to explicitly set the ``HomeDirectoryMapEntry`` ``Type`` to ``FILE`` if you want a mapping to have a file target.
        :param security_policy_name: Specifies the name of the security policy for the server.
        :param structured_log_destinations: Specifies the log groups to which your server logs are sent. To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows: ``arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*`` For example, ``arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*`` If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an ``update-server`` call. For example: ``update-server --server-id s-1234567890abcdef0 --structured-log-destinations``
        :param tags: Key-value pairs that can be used to group and search for servers.
        :param workflow_details: Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow. In addition to a workflow to execute when a file is uploaded completely, ``WorkflowDetails`` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when a file is open when the session disconnects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            cfn_server_props = transfer.CfnServerProps(
                certificate="certificate",
                domain="domain",
                endpoint_details=transfer.CfnServer.EndpointDetailsProperty(
                    address_allocation_ids=["addressAllocationIds"],
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"],
                    vpc_endpoint_id="vpcEndpointId",
                    vpc_id="vpcId"
                ),
                endpoint_type="endpointType",
                identity_provider_details=transfer.CfnServer.IdentityProviderDetailsProperty(
                    directory_id="directoryId",
                    function="function",
                    invocation_role="invocationRole",
                    sftp_authentication_methods="sftpAuthenticationMethods",
                    url="url"
                ),
                identity_provider_type="identityProviderType",
                logging_role="loggingRole",
                post_authentication_login_banner="postAuthenticationLoginBanner",
                pre_authentication_login_banner="preAuthenticationLoginBanner",
                protocol_details=transfer.CfnServer.ProtocolDetailsProperty(
                    as2_transports=["as2Transports"],
                    passive_ip="passiveIp",
                    set_stat_option="setStatOption",
                    tls_session_resumption_mode="tlsSessionResumptionMode"
                ),
                protocols=["protocols"],
                s3_storage_options=transfer.CfnServer.S3StorageOptionsProperty(
                    directory_listing_optimization="directoryListingOptimization"
                ),
                security_policy_name="securityPolicyName",
                structured_log_destinations=["structuredLogDestinations"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                workflow_details=transfer.CfnServer.WorkflowDetailsProperty(
                    on_partial_upload=[transfer.CfnServer.WorkflowDetailProperty(
                        execution_role="executionRole",
                        workflow_id="workflowId"
                    )],
                    on_upload=[transfer.CfnServer.WorkflowDetailProperty(
                        execution_role="executionRole",
                        workflow_id="workflowId"
                    )]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__755735299782e941527b817551c61582134dc6f25d12aff5d9120aeeb47a9ee6)
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument endpoint_details", value=endpoint_details, expected_type=type_hints["endpoint_details"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument identity_provider_details", value=identity_provider_details, expected_type=type_hints["identity_provider_details"])
            check_type(argname="argument identity_provider_type", value=identity_provider_type, expected_type=type_hints["identity_provider_type"])
            check_type(argname="argument logging_role", value=logging_role, expected_type=type_hints["logging_role"])
            check_type(argname="argument post_authentication_login_banner", value=post_authentication_login_banner, expected_type=type_hints["post_authentication_login_banner"])
            check_type(argname="argument pre_authentication_login_banner", value=pre_authentication_login_banner, expected_type=type_hints["pre_authentication_login_banner"])
            check_type(argname="argument protocol_details", value=protocol_details, expected_type=type_hints["protocol_details"])
            check_type(argname="argument protocols", value=protocols, expected_type=type_hints["protocols"])
            check_type(argname="argument s3_storage_options", value=s3_storage_options, expected_type=type_hints["s3_storage_options"])
            check_type(argname="argument security_policy_name", value=security_policy_name, expected_type=type_hints["security_policy_name"])
            check_type(argname="argument structured_log_destinations", value=structured_log_destinations, expected_type=type_hints["structured_log_destinations"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument workflow_details", value=workflow_details, expected_type=type_hints["workflow_details"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate is not None:
            self._values["certificate"] = certificate
        if domain is not None:
            self._values["domain"] = domain
        if endpoint_details is not None:
            self._values["endpoint_details"] = endpoint_details
        if endpoint_type is not None:
            self._values["endpoint_type"] = endpoint_type
        if identity_provider_details is not None:
            self._values["identity_provider_details"] = identity_provider_details
        if identity_provider_type is not None:
            self._values["identity_provider_type"] = identity_provider_type
        if logging_role is not None:
            self._values["logging_role"] = logging_role
        if post_authentication_login_banner is not None:
            self._values["post_authentication_login_banner"] = post_authentication_login_banner
        if pre_authentication_login_banner is not None:
            self._values["pre_authentication_login_banner"] = pre_authentication_login_banner
        if protocol_details is not None:
            self._values["protocol_details"] = protocol_details
        if protocols is not None:
            self._values["protocols"] = protocols
        if s3_storage_options is not None:
            self._values["s3_storage_options"] = s3_storage_options
        if security_policy_name is not None:
            self._values["security_policy_name"] = security_policy_name
        if structured_log_destinations is not None:
            self._values["structured_log_destinations"] = structured_log_destinations
        if tags is not None:
            self._values["tags"] = tags
        if workflow_details is not None:
            self._values["workflow_details"] = workflow_details

    @builtins.property
    def certificate(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate.

        Required when ``Protocols`` is set to ``FTPS`` .

        To request a new public certificate, see `Request a public certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html>`_ in the *AWS Certificate Manager User Guide* .

        To import an existing certificate into ACM, see `Importing certificates into ACM <https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html>`_ in the *AWS Certificate Manager User Guide* .

        To request a private certificate to use FTPS through private IP addresses, see `Request a private certificate <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html>`_ in the *AWS Certificate Manager User Guide* .

        Certificates with the following cryptographic algorithms and key sizes are supported:

        - 2048-bit RSA (RSA_2048)
        - 4096-bit RSA (RSA_4096)
        - Elliptic Prime Curve 256 bit (EC_prime256v1)
        - Elliptic Prime Curve 384 bit (EC_secp384r1)
        - Elliptic Prime Curve 521 bit (EC_secp521r1)

        .. epigraph::

           The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-certificate
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain(self) -> typing.Optional[builtins.str]:
        '''Specifies the domain of the storage system that is used for file transfers.

        There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def endpoint_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.EndpointDetailsProperty]]:
        '''The virtual private cloud (VPC) endpoint settings that are configured for your server.

        When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointdetails
        '''
        result = self._values.get("endpoint_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.EndpointDetailsProperty]], result)

    @builtins.property
    def endpoint_type(self) -> typing.Optional[builtins.str]:
        '''The type of endpoint that you want your server to use.

        You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.
        .. epigraph::

           After May 19, 2021, you won't be able to create a server using ``EndpointType=VPC_ENDPOINT`` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with ``EndpointType=VPC_ENDPOINT`` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use ``EndpointType`` = ``VPC`` .

           For more information, see `Discontinuing the use of VPC_ENDPOINT <https://docs.aws.amazon.com//transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint>`_ .

           It is recommended that you use ``VPC`` as the ``EndpointType`` . With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with ``EndpointType`` set to ``VPC_ENDPOINT`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-endpointtype
        '''
        result = self._values.get("endpoint_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.IdentityProviderDetailsProperty]]:
        '''Required when ``IdentityProviderType`` is set to ``AWS_DIRECTORY_SERVICE`` , ``AWS _LAMBDA`` or ``API_GATEWAY`` .

        Accepts an array containing all of the information required to use a directory in ``AWS_DIRECTORY_SERVICE`` or invoke a customer-supplied authentication API, including the API Gateway URL. Not required when ``IdentityProviderType`` is set to ``SERVICE_MANAGED`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityproviderdetails
        '''
        result = self._values.get("identity_provider_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.IdentityProviderDetailsProperty]], result)

    @builtins.property
    def identity_provider_type(self) -> typing.Optional[builtins.str]:
        '''The mode of authentication for a server.

        The default value is ``SERVICE_MANAGED`` , which allows you to store and access user credentials within the AWS Transfer Family service.

        Use ``AWS_DIRECTORY_SERVICE`` to provide access to Active Directory groups in AWS Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in AWS using AD Connector. This option also requires you to provide a Directory ID by using the ``IdentityProviderDetails`` parameter.

        Use the ``API_GATEWAY`` value to integrate with an identity provider of your choosing. The ``API_GATEWAY`` setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the ``IdentityProviderDetails`` parameter.

        Use the ``AWS_LAMBDA`` value to directly use an AWS Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the ``Function`` parameter for the ``IdentityProviderDetails`` data type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-identityprovidertype
        '''
        result = self._values.get("identity_provider_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def logging_role(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFSevents.

        When set, you can view user activity in your CloudWatch logs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-loggingrole
        '''
        result = self._values.get("logging_role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def post_authentication_login_banner(self) -> typing.Optional[builtins.str]:
        '''Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.

        .. epigraph::

           The SFTP protocol does not support post-authentication display banners.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-postauthenticationloginbanner
        '''
        result = self._values.get("post_authentication_login_banner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre_authentication_login_banner(self) -> typing.Optional[builtins.str]:
        '''Specifies a string to display when users connect to a server.

        This string is displayed before the user authenticates. For example, the following banner displays details about using the system:

        ``This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-preauthenticationloginbanner
        '''
        result = self._values.get("pre_authentication_login_banner")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.ProtocolDetailsProperty]]:
        '''The protocol settings that are configured for your server.

        - To indicate passive mode (for FTP and FTPS protocols), use the ``PassiveIp`` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer.
        - To ignore the error that is generated when the client attempts to use the ``SETSTAT`` command on a file that you are uploading to an Amazon S3 bucket, use the ``SetStatOption`` parameter. To have the AWS Transfer Family server ignore the ``SETSTAT`` command and upload files without needing to make any changes to your SFTP client, set the value to ``ENABLE_NO_OP`` . If you set the ``SetStatOption`` parameter to ``ENABLE_NO_OP`` , Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a ``SETSTAT`` call.
        - To determine whether your AWS Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the ``TlsSessionResumptionMode`` parameter.
        - ``As2Transports`` indicates the transport method for the AS2 messages. Currently, only HTTP is supported.

        The ``Protocols`` parameter is an array of strings.

        *Allowed values* : One or more of ``SFTP`` , ``FTPS`` , ``FTP`` , ``AS2``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocoldetails
        '''
        result = self._values.get("protocol_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.ProtocolDetailsProperty]], result)

    @builtins.property
    def protocols(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint.

        The available protocols are:

        - ``SFTP`` (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH
        - ``FTPS`` (File Transfer Protocol Secure): File transfer with TLS encryption
        - ``FTP`` (File Transfer Protocol): Unencrypted file transfer
        - ``AS2`` (Applicability Statement 2): used for transporting structured business-to-business data

        .. epigraph::

           - If you select ``FTPS`` , you must choose a certificate stored in AWS Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.
           - If ``Protocol`` includes either ``FTP`` or ``FTPS`` , then the ``EndpointType`` must be ``VPC`` and the ``IdentityProviderType`` must be either ``AWS_DIRECTORY_SERVICE`` , ``AWS_LAMBDA`` , or ``API_GATEWAY`` .
           - If ``Protocol`` includes ``FTP`` , then ``AddressAllocationIds`` cannot be associated.
           - If ``Protocol`` is set only to ``SFTP`` , the ``EndpointType`` can be set to ``PUBLIC`` and the ``IdentityProviderType`` can be set any of the supported identity types: ``SERVICE_MANAGED`` , ``AWS_DIRECTORY_SERVICE`` , ``AWS_LAMBDA`` , or ``API_GATEWAY`` .
           - If ``Protocol`` includes ``AS2`` , then the ``EndpointType`` must be ``VPC`` , and domain must be Amazon S3.

        The ``Protocols`` parameter is an array of strings.

        *Allowed values* : One or more of ``SFTP`` , ``FTPS`` , ``FTP`` , ``AS2``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-protocols
        '''
        result = self._values.get("protocols")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def s3_storage_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.S3StorageOptionsProperty]]:
        '''Specifies whether or not performance for your Amazon S3 directories is optimized. This is disabled by default.

        By default, home directory mappings have a ``TYPE`` of ``DIRECTORY`` . If you enable this option, you would then need to explicitly set the ``HomeDirectoryMapEntry`` ``Type`` to ``FILE`` if you want a mapping to have a file target.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-s3storageoptions
        '''
        result = self._values.get("s3_storage_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.S3StorageOptionsProperty]], result)

    @builtins.property
    def security_policy_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the name of the security policy for the server.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-securitypolicyname
        '''
        result = self._values.get("security_policy_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def structured_log_destinations(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the log groups to which your server logs are sent.

        To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:

        ``arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*``

        For example, ``arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*``

        If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an ``update-server`` call. For example:

        ``update-server --server-id s-1234567890abcdef0 --structured-log-destinations``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-structuredlogdestinations
        '''
        result = self._values.get("structured_log_destinations")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for servers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def workflow_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.WorkflowDetailsProperty]]:
        '''Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.

        In addition to a workflow to execute when a file is uploaded completely, ``WorkflowDetails`` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when a file is open when the session disconnects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-server.html#cfn-transfer-server-workflowdetails
        '''
        result = self._values.get("workflow_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.WorkflowDetailsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnUser(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnUser",
):
    '''The ``AWS::Transfer::User`` resource creates a user and associates them with an existing server.

    You can only create and associate users with servers that have the ``IdentityProviderType`` set to ``SERVICE_MANAGED`` . Using parameters for ``CreateUser`` , you can specify the user name, set the home directory, store the user's public key, and assign the user's AWS Identity and Access Management (IAM) role. You can also optionally add a session policy, and assign metadata with tags that can be used to group and search for users.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
    :cloudformationResource: AWS::Transfer::User
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        cfn_user = transfer.CfnUser(self, "MyCfnUser",
            role="role",
            server_id="serverId",
            user_name="userName",
        
            # the properties below are optional
            home_directory="homeDirectory",
            home_directory_mappings=[transfer.CfnUser.HomeDirectoryMapEntryProperty(
                entry="entry",
                target="target",
        
                # the properties below are optional
                type="type"
            )],
            home_directory_type="homeDirectoryType",
            policy="policy",
            posix_profile=transfer.CfnUser.PosixProfileProperty(
                gid=123,
                uid=123,
        
                # the properties below are optional
                secondary_gids=[123]
            ),
            ssh_public_keys=["sshPublicKeys"],
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
        role: builtins.str,
        server_id: builtins.str,
        user_name: builtins.str,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.HomeDirectoryMapEntryProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUser.PosixProfileProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.
        :param server_id: A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.
        :param user_name: A unique string that identifies a user and is associated with a ``ServerId`` . This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.
        :param home_directory: The landing directory (folder) for a user when they log in to the server using the client. A ``HomeDirectory`` example is ``/bucket_name/home/mydirectory`` . .. epigraph:: The ``HomeDirectory`` parameter is only used if ``HomeDirectoryType`` is set to ``PATH`` .
        :param home_directory_mappings: Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the ``Entry`` and ``Target`` pair, where ``Entry`` shows how the path is made visible and ``Target`` is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your AWS Identity and Access Management (IAM) role provides access to paths in ``Target`` . This value can be set only when ``HomeDirectoryType`` is set to *LOGICAL* . The following is an ``Entry`` and ``Target`` pair example. ``[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]`` In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory (" ``chroot`` "). To do this, you can set ``Entry`` to ``/`` and set ``Target`` to the value the user should see for their home directory when they log in. The following is an ``Entry`` and ``Target`` pair example for ``chroot`` . ``[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]``
        :param home_directory_type: The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to ``PATH`` , the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to ``LOGICAL`` , you need to provide mappings in the ``HomeDirectoryMappings`` for how you want to make Amazon S3 or Amazon EFS paths visible to your users. .. epigraph:: If ``HomeDirectoryType`` is ``LOGICAL`` , you must provide mappings, using the ``HomeDirectoryMappings`` parameter. If, on the other hand, ``HomeDirectoryType`` is ``PATH`` , you provide an absolute path using the ``HomeDirectory`` parameter. You cannot have both ``HomeDirectory`` and ``HomeDirectoryMappings`` in your template.
        :param policy: A session policy for your user so you can use the same IAM role across multiple users. This policy restricts user access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include ``${Transfer:UserName}`` , ``${Transfer:HomeDirectory}`` , and ``${Transfer:HomeBucket}`` . .. epigraph:: For session policies, AWS Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the ``Policy`` argument. For an example of a session policy, see `Example session policy <https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html>`_ . For more information, see `AssumeRole <https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>`_ in the *AWS Security Token Service API Reference* .
        :param posix_profile: Specifies the full POSIX identity, including user ID ( ``Uid`` ), group ID ( ``Gid`` ), and any secondary groups IDs ( ``SecondaryGids`` ), that controls your users' access to your Amazon Elastic File System (Amazon EFS) file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.
        :param ssh_public_keys: Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.
        :param tags: Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa42271c7d25cb4584b126195a9b597af920cd9c1e4f193efbe2a6d407fe665b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserProps(
            role=role,
            server_id=server_id,
            user_name=user_name,
            home_directory=home_directory,
            home_directory_mappings=home_directory_mappings,
            home_directory_type=home_directory_type,
            policy=policy,
            posix_profile=posix_profile,
            ssh_public_keys=ssh_public_keys,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c366b551ea828539c0b8832360f574b612c272eb72c45ba57186d6f9f88ece4c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__70895ace466ec04aabc03b4587de7b5439637bdc33988efc767695697eb579b5)
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
        '''The Amazon Resource Name associated with the user, in the form ``arn:aws:transfer:region: *account-id* :user/ *server-id* / *username*`` .

        An example of a user ARN is: ``arn:aws:transfer:us-east-1:123456789012:user/user1`` .

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
    @jsii.member(jsii_name="attrServerId")
    def attr_server_id(self) -> builtins.str:
        '''The ID of the server to which the user is attached.

        An example ``ServerId`` is ``s-01234567890abcdef`` .

        :cloudformationAttribute: ServerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServerId"))

    @builtins.property
    @jsii.member(jsii_name="attrUserName")
    def attr_user_name(self) -> builtins.str:
        '''A unique string that identifies a Transfer Family user account associated with a server.

        An example ``UserName`` is ``transfer-user-1`` .

        :cloudformationAttribute: UserName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserName"))

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
    @jsii.member(jsii_name="role")
    def role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system.'''
        return typing.cast(builtins.str, jsii.get(self, "role"))

    @role.setter
    def role(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc0b372f22cb0ef29120fe3ab548c0ca10b740c11468e6d61db51556704e1d36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="serverId")
    def server_id(self) -> builtins.str:
        '''A system-assigned unique identifier for a server instance.'''
        return typing.cast(builtins.str, jsii.get(self, "serverId"))

    @server_id.setter
    def server_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ef5ab6b990dd2596a8e24432c1b5cc6774c6fb7328a87f17aa8968f538a46aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverId", value)

    @builtins.property
    @jsii.member(jsii_name="userName")
    def user_name(self) -> builtins.str:
        '''A unique string that identifies a user and is associated with a ``ServerId`` .'''
        return typing.cast(builtins.str, jsii.get(self, "userName"))

    @user_name.setter
    def user_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fb81d11e7cb96377c122bfb8f45feadffb3ee576ada6993c1212e4729f5bdc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userName", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectory")
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''The landing directory (folder) for a user when they log in to the server using the client.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectory"))

    @home_directory.setter
    def home_directory(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c77e829c1d4a272a45dea8460ccc5e13dd485da9cee71caf0c5e21561309747)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectory", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryMappings")
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.HomeDirectoryMapEntryProperty"]]]]:
        '''Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.HomeDirectoryMapEntryProperty"]]]], jsii.get(self, "homeDirectoryMappings"))

    @home_directory_mappings.setter
    def home_directory_mappings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUser.HomeDirectoryMapEntryProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42f7f6bf54b856d03c6d1447bb9d5afe1e603f3c84d196395834b94ac8e1ad43)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectoryMappings", value)

    @builtins.property
    @jsii.member(jsii_name="homeDirectoryType")
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''The type of landing directory (folder) that you want your users' home directory to be when they log in to the server.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "homeDirectoryType"))

    @home_directory_type.setter
    def home_directory_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c456bc4531fb1dba11ebf05fae08ad26d41da8fd3c1268451a061ae0d2114753)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "homeDirectoryType", value)

    @builtins.property
    @jsii.member(jsii_name="policy")
    def policy(self) -> typing.Optional[builtins.str]:
        '''A session policy for your user so you can use the same IAM role across multiple users.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policy"))

    @policy.setter
    def policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__212dcb7d96de8b9904cbf9ca69ad0b82b41c0e878e3c7efec36fa71ec7fe0437)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policy", value)

    @builtins.property
    @jsii.member(jsii_name="posixProfile")
    def posix_profile(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.PosixProfileProperty"]]:
        '''Specifies the full POSIX identity, including user ID ( ``Uid`` ), group ID ( ``Gid`` ), and any secondary groups IDs ( ``SecondaryGids`` ), that controls your users' access to your Amazon Elastic File System (Amazon EFS) file systems.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.PosixProfileProperty"]], jsii.get(self, "posixProfile"))

    @posix_profile.setter
    def posix_profile(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUser.PosixProfileProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edc3910325c95eaad6c5b004cc7944e382cb7676aa1a2431f7113b2151ec86b9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "posixProfile", value)

    @builtins.property
    @jsii.member(jsii_name="sshPublicKeys")
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sshPublicKeys"))

    @ssh_public_keys.setter
    def ssh_public_keys(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e080a1baa764f200889f63bea8c8060d1553438f95a87e04bf4db6dca1b10305)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sshPublicKeys", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for users.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cd778c7c12e09594b9e52b3ef35f802dbbc36612c72eb9993d5f0bdb892407f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnUser.HomeDirectoryMapEntryProperty",
        jsii_struct_bases=[],
        name_mapping={"entry": "entry", "target": "target", "type": "type"},
    )
    class HomeDirectoryMapEntryProperty:
        def __init__(
            self,
            *,
            entry: builtins.str,
            target: builtins.str,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Represents an object that contains entries and targets for ``HomeDirectoryMappings`` .

            :param entry: Represents an entry for ``HomeDirectoryMappings`` .
            :param target: Represents the map target that is used in a ``HomeDirectoryMapEntry`` .
            :param type: Specifies the type of mapping. Set the type to ``FILE`` if you want the mapping to point to a file, or ``DIRECTORY`` for the directory to point to a directory. .. epigraph:: By default, home directory mappings have a ``Type`` of ``DIRECTORY`` when you create a Transfer Family server. You would need to explicitly set ``Type`` to ``FILE`` if you want a mapping to have a file target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                home_directory_map_entry_property = transfer.CfnUser.HomeDirectoryMapEntryProperty(
                    entry="entry",
                    target="target",
                
                    # the properties below are optional
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2013fa8cf00b48e7a477b3cfb9c7ba15a14fd8ec083155cdab295e5e906f4d34)
                check_type(argname="argument entry", value=entry, expected_type=type_hints["entry"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entry": entry,
                "target": target,
            }
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def entry(self) -> builtins.str:
            '''Represents an entry for ``HomeDirectoryMappings`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-entry
            '''
            result = self._values.get("entry")
            assert result is not None, "Required property 'entry' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target(self) -> builtins.str:
            '''Represents the map target that is used in a ``HomeDirectoryMapEntry`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-target
            '''
            result = self._values.get("target")
            assert result is not None, "Required property 'target' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Specifies the type of mapping.

            Set the type to ``FILE`` if you want the mapping to point to a file, or ``DIRECTORY`` for the directory to point to a directory.
            .. epigraph::

               By default, home directory mappings have a ``Type`` of ``DIRECTORY`` when you create a Transfer Family server. You would need to explicitly set ``Type`` to ``FILE`` if you want a mapping to have a file target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-homedirectorymapentry.html#cfn-transfer-user-homedirectorymapentry-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HomeDirectoryMapEntryProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnUser.PosixProfileProperty",
        jsii_struct_bases=[],
        name_mapping={"gid": "gid", "uid": "uid", "secondary_gids": "secondaryGids"},
    )
    class PosixProfileProperty:
        def __init__(
            self,
            *,
            gid: jsii.Number,
            uid: jsii.Number,
            secondary_gids: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
        ) -> None:
            '''The full POSIX identity, including user ID ( ``Uid`` ), group ID ( ``Gid`` ), and any secondary groups IDs ( ``SecondaryGids`` ), that controls your users' access to your Amazon EFS file systems.

            The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.

            :param gid: The POSIX group ID used for all EFS operations by this user.
            :param uid: The POSIX user ID used for all EFS operations by this user.
            :param secondary_gids: The secondary POSIX group IDs used for all EFS operations by this user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                posix_profile_property = transfer.CfnUser.PosixProfileProperty(
                    gid=123,
                    uid=123,
                
                    # the properties below are optional
                    secondary_gids=[123]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b8c3948f8e11532949a9c338eb57f070ee1d1b3a7da23c8e2dd5209058536c79)
                check_type(argname="argument gid", value=gid, expected_type=type_hints["gid"])
                check_type(argname="argument uid", value=uid, expected_type=type_hints["uid"])
                check_type(argname="argument secondary_gids", value=secondary_gids, expected_type=type_hints["secondary_gids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "gid": gid,
                "uid": uid,
            }
            if secondary_gids is not None:
                self._values["secondary_gids"] = secondary_gids

        @builtins.property
        def gid(self) -> jsii.Number:
            '''The POSIX group ID used for all EFS operations by this user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-gid
            '''
            result = self._values.get("gid")
            assert result is not None, "Required property 'gid' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def uid(self) -> jsii.Number:
            '''The POSIX user ID used for all EFS operations by this user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-uid
            '''
            result = self._values.get("uid")
            assert result is not None, "Required property 'uid' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def secondary_gids(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''The secondary POSIX group IDs used for all EFS operations by this user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-user-posixprofile.html#cfn-transfer-user-posixprofile-secondarygids
            '''
            result = self._values.get("secondary_gids")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PosixProfileProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnUserProps",
    jsii_struct_bases=[],
    name_mapping={
        "role": "role",
        "server_id": "serverId",
        "user_name": "userName",
        "home_directory": "homeDirectory",
        "home_directory_mappings": "homeDirectoryMappings",
        "home_directory_type": "homeDirectoryType",
        "policy": "policy",
        "posix_profile": "posixProfile",
        "ssh_public_keys": "sshPublicKeys",
        "tags": "tags",
    },
)
class CfnUserProps:
    def __init__(
        self,
        *,
        role: builtins.str,
        server_id: builtins.str,
        user_name: builtins.str,
        home_directory: typing.Optional[builtins.str] = None,
        home_directory_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.HomeDirectoryMapEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        home_directory_type: typing.Optional[builtins.str] = None,
        policy: typing.Optional[builtins.str] = None,
        posix_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.PosixProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUser``.

        :param role: The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system. The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.
        :param server_id: A system-assigned unique identifier for a server instance. This is the specific server that you added your user to.
        :param user_name: A unique string that identifies a user and is associated with a ``ServerId`` . This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.
        :param home_directory: The landing directory (folder) for a user when they log in to the server using the client. A ``HomeDirectory`` example is ``/bucket_name/home/mydirectory`` . .. epigraph:: The ``HomeDirectory`` parameter is only used if ``HomeDirectoryType`` is set to ``PATH`` .
        :param home_directory_mappings: Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible. You must specify the ``Entry`` and ``Target`` pair, where ``Entry`` shows how the path is made visible and ``Target`` is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your AWS Identity and Access Management (IAM) role provides access to paths in ``Target`` . This value can be set only when ``HomeDirectoryType`` is set to *LOGICAL* . The following is an ``Entry`` and ``Target`` pair example. ``[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]`` In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory (" ``chroot`` "). To do this, you can set ``Entry`` to ``/`` and set ``Target`` to the value the user should see for their home directory when they log in. The following is an ``Entry`` and ``Target`` pair example for ``chroot`` . ``[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]``
        :param home_directory_type: The type of landing directory (folder) that you want your users' home directory to be when they log in to the server. If you set it to ``PATH`` , the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to ``LOGICAL`` , you need to provide mappings in the ``HomeDirectoryMappings`` for how you want to make Amazon S3 or Amazon EFS paths visible to your users. .. epigraph:: If ``HomeDirectoryType`` is ``LOGICAL`` , you must provide mappings, using the ``HomeDirectoryMappings`` parameter. If, on the other hand, ``HomeDirectoryType`` is ``PATH`` , you provide an absolute path using the ``HomeDirectory`` parameter. You cannot have both ``HomeDirectory`` and ``HomeDirectoryMappings`` in your template.
        :param policy: A session policy for your user so you can use the same IAM role across multiple users. This policy restricts user access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include ``${Transfer:UserName}`` , ``${Transfer:HomeDirectory}`` , and ``${Transfer:HomeBucket}`` . .. epigraph:: For session policies, AWS Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the ``Policy`` argument. For an example of a session policy, see `Example session policy <https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html>`_ . For more information, see `AssumeRole <https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>`_ in the *AWS Security Token Service API Reference* .
        :param posix_profile: Specifies the full POSIX identity, including user ID ( ``Uid`` ), group ID ( ``Gid`` ), and any secondary groups IDs ( ``SecondaryGids`` ), that controls your users' access to your Amazon Elastic File System (Amazon EFS) file systems. The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.
        :param ssh_public_keys: Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.
        :param tags: Key-value pairs that can be used to group and search for users. Tags are metadata attached to users for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            cfn_user_props = transfer.CfnUserProps(
                role="role",
                server_id="serverId",
                user_name="userName",
            
                # the properties below are optional
                home_directory="homeDirectory",
                home_directory_mappings=[transfer.CfnUser.HomeDirectoryMapEntryProperty(
                    entry="entry",
                    target="target",
            
                    # the properties below are optional
                    type="type"
                )],
                home_directory_type="homeDirectoryType",
                policy="policy",
                posix_profile=transfer.CfnUser.PosixProfileProperty(
                    gid=123,
                    uid=123,
            
                    # the properties below are optional
                    secondary_gids=[123]
                ),
                ssh_public_keys=["sshPublicKeys"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0aa64ea17d55d9634df57b389b841e68b583b0c7f4818453a5cb08787dcc31)
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument server_id", value=server_id, expected_type=type_hints["server_id"])
            check_type(argname="argument user_name", value=user_name, expected_type=type_hints["user_name"])
            check_type(argname="argument home_directory", value=home_directory, expected_type=type_hints["home_directory"])
            check_type(argname="argument home_directory_mappings", value=home_directory_mappings, expected_type=type_hints["home_directory_mappings"])
            check_type(argname="argument home_directory_type", value=home_directory_type, expected_type=type_hints["home_directory_type"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument posix_profile", value=posix_profile, expected_type=type_hints["posix_profile"])
            check_type(argname="argument ssh_public_keys", value=ssh_public_keys, expected_type=type_hints["ssh_public_keys"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role": role,
            "server_id": server_id,
            "user_name": user_name,
        }
        if home_directory is not None:
            self._values["home_directory"] = home_directory
        if home_directory_mappings is not None:
            self._values["home_directory_mappings"] = home_directory_mappings
        if home_directory_type is not None:
            self._values["home_directory_type"] = home_directory_type
        if policy is not None:
            self._values["policy"] = policy
        if posix_profile is not None:
            self._values["posix_profile"] = posix_profile
        if ssh_public_keys is not None:
            self._values["ssh_public_keys"] = ssh_public_keys
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def role(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that controls your users' access to your Amazon S3 bucket or Amazon EFS file system.

        The policies attached to this role determine the level of access that you want to provide your users when transferring files into and out of your Amazon S3 bucket or Amazon EFS file system. The IAM role should also contain a trust relationship that allows the server to access your resources when servicing your users' transfer requests.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-role
        '''
        result = self._values.get("role")
        assert result is not None, "Required property 'role' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def server_id(self) -> builtins.str:
        '''A system-assigned unique identifier for a server instance.

        This is the specific server that you added your user to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-serverid
        '''
        result = self._values.get("server_id")
        assert result is not None, "Required property 'server_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def user_name(self) -> builtins.str:
        '''A unique string that identifies a user and is associated with a ``ServerId`` .

        This user name must be a minimum of 3 and a maximum of 100 characters long. The following are valid characters: a-z, A-Z, 0-9, underscore '_', hyphen '-', period '.', and at sign '@'. The user name can't start with a hyphen, period, or at sign.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-username
        '''
        result = self._values.get("user_name")
        assert result is not None, "Required property 'user_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def home_directory(self) -> typing.Optional[builtins.str]:
        '''The landing directory (folder) for a user when they log in to the server using the client.

        A ``HomeDirectory`` example is ``/bucket_name/home/mydirectory`` .
        .. epigraph::

           The ``HomeDirectory`` parameter is only used if ``HomeDirectoryType`` is set to ``PATH`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectory
        '''
        result = self._values.get("home_directory")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def home_directory_mappings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.HomeDirectoryMapEntryProperty]]]]:
        '''Logical directory mappings that specify what Amazon S3 or Amazon EFS paths and keys should be visible to your user and how you want to make them visible.

        You must specify the ``Entry`` and ``Target`` pair, where ``Entry`` shows how the path is made visible and ``Target`` is the actual Amazon S3 or Amazon EFS path. If you only specify a target, it is displayed as is. You also must ensure that your AWS Identity and Access Management (IAM) role provides access to paths in ``Target`` . This value can be set only when ``HomeDirectoryType`` is set to *LOGICAL* .

        The following is an ``Entry`` and ``Target`` pair example.

        ``[ { "Entry": "/directory1", "Target": "/bucket_name/home/mydirectory" } ]``

        In most cases, you can use this value instead of the session policy to lock your user down to the designated home directory (" ``chroot`` "). To do this, you can set ``Entry`` to ``/`` and set ``Target`` to the value the user should see for their home directory when they log in.

        The following is an ``Entry`` and ``Target`` pair example for ``chroot`` .

        ``[ { "Entry": "/", "Target": "/bucket_name/home/mydirectory" } ]``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorymappings
        '''
        result = self._values.get("home_directory_mappings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.HomeDirectoryMapEntryProperty]]]], result)

    @builtins.property
    def home_directory_type(self) -> typing.Optional[builtins.str]:
        '''The type of landing directory (folder) that you want your users' home directory to be when they log in to the server.

        If you set it to ``PATH`` , the user will see the absolute Amazon S3 bucket or Amazon EFS path as is in their file transfer protocol clients. If you set it to ``LOGICAL`` , you need to provide mappings in the ``HomeDirectoryMappings`` for how you want to make Amazon S3 or Amazon EFS paths visible to your users.
        .. epigraph::

           If ``HomeDirectoryType`` is ``LOGICAL`` , you must provide mappings, using the ``HomeDirectoryMappings`` parameter. If, on the other hand, ``HomeDirectoryType`` is ``PATH`` , you provide an absolute path using the ``HomeDirectory`` parameter. You cannot have both ``HomeDirectory`` and ``HomeDirectoryMappings`` in your template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-homedirectorytype
        '''
        result = self._values.get("home_directory_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[builtins.str]:
        '''A session policy for your user so you can use the same IAM role across multiple users.

        This policy restricts user access to portions of their Amazon S3 bucket. Variables that you can use inside this policy include ``${Transfer:UserName}`` , ``${Transfer:HomeDirectory}`` , and ``${Transfer:HomeBucket}`` .
        .. epigraph::

           For session policies, AWS Transfer Family stores the policy as a JSON blob, instead of the Amazon Resource Name (ARN) of the policy. You save the policy as a JSON blob and pass it in the ``Policy`` argument.

           For an example of a session policy, see `Example session policy <https://docs.aws.amazon.com/transfer/latest/userguide/session-policy.html>`_ .

           For more information, see `AssumeRole <https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html>`_ in the *AWS Security Token Service API Reference* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-policy
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def posix_profile(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.PosixProfileProperty]]:
        '''Specifies the full POSIX identity, including user ID ( ``Uid`` ), group ID ( ``Gid`` ), and any secondary groups IDs ( ``SecondaryGids`` ), that controls your users' access to your Amazon Elastic File System (Amazon EFS) file systems.

        The POSIX permissions that are set on files and directories in your file system determine the level of access your users get when transferring files into and out of your Amazon EFS file systems.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-posixprofile
        '''
        result = self._values.get("posix_profile")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.PosixProfileProperty]], result)

    @builtins.property
    def ssh_public_keys(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the public key portion of the Secure Shell (SSH) keys stored for the described user.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-sshpublickeys
        '''
        result = self._values.get("ssh_public_keys")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for users.

        Tags are metadata attached to users for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-user.html#cfn-transfer-user-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnWorkflow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow",
):
    '''Allows you to create a workflow with specified steps and step details the workflow invokes after file transfer completes.

    After creating a workflow, you can associate the workflow created with any transfer servers by specifying the ``workflow-details`` field in ``CreateServer`` and ``UpdateServer`` operations.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html
    :cloudformationResource: AWS::Transfer::Workflow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_transfer as transfer
        
        # copy_step_details: Any
        # custom_step_details: Any
        # delete_step_details: Any
        # tag_step_details: Any
        
        cfn_workflow = transfer.CfnWorkflow(self, "MyCfnWorkflow",
            steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                decrypt_step_details=transfer.CfnWorkflow.DecryptStepDetailsProperty(
                    destination_file_location=transfer.CfnWorkflow.InputFileLocationProperty(
                        efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                            file_system_id="fileSystemId",
                            path="path"
                        ),
                        s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    type="type",
        
                    # the properties below are optional
                    name="name",
                    overwrite_existing="overwriteExisting",
                    source_file_location="sourceFileLocation"
                ),
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
                type="type"
            )],
        
            # the properties below are optional
            description="description",
            on_exception_steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                copy_step_details=copy_step_details,
                custom_step_details=custom_step_details,
                decrypt_step_details=transfer.CfnWorkflow.DecryptStepDetailsProperty(
                    destination_file_location=transfer.CfnWorkflow.InputFileLocationProperty(
                        efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                            file_system_id="fileSystemId",
                            path="path"
                        ),
                        s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    type="type",
        
                    # the properties below are optional
                    name="name",
                    overwrite_existing="overwriteExisting",
                    source_file_location="sourceFileLocation"
                ),
                delete_step_details=delete_step_details,
                tag_step_details=tag_step_details,
                type="type"
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
        steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.WorkflowStepProperty", typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.WorkflowStepProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param steps: Specifies the details for the steps that are in the specified workflow.
        :param description: Specifies the text description for the workflow.
        :param on_exception_steps: Specifies the steps (actions) to take if errors are encountered during execution of the workflow.
        :param tags: Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a86ecf6f123d228f6edf61149bc2542f6ce02d9365ac8986ec7c6468379f655)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnWorkflowProps(
            steps=steps,
            description=description,
            on_exception_steps=on_exception_steps,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcf8488f51b3aba3af306d264af9434fa1e0040f1b353a0381fc97849f0e69f1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fa13620584d220c161b9db23ba579d9340ccaa284cc4962e4f437c8b538f0b6)
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
        '''Specifies the unique Amazon Resource Name (ARN) for the workflow.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrWorkflowId")
    def attr_workflow_id(self) -> builtins.str:
        '''A unique identifier for a workflow.

        :cloudformationAttribute: WorkflowId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrWorkflowId"))

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
    @jsii.member(jsii_name="steps")
    def steps(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowStepProperty"]]]:
        '''Specifies the details for the steps that are in the specified workflow.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowStepProperty"]]], jsii.get(self, "steps"))

    @steps.setter
    def steps(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowStepProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dad6eb0cfc84813f42cb30691eac8687d1c244e7b0c7a08584547c461c60b6e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "steps", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Specifies the text description for the workflow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__210eb2eb8f359d51c087a422da2997dfbca2c3a02ef0f5b0023c485aea5ac405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="onExceptionSteps")
    def on_exception_steps(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowStepProperty"]]]]:
        '''Specifies the steps (actions) to take if errors are encountered during execution of the workflow.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowStepProperty"]]]], jsii.get(self, "onExceptionSteps"))

    @on_exception_steps.setter
    def on_exception_steps(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.WorkflowStepProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbe5eec53a115ade4f8181ac2122f17276111f9d5675380186d596e738cbb4c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "onExceptionSteps", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for workflows.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71de7009c6ec1a7256bbbf8d8fea07e111e611f3c7ca8306d2156be4ff00a297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.CopyStepDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_file_location": "destinationFileLocation",
            "name": "name",
            "overwrite_existing": "overwriteExisting",
            "source_file_location": "sourceFileLocation",
        },
    )
    class CopyStepDetailsProperty:
        def __init__(
            self,
            *,
            destination_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.S3FileLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            overwrite_existing: typing.Optional[builtins.str] = None,
            source_file_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details for a step that performs a file copy.

            Consists of the following values:

            - A description
            - An Amazon S3 location for the destination of the file copy.
            - A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .

            :param destination_file_location: Specifies the location for the file being copied. Use ``${Transfer:UserName}`` or ``${Transfer:UploadDate}`` in this field to parametrize the destination prefix by username or uploaded date. - Set the value of ``DestinationFileLocation`` to ``${Transfer:UserName}`` to copy uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file. - Set the value of ``DestinationFileLocation`` to ``${Transfer:UploadDate}`` to copy uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload. .. epigraph:: The system resolves ``UploadDate`` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.
            :param name: The name of the step, used as an identifier.
            :param overwrite_existing: A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` . If the workflow is processing a file that has the same name as an existing file, the behavior is as follows: - If ``OverwriteExisting`` is ``TRUE`` , the existing file is replaced with the file being processed. - If ``OverwriteExisting`` is ``FALSE`` , nothing happens, and the workflow processing stops.
            :param source_file_location: Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow. - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value. - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                copy_step_details_property = transfer.CfnWorkflow.CopyStepDetailsProperty(
                    destination_file_location=transfer.CfnWorkflow.S3FileLocationProperty(
                        s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    name="name",
                    overwrite_existing="overwriteExisting",
                    source_file_location="sourceFileLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b697f702761c46ff428c59596a9536b6c93219cf1dc035facf49a7a9ded2b041)
                check_type(argname="argument destination_file_location", value=destination_file_location, expected_type=type_hints["destination_file_location"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument overwrite_existing", value=overwrite_existing, expected_type=type_hints["overwrite_existing"])
                check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_file_location is not None:
                self._values["destination_file_location"] = destination_file_location
            if name is not None:
                self._values["name"] = name
            if overwrite_existing is not None:
                self._values["overwrite_existing"] = overwrite_existing
            if source_file_location is not None:
                self._values["source_file_location"] = source_file_location

        @builtins.property
        def destination_file_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.S3FileLocationProperty"]]:
            '''Specifies the location for the file being copied.

            Use ``${Transfer:UserName}`` or ``${Transfer:UploadDate}`` in this field to parametrize the destination prefix by username or uploaded date.

            - Set the value of ``DestinationFileLocation`` to ``${Transfer:UserName}`` to copy uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.
            - Set the value of ``DestinationFileLocation`` to ``${Transfer:UploadDate}`` to copy uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.

            .. epigraph::

               The system resolves ``UploadDate`` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-destinationfilelocation
            '''
            result = self._values.get("destination_file_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.S3FileLocationProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the step, used as an identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def overwrite_existing(self) -> typing.Optional[builtins.str]:
            '''A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .

            If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:

            - If ``OverwriteExisting`` is ``TRUE`` , the existing file is replaced with the file being processed.
            - If ``OverwriteExisting`` is ``FALSE`` , nothing happens, and the workflow processing stops.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-overwriteexisting
            '''
            result = self._values.get("overwrite_existing")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_file_location(self) -> typing.Optional[builtins.str]:
            '''Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

            - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
            - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-copystepdetails.html#cfn-transfer-workflow-copystepdetails-sourcefilelocation
            '''
            result = self._values.get("source_file_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CopyStepDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.CustomStepDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "source_file_location": "sourceFileLocation",
            "target": "target",
            "timeout_seconds": "timeoutSeconds",
        },
    )
    class CustomStepDetailsProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            source_file_location: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
            timeout_seconds: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Details for a step that invokes an AWS Lambda function.

            Consists of the Lambda function's name, target, and timeout (in seconds).

            :param name: The name of the step, used as an identifier.
            :param source_file_location: Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow. - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value. - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .
            :param target: The ARN for the Lambda function that is being called.
            :param timeout_seconds: Timeout, in seconds, for the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                custom_step_details_property = transfer.CfnWorkflow.CustomStepDetailsProperty(
                    name="name",
                    source_file_location="sourceFileLocation",
                    target="target",
                    timeout_seconds=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe264913218615c435ebf846cbfed95b995c342d261b4903fa71634538959ea6)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
                check_type(argname="argument timeout_seconds", value=timeout_seconds, expected_type=type_hints["timeout_seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if source_file_location is not None:
                self._values["source_file_location"] = source_file_location
            if target is not None:
                self._values["target"] = target
            if timeout_seconds is not None:
                self._values["timeout_seconds"] = timeout_seconds

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the step, used as an identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_file_location(self) -> typing.Optional[builtins.str]:
            '''Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

            - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
            - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-sourcefilelocation
            '''
            result = self._values.get("source_file_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''The ARN for the Lambda function that is being called.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_seconds(self) -> typing.Optional[jsii.Number]:
            '''Timeout, in seconds, for the step.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-customstepdetails.html#cfn-transfer-workflow-customstepdetails-timeoutseconds
            '''
            result = self._values.get("timeout_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomStepDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.DecryptStepDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_file_location": "destinationFileLocation",
            "type": "type",
            "name": "name",
            "overwrite_existing": "overwriteExisting",
            "source_file_location": "sourceFileLocation",
        },
    )
    class DecryptStepDetailsProperty:
        def __init__(
            self,
            *,
            destination_file_location: typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.InputFileLocationProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
            name: typing.Optional[builtins.str] = None,
            overwrite_existing: typing.Optional[builtins.str] = None,
            source_file_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Details for a step that decrypts an encrypted file.

            Consists of the following values:

            - A descriptive name
            - An Amazon S3 or Amazon Elastic File System (Amazon EFS) location for the source file to decrypt.
            - An S3 or Amazon EFS location for the destination of the file decryption.
            - A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .
            - The type of encryption that's used. Currently, only PGP encryption is supported.

            :param destination_file_location: Specifies the location for the file being decrypted. Use ``${Transfer:UserName}`` or ``${Transfer:UploadDate}`` in this field to parametrize the destination prefix by username or uploaded date. - Set the value of ``DestinationFileLocation`` to ``${Transfer:UserName}`` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file. - Set the value of ``DestinationFileLocation`` to ``${Transfer:UploadDate}`` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload. .. epigraph:: The system resolves ``UploadDate`` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.
            :param type: The type of encryption used. Currently, this value must be ``PGP`` .
            :param name: The name of the step, used as an identifier.
            :param overwrite_existing: A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` . If the workflow is processing a file that has the same name as an existing file, the behavior is as follows: - If ``OverwriteExisting`` is ``TRUE`` , the existing file is replaced with the file being processed. - If ``OverwriteExisting`` is ``FALSE`` , nothing happens, and the workflow processing stops.
            :param source_file_location: Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow. - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value. - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                decrypt_step_details_property = transfer.CfnWorkflow.DecryptStepDetailsProperty(
                    destination_file_location=transfer.CfnWorkflow.InputFileLocationProperty(
                        efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                            file_system_id="fileSystemId",
                            path="path"
                        ),
                        s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                            bucket="bucket",
                            key="key"
                        )
                    ),
                    type="type",
                
                    # the properties below are optional
                    name="name",
                    overwrite_existing="overwriteExisting",
                    source_file_location="sourceFileLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad8f772a5a88a70744cbdb419880ea7a579190d4fea687585ef9c062d4a6c34c)
                check_type(argname="argument destination_file_location", value=destination_file_location, expected_type=type_hints["destination_file_location"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument overwrite_existing", value=overwrite_existing, expected_type=type_hints["overwrite_existing"])
                check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination_file_location": destination_file_location,
                "type": type,
            }
            if name is not None:
                self._values["name"] = name
            if overwrite_existing is not None:
                self._values["overwrite_existing"] = overwrite_existing
            if source_file_location is not None:
                self._values["source_file_location"] = source_file_location

        @builtins.property
        def destination_file_location(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnWorkflow.InputFileLocationProperty"]:
            '''Specifies the location for the file being decrypted.

            Use ``${Transfer:UserName}`` or ``${Transfer:UploadDate}`` in this field to parametrize the destination prefix by username or uploaded date.

            - Set the value of ``DestinationFileLocation`` to ``${Transfer:UserName}`` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the name of the Transfer Family user that uploaded the file.
            - Set the value of ``DestinationFileLocation`` to ``${Transfer:UploadDate}`` to decrypt uploaded files to an Amazon S3 bucket that is prefixed with the date of the upload.

            .. epigraph::

               The system resolves ``UploadDate`` to a date format of *YYYY-MM-DD* , based on the date the file is uploaded in UTC.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-destinationfilelocation
            '''
            result = self._values.get("destination_file_location")
            assert result is not None, "Required property 'destination_file_location' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnWorkflow.InputFileLocationProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of encryption used.

            Currently, this value must be ``PGP`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the step, used as an identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def overwrite_existing(self) -> typing.Optional[builtins.str]:
            '''A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .

            If the workflow is processing a file that has the same name as an existing file, the behavior is as follows:

            - If ``OverwriteExisting`` is ``TRUE`` , the existing file is replaced with the file being processed.
            - If ``OverwriteExisting`` is ``FALSE`` , nothing happens, and the workflow processing stops.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-overwriteexisting
            '''
            result = self._values.get("overwrite_existing")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_file_location(self) -> typing.Optional[builtins.str]:
            '''Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

            - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
            - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-decryptstepdetails.html#cfn-transfer-workflow-decryptstepdetails-sourcefilelocation
            '''
            result = self._values.get("source_file_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DecryptStepDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.DeleteStepDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "source_file_location": "sourceFileLocation"},
    )
    class DeleteStepDetailsProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            source_file_location: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that contains the name and file location for a file being deleted by a workflow.

            :param name: The name of the step, used as an identifier.
            :param source_file_location: Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow. - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value. - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-deletestepdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                delete_step_details_property = transfer.CfnWorkflow.DeleteStepDetailsProperty(
                    name="name",
                    source_file_location="sourceFileLocation"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f7c2e3d97255e3322719fe080a52277d52ed4d775d4690ad7c2085afe87a542d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if source_file_location is not None:
                self._values["source_file_location"] = source_file_location

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the step, used as an identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-deletestepdetails.html#cfn-transfer-workflow-deletestepdetails-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_file_location(self) -> typing.Optional[builtins.str]:
            '''Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

            - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
            - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-deletestepdetails.html#cfn-transfer-workflow-deletestepdetails-sourcefilelocation
            '''
            result = self._values.get("source_file_location")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeleteStepDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.EfsInputFileLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"file_system_id": "fileSystemId", "path": "path"},
    )
    class EfsInputFileLocationProperty:
        def __init__(
            self,
            *,
            file_system_id: typing.Optional[builtins.str] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the Amazon EFS identifier and the path for the file being used.

            :param file_system_id: The identifier of the file system, assigned by Amazon EFS.
            :param path: The pathname for the folder being used by a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-efsinputfilelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                efs_input_file_location_property = transfer.CfnWorkflow.EfsInputFileLocationProperty(
                    file_system_id="fileSystemId",
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__965e5b699ccd8f8f2386ed680c1e17a4c9e619a3710a51cfb67ad595180d5115)
                check_type(argname="argument file_system_id", value=file_system_id, expected_type=type_hints["file_system_id"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if file_system_id is not None:
                self._values["file_system_id"] = file_system_id
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def file_system_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the file system, assigned by Amazon EFS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-efsinputfilelocation.html#cfn-transfer-workflow-efsinputfilelocation-filesystemid
            '''
            result = self._values.get("file_system_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The pathname for the folder being used by a workflow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-efsinputfilelocation.html#cfn-transfer-workflow-efsinputfilelocation-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EfsInputFileLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.InputFileLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "efs_file_location": "efsFileLocation",
            "s3_file_location": "s3FileLocation",
        },
    )
    class InputFileLocationProperty:
        def __init__(
            self,
            *,
            efs_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.EfsInputFileLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.S3InputFileLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the location for the file that's being processed.

            :param efs_file_location: Specifies the details for the Amazon Elastic File System (Amazon EFS) file that's being decrypted.
            :param s3_file_location: Specifies the details for the Amazon S3 file that's being copied or decrypted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-inputfilelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                input_file_location_property = transfer.CfnWorkflow.InputFileLocationProperty(
                    efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                        file_system_id="fileSystemId",
                        path="path"
                    ),
                    s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                        bucket="bucket",
                        key="key"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ef802ac0b693b02c2051aafe1b23dea74bfda5557e215fc1fead5cd05a03102c)
                check_type(argname="argument efs_file_location", value=efs_file_location, expected_type=type_hints["efs_file_location"])
                check_type(argname="argument s3_file_location", value=s3_file_location, expected_type=type_hints["s3_file_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if efs_file_location is not None:
                self._values["efs_file_location"] = efs_file_location
            if s3_file_location is not None:
                self._values["s3_file_location"] = s3_file_location

        @builtins.property
        def efs_file_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.EfsInputFileLocationProperty"]]:
            '''Specifies the details for the Amazon Elastic File System (Amazon EFS) file that's being decrypted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-inputfilelocation.html#cfn-transfer-workflow-inputfilelocation-efsfilelocation
            '''
            result = self._values.get("efs_file_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.EfsInputFileLocationProperty"]], result)

        @builtins.property
        def s3_file_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.S3InputFileLocationProperty"]]:
            '''Specifies the details for the Amazon S3 file that's being copied or decrypted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-inputfilelocation.html#cfn-transfer-workflow-inputfilelocation-s3filelocation
            '''
            result = self._values.get("s3_file_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.S3InputFileLocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InputFileLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.S3FileLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_file_location": "s3FileLocation"},
    )
    class S3FileLocationProperty:
        def __init__(
            self,
            *,
            s3_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.S3InputFileLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the S3 details for the file being used, such as bucket, ETag, and so forth.

            :param s3_file_location: Specifies the details for the file location for the file that's being used in the workflow. Only applicable if you are using Amazon S3 storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3filelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                s3_file_location_property = transfer.CfnWorkflow.S3FileLocationProperty(
                    s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                        bucket="bucket",
                        key="key"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f714b7930cabbe06c3dfd1b5e02aa72026653ee111778c90f6dfa421e96ecb8)
                check_type(argname="argument s3_file_location", value=s3_file_location, expected_type=type_hints["s3_file_location"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_file_location is not None:
                self._values["s3_file_location"] = s3_file_location

        @builtins.property
        def s3_file_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.S3InputFileLocationProperty"]]:
            '''Specifies the details for the file location for the file that's being used in the workflow.

            Only applicable if you are using Amazon S3 storage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3filelocation.html#cfn-transfer-workflow-s3filelocation-s3filelocation
            '''
            result = self._values.get("s3_file_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.S3InputFileLocationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3FileLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.S3InputFileLocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key"},
    )
    class S3InputFileLocationProperty:
        def __init__(
            self,
            *,
            bucket: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the details for the Amazon S3 location for an input file to a workflow.

            :param bucket: Specifies the S3 bucket for the customer input file.
            :param key: The name assigned to the file when it was created in Amazon S3. You use the object key to retrieve the object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3inputfilelocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                s3_input_file_location_property = transfer.CfnWorkflow.S3InputFileLocationProperty(
                    bucket="bucket",
                    key="key"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__660c881d769ef4b4e63d6ded2cd19d89aa29e650a554a62d9f305f065c1f2d18)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket is not None:
                self._values["bucket"] = bucket
            if key is not None:
                self._values["key"] = key

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''Specifies the S3 bucket for the customer input file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3inputfilelocation.html#cfn-transfer-workflow-s3inputfilelocation-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The name assigned to the file when it was created in Amazon S3.

            You use the object key to retrieve the object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3inputfilelocation.html#cfn-transfer-workflow-s3inputfilelocation-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3InputFileLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.S3TagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class S3TagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''Specifies the key-value pair that are assigned to a file during the execution of a Tagging step.

            :param key: The name assigned to the tag that you create.
            :param value: The value that corresponds to the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3tag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                s3_tag_property = transfer.CfnWorkflow.S3TagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c976de0d6fa72a21707e195260acc4a49fbfdb932fbde6ec4bc76f0ad1e4070)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The name assigned to the tag that you create.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3tag.html#cfn-transfer-workflow-s3tag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value that corresponds to the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-s3tag.html#cfn-transfer-workflow-s3tag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3TagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.TagStepDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "source_file_location": "sourceFileLocation",
            "tags": "tags",
        },
    )
    class TagStepDetailsProperty:
        def __init__(
            self,
            *,
            name: typing.Optional[builtins.str] = None,
            source_file_location: typing.Optional[builtins.str] = None,
            tags: typing.Optional[typing.Sequence[typing.Union["CfnWorkflow.S3TagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Details for a step that creates one or more tags.

            You specify one or more tags. Each tag contains a key-value pair.

            :param name: The name of the step, used as an identifier.
            :param source_file_location: Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow. - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value. - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .
            :param tags: Array that contains from 1 to 10 key/value pairs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                tag_step_details_property = transfer.CfnWorkflow.TagStepDetailsProperty(
                    name="name",
                    source_file_location="sourceFileLocation",
                    tags=[transfer.CfnWorkflow.S3TagProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed94f236dc5aedb7f83ef33e983923fd8cb323ee4911ae594c780e24f79e9e0b)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument source_file_location", value=source_file_location, expected_type=type_hints["source_file_location"])
                check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if name is not None:
                self._values["name"] = name
            if source_file_location is not None:
                self._values["source_file_location"] = source_file_location
            if tags is not None:
                self._values["tags"] = tags

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the step, used as an identifier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html#cfn-transfer-workflow-tagstepdetails-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_file_location(self) -> typing.Optional[builtins.str]:
            '''Specifies which file to use as input to the workflow step: either the output from the previous step, or the originally uploaded file for the workflow.

            - To use the previous file as the input, enter ``${previous.file}`` . In this case, this workflow step uses the output file from the previous workflow step as input. This is the default value.
            - To use the originally uploaded file location as input for this step, enter ``${original.file}`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html#cfn-transfer-workflow-tagstepdetails-sourcefilelocation
            '''
            result = self._values.get("source_file_location")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tags(self) -> typing.Optional[typing.List["CfnWorkflow.S3TagProperty"]]:
            '''Array that contains from 1 to 10 key/value pairs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-tagstepdetails.html#cfn-transfer-workflow-tagstepdetails-tags
            '''
            result = self._values.get("tags")
            return typing.cast(typing.Optional[typing.List["CfnWorkflow.S3TagProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TagStepDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflow.WorkflowStepProperty",
        jsii_struct_bases=[],
        name_mapping={
            "copy_step_details": "copyStepDetails",
            "custom_step_details": "customStepDetails",
            "decrypt_step_details": "decryptStepDetails",
            "delete_step_details": "deleteStepDetails",
            "tag_step_details": "tagStepDetails",
            "type": "type",
        },
    )
    class WorkflowStepProperty:
        def __init__(
            self,
            *,
            copy_step_details: typing.Any = None,
            custom_step_details: typing.Any = None,
            decrypt_step_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnWorkflow.DecryptStepDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            delete_step_details: typing.Any = None,
            tag_step_details: typing.Any = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The basic building block of a workflow.

            :param copy_step_details: Details for a step that performs a file copy. Consists of the following values: - A description - An Amazon S3 location for the destination of the file copy. - A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .
            :param custom_step_details: Details for a step that invokes an AWS Lambda function. Consists of the Lambda function's name, target, and timeout (in seconds).
            :param decrypt_step_details: Details for a step that decrypts an encrypted file. Consists of the following values: - A descriptive name - An Amazon S3 or Amazon Elastic File System (Amazon EFS) location for the source file to decrypt. - An S3 or Amazon EFS location for the destination of the file decryption. - A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` . - The type of encryption that's used. Currently, only PGP encryption is supported.
            :param delete_step_details: Details for a step that deletes the file.
            :param tag_step_details: Details for a step that creates one or more tags. You specify one or more tags. Each tag contains a key-value pair.
            :param type: Currently, the following step types are supported. - *``COPY``* - Copy the file to another location. - *``CUSTOM``* - Perform a custom step with an AWS Lambda function target. - *``DECRYPT``* - Decrypt a file that was encrypted before it was uploaded. - *``DELETE``* - Delete the file. - *``TAG``* - Add a tag to the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_transfer as transfer
                
                # copy_step_details: Any
                # custom_step_details: Any
                # delete_step_details: Any
                # tag_step_details: Any
                
                workflow_step_property = transfer.CfnWorkflow.WorkflowStepProperty(
                    copy_step_details=copy_step_details,
                    custom_step_details=custom_step_details,
                    decrypt_step_details=transfer.CfnWorkflow.DecryptStepDetailsProperty(
                        destination_file_location=transfer.CfnWorkflow.InputFileLocationProperty(
                            efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                                file_system_id="fileSystemId",
                                path="path"
                            ),
                            s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        type="type",
                
                        # the properties below are optional
                        name="name",
                        overwrite_existing="overwriteExisting",
                        source_file_location="sourceFileLocation"
                    ),
                    delete_step_details=delete_step_details,
                    tag_step_details=tag_step_details,
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b548edb0a5fb9cfebb89a31ba69695395ed26d4793bbaa01e670bb55854f90be)
                check_type(argname="argument copy_step_details", value=copy_step_details, expected_type=type_hints["copy_step_details"])
                check_type(argname="argument custom_step_details", value=custom_step_details, expected_type=type_hints["custom_step_details"])
                check_type(argname="argument decrypt_step_details", value=decrypt_step_details, expected_type=type_hints["decrypt_step_details"])
                check_type(argname="argument delete_step_details", value=delete_step_details, expected_type=type_hints["delete_step_details"])
                check_type(argname="argument tag_step_details", value=tag_step_details, expected_type=type_hints["tag_step_details"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if copy_step_details is not None:
                self._values["copy_step_details"] = copy_step_details
            if custom_step_details is not None:
                self._values["custom_step_details"] = custom_step_details
            if decrypt_step_details is not None:
                self._values["decrypt_step_details"] = decrypt_step_details
            if delete_step_details is not None:
                self._values["delete_step_details"] = delete_step_details
            if tag_step_details is not None:
                self._values["tag_step_details"] = tag_step_details
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def copy_step_details(self) -> typing.Any:
            '''Details for a step that performs a file copy.

            Consists of the following values:

            - A description
            - An Amazon S3 location for the destination of the file copy.
            - A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-copystepdetails
            '''
            result = self._values.get("copy_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def custom_step_details(self) -> typing.Any:
            '''Details for a step that invokes an AWS Lambda function.

            Consists of the Lambda function's name, target, and timeout (in seconds).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-customstepdetails
            '''
            result = self._values.get("custom_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def decrypt_step_details(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.DecryptStepDetailsProperty"]]:
            '''Details for a step that decrypts an encrypted file.

            Consists of the following values:

            - A descriptive name
            - An Amazon S3 or Amazon Elastic File System (Amazon EFS) location for the source file to decrypt.
            - An S3 or Amazon EFS location for the destination of the file decryption.
            - A flag that indicates whether to overwrite an existing file of the same name. The default is ``FALSE`` .
            - The type of encryption that's used. Currently, only PGP encryption is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-decryptstepdetails
            '''
            result = self._values.get("decrypt_step_details")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnWorkflow.DecryptStepDetailsProperty"]], result)

        @builtins.property
        def delete_step_details(self) -> typing.Any:
            '''Details for a step that deletes the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-deletestepdetails
            '''
            result = self._values.get("delete_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def tag_step_details(self) -> typing.Any:
            '''Details for a step that creates one or more tags.

            You specify one or more tags. Each tag contains a key-value pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-tagstepdetails
            '''
            result = self._values.get("tag_step_details")
            return typing.cast(typing.Any, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''Currently, the following step types are supported.

            - *``COPY``* - Copy the file to another location.
            - *``CUSTOM``* - Perform a custom step with an AWS Lambda function target.
            - *``DECRYPT``* - Decrypt a file that was encrypted before it was uploaded.
            - *``DELETE``* - Delete the file.
            - *``TAG``* - Add a tag to the file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-transfer-workflow-workflowstep.html#cfn-transfer-workflow-workflowstep-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkflowStepProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_transfer.CfnWorkflowProps",
    jsii_struct_bases=[],
    name_mapping={
        "steps": "steps",
        "description": "description",
        "on_exception_steps": "onExceptionSteps",
        "tags": "tags",
    },
)
class CfnWorkflowProps:
    def __init__(
        self,
        *,
        steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowStepProperty, typing.Dict[builtins.str, typing.Any]]]]],
        description: typing.Optional[builtins.str] = None,
        on_exception_steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowStepProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnWorkflow``.

        :param steps: Specifies the details for the steps that are in the specified workflow.
        :param description: Specifies the text description for the workflow.
        :param on_exception_steps: Specifies the steps (actions) to take if errors are encountered during execution of the workflow.
        :param tags: Key-value pairs that can be used to group and search for workflows. Tags are metadata attached to workflows for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_transfer as transfer
            
            # copy_step_details: Any
            # custom_step_details: Any
            # delete_step_details: Any
            # tag_step_details: Any
            
            cfn_workflow_props = transfer.CfnWorkflowProps(
                steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                    copy_step_details=copy_step_details,
                    custom_step_details=custom_step_details,
                    decrypt_step_details=transfer.CfnWorkflow.DecryptStepDetailsProperty(
                        destination_file_location=transfer.CfnWorkflow.InputFileLocationProperty(
                            efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                                file_system_id="fileSystemId",
                                path="path"
                            ),
                            s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        type="type",
            
                        # the properties below are optional
                        name="name",
                        overwrite_existing="overwriteExisting",
                        source_file_location="sourceFileLocation"
                    ),
                    delete_step_details=delete_step_details,
                    tag_step_details=tag_step_details,
                    type="type"
                )],
            
                # the properties below are optional
                description="description",
                on_exception_steps=[transfer.CfnWorkflow.WorkflowStepProperty(
                    copy_step_details=copy_step_details,
                    custom_step_details=custom_step_details,
                    decrypt_step_details=transfer.CfnWorkflow.DecryptStepDetailsProperty(
                        destination_file_location=transfer.CfnWorkflow.InputFileLocationProperty(
                            efs_file_location=transfer.CfnWorkflow.EfsInputFileLocationProperty(
                                file_system_id="fileSystemId",
                                path="path"
                            ),
                            s3_file_location=transfer.CfnWorkflow.S3InputFileLocationProperty(
                                bucket="bucket",
                                key="key"
                            )
                        ),
                        type="type",
            
                        # the properties below are optional
                        name="name",
                        overwrite_existing="overwriteExisting",
                        source_file_location="sourceFileLocation"
                    ),
                    delete_step_details=delete_step_details,
                    tag_step_details=tag_step_details,
                    type="type"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3204d3f05faa7a2fceeb6ac7adbf97f5ede342d5c8c3228d5aa0cfb4e29022b4)
            check_type(argname="argument steps", value=steps, expected_type=type_hints["steps"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument on_exception_steps", value=on_exception_steps, expected_type=type_hints["on_exception_steps"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "steps": steps,
        }
        if description is not None:
            self._values["description"] = description
        if on_exception_steps is not None:
            self._values["on_exception_steps"] = on_exception_steps
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def steps(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowStepProperty]]]:
        '''Specifies the details for the steps that are in the specified workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-steps
        '''
        result = self._values.get("steps")
        assert result is not None, "Required property 'steps' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowStepProperty]]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Specifies the text description for the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def on_exception_steps(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowStepProperty]]]]:
        '''Specifies the steps (actions) to take if errors are encountered during execution of the workflow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-onexceptionsteps
        '''
        result = self._values.get("on_exception_steps")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowStepProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can be used to group and search for workflows.

        Tags are metadata attached to workflows for any purpose.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-transfer-workflow.html#cfn-transfer-workflow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnWorkflowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAgreement",
    "CfnAgreementProps",
    "CfnCertificate",
    "CfnCertificateProps",
    "CfnConnector",
    "CfnConnectorProps",
    "CfnProfile",
    "CfnProfileProps",
    "CfnServer",
    "CfnServerProps",
    "CfnUser",
    "CfnUserProps",
    "CfnWorkflow",
    "CfnWorkflowProps",
]

publication.publish()

def _typecheckingstub__f95ec07e6c4ee624e4f9374f7db0e66b46af64fa8c86e2e41aa290c72214e4ab(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_role: builtins.str,
    base_directory: builtins.str,
    local_profile_id: builtins.str,
    partner_profile_id: builtins.str,
    server_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__228db9cea00437d476e4860ef1214693d948e861477e0b0435205c3df9bf79f1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6401d5baaa894d0f43e7153a11e00450f84a7d2eae08481fba5d6eeece91aa77(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6846ae06100d907ce47940f1c737179b266cb64b8ba5e2c4167475979e0e2716(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e95a046a6530138645bcc3d9ea79bf173c25ac44d2324af6ecc4137b705bfc28(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3167bad2c7efdb7b3e0dd7d0402156f8d6e14fae7c15dd40a5fccd0b81e057(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd438983791db4dad3b3d480a6bf25cacd9537198e1ed06c6a676fa3b408f77a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14dc2bb42fd7d8e680f89ab4bbef23a05ad685bb8ba0ece9fc2d04ff9c7d508a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53c57c4c1fcab40ff6fbf72d1b3a40161b6904921f0e56930629bce8dc6662fb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78211aad1a50ad3834dcb7a48092349fa0f45f77997fe33f6e8cab4593032c48(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbeccb7f697f73180ad5ee02e1bc0a8b54212c0eb54c653977d2989de01ad6f1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c92e8cdff7d6f57ae5fd00ef4190544d79a76c01e88d32b21b88588eeb47ba2e(
    *,
    access_role: builtins.str,
    base_directory: builtins.str,
    local_profile_id: builtins.str,
    partner_profile_id: builtins.str,
    server_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    status: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f95ee160137bed43b6b325f0de8dc95bc0d10db792e4492913f9d664df9a567(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate: builtins.str,
    usage: builtins.str,
    active_date: typing.Optional[builtins.str] = None,
    certificate_chain: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inactive_date: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1474a816abc465fbde815216c7dd03f20d910c99fb002aee78d0f01c8d4f55c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__277a102c432293cf858b418d7187668fb07e13095bca6276d8a05cc05818e185(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fa83398b89b8d2e8d3148b42b343e817bfe6f78b80958b2d783b221499449d8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17d42e7b31f98bf4936b925740b19e31175848292139c852b96ff6f0b4e1fe90(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e21cd62811200a42c14a35c21b39187a62f01e9ea383c2661f6e2554927157a2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2df481347ef056a66debc0e80f934287081532818a1ce5e1ba0d0537183f006(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__333e9a8ceb39861e44203fc455ed2ec68cd2d164b99b9114af865c90e44a7f2c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__154790047dfce512ca194065423dd7cea885f3c80210af5f1388990a82c42986(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2850ba9bd4e8becb665faeed903ba33f4e9e56676cc1fa8d8a849f7bd65cd8df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__112d41348367dd1df7b4520890e43a0633334e24689066a3866ad51862dc97c9(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9b7c390d04a925160e4d0a39429a22ee9641e79a668a3dcae449e157976c325(
    *,
    certificate: builtins.str,
    usage: builtins.str,
    active_date: typing.Optional[builtins.str] = None,
    certificate_chain: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    inactive_date: typing.Optional[builtins.str] = None,
    private_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a3d92be7ab611ebe6dbf531ad899c2a95b3655fb829aeffdf52fdb11aae9d07(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_role: builtins.str,
    url: builtins.str,
    as2_config: typing.Any = None,
    logging_role: typing.Optional[builtins.str] = None,
    security_policy_name: typing.Optional[builtins.str] = None,
    sftp_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.SftpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a4f5bff2b8dd506b9f1b6f0cd274f6a295704751fa097cd5e1cf149d089e94(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aab4ede341c608327700d1830ce91ecccf256e71cd06e45d4bd1c9fe8e81f16(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f4bab9f1a3e47eaac0c429ed6125ef23e8b2d8f33fac6396c2ef4a60b8617a2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f2f8d48aab925fcdb11fb86f8b12aeae11aa8b85048a7ded27a817b5864536d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b16726d88010ccba3b94afdf2e5c9f9c1e8e4dc3d9f7d56e2edf0140e687d75c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6fd1718d368db980c8cf49c237a691317f958db670b242715c5440aaf081b1b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c96b636b491e11ce074e40058c1620fda321bb7685ad3a5204502b6fdb4cc24(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__391f4dfc56c4811c4c4aedb8ffcfac5c521d440de2f0de853365abcdec435568(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnector.SftpConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207f7abcb769a2e1717d82ad1c8c7df0c05b8d8d3d89a23127362727dcd65473(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328497a7bbb181a996e0747268f6105731221ad3f578e8a5ca68e405dcdd7e63(
    *,
    basic_auth_secret_id: typing.Optional[builtins.str] = None,
    compression: typing.Optional[builtins.str] = None,
    encryption_algorithm: typing.Optional[builtins.str] = None,
    local_profile_id: typing.Optional[builtins.str] = None,
    mdn_response: typing.Optional[builtins.str] = None,
    mdn_signing_algorithm: typing.Optional[builtins.str] = None,
    message_subject: typing.Optional[builtins.str] = None,
    partner_profile_id: typing.Optional[builtins.str] = None,
    signing_algorithm: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4f8d4be2ad63a06a458c41605c9c21318e1d9117d48f21b9ee2ea6bb109d2e8(
    *,
    trusted_host_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    user_secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7675f9dcded8f51977cf70f499821100319fe5d62996cb917457f772cfcc9a2e(
    *,
    access_role: builtins.str,
    url: builtins.str,
    as2_config: typing.Any = None,
    logging_role: typing.Optional[builtins.str] = None,
    security_policy_name: typing.Optional[builtins.str] = None,
    sftp_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.SftpConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5b82428b7fd1ac13f1a57b868694175d216c1f61c671da5b091d46d81a7fa5c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    as2_id: builtins.str,
    profile_type: builtins.str,
    certificate_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56325834528256f6c2bd12b40bde80e132a645d3bffd84876d0f808ee64a8d81(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf2a5779da146ecf6baff4b026696b629a9454da25b91d74ddd76ab2d5e3b0c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__874129323a36e45f11222542eec1aaa8f0c6a101af85c9157bd91e99153e1f4c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0b0d24da9b7ec761d77dbb7a24743425517ee4b5e684246e4a4a66f364ecc89(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9becc0cd340df21123a424e73d8ffeb9b49be520391d98ec1ecf3c32081ef00(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c41001d8363b6450b3342fb333eb5b5d2a570b2a64b0911308cd8d2824ad0419(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca248e37e97df6c091c4a5b1f174228ff41c93e4175048b0f4e76df0547f4cd7(
    *,
    as2_id: builtins.str,
    profile_type: builtins.str,
    certificate_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf4192baa4fd5a52c9092a6bab5b78398f0e5f14bdad138f58e7990699f038ae(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate: typing.Optional[builtins.str] = None,
    domain: typing.Optional[builtins.str] = None,
    endpoint_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint_type: typing.Optional[builtins.str] = None,
    identity_provider_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.IdentityProviderDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_provider_type: typing.Optional[builtins.str] = None,
    logging_role: typing.Optional[builtins.str] = None,
    post_authentication_login_banner: typing.Optional[builtins.str] = None,
    pre_authentication_login_banner: typing.Optional[builtins.str] = None,
    protocol_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.ProtocolDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.S3StorageOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_policy_name: typing.Optional[builtins.str] = None,
    structured_log_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    workflow_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.WorkflowDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a102be38a6d3ae9d49e28b8883914d07542c58d9491bf5753554a0113ffa87f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b97045b0c5fc436bbcfa181809dbf495470f670463751ef7893661923f939bd5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d563df1c135ed9313e3dcb00bca6377542fc063b499e5019b63083d76d98d4a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fec79565f0dbe159eaa20c23eb0a3a83bd02830760cb60e52cacf1a4cb63a759(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__823691982357b872378325dd203d71148265650854d8786177cbfe72d5cd1cef(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.EndpointDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00ba0605ab69aa9a51bf216b956c181794abc5a526276ac4b9db623c6c0bf7b7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1216795787e100411fafd375b3cfc4b841d96cdfab5edb3bdaad0c4035f93113(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.IdentityProviderDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a6cb2bcf7a55379e6b89fa02d0735271e11fc131bf9d9b0693cea393aa4401(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85db09859b7fcfcae20f45283fb5e74d7f731e8583b8055856472647123250d9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1dfef6051ebbe7b359e51fbbccf44bdd359cd353801a4563eec263eef777c769(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__285d90628b0741ae262fa6e66817df857f96385dc0d6e597c8117867ee84ced2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a9f48a90693f920a173d0269d8553ecc5b0e8d2f2d14cb94fe1075b3651a3d1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.ProtocolDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd2c10237c6e32f4456347dbaa9e2a6133f24a85fbbc337ffc36e289abcbeae1(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__163a1c09687c961e3488fbf0c1737554423fa0fc38fcd229be5018973ec9bb51(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.S3StorageOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c01276e220c0838559c857ba2fd6565aeb281872677b4ec1a9cf3ef85100bd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11770f5eaa4f458a4acec04511188ac9b4a7a0177f6c2e8de622a00cd0a8700(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6c88c4497661801373ac6dc027449a26f4bf736a03ee6cf692728004fb17b26(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b4b59cf92c244a6a1f87cc398c2d4baeea212278bda328f2dd6f2c84abc67e4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnServer.WorkflowDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86c738b4725d61d9fcf1e57609114312f1194c719c25f07a2b6061397bb99d7(
    *,
    address_allocation_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    subnet_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    vpc_endpoint_id: typing.Optional[builtins.str] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8252699fb02969aa8fc67db81cc180b0bb34e8f04f1c627cb561c7fe4f3bb85f(
    *,
    directory_id: typing.Optional[builtins.str] = None,
    function: typing.Optional[builtins.str] = None,
    invocation_role: typing.Optional[builtins.str] = None,
    sftp_authentication_methods: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b1af46c3c18a62e5483e3be74497e66aaecc076ccfe0d473686a4e4b38255cc(
    *,
    as2_transports: typing.Optional[typing.Sequence[builtins.str]] = None,
    passive_ip: typing.Optional[builtins.str] = None,
    set_stat_option: typing.Optional[builtins.str] = None,
    tls_session_resumption_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7f2be4894cf62db2547a5d072c4de8c6e51d04c741195403ed629be98852110(
    *,
    directory_listing_optimization: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03eaccaa8c41960eed5ac1d533ff7d5c2d5b8fb55954177db820e8382860df05(
    *,
    execution_role: builtins.str,
    workflow_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0511d1dd99e09b5726ca7209160f14134b7339c966fe43485d5e7f3ee614892(
    *,
    on_partial_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.WorkflowDetailProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    on_upload: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.WorkflowDetailProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__755735299782e941527b817551c61582134dc6f25d12aff5d9120aeeb47a9ee6(
    *,
    certificate: typing.Optional[builtins.str] = None,
    domain: typing.Optional[builtins.str] = None,
    endpoint_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.EndpointDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint_type: typing.Optional[builtins.str] = None,
    identity_provider_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.IdentityProviderDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    identity_provider_type: typing.Optional[builtins.str] = None,
    logging_role: typing.Optional[builtins.str] = None,
    post_authentication_login_banner: typing.Optional[builtins.str] = None,
    pre_authentication_login_banner: typing.Optional[builtins.str] = None,
    protocol_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.ProtocolDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    protocols: typing.Optional[typing.Sequence[builtins.str]] = None,
    s3_storage_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.S3StorageOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_policy_name: typing.Optional[builtins.str] = None,
    structured_log_destinations: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    workflow_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnServer.WorkflowDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa42271c7d25cb4584b126195a9b597af920cd9c1e4f193efbe2a6d407fe665b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role: builtins.str,
    server_id: builtins.str,
    user_name: builtins.str,
    home_directory: typing.Optional[builtins.str] = None,
    home_directory_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.HomeDirectoryMapEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    home_directory_type: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    posix_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.PosixProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c366b551ea828539c0b8832360f574b612c272eb72c45ba57186d6f9f88ece4c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70895ace466ec04aabc03b4587de7b5439637bdc33988efc767695697eb579b5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc0b372f22cb0ef29120fe3ab548c0ca10b740c11468e6d61db51556704e1d36(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ef5ab6b990dd2596a8e24432c1b5cc6774c6fb7328a87f17aa8968f538a46aa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fb81d11e7cb96377c122bfb8f45feadffb3ee576ada6993c1212e4729f5bdc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c77e829c1d4a272a45dea8460ccc5e13dd485da9cee71caf0c5e21561309747(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42f7f6bf54b856d03c6d1447bb9d5afe1e603f3c84d196395834b94ac8e1ad43(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnUser.HomeDirectoryMapEntryProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c456bc4531fb1dba11ebf05fae08ad26d41da8fd3c1268451a061ae0d2114753(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__212dcb7d96de8b9904cbf9ca69ad0b82b41c0e878e3c7efec36fa71ec7fe0437(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edc3910325c95eaad6c5b004cc7944e382cb7676aa1a2431f7113b2151ec86b9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUser.PosixProfileProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e080a1baa764f200889f63bea8c8060d1553438f95a87e04bf4db6dca1b10305(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cd778c7c12e09594b9e52b3ef35f802dbbc36612c72eb9993d5f0bdb892407f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2013fa8cf00b48e7a477b3cfb9c7ba15a14fd8ec083155cdab295e5e906f4d34(
    *,
    entry: builtins.str,
    target: builtins.str,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8c3948f8e11532949a9c338eb57f070ee1d1b3a7da23c8e2dd5209058536c79(
    *,
    gid: jsii.Number,
    uid: jsii.Number,
    secondary_gids: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad0aa64ea17d55d9634df57b389b841e68b583b0c7f4818453a5cb08787dcc31(
    *,
    role: builtins.str,
    server_id: builtins.str,
    user_name: builtins.str,
    home_directory: typing.Optional[builtins.str] = None,
    home_directory_mappings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.HomeDirectoryMapEntryProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    home_directory_type: typing.Optional[builtins.str] = None,
    policy: typing.Optional[builtins.str] = None,
    posix_profile: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUser.PosixProfileProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ssh_public_keys: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a86ecf6f123d228f6edf61149bc2542f6ce02d9365ac8986ec7c6468379f655(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowStepProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    on_exception_steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowStepProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fcf8488f51b3aba3af306d264af9434fa1e0040f1b353a0381fc97849f0e69f1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa13620584d220c161b9db23ba579d9340ccaa284cc4962e4f437c8b538f0b6(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dad6eb0cfc84813f42cb30691eac8687d1c244e7b0c7a08584547c461c60b6e6(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowStepProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__210eb2eb8f359d51c087a422da2997dfbca2c3a02ef0f5b0023c485aea5ac405(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbe5eec53a115ade4f8181ac2122f17276111f9d5675380186d596e738cbb4c7(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnWorkflow.WorkflowStepProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71de7009c6ec1a7256bbbf8d8fea07e111e611f3c7ca8306d2156be4ff00a297(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b697f702761c46ff428c59596a9536b6c93219cf1dc035facf49a7a9ded2b041(
    *,
    destination_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.S3FileLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    overwrite_existing: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe264913218615c435ebf846cbfed95b995c342d261b4903fa71634538959ea6(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
    timeout_seconds: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad8f772a5a88a70744cbdb419880ea7a579190d4fea687585ef9c062d4a6c34c(
    *,
    destination_file_location: typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.InputFileLocationProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
    overwrite_existing: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7c2e3d97255e3322719fe080a52277d52ed4d775d4690ad7c2085afe87a542d(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__965e5b699ccd8f8f2386ed680c1e17a4c9e619a3710a51cfb67ad595180d5115(
    *,
    file_system_id: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef802ac0b693b02c2051aafe1b23dea74bfda5557e215fc1fead5cd05a03102c(
    *,
    efs_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.EfsInputFileLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.S3InputFileLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f714b7930cabbe06c3dfd1b5e02aa72026653ee111778c90f6dfa421e96ecb8(
    *,
    s3_file_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.S3InputFileLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__660c881d769ef4b4e63d6ded2cd19d89aa29e650a554a62d9f305f065c1f2d18(
    *,
    bucket: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c976de0d6fa72a21707e195260acc4a49fbfdb932fbde6ec4bc76f0ad1e4070(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed94f236dc5aedb7f83ef33e983923fd8cb323ee4911ae594c780e24f79e9e0b(
    *,
    name: typing.Optional[builtins.str] = None,
    source_file_location: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[CfnWorkflow.S3TagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b548edb0a5fb9cfebb89a31ba69695395ed26d4793bbaa01e670bb55854f90be(
    *,
    copy_step_details: typing.Any = None,
    custom_step_details: typing.Any = None,
    decrypt_step_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.DecryptStepDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    delete_step_details: typing.Any = None,
    tag_step_details: typing.Any = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3204d3f05faa7a2fceeb6ac7adbf97f5ede342d5c8c3228d5aa0cfb4e29022b4(
    *,
    steps: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowStepProperty, typing.Dict[builtins.str, typing.Any]]]]],
    description: typing.Optional[builtins.str] = None,
    on_exception_steps: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnWorkflow.WorkflowStepProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
