'''
# AWS Database Migration Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_dms as dms
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for DMS construct libraries](https://constructs.dev/search?q=dms)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::DMS resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::DMS](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_DMS.html).

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
class CfnCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnCertificate",
):
    '''The ``AWS::DMS::Certificate`` resource creates an Secure Sockets Layer (SSL) certificate that encrypts connections between AWS DMS endpoints and the replication instance.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html
    :cloudformationResource: AWS::DMS::Certificate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_certificate = dms.CfnCertificate(self, "MyCfnCertificate",
            certificate_identifier="certificateIdentifier",
            certificate_pem="certificatePem",
            certificate_wallet="certificateWallet"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate_identifier: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_wallet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_identifier: A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
        :param certificate_pem: The contents of a ``.pem`` file, which contains an X.509 certificate.
        :param certificate_wallet: The location of an imported Oracle Wallet certificate for use with SSL. An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7c4a44b8a3c02f3f6ada86310479fa26dc0b32d4fba95316eb3faa446936347)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            certificate_identifier=certificate_identifier,
            certificate_pem=certificate_pem,
            certificate_wallet=certificate_wallet,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec185f31d9affa5fa834d99f40ff8a27fcf34f84f01e6395782727e60768851f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__156b71bbee83d022775901dd6edb948295c746f554fa1406537af9a5b4771300)
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="certificateIdentifier")
    def certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''A customer-assigned name for the certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateIdentifier"))

    @certificate_identifier.setter
    def certificate_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f62a480b92e0600c6f9c24ec065961ca68c8267f28552593ff2bd04d1a6071d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="certificatePem")
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The contents of a ``.pem`` file, which contains an X.509 certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificatePem"))

    @certificate_pem.setter
    def certificate_pem(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__313faf62724606e0e1418e631be23b5d6929e5f5b5dc81d9efcf33f65b18ee6f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificatePem", value)

    @builtins.property
    @jsii.member(jsii_name="certificateWallet")
    def certificate_wallet(self) -> typing.Optional[builtins.str]:
        '''The location of an imported Oracle Wallet certificate for use with SSL.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateWallet"))

    @certificate_wallet.setter
    def certificate_wallet(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d761187c2ccc6e6454d7cb505d195a8e53d4bc1a28c7f3f46d3c576a1fb0671)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateWallet", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_identifier": "certificateIdentifier",
        "certificate_pem": "certificatePem",
        "certificate_wallet": "certificateWallet",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        certificate_identifier: typing.Optional[builtins.str] = None,
        certificate_pem: typing.Optional[builtins.str] = None,
        certificate_wallet: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param certificate_identifier: A customer-assigned name for the certificate. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.
        :param certificate_pem: The contents of a ``.pem`` file, which contains an X.509 certificate.
        :param certificate_wallet: The location of an imported Oracle Wallet certificate for use with SSL. An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_certificate_props = dms.CfnCertificateProps(
                certificate_identifier="certificateIdentifier",
                certificate_pem="certificatePem",
                certificate_wallet="certificateWallet"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70c99920ee84fe825d1d27715d21a77c22d5de3f61e54de6d533397773981c50)
            check_type(argname="argument certificate_identifier", value=certificate_identifier, expected_type=type_hints["certificate_identifier"])
            check_type(argname="argument certificate_pem", value=certificate_pem, expected_type=type_hints["certificate_pem"])
            check_type(argname="argument certificate_wallet", value=certificate_wallet, expected_type=type_hints["certificate_wallet"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if certificate_identifier is not None:
            self._values["certificate_identifier"] = certificate_identifier
        if certificate_pem is not None:
            self._values["certificate_pem"] = certificate_pem
        if certificate_wallet is not None:
            self._values["certificate_wallet"] = certificate_wallet

    @builtins.property
    def certificate_identifier(self) -> typing.Optional[builtins.str]:
        '''A customer-assigned name for the certificate.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificateidentifier
        '''
        result = self._values.get("certificate_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_pem(self) -> typing.Optional[builtins.str]:
        '''The contents of a ``.pem`` file, which contains an X.509 certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatepem
        '''
        result = self._values.get("certificate_pem")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_wallet(self) -> typing.Optional[builtins.str]:
        '''The location of an imported Oracle Wallet certificate for use with SSL.

        An example is: ``filebase64("${path.root}/rds-ca-2019-root.sso")``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-certificate.html#cfn-dms-certificate-certificatewallet
        '''
        result = self._values.get("certificate_wallet")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnDataProvider(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnDataProvider",
):
    '''Provides information that defines a data provider.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html
    :cloudformationResource: AWS::DMS::DataProvider
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_data_provider = dms.CfnDataProvider(self, "MyCfnDataProvider",
            engine="engine",
        
            # the properties below are optional
            data_provider_identifier="dataProviderIdentifier",
            data_provider_name="dataProviderName",
            description="description",
            exact_settings=False,
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
        engine: builtins.str,
        data_provider_identifier: typing.Optional[builtins.str] = None,
        data_provider_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        exact_settings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param engine: The type of database engine for the data provider. Valid values include ``"aurora"`` , ``"aurora-postgresql"`` , ``"mysql"`` , ``"oracle"`` , ``"postgres"`` , ``"sqlserver"`` , ``redshift`` , ``mariadb`` , ``mongodb`` , and ``docdb`` . A value of ``"aurora"`` represents Amazon Aurora MySQL-Compatible Edition.
        :param data_provider_identifier: The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param data_provider_name: The name of the data provider.
        :param description: A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
        :param exact_settings: The property describes the exact settings which can be modified. Default: - false
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf28699baa8f0b678c6576c66e1c53e33b16d9f9cc37b854d4edbc95bf024780)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDataProviderProps(
            engine=engine,
            data_provider_identifier=data_provider_identifier,
            data_provider_name=data_provider_name,
            description=description,
            exact_settings=exact_settings,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c1b19747788e548c485229450a0322a76649d72c3ccc24727e3a33db1fbdf372)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5f3e870b0edacc6af82460cb592fd3d971822bf9675e4fe90ee87e3566e0e6f4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDataProviderArn")
    def attr_data_provider_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) string that uniquely identifies the data provider.

        :cloudformationAttribute: DataProviderArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataProviderArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDataProviderCreationTime")
    def attr_data_provider_creation_time(self) -> builtins.str:
        '''The time the data provider was created.

        :cloudformationAttribute: DataProviderCreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDataProviderCreationTime"))

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
    @jsii.member(jsii_name="engine")
    def engine(self) -> builtins.str:
        '''The type of database engine for the data provider.'''
        return typing.cast(builtins.str, jsii.get(self, "engine"))

    @engine.setter
    def engine(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__020de7951d6d70bc9d3efa600e1210f388dcd2776433c31a4e92b6afe9782ff2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engine", value)

    @builtins.property
    @jsii.member(jsii_name="dataProviderIdentifier")
    def data_provider_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the data provider.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataProviderIdentifier"))

    @data_provider_identifier.setter
    def data_provider_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05caa8991d8aa025161e83d5ae88c03b5b1d3dc49c14071f0728788a968f2568)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataProviderIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="dataProviderName")
    def data_provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the data provider.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "dataProviderName"))

    @data_provider_name.setter
    def data_provider_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__454cfcd7845bc90fe7e1a58a73587247e646a6372c641c3514ea21f8d6f11777)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataProviderName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data provider.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ecadd16a9c7e49c8bf8e1b2e26f904f253dbd4bbefc352e35330e2788cb60915)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="exactSettings")
    def exact_settings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The property describes the exact settings which can be modified.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "exactSettings"))

    @exact_settings.setter
    def exact_settings(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4d016d92a836fecec39275d37ba39e9b434aac43e0b8d6b9a644a15bfff4ef8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exactSettings", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15d6e40a485e85376660625e14969b38fc293c419cb77e7880107c25ae376134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnDataProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "engine": "engine",
        "data_provider_identifier": "dataProviderIdentifier",
        "data_provider_name": "dataProviderName",
        "description": "description",
        "exact_settings": "exactSettings",
        "tags": "tags",
    },
)
class CfnDataProviderProps:
    def __init__(
        self,
        *,
        engine: builtins.str,
        data_provider_identifier: typing.Optional[builtins.str] = None,
        data_provider_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        exact_settings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDataProvider``.

        :param engine: The type of database engine for the data provider. Valid values include ``"aurora"`` , ``"aurora-postgresql"`` , ``"mysql"`` , ``"oracle"`` , ``"postgres"`` , ``"sqlserver"`` , ``redshift`` , ``mariadb`` , ``mongodb`` , and ``docdb`` . A value of ``"aurora"`` represents Amazon Aurora MySQL-Compatible Edition.
        :param data_provider_identifier: The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param data_provider_name: The name of the data provider.
        :param description: A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
        :param exact_settings: The property describes the exact settings which can be modified. Default: - false
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_data_provider_props = dms.CfnDataProviderProps(
                engine="engine",
            
                # the properties below are optional
                data_provider_identifier="dataProviderIdentifier",
                data_provider_name="dataProviderName",
                description="description",
                exact_settings=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97cc3506a599073ab7e0ec6de0479e22078eea7f9108a8ff9c54e506d212555c)
            check_type(argname="argument engine", value=engine, expected_type=type_hints["engine"])
            check_type(argname="argument data_provider_identifier", value=data_provider_identifier, expected_type=type_hints["data_provider_identifier"])
            check_type(argname="argument data_provider_name", value=data_provider_name, expected_type=type_hints["data_provider_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument exact_settings", value=exact_settings, expected_type=type_hints["exact_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "engine": engine,
        }
        if data_provider_identifier is not None:
            self._values["data_provider_identifier"] = data_provider_identifier
        if data_provider_name is not None:
            self._values["data_provider_name"] = data_provider_name
        if description is not None:
            self._values["description"] = description
        if exact_settings is not None:
            self._values["exact_settings"] = exact_settings
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def engine(self) -> builtins.str:
        '''The type of database engine for the data provider.

        Valid values include ``"aurora"`` , ``"aurora-postgresql"`` , ``"mysql"`` , ``"oracle"`` , ``"postgres"`` , ``"sqlserver"`` , ``redshift`` , ``mariadb`` , ``mongodb`` , and ``docdb`` . A value of ``"aurora"`` represents Amazon Aurora MySQL-Compatible Edition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html#cfn-dms-dataprovider-engine
        '''
        result = self._values.get("engine")
        assert result is not None, "Required property 'engine' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_provider_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the data provider.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html#cfn-dms-dataprovider-dataprovideridentifier
        '''
        result = self._values.get("data_provider_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def data_provider_name(self) -> typing.Optional[builtins.str]:
        '''The name of the data provider.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html#cfn-dms-dataprovider-dataprovidername
        '''
        result = self._values.get("data_provider_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the data provider.

        Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html#cfn-dms-dataprovider-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def exact_settings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''The property describes the exact settings which can be modified.

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html#cfn-dms-dataprovider-exactsettings
        '''
        result = self._values.get("exact_settings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-dataprovider.html#cfn-dms-dataprovider-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDataProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEndpoint(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint",
):
    '''The ``AWS::DMS::Endpoint`` resource specifies an AWS DMS endpoint.

    Currently, AWS CloudFormation supports all AWS DMS endpoint types.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html
    :cloudformationResource: AWS::DMS::Endpoint
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_endpoint = dms.CfnEndpoint(self, "MyCfnEndpoint",
            endpoint_type="endpointType",
            engine_name="engineName",
        
            # the properties below are optional
            certificate_arn="certificateArn",
            database_name="databaseName",
            doc_db_settings=dms.CfnEndpoint.DocDbSettingsProperty(
                docs_to_investigate=123,
                extract_doc_id=False,
                nesting_level="nestingLevel",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId"
            ),
            dynamo_db_settings=dms.CfnEndpoint.DynamoDbSettingsProperty(
                service_access_role_arn="serviceAccessRoleArn"
            ),
            elasticsearch_settings=dms.CfnEndpoint.ElasticsearchSettingsProperty(
                endpoint_uri="endpointUri",
                error_retry_duration=123,
                full_load_error_percentage=123,
                service_access_role_arn="serviceAccessRoleArn"
            ),
            endpoint_identifier="endpointIdentifier",
            extra_connection_attributes="extraConnectionAttributes",
            gcp_my_sql_settings=dms.CfnEndpoint.GcpMySQLSettingsProperty(
                after_connect_script="afterConnectScript",
                clean_source_metadata_on_mismatch=False,
                database_name="databaseName",
                events_poll_interval=123,
                max_file_size=123,
                parallel_load_threads=123,
                password="password",
                port=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_name="serverName",
                server_timezone="serverTimezone",
                username="username"
            ),
            ibm_db2_settings=dms.CfnEndpoint.IbmDb2SettingsProperty(
                current_lsn="currentLsn",
                keep_csv_files=False,
                load_timeout=123,
                max_file_size=123,
                max_kBytes_per_read=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                set_data_capture_changes=False,
                write_buffer_size=123
            ),
            kafka_settings=dms.CfnEndpoint.KafkaSettingsProperty(
                broker="broker",
                include_control_details=False,
                include_null_and_empty=False,
                include_partition_value=False,
                include_table_alter_operations=False,
                include_transaction_details=False,
                message_format="messageFormat",
                message_max_bytes=123,
                no_hex_prefix=False,
                partition_include_schema_table=False,
                sasl_password="saslPassword",
                sasl_user_name="saslUserName",
                security_protocol="securityProtocol",
                ssl_ca_certificate_arn="sslCaCertificateArn",
                ssl_client_certificate_arn="sslClientCertificateArn",
                ssl_client_key_arn="sslClientKeyArn",
                ssl_client_key_password="sslClientKeyPassword",
                topic="topic"
            ),
            kinesis_settings=dms.CfnEndpoint.KinesisSettingsProperty(
                include_control_details=False,
                include_null_and_empty=False,
                include_partition_value=False,
                include_table_alter_operations=False,
                include_transaction_details=False,
                message_format="messageFormat",
                no_hex_prefix=False,
                partition_include_schema_table=False,
                service_access_role_arn="serviceAccessRoleArn",
                stream_arn="streamArn"
            ),
            kms_key_id="kmsKeyId",
            microsoft_sql_server_settings=dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty(
                bcp_packet_size=123,
                control_tables_file_group="controlTablesFileGroup",
                database_name="databaseName",
                force_lob_lookup=False,
                password="password",
                port=123,
                query_single_always_on_node=False,
                read_backup_only=False,
                safeguard_policy="safeguardPolicy",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_name="serverName",
                tlog_access_mode="tlogAccessMode",
                trim_space_in_char=False,
                use_bcp_full_load=False,
                username="username",
                use_third_party_backup_device=False
            ),
            mongo_db_settings=dms.CfnEndpoint.MongoDbSettingsProperty(
                auth_mechanism="authMechanism",
                auth_source="authSource",
                auth_type="authType",
                database_name="databaseName",
                docs_to_investigate="docsToInvestigate",
                extract_doc_id="extractDocId",
                nesting_level="nestingLevel",
                password="password",
                port=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_name="serverName",
                username="username"
            ),
            my_sql_settings=dms.CfnEndpoint.MySqlSettingsProperty(
                after_connect_script="afterConnectScript",
                clean_source_metadata_on_mismatch=False,
                events_poll_interval=123,
                max_file_size=123,
                parallel_load_threads=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_timezone="serverTimezone",
                target_db_type="targetDbType"
            ),
            neptune_settings=dms.CfnEndpoint.NeptuneSettingsProperty(
                error_retry_duration=123,
                iam_auth_enabled=False,
                max_file_size=123,
                max_retry_count=123,
                s3_bucket_folder="s3BucketFolder",
                s3_bucket_name="s3BucketName",
                service_access_role_arn="serviceAccessRoleArn"
            ),
            oracle_settings=dms.CfnEndpoint.OracleSettingsProperty(
                access_alternate_directly=False,
                additional_archived_log_dest_id=123,
                add_supplemental_logging=False,
                allow_select_nested_tables=False,
                archived_log_dest_id=123,
                archived_logs_only=False,
                asm_password="asmPassword",
                asm_server="asmServer",
                asm_user="asmUser",
                char_length_semantics="charLengthSemantics",
                direct_path_no_log=False,
                direct_path_parallel_load=False,
                enable_homogenous_tablespace=False,
                extra_archived_log_dest_ids=[123],
                fail_tasks_on_lob_truncation=False,
                number_datatype_scale=123,
                oracle_path_prefix="oraclePathPrefix",
                parallel_asm_read_threads=123,
                read_ahead_blocks=123,
                read_table_space_name=False,
                replace_path_prefix=False,
                retry_interval=123,
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_oracle_asm_access_role_arn="secretsManagerOracleAsmAccessRoleArn",
                secrets_manager_oracle_asm_secret_id="secretsManagerOracleAsmSecretId",
                secrets_manager_secret_id="secretsManagerSecretId",
                security_db_encryption="securityDbEncryption",
                security_db_encryption_name="securityDbEncryptionName",
                spatial_data_option_to_geo_json_function_name="spatialDataOptionToGeoJsonFunctionName",
                standby_delay_time=123,
                use_alternate_folder_for_online=False,
                use_bFile=False,
                use_direct_path_full_load=False,
                use_logminer_reader=False,
                use_path_prefix="usePathPrefix"
            ),
            password="password",
            port=123,
            postgre_sql_settings=dms.CfnEndpoint.PostgreSqlSettingsProperty(
                after_connect_script="afterConnectScript",
                babelfish_database_name="babelfishDatabaseName",
                capture_ddls=False,
                database_mode="databaseMode",
                ddl_artifacts_schema="ddlArtifactsSchema",
                execute_timeout=123,
                fail_tasks_on_lob_truncation=False,
                heartbeat_enable=False,
                heartbeat_frequency=123,
                heartbeat_schema="heartbeatSchema",
                map_boolean_as_boolean=False,
                max_file_size=123,
                plugin_name="pluginName",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                slot_name="slotName"
            ),
            redis_settings=dms.CfnEndpoint.RedisSettingsProperty(
                auth_password="authPassword",
                auth_type="authType",
                auth_user_name="authUserName",
                port=123,
                server_name="serverName",
                ssl_ca_certificate_arn="sslCaCertificateArn",
                ssl_security_protocol="sslSecurityProtocol"
            ),
            redshift_settings=dms.CfnEndpoint.RedshiftSettingsProperty(
                accept_any_date=False,
                after_connect_script="afterConnectScript",
                bucket_folder="bucketFolder",
                bucket_name="bucketName",
                case_sensitive_names=False,
                comp_update=False,
                connection_timeout=123,
                date_format="dateFormat",
                empty_as_null=False,
                encryption_mode="encryptionMode",
                explicit_ids=False,
                file_transfer_upload_streams=123,
                load_timeout=123,
                map_boolean_as_boolean=False,
                max_file_size=123,
                remove_quotes=False,
                replace_chars="replaceChars",
                replace_invalid_chars="replaceInvalidChars",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId",
                server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                service_access_role_arn="serviceAccessRoleArn",
                time_format="timeFormat",
                trim_blanks=False,
                truncate_columns=False,
                write_buffer_size=123
            ),
            resource_identifier="resourceIdentifier",
            s3_settings=dms.CfnEndpoint.S3SettingsProperty(
                add_column_name=False,
                add_trailing_padding_character=False,
                bucket_folder="bucketFolder",
                bucket_name="bucketName",
                canned_acl_for_objects="cannedAclForObjects",
                cdc_inserts_and_updates=False,
                cdc_inserts_only=False,
                cdc_max_batch_interval=123,
                cdc_min_file_size=123,
                cdc_path="cdcPath",
                compression_type="compressionType",
                csv_delimiter="csvDelimiter",
                csv_no_sup_value="csvNoSupValue",
                csv_null_value="csvNullValue",
                csv_row_delimiter="csvRowDelimiter",
                data_format="dataFormat",
                data_page_size=123,
                date_partition_delimiter="datePartitionDelimiter",
                date_partition_enabled=False,
                date_partition_sequence="datePartitionSequence",
                date_partition_timezone="datePartitionTimezone",
                dict_page_size_limit=123,
                enable_statistics=False,
                encoding_type="encodingType",
                encryption_mode="encryptionMode",
                expected_bucket_owner="expectedBucketOwner",
                external_table_definition="externalTableDefinition",
                glue_catalog_generation=False,
                ignore_header_rows=123,
                include_op_for_full_load=False,
                max_file_size=123,
                parquet_timestamp_in_millisecond=False,
                parquet_version="parquetVersion",
                preserve_transactions=False,
                rfc4180=False,
                row_group_length=123,
                server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                service_access_role_arn="serviceAccessRoleArn",
                timestamp_column_name="timestampColumnName",
                use_csv_no_sup_value=False,
                use_task_start_time_for_full_load_timestamp=False
            ),
            server_name="serverName",
            ssl_mode="sslMode",
            sybase_settings=dms.CfnEndpoint.SybaseSettingsProperty(
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId"
            ),
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
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        doc_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.DocDbSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dynamo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.DynamoDbSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.ElasticsearchSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        endpoint_identifier: typing.Optional[builtins.str] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        gcp_my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.GcpMySQLSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ibm_db2_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.IbmDb2SettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kafka_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.KafkaSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.KinesisSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        microsoft_sql_server_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.MicrosoftSqlServerSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.MongoDbSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.MySqlSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        neptune_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.NeptuneSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        oracle_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.OracleSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        postgre_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.PostgreSqlSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        redis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.RedisSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        redshift_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.RedshiftSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        s3_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.S3SettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        server_name: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sybase_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEndpoint.SybaseSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param endpoint_type: The type of endpoint. Valid values are ``source`` and ``target`` .
        :param engine_name: The type of engine for the endpoint, depending on the ``EndpointType`` value. *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``redshift-serverless`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``
        :param certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param database_name: The name of the endpoint database. For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .
        :param doc_db_settings: Settings in JSON format for the source and target DocumentDB endpoint. For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .
        :param dynamo_db_settings: Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param elasticsearch_settings: Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param endpoint_identifier: The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param extra_connection_attributes: Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .
        :param gcp_my_sql_settings: Settings in JSON format for the source GCP MySQL endpoint. These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param ibm_db2_settings: Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param kafka_settings: Settings in JSON format for the target Apache Kafka endpoint. For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kinesis_settings: Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param microsoft_sql_server_settings: Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param mongo_db_settings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param my_sql_settings: Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param neptune_settings: Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param oracle_settings: Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param password: The password to be used to log in to the endpoint database.
        :param port: The port used by the endpoint database.
        :param postgre_sql_settings: Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param redis_settings: Settings in JSON format for the target Redis endpoint. For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param redshift_settings: Settings in JSON format for the Amazon Redshift endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param s3_settings: Settings in JSON format for the source and target Amazon S3 endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .
        :param server_name: The name of the server where the endpoint database resides.
        :param ssl_mode: The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` . .. epigraph:: When ``engine_name`` is set to S3, the only allowed value is ``none`` .
        :param sybase_settings: Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param tags: One or more tags to be assigned to the endpoint.
        :param username: The user name to be used to log in to the endpoint database.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__738d71cd2300575c2c6537801f3dede195e2179cefcdceb9d0410340f5b1615e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEndpointProps(
            endpoint_type=endpoint_type,
            engine_name=engine_name,
            certificate_arn=certificate_arn,
            database_name=database_name,
            doc_db_settings=doc_db_settings,
            dynamo_db_settings=dynamo_db_settings,
            elasticsearch_settings=elasticsearch_settings,
            endpoint_identifier=endpoint_identifier,
            extra_connection_attributes=extra_connection_attributes,
            gcp_my_sql_settings=gcp_my_sql_settings,
            ibm_db2_settings=ibm_db2_settings,
            kafka_settings=kafka_settings,
            kinesis_settings=kinesis_settings,
            kms_key_id=kms_key_id,
            microsoft_sql_server_settings=microsoft_sql_server_settings,
            mongo_db_settings=mongo_db_settings,
            my_sql_settings=my_sql_settings,
            neptune_settings=neptune_settings,
            oracle_settings=oracle_settings,
            password=password,
            port=port,
            postgre_sql_settings=postgre_sql_settings,
            redis_settings=redis_settings,
            redshift_settings=redshift_settings,
            resource_identifier=resource_identifier,
            s3_settings=s3_settings,
            server_name=server_name,
            ssl_mode=ssl_mode,
            sybase_settings=sybase_settings,
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
            type_hints = typing.get_type_hints(_typecheckingstub__f057bd27ac6280cd130ed12f9511a5cdfb108a079b1bda778b1eafc415ee366d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dabdd788a3f89fb25343348143b10c8f247445904b595e33249479bbe047aa2f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrExternalId")
    def attr_external_id(self) -> builtins.str:
        '''A value that can be used for cross-account validation.

        :cloudformationAttribute: ExternalId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrExternalId"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''
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
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        '''The type of endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eda1263f706197fdf07170ebe2dd59f394f263e412b2d4e5dd097f6126b80995)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="engineName")
    def engine_name(self) -> builtins.str:
        '''The type of engine for the endpoint, depending on the ``EndpointType`` value.'''
        return typing.cast(builtins.str, jsii.get(self, "engineName"))

    @engine_name.setter
    def engine_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63622e2ea94914c36460dc51358529b45a8dccc7d4b2c8b2cd29cfa5a8a292c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateArn"))

    @certificate_arn.setter
    def certificate_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a24a958c0fb12c44c9cb90d3499e73f80f94637351708be30c85163fc7c3694)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateArn", value)

    @builtins.property
    @jsii.member(jsii_name="databaseName")
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the endpoint database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "databaseName"))

    @database_name.setter
    def database_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7fa111faf4b7852de973ab5c9eef4a2e95048c2fb0e4c4677655ec5b350a002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "databaseName", value)

    @builtins.property
    @jsii.member(jsii_name="docDbSettings")
    def doc_db_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.DocDbSettingsProperty"]]:
        '''Settings in JSON format for the source and target DocumentDB endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.DocDbSettingsProperty"]], jsii.get(self, "docDbSettings"))

    @doc_db_settings.setter
    def doc_db_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.DocDbSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__964181ee2a910015024cb3f101a00f9f8185212a583fc0880419c4b8f4665704)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "docDbSettings", value)

    @builtins.property
    @jsii.member(jsii_name="dynamoDbSettings")
    def dynamo_db_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.DynamoDbSettingsProperty"]]:
        '''Settings in JSON format for the target Amazon DynamoDB endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.DynamoDbSettingsProperty"]], jsii.get(self, "dynamoDbSettings"))

    @dynamo_db_settings.setter
    def dynamo_db_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.DynamoDbSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1e66bdb10c14f72319011edd2b4677a0c649392f33602507802cb167a5121d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dynamoDbSettings", value)

    @builtins.property
    @jsii.member(jsii_name="elasticsearchSettings")
    def elasticsearch_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.ElasticsearchSettingsProperty"]]:
        '''Settings in JSON format for the target OpenSearch endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.ElasticsearchSettingsProperty"]], jsii.get(self, "elasticsearchSettings"))

    @elasticsearch_settings.setter
    def elasticsearch_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.ElasticsearchSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a06f40e1959e428f7f5c27f542081cd85f979ba31209ebc3fe63da010fddb64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "elasticsearchSettings", value)

    @builtins.property
    @jsii.member(jsii_name="endpointIdentifier")
    def endpoint_identifier(self) -> typing.Optional[builtins.str]:
        '''The database endpoint identifier.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "endpointIdentifier"))

    @endpoint_identifier.setter
    def endpoint_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92a35632be5509ee14e90879734777fda7c0b08f4db0213ccb6b20ac83182823)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="extraConnectionAttributes")
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Additional attributes associated with the connection.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "extraConnectionAttributes"))

    @extra_connection_attributes.setter
    def extra_connection_attributes(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e00122aa6cacf409b94a9e3ae515c70d887464581820b45e08ce367673072c58)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "extraConnectionAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="gcpMySqlSettings")
    def gcp_my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.GcpMySQLSettingsProperty"]]:
        '''Settings in JSON format for the source GCP MySQL endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.GcpMySQLSettingsProperty"]], jsii.get(self, "gcpMySqlSettings"))

    @gcp_my_sql_settings.setter
    def gcp_my_sql_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.GcpMySQLSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c3a8d92e577dbc9df7cec45318f33c1e0fcbdf463cc7dfd5569ea58f1d00c06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gcpMySqlSettings", value)

    @builtins.property
    @jsii.member(jsii_name="ibmDb2Settings")
    def ibm_db2_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.IbmDb2SettingsProperty"]]:
        '''Settings in JSON format for the source IBM Db2 LUW endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.IbmDb2SettingsProperty"]], jsii.get(self, "ibmDb2Settings"))

    @ibm_db2_settings.setter
    def ibm_db2_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.IbmDb2SettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44fef44c81ef6b8da87158243f0ccbedc43e7299d8652a35b098afa7a04a61c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ibmDb2Settings", value)

    @builtins.property
    @jsii.member(jsii_name="kafkaSettings")
    def kafka_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.KafkaSettingsProperty"]]:
        '''Settings in JSON format for the target Apache Kafka endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.KafkaSettingsProperty"]], jsii.get(self, "kafkaSettings"))

    @kafka_settings.setter
    def kafka_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.KafkaSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b7582d27225e5fe52e2294251941bf9c566610655a620a14039a2b6f9e42b21)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kafkaSettings", value)

    @builtins.property
    @jsii.member(jsii_name="kinesisSettings")
    def kinesis_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.KinesisSettingsProperty"]]:
        '''Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.KinesisSettingsProperty"]], jsii.get(self, "kinesisSettings"))

    @kinesis_settings.setter
    def kinesis_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.KinesisSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ceccea684f95f5083095044bdbf739f8871dcf9b280587dfc9f741fad0e19969)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisSettings", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f98695584c46299d7a2dcf051622c328dcc6be01c1ec45e4645a4976755b9b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="microsoftSqlServerSettings")
    def microsoft_sql_server_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MicrosoftSqlServerSettingsProperty"]]:
        '''Settings in JSON format for the source and target Microsoft SQL Server endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MicrosoftSqlServerSettingsProperty"]], jsii.get(self, "microsoftSqlServerSettings"))

    @microsoft_sql_server_settings.setter
    def microsoft_sql_server_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MicrosoftSqlServerSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0d6650a04db2e7248a94227234af24d3685774adf590b885acf6d9a8e46f33c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "microsoftSqlServerSettings", value)

    @builtins.property
    @jsii.member(jsii_name="mongoDbSettings")
    def mongo_db_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MongoDbSettingsProperty"]]:
        '''Settings in JSON format for the source MongoDB endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MongoDbSettingsProperty"]], jsii.get(self, "mongoDbSettings"))

    @mongo_db_settings.setter
    def mongo_db_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MongoDbSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c34d02d08d15c9c23ee3acd69fc24c805faf00f28977c15fc4904ad2240ff59)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mongoDbSettings", value)

    @builtins.property
    @jsii.member(jsii_name="mySqlSettings")
    def my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MySqlSettingsProperty"]]:
        '''Settings in JSON format for the source and target MySQL endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MySqlSettingsProperty"]], jsii.get(self, "mySqlSettings"))

    @my_sql_settings.setter
    def my_sql_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.MySqlSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33dc654f9976a21468a898b3a1a83eab0b9827d20b4050ca617ac942a51a2bc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mySqlSettings", value)

    @builtins.property
    @jsii.member(jsii_name="neptuneSettings")
    def neptune_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.NeptuneSettingsProperty"]]:
        '''Settings in JSON format for the target Amazon Neptune endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.NeptuneSettingsProperty"]], jsii.get(self, "neptuneSettings"))

    @neptune_settings.setter
    def neptune_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.NeptuneSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4bf2bf255501ef1ab216d754bda1b21fd5c2d7fa8b9eb7aef6710a3a3486ac0e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "neptuneSettings", value)

    @builtins.property
    @jsii.member(jsii_name="oracleSettings")
    def oracle_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.OracleSettingsProperty"]]:
        '''Settings in JSON format for the source and target Oracle endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.OracleSettingsProperty"]], jsii.get(self, "oracleSettings"))

    @oracle_settings.setter
    def oracle_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.OracleSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b582a457202f3791a344c9af49ce79ffaf942cd191b44898b2f3c01b25dcc73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "oracleSettings", value)

    @builtins.property
    @jsii.member(jsii_name="password")
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to be used to log in to the endpoint database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "password"))

    @password.setter
    def password(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8fd19a57de2f1cfb856e6db1169b1753391b1b029e1d88babd8e74254c6a135)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "password", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port used by the endpoint database.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc21911fa58b80854e027035398d650995a4315e7a391656d88cbdffe85c10b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="postgreSqlSettings")
    def postgre_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.PostgreSqlSettingsProperty"]]:
        '''Settings in JSON format for the source and target PostgreSQL endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.PostgreSqlSettingsProperty"]], jsii.get(self, "postgreSqlSettings"))

    @postgre_sql_settings.setter
    def postgre_sql_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.PostgreSqlSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ae50808797b6c50dc9996fead375c4ab91f2b93a7e63dfb0f24b0eda9b51f9e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "postgreSqlSettings", value)

    @builtins.property
    @jsii.member(jsii_name="redisSettings")
    def redis_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.RedisSettingsProperty"]]:
        '''Settings in JSON format for the target Redis endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.RedisSettingsProperty"]], jsii.get(self, "redisSettings"))

    @redis_settings.setter
    def redis_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.RedisSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__804bbb4ffca52155c93eb3b6c86a39edc8f1c8e0f7285eed7a57484757768a01)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redisSettings", value)

    @builtins.property
    @jsii.member(jsii_name="redshiftSettings")
    def redshift_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.RedshiftSettingsProperty"]]:
        '''Settings in JSON format for the Amazon Redshift endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.RedshiftSettingsProperty"]], jsii.get(self, "redshiftSettings"))

    @redshift_settings.setter
    def redshift_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.RedshiftSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29371f2c2b4a796793306172c888eba1b4d13b9962006ea4ea55d37fd5168a89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "redshiftSettings", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b0c28b3eb52d69409a66690703aa50b58092a39244a75cec0482fe1b15ddf90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="s3Settings")
    def s3_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.S3SettingsProperty"]]:
        '''Settings in JSON format for the source and target Amazon S3 endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.S3SettingsProperty"]], jsii.get(self, "s3Settings"))

    @s3_settings.setter
    def s3_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.S3SettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beebfa648d87c594a19d4f5008c375d047ed33feb9cda485735fdfbdf6778832)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "s3Settings", value)

    @builtins.property
    @jsii.member(jsii_name="serverName")
    def server_name(self) -> typing.Optional[builtins.str]:
        '''The name of the server where the endpoint database resides.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "serverName"))

    @server_name.setter
    def server_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47a4f86e530d3114bac695174df1fa4dfd6e883942abff5dbd2860264e4f021d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serverName", value)

    @builtins.property
    @jsii.member(jsii_name="sslMode")
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''The Secure Sockets Layer (SSL) mode to use for the SSL connection.

        The default is ``none`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sslMode"))

    @ssl_mode.setter
    def ssl_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b43aa7a197c10a98a463aa675a5dab6fedd3c8ab62c561e6c675f9cbf2294ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sslMode", value)

    @builtins.property
    @jsii.member(jsii_name="sybaseSettings")
    def sybase_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.SybaseSettingsProperty"]]:
        '''Settings in JSON format for the source and target SAP ASE endpoint.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.SybaseSettingsProperty"]], jsii.get(self, "sybaseSettings"))

    @sybase_settings.setter
    def sybase_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEndpoint.SybaseSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8233892017699d61eafcea4f1e10c7e0569b5267219badd590e4c1371d4b6fad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sybaseSettings", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the endpoint.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8deb35cf3c053bed3738b0ba1313a78b00c19fe30ee591619e0da0e7a7a4be5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="username")
    def username(self) -> typing.Optional[builtins.str]:
        '''The user name to be used to log in to the endpoint database.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "username"))

    @username.setter
    def username(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b95c2f7591c459e1e407d93e4a7301b1635408431907ffa3cf1c028147952ba)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "username", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.DocDbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "docs_to_investigate": "docsToInvestigate",
            "extract_doc_id": "extractDocId",
            "nesting_level": "nestingLevel",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
        },
    )
    class DocDbSettingsProperty:
        def __init__(
            self,
            *,
            docs_to_investigate: typing.Optional[jsii.Number] = None,
            extract_doc_id: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            nesting_level: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a DocumentDB endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .

            :param docs_to_investigate: Indicates the number of documents to preview to determine the document organization. Use this setting when ``NestingLevel`` is set to ``"one"`` . Must be a positive value greater than ``0`` . Default value is ``1000`` .
            :param extract_doc_id: Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` . Default value is ``"false"`` .
            :param nesting_level: Specifies either document or table mode. Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the DocumentDB endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the DocumentDB endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                doc_db_settings_property = dms.CfnEndpoint.DocDbSettingsProperty(
                    docs_to_investigate=123,
                    extract_doc_id=False,
                    nesting_level="nestingLevel",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a8cdb9146705c1a54770bd05f52b51754d3652539f062721a2b89a9e45593717)
                check_type(argname="argument docs_to_investigate", value=docs_to_investigate, expected_type=type_hints["docs_to_investigate"])
                check_type(argname="argument extract_doc_id", value=extract_doc_id, expected_type=type_hints["extract_doc_id"])
                check_type(argname="argument nesting_level", value=nesting_level, expected_type=type_hints["nesting_level"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if docs_to_investigate is not None:
                self._values["docs_to_investigate"] = docs_to_investigate
            if extract_doc_id is not None:
                self._values["extract_doc_id"] = extract_doc_id
            if nesting_level is not None:
                self._values["nesting_level"] = nesting_level
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id

        @builtins.property
        def docs_to_investigate(self) -> typing.Optional[jsii.Number]:
            '''Indicates the number of documents to preview to determine the document organization.

            Use this setting when ``NestingLevel`` is set to ``"one"`` .

            Must be a positive value greater than ``0`` . Default value is ``1000`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-docstoinvestigate
            '''
            result = self._values.get("docs_to_investigate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def extract_doc_id(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` .

            Default value is ``"false"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-extractdocid
            '''
            result = self._values.get("extract_doc_id")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def nesting_level(self) -> typing.Optional[builtins.str]:
            '''Specifies either document or table mode.

            Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-nestinglevel
            '''
            result = self._values.get("nesting_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the DocumentDB endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the DocumentDB endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-docdbsettings.html#cfn-dms-endpoint-docdbsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DocDbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.DynamoDbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"service_access_role_arn": "serviceAccessRoleArn"},
    )
    class DynamoDbSettingsProperty:
        def __init__(
            self,
            *,
            service_access_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information, including the Amazon Resource Name (ARN) of the IAM role used to define an Amazon DynamoDB target endpoint.

            This information also includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

            :param service_access_role_arn: The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the ``iam:PassRole`` action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                dynamo_db_settings_property = dms.CfnEndpoint.DynamoDbSettingsProperty(
                    service_access_role_arn="serviceAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5fec091a86dd85d23a1c02ae7d2b8611a5b093400587254d7ab8c085313f61e)
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) used by the service to access the IAM role.

            The role must allow the ``iam:PassRole`` action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-dynamodbsettings.html#cfn-dms-endpoint-dynamodbsettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.ElasticsearchSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "endpoint_uri": "endpointUri",
            "error_retry_duration": "errorRetryDuration",
            "full_load_error_percentage": "fullLoadErrorPercentage",
            "service_access_role_arn": "serviceAccessRoleArn",
        },
    )
    class ElasticsearchSettingsProperty:
        def __init__(
            self,
            *,
            endpoint_uri: typing.Optional[builtins.str] = None,
            error_retry_duration: typing.Optional[jsii.Number] = None,
            full_load_error_percentage: typing.Optional[jsii.Number] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines an OpenSearch endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .

            :param endpoint_uri: The endpoint for the OpenSearch cluster. AWS DMS uses HTTPS if a transport protocol (either HTTP or HTTPS) isn't specified.
            :param error_retry_duration: The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.
            :param full_load_error_percentage: The maximum percentage of records that can fail to be written before a full load operation stops. To avoid early failure, this counter is only effective after 1,000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.
            :param service_access_role_arn: The Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the ``iam:PassRole`` action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                elasticsearch_settings_property = dms.CfnEndpoint.ElasticsearchSettingsProperty(
                    endpoint_uri="endpointUri",
                    error_retry_duration=123,
                    full_load_error_percentage=123,
                    service_access_role_arn="serviceAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b42a4ad0c21b34a6010425ced42894f16cb42370a9e17e351b058db62751a2c6)
                check_type(argname="argument endpoint_uri", value=endpoint_uri, expected_type=type_hints["endpoint_uri"])
                check_type(argname="argument error_retry_duration", value=error_retry_duration, expected_type=type_hints["error_retry_duration"])
                check_type(argname="argument full_load_error_percentage", value=full_load_error_percentage, expected_type=type_hints["full_load_error_percentage"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint_uri is not None:
                self._values["endpoint_uri"] = endpoint_uri
            if error_retry_duration is not None:
                self._values["error_retry_duration"] = error_retry_duration
            if full_load_error_percentage is not None:
                self._values["full_load_error_percentage"] = full_load_error_percentage
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn

        @builtins.property
        def endpoint_uri(self) -> typing.Optional[builtins.str]:
            '''The endpoint for the OpenSearch cluster.

            AWS DMS uses HTTPS if a transport protocol (either HTTP or HTTPS) isn't specified.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-endpointuri
            '''
            result = self._values.get("endpoint_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_retry_duration(self) -> typing.Optional[jsii.Number]:
            '''The maximum number of seconds for which DMS retries failed API requests to the OpenSearch cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-errorretryduration
            '''
            result = self._values.get("error_retry_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def full_load_error_percentage(self) -> typing.Optional[jsii.Number]:
            '''The maximum percentage of records that can fail to be written before a full load operation stops.

            To avoid early failure, this counter is only effective after 1,000 records are transferred. OpenSearch also has the concept of error monitoring during the last 10 minutes of an Observation Window. If transfer of all records fail in the last 10 minutes, the full load operation stops.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-fullloaderrorpercentage
            '''
            result = self._values.get("full_load_error_percentage")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) used by the service to access the IAM role.

            The role must allow the ``iam:PassRole`` action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-elasticsearchsettings.html#cfn-dms-endpoint-elasticsearchsettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ElasticsearchSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.GcpMySQLSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_connect_script": "afterConnectScript",
            "clean_source_metadata_on_mismatch": "cleanSourceMetadataOnMismatch",
            "database_name": "databaseName",
            "events_poll_interval": "eventsPollInterval",
            "max_file_size": "maxFileSize",
            "parallel_load_threads": "parallelLoadThreads",
            "password": "password",
            "port": "port",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_name": "serverName",
            "server_timezone": "serverTimezone",
            "username": "username",
        },
    )
    class GcpMySQLSettingsProperty:
        def __init__(
            self,
            *,
            after_connect_script: typing.Optional[builtins.str] = None,
            clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            database_name: typing.Optional[builtins.str] = None,
            events_poll_interval: typing.Optional[jsii.Number] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            parallel_load_threads: typing.Optional[jsii.Number] = None,
            password: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_name: typing.Optional[builtins.str] = None,
            server_timezone: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a GCP MySQL endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param after_connect_script: Specifies a script to run immediately after AWS DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails. For this parameter, provide the code of the script itself, not the name of a file containing the script.
            :param clean_source_metadata_on_mismatch: Adjusts the behavior of AWS DMS when migrating from an SQL Server source database that is hosted as part of an Always On availability group cluster. If you need AWS DMS to poll all the nodes in the Always On cluster for transaction backups, set this attribute to ``false`` .
            :param database_name: Database name for the endpoint. For a MySQL source or target endpoint, don't explicitly specify the database using the ``DatabaseName`` request parameter on either the ``CreateEndpoint`` or ``ModifyEndpoint`` API call. Specifying ``DatabaseName`` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.
            :param events_poll_interval: Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds. Example: ``eventsPollInterval=5;`` In the example, AWS DMS checks for changes in the binary logs every five seconds.
            :param max_file_size: Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database. Example: ``maxFileSize=512``
            :param parallel_load_threads: Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one. Example: ``parallelLoadThreads=1``
            :param password: Endpoint connection password.
            :param port: The port used by the endpoint database.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret.`` The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.
            :param server_name: The MySQL host name.
            :param server_timezone: Specifies the time zone for the source MySQL database. Don't enclose time zones in single quotation marks. Example: ``serverTimezone=US/Pacific;``
            :param username: Endpoint connection user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                gcp_my_sQLSettings_property = dms.CfnEndpoint.GcpMySQLSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    database_name="databaseName",
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    server_timezone="serverTimezone",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__71c426338e480f2fd367da249eee3d680fa0655f66784733cc1ee66376abd5e2)
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument clean_source_metadata_on_mismatch", value=clean_source_metadata_on_mismatch, expected_type=type_hints["clean_source_metadata_on_mismatch"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument events_poll_interval", value=events_poll_interval, expected_type=type_hints["events_poll_interval"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument parallel_load_threads", value=parallel_load_threads, expected_type=type_hints["parallel_load_threads"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument server_timezone", value=server_timezone, expected_type=type_hints["server_timezone"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if clean_source_metadata_on_mismatch is not None:
                self._values["clean_source_metadata_on_mismatch"] = clean_source_metadata_on_mismatch
            if database_name is not None:
                self._values["database_name"] = database_name
            if events_poll_interval is not None:
                self._values["events_poll_interval"] = events_poll_interval
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if parallel_load_threads is not None:
                self._values["parallel_load_threads"] = parallel_load_threads
            if password is not None:
                self._values["password"] = password
            if port is not None:
                self._values["port"] = port
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_name is not None:
                self._values["server_name"] = server_name
            if server_timezone is not None:
                self._values["server_timezone"] = server_timezone
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''Specifies a script to run immediately after AWS DMS connects to the endpoint.

            The migration task continues running regardless if the SQL statement succeeds or fails.

            For this parameter, provide the code of the script itself, not the name of a file containing the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def clean_source_metadata_on_mismatch(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Adjusts the behavior of AWS DMS when migrating from an SQL Server source database that is hosted as part of an Always On availability group cluster.

            If you need AWS DMS to poll all the nodes in the Always On cluster for transaction backups, set this attribute to ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-cleansourcemetadataonmismatch
            '''
            result = self._values.get("clean_source_metadata_on_mismatch")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Database name for the endpoint.

            For a MySQL source or target endpoint, don't explicitly specify the database using the ``DatabaseName`` request parameter on either the ``CreateEndpoint`` or ``ModifyEndpoint`` API call. Specifying ``DatabaseName`` when you create or modify a MySQL endpoint replicates all the task tables to this single database. For MySQL endpoints, you specify the database only when you specify the schema in the table-mapping rules of the AWS DMS task.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def events_poll_interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies how often to check the binary log for new changes/events when the database is idle.

            The default is five seconds.

            Example: ``eventsPollInterval=5;``

            In the example, AWS DMS checks for changes in the binary logs every five seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-eventspollinterval
            '''
            result = self._values.get("events_poll_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

            Example: ``maxFileSize=512``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallel_load_threads(self) -> typing.Optional[jsii.Number]:
            '''Improves performance when loading data into the MySQL-compatible target database.

            Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

            Example: ``parallelLoadThreads=1``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-parallelloadthreads
            '''
            result = self._values.get("parallel_load_threads")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''Endpoint connection password.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port used by the endpoint database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret.`` The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint.

            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''The MySQL host name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_timezone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone for the source MySQL database. Don't enclose time zones in single quotation marks.

            Example: ``serverTimezone=US/Pacific;``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-servertimezone
            '''
            result = self._values.get("server_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''Endpoint connection user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-gcpmysqlsettings.html#cfn-dms-endpoint-gcpmysqlsettings-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GcpMySQLSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.IbmDb2SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "current_lsn": "currentLsn",
            "keep_csv_files": "keepCsvFiles",
            "load_timeout": "loadTimeout",
            "max_file_size": "maxFileSize",
            "max_k_bytes_per_read": "maxKBytesPerRead",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "set_data_capture_changes": "setDataCaptureChanges",
            "write_buffer_size": "writeBufferSize",
        },
    )
    class IbmDb2SettingsProperty:
        def __init__(
            self,
            *,
            current_lsn: typing.Optional[builtins.str] = None,
            keep_csv_files: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            load_timeout: typing.Optional[jsii.Number] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            max_k_bytes_per_read: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            set_data_capture_changes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            write_buffer_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Provides information that defines an IBMDB2 endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param current_lsn: For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.
            :param keep_csv_files: If true, AWS DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting. The default value is false.
            :param load_timeout: The amount of time (in milliseconds) before AWS DMS times out operations performed by DMS on the Db2 target. The default value is 1200 (20 minutes).
            :param max_file_size: Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.
            :param max_k_bytes_per_read: Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value ofthe AWS Secrets Manager secret that allows access to the Db2 LUW endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the IBMDB2 endpoint connection details.
            :param set_data_capture_changes: Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.
            :param write_buffer_size: The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                ibm_db2_settings_property = dms.CfnEndpoint.IbmDb2SettingsProperty(
                    current_lsn="currentLsn",
                    keep_csv_files=False,
                    load_timeout=123,
                    max_file_size=123,
                    max_kBytes_per_read=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    set_data_capture_changes=False,
                    write_buffer_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1d6fbc1cf195619dd4c4ec936108c9aa18b32dd75831ce4e5f419f51f377abef)
                check_type(argname="argument current_lsn", value=current_lsn, expected_type=type_hints["current_lsn"])
                check_type(argname="argument keep_csv_files", value=keep_csv_files, expected_type=type_hints["keep_csv_files"])
                check_type(argname="argument load_timeout", value=load_timeout, expected_type=type_hints["load_timeout"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument max_k_bytes_per_read", value=max_k_bytes_per_read, expected_type=type_hints["max_k_bytes_per_read"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument set_data_capture_changes", value=set_data_capture_changes, expected_type=type_hints["set_data_capture_changes"])
                check_type(argname="argument write_buffer_size", value=write_buffer_size, expected_type=type_hints["write_buffer_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if current_lsn is not None:
                self._values["current_lsn"] = current_lsn
            if keep_csv_files is not None:
                self._values["keep_csv_files"] = keep_csv_files
            if load_timeout is not None:
                self._values["load_timeout"] = load_timeout
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if max_k_bytes_per_read is not None:
                self._values["max_k_bytes_per_read"] = max_k_bytes_per_read
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if set_data_capture_changes is not None:
                self._values["set_data_capture_changes"] = set_data_capture_changes
            if write_buffer_size is not None:
                self._values["write_buffer_size"] = write_buffer_size

        @builtins.property
        def current_lsn(self) -> typing.Optional[builtins.str]:
            '''For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-currentlsn
            '''
            result = self._values.get("current_lsn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def keep_csv_files(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If true, AWS DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting.

            The default value is false.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-keepcsvfiles
            '''
            result = self._values.get("keep_csv_files")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def load_timeout(self) -> typing.Optional[jsii.Number]:
            '''The amount of time (in milliseconds) before AWS DMS times out operations performed by DMS on the Db2 target.

            The default value is 1200 (20 minutes).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-loadtimeout
            '''
            result = self._values.get("load_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_k_bytes_per_read(self) -> typing.Optional[jsii.Number]:
            '''Maximum number of bytes per read, as a NUMBER value.

            The default is 64 KB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-maxkbytesperread
            '''
            result = self._values.get("max_k_bytes_per_read")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value ofthe AWS Secrets Manager secret that allows access to the Db2 LUW endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the IBMDB2 endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def set_data_capture_changes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Enables ongoing replication (CDC) as a BOOLEAN value.

            The default is true.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-setdatacapturechanges
            '''
            result = self._values.get("set_data_capture_changes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def write_buffer_size(self) -> typing.Optional[jsii.Number]:
            '''The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-ibmdb2settings.html#cfn-dms-endpoint-ibmdb2settings-writebuffersize
            '''
            result = self._values.get("write_buffer_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IbmDb2SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.KafkaSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "broker": "broker",
            "include_control_details": "includeControlDetails",
            "include_null_and_empty": "includeNullAndEmpty",
            "include_partition_value": "includePartitionValue",
            "include_table_alter_operations": "includeTableAlterOperations",
            "include_transaction_details": "includeTransactionDetails",
            "message_format": "messageFormat",
            "message_max_bytes": "messageMaxBytes",
            "no_hex_prefix": "noHexPrefix",
            "partition_include_schema_table": "partitionIncludeSchemaTable",
            "sasl_password": "saslPassword",
            "sasl_user_name": "saslUserName",
            "security_protocol": "securityProtocol",
            "ssl_ca_certificate_arn": "sslCaCertificateArn",
            "ssl_client_certificate_arn": "sslClientCertificateArn",
            "ssl_client_key_arn": "sslClientKeyArn",
            "ssl_client_key_password": "sslClientKeyPassword",
            "topic": "topic",
        },
    )
    class KafkaSettingsProperty:
        def __init__(
            self,
            *,
            broker: typing.Optional[builtins.str] = None,
            include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            message_format: typing.Optional[builtins.str] = None,
            message_max_bytes: typing.Optional[jsii.Number] = None,
            no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            sasl_password: typing.Optional[builtins.str] = None,
            sasl_user_name: typing.Optional[builtins.str] = None,
            security_protocol: typing.Optional[builtins.str] = None,
            ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
            ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
            ssl_client_key_arn: typing.Optional[builtins.str] = None,
            ssl_client_key_password: typing.Optional[builtins.str] = None,
            topic: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that describes an Apache Kafka endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

            :param broker: A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance. Specify each broker location in the form ``*broker-hostname-or-ip* : *port*`` . For example, ``"ec2-12-345-678-901.compute-1.amazonaws.com:2345"`` . For more information and examples of specifying a list of broker locations, see `Using Apache Kafka as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html>`_ in the *AWS Database Migration Service User Guide* .
            :param include_control_details: Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output. The default is ``false`` .
            :param include_null_and_empty: Include NULL and empty columns for records migrated to the endpoint. The default is ``false`` .
            :param include_partition_value: Shows the partition value within the Kafka message output unless the partition type is ``schema-table-type`` . The default is ``false`` .
            :param include_table_alter_operations: Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` . The default is ``false`` .
            :param include_transaction_details: Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .
            :param message_format: The output format for the records created on the endpoint. The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).
            :param message_max_bytes: The maximum size in bytes for records created on the endpoint The default is 1,000,000.
            :param no_hex_prefix: Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.
            :param partition_include_schema_table: Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` . Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is ``false`` .
            :param sasl_password: The secure password that you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.
            :param sasl_user_name: The secure user name you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.
            :param security_protocol: Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS). Options include ``ssl-encryption`` , ``ssl-authentication`` , and ``sasl-ssl`` . ``sasl-ssl`` requires ``SaslUsername`` and ``SaslPassword`` .
            :param ssl_ca_certificate_arn: The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that AWS DMS uses to securely connect to your Kafka target endpoint.
            :param ssl_client_certificate_arn: The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.
            :param ssl_client_key_arn: The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.
            :param ssl_client_key_password: The password for the client private key used to securely connect to a Kafka target endpoint.
            :param topic: The topic to which you migrate the data. If you don't specify a topic, AWS DMS specifies ``"kafka-default-topic"`` as the migration topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                kafka_settings_property = dms.CfnEndpoint.KafkaSettingsProperty(
                    broker="broker",
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    message_max_bytes=123,
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    sasl_password="saslPassword",
                    sasl_user_name="saslUserName",
                    security_protocol="securityProtocol",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_client_certificate_arn="sslClientCertificateArn",
                    ssl_client_key_arn="sslClientKeyArn",
                    ssl_client_key_password="sslClientKeyPassword",
                    topic="topic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ef2e1b1010b2e04e20a0f1bedb9c97d4fea3afa8fb07e8b223e6dec6cd661d7)
                check_type(argname="argument broker", value=broker, expected_type=type_hints["broker"])
                check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
                check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
                check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
                check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
                check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
                check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
                check_type(argname="argument message_max_bytes", value=message_max_bytes, expected_type=type_hints["message_max_bytes"])
                check_type(argname="argument no_hex_prefix", value=no_hex_prefix, expected_type=type_hints["no_hex_prefix"])
                check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
                check_type(argname="argument sasl_password", value=sasl_password, expected_type=type_hints["sasl_password"])
                check_type(argname="argument sasl_user_name", value=sasl_user_name, expected_type=type_hints["sasl_user_name"])
                check_type(argname="argument security_protocol", value=security_protocol, expected_type=type_hints["security_protocol"])
                check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
                check_type(argname="argument ssl_client_certificate_arn", value=ssl_client_certificate_arn, expected_type=type_hints["ssl_client_certificate_arn"])
                check_type(argname="argument ssl_client_key_arn", value=ssl_client_key_arn, expected_type=type_hints["ssl_client_key_arn"])
                check_type(argname="argument ssl_client_key_password", value=ssl_client_key_password, expected_type=type_hints["ssl_client_key_password"])
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if broker is not None:
                self._values["broker"] = broker
            if include_control_details is not None:
                self._values["include_control_details"] = include_control_details
            if include_null_and_empty is not None:
                self._values["include_null_and_empty"] = include_null_and_empty
            if include_partition_value is not None:
                self._values["include_partition_value"] = include_partition_value
            if include_table_alter_operations is not None:
                self._values["include_table_alter_operations"] = include_table_alter_operations
            if include_transaction_details is not None:
                self._values["include_transaction_details"] = include_transaction_details
            if message_format is not None:
                self._values["message_format"] = message_format
            if message_max_bytes is not None:
                self._values["message_max_bytes"] = message_max_bytes
            if no_hex_prefix is not None:
                self._values["no_hex_prefix"] = no_hex_prefix
            if partition_include_schema_table is not None:
                self._values["partition_include_schema_table"] = partition_include_schema_table
            if sasl_password is not None:
                self._values["sasl_password"] = sasl_password
            if sasl_user_name is not None:
                self._values["sasl_user_name"] = sasl_user_name
            if security_protocol is not None:
                self._values["security_protocol"] = security_protocol
            if ssl_ca_certificate_arn is not None:
                self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
            if ssl_client_certificate_arn is not None:
                self._values["ssl_client_certificate_arn"] = ssl_client_certificate_arn
            if ssl_client_key_arn is not None:
                self._values["ssl_client_key_arn"] = ssl_client_key_arn
            if ssl_client_key_password is not None:
                self._values["ssl_client_key_password"] = ssl_client_key_password
            if topic is not None:
                self._values["topic"] = topic

        @builtins.property
        def broker(self) -> typing.Optional[builtins.str]:
            '''A comma-separated list of one or more broker locations in your Kafka cluster that host your Kafka instance.

            Specify each broker location in the form ``*broker-hostname-or-ip* : *port*`` . For example, ``"ec2-12-345-678-901.compute-1.amazonaws.com:2345"`` . For more information and examples of specifying a list of broker locations, see `Using Apache Kafka as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-broker
            '''
            result = self._values.get("broker")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_control_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Shows detailed control information for table definition, column definition, and table and column changes in the Kafka message output.

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includecontroldetails
            '''
            result = self._values.get("include_control_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_null_and_empty(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include NULL and empty columns for records migrated to the endpoint.

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includenullandempty
            '''
            result = self._values.get("include_null_and_empty")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_partition_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Shows the partition value within the Kafka message output unless the partition type is ``schema-table-type`` .

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includepartitionvalue
            '''
            result = self._values.get("include_partition_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_table_alter_operations(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` .

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includetablealteroperations
            '''
            result = self._values.get("include_table_alter_operations")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_transaction_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Provides detailed transaction information from the source database.

            This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-includetransactiondetails
            '''
            result = self._values.get("include_transaction_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def message_format(self) -> typing.Optional[builtins.str]:
            '''The output format for the records created on the endpoint.

            The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-messageformat
            '''
            result = self._values.get("message_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def message_max_bytes(self) -> typing.Optional[jsii.Number]:
            '''The maximum size in bytes for records created on the endpoint The default is 1,000,000.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-messagemaxbytes
            '''
            result = self._values.get("message_max_bytes")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def no_hex_prefix(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format.

            For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to a Kafka target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-nohexprefix
            '''
            result = self._values.get("no_hex_prefix")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def partition_include_schema_table(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` .

            Doing this increases data distribution among Kafka partitions. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same partition, which causes throttling. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-partitionincludeschematable
            '''
            result = self._values.get("partition_include_schema_table")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def sasl_password(self) -> typing.Optional[builtins.str]:
            '''The secure password that you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-saslpassword
            '''
            result = self._values.get("sasl_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sasl_user_name(self) -> typing.Optional[builtins.str]:
            '''The secure user name you created when you first set up your Amazon MSK cluster to validate a client identity and make an encrypted connection between server and client using SASL-SSL authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-saslusername
            '''
            result = self._values.get("sasl_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_protocol(self) -> typing.Optional[builtins.str]:
            '''Set secure connection to a Kafka target endpoint using Transport Layer Security (TLS).

            Options include ``ssl-encryption`` , ``ssl-authentication`` , and ``sasl-ssl`` . ``sasl-ssl`` requires ``SaslUsername`` and ``SaslPassword`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-securityprotocol
            '''
            result = self._values.get("security_protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the private certificate authority (CA) cert that AWS DMS uses to securely connect to your Kafka target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslcacertificatearn
            '''
            result = self._values.get("ssl_ca_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_client_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the client certificate used to securely connect to a Kafka target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientcertificatearn
            '''
            result = self._values.get("ssl_client_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_client_key_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the client private key used to securely connect to a Kafka target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientkeyarn
            '''
            result = self._values.get("ssl_client_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_client_key_password(self) -> typing.Optional[builtins.str]:
            '''The password for the client private key used to securely connect to a Kafka target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-sslclientkeypassword
            '''
            result = self._values.get("ssl_client_key_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic(self) -> typing.Optional[builtins.str]:
            '''The topic to which you migrate the data.

            If you don't specify a topic, AWS DMS specifies ``"kafka-default-topic"`` as the migration topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kafkasettings.html#cfn-dms-endpoint-kafkasettings-topic
            '''
            result = self._values.get("topic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KafkaSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.KinesisSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "include_control_details": "includeControlDetails",
            "include_null_and_empty": "includeNullAndEmpty",
            "include_partition_value": "includePartitionValue",
            "include_table_alter_operations": "includeTableAlterOperations",
            "include_transaction_details": "includeTransactionDetails",
            "message_format": "messageFormat",
            "no_hex_prefix": "noHexPrefix",
            "partition_include_schema_table": "partitionIncludeSchemaTable",
            "service_access_role_arn": "serviceAccessRoleArn",
            "stream_arn": "streamArn",
        },
    )
    class KinesisSettingsProperty:
        def __init__(
            self,
            *,
            include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            message_format: typing.Optional[builtins.str] = None,
            no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
            stream_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that describes an Amazon Kinesis Data Stream endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

            :param include_control_details: Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output. The default is ``false`` .
            :param include_null_and_empty: Include NULL and empty columns for records migrated to the endpoint. The default is ``false`` .
            :param include_partition_value: Shows the partition value within the Kinesis message output, unless the partition type is ``schema-table-type`` . The default is ``false`` .
            :param include_table_alter_operations: Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` . The default is ``false`` .
            :param include_transaction_details: Provides detailed transaction information from the source database. This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .
            :param message_format: The output format for the records created on the endpoint. The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).
            :param no_hex_prefix: Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format. For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.
            :param partition_include_schema_table: Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` . Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is ``false`` .
            :param service_access_role_arn: The Amazon Resource Name (ARN) for the IAM role that AWS DMS uses to write to the Kinesis data stream. The role must allow the ``iam:PassRole`` action.
            :param stream_arn: The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                kinesis_settings_property = dms.CfnEndpoint.KinesisSettingsProperty(
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    service_access_role_arn="serviceAccessRoleArn",
                    stream_arn="streamArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c5a51439b5e4a710a546672de30983c7b1b763f1ce8451c08fc99623fce9ed6d)
                check_type(argname="argument include_control_details", value=include_control_details, expected_type=type_hints["include_control_details"])
                check_type(argname="argument include_null_and_empty", value=include_null_and_empty, expected_type=type_hints["include_null_and_empty"])
                check_type(argname="argument include_partition_value", value=include_partition_value, expected_type=type_hints["include_partition_value"])
                check_type(argname="argument include_table_alter_operations", value=include_table_alter_operations, expected_type=type_hints["include_table_alter_operations"])
                check_type(argname="argument include_transaction_details", value=include_transaction_details, expected_type=type_hints["include_transaction_details"])
                check_type(argname="argument message_format", value=message_format, expected_type=type_hints["message_format"])
                check_type(argname="argument no_hex_prefix", value=no_hex_prefix, expected_type=type_hints["no_hex_prefix"])
                check_type(argname="argument partition_include_schema_table", value=partition_include_schema_table, expected_type=type_hints["partition_include_schema_table"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
                check_type(argname="argument stream_arn", value=stream_arn, expected_type=type_hints["stream_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if include_control_details is not None:
                self._values["include_control_details"] = include_control_details
            if include_null_and_empty is not None:
                self._values["include_null_and_empty"] = include_null_and_empty
            if include_partition_value is not None:
                self._values["include_partition_value"] = include_partition_value
            if include_table_alter_operations is not None:
                self._values["include_table_alter_operations"] = include_table_alter_operations
            if include_transaction_details is not None:
                self._values["include_transaction_details"] = include_transaction_details
            if message_format is not None:
                self._values["message_format"] = message_format
            if no_hex_prefix is not None:
                self._values["no_hex_prefix"] = no_hex_prefix
            if partition_include_schema_table is not None:
                self._values["partition_include_schema_table"] = partition_include_schema_table
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn
            if stream_arn is not None:
                self._values["stream_arn"] = stream_arn

        @builtins.property
        def include_control_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Shows detailed control information for table definition, column definition, and table and column changes in the Kinesis message output.

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includecontroldetails
            '''
            result = self._values.get("include_control_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_null_and_empty(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Include NULL and empty columns for records migrated to the endpoint.

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includenullandempty
            '''
            result = self._values.get("include_null_and_empty")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_partition_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Shows the partition value within the Kinesis message output, unless the partition type is ``schema-table-type`` .

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includepartitionvalue
            '''
            result = self._values.get("include_partition_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_table_alter_operations(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Includes any data definition language (DDL) operations that change the table in the control data, such as ``rename-table`` , ``drop-table`` , ``add-column`` , ``drop-column`` , and ``rename-column`` .

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includetablealteroperations
            '''
            result = self._values.get("include_table_alter_operations")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_transaction_details(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Provides detailed transaction information from the source database.

            This information includes a commit timestamp, a log position, and values for ``transaction_id`` , previous ``transaction_id`` , and ``transaction_record_id`` (the record offset within a transaction). The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-includetransactiondetails
            '''
            result = self._values.get("include_transaction_details")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def message_format(self) -> typing.Optional[builtins.str]:
            '''The output format for the records created on the endpoint.

            The message format is ``JSON`` (default) or ``JSON_UNFORMATTED`` (a single line with no tab).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-messageformat
            '''
            result = self._values.get("message_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def no_hex_prefix(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this optional parameter to ``true`` to avoid adding a '0x' prefix to raw data in hexadecimal format.

            For example, by default, AWS DMS adds a '0x' prefix to the LOB column type in hexadecimal format moving from an Oracle source to an Amazon Kinesis target. Use the ``NoHexPrefix`` endpoint setting to enable migration of RAW data type columns without adding the '0x' prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-nohexprefix
            '''
            result = self._values.get("no_hex_prefix")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def partition_include_schema_table(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Prefixes schema and table names to partition values, when the partition type is ``primary-key-type`` .

            Doing this increases data distribution among Kinesis shards. For example, suppose that a SysBench schema has thousands of tables and each table has only limited range for a primary key. In this case, the same primary key is sent from thousands of tables to the same shard, which causes throttling. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-partitionincludeschematable
            '''
            result = self._values.get("partition_include_schema_table")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the IAM role that AWS DMS uses to write to the Kinesis data stream.

            The role must allow the ``iam:PassRole`` action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stream_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Amazon Kinesis Data Streams endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-kinesissettings.html#cfn-dms-endpoint-kinesissettings-streamarn
            '''
            result = self._values.get("stream_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bcp_packet_size": "bcpPacketSize",
            "control_tables_file_group": "controlTablesFileGroup",
            "database_name": "databaseName",
            "force_lob_lookup": "forceLobLookup",
            "password": "password",
            "port": "port",
            "query_single_always_on_node": "querySingleAlwaysOnNode",
            "read_backup_only": "readBackupOnly",
            "safeguard_policy": "safeguardPolicy",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_name": "serverName",
            "tlog_access_mode": "tlogAccessMode",
            "trim_space_in_char": "trimSpaceInChar",
            "use_bcp_full_load": "useBcpFullLoad",
            "username": "username",
            "use_third_party_backup_device": "useThirdPartyBackupDevice",
        },
    )
    class MicrosoftSqlServerSettingsProperty:
        def __init__(
            self,
            *,
            bcp_packet_size: typing.Optional[jsii.Number] = None,
            control_tables_file_group: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            force_lob_lookup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            password: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            query_single_always_on_node: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            read_backup_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            safeguard_policy: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_name: typing.Optional[builtins.str] = None,
            tlog_access_mode: typing.Optional[builtins.str] = None,
            trim_space_in_char: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_bcp_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            username: typing.Optional[builtins.str] = None,
            use_third_party_backup_device: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides information that defines a Microsoft SQL Server endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param bcp_packet_size: The maximum size of the packets (in bytes) used to transfer data using BCP.
            :param control_tables_file_group: Specifies a file group for the AWS DMS internal tables. When the replication task starts, all the internal AWS DMS control tables (awsdms_ apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.
            :param database_name: Database name for the endpoint.
            :param force_lob_lookup: Forces LOB lookup on inline LOB.
            :param password: Endpoint connection password.
            :param port: Endpoint TCP port.
            :param query_single_always_on_node: Cleans and recreates table metadata information on the replication instance when a mismatch occurs. An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.
            :param read_backup_only: When this attribute is set to ``Y`` , AWS DMS only reads changes from transaction log backups and doesn't read from the active transaction log file during ongoing replication. Setting this parameter to ``Y`` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.
            :param safeguard_policy: Use this attribute to minimize the need to access the backup log and enable AWS DMS to prevent truncation using one of the following two methods. *Start transactions in the database:* This is the default method. When this method is used, AWS DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started aren't truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method. *Exclusively use sp_repldone within a single task* : When this method is used, AWS DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesn't involve any transactional activities, it can only be used when Microsoft Replication isn't running. Also, when using this method, only one AWS DMS task can access the database at any given time. Therefore, if you need to run parallel AWS DMS tasks against the same database, use the default method.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SQL Server endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MicrosoftSQLServer endpoint connection details.
            :param server_name: Fully qualified domain name of the endpoint. For an Amazon RDS SQL Server instance, this is the output of `DescribeDBInstances <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html>`_ , in the ``[Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.
            :param tlog_access_mode: Indicates the mode used to fetch CDC data.
            :param trim_space_in_char: Use the ``TrimSpaceInChar`` source endpoint setting to right-trim data on CHAR and NCHAR data types during migration. Setting ``TrimSpaceInChar`` does not left-trim data. The default value is ``true`` .
            :param use_bcp_full_load: Use this to attribute to transfer data for full-load operations using BCP. When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.
            :param username: Endpoint connection user name.
            :param use_third_party_backup_device: When this attribute is set to ``Y`` , DMS processes third-party transaction log backups if they are created in native format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                microsoft_sql_server_settings_property = dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty(
                    bcp_packet_size=123,
                    control_tables_file_group="controlTablesFileGroup",
                    database_name="databaseName",
                    force_lob_lookup=False,
                    password="password",
                    port=123,
                    query_single_always_on_node=False,
                    read_backup_only=False,
                    safeguard_policy="safeguardPolicy",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    tlog_access_mode="tlogAccessMode",
                    trim_space_in_char=False,
                    use_bcp_full_load=False,
                    username="username",
                    use_third_party_backup_device=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__200804814bec4b3dcdc4d865d66320326f539657f293b56ba530cb6a08841175)
                check_type(argname="argument bcp_packet_size", value=bcp_packet_size, expected_type=type_hints["bcp_packet_size"])
                check_type(argname="argument control_tables_file_group", value=control_tables_file_group, expected_type=type_hints["control_tables_file_group"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument force_lob_lookup", value=force_lob_lookup, expected_type=type_hints["force_lob_lookup"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument query_single_always_on_node", value=query_single_always_on_node, expected_type=type_hints["query_single_always_on_node"])
                check_type(argname="argument read_backup_only", value=read_backup_only, expected_type=type_hints["read_backup_only"])
                check_type(argname="argument safeguard_policy", value=safeguard_policy, expected_type=type_hints["safeguard_policy"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument tlog_access_mode", value=tlog_access_mode, expected_type=type_hints["tlog_access_mode"])
                check_type(argname="argument trim_space_in_char", value=trim_space_in_char, expected_type=type_hints["trim_space_in_char"])
                check_type(argname="argument use_bcp_full_load", value=use_bcp_full_load, expected_type=type_hints["use_bcp_full_load"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
                check_type(argname="argument use_third_party_backup_device", value=use_third_party_backup_device, expected_type=type_hints["use_third_party_backup_device"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bcp_packet_size is not None:
                self._values["bcp_packet_size"] = bcp_packet_size
            if control_tables_file_group is not None:
                self._values["control_tables_file_group"] = control_tables_file_group
            if database_name is not None:
                self._values["database_name"] = database_name
            if force_lob_lookup is not None:
                self._values["force_lob_lookup"] = force_lob_lookup
            if password is not None:
                self._values["password"] = password
            if port is not None:
                self._values["port"] = port
            if query_single_always_on_node is not None:
                self._values["query_single_always_on_node"] = query_single_always_on_node
            if read_backup_only is not None:
                self._values["read_backup_only"] = read_backup_only
            if safeguard_policy is not None:
                self._values["safeguard_policy"] = safeguard_policy
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_name is not None:
                self._values["server_name"] = server_name
            if tlog_access_mode is not None:
                self._values["tlog_access_mode"] = tlog_access_mode
            if trim_space_in_char is not None:
                self._values["trim_space_in_char"] = trim_space_in_char
            if use_bcp_full_load is not None:
                self._values["use_bcp_full_load"] = use_bcp_full_load
            if username is not None:
                self._values["username"] = username
            if use_third_party_backup_device is not None:
                self._values["use_third_party_backup_device"] = use_third_party_backup_device

        @builtins.property
        def bcp_packet_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size of the packets (in bytes) used to transfer data using BCP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-bcppacketsize
            '''
            result = self._values.get("bcp_packet_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def control_tables_file_group(self) -> typing.Optional[builtins.str]:
            '''Specifies a file group for the AWS DMS internal tables.

            When the replication task starts, all the internal AWS DMS control tables (awsdms_ apply_exception, awsdms_apply, awsdms_changes) are created for the specified file group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-controltablesfilegroup
            '''
            result = self._values.get("control_tables_file_group")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''Database name for the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def force_lob_lookup(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Forces LOB lookup on inline LOB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-forceloblookup
            '''
            result = self._values.get("force_lob_lookup")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''Endpoint connection password.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''Endpoint TCP port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def query_single_always_on_node(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Cleans and recreates table metadata information on the replication instance when a mismatch occurs.

            An example is a situation where running an alter DDL statement on a table might result in different information about the table cached in the replication instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-querysinglealwaysonnode
            '''
            result = self._values.get("query_single_always_on_node")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def read_backup_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this attribute is set to ``Y`` , AWS DMS only reads changes from transaction log backups and doesn't read from the active transaction log file during ongoing replication.

            Setting this parameter to ``Y`` enables you to control active transaction log file growth during full load and ongoing replication tasks. However, it can add some source latency to ongoing replication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-readbackuponly
            '''
            result = self._values.get("read_backup_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def safeguard_policy(self) -> typing.Optional[builtins.str]:
            '''Use this attribute to minimize the need to access the backup log and enable AWS DMS to prevent truncation using one of the following two methods.

            *Start transactions in the database:* This is the default method. When this method is used, AWS DMS prevents TLOG truncation by mimicking a transaction in the database. As long as such a transaction is open, changes that appear after the transaction started aren't truncated. If you need Microsoft Replication to be enabled in your database, then you must choose this method.

            *Exclusively use sp_repldone within a single task* : When this method is used, AWS DMS reads the changes and then uses sp_repldone to mark the TLOG transactions as ready for truncation. Although this method doesn't involve any transactional activities, it can only be used when Microsoft Replication isn't running. Also, when using this method, only one AWS DMS task can access the database at any given time. Therefore, if you need to run parallel AWS DMS tasks against the same database, use the default method.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-safeguardpolicy
            '''
            result = self._values.get("safeguard_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SQL Server endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MicrosoftSQLServer endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''Fully qualified domain name of the endpoint.

            For an Amazon RDS SQL Server instance, this is the output of `DescribeDBInstances <https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_DescribeDBInstances.html>`_ , in the ``[Endpoint](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_Endpoint.html) .Address`` field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tlog_access_mode(self) -> typing.Optional[builtins.str]:
            '''Indicates the mode used to fetch CDC data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-tlogaccessmode
            '''
            result = self._values.get("tlog_access_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def trim_space_in_char(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use the ``TrimSpaceInChar`` source endpoint setting to right-trim data on CHAR and NCHAR data types during migration.

            Setting ``TrimSpaceInChar`` does not left-trim data. The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-trimspaceinchar
            '''
            result = self._values.get("trim_space_in_char")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_bcp_full_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use this to attribute to transfer data for full-load operations using BCP.

            When the target table contains an identity column that does not exist in the source table, you must disable the use BCP for loading table option.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-usebcpfullload
            '''
            result = self._values.get("use_bcp_full_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''Endpoint connection user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_third_party_backup_device(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this attribute is set to ``Y`` , DMS processes third-party transaction log backups if they are created in native format.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-microsoftsqlserversettings.html#cfn-dms-endpoint-microsoftsqlserversettings-usethirdpartybackupdevice
            '''
            result = self._values.get("use_third_party_backup_device")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MicrosoftSqlServerSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.MongoDbSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_mechanism": "authMechanism",
            "auth_source": "authSource",
            "auth_type": "authType",
            "database_name": "databaseName",
            "docs_to_investigate": "docsToInvestigate",
            "extract_doc_id": "extractDocId",
            "nesting_level": "nestingLevel",
            "password": "password",
            "port": "port",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_name": "serverName",
            "username": "username",
        },
    )
    class MongoDbSettingsProperty:
        def __init__(
            self,
            *,
            auth_mechanism: typing.Optional[builtins.str] = None,
            auth_source: typing.Optional[builtins.str] = None,
            auth_type: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            docs_to_investigate: typing.Optional[builtins.str] = None,
            extract_doc_id: typing.Optional[builtins.str] = None,
            nesting_level: typing.Optional[builtins.str] = None,
            password: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_name: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a MongoDB endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Endpoint configuration settings when using MongoDB as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .

            :param auth_mechanism: The authentication mechanism you use to access the MongoDB source endpoint. For the default value, in MongoDB version 2.x, ``"default"`` is ``"mongodb_cr"`` . For MongoDB version 3.x or later, ``"default"`` is ``"scram_sha_1"`` . This setting isn't used when ``AuthType`` is set to ``"no"`` .
            :param auth_source: The MongoDB database name. This setting isn't used when ``AuthType`` is set to ``"no"`` . The default is ``"admin"`` .
            :param auth_type: The authentication type you use to access the MongoDB source endpoint. When set to ``"no"`` , user name and password parameters are not used and can be empty.
            :param database_name: The database name on the MongoDB source endpoint.
            :param docs_to_investigate: Indicates the number of documents to preview to determine the document organization. Use this setting when ``NestingLevel`` is set to ``"one"`` . Must be a positive value greater than ``0`` . Default value is ``1000`` .
            :param extract_doc_id: Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` . Default value is ``"false"`` .
            :param nesting_level: Specifies either document or table mode. Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.
            :param password: The password for the user account you use to access the MongoDB source endpoint.
            :param port: The port value for the MongoDB source endpoint.
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MongoDB endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MongoDB endpoint connection details.
            :param server_name: The name of the server on the MongoDB source endpoint.
            :param username: The user name you use to access the MongoDB source endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                mongo_db_settings_property = dms.CfnEndpoint.MongoDbSettingsProperty(
                    auth_mechanism="authMechanism",
                    auth_source="authSource",
                    auth_type="authType",
                    database_name="databaseName",
                    docs_to_investigate="docsToInvestigate",
                    extract_doc_id="extractDocId",
                    nesting_level="nestingLevel",
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f47aa57b2c4073da641cad41ba07cbd9f41d4616eed682a61b712170dcda03e0)
                check_type(argname="argument auth_mechanism", value=auth_mechanism, expected_type=type_hints["auth_mechanism"])
                check_type(argname="argument auth_source", value=auth_source, expected_type=type_hints["auth_source"])
                check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument docs_to_investigate", value=docs_to_investigate, expected_type=type_hints["docs_to_investigate"])
                check_type(argname="argument extract_doc_id", value=extract_doc_id, expected_type=type_hints["extract_doc_id"])
                check_type(argname="argument nesting_level", value=nesting_level, expected_type=type_hints["nesting_level"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_mechanism is not None:
                self._values["auth_mechanism"] = auth_mechanism
            if auth_source is not None:
                self._values["auth_source"] = auth_source
            if auth_type is not None:
                self._values["auth_type"] = auth_type
            if database_name is not None:
                self._values["database_name"] = database_name
            if docs_to_investigate is not None:
                self._values["docs_to_investigate"] = docs_to_investigate
            if extract_doc_id is not None:
                self._values["extract_doc_id"] = extract_doc_id
            if nesting_level is not None:
                self._values["nesting_level"] = nesting_level
            if password is not None:
                self._values["password"] = password
            if port is not None:
                self._values["port"] = port
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_name is not None:
                self._values["server_name"] = server_name
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def auth_mechanism(self) -> typing.Optional[builtins.str]:
            '''The authentication mechanism you use to access the MongoDB source endpoint.

            For the default value, in MongoDB version 2.x, ``"default"`` is ``"mongodb_cr"`` . For MongoDB version 3.x or later, ``"default"`` is ``"scram_sha_1"`` . This setting isn't used when ``AuthType`` is set to ``"no"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authmechanism
            '''
            result = self._values.get("auth_mechanism")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_source(self) -> typing.Optional[builtins.str]:
            '''The MongoDB database name. This setting isn't used when ``AuthType`` is set to ``"no"`` .

            The default is ``"admin"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authsource
            '''
            result = self._values.get("auth_source")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_type(self) -> typing.Optional[builtins.str]:
            '''The authentication type you use to access the MongoDB source endpoint.

            When set to ``"no"`` , user name and password parameters are not used and can be empty.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-authtype
            '''
            result = self._values.get("auth_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The database name on the MongoDB source endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def docs_to_investigate(self) -> typing.Optional[builtins.str]:
            '''Indicates the number of documents to preview to determine the document organization.

            Use this setting when ``NestingLevel`` is set to ``"one"`` .

            Must be a positive value greater than ``0`` . Default value is ``1000`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-docstoinvestigate
            '''
            result = self._values.get("docs_to_investigate")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def extract_doc_id(self) -> typing.Optional[builtins.str]:
            '''Specifies the document ID. Use this setting when ``NestingLevel`` is set to ``"none"`` .

            Default value is ``"false"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-extractdocid
            '''
            result = self._values.get("extract_doc_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def nesting_level(self) -> typing.Optional[builtins.str]:
            '''Specifies either document or table mode.

            Default value is ``"none"`` . Specify ``"none"`` to use document mode. Specify ``"one"`` to use table mode.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-nestinglevel
            '''
            result = self._values.get("nesting_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password for the user account you use to access the MongoDB source endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port value for the MongoDB source endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MongoDB endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MongoDB endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''The name of the server on the MongoDB source endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The user name you use to access the MongoDB source endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mongodbsettings.html#cfn-dms-endpoint-mongodbsettings-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MongoDbSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.MySqlSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_connect_script": "afterConnectScript",
            "clean_source_metadata_on_mismatch": "cleanSourceMetadataOnMismatch",
            "events_poll_interval": "eventsPollInterval",
            "max_file_size": "maxFileSize",
            "parallel_load_threads": "parallelLoadThreads",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_timezone": "serverTimezone",
            "target_db_type": "targetDbType",
        },
    )
    class MySqlSettingsProperty:
        def __init__(
            self,
            *,
            after_connect_script: typing.Optional[builtins.str] = None,
            clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            events_poll_interval: typing.Optional[jsii.Number] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            parallel_load_threads: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_timezone: typing.Optional[builtins.str] = None,
            target_db_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a MySQL endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param after_connect_script: Specifies a script to run immediately after AWS DMS connects to the endpoint. The migration task continues running regardless if the SQL statement succeeds or fails. For this parameter, provide the code of the script itself, not the name of a file containing the script.
            :param clean_source_metadata_on_mismatch: Cleans and recreates table metadata information on the replication instance when a mismatch occurs. For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.
            :param events_poll_interval: Specifies how often to check the binary log for new changes/events when the database is idle. The default is five seconds. Example: ``eventsPollInterval=5;`` In the example, AWS DMS checks for changes in the binary logs every five seconds.
            :param max_file_size: Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database. Example: ``maxFileSize=512``
            :param parallel_load_threads: Improves performance when loading data into the MySQL-compatible target database. Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one. Example: ``parallelLoadThreads=1``
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.
            :param server_timezone: Specifies the time zone for the source MySQL database. Example: ``serverTimezone=US/Pacific;`` Note: Do not enclose time zones in single quotes.
            :param target_db_type: Specifies where to migrate source tables on the target, either to a single database or multiple databases. If you specify ``SPECIFIC_DATABASE`` , specify the database name using the ``DatabaseName`` parameter of the ``Endpoint`` object. Example: ``targetDbType=MULTIPLE_DATABASES``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                my_sql_settings_property = dms.CfnEndpoint.MySqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_timezone="serverTimezone",
                    target_db_type="targetDbType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e498a760044089b042c26e470ecb6641a0808cbad39ca3138efe525c32fd7b4f)
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument clean_source_metadata_on_mismatch", value=clean_source_metadata_on_mismatch, expected_type=type_hints["clean_source_metadata_on_mismatch"])
                check_type(argname="argument events_poll_interval", value=events_poll_interval, expected_type=type_hints["events_poll_interval"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument parallel_load_threads", value=parallel_load_threads, expected_type=type_hints["parallel_load_threads"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_timezone", value=server_timezone, expected_type=type_hints["server_timezone"])
                check_type(argname="argument target_db_type", value=target_db_type, expected_type=type_hints["target_db_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if clean_source_metadata_on_mismatch is not None:
                self._values["clean_source_metadata_on_mismatch"] = clean_source_metadata_on_mismatch
            if events_poll_interval is not None:
                self._values["events_poll_interval"] = events_poll_interval
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if parallel_load_threads is not None:
                self._values["parallel_load_threads"] = parallel_load_threads
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_timezone is not None:
                self._values["server_timezone"] = server_timezone
            if target_db_type is not None:
                self._values["target_db_type"] = target_db_type

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''Specifies a script to run immediately after AWS DMS connects to the endpoint.

            The migration task continues running regardless if the SQL statement succeeds or fails.

            For this parameter, provide the code of the script itself, not the name of a file containing the script.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def clean_source_metadata_on_mismatch(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Cleans and recreates table metadata information on the replication instance when a mismatch occurs.

            For example, in a situation where running an alter DDL on the table could result in different information about the table cached in the replication instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-cleansourcemetadataonmismatch
            '''
            result = self._values.get("clean_source_metadata_on_mismatch")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def events_poll_interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies how often to check the binary log for new changes/events when the database is idle.

            The default is five seconds.

            Example: ``eventsPollInterval=5;``

            In the example, AWS DMS checks for changes in the binary logs every five seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-eventspollinterval
            '''
            result = self._values.get("events_poll_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of any .csv file used to transfer data to a MySQL-compatible database.

            Example: ``maxFileSize=512``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallel_load_threads(self) -> typing.Optional[jsii.Number]:
            '''Improves performance when loading data into the MySQL-compatible target database.

            Specifies how many threads to use to load the data into the MySQL-compatible target database. Setting a large number of threads can have an adverse effect on database performance, because a separate connection is required for each thread. The default is one.

            Example: ``parallelLoadThreads=1``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-parallelloadthreads
            '''
            result = self._values.get("parallel_load_threads")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the MySQL endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the MySQL endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_timezone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone for the source MySQL database.

            Example: ``serverTimezone=US/Pacific;``

            Note: Do not enclose time zones in single quotes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-servertimezone
            '''
            result = self._values.get("server_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_db_type(self) -> typing.Optional[builtins.str]:
            '''Specifies where to migrate source tables on the target, either to a single database or multiple databases.

            If you specify ``SPECIFIC_DATABASE`` , specify the database name using the ``DatabaseName`` parameter of the ``Endpoint`` object.

            Example: ``targetDbType=MULTIPLE_DATABASES``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-mysqlsettings.html#cfn-dms-endpoint-mysqlsettings-targetdbtype
            '''
            result = self._values.get("target_db_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MySqlSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.NeptuneSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "error_retry_duration": "errorRetryDuration",
            "iam_auth_enabled": "iamAuthEnabled",
            "max_file_size": "maxFileSize",
            "max_retry_count": "maxRetryCount",
            "s3_bucket_folder": "s3BucketFolder",
            "s3_bucket_name": "s3BucketName",
            "service_access_role_arn": "serviceAccessRoleArn",
        },
    )
    class NeptuneSettingsProperty:
        def __init__(
            self,
            *,
            error_retry_duration: typing.Optional[jsii.Number] = None,
            iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            max_retry_count: typing.Optional[jsii.Number] = None,
            s3_bucket_folder: typing.Optional[builtins.str] = None,
            s3_bucket_name: typing.Optional[builtins.str] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines an Amazon Neptune endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

            :param error_retry_duration: The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error. The default is 250.
            :param iam_auth_enabled: If you want IAM authorization enabled for this endpoint, set this parameter to ``true`` . Then attach the appropriate IAM policy document to your service role specified by ``ServiceAccessRoleArn`` . The default is ``false`` .
            :param max_file_size: The maximum size in kilobytes of migrated graph data stored in a .csv file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.
            :param max_retry_count: The number of times for AWS DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error. The default is 5.
            :param s3_bucket_folder: A folder path where you want AWS DMS to store migrated graph data in the S3 bucket specified by ``S3BucketName``.
            :param s3_bucket_name: The name of the Amazon S3 bucket where AWS DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these .csv files.
            :param service_access_role_arn: The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint. The role must allow the ``iam:PassRole`` action. For more information, see `Creating an IAM Service Role for Accessing Amazon Neptune as a Target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                neptune_settings_property = dms.CfnEndpoint.NeptuneSettingsProperty(
                    error_retry_duration=123,
                    iam_auth_enabled=False,
                    max_file_size=123,
                    max_retry_count=123,
                    s3_bucket_folder="s3BucketFolder",
                    s3_bucket_name="s3BucketName",
                    service_access_role_arn="serviceAccessRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__18643502ff334362a3e0ace1eca2f5044f5a5e4bae5404b7919a779dd4b9da96)
                check_type(argname="argument error_retry_duration", value=error_retry_duration, expected_type=type_hints["error_retry_duration"])
                check_type(argname="argument iam_auth_enabled", value=iam_auth_enabled, expected_type=type_hints["iam_auth_enabled"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument max_retry_count", value=max_retry_count, expected_type=type_hints["max_retry_count"])
                check_type(argname="argument s3_bucket_folder", value=s3_bucket_folder, expected_type=type_hints["s3_bucket_folder"])
                check_type(argname="argument s3_bucket_name", value=s3_bucket_name, expected_type=type_hints["s3_bucket_name"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if error_retry_duration is not None:
                self._values["error_retry_duration"] = error_retry_duration
            if iam_auth_enabled is not None:
                self._values["iam_auth_enabled"] = iam_auth_enabled
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if max_retry_count is not None:
                self._values["max_retry_count"] = max_retry_count
            if s3_bucket_folder is not None:
                self._values["s3_bucket_folder"] = s3_bucket_folder
            if s3_bucket_name is not None:
                self._values["s3_bucket_name"] = s3_bucket_name
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn

        @builtins.property
        def error_retry_duration(self) -> typing.Optional[jsii.Number]:
            '''The number of milliseconds for AWS DMS to wait to retry a bulk-load of migrated graph data to the Neptune target database before raising an error.

            The default is 250.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-errorretryduration
            '''
            result = self._values.get("error_retry_duration")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def iam_auth_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If you want IAM authorization enabled for this endpoint, set this parameter to ``true`` .

            Then attach the appropriate IAM policy document to your service role specified by ``ServiceAccessRoleArn`` . The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-iamauthenabled
            '''
            result = self._values.get("iam_auth_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size in kilobytes of migrated graph data stored in a .csv file before AWS DMS bulk-loads the data to the Neptune target database. The default is 1,048,576 KB. If the bulk load is successful, AWS DMS clears the bucket, ready to store the next batch of migrated graph data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_retry_count(self) -> typing.Optional[jsii.Number]:
            '''The number of times for AWS DMS to retry a bulk load of migrated graph data to the Neptune target database before raising an error.

            The default is 5.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-maxretrycount
            '''
            result = self._values.get("max_retry_count")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def s3_bucket_folder(self) -> typing.Optional[builtins.str]:
            '''A folder path where you want AWS DMS to store migrated graph data in the S3 bucket specified by ``S3BucketName``.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-s3bucketfolder
            '''
            result = self._values.get("s3_bucket_folder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon S3 bucket where AWS DMS can temporarily store migrated graph data in .csv files before bulk-loading it to the Neptune target database. AWS DMS maps the SQL source data to graph data before storing it in these .csv files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-s3bucketname
            '''
            result = self._values.get("s3_bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the service role that you created for the Neptune target endpoint.

            The role must allow the ``iam:PassRole`` action.

            For more information, see `Creating an IAM Service Role for Accessing Amazon Neptune as a Target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.ServiceRole>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-neptunesettings.html#cfn-dms-endpoint-neptunesettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NeptuneSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.OracleSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_alternate_directly": "accessAlternateDirectly",
            "additional_archived_log_dest_id": "additionalArchivedLogDestId",
            "add_supplemental_logging": "addSupplementalLogging",
            "allow_select_nested_tables": "allowSelectNestedTables",
            "archived_log_dest_id": "archivedLogDestId",
            "archived_logs_only": "archivedLogsOnly",
            "asm_password": "asmPassword",
            "asm_server": "asmServer",
            "asm_user": "asmUser",
            "char_length_semantics": "charLengthSemantics",
            "direct_path_no_log": "directPathNoLog",
            "direct_path_parallel_load": "directPathParallelLoad",
            "enable_homogenous_tablespace": "enableHomogenousTablespace",
            "extra_archived_log_dest_ids": "extraArchivedLogDestIds",
            "fail_tasks_on_lob_truncation": "failTasksOnLobTruncation",
            "number_datatype_scale": "numberDatatypeScale",
            "oracle_path_prefix": "oraclePathPrefix",
            "parallel_asm_read_threads": "parallelAsmReadThreads",
            "read_ahead_blocks": "readAheadBlocks",
            "read_table_space_name": "readTableSpaceName",
            "replace_path_prefix": "replacePathPrefix",
            "retry_interval": "retryInterval",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_oracle_asm_access_role_arn": "secretsManagerOracleAsmAccessRoleArn",
            "secrets_manager_oracle_asm_secret_id": "secretsManagerOracleAsmSecretId",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "security_db_encryption": "securityDbEncryption",
            "security_db_encryption_name": "securityDbEncryptionName",
            "spatial_data_option_to_geo_json_function_name": "spatialDataOptionToGeoJsonFunctionName",
            "standby_delay_time": "standbyDelayTime",
            "use_alternate_folder_for_online": "useAlternateFolderForOnline",
            "use_b_file": "useBFile",
            "use_direct_path_full_load": "useDirectPathFullLoad",
            "use_logminer_reader": "useLogminerReader",
            "use_path_prefix": "usePathPrefix",
        },
    )
    class OracleSettingsProperty:
        def __init__(
            self,
            *,
            access_alternate_directly: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            additional_archived_log_dest_id: typing.Optional[jsii.Number] = None,
            add_supplemental_logging: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            allow_select_nested_tables: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            archived_log_dest_id: typing.Optional[jsii.Number] = None,
            archived_logs_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            asm_password: typing.Optional[builtins.str] = None,
            asm_server: typing.Optional[builtins.str] = None,
            asm_user: typing.Optional[builtins.str] = None,
            char_length_semantics: typing.Optional[builtins.str] = None,
            direct_path_no_log: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            direct_path_parallel_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            enable_homogenous_tablespace: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            extra_archived_log_dest_ids: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
            fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            number_datatype_scale: typing.Optional[jsii.Number] = None,
            oracle_path_prefix: typing.Optional[builtins.str] = None,
            parallel_asm_read_threads: typing.Optional[jsii.Number] = None,
            read_ahead_blocks: typing.Optional[jsii.Number] = None,
            read_table_space_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            replace_path_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            retry_interval: typing.Optional[jsii.Number] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_oracle_asm_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_oracle_asm_secret_id: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            security_db_encryption: typing.Optional[builtins.str] = None,
            security_db_encryption_name: typing.Optional[builtins.str] = None,
            spatial_data_option_to_geo_json_function_name: typing.Optional[builtins.str] = None,
            standby_delay_time: typing.Optional[jsii.Number] = None,
            use_alternate_folder_for_online: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_b_file: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_direct_path_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_logminer_reader: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_path_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines an Oracle endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param access_alternate_directly: Set this attribute to ``false`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.
            :param additional_archived_log_dest_id: Set this attribute with ``ArchivedLogDestId`` in a primary/ standby setup. This attribute is useful in the case of a switchover. In this case, AWS DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover. Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless necessary. For additional information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .
            :param add_supplemental_logging: Set this attribute to set up table-level supplemental logging for the Oracle database. This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task. If you use this option, you still need to enable database-level supplemental logging.
            :param allow_select_nested_tables: Set this attribute to ``true`` to enable replication of Oracle tables containing columns that are nested tables or defined types.
            :param archived_log_dest_id: Specifies the ID of the destination for the archived redo logs. This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the ``AdditionalArchivedLogDestId`` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.
            :param archived_logs_only: When this field is set to ``Y`` , AWS DMS only accesses the archived redo logs. If the archived redo logs are stored on Automatic Storage Management (ASM) only, the AWS DMS user account needs to be granted ASM privileges.
            :param asm_password: For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password. You can set this value from the ``*asm_user_password*`` value. You set this value as part of the comma-separated value that you set to the ``Password`` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .
            :param asm_server: For an Oracle source endpoint, your ASM server address. You can set this value from the ``asm_server`` value. You set ``asm_server`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .
            :param asm_user: For an Oracle source endpoint, your ASM user name. You can set this value from the ``asm_user`` value. You set ``asm_user`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .
            :param char_length_semantics: Specifies whether the length of a character column is in bytes or in characters. To indicate that the character column length is in characters, set this attribute to ``CHAR`` . Otherwise, the character column length is in bytes. Example: ``charLengthSemantics=CHAR;``
            :param direct_path_no_log: When set to ``true`` , this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.
            :param direct_path_parallel_load: When set to ``true`` , this attribute specifies a parallel load when ``useDirectPathFullLoad`` is set to ``Y`` . This attribute also only applies when you use the AWS DMS parallel load feature. Note that the target table cannot have any constraints or indexes.
            :param enable_homogenous_tablespace: Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.
            :param extra_archived_log_dest_ids: Specifies the IDs of one more destinations for one or more archived redo logs. These IDs are the values of the ``dest_id`` column in the ``v$archived_log`` view. Use this setting with the ``archivedLogDestId`` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup. This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, AWS DMS needs information about what destination to get archive redo logs from to read changes. AWS DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings. ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2]`` In a primary-to-multiple-standby setup, you might apply the following settings. ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]`` Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless it's necessary. For more information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .
            :param fail_tasks_on_lob_truncation: When set to ``true`` , this attribute causes a task to fail if the actual size of an LOB column is greater than the specified ``LobMaxSize`` . If a task is set to limited LOB mode and this option is set to ``true`` , the task fails instead of truncating the LOB data.
            :param number_datatype_scale: Specifies the number scale. You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10. Example: ``numberDataTypeScale=12``
            :param oracle_path_prefix: Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the default Oracle root used to access the redo logs.
            :param parallel_asm_read_threads: Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the ``readAheadBlocks`` attribute.
            :param read_ahead_blocks: Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM). You can specify an integer value between 1000 (the default) and 200,000 (the maximum).
            :param read_table_space_name: When set to ``true`` , this attribute supports tablespace replication.
            :param replace_path_prefix: Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This setting tells DMS instance to replace the default Oracle root with the specified ``usePathPrefix`` setting to access the redo logs.
            :param retry_interval: Specifies the number of seconds that the system waits before resending a query. Example: ``retryInterval=6;``
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Oracle endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_oracle_asm_access_role_arn: Required only if your Oracle endpoint uses Advanced Storage Manager (ASM). The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the ``SecretsManagerOracleAsmSecret`` . This ``SecretsManagerOracleAsmSecret`` has the secret value that allows access to the Oracle ASM of the endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerOracleAsmSecretId`` . Or you can specify clear-text values for ``AsmUser`` , ``AsmPassword`` , and ``AsmServerName`` . You can't specify both. For more information on creating this ``SecretsManagerOracleAsmSecret`` , the corresponding ``SecretsManagerOracleAsmAccessRoleArn`` , and the ``SecretsManagerOracleAsmSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_oracle_asm_secret_id: Required only if your Oracle endpoint uses Advanced Storage Manager (ASM). The full ARN, partial ARN, or display name of the ``SecretsManagerOracleAsmSecret`` that contains the Oracle ASM connection details for the Oracle endpoint.
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Oracle endpoint connection details.
            :param security_db_encryption: For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader. It is also the ``*TDE_Password*`` part of the comma-separated value you set to the ``Password`` request parameter when you create the endpoint. The ``SecurityDbEncryptian`` setting is related to this ``SecurityDbEncryptionName`` setting. For more information, see `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .
            :param security_db_encryption_name: For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE. The key value is the value of the ``SecurityDbEncryption`` setting. For more information on setting the key name value of ``SecurityDbEncryptionName`` , see the information and example for setting the ``securityDbEncryptionName`` extra connection attribute in `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .
            :param spatial_data_option_to_geo_json_function_name: Use this attribute to convert ``SDO_GEOMETRY`` to ``GEOJSON`` format. By default, DMS calls the ``SDO2GEOJSON`` custom function if present and accessible. Or you can create your own custom function that mimics the operation of ``SDOGEOJSON`` and set ``SpatialDataOptionToGeoJsonFunctionName`` to call it instead.
            :param standby_delay_time: Use this attribute to specify a time in minutes for the delay in standby sync. If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases. In AWS DMS , you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.
            :param use_alternate_folder_for_online: Set this attribute to ``true`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This tells the DMS instance to use any specified prefix replacement to access all online redo logs.
            :param use_b_file: Set this attribute to Y to capture change data using the Binary Reader utility. Set ``UseLogminerReader`` to N to set this attribute to Y. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ .
            :param use_direct_path_full_load: Set this attribute to Y to have AWS DMS use a direct path full load. Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.
            :param use_logminer_reader: Set this attribute to Y to capture change data using the Oracle LogMiner utility (the default). Set this attribute to N if you want to access the redo logs as a binary file. When you set ``UseLogminerReader`` to N, also set ``UseBfile`` to Y. For more information on this setting and using Oracle ASM, see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ in the *AWS DMS User Guide* .
            :param use_path_prefix: Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source. This value specifies the path prefix used to replace the default Oracle root to access the redo logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                oracle_settings_property = dms.CfnEndpoint.OracleSettingsProperty(
                    access_alternate_directly=False,
                    additional_archived_log_dest_id=123,
                    add_supplemental_logging=False,
                    allow_select_nested_tables=False,
                    archived_log_dest_id=123,
                    archived_logs_only=False,
                    asm_password="asmPassword",
                    asm_server="asmServer",
                    asm_user="asmUser",
                    char_length_semantics="charLengthSemantics",
                    direct_path_no_log=False,
                    direct_path_parallel_load=False,
                    enable_homogenous_tablespace=False,
                    extra_archived_log_dest_ids=[123],
                    fail_tasks_on_lob_truncation=False,
                    number_datatype_scale=123,
                    oracle_path_prefix="oraclePathPrefix",
                    parallel_asm_read_threads=123,
                    read_ahead_blocks=123,
                    read_table_space_name=False,
                    replace_path_prefix=False,
                    retry_interval=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_oracle_asm_access_role_arn="secretsManagerOracleAsmAccessRoleArn",
                    secrets_manager_oracle_asm_secret_id="secretsManagerOracleAsmSecretId",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    security_db_encryption="securityDbEncryption",
                    security_db_encryption_name="securityDbEncryptionName",
                    spatial_data_option_to_geo_json_function_name="spatialDataOptionToGeoJsonFunctionName",
                    standby_delay_time=123,
                    use_alternate_folder_for_online=False,
                    use_bFile=False,
                    use_direct_path_full_load=False,
                    use_logminer_reader=False,
                    use_path_prefix="usePathPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7cce1496a9f9494141ae407b9fa752179dcdfea2913cf1fd3d74b79dbdb605c)
                check_type(argname="argument access_alternate_directly", value=access_alternate_directly, expected_type=type_hints["access_alternate_directly"])
                check_type(argname="argument additional_archived_log_dest_id", value=additional_archived_log_dest_id, expected_type=type_hints["additional_archived_log_dest_id"])
                check_type(argname="argument add_supplemental_logging", value=add_supplemental_logging, expected_type=type_hints["add_supplemental_logging"])
                check_type(argname="argument allow_select_nested_tables", value=allow_select_nested_tables, expected_type=type_hints["allow_select_nested_tables"])
                check_type(argname="argument archived_log_dest_id", value=archived_log_dest_id, expected_type=type_hints["archived_log_dest_id"])
                check_type(argname="argument archived_logs_only", value=archived_logs_only, expected_type=type_hints["archived_logs_only"])
                check_type(argname="argument asm_password", value=asm_password, expected_type=type_hints["asm_password"])
                check_type(argname="argument asm_server", value=asm_server, expected_type=type_hints["asm_server"])
                check_type(argname="argument asm_user", value=asm_user, expected_type=type_hints["asm_user"])
                check_type(argname="argument char_length_semantics", value=char_length_semantics, expected_type=type_hints["char_length_semantics"])
                check_type(argname="argument direct_path_no_log", value=direct_path_no_log, expected_type=type_hints["direct_path_no_log"])
                check_type(argname="argument direct_path_parallel_load", value=direct_path_parallel_load, expected_type=type_hints["direct_path_parallel_load"])
                check_type(argname="argument enable_homogenous_tablespace", value=enable_homogenous_tablespace, expected_type=type_hints["enable_homogenous_tablespace"])
                check_type(argname="argument extra_archived_log_dest_ids", value=extra_archived_log_dest_ids, expected_type=type_hints["extra_archived_log_dest_ids"])
                check_type(argname="argument fail_tasks_on_lob_truncation", value=fail_tasks_on_lob_truncation, expected_type=type_hints["fail_tasks_on_lob_truncation"])
                check_type(argname="argument number_datatype_scale", value=number_datatype_scale, expected_type=type_hints["number_datatype_scale"])
                check_type(argname="argument oracle_path_prefix", value=oracle_path_prefix, expected_type=type_hints["oracle_path_prefix"])
                check_type(argname="argument parallel_asm_read_threads", value=parallel_asm_read_threads, expected_type=type_hints["parallel_asm_read_threads"])
                check_type(argname="argument read_ahead_blocks", value=read_ahead_blocks, expected_type=type_hints["read_ahead_blocks"])
                check_type(argname="argument read_table_space_name", value=read_table_space_name, expected_type=type_hints["read_table_space_name"])
                check_type(argname="argument replace_path_prefix", value=replace_path_prefix, expected_type=type_hints["replace_path_prefix"])
                check_type(argname="argument retry_interval", value=retry_interval, expected_type=type_hints["retry_interval"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_oracle_asm_access_role_arn", value=secrets_manager_oracle_asm_access_role_arn, expected_type=type_hints["secrets_manager_oracle_asm_access_role_arn"])
                check_type(argname="argument secrets_manager_oracle_asm_secret_id", value=secrets_manager_oracle_asm_secret_id, expected_type=type_hints["secrets_manager_oracle_asm_secret_id"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument security_db_encryption", value=security_db_encryption, expected_type=type_hints["security_db_encryption"])
                check_type(argname="argument security_db_encryption_name", value=security_db_encryption_name, expected_type=type_hints["security_db_encryption_name"])
                check_type(argname="argument spatial_data_option_to_geo_json_function_name", value=spatial_data_option_to_geo_json_function_name, expected_type=type_hints["spatial_data_option_to_geo_json_function_name"])
                check_type(argname="argument standby_delay_time", value=standby_delay_time, expected_type=type_hints["standby_delay_time"])
                check_type(argname="argument use_alternate_folder_for_online", value=use_alternate_folder_for_online, expected_type=type_hints["use_alternate_folder_for_online"])
                check_type(argname="argument use_b_file", value=use_b_file, expected_type=type_hints["use_b_file"])
                check_type(argname="argument use_direct_path_full_load", value=use_direct_path_full_load, expected_type=type_hints["use_direct_path_full_load"])
                check_type(argname="argument use_logminer_reader", value=use_logminer_reader, expected_type=type_hints["use_logminer_reader"])
                check_type(argname="argument use_path_prefix", value=use_path_prefix, expected_type=type_hints["use_path_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_alternate_directly is not None:
                self._values["access_alternate_directly"] = access_alternate_directly
            if additional_archived_log_dest_id is not None:
                self._values["additional_archived_log_dest_id"] = additional_archived_log_dest_id
            if add_supplemental_logging is not None:
                self._values["add_supplemental_logging"] = add_supplemental_logging
            if allow_select_nested_tables is not None:
                self._values["allow_select_nested_tables"] = allow_select_nested_tables
            if archived_log_dest_id is not None:
                self._values["archived_log_dest_id"] = archived_log_dest_id
            if archived_logs_only is not None:
                self._values["archived_logs_only"] = archived_logs_only
            if asm_password is not None:
                self._values["asm_password"] = asm_password
            if asm_server is not None:
                self._values["asm_server"] = asm_server
            if asm_user is not None:
                self._values["asm_user"] = asm_user
            if char_length_semantics is not None:
                self._values["char_length_semantics"] = char_length_semantics
            if direct_path_no_log is not None:
                self._values["direct_path_no_log"] = direct_path_no_log
            if direct_path_parallel_load is not None:
                self._values["direct_path_parallel_load"] = direct_path_parallel_load
            if enable_homogenous_tablespace is not None:
                self._values["enable_homogenous_tablespace"] = enable_homogenous_tablespace
            if extra_archived_log_dest_ids is not None:
                self._values["extra_archived_log_dest_ids"] = extra_archived_log_dest_ids
            if fail_tasks_on_lob_truncation is not None:
                self._values["fail_tasks_on_lob_truncation"] = fail_tasks_on_lob_truncation
            if number_datatype_scale is not None:
                self._values["number_datatype_scale"] = number_datatype_scale
            if oracle_path_prefix is not None:
                self._values["oracle_path_prefix"] = oracle_path_prefix
            if parallel_asm_read_threads is not None:
                self._values["parallel_asm_read_threads"] = parallel_asm_read_threads
            if read_ahead_blocks is not None:
                self._values["read_ahead_blocks"] = read_ahead_blocks
            if read_table_space_name is not None:
                self._values["read_table_space_name"] = read_table_space_name
            if replace_path_prefix is not None:
                self._values["replace_path_prefix"] = replace_path_prefix
            if retry_interval is not None:
                self._values["retry_interval"] = retry_interval
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_oracle_asm_access_role_arn is not None:
                self._values["secrets_manager_oracle_asm_access_role_arn"] = secrets_manager_oracle_asm_access_role_arn
            if secrets_manager_oracle_asm_secret_id is not None:
                self._values["secrets_manager_oracle_asm_secret_id"] = secrets_manager_oracle_asm_secret_id
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if security_db_encryption is not None:
                self._values["security_db_encryption"] = security_db_encryption
            if security_db_encryption_name is not None:
                self._values["security_db_encryption_name"] = security_db_encryption_name
            if spatial_data_option_to_geo_json_function_name is not None:
                self._values["spatial_data_option_to_geo_json_function_name"] = spatial_data_option_to_geo_json_function_name
            if standby_delay_time is not None:
                self._values["standby_delay_time"] = standby_delay_time
            if use_alternate_folder_for_online is not None:
                self._values["use_alternate_folder_for_online"] = use_alternate_folder_for_online
            if use_b_file is not None:
                self._values["use_b_file"] = use_b_file
            if use_direct_path_full_load is not None:
                self._values["use_direct_path_full_load"] = use_direct_path_full_load
            if use_logminer_reader is not None:
                self._values["use_logminer_reader"] = use_logminer_reader
            if use_path_prefix is not None:
                self._values["use_path_prefix"] = use_path_prefix

        @builtins.property
        def access_alternate_directly(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to ``false`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This tells the DMS instance to not access redo logs through any specified path prefix replacement using direct file access.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-accessalternatedirectly
            '''
            result = self._values.get("access_alternate_directly")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def additional_archived_log_dest_id(self) -> typing.Optional[jsii.Number]:
            '''Set this attribute with ``ArchivedLogDestId`` in a primary/ standby setup.

            This attribute is useful in the case of a switchover. In this case, AWS DMS needs to know which destination to get archive redo logs from to read changes. This need arises because the previous primary instance is now a standby instance after switchover.

            Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless necessary. For additional information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-additionalarchivedlogdestid
            '''
            result = self._values.get("additional_archived_log_dest_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def add_supplemental_logging(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to set up table-level supplemental logging for the Oracle database.

            This attribute enables PRIMARY KEY supplemental logging on all tables selected for a migration task.

            If you use this option, you still need to enable database-level supplemental logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-addsupplementallogging
            '''
            result = self._values.get("add_supplemental_logging")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def allow_select_nested_tables(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to ``true`` to enable replication of Oracle tables containing columns that are nested tables or defined types.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-allowselectnestedtables
            '''
            result = self._values.get("allow_select_nested_tables")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def archived_log_dest_id(self) -> typing.Optional[jsii.Number]:
            '''Specifies the ID of the destination for the archived redo logs.

            This value should be the same as a number in the dest_id column of the v$archived_log view. If you work with an additional redo log destination, use the ``AdditionalArchivedLogDestId`` option to specify the additional destination ID. Doing this improves performance by ensuring that the correct logs are accessed from the outset.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-archivedlogdestid
            '''
            result = self._values.get("archived_log_dest_id")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def archived_logs_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When this field is set to ``Y`` , AWS DMS only accesses the archived redo logs.

            If the archived redo logs are stored on Automatic Storage Management (ASM) only, the AWS DMS user account needs to be granted ASM privileges.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-archivedlogsonly
            '''
            result = self._values.get("archived_logs_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def asm_password(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, your Oracle Automatic Storage Management (ASM) password.

            You can set this value from the ``*asm_user_password*`` value. You set this value as part of the comma-separated value that you set to the ``Password`` request parameter when you create the endpoint to access transaction logs using Binary Reader. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmpassword
            '''
            result = self._values.get("asm_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def asm_server(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, your ASM server address.

            You can set this value from the ``asm_server`` value. You set ``asm_server`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmserver
            '''
            result = self._values.get("asm_server")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def asm_user(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, your ASM user name.

            You can set this value from the ``asm_user`` value. You set ``asm_user`` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see `Configuration for change data capture (CDC) on an Oracle source database <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-asmuser
            '''
            result = self._values.get("asm_user")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def char_length_semantics(self) -> typing.Optional[builtins.str]:
            '''Specifies whether the length of a character column is in bytes or in characters.

            To indicate that the character column length is in characters, set this attribute to ``CHAR`` . Otherwise, the character column length is in bytes.

            Example: ``charLengthSemantics=CHAR;``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-charlengthsemantics
            '''
            result = self._values.get("char_length_semantics")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def direct_path_no_log(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , this attribute helps to increase the commit rate on the Oracle target database by writing directly to tables and not writing a trail to database logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-directpathnolog
            '''
            result = self._values.get("direct_path_no_log")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def direct_path_parallel_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , this attribute specifies a parallel load when ``useDirectPathFullLoad`` is set to ``Y`` .

            This attribute also only applies when you use the AWS DMS parallel load feature. Note that the target table cannot have any constraints or indexes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-directpathparallelload
            '''
            result = self._values.get("direct_path_parallel_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def enable_homogenous_tablespace(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to enable homogenous tablespace replication and create existing tables or indexes under the same tablespace on the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-enablehomogenoustablespace
            '''
            result = self._values.get("enable_homogenous_tablespace")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def extra_archived_log_dest_ids(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]]:
            '''Specifies the IDs of one more destinations for one or more archived redo logs.

            These IDs are the values of the ``dest_id`` column in the ``v$archived_log`` view. Use this setting with the ``archivedLogDestId`` extra connection attribute in a primary-to-single setup or a primary-to-multiple-standby setup.

            This setting is useful in a switchover when you use an Oracle Data Guard database as a source. In this case, AWS DMS needs information about what destination to get archive redo logs from to read changes. AWS DMS needs this because after the switchover the previous primary is a standby instance. For example, in a primary-to-single standby setup you might apply the following settings.

            ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2]``

            In a primary-to-multiple-standby setup, you might apply the following settings.

            ``archivedLogDestId=1; ExtraArchivedLogDestIds=[2,3,4]``

            Although AWS DMS supports the use of the Oracle ``RESETLOGS`` option to open the database, never use ``RESETLOGS`` unless it's necessary. For more information about ``RESETLOGS`` , see `RMAN Data Repair Concepts <https://docs.aws.amazon.com/https://docs.oracle.com/en/database/oracle/oracle-database/19/bradv/rman-data-repair-concepts.html#GUID-1805CCF7-4AF2-482D-B65A-998192F89C2B>`_ in the *Oracle Database Backup and Recovery User's Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-extraarchivedlogdestids
            '''
            result = self._values.get("extra_archived_log_dest_ids")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[jsii.Number]]], result)

        @builtins.property
        def fail_tasks_on_lob_truncation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , this attribute causes a task to fail if the actual size of an LOB column is greater than the specified ``LobMaxSize`` .

            If a task is set to limited LOB mode and this option is set to ``true`` , the task fails instead of truncating the LOB data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-failtasksonlobtruncation
            '''
            result = self._values.get("fail_tasks_on_lob_truncation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def number_datatype_scale(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number scale.

            You can select a scale up to 38, or you can select FLOAT. By default, the NUMBER data type is converted to precision 38, scale 10.

            Example: ``numberDataTypeScale=12``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-numberdatatypescale
            '''
            result = self._values.get("number_datatype_scale")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def oracle_path_prefix(self) -> typing.Optional[builtins.str]:
            '''Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This value specifies the default Oracle root used to access the redo logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-oraclepathprefix
            '''
            result = self._values.get("oracle_path_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def parallel_asm_read_threads(self) -> typing.Optional[jsii.Number]:
            '''Set this attribute to change the number of threads that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM).

            You can specify an integer value between 2 (the default) and 8 (the maximum). Use this attribute together with the ``readAheadBlocks`` attribute.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-parallelasmreadthreads
            '''
            result = self._values.get("parallel_asm_read_threads")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def read_ahead_blocks(self) -> typing.Optional[jsii.Number]:
            '''Set this attribute to change the number of read-ahead blocks that DMS configures to perform a change data capture (CDC) load using Oracle Automatic Storage Management (ASM).

            You can specify an integer value between 1000 (the default) and 200,000 (the maximum).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-readaheadblocks
            '''
            result = self._values.get("read_ahead_blocks")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def read_table_space_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , this attribute supports tablespace replication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-readtablespacename
            '''
            result = self._values.get("read_table_space_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def replace_path_prefix(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to true in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This setting tells DMS instance to replace the default Oracle root with the specified ``usePathPrefix`` setting to access the redo logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-replacepathprefix
            '''
            result = self._values.get("replace_path_prefix")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def retry_interval(self) -> typing.Optional[jsii.Number]:
            '''Specifies the number of seconds that the system waits before resending a query.

            Example: ``retryInterval=6;``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-retryinterval
            '''
            result = self._values.get("retry_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Oracle endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_oracle_asm_access_role_arn(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Required only if your Oracle endpoint uses Advanced Storage Manager (ASM).

            The full ARN of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the ``SecretsManagerOracleAsmSecret`` . This ``SecretsManagerOracleAsmSecret`` has the secret value that allows access to the Oracle ASM of the endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerOracleAsmSecretId`` . Or you can specify clear-text values for ``AsmUser`` , ``AsmPassword`` , and ``AsmServerName`` . You can't specify both.

               For more information on creating this ``SecretsManagerOracleAsmSecret`` , the corresponding ``SecretsManagerOracleAsmAccessRoleArn`` , and the ``SecretsManagerOracleAsmSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageroracleasmaccessrolearn
            '''
            result = self._values.get("secrets_manager_oracle_asm_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_oracle_asm_secret_id(self) -> typing.Optional[builtins.str]:
            '''Required only if your Oracle endpoint uses Advanced Storage Manager (ASM).

            The full ARN, partial ARN, or display name of the ``SecretsManagerOracleAsmSecret`` that contains the Oracle ASM connection details for the Oracle endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanageroracleasmsecretid
            '''
            result = self._values.get("secrets_manager_oracle_asm_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Oracle endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_db_encryption(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, the transparent data encryption (TDE) password required by AWM DMS to access Oracle redo logs encrypted by TDE using Binary Reader.

            It is also the ``*TDE_Password*`` part of the comma-separated value you set to the ``Password`` request parameter when you create the endpoint. The ``SecurityDbEncryptian`` setting is related to this ``SecurityDbEncryptionName`` setting. For more information, see `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-securitydbencryption
            '''
            result = self._values.get("security_db_encryption")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_db_encryption_name(self) -> typing.Optional[builtins.str]:
            '''For an Oracle source endpoint, the name of a key used for the transparent data encryption (TDE) of the columns and tablespaces in an Oracle source database that is encrypted using TDE.

            The key value is the value of the ``SecurityDbEncryption`` setting. For more information on setting the key name value of ``SecurityDbEncryptionName`` , see the information and example for setting the ``securityDbEncryptionName`` extra connection attribute in `Supported encryption methods for using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.Encryption>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-securitydbencryptionname
            '''
            result = self._values.get("security_db_encryption_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def spatial_data_option_to_geo_json_function_name(
            self,
        ) -> typing.Optional[builtins.str]:
            '''Use this attribute to convert ``SDO_GEOMETRY`` to ``GEOJSON`` format.

            By default, DMS calls the ``SDO2GEOJSON`` custom function if present and accessible. Or you can create your own custom function that mimics the operation of ``SDOGEOJSON`` and set ``SpatialDataOptionToGeoJsonFunctionName`` to call it instead.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-spatialdataoptiontogeojsonfunctionname
            '''
            result = self._values.get("spatial_data_option_to_geo_json_function_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def standby_delay_time(self) -> typing.Optional[jsii.Number]:
            '''Use this attribute to specify a time in minutes for the delay in standby sync.

            If the source is an Oracle Active Data Guard standby database, use this attribute to specify the time lag between primary and standby databases.

            In AWS DMS , you can create an Oracle CDC task that uses an Active Data Guard standby instance as a source for replicating ongoing changes. Doing this eliminates the need to connect to an active database that might be in production.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-standbydelaytime
            '''
            result = self._values.get("standby_delay_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def use_alternate_folder_for_online(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to ``true`` in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This tells the DMS instance to use any specified prefix replacement to access all online redo logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usealternatefolderforonline
            '''
            result = self._values.get("use_alternate_folder_for_online")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_b_file(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to Y to capture change data using the Binary Reader utility.

            Set ``UseLogminerReader`` to N to set this attribute to Y. To use Binary Reader with Amazon RDS for Oracle as the source, you set additional attributes. For more information about using this setting with Oracle Automatic Storage Management (ASM), see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usebfile
            '''
            result = self._values.get("use_b_file")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_direct_path_full_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to Y to have AWS DMS use a direct path full load.

            Specify this value to use the direct path protocol in the Oracle Call Interface (OCI). By using this OCI protocol, you can bulk-load Oracle target tables during a full load.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usedirectpathfullload
            '''
            result = self._values.get("use_direct_path_full_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_logminer_reader(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Set this attribute to Y to capture change data using the Oracle LogMiner utility (the default).

            Set this attribute to N if you want to access the redo logs as a binary file. When you set ``UseLogminerReader`` to N, also set ``UseBfile`` to Y. For more information on this setting and using Oracle ASM, see `Using Oracle LogMiner or AWS DMS Binary Reader for CDC <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC>`_ in the *AWS DMS User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-uselogminerreader
            '''
            result = self._values.get("use_logminer_reader")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_path_prefix(self) -> typing.Optional[builtins.str]:
            '''Set this string attribute to the required value in order to use the Binary Reader to capture change data for an Amazon RDS for Oracle as the source.

            This value specifies the path prefix used to replace the default Oracle root to access the redo logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-oraclesettings.html#cfn-dms-endpoint-oraclesettings-usepathprefix
            '''
            result = self._values.get("use_path_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OracleSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.PostgreSqlSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "after_connect_script": "afterConnectScript",
            "babelfish_database_name": "babelfishDatabaseName",
            "capture_ddls": "captureDdls",
            "database_mode": "databaseMode",
            "ddl_artifacts_schema": "ddlArtifactsSchema",
            "execute_timeout": "executeTimeout",
            "fail_tasks_on_lob_truncation": "failTasksOnLobTruncation",
            "heartbeat_enable": "heartbeatEnable",
            "heartbeat_frequency": "heartbeatFrequency",
            "heartbeat_schema": "heartbeatSchema",
            "map_boolean_as_boolean": "mapBooleanAsBoolean",
            "max_file_size": "maxFileSize",
            "plugin_name": "pluginName",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "slot_name": "slotName",
        },
    )
    class PostgreSqlSettingsProperty:
        def __init__(
            self,
            *,
            after_connect_script: typing.Optional[builtins.str] = None,
            babelfish_database_name: typing.Optional[builtins.str] = None,
            capture_ddls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            database_mode: typing.Optional[builtins.str] = None,
            ddl_artifacts_schema: typing.Optional[builtins.str] = None,
            execute_timeout: typing.Optional[jsii.Number] = None,
            fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            heartbeat_enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            heartbeat_frequency: typing.Optional[jsii.Number] = None,
            heartbeat_schema: typing.Optional[builtins.str] = None,
            map_boolean_as_boolean: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            plugin_name: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            slot_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a PostgreSQL endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param after_connect_script: For use with change data capture (CDC) only, this attribute has AWS DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data. Example: ``afterConnectScript=SET session_replication_role='replica'``
            :param babelfish_database_name: The Babelfish for Aurora PostgreSQL database name for the endpoint.
            :param capture_ddls: To capture DDL events, AWS DMS creates various artifacts in the PostgreSQL database when the task starts. You can later remove these artifacts. If this value is set to ``True`` , you don't have to create tables or triggers on the source database.
            :param database_mode: Specifies the default behavior of the replication's handling of PostgreSQL- compatible endpoints that require some additional configuration, such as Babelfish endpoints.
            :param ddl_artifacts_schema: The schema in which the operational DDL database artifacts are created. The default value is ``public`` . Example: ``ddlArtifactsSchema=xyzddlschema;``
            :param execute_timeout: Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds. Example: ``executeTimeout=100;``
            :param fail_tasks_on_lob_truncation: When set to ``true`` , this value causes a task to fail if the actual size of a LOB column is greater than the specified ``LobMaxSize`` . The default value is ``false`` . If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.
            :param heartbeat_enable: The write-ahead log (WAL) heartbeat feature mimics a dummy transaction. By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps ``restart_lsn`` moving and prevents storage full scenarios. The default value is ``false`` .
            :param heartbeat_frequency: Sets the WAL heartbeat frequency (in minutes). The default value is 5 minutes.
            :param heartbeat_schema: Sets the schema in which the heartbeat artifacts are created. The default value is ``public`` .
            :param map_boolean_as_boolean: When true, lets PostgreSQL migrate the boolean type as boolean. By default, PostgreSQL migrates booleans as ``varchar(5)`` . You must set this setting on both the source and target endpoints for it to take effect. The default value is ``false`` .
            :param max_file_size: Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL. The default value is 32,768 KB (32 MB). Example: ``maxFileSize=512``
            :param plugin_name: Specifies the plugin to use to create a replication slot. The default value is ``pglogical`` .
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the PostgreSQL endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the PostgreSQL endpoint connection details.
            :param slot_name: Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance. When used with the ``CdcStartPosition`` request parameter for the AWS DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of ``CdcStartPosition`` . If the specified slot doesn't exist or the task doesn't have a valid ``CdcStartPosition`` setting, DMS raises an error. For more information about setting the ``CdcStartPosition`` request parameter, see `Determining a CDC native start point <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native>`_ in the *AWS Database Migration Service User Guide* . For more information about using ``CdcStartPosition`` , see `CreateReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html>`_ , `StartReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html>`_ , and `ModifyReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                postgre_sql_settings_property = dms.CfnEndpoint.PostgreSqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    babelfish_database_name="babelfishDatabaseName",
                    capture_ddls=False,
                    database_mode="databaseMode",
                    ddl_artifacts_schema="ddlArtifactsSchema",
                    execute_timeout=123,
                    fail_tasks_on_lob_truncation=False,
                    heartbeat_enable=False,
                    heartbeat_frequency=123,
                    heartbeat_schema="heartbeatSchema",
                    map_boolean_as_boolean=False,
                    max_file_size=123,
                    plugin_name="pluginName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    slot_name="slotName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f006252c94d67f9b7da655f75e078cda6ee89974586c55a2d16ba2775091e058)
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument babelfish_database_name", value=babelfish_database_name, expected_type=type_hints["babelfish_database_name"])
                check_type(argname="argument capture_ddls", value=capture_ddls, expected_type=type_hints["capture_ddls"])
                check_type(argname="argument database_mode", value=database_mode, expected_type=type_hints["database_mode"])
                check_type(argname="argument ddl_artifacts_schema", value=ddl_artifacts_schema, expected_type=type_hints["ddl_artifacts_schema"])
                check_type(argname="argument execute_timeout", value=execute_timeout, expected_type=type_hints["execute_timeout"])
                check_type(argname="argument fail_tasks_on_lob_truncation", value=fail_tasks_on_lob_truncation, expected_type=type_hints["fail_tasks_on_lob_truncation"])
                check_type(argname="argument heartbeat_enable", value=heartbeat_enable, expected_type=type_hints["heartbeat_enable"])
                check_type(argname="argument heartbeat_frequency", value=heartbeat_frequency, expected_type=type_hints["heartbeat_frequency"])
                check_type(argname="argument heartbeat_schema", value=heartbeat_schema, expected_type=type_hints["heartbeat_schema"])
                check_type(argname="argument map_boolean_as_boolean", value=map_boolean_as_boolean, expected_type=type_hints["map_boolean_as_boolean"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument plugin_name", value=plugin_name, expected_type=type_hints["plugin_name"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument slot_name", value=slot_name, expected_type=type_hints["slot_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if babelfish_database_name is not None:
                self._values["babelfish_database_name"] = babelfish_database_name
            if capture_ddls is not None:
                self._values["capture_ddls"] = capture_ddls
            if database_mode is not None:
                self._values["database_mode"] = database_mode
            if ddl_artifacts_schema is not None:
                self._values["ddl_artifacts_schema"] = ddl_artifacts_schema
            if execute_timeout is not None:
                self._values["execute_timeout"] = execute_timeout
            if fail_tasks_on_lob_truncation is not None:
                self._values["fail_tasks_on_lob_truncation"] = fail_tasks_on_lob_truncation
            if heartbeat_enable is not None:
                self._values["heartbeat_enable"] = heartbeat_enable
            if heartbeat_frequency is not None:
                self._values["heartbeat_frequency"] = heartbeat_frequency
            if heartbeat_schema is not None:
                self._values["heartbeat_schema"] = heartbeat_schema
            if map_boolean_as_boolean is not None:
                self._values["map_boolean_as_boolean"] = map_boolean_as_boolean
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if plugin_name is not None:
                self._values["plugin_name"] = plugin_name
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if slot_name is not None:
                self._values["slot_name"] = slot_name

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''For use with change data capture (CDC) only, this attribute has AWS DMS bypass foreign keys and user triggers to reduce the time it takes to bulk load data.

            Example: ``afterConnectScript=SET session_replication_role='replica'``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def babelfish_database_name(self) -> typing.Optional[builtins.str]:
            '''The Babelfish for Aurora PostgreSQL database name for the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-babelfishdatabasename
            '''
            result = self._values.get("babelfish_database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def capture_ddls(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''To capture DDL events, AWS DMS creates various artifacts in the PostgreSQL database when the task starts.

            You can later remove these artifacts.

            If this value is set to ``True`` , you don't have to create tables or triggers on the source database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-captureddls
            '''
            result = self._values.get("capture_ddls")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def database_mode(self) -> typing.Optional[builtins.str]:
            '''Specifies the default behavior of the replication's handling of PostgreSQL- compatible endpoints that require some additional configuration, such as Babelfish endpoints.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-databasemode
            '''
            result = self._values.get("database_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ddl_artifacts_schema(self) -> typing.Optional[builtins.str]:
            '''The schema in which the operational DDL database artifacts are created.

            The default value is ``public`` .

            Example: ``ddlArtifactsSchema=xyzddlschema;``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-ddlartifactsschema
            '''
            result = self._values.get("ddl_artifacts_schema")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def execute_timeout(self) -> typing.Optional[jsii.Number]:
            '''Sets the client statement timeout for the PostgreSQL instance, in seconds. The default value is 60 seconds.

            Example: ``executeTimeout=100;``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-executetimeout
            '''
            result = self._values.get("execute_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def fail_tasks_on_lob_truncation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , this value causes a task to fail if the actual size of a LOB column is greater than the specified ``LobMaxSize`` .

            The default value is ``false`` .

            If task is set to Limited LOB mode and this option is set to true, the task fails instead of truncating the LOB data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-failtasksonlobtruncation
            '''
            result = self._values.get("fail_tasks_on_lob_truncation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def heartbeat_enable(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The write-ahead log (WAL) heartbeat feature mimics a dummy transaction.

            By doing this, it prevents idle logical replication slots from holding onto old WAL logs, which can result in storage full situations on the source. This heartbeat keeps ``restart_lsn`` moving and prevents storage full scenarios.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatenable
            '''
            result = self._values.get("heartbeat_enable")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def heartbeat_frequency(self) -> typing.Optional[jsii.Number]:
            '''Sets the WAL heartbeat frequency (in minutes).

            The default value is 5 minutes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatfrequency
            '''
            result = self._values.get("heartbeat_frequency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def heartbeat_schema(self) -> typing.Optional[builtins.str]:
            '''Sets the schema in which the heartbeat artifacts are created.

            The default value is ``public`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-heartbeatschema
            '''
            result = self._values.get("heartbeat_schema")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def map_boolean_as_boolean(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, lets PostgreSQL migrate the boolean type as boolean.

            By default, PostgreSQL migrates booleans as ``varchar(5)`` . You must set this setting on both the source and target endpoints for it to take effect.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-mapbooleanasboolean
            '''
            result = self._values.get("map_boolean_as_boolean")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''Specifies the maximum size (in KB) of any .csv file used to transfer data to PostgreSQL.

            The default value is 32,768 KB (32 MB).

            Example: ``maxFileSize=512``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def plugin_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the plugin to use to create a replication slot.

            The default value is ``pglogical`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-pluginname
            '''
            result = self._values.get("plugin_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the PostgreSQL endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the PostgreSQL endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slot_name(self) -> typing.Optional[builtins.str]:
            '''Sets the name of a previously created logical replication slot for a change data capture (CDC) load of the PostgreSQL source instance.

            When used with the ``CdcStartPosition`` request parameter for the AWS DMS API , this attribute also makes it possible to use native CDC start points. DMS verifies that the specified logical replication slot exists before starting the CDC load task. It also verifies that the task was created with a valid setting of ``CdcStartPosition`` . If the specified slot doesn't exist or the task doesn't have a valid ``CdcStartPosition`` setting, DMS raises an error.

            For more information about setting the ``CdcStartPosition`` request parameter, see `Determining a CDC native start point <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Task.CDC.html#CHAP_Task.CDC.StartPoint.Native>`_ in the *AWS Database Migration Service User Guide* . For more information about using ``CdcStartPosition`` , see `CreateReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_CreateReplicationTask.html>`_ , `StartReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTask.html>`_ , and `ModifyReplicationTask <https://docs.aws.amazon.com/dms/latest/APIReference/API_ModifyReplicationTask.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-postgresqlsettings.html#cfn-dms-endpoint-postgresqlsettings-slotname
            '''
            result = self._values.get("slot_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PostgreSqlSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.RedisSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_password": "authPassword",
            "auth_type": "authType",
            "auth_user_name": "authUserName",
            "port": "port",
            "server_name": "serverName",
            "ssl_ca_certificate_arn": "sslCaCertificateArn",
            "ssl_security_protocol": "sslSecurityProtocol",
        },
    )
    class RedisSettingsProperty:
        def __init__(
            self,
            *,
            auth_password: typing.Optional[builtins.str] = None,
            auth_type: typing.Optional[builtins.str] = None,
            auth_user_name: typing.Optional[builtins.str] = None,
            port: typing.Optional[jsii.Number] = None,
            server_name: typing.Optional[builtins.str] = None,
            ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
            ssl_security_protocol: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a Redis target endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

            :param auth_password: The password provided with the ``auth-role`` and ``auth-token`` options of the ``AuthType`` setting for a Redis target endpoint.
            :param auth_type: The type of authentication to perform when connecting to a Redis target. Options include ``none`` , ``auth-token`` , and ``auth-role`` . The ``auth-token`` option requires an ``AuthPassword`` value to be provided. The ``auth-role`` option requires ``AuthUserName`` and ``AuthPassword`` values to be provided.
            :param auth_user_name: The user name provided with the ``auth-role`` option of the ``AuthType`` setting for a Redis target endpoint.
            :param port: Transmission Control Protocol (TCP) port for the endpoint.
            :param server_name: Fully qualified domain name of the endpoint.
            :param ssl_ca_certificate_arn: The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.
            :param ssl_security_protocol: The connection to a Redis target endpoint using Transport Layer Security (TLS). Valid values include ``plaintext`` and ``ssl-encryption`` . The default is ``ssl-encryption`` . The ``ssl-encryption`` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the ``SslCaCertificateArn`` setting. If an ARN isn't given for a CA, DMS uses the Amazon root CA. The ``plaintext`` option doesn't provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                redis_settings_property = dms.CfnEndpoint.RedisSettingsProperty(
                    auth_password="authPassword",
                    auth_type="authType",
                    auth_user_name="authUserName",
                    port=123,
                    server_name="serverName",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_security_protocol="sslSecurityProtocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__011bfd078b664e3e69dd00e5da3734673e821b3644ee94fbbff42c5cd3e5b746)
                check_type(argname="argument auth_password", value=auth_password, expected_type=type_hints["auth_password"])
                check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
                check_type(argname="argument auth_user_name", value=auth_user_name, expected_type=type_hints["auth_user_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
                check_type(argname="argument ssl_ca_certificate_arn", value=ssl_ca_certificate_arn, expected_type=type_hints["ssl_ca_certificate_arn"])
                check_type(argname="argument ssl_security_protocol", value=ssl_security_protocol, expected_type=type_hints["ssl_security_protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_password is not None:
                self._values["auth_password"] = auth_password
            if auth_type is not None:
                self._values["auth_type"] = auth_type
            if auth_user_name is not None:
                self._values["auth_user_name"] = auth_user_name
            if port is not None:
                self._values["port"] = port
            if server_name is not None:
                self._values["server_name"] = server_name
            if ssl_ca_certificate_arn is not None:
                self._values["ssl_ca_certificate_arn"] = ssl_ca_certificate_arn
            if ssl_security_protocol is not None:
                self._values["ssl_security_protocol"] = ssl_security_protocol

        @builtins.property
        def auth_password(self) -> typing.Optional[builtins.str]:
            '''The password provided with the ``auth-role`` and ``auth-token`` options of the ``AuthType`` setting for a Redis target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authpassword
            '''
            result = self._values.get("auth_password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_type(self) -> typing.Optional[builtins.str]:
            '''The type of authentication to perform when connecting to a Redis target.

            Options include ``none`` , ``auth-token`` , and ``auth-role`` . The ``auth-token`` option requires an ``AuthPassword`` value to be provided. The ``auth-role`` option requires ``AuthUserName`` and ``AuthPassword`` values to be provided.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authtype
            '''
            result = self._values.get("auth_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth_user_name(self) -> typing.Optional[builtins.str]:
            '''The user name provided with the ``auth-role`` option of the ``AuthType`` setting for a Redis target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-authusername
            '''
            result = self._values.get("auth_user_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''Transmission Control Protocol (TCP) port for the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_name(self) -> typing.Optional[builtins.str]:
            '''Fully qualified domain name of the endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-servername
            '''
            result = self._values.get("server_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_ca_certificate_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the certificate authority (CA) that DMS uses to connect to your Redis target endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-sslcacertificatearn
            '''
            result = self._values.get("ssl_ca_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ssl_security_protocol(self) -> typing.Optional[builtins.str]:
            '''The connection to a Redis target endpoint using Transport Layer Security (TLS).

            Valid values include ``plaintext`` and ``ssl-encryption`` . The default is ``ssl-encryption`` . The ``ssl-encryption`` option makes an encrypted connection. Optionally, you can identify an Amazon Resource Name (ARN) for an SSL certificate authority (CA) using the ``SslCaCertificateArn`` setting. If an ARN isn't given for a CA, DMS uses the Amazon root CA.

            The ``plaintext`` option doesn't provide Transport Layer Security (TLS) encryption for traffic between endpoint and database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redissettings.html#cfn-dms-endpoint-redissettings-sslsecurityprotocol
            '''
            result = self._values.get("ssl_security_protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedisSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.RedshiftSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "accept_any_date": "acceptAnyDate",
            "after_connect_script": "afterConnectScript",
            "bucket_folder": "bucketFolder",
            "bucket_name": "bucketName",
            "case_sensitive_names": "caseSensitiveNames",
            "comp_update": "compUpdate",
            "connection_timeout": "connectionTimeout",
            "date_format": "dateFormat",
            "empty_as_null": "emptyAsNull",
            "encryption_mode": "encryptionMode",
            "explicit_ids": "explicitIds",
            "file_transfer_upload_streams": "fileTransferUploadStreams",
            "load_timeout": "loadTimeout",
            "map_boolean_as_boolean": "mapBooleanAsBoolean",
            "max_file_size": "maxFileSize",
            "remove_quotes": "removeQuotes",
            "replace_chars": "replaceChars",
            "replace_invalid_chars": "replaceInvalidChars",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
            "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
            "service_access_role_arn": "serviceAccessRoleArn",
            "time_format": "timeFormat",
            "trim_blanks": "trimBlanks",
            "truncate_columns": "truncateColumns",
            "write_buffer_size": "writeBufferSize",
        },
    )
    class RedshiftSettingsProperty:
        def __init__(
            self,
            *,
            accept_any_date: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            after_connect_script: typing.Optional[builtins.str] = None,
            bucket_folder: typing.Optional[builtins.str] = None,
            bucket_name: typing.Optional[builtins.str] = None,
            case_sensitive_names: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            comp_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            connection_timeout: typing.Optional[jsii.Number] = None,
            date_format: typing.Optional[builtins.str] = None,
            empty_as_null: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encryption_mode: typing.Optional[builtins.str] = None,
            explicit_ids: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            file_transfer_upload_streams: typing.Optional[jsii.Number] = None,
            load_timeout: typing.Optional[jsii.Number] = None,
            map_boolean_as_boolean: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            remove_quotes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            replace_chars: typing.Optional[builtins.str] = None,
            replace_invalid_chars: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
            server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
            time_format: typing.Optional[builtins.str] = None,
            trim_blanks: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            truncate_columns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            write_buffer_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Provides information that defines an Amazon Redshift endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param accept_any_date: A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose ``true`` or ``false`` (the default). This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.
            :param after_connect_script: Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.
            :param bucket_folder: An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster. For full load mode, AWS DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. AWS DMS uses the Redshift ``COPY`` command to upload the .csv files to the target table. The files are deleted once the ``COPY`` operation has finished. For more information, see `COPY <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`_ in the *Amazon Redshift Database Developer Guide* . For change-data-capture (CDC) mode, AWS DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.
            :param bucket_name: The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.
            :param case_sensitive_names: If Amazon Redshift is configured to support case sensitive schema names, set ``CaseSensitiveNames`` to ``true`` . The default is ``false`` .
            :param comp_update: If you set ``CompUpdate`` to ``true`` Amazon Redshift applies automatic compression if the table is empty. This applies even if the table columns already have encodings other than ``RAW`` . If you set ``CompUpdate`` to ``false`` , automatic compression is disabled and existing column encodings aren't changed. The default is ``true`` .
            :param connection_timeout: A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.
            :param date_format: The date format that you are using. Valid values are ``auto`` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't supported when you use a date format string. If your date and time values use formats different from each other, set this to ``auto`` .
            :param empty_as_null: A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .
            :param encryption_mode: The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . .. epigraph:: For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` . To use ``SSE_S3`` , create an AWS Identity and Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``
            :param explicit_ids: This setting is only valid for a full-load migration task. Set ``ExplicitIds`` to ``true`` to have tables with ``IDENTITY`` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is ``false`` .
            :param file_transfer_upload_streams: The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10. The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see `Multipart upload overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_ . ``FileTransferUploadStreams`` accepts a value from 1 through 64. It defaults to 10.
            :param load_timeout: The amount of time to wait (in milliseconds) before timing out of operations performed by AWS DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.
            :param map_boolean_as_boolean: When true, lets Redshift migrate the boolean type as boolean. By default, Redshift migrates booleans as ``varchar(1)`` . You must set this setting on both the source and target endpoints for it to take effect.
            :param max_file_size: The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).
            :param remove_quotes: A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose ``true`` to remove quotation marks. The default is ``false`` .
            :param replace_chars: A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars`` , substituting the specified characters instead. The default is ``"?"`` .
            :param replace_invalid_chars: A list of characters that you want to replace. Use with ``ReplaceChars`` .
            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Amazon Redshift endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Amazon Redshift endpoint connection details.
            :param server_side_encryption_kms_key_id: The AWS KMS key ID. If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.
            :param service_access_role_arn: The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service. The role must allow the ``iam:PassRole`` action.
            :param time_format: The time format that you want to use. Valid values are ``auto`` (case-sensitive), ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using ``auto`` recognizes most strings, even some that aren't supported when you use a time format string. If your date and time values use formats different from each other, set this parameter to ``auto`` .
            :param trim_blanks: A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove unneeded white space. The default is ``false`` .
            :param truncate_columns: A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default is ``false`` .
            :param write_buffer_size: The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                redshift_settings_property = dms.CfnEndpoint.RedshiftSettingsProperty(
                    accept_any_date=False,
                    after_connect_script="afterConnectScript",
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    case_sensitive_names=False,
                    comp_update=False,
                    connection_timeout=123,
                    date_format="dateFormat",
                    empty_as_null=False,
                    encryption_mode="encryptionMode",
                    explicit_ids=False,
                    file_transfer_upload_streams=123,
                    load_timeout=123,
                    map_boolean_as_boolean=False,
                    max_file_size=123,
                    remove_quotes=False,
                    replace_chars="replaceChars",
                    replace_invalid_chars="replaceInvalidChars",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    time_format="timeFormat",
                    trim_blanks=False,
                    truncate_columns=False,
                    write_buffer_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__017ba234c381b7c658aebe454c862c9121467fb310463c84973a8df81bb614f1)
                check_type(argname="argument accept_any_date", value=accept_any_date, expected_type=type_hints["accept_any_date"])
                check_type(argname="argument after_connect_script", value=after_connect_script, expected_type=type_hints["after_connect_script"])
                check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument case_sensitive_names", value=case_sensitive_names, expected_type=type_hints["case_sensitive_names"])
                check_type(argname="argument comp_update", value=comp_update, expected_type=type_hints["comp_update"])
                check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
                check_type(argname="argument date_format", value=date_format, expected_type=type_hints["date_format"])
                check_type(argname="argument empty_as_null", value=empty_as_null, expected_type=type_hints["empty_as_null"])
                check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
                check_type(argname="argument explicit_ids", value=explicit_ids, expected_type=type_hints["explicit_ids"])
                check_type(argname="argument file_transfer_upload_streams", value=file_transfer_upload_streams, expected_type=type_hints["file_transfer_upload_streams"])
                check_type(argname="argument load_timeout", value=load_timeout, expected_type=type_hints["load_timeout"])
                check_type(argname="argument map_boolean_as_boolean", value=map_boolean_as_boolean, expected_type=type_hints["map_boolean_as_boolean"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument remove_quotes", value=remove_quotes, expected_type=type_hints["remove_quotes"])
                check_type(argname="argument replace_chars", value=replace_chars, expected_type=type_hints["replace_chars"])
                check_type(argname="argument replace_invalid_chars", value=replace_invalid_chars, expected_type=type_hints["replace_invalid_chars"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
                check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
                check_type(argname="argument time_format", value=time_format, expected_type=type_hints["time_format"])
                check_type(argname="argument trim_blanks", value=trim_blanks, expected_type=type_hints["trim_blanks"])
                check_type(argname="argument truncate_columns", value=truncate_columns, expected_type=type_hints["truncate_columns"])
                check_type(argname="argument write_buffer_size", value=write_buffer_size, expected_type=type_hints["write_buffer_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if accept_any_date is not None:
                self._values["accept_any_date"] = accept_any_date
            if after_connect_script is not None:
                self._values["after_connect_script"] = after_connect_script
            if bucket_folder is not None:
                self._values["bucket_folder"] = bucket_folder
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if case_sensitive_names is not None:
                self._values["case_sensitive_names"] = case_sensitive_names
            if comp_update is not None:
                self._values["comp_update"] = comp_update
            if connection_timeout is not None:
                self._values["connection_timeout"] = connection_timeout
            if date_format is not None:
                self._values["date_format"] = date_format
            if empty_as_null is not None:
                self._values["empty_as_null"] = empty_as_null
            if encryption_mode is not None:
                self._values["encryption_mode"] = encryption_mode
            if explicit_ids is not None:
                self._values["explicit_ids"] = explicit_ids
            if file_transfer_upload_streams is not None:
                self._values["file_transfer_upload_streams"] = file_transfer_upload_streams
            if load_timeout is not None:
                self._values["load_timeout"] = load_timeout
            if map_boolean_as_boolean is not None:
                self._values["map_boolean_as_boolean"] = map_boolean_as_boolean
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if remove_quotes is not None:
                self._values["remove_quotes"] = remove_quotes
            if replace_chars is not None:
                self._values["replace_chars"] = replace_chars
            if replace_invalid_chars is not None:
                self._values["replace_invalid_chars"] = replace_invalid_chars
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id
            if server_side_encryption_kms_key_id is not None:
                self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn
            if time_format is not None:
                self._values["time_format"] = time_format
            if trim_blanks is not None:
                self._values["trim_blanks"] = trim_blanks
            if truncate_columns is not None:
                self._values["truncate_columns"] = truncate_columns
            if write_buffer_size is not None:
                self._values["write_buffer_size"] = write_buffer_size

        @builtins.property
        def accept_any_date(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error.

            You can choose ``true`` or ``false`` (the default).

            This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-acceptanydate
            '''
            result = self._values.get("accept_any_date")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def after_connect_script(self) -> typing.Optional[builtins.str]:
            '''Code to run after connecting.

            This parameter should contain the code itself, not the name of a file containing the code.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-afterconnectscript
            '''
            result = self._values.get("after_connect_script")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_folder(self) -> typing.Optional[builtins.str]:
            '''An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster.

            For full load mode, AWS DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. AWS DMS uses the Redshift ``COPY`` command to upload the .csv files to the target table. The files are deleted once the ``COPY`` operation has finished. For more information, see `COPY <https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html>`_ in the *Amazon Redshift Database Developer Guide* .

            For change-data-capture (CDC) mode, AWS DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-bucketfolder
            '''
            result = self._values.get("bucket_folder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def case_sensitive_names(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If Amazon Redshift is configured to support case sensitive schema names, set ``CaseSensitiveNames`` to ``true`` .

            The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-casesensitivenames
            '''
            result = self._values.get("case_sensitive_names")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def comp_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If you set ``CompUpdate`` to ``true`` Amazon Redshift applies automatic compression if the table is empty.

            This applies even if the table columns already have encodings other than ``RAW`` . If you set ``CompUpdate`` to ``false`` , automatic compression is disabled and existing column encodings aren't changed. The default is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-compupdate
            '''
            result = self._values.get("comp_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def connection_timeout(self) -> typing.Optional[jsii.Number]:
            '''A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-connectiontimeout
            '''
            result = self._values.get("connection_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def date_format(self) -> typing.Optional[builtins.str]:
            '''The date format that you are using.

            Valid values are ``auto`` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using ``auto`` recognizes most strings, even some that aren't supported when you use a date format string.

            If your date and time values use formats different from each other, set this to ``auto`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-dateformat
            '''
            result = self._values.get("date_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def empty_as_null(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL.

            A value of ``true`` sets empty CHAR and VARCHAR fields to null. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-emptyasnull
            '''
            result = self._values.get("empty_as_null")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The type of server-side encryption that you want to use for your data.

            This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` .
            .. epigraph::

               For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` .

            To use ``SSE_S3`` , create an AWS Identity and Access Management (IAM) role with a policy that allows ``"arn:aws:s3:::*"`` to use the following actions: ``"s3:PutObject", "s3:ListBucket"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-encryptionmode
            '''
            result = self._values.get("encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def explicit_ids(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This setting is only valid for a full-load migration task.

            Set ``ExplicitIds`` to ``true`` to have tables with ``IDENTITY`` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-explicitids
            '''
            result = self._values.get("explicit_ids")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def file_transfer_upload_streams(self) -> typing.Optional[jsii.Number]:
            '''The number of threads used to upload a single file.

            This parameter accepts a value from 1 through 64. It defaults to 10.

            The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see `Multipart upload overview <https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html>`_ .

            ``FileTransferUploadStreams`` accepts a value from 1 through 64. It defaults to 10.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-filetransferuploadstreams
            '''
            result = self._values.get("file_transfer_upload_streams")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def load_timeout(self) -> typing.Optional[jsii.Number]:
            '''The amount of time to wait (in milliseconds) before timing out of operations performed by AWS DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-loadtimeout
            '''
            result = self._values.get("load_timeout")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def map_boolean_as_boolean(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, lets Redshift migrate the boolean type as boolean.

            By default, Redshift migrates booleans as ``varchar(1)`` . You must set this setting on both the source and target endpoints for it to take effect.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-mapbooleanasboolean
            '''
            result = self._values.get("map_boolean_as_boolean")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def remove_quotes(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies to remove surrounding quotation marks from strings in the incoming data.

            All characters within the quotation marks, including delimiters, are retained. Choose ``true`` to remove quotation marks. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-removequotes
            '''
            result = self._values.get("remove_quotes")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def replace_chars(self) -> typing.Optional[builtins.str]:
            '''A value that specifies to replaces the invalid characters specified in ``ReplaceInvalidChars`` , substituting the specified characters instead.

            The default is ``"?"`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-replacechars
            '''
            result = self._values.get("replace_chars")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replace_invalid_chars(self) -> typing.Optional[builtins.str]:
            '''A list of characters that you want to replace.

            Use with ``ReplaceChars`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-replaceinvalidchars
            '''
            result = self._values.get("replace_invalid_chars")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the Amazon Redshift endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the Amazon Redshift endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The AWS KMS key ID.

            If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-serversideencryptionkmskeyid
            '''
            result = self._values.get("server_side_encryption_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service.

            The role must allow the ``iam:PassRole`` action.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def time_format(self) -> typing.Optional[builtins.str]:
            '''The time format that you want to use.

            Valid values are ``auto`` (case-sensitive), ``'timeformat_string'`` , ``'epochsecs'`` , or ``'epochmillisecs'`` . It defaults to 10. Using ``auto`` recognizes most strings, even some that aren't supported when you use a time format string.

            If your date and time values use formats different from each other, set this parameter to ``auto`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-timeformat
            '''
            result = self._values.get("time_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def trim_blanks(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies to remove the trailing white space characters from a VARCHAR string.

            This parameter applies only to columns with a VARCHAR data type. Choose ``true`` to remove unneeded white space. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-trimblanks
            '''
            result = self._values.get("trim_blanks")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def truncate_columns(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column.

            This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose ``true`` to truncate data. The default is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-truncatecolumns
            '''
            result = self._values.get("truncate_columns")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def write_buffer_size(self) -> typing.Optional[jsii.Number]:
            '''The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-redshiftsettings.html#cfn-dms-endpoint-redshiftsettings-writebuffersize
            '''
            result = self._values.get("write_buffer_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.S3SettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_column_name": "addColumnName",
            "add_trailing_padding_character": "addTrailingPaddingCharacter",
            "bucket_folder": "bucketFolder",
            "bucket_name": "bucketName",
            "canned_acl_for_objects": "cannedAclForObjects",
            "cdc_inserts_and_updates": "cdcInsertsAndUpdates",
            "cdc_inserts_only": "cdcInsertsOnly",
            "cdc_max_batch_interval": "cdcMaxBatchInterval",
            "cdc_min_file_size": "cdcMinFileSize",
            "cdc_path": "cdcPath",
            "compression_type": "compressionType",
            "csv_delimiter": "csvDelimiter",
            "csv_no_sup_value": "csvNoSupValue",
            "csv_null_value": "csvNullValue",
            "csv_row_delimiter": "csvRowDelimiter",
            "data_format": "dataFormat",
            "data_page_size": "dataPageSize",
            "date_partition_delimiter": "datePartitionDelimiter",
            "date_partition_enabled": "datePartitionEnabled",
            "date_partition_sequence": "datePartitionSequence",
            "date_partition_timezone": "datePartitionTimezone",
            "dict_page_size_limit": "dictPageSizeLimit",
            "enable_statistics": "enableStatistics",
            "encoding_type": "encodingType",
            "encryption_mode": "encryptionMode",
            "expected_bucket_owner": "expectedBucketOwner",
            "external_table_definition": "externalTableDefinition",
            "glue_catalog_generation": "glueCatalogGeneration",
            "ignore_header_rows": "ignoreHeaderRows",
            "include_op_for_full_load": "includeOpForFullLoad",
            "max_file_size": "maxFileSize",
            "parquet_timestamp_in_millisecond": "parquetTimestampInMillisecond",
            "parquet_version": "parquetVersion",
            "preserve_transactions": "preserveTransactions",
            "rfc4180": "rfc4180",
            "row_group_length": "rowGroupLength",
            "server_side_encryption_kms_key_id": "serverSideEncryptionKmsKeyId",
            "service_access_role_arn": "serviceAccessRoleArn",
            "timestamp_column_name": "timestampColumnName",
            "use_csv_no_sup_value": "useCsvNoSupValue",
            "use_task_start_time_for_full_load_timestamp": "useTaskStartTimeForFullLoadTimestamp",
        },
    )
    class S3SettingsProperty:
        def __init__(
            self,
            *,
            add_column_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            add_trailing_padding_character: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            bucket_folder: typing.Optional[builtins.str] = None,
            bucket_name: typing.Optional[builtins.str] = None,
            canned_acl_for_objects: typing.Optional[builtins.str] = None,
            cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
            cdc_min_file_size: typing.Optional[jsii.Number] = None,
            cdc_path: typing.Optional[builtins.str] = None,
            compression_type: typing.Optional[builtins.str] = None,
            csv_delimiter: typing.Optional[builtins.str] = None,
            csv_no_sup_value: typing.Optional[builtins.str] = None,
            csv_null_value: typing.Optional[builtins.str] = None,
            csv_row_delimiter: typing.Optional[builtins.str] = None,
            data_format: typing.Optional[builtins.str] = None,
            data_page_size: typing.Optional[jsii.Number] = None,
            date_partition_delimiter: typing.Optional[builtins.str] = None,
            date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            date_partition_sequence: typing.Optional[builtins.str] = None,
            date_partition_timezone: typing.Optional[builtins.str] = None,
            dict_page_size_limit: typing.Optional[jsii.Number] = None,
            enable_statistics: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encoding_type: typing.Optional[builtins.str] = None,
            encryption_mode: typing.Optional[builtins.str] = None,
            expected_bucket_owner: typing.Optional[builtins.str] = None,
            external_table_definition: typing.Optional[builtins.str] = None,
            glue_catalog_generation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ignore_header_rows: typing.Optional[jsii.Number] = None,
            include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            max_file_size: typing.Optional[jsii.Number] = None,
            parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            parquet_version: typing.Optional[builtins.str] = None,
            preserve_transactions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            rfc4180: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            row_group_length: typing.Optional[jsii.Number] = None,
            server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
            service_access_role_arn: typing.Optional[builtins.str] = None,
            timestamp_column_name: typing.Optional[builtins.str] = None,
            use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Provides information that defines an Amazon S3 endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about the available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .

            :param add_column_name: An optional parameter that, when set to ``true`` or ``y`` , you can use to add column name information to the .csv output file. The default value is ``false`` . Valid values are ``true`` , ``false`` , ``y`` , and ``n`` .
            :param add_trailing_padding_character: Use the S3 target endpoint setting ``AddTrailingPaddingCharacter`` to add padding on string data. The default value is ``false`` .
            :param bucket_folder: An optional parameter to set a folder name in the S3 bucket. If provided, tables are created in the path ``*bucketFolder* / *schema_name* / *table_name* /`` . If this parameter isn't specified, the path used is ``*schema_name* / *table_name* /`` .
            :param bucket_name: The name of the S3 bucket.
            :param canned_acl_for_objects: A value that enables AWS DMS to specify a predefined (canned) access control list (ACL) for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ in the *Amazon S3 Developer Guide* . The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.
            :param cdc_inserts_and_updates: A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is ``false`` , but when ``CdcInsertsAndUpdates`` is set to ``true`` or ``y`` , only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file. For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the ``IncludeOpForFullLoad`` parameter. If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to either ``I`` or ``U`` to indicate INSERT and UPDATE operations at the source. But if ``IncludeOpForFullLoad`` is set to ``false`` , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* . .. epigraph:: AWS DMS supports the use of the ``CdcInsertsAndUpdates`` parameter in versions 3.3.1 and later. ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.
            :param cdc_inserts_only: A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target. If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* . .. epigraph:: AWS DMS supports the interaction described preceding between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later. ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.
            :param cdc_max_batch_interval: Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3. When ``CdcMaxBatchInterval`` and ``CdcMinFileSize`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template. The default value is 60 seconds.
            :param cdc_min_file_size: Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3. When ``CdcMinFileSize`` and ``CdcMaxBatchInterval`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template. The default value is 32 MB.
            :param cdc_path: Specifies the folder path of CDC files. For an S3 source, this setting is required if a task captures change data; otherwise, it's optional. If ``CdcPath`` is set, AWS DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set ```PreserveTransactions`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-PreserveTransactions>`_ to ``true`` , AWS DMS verifies that you have set this parameter to a folder path on your S3 target where AWS DMS can save the transaction order for the CDC load. AWS DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by ```BucketFolder`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketFolder>`_ and ```BucketName`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketName>`_ . For example, if you specify ``CdcPath`` as ``MyChangedData`` , and you specify ``BucketName`` as ``MyTargetBucket`` but do not specify ``BucketFolder`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyChangedData`` . If you specify the same ``CdcPath`` , and you specify ``BucketName`` as ``MyTargetBucket`` and ``BucketFolder`` as ``MyTargetData`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyTargetData/MyChangedData`` . For more information on CDC including transaction order on an S3 target, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ . .. epigraph:: This setting is supported in AWS DMS versions 3.4.2 and later.
            :param compression_type: An optional parameter. When set to GZIP it enables the service to compress the target files. To allow the service to write the target files uncompressed, either set this parameter to NONE (the default) or don't specify the parameter at all. This parameter applies to both .csv and .parquet file formats.
            :param csv_delimiter: The delimiter used to separate columns in the .csv file for both source and target. The default is a comma.
            :param csv_no_sup_value: This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If ```UseCsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-UseCsvNoSupValue>`_ is set to true, specify a string value that you want AWS DMS to use for all columns not included in the supplemental log. If you do not specify a string value, AWS DMS uses the null value for these columns regardless of the ``UseCsvNoSupValue`` setting. .. epigraph:: This setting is supported in AWS DMS versions 3.4.1 and later.
            :param csv_null_value: An optional parameter that specifies how AWS DMS treats null values. While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are not nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string ("" or ''), AWS DMS treats the empty string as the null value instead of ``NULL`` . The default value is ``NULL`` . Valid values include any valid string.
            :param csv_row_delimiter: The delimiter used to separate rows in the .csv file for both source and target. The default is a carriage return ( ``\\n`` ).
            :param data_format: The format of the data that you want to use for output. You can choose one of the following:. - ``csv`` : This is a row-based file format with comma-separated values (.csv). - ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.
            :param data_page_size: The size of one data page in bytes. This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.
            :param date_partition_delimiter: Specifies a date separating delimiter to use during folder partitioning. The default value is ``SLASH`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .
            :param date_partition_enabled: When set to ``true`` , this parameter partitions S3 bucket folders based on transaction commit dates. The default value is ``false`` . For more information about date-based folder partitioning, see `Using date-based folder partitioning <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning>`_ .
            :param date_partition_sequence: Identifies the sequence of the date format to use during folder partitioning. The default value is ``YYYYMMDD`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .
            :param date_partition_timezone: When creating an S3 target endpoint, set ``DatePartitionTimezone`` to convert the current UTC time into a specified time zone. The conversion occurs when a date partition folder is created and a change data capture (CDC) file name is generated. The time zone format is Area/Location. Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` , as shown in the following example. ``s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":" *Asia/Seoul* ", "BucketName": "dms-nattarat-test"}'``
            :param dict_page_size_limit: The maximum size of an encoded dictionary page of a column. If the dictionary page exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.
            :param enable_statistics: A value that enables statistics for Parquet pages and row groups. Choose ``true`` to enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file format only.
            :param encoding_type: The type of encoding that you're using:. - ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default. - ``PLAIN`` doesn't use encoding at all. Values are stored as they are. - ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.
            :param encryption_mode: The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` . .. epigraph:: For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` . To use ``SSE_S3`` , you need an IAM role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the following actions: - ``s3:CreateBucket`` - ``s3:ListBucket`` - ``s3:DeleteBucket`` - ``s3:GetBucketLocation`` - ``s3:GetObject`` - ``s3:PutObject`` - ``s3:DeleteObject`` - ``s3:GetObjectVersion`` - ``s3:GetBucketPolicy`` - ``s3:PutBucketPolicy`` - ``s3:DeleteBucketPolicy``
            :param expected_bucket_owner: To specify a bucket owner and prevent sniping, you can use the ``ExpectedBucketOwner`` endpoint setting. Example: ``--s3-settings='{"ExpectedBucketOwner": " *AWS_Account_ID* "}'`` When you make a request to test a connection or perform a migration, S3 checks the account ID of the bucket owner against the specified parameter.
            :param external_table_definition: The external table definition. Conditional: If ``S3`` is used as a source then ``ExternalTableDefinition`` is required.
            :param glue_catalog_generation: When true, allows AWS Glue to catalog your S3 bucket. Creating an AWS Glue catalog lets you use Athena to query your data.
            :param ignore_header_rows: When this value is set to 1, AWS DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature. The default is 0.
            :param include_op_for_full_load: A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database. .. epigraph:: AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later. For full load, records can only be inserted. By default (the ``false`` setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load. .. epigraph:: This setting works together with the ``CdcInsertsOnly`` and the ``CdcInsertsAndUpdates`` parameters for output to .csv files only. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .
            :param max_file_size: A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load. The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.
            :param parquet_timestamp_in_millisecond: A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an Amazon S3 object file in .parquet format. .. epigraph:: AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later. When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision. Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue . .. epigraph:: AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with microsecond precision. Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp column value that is inserted by setting the ``TimestampColumnName`` parameter.
            :param parquet_version: The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or ``parquet_2_0`` .
            :param preserve_transactions: If this setting is set to ``true`` , AWS DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by ```CdcPath`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CdcPath>`_ . For more information, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ . .. epigraph:: This setting is supported in AWS DMS versions 3.4.2 and later.
            :param rfc4180: For an S3 source, when this value is set to ``true`` or ``y`` , each leading double quotation mark has to be followed by an ending double quotation mark. This formatting complies with RFC 4180. When this value is set to ``false`` or ``n`` , string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you can't use a delimiter as part of the string, because it signals the end of the value. For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to ``true`` or ``y`` using Amazon S3 as a target, if the data has quotation marks or newline characters in it, AWS DMS encloses the entire column with an additional pair of double quotation marks ("). Every quotation mark within the data is repeated twice. The default value is ``true`` . Valid values include ``true`` , ``false`` , ``y`` , and ``n`` .
            :param row_group_length: The number of rows in a row group. A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only. If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group length in bytes (64 * 1024 * 1024).
            :param server_side_encryption_kms_key_id: If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key. Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn= *value* ,BucketFolder= *value* ,BucketName= *value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId= *value*``
            :param service_access_role_arn: A required parameter that specifies the Amazon Resource Name (ARN) used by the service to access the IAM role. The role must allow the ``iam:PassRole`` action. It enables AWS DMS to read and write objects from an S3 bucket.
            :param timestamp_column_name: A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target. .. epigraph:: AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later. AWS DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your migrated data when you set ``TimestampColumnName`` to a nonblank value. For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS. For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database. The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database. When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the timestamp column that you set with ``TimestampColumnName`` .
            :param use_csv_no_sup_value: This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If this setting is set to ``true`` for columns not included in the supplemental log, AWS DMS uses the value specified by ```CsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CsvNoSupValue>`_ . If this setting isn't set or is set to ``false`` , AWS DMS uses the null value for these columns. .. epigraph:: This setting is supported in AWS DMS versions 3.4.1 and later.
            :param use_task_start_time_for_full_load_timestamp: When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target. For full load, when ``useTaskStartTimeForFullLoadTimestamp`` is set to ``true`` , each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time. When ``useTaskStartTimeForFullLoadTimestamp`` is set to ``false`` , the full load timestamp in the timestamp column increments with the time data arrives at the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                s3_settings_property = dms.CfnEndpoint.S3SettingsProperty(
                    add_column_name=False,
                    add_trailing_padding_character=False,
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    canned_acl_for_objects="cannedAclForObjects",
                    cdc_inserts_and_updates=False,
                    cdc_inserts_only=False,
                    cdc_max_batch_interval=123,
                    cdc_min_file_size=123,
                    cdc_path="cdcPath",
                    compression_type="compressionType",
                    csv_delimiter="csvDelimiter",
                    csv_no_sup_value="csvNoSupValue",
                    csv_null_value="csvNullValue",
                    csv_row_delimiter="csvRowDelimiter",
                    data_format="dataFormat",
                    data_page_size=123,
                    date_partition_delimiter="datePartitionDelimiter",
                    date_partition_enabled=False,
                    date_partition_sequence="datePartitionSequence",
                    date_partition_timezone="datePartitionTimezone",
                    dict_page_size_limit=123,
                    enable_statistics=False,
                    encoding_type="encodingType",
                    encryption_mode="encryptionMode",
                    expected_bucket_owner="expectedBucketOwner",
                    external_table_definition="externalTableDefinition",
                    glue_catalog_generation=False,
                    ignore_header_rows=123,
                    include_op_for_full_load=False,
                    max_file_size=123,
                    parquet_timestamp_in_millisecond=False,
                    parquet_version="parquetVersion",
                    preserve_transactions=False,
                    rfc4180=False,
                    row_group_length=123,
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    timestamp_column_name="timestampColumnName",
                    use_csv_no_sup_value=False,
                    use_task_start_time_for_full_load_timestamp=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf3699d4ca56a7d5e4abdba623281a4b6de1d7578f7fe1bf3add9c31bb3c33fd)
                check_type(argname="argument add_column_name", value=add_column_name, expected_type=type_hints["add_column_name"])
                check_type(argname="argument add_trailing_padding_character", value=add_trailing_padding_character, expected_type=type_hints["add_trailing_padding_character"])
                check_type(argname="argument bucket_folder", value=bucket_folder, expected_type=type_hints["bucket_folder"])
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument canned_acl_for_objects", value=canned_acl_for_objects, expected_type=type_hints["canned_acl_for_objects"])
                check_type(argname="argument cdc_inserts_and_updates", value=cdc_inserts_and_updates, expected_type=type_hints["cdc_inserts_and_updates"])
                check_type(argname="argument cdc_inserts_only", value=cdc_inserts_only, expected_type=type_hints["cdc_inserts_only"])
                check_type(argname="argument cdc_max_batch_interval", value=cdc_max_batch_interval, expected_type=type_hints["cdc_max_batch_interval"])
                check_type(argname="argument cdc_min_file_size", value=cdc_min_file_size, expected_type=type_hints["cdc_min_file_size"])
                check_type(argname="argument cdc_path", value=cdc_path, expected_type=type_hints["cdc_path"])
                check_type(argname="argument compression_type", value=compression_type, expected_type=type_hints["compression_type"])
                check_type(argname="argument csv_delimiter", value=csv_delimiter, expected_type=type_hints["csv_delimiter"])
                check_type(argname="argument csv_no_sup_value", value=csv_no_sup_value, expected_type=type_hints["csv_no_sup_value"])
                check_type(argname="argument csv_null_value", value=csv_null_value, expected_type=type_hints["csv_null_value"])
                check_type(argname="argument csv_row_delimiter", value=csv_row_delimiter, expected_type=type_hints["csv_row_delimiter"])
                check_type(argname="argument data_format", value=data_format, expected_type=type_hints["data_format"])
                check_type(argname="argument data_page_size", value=data_page_size, expected_type=type_hints["data_page_size"])
                check_type(argname="argument date_partition_delimiter", value=date_partition_delimiter, expected_type=type_hints["date_partition_delimiter"])
                check_type(argname="argument date_partition_enabled", value=date_partition_enabled, expected_type=type_hints["date_partition_enabled"])
                check_type(argname="argument date_partition_sequence", value=date_partition_sequence, expected_type=type_hints["date_partition_sequence"])
                check_type(argname="argument date_partition_timezone", value=date_partition_timezone, expected_type=type_hints["date_partition_timezone"])
                check_type(argname="argument dict_page_size_limit", value=dict_page_size_limit, expected_type=type_hints["dict_page_size_limit"])
                check_type(argname="argument enable_statistics", value=enable_statistics, expected_type=type_hints["enable_statistics"])
                check_type(argname="argument encoding_type", value=encoding_type, expected_type=type_hints["encoding_type"])
                check_type(argname="argument encryption_mode", value=encryption_mode, expected_type=type_hints["encryption_mode"])
                check_type(argname="argument expected_bucket_owner", value=expected_bucket_owner, expected_type=type_hints["expected_bucket_owner"])
                check_type(argname="argument external_table_definition", value=external_table_definition, expected_type=type_hints["external_table_definition"])
                check_type(argname="argument glue_catalog_generation", value=glue_catalog_generation, expected_type=type_hints["glue_catalog_generation"])
                check_type(argname="argument ignore_header_rows", value=ignore_header_rows, expected_type=type_hints["ignore_header_rows"])
                check_type(argname="argument include_op_for_full_load", value=include_op_for_full_load, expected_type=type_hints["include_op_for_full_load"])
                check_type(argname="argument max_file_size", value=max_file_size, expected_type=type_hints["max_file_size"])
                check_type(argname="argument parquet_timestamp_in_millisecond", value=parquet_timestamp_in_millisecond, expected_type=type_hints["parquet_timestamp_in_millisecond"])
                check_type(argname="argument parquet_version", value=parquet_version, expected_type=type_hints["parquet_version"])
                check_type(argname="argument preserve_transactions", value=preserve_transactions, expected_type=type_hints["preserve_transactions"])
                check_type(argname="argument rfc4180", value=rfc4180, expected_type=type_hints["rfc4180"])
                check_type(argname="argument row_group_length", value=row_group_length, expected_type=type_hints["row_group_length"])
                check_type(argname="argument server_side_encryption_kms_key_id", value=server_side_encryption_kms_key_id, expected_type=type_hints["server_side_encryption_kms_key_id"])
                check_type(argname="argument service_access_role_arn", value=service_access_role_arn, expected_type=type_hints["service_access_role_arn"])
                check_type(argname="argument timestamp_column_name", value=timestamp_column_name, expected_type=type_hints["timestamp_column_name"])
                check_type(argname="argument use_csv_no_sup_value", value=use_csv_no_sup_value, expected_type=type_hints["use_csv_no_sup_value"])
                check_type(argname="argument use_task_start_time_for_full_load_timestamp", value=use_task_start_time_for_full_load_timestamp, expected_type=type_hints["use_task_start_time_for_full_load_timestamp"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_column_name is not None:
                self._values["add_column_name"] = add_column_name
            if add_trailing_padding_character is not None:
                self._values["add_trailing_padding_character"] = add_trailing_padding_character
            if bucket_folder is not None:
                self._values["bucket_folder"] = bucket_folder
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if canned_acl_for_objects is not None:
                self._values["canned_acl_for_objects"] = canned_acl_for_objects
            if cdc_inserts_and_updates is not None:
                self._values["cdc_inserts_and_updates"] = cdc_inserts_and_updates
            if cdc_inserts_only is not None:
                self._values["cdc_inserts_only"] = cdc_inserts_only
            if cdc_max_batch_interval is not None:
                self._values["cdc_max_batch_interval"] = cdc_max_batch_interval
            if cdc_min_file_size is not None:
                self._values["cdc_min_file_size"] = cdc_min_file_size
            if cdc_path is not None:
                self._values["cdc_path"] = cdc_path
            if compression_type is not None:
                self._values["compression_type"] = compression_type
            if csv_delimiter is not None:
                self._values["csv_delimiter"] = csv_delimiter
            if csv_no_sup_value is not None:
                self._values["csv_no_sup_value"] = csv_no_sup_value
            if csv_null_value is not None:
                self._values["csv_null_value"] = csv_null_value
            if csv_row_delimiter is not None:
                self._values["csv_row_delimiter"] = csv_row_delimiter
            if data_format is not None:
                self._values["data_format"] = data_format
            if data_page_size is not None:
                self._values["data_page_size"] = data_page_size
            if date_partition_delimiter is not None:
                self._values["date_partition_delimiter"] = date_partition_delimiter
            if date_partition_enabled is not None:
                self._values["date_partition_enabled"] = date_partition_enabled
            if date_partition_sequence is not None:
                self._values["date_partition_sequence"] = date_partition_sequence
            if date_partition_timezone is not None:
                self._values["date_partition_timezone"] = date_partition_timezone
            if dict_page_size_limit is not None:
                self._values["dict_page_size_limit"] = dict_page_size_limit
            if enable_statistics is not None:
                self._values["enable_statistics"] = enable_statistics
            if encoding_type is not None:
                self._values["encoding_type"] = encoding_type
            if encryption_mode is not None:
                self._values["encryption_mode"] = encryption_mode
            if expected_bucket_owner is not None:
                self._values["expected_bucket_owner"] = expected_bucket_owner
            if external_table_definition is not None:
                self._values["external_table_definition"] = external_table_definition
            if glue_catalog_generation is not None:
                self._values["glue_catalog_generation"] = glue_catalog_generation
            if ignore_header_rows is not None:
                self._values["ignore_header_rows"] = ignore_header_rows
            if include_op_for_full_load is not None:
                self._values["include_op_for_full_load"] = include_op_for_full_load
            if max_file_size is not None:
                self._values["max_file_size"] = max_file_size
            if parquet_timestamp_in_millisecond is not None:
                self._values["parquet_timestamp_in_millisecond"] = parquet_timestamp_in_millisecond
            if parquet_version is not None:
                self._values["parquet_version"] = parquet_version
            if preserve_transactions is not None:
                self._values["preserve_transactions"] = preserve_transactions
            if rfc4180 is not None:
                self._values["rfc4180"] = rfc4180
            if row_group_length is not None:
                self._values["row_group_length"] = row_group_length
            if server_side_encryption_kms_key_id is not None:
                self._values["server_side_encryption_kms_key_id"] = server_side_encryption_kms_key_id
            if service_access_role_arn is not None:
                self._values["service_access_role_arn"] = service_access_role_arn
            if timestamp_column_name is not None:
                self._values["timestamp_column_name"] = timestamp_column_name
            if use_csv_no_sup_value is not None:
                self._values["use_csv_no_sup_value"] = use_csv_no_sup_value
            if use_task_start_time_for_full_load_timestamp is not None:
                self._values["use_task_start_time_for_full_load_timestamp"] = use_task_start_time_for_full_load_timestamp

        @builtins.property
        def add_column_name(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''An optional parameter that, when set to ``true`` or ``y`` , you can use to add column name information to the .csv output file.

            The default value is ``false`` . Valid values are ``true`` , ``false`` , ``y`` , and ``n`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-addcolumnname
            '''
            result = self._values.get("add_column_name")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def add_trailing_padding_character(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Use the S3 target endpoint setting ``AddTrailingPaddingCharacter`` to add padding on string data.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-addtrailingpaddingcharacter
            '''
            result = self._values.get("add_trailing_padding_character")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def bucket_folder(self) -> typing.Optional[builtins.str]:
            '''An optional parameter to set a folder name in the S3 bucket.

            If provided, tables are created in the path ``*bucketFolder* / *schema_name* / *table_name* /`` . If this parameter isn't specified, the path used is ``*schema_name* / *table_name* /`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-bucketfolder
            '''
            result = self._values.get("bucket_folder")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def canned_acl_for_objects(self) -> typing.Optional[builtins.str]:
            '''A value that enables AWS DMS to specify a predefined (canned) access control list (ACL) for objects created in an Amazon S3 bucket as .csv or .parquet files. For more information about Amazon S3 canned ACLs, see `Canned ACL <https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl>`_ in the *Amazon S3 Developer Guide* .

            The default value is NONE. Valid values include NONE, PRIVATE, PUBLIC_READ, PUBLIC_READ_WRITE, AUTHENTICATED_READ, AWS_EXEC_READ, BUCKET_OWNER_READ, and BUCKET_OWNER_FULL_CONTROL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cannedaclforobjects
            '''
            result = self._values.get("canned_acl_for_objects")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cdc_inserts_and_updates(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that enables a change data capture (CDC) load to write INSERT and UPDATE operations to .csv or .parquet (columnar storage) output files. The default setting is ``false`` , but when ``CdcInsertsAndUpdates`` is set to ``true`` or ``y`` , only INSERTs and UPDATEs from the source database are migrated to the .csv or .parquet file.

            For .csv file format only, how these INSERTs and UPDATEs are recorded depends on the value of the ``IncludeOpForFullLoad`` parameter. If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to either ``I`` or ``U`` to indicate INSERT and UPDATE operations at the source. But if ``IncludeOpForFullLoad`` is set to ``false`` , CDC records are written without an indication of INSERT or UPDATE operations at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .
            .. epigraph::

               AWS DMS supports the use of the ``CdcInsertsAndUpdates`` parameter in versions 3.3.1 and later.

               ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcinsertsandupdates
            '''
            result = self._values.get("cdc_inserts_and_updates")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def cdc_inserts_only(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that enables a change data capture (CDC) load to write only INSERT operations to .csv or columnar storage (.parquet) output files. By default (the ``false`` setting), the first field in a .csv or .parquet record contains the letter I (INSERT), U (UPDATE), or D (DELETE). These values indicate whether the row was inserted, updated, or deleted at the source database for a CDC load to the target.

            If ``CdcInsertsOnly`` is set to ``true`` or ``y`` , only INSERTs from the source database are migrated to the .csv or .parquet file. For .csv format only, how these INSERTs are recorded depends on the value of ``IncludeOpForFullLoad`` . If ``IncludeOpForFullLoad`` is set to ``true`` , the first field of every CDC record is set to I to indicate the INSERT operation at the source. If ``IncludeOpForFullLoad`` is set to ``false`` , every CDC record is written without a first field to indicate the INSERT operation at the source. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .
            .. epigraph::

               AWS DMS supports the interaction described preceding between the ``CdcInsertsOnly`` and ``IncludeOpForFullLoad`` parameters in versions 3.1.4 and later.

               ``CdcInsertsOnly`` and ``CdcInsertsAndUpdates`` can't both be set to ``true`` for the same endpoint. Set either ``CdcInsertsOnly`` or ``CdcInsertsAndUpdates`` to ``true`` for the same endpoint, but not both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcinsertsonly
            '''
            result = self._values.get("cdc_inserts_only")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def cdc_max_batch_interval(self) -> typing.Optional[jsii.Number]:
            '''Maximum length of the interval, defined in seconds, after which to output a file to Amazon S3.

            When ``CdcMaxBatchInterval`` and ``CdcMinFileSize`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template.

            The default value is 60 seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcmaxbatchinterval
            '''
            result = self._values.get("cdc_max_batch_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def cdc_min_file_size(self) -> typing.Optional[jsii.Number]:
            '''Minimum file size, defined in kilobytes, to reach for a file output to Amazon S3.

            When ``CdcMinFileSize`` and ``CdcMaxBatchInterval`` are both specified, the file write is triggered by whichever parameter condition is met first within an AWS DMS CloudFormation template.

            The default value is 32 MB.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcminfilesize
            '''
            result = self._values.get("cdc_min_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def cdc_path(self) -> typing.Optional[builtins.str]:
            '''Specifies the folder path of CDC files.

            For an S3 source, this setting is required if a task captures change data; otherwise, it's optional. If ``CdcPath`` is set, AWS DMS reads CDC files from this path and replicates the data changes to the target endpoint. For an S3 target if you set ```PreserveTransactions`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-PreserveTransactions>`_ to ``true`` , AWS DMS verifies that you have set this parameter to a folder path on your S3 target where AWS DMS can save the transaction order for the CDC load. AWS DMS creates this CDC folder path in either your S3 target working directory or the S3 target location specified by ```BucketFolder`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketFolder>`_ and ```BucketName`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-BucketName>`_ .

            For example, if you specify ``CdcPath`` as ``MyChangedData`` , and you specify ``BucketName`` as ``MyTargetBucket`` but do not specify ``BucketFolder`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyChangedData`` .

            If you specify the same ``CdcPath`` , and you specify ``BucketName`` as ``MyTargetBucket`` and ``BucketFolder`` as ``MyTargetData`` , AWS DMS creates the CDC folder path following: ``MyTargetBucket/MyTargetData/MyChangedData`` .

            For more information on CDC including transaction order on an S3 target, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ .
            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.2 and later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-cdcpath
            '''
            result = self._values.get("cdc_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def compression_type(self) -> typing.Optional[builtins.str]:
            '''An optional parameter.

            When set to GZIP it enables the service to compress the target files. To allow the service to write the target files uncompressed, either set this parameter to NONE (the default) or don't specify the parameter at all. This parameter applies to both .csv and .parquet file formats.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-compressiontype
            '''
            result = self._values.get("compression_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter used to separate columns in the .csv file for both source and target. The default is a comma.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvdelimiter
            '''
            result = self._values.get("csv_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_no_sup_value(self) -> typing.Optional[builtins.str]:
            '''This setting only applies if your Amazon S3 output files during a change data capture (CDC) load are written in .csv format. If ```UseCsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-UseCsvNoSupValue>`_ is set to true, specify a string value that you want AWS DMS to use for all columns not included in the supplemental log. If you do not specify a string value, AWS DMS uses the null value for these columns regardless of the ``UseCsvNoSupValue`` setting.

            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.1 and later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvnosupvalue
            '''
            result = self._values.get("csv_no_sup_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_null_value(self) -> typing.Optional[builtins.str]:
            '''An optional parameter that specifies how AWS DMS treats null values.

            While handling the null value, you can use this parameter to pass a user-defined string as null when writing to the target. For example, when target columns are not nullable, you can use this option to differentiate between the empty string value and the null value. So, if you set this parameter value to the empty string ("" or ''), AWS DMS treats the empty string as the null value instead of ``NULL`` .

            The default value is ``NULL`` . Valid values include any valid string.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvnullvalue
            '''
            result = self._values.get("csv_null_value")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def csv_row_delimiter(self) -> typing.Optional[builtins.str]:
            '''The delimiter used to separate rows in the .csv file for both source and target.

            The default is a carriage return ( ``\\n`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-csvrowdelimiter
            '''
            result = self._values.get("csv_row_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_format(self) -> typing.Optional[builtins.str]:
            '''The format of the data that you want to use for output. You can choose one of the following:.

            - ``csv`` : This is a row-based file format with comma-separated values (.csv).
            - ``parquet`` : Apache Parquet (.parquet) is a columnar storage file format that features efficient compression and provides faster query response.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-dataformat
            '''
            result = self._values.get("data_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_page_size(self) -> typing.Optional[jsii.Number]:
            '''The size of one data page in bytes.

            This parameter defaults to 1024 * 1024 bytes (1 MiB). This number is used for .parquet file format only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datapagesize
            '''
            result = self._values.get("data_page_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def date_partition_delimiter(self) -> typing.Optional[builtins.str]:
            '''Specifies a date separating delimiter to use during folder partitioning.

            The default value is ``SLASH`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitiondelimiter
            '''
            result = self._values.get("date_partition_delimiter")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_partition_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to ``true`` , this parameter partitions S3 bucket folders based on transaction commit dates.

            The default value is ``false`` . For more information about date-based folder partitioning, see `Using date-based folder partitioning <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.DatePartitioning>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitionenabled
            '''
            result = self._values.get("date_partition_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def date_partition_sequence(self) -> typing.Optional[builtins.str]:
            '''Identifies the sequence of the date format to use during folder partitioning.

            The default value is ``YYYYMMDD`` . Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitionsequence
            '''
            result = self._values.get("date_partition_sequence")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def date_partition_timezone(self) -> typing.Optional[builtins.str]:
            '''When creating an S3 target endpoint, set ``DatePartitionTimezone`` to convert the current UTC time into a specified time zone.

            The conversion occurs when a date partition folder is created and a change data capture (CDC) file name is generated. The time zone format is Area/Location. Use this parameter when ``DatePartitionedEnabled`` is set to ``true`` , as shown in the following example.

            ``s3-settings='{"DatePartitionEnabled": true, "DatePartitionSequence": "YYYYMMDDHH", "DatePartitionDelimiter": "SLASH", "DatePartitionTimezone":" *Asia/Seoul* ", "BucketName": "dms-nattarat-test"}'``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-datepartitiontimezone
            '''
            result = self._values.get("date_partition_timezone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dict_page_size_limit(self) -> typing.Optional[jsii.Number]:
            '''The maximum size of an encoded dictionary page of a column.

            If the dictionary page exceeds this, this column is stored using an encoding type of ``PLAIN`` . This parameter defaults to 1024 * 1024 bytes (1 MiB), the maximum size of a dictionary page before it reverts to ``PLAIN`` encoding. This size is used for .parquet file format only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-dictpagesizelimit
            '''
            result = self._values.get("dict_page_size_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enable_statistics(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that enables statistics for Parquet pages and row groups.

            Choose ``true`` to enable statistics, ``false`` to disable. Statistics include ``NULL`` , ``DISTINCT`` , ``MAX`` , and ``MIN`` values. This parameter defaults to ``true`` . This value is used for .parquet file format only.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-enablestatistics
            '''
            result = self._values.get("enable_statistics")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encoding_type(self) -> typing.Optional[builtins.str]:
            '''The type of encoding that you're using:.

            - ``RLE_DICTIONARY`` uses a combination of bit-packing and run-length encoding to store repeated values more efficiently. This is the default.
            - ``PLAIN`` doesn't use encoding at all. Values are stored as they are.
            - ``PLAIN_DICTIONARY`` builds a dictionary of the values encountered in a given column. The dictionary is stored in a dictionary page for each column chunk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-encodingtype
            '''
            result = self._values.get("encoding_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def encryption_mode(self) -> typing.Optional[builtins.str]:
            '''The type of server-side encryption that you want to use for your data.

            This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either ``SSE_S3`` (the default) or ``SSE_KMS`` .
            .. epigraph::

               For the ``ModifyEndpoint`` operation, you can change the existing value of the ``EncryptionMode`` parameter from ``SSE_KMS`` to ``SSE_S3`` . But you can’t change the existing value from ``SSE_S3`` to ``SSE_KMS`` .

            To use ``SSE_S3`` , you need an IAM role with permission to allow ``"arn:aws:s3:::dms-*"`` to use the following actions:

            - ``s3:CreateBucket``
            - ``s3:ListBucket``
            - ``s3:DeleteBucket``
            - ``s3:GetBucketLocation``
            - ``s3:GetObject``
            - ``s3:PutObject``
            - ``s3:DeleteObject``
            - ``s3:GetObjectVersion``
            - ``s3:GetBucketPolicy``
            - ``s3:PutBucketPolicy``
            - ``s3:DeleteBucketPolicy``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-encryptionmode
            '''
            result = self._values.get("encryption_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def expected_bucket_owner(self) -> typing.Optional[builtins.str]:
            '''To specify a bucket owner and prevent sniping, you can use the ``ExpectedBucketOwner`` endpoint setting.

            Example: ``--s3-settings='{"ExpectedBucketOwner": " *AWS_Account_ID* "}'``

            When you make a request to test a connection or perform a migration, S3 checks the account ID of the bucket owner against the specified parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-expectedbucketowner
            '''
            result = self._values.get("expected_bucket_owner")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def external_table_definition(self) -> typing.Optional[builtins.str]:
            '''The external table definition.

            Conditional: If ``S3`` is used as a source then ``ExternalTableDefinition`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-externaltabledefinition
            '''
            result = self._values.get("external_table_definition")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def glue_catalog_generation(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When true, allows AWS Glue to catalog your S3 bucket.

            Creating an AWS Glue catalog lets you use Athena to query your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-gluecataloggeneration
            '''
            result = self._values.get("glue_catalog_generation")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ignore_header_rows(self) -> typing.Optional[jsii.Number]:
            '''When this value is set to 1, AWS DMS ignores the first row header in a .csv file. A value of 1 turns on the feature; a value of 0 turns off the feature.

            The default is 0.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-ignoreheaderrows
            '''
            result = self._values.get("ignore_header_rows")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def include_op_for_full_load(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that enables a full load to write INSERT operations to the comma-separated value (.csv) output files only to indicate how the rows were added to the source database.

            .. epigraph::

               AWS DMS supports the ``IncludeOpForFullLoad`` parameter in versions 3.1.4 and later.

            For full load, records can only be inserted. By default (the ``false`` setting), no information is recorded in these output files for a full load to indicate that the rows were inserted at the source database. If ``IncludeOpForFullLoad`` is set to ``true`` or ``y`` , the INSERT is recorded as an I annotation in the first field of the .csv file. This allows the format of your target records from a full load to be consistent with the target records from a CDC load.
            .. epigraph::

               This setting works together with the ``CdcInsertsOnly`` and the ``CdcInsertsAndUpdates`` parameters for output to .csv files only. For more information about how these settings work together, see `Indicating Source DB Operations in Migrated S3 Data <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring.InsertOps>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-includeopforfullload
            '''
            result = self._values.get("include_op_for_full_load")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def max_file_size(self) -> typing.Optional[jsii.Number]:
            '''A value that specifies the maximum size (in KB) of any .csv file to be created while migrating to an S3 target during full load.

            The default value is 1,048,576 KB (1 GB). Valid values include 1 to 1,048,576.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-maxfilesize
            '''
            result = self._values.get("max_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parquet_timestamp_in_millisecond(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''A value that specifies the precision of any ``TIMESTAMP`` column values that are written to an Amazon S3 object file in .parquet format.

            .. epigraph::

               AWS DMS supports the ``ParquetTimestampInMillisecond`` parameter in versions 3.1.4 and later.

            When ``ParquetTimestampInMillisecond`` is set to ``true`` or ``y`` , AWS DMS writes all ``TIMESTAMP`` columns in a .parquet formatted file with millisecond precision. Otherwise, DMS writes them with microsecond precision.

            Currently, Amazon Athena and AWS Glue can handle only millisecond precision for ``TIMESTAMP`` values. Set this parameter to ``true`` for S3 endpoint object files that are .parquet formatted only if you plan to query or process the data with Athena or AWS Glue .
            .. epigraph::

               AWS DMS writes any ``TIMESTAMP`` column values written to an S3 file in .csv format with microsecond precision.

               Setting ``ParquetTimestampInMillisecond`` has no effect on the string format of the timestamp column value that is inserted by setting the ``TimestampColumnName`` parameter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-parquettimestampinmillisecond
            '''
            result = self._values.get("parquet_timestamp_in_millisecond")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def parquet_version(self) -> typing.Optional[builtins.str]:
            '''The version of the Apache Parquet format that you want to use: ``parquet_1_0`` (the default) or ``parquet_2_0`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-parquetversion
            '''
            result = self._values.get("parquet_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def preserve_transactions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If this setting is set to ``true`` , AWS DMS saves the transaction order for a change data capture (CDC) load on the Amazon S3 target specified by ```CdcPath`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CdcPath>`_ . For more information, see `Capturing data changes (CDC) including transaction order on the S3 target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.EndpointSettings.CdcPath>`_ .

            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.2 and later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-preservetransactions
            '''
            result = self._values.get("preserve_transactions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def rfc4180(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''For an S3 source, when this value is set to ``true`` or ``y`` , each leading double quotation mark has to be followed by an ending double quotation mark.

            This formatting complies with RFC 4180. When this value is set to ``false`` or ``n`` , string literals are copied to the target as is. In this case, a delimiter (row or column) signals the end of the field. Thus, you can't use a delimiter as part of the string, because it signals the end of the value.

            For an S3 target, an optional parameter used to set behavior to comply with RFC 4180 for data migrated to Amazon S3 using .csv file format only. When this value is set to ``true`` or ``y`` using Amazon S3 as a target, if the data has quotation marks or newline characters in it, AWS DMS encloses the entire column with an additional pair of double quotation marks ("). Every quotation mark within the data is repeated twice.

            The default value is ``true`` . Valid values include ``true`` , ``false`` , ``y`` , and ``n`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-rfc4180
            '''
            result = self._values.get("rfc4180")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def row_group_length(self) -> typing.Optional[jsii.Number]:
            '''The number of rows in a row group.

            A smaller row group size provides faster reads. But as the number of row groups grows, the slower writes become. This parameter defaults to 10,000 rows. This number is used for .parquet file format only.

            If you choose a value larger than the maximum, ``RowGroupLength`` is set to the max row group length in bytes (64 * 1024 * 1024).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-rowgrouplength
            '''
            result = self._values.get("row_group_length")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def server_side_encryption_kms_key_id(self) -> typing.Optional[builtins.str]:
            '''If you are using ``SSE_KMS`` for the ``EncryptionMode`` , provide the AWS KMS key ID.

            The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.

            Here is a CLI example: ``aws dms create-endpoint --endpoint-identifier *value* --endpoint-type target --engine-name s3 --s3-settings ServiceAccessRoleArn= *value* ,BucketFolder= *value* ,BucketName= *value* ,EncryptionMode=SSE_KMS,ServerSideEncryptionKmsKeyId= *value*``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-serversideencryptionkmskeyid
            '''
            result = self._values.get("server_side_encryption_kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''A required parameter that specifies the Amazon Resource Name (ARN) used by the service to access the IAM role.

            The role must allow the ``iam:PassRole`` action. It enables AWS DMS to read and write objects from an S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-serviceaccessrolearn
            '''
            result = self._values.get("service_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timestamp_column_name(self) -> typing.Optional[builtins.str]:
            '''A value that when nonblank causes AWS DMS to add a column with timestamp information to the endpoint data for an Amazon S3 target.

            .. epigraph::

               AWS DMS supports the ``TimestampColumnName`` parameter in versions 3.1.4 and later.

            AWS DMS includes an additional ``STRING`` column in the .csv or .parquet object files of your migrated data when you set ``TimestampColumnName`` to a nonblank value.

            For a full load, each row of this timestamp column contains a timestamp for when the data was transferred from the source to the target by DMS.

            For a change data capture (CDC) load, each row of the timestamp column contains the timestamp for the commit of that row in the source database.

            The string format for this timestamp column value is ``yyyy-MM-dd HH:mm:ss.SSSSSS`` . By default, the precision of this value is in microseconds. For a CDC load, the rounding of the precision depends on the commit timestamp supported by DMS for the source database.

            When the ``AddColumnName`` parameter is set to ``true`` , DMS also includes a name for the timestamp column that you set with ``TimestampColumnName`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-timestampcolumnname
            '''
            result = self._values.get("timestamp_column_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def use_csv_no_sup_value(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''This setting applies if the S3 output files during a change data capture (CDC) load are written in .csv format. If this setting is set to ``true`` for columns not included in the supplemental log, AWS DMS uses the value specified by ```CsvNoSupValue`` <https://docs.aws.amazon.com/dms/latest/APIReference/API_S3Settings.html#DMS-Type-S3Settings-CsvNoSupValue>`_ . If this setting isn't set or is set to ``false`` , AWS DMS uses the null value for these columns.

            .. epigraph::

               This setting is supported in AWS DMS versions 3.4.1 and later.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-usecsvnosupvalue
            '''
            result = self._values.get("use_csv_no_sup_value")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_task_start_time_for_full_load_timestamp(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''When set to true, this parameter uses the task start time as the timestamp column value instead of the time data is written to target.

            For full load, when ``useTaskStartTimeForFullLoadTimestamp`` is set to ``true`` , each row of the timestamp column contains the task start time. For CDC loads, each row of the timestamp column contains the transaction commit time.

            When ``useTaskStartTimeForFullLoadTimestamp`` is set to ``false`` , the full load timestamp in the timestamp column increments with the time data arrives at the target.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-s3settings.html#cfn-dms-endpoint-s3settings-usetaskstarttimeforfullloadtimestamp
            '''
            result = self._values.get("use_task_start_time_for_full_load_timestamp")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnEndpoint.SybaseSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
        },
    )
    class SybaseSettingsProperty:
        def __init__(
            self,
            *,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Provides information that defines a SAP ASE endpoint.

            This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

            :param secrets_manager_access_role_arn: The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` . The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SAP ASE endpoint. .. epigraph:: You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both. For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .
            :param secrets_manager_secret_id: The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the SAP SAE endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                sybase_settings_property = dms.CfnEndpoint.SybaseSettingsProperty(
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e0193ec81432f45bd3d781189917549ea6b46383bd54edb4ce2f3cd3f08b07b4)
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in ``SecretsManagerSecret`` .

            The role must allow the ``iam:PassRole`` action. ``SecretsManagerSecret`` has the value of the AWS Secrets Manager secret that allows access to the SAP ASE endpoint.
            .. epigraph::

               You can specify one of two sets of values for these permissions. You can specify the values for this setting and ``SecretsManagerSecretId`` . Or you can specify clear-text values for ``UserName`` , ``Password`` , ``ServerName`` , and ``Port`` . You can't specify both.

               For more information on creating this ``SecretsManagerSecret`` , the corresponding ``SecretsManagerAccessRoleArn`` , and the ``SecretsManagerSecretId`` that is required to access it, see `Using secrets to access AWS Database Migration Service resources <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager>`_ in the *AWS Database Migration Service User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html#cfn-dms-endpoint-sybasesettings-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The full ARN, partial ARN, or display name of the ``SecretsManagerSecret`` that contains the SAP SAE endpoint connection details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-endpoint-sybasesettings.html#cfn-dms-endpoint-sybasesettings-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SybaseSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnEndpointProps",
    jsii_struct_bases=[],
    name_mapping={
        "endpoint_type": "endpointType",
        "engine_name": "engineName",
        "certificate_arn": "certificateArn",
        "database_name": "databaseName",
        "doc_db_settings": "docDbSettings",
        "dynamo_db_settings": "dynamoDbSettings",
        "elasticsearch_settings": "elasticsearchSettings",
        "endpoint_identifier": "endpointIdentifier",
        "extra_connection_attributes": "extraConnectionAttributes",
        "gcp_my_sql_settings": "gcpMySqlSettings",
        "ibm_db2_settings": "ibmDb2Settings",
        "kafka_settings": "kafkaSettings",
        "kinesis_settings": "kinesisSettings",
        "kms_key_id": "kmsKeyId",
        "microsoft_sql_server_settings": "microsoftSqlServerSettings",
        "mongo_db_settings": "mongoDbSettings",
        "my_sql_settings": "mySqlSettings",
        "neptune_settings": "neptuneSettings",
        "oracle_settings": "oracleSettings",
        "password": "password",
        "port": "port",
        "postgre_sql_settings": "postgreSqlSettings",
        "redis_settings": "redisSettings",
        "redshift_settings": "redshiftSettings",
        "resource_identifier": "resourceIdentifier",
        "s3_settings": "s3Settings",
        "server_name": "serverName",
        "ssl_mode": "sslMode",
        "sybase_settings": "sybaseSettings",
        "tags": "tags",
        "username": "username",
    },
)
class CfnEndpointProps:
    def __init__(
        self,
        *,
        endpoint_type: builtins.str,
        engine_name: builtins.str,
        certificate_arn: typing.Optional[builtins.str] = None,
        database_name: typing.Optional[builtins.str] = None,
        doc_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.DocDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dynamo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.DynamoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        elasticsearch_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        endpoint_identifier: typing.Optional[builtins.str] = None,
        extra_connection_attributes: typing.Optional[builtins.str] = None,
        gcp_my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ibm_db2_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.IbmDb2SettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kafka_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.KafkaSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kinesis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.KinesisSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        microsoft_sql_server_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        mongo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MongoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MySqlSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        neptune_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.NeptuneSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        oracle_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.OracleSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        password: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        postgre_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        redis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.RedisSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        redshift_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.RedshiftSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        s3_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.S3SettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        server_name: typing.Optional[builtins.str] = None,
        ssl_mode: typing.Optional[builtins.str] = None,
        sybase_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.SybaseSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        username: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnEndpoint``.

        :param endpoint_type: The type of endpoint. Valid values are ``source`` and ``target`` .
        :param engine_name: The type of engine for the endpoint, depending on the ``EndpointType`` value. *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``redshift-serverless`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``
        :param certificate_arn: The Amazon Resource Name (ARN) for the certificate.
        :param database_name: The name of the endpoint database. For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .
        :param doc_db_settings: Settings in JSON format for the source and target DocumentDB endpoint. For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .
        :param dynamo_db_settings: Settings in JSON format for the target Amazon DynamoDB endpoint. For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param elasticsearch_settings: Settings in JSON format for the target OpenSearch endpoint. For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param endpoint_identifier: The database endpoint identifier. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param extra_connection_attributes: Additional attributes associated with the connection. Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .
        :param gcp_my_sql_settings: Settings in JSON format for the source GCP MySQL endpoint. These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param ibm_db2_settings: Settings in JSON format for the source IBM Db2 LUW endpoint. For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param kafka_settings: Settings in JSON format for the target Apache Kafka endpoint. For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kinesis_settings: Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams. For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param microsoft_sql_server_settings: Settings in JSON format for the source and target Microsoft SQL Server endpoint. For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param mongo_db_settings: Settings in JSON format for the source MongoDB endpoint. For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .
        :param my_sql_settings: Settings in JSON format for the source and target MySQL endpoint. For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param neptune_settings: Settings in JSON format for the target Amazon Neptune endpoint. For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param oracle_settings: Settings in JSON format for the source and target Oracle endpoint. For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param password: The password to be used to log in to the endpoint database.
        :param port: The port used by the endpoint database.
        :param postgre_sql_settings: Settings in JSON format for the source and target PostgreSQL endpoint. For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param redis_settings: Settings in JSON format for the target Redis endpoint. For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .
        :param redshift_settings: Settings in JSON format for the Amazon Redshift endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param s3_settings: Settings in JSON format for the source and target Amazon S3 endpoint. For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .
        :param server_name: The name of the server where the endpoint database resides.
        :param ssl_mode: The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` . .. epigraph:: When ``engine_name`` is set to S3, the only allowed value is ``none`` .
        :param sybase_settings: Settings in JSON format for the source and target SAP ASE endpoint. For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param tags: One or more tags to be assigned to the endpoint.
        :param username: The user name to be used to log in to the endpoint database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_endpoint_props = dms.CfnEndpointProps(
                endpoint_type="endpointType",
                engine_name="engineName",
            
                # the properties below are optional
                certificate_arn="certificateArn",
                database_name="databaseName",
                doc_db_settings=dms.CfnEndpoint.DocDbSettingsProperty(
                    docs_to_investigate=123,
                    extract_doc_id=False,
                    nesting_level="nestingLevel",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                ),
                dynamo_db_settings=dms.CfnEndpoint.DynamoDbSettingsProperty(
                    service_access_role_arn="serviceAccessRoleArn"
                ),
                elasticsearch_settings=dms.CfnEndpoint.ElasticsearchSettingsProperty(
                    endpoint_uri="endpointUri",
                    error_retry_duration=123,
                    full_load_error_percentage=123,
                    service_access_role_arn="serviceAccessRoleArn"
                ),
                endpoint_identifier="endpointIdentifier",
                extra_connection_attributes="extraConnectionAttributes",
                gcp_my_sql_settings=dms.CfnEndpoint.GcpMySQLSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    database_name="databaseName",
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    server_timezone="serverTimezone",
                    username="username"
                ),
                ibm_db2_settings=dms.CfnEndpoint.IbmDb2SettingsProperty(
                    current_lsn="currentLsn",
                    keep_csv_files=False,
                    load_timeout=123,
                    max_file_size=123,
                    max_kBytes_per_read=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    set_data_capture_changes=False,
                    write_buffer_size=123
                ),
                kafka_settings=dms.CfnEndpoint.KafkaSettingsProperty(
                    broker="broker",
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    message_max_bytes=123,
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    sasl_password="saslPassword",
                    sasl_user_name="saslUserName",
                    security_protocol="securityProtocol",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_client_certificate_arn="sslClientCertificateArn",
                    ssl_client_key_arn="sslClientKeyArn",
                    ssl_client_key_password="sslClientKeyPassword",
                    topic="topic"
                ),
                kinesis_settings=dms.CfnEndpoint.KinesisSettingsProperty(
                    include_control_details=False,
                    include_null_and_empty=False,
                    include_partition_value=False,
                    include_table_alter_operations=False,
                    include_transaction_details=False,
                    message_format="messageFormat",
                    no_hex_prefix=False,
                    partition_include_schema_table=False,
                    service_access_role_arn="serviceAccessRoleArn",
                    stream_arn="streamArn"
                ),
                kms_key_id="kmsKeyId",
                microsoft_sql_server_settings=dms.CfnEndpoint.MicrosoftSqlServerSettingsProperty(
                    bcp_packet_size=123,
                    control_tables_file_group="controlTablesFileGroup",
                    database_name="databaseName",
                    force_lob_lookup=False,
                    password="password",
                    port=123,
                    query_single_always_on_node=False,
                    read_backup_only=False,
                    safeguard_policy="safeguardPolicy",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    tlog_access_mode="tlogAccessMode",
                    trim_space_in_char=False,
                    use_bcp_full_load=False,
                    username="username",
                    use_third_party_backup_device=False
                ),
                mongo_db_settings=dms.CfnEndpoint.MongoDbSettingsProperty(
                    auth_mechanism="authMechanism",
                    auth_source="authSource",
                    auth_type="authType",
                    database_name="databaseName",
                    docs_to_investigate="docsToInvestigate",
                    extract_doc_id="extractDocId",
                    nesting_level="nestingLevel",
                    password="password",
                    port=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_name="serverName",
                    username="username"
                ),
                my_sql_settings=dms.CfnEndpoint.MySqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    clean_source_metadata_on_mismatch=False,
                    events_poll_interval=123,
                    max_file_size=123,
                    parallel_load_threads=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_timezone="serverTimezone",
                    target_db_type="targetDbType"
                ),
                neptune_settings=dms.CfnEndpoint.NeptuneSettingsProperty(
                    error_retry_duration=123,
                    iam_auth_enabled=False,
                    max_file_size=123,
                    max_retry_count=123,
                    s3_bucket_folder="s3BucketFolder",
                    s3_bucket_name="s3BucketName",
                    service_access_role_arn="serviceAccessRoleArn"
                ),
                oracle_settings=dms.CfnEndpoint.OracleSettingsProperty(
                    access_alternate_directly=False,
                    additional_archived_log_dest_id=123,
                    add_supplemental_logging=False,
                    allow_select_nested_tables=False,
                    archived_log_dest_id=123,
                    archived_logs_only=False,
                    asm_password="asmPassword",
                    asm_server="asmServer",
                    asm_user="asmUser",
                    char_length_semantics="charLengthSemantics",
                    direct_path_no_log=False,
                    direct_path_parallel_load=False,
                    enable_homogenous_tablespace=False,
                    extra_archived_log_dest_ids=[123],
                    fail_tasks_on_lob_truncation=False,
                    number_datatype_scale=123,
                    oracle_path_prefix="oraclePathPrefix",
                    parallel_asm_read_threads=123,
                    read_ahead_blocks=123,
                    read_table_space_name=False,
                    replace_path_prefix=False,
                    retry_interval=123,
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_oracle_asm_access_role_arn="secretsManagerOracleAsmAccessRoleArn",
                    secrets_manager_oracle_asm_secret_id="secretsManagerOracleAsmSecretId",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    security_db_encryption="securityDbEncryption",
                    security_db_encryption_name="securityDbEncryptionName",
                    spatial_data_option_to_geo_json_function_name="spatialDataOptionToGeoJsonFunctionName",
                    standby_delay_time=123,
                    use_alternate_folder_for_online=False,
                    use_bFile=False,
                    use_direct_path_full_load=False,
                    use_logminer_reader=False,
                    use_path_prefix="usePathPrefix"
                ),
                password="password",
                port=123,
                postgre_sql_settings=dms.CfnEndpoint.PostgreSqlSettingsProperty(
                    after_connect_script="afterConnectScript",
                    babelfish_database_name="babelfishDatabaseName",
                    capture_ddls=False,
                    database_mode="databaseMode",
                    ddl_artifacts_schema="ddlArtifactsSchema",
                    execute_timeout=123,
                    fail_tasks_on_lob_truncation=False,
                    heartbeat_enable=False,
                    heartbeat_frequency=123,
                    heartbeat_schema="heartbeatSchema",
                    map_boolean_as_boolean=False,
                    max_file_size=123,
                    plugin_name="pluginName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    slot_name="slotName"
                ),
                redis_settings=dms.CfnEndpoint.RedisSettingsProperty(
                    auth_password="authPassword",
                    auth_type="authType",
                    auth_user_name="authUserName",
                    port=123,
                    server_name="serverName",
                    ssl_ca_certificate_arn="sslCaCertificateArn",
                    ssl_security_protocol="sslSecurityProtocol"
                ),
                redshift_settings=dms.CfnEndpoint.RedshiftSettingsProperty(
                    accept_any_date=False,
                    after_connect_script="afterConnectScript",
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    case_sensitive_names=False,
                    comp_update=False,
                    connection_timeout=123,
                    date_format="dateFormat",
                    empty_as_null=False,
                    encryption_mode="encryptionMode",
                    explicit_ids=False,
                    file_transfer_upload_streams=123,
                    load_timeout=123,
                    map_boolean_as_boolean=False,
                    max_file_size=123,
                    remove_quotes=False,
                    replace_chars="replaceChars",
                    replace_invalid_chars="replaceInvalidChars",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId",
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    time_format="timeFormat",
                    trim_blanks=False,
                    truncate_columns=False,
                    write_buffer_size=123
                ),
                resource_identifier="resourceIdentifier",
                s3_settings=dms.CfnEndpoint.S3SettingsProperty(
                    add_column_name=False,
                    add_trailing_padding_character=False,
                    bucket_folder="bucketFolder",
                    bucket_name="bucketName",
                    canned_acl_for_objects="cannedAclForObjects",
                    cdc_inserts_and_updates=False,
                    cdc_inserts_only=False,
                    cdc_max_batch_interval=123,
                    cdc_min_file_size=123,
                    cdc_path="cdcPath",
                    compression_type="compressionType",
                    csv_delimiter="csvDelimiter",
                    csv_no_sup_value="csvNoSupValue",
                    csv_null_value="csvNullValue",
                    csv_row_delimiter="csvRowDelimiter",
                    data_format="dataFormat",
                    data_page_size=123,
                    date_partition_delimiter="datePartitionDelimiter",
                    date_partition_enabled=False,
                    date_partition_sequence="datePartitionSequence",
                    date_partition_timezone="datePartitionTimezone",
                    dict_page_size_limit=123,
                    enable_statistics=False,
                    encoding_type="encodingType",
                    encryption_mode="encryptionMode",
                    expected_bucket_owner="expectedBucketOwner",
                    external_table_definition="externalTableDefinition",
                    glue_catalog_generation=False,
                    ignore_header_rows=123,
                    include_op_for_full_load=False,
                    max_file_size=123,
                    parquet_timestamp_in_millisecond=False,
                    parquet_version="parquetVersion",
                    preserve_transactions=False,
                    rfc4180=False,
                    row_group_length=123,
                    server_side_encryption_kms_key_id="serverSideEncryptionKmsKeyId",
                    service_access_role_arn="serviceAccessRoleArn",
                    timestamp_column_name="timestampColumnName",
                    use_csv_no_sup_value=False,
                    use_task_start_time_for_full_load_timestamp=False
                ),
                server_name="serverName",
                ssl_mode="sslMode",
                sybase_settings=dms.CfnEndpoint.SybaseSettingsProperty(
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                username="username"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f339ae28a930c099a0a813d874222c50e581fbff0c5b98878c1f5ae0871a0236)
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument engine_name", value=engine_name, expected_type=type_hints["engine_name"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
            check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
            check_type(argname="argument doc_db_settings", value=doc_db_settings, expected_type=type_hints["doc_db_settings"])
            check_type(argname="argument dynamo_db_settings", value=dynamo_db_settings, expected_type=type_hints["dynamo_db_settings"])
            check_type(argname="argument elasticsearch_settings", value=elasticsearch_settings, expected_type=type_hints["elasticsearch_settings"])
            check_type(argname="argument endpoint_identifier", value=endpoint_identifier, expected_type=type_hints["endpoint_identifier"])
            check_type(argname="argument extra_connection_attributes", value=extra_connection_attributes, expected_type=type_hints["extra_connection_attributes"])
            check_type(argname="argument gcp_my_sql_settings", value=gcp_my_sql_settings, expected_type=type_hints["gcp_my_sql_settings"])
            check_type(argname="argument ibm_db2_settings", value=ibm_db2_settings, expected_type=type_hints["ibm_db2_settings"])
            check_type(argname="argument kafka_settings", value=kafka_settings, expected_type=type_hints["kafka_settings"])
            check_type(argname="argument kinesis_settings", value=kinesis_settings, expected_type=type_hints["kinesis_settings"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument microsoft_sql_server_settings", value=microsoft_sql_server_settings, expected_type=type_hints["microsoft_sql_server_settings"])
            check_type(argname="argument mongo_db_settings", value=mongo_db_settings, expected_type=type_hints["mongo_db_settings"])
            check_type(argname="argument my_sql_settings", value=my_sql_settings, expected_type=type_hints["my_sql_settings"])
            check_type(argname="argument neptune_settings", value=neptune_settings, expected_type=type_hints["neptune_settings"])
            check_type(argname="argument oracle_settings", value=oracle_settings, expected_type=type_hints["oracle_settings"])
            check_type(argname="argument password", value=password, expected_type=type_hints["password"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument postgre_sql_settings", value=postgre_sql_settings, expected_type=type_hints["postgre_sql_settings"])
            check_type(argname="argument redis_settings", value=redis_settings, expected_type=type_hints["redis_settings"])
            check_type(argname="argument redshift_settings", value=redshift_settings, expected_type=type_hints["redshift_settings"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument s3_settings", value=s3_settings, expected_type=type_hints["s3_settings"])
            check_type(argname="argument server_name", value=server_name, expected_type=type_hints["server_name"])
            check_type(argname="argument ssl_mode", value=ssl_mode, expected_type=type_hints["ssl_mode"])
            check_type(argname="argument sybase_settings", value=sybase_settings, expected_type=type_hints["sybase_settings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument username", value=username, expected_type=type_hints["username"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "endpoint_type": endpoint_type,
            "engine_name": engine_name,
        }
        if certificate_arn is not None:
            self._values["certificate_arn"] = certificate_arn
        if database_name is not None:
            self._values["database_name"] = database_name
        if doc_db_settings is not None:
            self._values["doc_db_settings"] = doc_db_settings
        if dynamo_db_settings is not None:
            self._values["dynamo_db_settings"] = dynamo_db_settings
        if elasticsearch_settings is not None:
            self._values["elasticsearch_settings"] = elasticsearch_settings
        if endpoint_identifier is not None:
            self._values["endpoint_identifier"] = endpoint_identifier
        if extra_connection_attributes is not None:
            self._values["extra_connection_attributes"] = extra_connection_attributes
        if gcp_my_sql_settings is not None:
            self._values["gcp_my_sql_settings"] = gcp_my_sql_settings
        if ibm_db2_settings is not None:
            self._values["ibm_db2_settings"] = ibm_db2_settings
        if kafka_settings is not None:
            self._values["kafka_settings"] = kafka_settings
        if kinesis_settings is not None:
            self._values["kinesis_settings"] = kinesis_settings
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if microsoft_sql_server_settings is not None:
            self._values["microsoft_sql_server_settings"] = microsoft_sql_server_settings
        if mongo_db_settings is not None:
            self._values["mongo_db_settings"] = mongo_db_settings
        if my_sql_settings is not None:
            self._values["my_sql_settings"] = my_sql_settings
        if neptune_settings is not None:
            self._values["neptune_settings"] = neptune_settings
        if oracle_settings is not None:
            self._values["oracle_settings"] = oracle_settings
        if password is not None:
            self._values["password"] = password
        if port is not None:
            self._values["port"] = port
        if postgre_sql_settings is not None:
            self._values["postgre_sql_settings"] = postgre_sql_settings
        if redis_settings is not None:
            self._values["redis_settings"] = redis_settings
        if redshift_settings is not None:
            self._values["redshift_settings"] = redshift_settings
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if s3_settings is not None:
            self._values["s3_settings"] = s3_settings
        if server_name is not None:
            self._values["server_name"] = server_name
        if ssl_mode is not None:
            self._values["ssl_mode"] = ssl_mode
        if sybase_settings is not None:
            self._values["sybase_settings"] = sybase_settings
        if tags is not None:
            self._values["tags"] = tags
        if username is not None:
            self._values["username"] = username

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''The type of endpoint.

        Valid values are ``source`` and ``target`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointtype
        '''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def engine_name(self) -> builtins.str:
        '''The type of engine for the endpoint, depending on the ``EndpointType`` value.

        *Valid values* : ``mysql`` | ``oracle`` | ``postgres`` | ``mariadb`` | ``aurora`` | ``aurora-postgresql`` | ``opensearch`` | ``redshift`` | ``redshift-serverless`` | ``s3`` | ``db2`` | ``azuredb`` | ``sybase`` | ``dynamodb`` | ``mongodb`` | ``kinesis`` | ``kafka`` | ``elasticsearch`` | ``docdb`` | ``sqlserver`` | ``neptune``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-enginename
        '''
        result = self._values.get("engine_name")
        assert result is not None, "Required property 'engine_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-certificatearn
        '''
        result = self._values.get("certificate_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def database_name(self) -> typing.Optional[builtins.str]:
        '''The name of the endpoint database.

        For a MySQL source or target endpoint, don't specify ``DatabaseName`` . To migrate to a specific database, use this setting and ``targetDbType`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-databasename
        '''
        result = self._values.get("database_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def doc_db_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.DocDbSettingsProperty]]:
        '''Settings in JSON format for the source and target DocumentDB endpoint.

        For more information about other available settings, see `Using extra connections attributes with Amazon DocumentDB as a source <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DocumentDB.html#CHAP_Source.DocumentDB.ECAs>`_ and `Using Amazon DocumentDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DocumentDB.html>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-docdbsettings
        '''
        result = self._values.get("doc_db_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.DocDbSettingsProperty]], result)

    @builtins.property
    def dynamo_db_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.DynamoDbSettingsProperty]]:
        '''Settings in JSON format for the target Amazon DynamoDB endpoint.

        For information about other available settings, see `Using object mapping to migrate data to DynamoDB <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.DynamoDB.html#CHAP_Target.DynamoDB.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-dynamodbsettings
        '''
        result = self._values.get("dynamo_db_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.DynamoDbSettingsProperty]], result)

    @builtins.property
    def elasticsearch_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.ElasticsearchSettingsProperty]]:
        '''Settings in JSON format for the target OpenSearch endpoint.

        For more information about the available settings, see `Extra connection attributes when using OpenSearch as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Elasticsearch.html#CHAP_Target.Elasticsearch.Configuration>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-elasticsearchsettings
        '''
        result = self._values.get("elasticsearch_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.ElasticsearchSettingsProperty]], result)

    @builtins.property
    def endpoint_identifier(self) -> typing.Optional[builtins.str]:
        '''The database endpoint identifier.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-endpointidentifier
        '''
        result = self._values.get("endpoint_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def extra_connection_attributes(self) -> typing.Optional[builtins.str]:
        '''Additional attributes associated with the connection.

        Each attribute is specified as a name-value pair associated by an equal sign (=). Multiple attributes are separated by a semicolon (;) with no additional white space. For information on the attributes available for connecting your source or target endpoint, see `Working with AWS DMS Endpoints <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-extraconnectionattributes
        '''
        result = self._values.get("extra_connection_attributes")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gcp_my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.GcpMySQLSettingsProperty]]:
        '''Settings in JSON format for the source GCP MySQL endpoint.

        These settings are much the same as the settings for any MySQL-compatible endpoint. For more information, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-gcpmysqlsettings
        '''
        result = self._values.get("gcp_my_sql_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.GcpMySQLSettingsProperty]], result)

    @builtins.property
    def ibm_db2_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.IbmDb2SettingsProperty]]:
        '''Settings in JSON format for the source IBM Db2 LUW endpoint.

        For information about other available settings, see `Extra connection attributes when using Db2 LUW as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-ibmdb2settings
        '''
        result = self._values.get("ibm_db2_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.IbmDb2SettingsProperty]], result)

    @builtins.property
    def kafka_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.KafkaSettingsProperty]]:
        '''Settings in JSON format for the target Apache Kafka endpoint.

        For more information about other available settings, see `Using object mapping to migrate data to a Kafka topic <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kafka.html#CHAP_Target.Kafka.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kafkasettings
        '''
        result = self._values.get("kafka_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.KafkaSettingsProperty]], result)

    @builtins.property
    def kinesis_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.KinesisSettingsProperty]]:
        '''Settings in JSON format for the target endpoint for Amazon Kinesis Data Streams.

        For more information about other available settings, see `Using object mapping to migrate data to a Kinesis data stream <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Kinesis.html#CHAP_Target.Kinesis.ObjectMapping>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kinesissettings
        '''
        result = self._values.get("kinesis_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.KinesisSettingsProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the connection parameters for the endpoint.

        If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def microsoft_sql_server_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MicrosoftSqlServerSettingsProperty]]:
        '''Settings in JSON format for the source and target Microsoft SQL Server endpoint.

        For information about other available settings, see `Extra connection attributes when using SQL Server as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SQLServer.html#CHAP_Source.SQLServer.ConnectionAttrib>`_ and `Extra connection attributes when using SQL Server as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SQLServer.html#CHAP_Target.SQLServer.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-microsoftsqlserversettings
        '''
        result = self._values.get("microsoft_sql_server_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MicrosoftSqlServerSettingsProperty]], result)

    @builtins.property
    def mongo_db_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MongoDbSettingsProperty]]:
        '''Settings in JSON format for the source MongoDB endpoint.

        For more information about the available settings, see `Using MongoDB as a target for AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MongoDB.html#CHAP_Source.MongoDB.Configuration>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mongodbsettings
        '''
        result = self._values.get("mongo_db_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MongoDbSettingsProperty]], result)

    @builtins.property
    def my_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MySqlSettingsProperty]]:
        '''Settings in JSON format for the source and target MySQL endpoint.

        For information about other available settings, see `Extra connection attributes when using MySQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.ConnectionAttrib>`_ and `Extra connection attributes when using a MySQL-compatible database as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.MySQL.html#CHAP_Target.MySQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-mysqlsettings
        '''
        result = self._values.get("my_sql_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MySqlSettingsProperty]], result)

    @builtins.property
    def neptune_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.NeptuneSettingsProperty]]:
        '''Settings in JSON format for the target Amazon Neptune endpoint.

        For more information about the available settings, see `Specifying endpoint settings for Amazon Neptune as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Neptune.html#CHAP_Target.Neptune.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-neptunesettings
        '''
        result = self._values.get("neptune_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.NeptuneSettingsProperty]], result)

    @builtins.property
    def oracle_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.OracleSettingsProperty]]:
        '''Settings in JSON format for the source and target Oracle endpoint.

        For information about other available settings, see `Extra connection attributes when using Oracle as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.ConnectionAttrib>`_ and `Extra connection attributes when using Oracle as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Oracle.html#CHAP_Target.Oracle.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-oraclesettings
        '''
        result = self._values.get("oracle_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.OracleSettingsProperty]], result)

    @builtins.property
    def password(self) -> typing.Optional[builtins.str]:
        '''The password to be used to log in to the endpoint database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-password
        '''
        result = self._values.get("password")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port used by the endpoint database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def postgre_sql_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.PostgreSqlSettingsProperty]]:
        '''Settings in JSON format for the source and target PostgreSQL endpoint.

        For information about other available settings, see `Extra connection attributes when using PostgreSQL as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ and `Extra connection attributes when using PostgreSQL as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.PostgreSQL.html#CHAP_Target.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-postgresqlsettings
        '''
        result = self._values.get("postgre_sql_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.PostgreSqlSettingsProperty]], result)

    @builtins.property
    def redis_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.RedisSettingsProperty]]:
        '''Settings in JSON format for the target Redis endpoint.

        For information about other available settings, see `Specifying endpoint settings for Redis as a target <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redis.html#CHAP_Target.Redis.EndpointSettings>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redissettings
        '''
        result = self._values.get("redis_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.RedisSettingsProperty]], result)

    @builtins.property
    def redshift_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.RedshiftSettingsProperty]]:
        '''Settings in JSON format for the Amazon Redshift endpoint.

        For more information about other available settings, see `Extra connection attributes when using Amazon Redshift as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.Redshift.html#CHAP_Target.Redshift.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-redshiftsettings
        '''
        result = self._values.get("redshift_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.RedshiftSettingsProperty]], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` .

        For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def s3_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.S3SettingsProperty]]:
        '''Settings in JSON format for the source and target Amazon S3 endpoint.

        For more information about other available settings, see `Extra connection attributes when using Amazon S3 as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.S3.html#CHAP_Source.S3.Configuring>`_ and `Extra connection attributes when using Amazon S3 as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html#CHAP_Target.S3.Configuring>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-s3settings
        '''
        result = self._values.get("s3_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.S3SettingsProperty]], result)

    @builtins.property
    def server_name(self) -> typing.Optional[builtins.str]:
        '''The name of the server where the endpoint database resides.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-servername
        '''
        result = self._values.get("server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ssl_mode(self) -> typing.Optional[builtins.str]:
        '''The Secure Sockets Layer (SSL) mode to use for the SSL connection. The default is ``none`` .

        .. epigraph::

           When ``engine_name`` is set to S3, the only allowed value is ``none`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sslmode
        '''
        result = self._values.get("ssl_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sybase_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.SybaseSettingsProperty]]:
        '''Settings in JSON format for the source and target SAP ASE endpoint.

        For information about other available settings, see `Extra connection attributes when using SAP ASE as a source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.SAP.html#CHAP_Source.SAP.ConnectionAttrib>`_ and `Extra connection attributes when using SAP ASE as a target for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.SAP.html#CHAP_Target.SAP.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-sybasesettings
        '''
        result = self._values.get("sybase_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.SybaseSettingsProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def username(self) -> typing.Optional[builtins.str]:
        '''The user name to be used to log in to the endpoint database.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-endpoint.html#cfn-dms-endpoint-username
        '''
        result = self._values.get("username")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEventSubscription(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnEventSubscription",
):
    '''Use the ``AWS::DMS::EventSubscription`` resource to get notifications for AWS Database Migration Service events through the Amazon Simple Notification Service .

    For more information, see `Working with events and notifications in AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Events.html>`_ in the *AWS Database Migration Service User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html
    :cloudformationResource: AWS::DMS::EventSubscription
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_event_subscription = dms.CfnEventSubscription(self, "MyCfnEventSubscription",
            sns_topic_arn="snsTopicArn",
        
            # the properties below are optional
            enabled=False,
            event_categories=["eventCategories"],
            source_ids=["sourceIds"],
            source_type="sourceType",
            subscription_name="subscriptionName",
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
        sns_topic_arn: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        subscription_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param enabled: Indicates whether to activate the subscription. If you don't specify this property, AWS CloudFormation activates the subscription.
        :param event_categories: A list of event categories for a source type that you want to subscribe to. If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .
        :param source_ids: A list of identifiers for which AWS DMS provides notification events. If you don't specify a value, notifications are provided for all sources. If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.
        :param source_type: The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned. *Valid values* : ``replication-instance`` | ``replication-task``
        :param subscription_name: The name of the AWS DMS event notification subscription. This name must be less than 255 characters.
        :param tags: One or more tags to be assigned to the event subscription.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d3042ac05bcc07c1b704196991fd764899b9b67bfb7cba510adb9fdde82fea2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEventSubscriptionProps(
            sns_topic_arn=sns_topic_arn,
            enabled=enabled,
            event_categories=event_categories,
            source_ids=source_ids,
            source_type=source_type,
            subscription_name=subscription_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a520e2d84ac9276dbb4367e25dcf72534a967d6d8ffc82a2a23176413a6d560c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4b0fb4580db11b3e885f145de5fc0563bace437ccec3f99cc736c88d07578906)
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="snsTopicArn")
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification.'''
        return typing.cast(builtins.str, jsii.get(self, "snsTopicArn"))

    @sns_topic_arn.setter
    def sns_topic_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__593d665e1b397d43ab850799dd046cefd2398ae5f20b75c1c583ffd38e44a267)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "snsTopicArn", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to activate the subscription.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f9e6185bdbcfc8331ed5d83bf2fbaa37dd9cb811c4e70a7c8fa3cf2a9f73604)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="eventCategories")
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of event categories for a source type that you want to subscribe to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "eventCategories"))

    @event_categories.setter
    def event_categories(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81aa84e39b9b7bbdb179d4aaaf48fa31beb2f53900fa1922bc6eec95a164d353)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventCategories", value)

    @builtins.property
    @jsii.member(jsii_name="sourceIds")
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identifiers for which AWS DMS provides notification events.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceIds"))

    @source_ids.setter
    def source_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5edd33fe4079b583e104f1f4e62422a4260f4f203418e37a0cf7bcc1966c9565)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceIds", value)

    @builtins.property
    @jsii.member(jsii_name="sourceType")
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of AWS DMS resource that generates the events.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceType"))

    @source_type.setter
    def source_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df31bd385d9a632c6d6aefb66fd10f1e20bfc574f4166fbdc97e9057812618dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceType", value)

    @builtins.property
    @jsii.member(jsii_name="subscriptionName")
    def subscription_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AWS DMS event notification subscription.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subscriptionName"))

    @subscription_name.setter
    def subscription_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff68707f28923ac91e18c59be07ef7df511b633754f39276fd09448e2df08f91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscriptionName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the event subscription.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80baa3035b4fe50b1e5040583141b0b892965c1bceea423668eba59b6a4693e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnEventSubscriptionProps",
    jsii_struct_bases=[],
    name_mapping={
        "sns_topic_arn": "snsTopicArn",
        "enabled": "enabled",
        "event_categories": "eventCategories",
        "source_ids": "sourceIds",
        "source_type": "sourceType",
        "subscription_name": "subscriptionName",
        "tags": "tags",
    },
)
class CfnEventSubscriptionProps:
    def __init__(
        self,
        *,
        sns_topic_arn: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        source_type: typing.Optional[builtins.str] = None,
        subscription_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEventSubscription``.

        :param sns_topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification. The ARN is created by Amazon SNS when you create a topic and subscribe to it.
        :param enabled: Indicates whether to activate the subscription. If you don't specify this property, AWS CloudFormation activates the subscription.
        :param event_categories: A list of event categories for a source type that you want to subscribe to. If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .
        :param source_ids: A list of identifiers for which AWS DMS provides notification events. If you don't specify a value, notifications are provided for all sources. If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.
        :param source_type: The type of AWS DMS resource that generates the events. For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned. *Valid values* : ``replication-instance`` | ``replication-task``
        :param subscription_name: The name of the AWS DMS event notification subscription. This name must be less than 255 characters.
        :param tags: One or more tags to be assigned to the event subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_event_subscription_props = dms.CfnEventSubscriptionProps(
                sns_topic_arn="snsTopicArn",
            
                # the properties below are optional
                enabled=False,
                event_categories=["eventCategories"],
                source_ids=["sourceIds"],
                source_type="sourceType",
                subscription_name="subscriptionName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1555cbc21ca1acdd6ec0e2aad881e8c61105a38d2f194a09e644f876547b64e6)
            check_type(argname="argument sns_topic_arn", value=sns_topic_arn, expected_type=type_hints["sns_topic_arn"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument event_categories", value=event_categories, expected_type=type_hints["event_categories"])
            check_type(argname="argument source_ids", value=source_ids, expected_type=type_hints["source_ids"])
            check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            check_type(argname="argument subscription_name", value=subscription_name, expected_type=type_hints["subscription_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "sns_topic_arn": sns_topic_arn,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if event_categories is not None:
            self._values["event_categories"] = event_categories
        if source_ids is not None:
            self._values["source_ids"] = source_ids
        if source_type is not None:
            self._values["source_type"] = source_type
        if subscription_name is not None:
            self._values["subscription_name"] = subscription_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def sns_topic_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic created for event notification.

        The ARN is created by Amazon SNS when you create a topic and subscribe to it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-snstopicarn
        '''
        result = self._values.get("sns_topic_arn")
        assert result is not None, "Required property 'sns_topic_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether to activate the subscription.

        If you don't specify this property, AWS CloudFormation activates the subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def event_categories(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of event categories for a source type that you want to subscribe to.

        If you don't specify this property, you are notified about all event categories. For more information, see `Working with Events and Notifications <https://docs.aws.amazon.com//dms/latest/userguide/CHAP_Events.html>`_ in the *AWS DMS User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-eventcategories
        '''
        result = self._values.get("event_categories")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of identifiers for which AWS DMS provides notification events.

        If you don't specify a value, notifications are provided for all sources.

        If you specify multiple values, they must be of the same type. For example, if you specify a database instance ID, then all of the other values must be database instance IDs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourceids
        '''
        result = self._values.get("source_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def source_type(self) -> typing.Optional[builtins.str]:
        '''The type of AWS DMS resource that generates the events.

        For example, if you want to be notified of events generated by a replication instance, you set this parameter to ``replication-instance`` . If this value isn't specified, all events are returned.

        *Valid values* : ``replication-instance`` | ``replication-task``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-sourcetype
        '''
        result = self._values.get("source_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subscription_name(self) -> typing.Optional[builtins.str]:
        '''The name of the AWS DMS event notification subscription.

        This name must be less than 255 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-subscriptionname
        '''
        result = self._values.get("subscription_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the event subscription.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-eventsubscription.html#cfn-dms-eventsubscription-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEventSubscriptionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnInstanceProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnInstanceProfile",
):
    '''Provides information that defines an instance profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html
    :cloudformationResource: AWS::DMS::InstanceProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_instance_profile = dms.CfnInstanceProfile(self, "MyCfnInstanceProfile",
            availability_zone="availabilityZone",
            description="description",
            instance_profile_identifier="instanceProfileIdentifier",
            instance_profile_name="instanceProfileName",
            kms_key_arn="kmsKeyArn",
            network_type="networkType",
            publicly_accessible=False,
            subnet_group_identifier="subnetGroupIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_groups=["vpcSecurityGroups"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        availability_zone: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        instance_profile_identifier: typing.Optional[builtins.str] = None,
        instance_profile_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        subnet_group_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param availability_zone: The Availability Zone where the instance profile runs.
        :param description: A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
        :param instance_profile_identifier: The identifier of the instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param instance_profile_name: The user-friendly name for the instance profile.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile. If you don't specify a value for the ``KmsKeyArn`` parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param network_type: Specifies the network type for the instance profile. A value of ``IPV4`` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of ``IPV6`` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of ``DUAL`` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.
        :param publicly_accessible: Specifies the accessibility options for the instance profile. A value of ``true`` represents an instance profile with a public IP address. A value of ``false`` represents an instance profile with a private IP address. The default value is ``true`` . Default: - false
        :param subnet_group_identifier: The identifier of the subnet group that is associated with the instance profile.
        :param tags: An array of key-value pairs to apply to this resource.
        :param vpc_security_groups: The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c72f2ad0340026b7e11a2dcfa2f16a6cc0dd6393207ad4c41449ed94d6f4a58)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnInstanceProfileProps(
            availability_zone=availability_zone,
            description=description,
            instance_profile_identifier=instance_profile_identifier,
            instance_profile_name=instance_profile_name,
            kms_key_arn=kms_key_arn,
            network_type=network_type,
            publicly_accessible=publicly_accessible,
            subnet_group_identifier=subnet_group_identifier,
            tags=tags,
            vpc_security_groups=vpc_security_groups,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8342c573d42f8c324d79b2e95f84d87e6e369d07fdb8d38ff3910d46a7fdbc9b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d34fee644628abdf39d7679305233b8f3684c6179e63a5b1d72923ca21dc8098)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrInstanceProfileArn")
    def attr_instance_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) string that uniquely identifies the instance profile.

        :cloudformationAttribute: InstanceProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInstanceProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="attrInstanceProfileCreationTime")
    def attr_instance_profile_creation_time(self) -> builtins.str:
        '''The time the instance profile was created.

        :cloudformationAttribute: InstanceProfileCreationTime
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrInstanceProfileCreationTime"))

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
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone where the instance profile runs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7805a3c0f395e2f5616503be94a7a3d3a684e843abb549e10dafe313f3b6963e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98de871dda338355afedba4e4db5b2f2d06c3dac29d4225e710c03a257396bda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileIdentifier")
    def instance_profile_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileIdentifier"))

    @instance_profile_identifier.setter
    def instance_profile_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__adc46e83492bd9e5c1b2998646230bbfaefa04312834f26a3704ed50fe6d3c73)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name for the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileName"))

    @instance_profile_name.setter
    def instance_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e1381637e90360c57a7887d83c6d85fd5d618213f81718da1dcf9c140a95966)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f4d581525fcc739af608fad445ea300f231676aaaddbc1fe7ef970e225bb1f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="networkType")
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the network type for the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkType"))

    @network_type.setter
    def network_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__23bc9a7e8ff96ae22982668c0a90e427cd65f81443fa65b96881009765893978)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkType", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies the accessibility options for the instance profile.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bab01c20133942c669cfa6364b41fe2f0884195135cdb484b907cd1d017de096)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="subnetGroupIdentifier")
    def subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the subnet group that is associated with the instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subnetGroupIdentifier"))

    @subnet_group_identifier.setter
    def subnet_group_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dd1328bedaa07486f249a94e5cb045c3d86574e3e0b22d39915c10b0944c77d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetGroupIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18cb1326620745b811df71b6f775ffff322b6d7a24cc629d76bd1a938e4e1e10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroups")
    def vpc_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The VPC security groups that are used with the instance profile.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroups"))

    @vpc_security_groups.setter
    def vpc_security_groups(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4acb79a955201c074f7475d3a51ea385cae01e682de7bd61381384953fb050e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroups", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnInstanceProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "availability_zone": "availabilityZone",
        "description": "description",
        "instance_profile_identifier": "instanceProfileIdentifier",
        "instance_profile_name": "instanceProfileName",
        "kms_key_arn": "kmsKeyArn",
        "network_type": "networkType",
        "publicly_accessible": "publiclyAccessible",
        "subnet_group_identifier": "subnetGroupIdentifier",
        "tags": "tags",
        "vpc_security_groups": "vpcSecurityGroups",
    },
)
class CfnInstanceProfileProps:
    def __init__(
        self,
        *,
        availability_zone: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        instance_profile_identifier: typing.Optional[builtins.str] = None,
        instance_profile_name: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        network_type: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        subnet_group_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnInstanceProfile``.

        :param availability_zone: The Availability Zone where the instance profile runs.
        :param description: A description of the instance profile. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.
        :param instance_profile_identifier: The identifier of the instance profile. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param instance_profile_name: The user-friendly name for the instance profile.
        :param kms_key_arn: The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile. If you don't specify a value for the ``KmsKeyArn`` parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param network_type: Specifies the network type for the instance profile. A value of ``IPV4`` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of ``IPV6`` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of ``DUAL`` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.
        :param publicly_accessible: Specifies the accessibility options for the instance profile. A value of ``true`` represents an instance profile with a public IP address. A value of ``false`` represents an instance profile with a private IP address. The default value is ``true`` . Default: - false
        :param subnet_group_identifier: The identifier of the subnet group that is associated with the instance profile.
        :param tags: An array of key-value pairs to apply to this resource.
        :param vpc_security_groups: The VPC security groups that are used with the instance profile. The VPC security group must work with the VPC containing the instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_instance_profile_props = dms.CfnInstanceProfileProps(
                availability_zone="availabilityZone",
                description="description",
                instance_profile_identifier="instanceProfileIdentifier",
                instance_profile_name="instanceProfileName",
                kms_key_arn="kmsKeyArn",
                network_type="networkType",
                publicly_accessible=False,
                subnet_group_identifier="subnetGroupIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_groups=["vpcSecurityGroups"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb987e57079646d3b74d43384b58a2e19975492c1f1b317aba746e6fa1f47b4e)
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument instance_profile_identifier", value=instance_profile_identifier, expected_type=type_hints["instance_profile_identifier"])
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument network_type", value=network_type, expected_type=type_hints["network_type"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument subnet_group_identifier", value=subnet_group_identifier, expected_type=type_hints["subnet_group_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_groups", value=vpc_security_groups, expected_type=type_hints["vpc_security_groups"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if description is not None:
            self._values["description"] = description
        if instance_profile_identifier is not None:
            self._values["instance_profile_identifier"] = instance_profile_identifier
        if instance_profile_name is not None:
            self._values["instance_profile_name"] = instance_profile_name
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if network_type is not None:
            self._values["network_type"] = network_type
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if subnet_group_identifier is not None:
            self._values["subnet_group_identifier"] = subnet_group_identifier
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_groups is not None:
            self._values["vpc_security_groups"] = vpc_security_groups

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone where the instance profile runs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the instance profile.

        Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the instance profile.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-instanceprofileidentifier
        '''
        result = self._values.get("instance_profile_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The user-friendly name for the instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-instanceprofilename
        '''
        result = self._values.get("instance_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the AWS KMS key that is used to encrypt the connection parameters for the instance profile.

        If you don't specify a value for the ``KmsKeyArn`` parameter, then AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def network_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the network type for the instance profile.

        A value of ``IPV4`` represents an instance profile with IPv4 network type and only supports IPv4 addressing. A value of ``IPV6`` represents an instance profile with IPv6 network type and only supports IPv6 addressing. A value of ``DUAL`` represents an instance profile with dual network type that supports IPv4 and IPv6 addressing.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-networktype
        '''
        result = self._values.get("network_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies the accessibility options for the instance profile.

        A value of ``true`` represents an instance profile with a public IP address. A value of ``false`` represents an instance profile with a private IP address. The default value is ``true`` .

        :default: - false

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the subnet group that is associated with the instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-subnetgroupidentifier
        '''
        result = self._values.get("subnet_group_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_security_groups(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The VPC security groups that are used with the instance profile.

        The VPC security group must work with the VPC containing the instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-instanceprofile.html#cfn-dms-instanceprofile-vpcsecuritygroups
        '''
        result = self._values.get("vpc_security_groups")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnInstanceProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnMigrationProject(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnMigrationProject",
):
    '''Provides information that defines a migration project.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html
    :cloudformationResource: AWS::DMS::MigrationProject
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_migration_project = dms.CfnMigrationProject(self, "MyCfnMigrationProject",
            description="description",
            instance_profile_arn="instanceProfileArn",
            instance_profile_identifier="instanceProfileIdentifier",
            instance_profile_name="instanceProfileName",
            migration_project_creation_time="migrationProjectCreationTime",
            migration_project_identifier="migrationProjectIdentifier",
            migration_project_name="migrationProjectName",
            schema_conversion_application_attributes=dms.CfnMigrationProject.SchemaConversionApplicationAttributesProperty(
                s3_bucket_path="s3BucketPath",
                s3_bucket_role_arn="s3BucketRoleArn"
            ),
            source_data_provider_descriptors=[dms.CfnMigrationProject.DataProviderDescriptorProperty(
                data_provider_arn="dataProviderArn",
                data_provider_identifier="dataProviderIdentifier",
                data_provider_name="dataProviderName",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId"
            )],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_data_provider_descriptors=[dms.CfnMigrationProject.DataProviderDescriptorProperty(
                data_provider_arn="dataProviderArn",
                data_provider_identifier="dataProviderIdentifier",
                data_provider_name="dataProviderName",
                secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                secrets_manager_secret_id="secretsManagerSecretId"
            )],
            transformation_rules="transformationRules"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: typing.Optional[builtins.str] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        instance_profile_identifier: typing.Optional[builtins.str] = None,
        instance_profile_name: typing.Optional[builtins.str] = None,
        migration_project_creation_time: typing.Optional[builtins.str] = None,
        migration_project_identifier: typing.Optional[builtins.str] = None,
        migration_project_name: typing.Optional[builtins.str] = None,
        schema_conversion_application_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMigrationProject.SchemaConversionApplicationAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        source_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMigrationProject.DataProviderDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnMigrationProject.DataProviderDescriptorProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        transformation_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A user-friendly description of the migration project.
        :param instance_profile_arn: The Amazon Resource Name (ARN) of the instance profile for your migration project.
        :param instance_profile_identifier: The identifier of the instance profile for your migration project.
        :param instance_profile_name: The name of the associated instance profile.
        :param migration_project_creation_time: (deprecated) The property describes a creating time of the migration project.
        :param migration_project_identifier: The identifier of the migration project. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param migration_project_name: The name of the migration project.
        :param schema_conversion_application_attributes: The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.
        :param source_data_provider_descriptors: Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.
        :param tags: An array of key-value pairs to apply to this resource.
        :param target_data_provider_descriptors: Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.
        :param transformation_rules: The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02169f44825ddf8b21ca2acf1c203831f0a34ba053b5b8f4fea59ef921f5b56d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnMigrationProjectProps(
            description=description,
            instance_profile_arn=instance_profile_arn,
            instance_profile_identifier=instance_profile_identifier,
            instance_profile_name=instance_profile_name,
            migration_project_creation_time=migration_project_creation_time,
            migration_project_identifier=migration_project_identifier,
            migration_project_name=migration_project_name,
            schema_conversion_application_attributes=schema_conversion_application_attributes,
            source_data_provider_descriptors=source_data_provider_descriptors,
            tags=tags,
            target_data_provider_descriptors=target_data_provider_descriptors,
            transformation_rules=transformation_rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__065b1cff71013e652903120372025cf335be7540413e4796b5304cc45f7551ff)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca6cab78ffccaad1c9b4efb641e75a6a31291549ab60102fad047e242f4b2e7f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrMigrationProjectArn")
    def attr_migration_project_arn(self) -> builtins.str:
        '''The ARN string that uniquely identifies the migration project.

        :cloudformationAttribute: MigrationProjectArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrMigrationProjectArn"))

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
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-friendly description of the migration project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c4df3a27d190edf622a69f5bd243619958a52f12a7a2096b3c8915be11ee0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileArn")
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the instance profile for your migration project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileArn"))

    @instance_profile_arn.setter
    def instance_profile_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb1088337e159a58c057cac4f84e3b23c6881a1c6ead507f336ae854ce449cc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileArn", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileIdentifier")
    def instance_profile_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the instance profile for your migration project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileIdentifier"))

    @instance_profile_identifier.setter
    def instance_profile_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__69e488dc8697a5afa8fd5ad8a91be36da51b419476ffb73594779e6c292e3cd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="instanceProfileName")
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the associated instance profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceProfileName"))

    @instance_profile_name.setter
    def instance_profile_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__812b2039dff2aa0cc8cc17107db06bd70989e3fa445f454e3410c74ec7c6255e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="migrationProjectCreationTime")
    def migration_project_creation_time(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The property describes a creating time of the migration project.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "migrationProjectCreationTime"))

    @migration_project_creation_time.setter
    def migration_project_creation_time(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b554b998a3f49e6d6edda5123f6f8268659d40c8705e87858e33b1f6edcce8e6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationProjectCreationTime", value)

    @builtins.property
    @jsii.member(jsii_name="migrationProjectIdentifier")
    def migration_project_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the migration project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "migrationProjectIdentifier"))

    @migration_project_identifier.setter
    def migration_project_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57db7ced3b40ef7d0d29ee5e2525eaa55617b8369a29470dc7866521cffd6b47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationProjectIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="migrationProjectName")
    def migration_project_name(self) -> typing.Optional[builtins.str]:
        '''The name of the migration project.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "migrationProjectName"))

    @migration_project_name.setter
    def migration_project_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__12a0e20b765f80d1bd487470e2ba2e107b2e528e71b3f54206b3fa21f1350973)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationProjectName", value)

    @builtins.property
    @jsii.member(jsii_name="schemaConversionApplicationAttributes")
    def schema_conversion_application_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.SchemaConversionApplicationAttributesProperty"]]:
        '''The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.SchemaConversionApplicationAttributesProperty"]], jsii.get(self, "schemaConversionApplicationAttributes"))

    @schema_conversion_application_attributes.setter
    def schema_conversion_application_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.SchemaConversionApplicationAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8248f02c8a28507c6fd7b69d9078ece62cf902113b4922ac2c3b1eb1efe99e47)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaConversionApplicationAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="sourceDataProviderDescriptors")
    def source_data_provider_descriptors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.DataProviderDescriptorProperty"]]]]:
        '''Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.DataProviderDescriptorProperty"]]]], jsii.get(self, "sourceDataProviderDescriptors"))

    @source_data_provider_descriptors.setter
    def source_data_provider_descriptors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.DataProviderDescriptorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a00bd941d6a9f753e2588061a187fa267a4026e4ad4481a8223f35bfb06bc87c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceDataProviderDescriptors", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8af1fc70b174a366c98ab2a01a5b731e43ae5aea452d554ac059c8709dc325)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targetDataProviderDescriptors")
    def target_data_provider_descriptors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.DataProviderDescriptorProperty"]]]]:
        '''Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.DataProviderDescriptorProperty"]]]], jsii.get(self, "targetDataProviderDescriptors"))

    @target_data_provider_descriptors.setter
    def target_data_provider_descriptors(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnMigrationProject.DataProviderDescriptorProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e70fa24655fe3ca5e620c8a935fd467925c600296ae5d6c563060ae2bd7b8ebb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetDataProviderDescriptors", value)

    @builtins.property
    @jsii.member(jsii_name="transformationRules")
    def transformation_rules(self) -> typing.Optional[builtins.str]:
        '''The settings in JSON format for migration rules.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "transformationRules"))

    @transformation_rules.setter
    def transformation_rules(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b22cebadf8cc06e1152ada0e5ac728f60ae06205a5b8fdd994f6a4353bbae96)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "transformationRules", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnMigrationProject.DataProviderDescriptorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_provider_arn": "dataProviderArn",
            "data_provider_identifier": "dataProviderIdentifier",
            "data_provider_name": "dataProviderName",
            "secrets_manager_access_role_arn": "secretsManagerAccessRoleArn",
            "secrets_manager_secret_id": "secretsManagerSecretId",
        },
    )
    class DataProviderDescriptorProperty:
        def __init__(
            self,
            *,
            data_provider_arn: typing.Optional[builtins.str] = None,
            data_provider_identifier: typing.Optional[builtins.str] = None,
            data_provider_name: typing.Optional[builtins.str] = None,
            secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
            secrets_manager_secret_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about a data provider.

            :param data_provider_arn: The Amazon Resource Name (ARN) of the data provider.
            :param data_provider_identifier: 
            :param data_provider_name: The user-friendly name of the data provider.
            :param secrets_manager_access_role_arn: The ARN of the role used to access AWS Secrets Manager.
            :param secrets_manager_secret_id: The identifier of the AWS Secrets Manager Secret used to store access credentials for the data provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                data_provider_descriptor_property = dms.CfnMigrationProject.DataProviderDescriptorProperty(
                    data_provider_arn="dataProviderArn",
                    data_provider_identifier="dataProviderIdentifier",
                    data_provider_name="dataProviderName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__299742754139f0f8b894350a42e410914b67658b976b2ba7cdd3a1e776217876)
                check_type(argname="argument data_provider_arn", value=data_provider_arn, expected_type=type_hints["data_provider_arn"])
                check_type(argname="argument data_provider_identifier", value=data_provider_identifier, expected_type=type_hints["data_provider_identifier"])
                check_type(argname="argument data_provider_name", value=data_provider_name, expected_type=type_hints["data_provider_name"])
                check_type(argname="argument secrets_manager_access_role_arn", value=secrets_manager_access_role_arn, expected_type=type_hints["secrets_manager_access_role_arn"])
                check_type(argname="argument secrets_manager_secret_id", value=secrets_manager_secret_id, expected_type=type_hints["secrets_manager_secret_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_provider_arn is not None:
                self._values["data_provider_arn"] = data_provider_arn
            if data_provider_identifier is not None:
                self._values["data_provider_identifier"] = data_provider_identifier
            if data_provider_name is not None:
                self._values["data_provider_name"] = data_provider_name
            if secrets_manager_access_role_arn is not None:
                self._values["secrets_manager_access_role_arn"] = secrets_manager_access_role_arn
            if secrets_manager_secret_id is not None:
                self._values["secrets_manager_secret_id"] = secrets_manager_secret_id

        @builtins.property
        def data_provider_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the data provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html#cfn-dms-migrationproject-dataproviderdescriptor-dataproviderarn
            '''
            result = self._values.get("data_provider_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_provider_identifier(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html#cfn-dms-migrationproject-dataproviderdescriptor-dataprovideridentifier
            '''
            result = self._values.get("data_provider_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_provider_name(self) -> typing.Optional[builtins.str]:
            '''The user-friendly name of the data provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html#cfn-dms-migrationproject-dataproviderdescriptor-dataprovidername
            '''
            result = self._values.get("data_provider_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_access_role_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the role used to access AWS Secrets Manager.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html#cfn-dms-migrationproject-dataproviderdescriptor-secretsmanageraccessrolearn
            '''
            result = self._values.get("secrets_manager_access_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secrets_manager_secret_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the AWS Secrets Manager Secret used to store access credentials for the data provider.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-dataproviderdescriptor.html#cfn-dms-migrationproject-dataproviderdescriptor-secretsmanagersecretid
            '''
            result = self._values.get("secrets_manager_secret_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataProviderDescriptorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnMigrationProject.SchemaConversionApplicationAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket_path": "s3BucketPath",
            "s3_bucket_role_arn": "s3BucketRoleArn",
        },
    )
    class SchemaConversionApplicationAttributesProperty:
        def __init__(
            self,
            *,
            s3_bucket_path: typing.Optional[builtins.str] = None,
            s3_bucket_role_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The property describes schema conversion application attributes for the migration project.

            :param s3_bucket_path: 
            :param s3_bucket_role_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-schemaconversionapplicationattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                schema_conversion_application_attributes_property = dms.CfnMigrationProject.SchemaConversionApplicationAttributesProperty(
                    s3_bucket_path="s3BucketPath",
                    s3_bucket_role_arn="s3BucketRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__845461800c57296041434f4d61b34cd11fc19c1e5835ee02c0868f4fc30ae9c0)
                check_type(argname="argument s3_bucket_path", value=s3_bucket_path, expected_type=type_hints["s3_bucket_path"])
                check_type(argname="argument s3_bucket_role_arn", value=s3_bucket_role_arn, expected_type=type_hints["s3_bucket_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_bucket_path is not None:
                self._values["s3_bucket_path"] = s3_bucket_path
            if s3_bucket_role_arn is not None:
                self._values["s3_bucket_role_arn"] = s3_bucket_role_arn

        @builtins.property
        def s3_bucket_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-schemaconversionapplicationattributes.html#cfn-dms-migrationproject-schemaconversionapplicationattributes-s3bucketpath
            '''
            result = self._values.get("s3_bucket_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_bucket_role_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-migrationproject-schemaconversionapplicationattributes.html#cfn-dms-migrationproject-schemaconversionapplicationattributes-s3bucketrolearn
            '''
            result = self._values.get("s3_bucket_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaConversionApplicationAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnMigrationProjectProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "instance_profile_arn": "instanceProfileArn",
        "instance_profile_identifier": "instanceProfileIdentifier",
        "instance_profile_name": "instanceProfileName",
        "migration_project_creation_time": "migrationProjectCreationTime",
        "migration_project_identifier": "migrationProjectIdentifier",
        "migration_project_name": "migrationProjectName",
        "schema_conversion_application_attributes": "schemaConversionApplicationAttributes",
        "source_data_provider_descriptors": "sourceDataProviderDescriptors",
        "tags": "tags",
        "target_data_provider_descriptors": "targetDataProviderDescriptors",
        "transformation_rules": "transformationRules",
    },
)
class CfnMigrationProjectProps:
    def __init__(
        self,
        *,
        description: typing.Optional[builtins.str] = None,
        instance_profile_arn: typing.Optional[builtins.str] = None,
        instance_profile_identifier: typing.Optional[builtins.str] = None,
        instance_profile_name: typing.Optional[builtins.str] = None,
        migration_project_creation_time: typing.Optional[builtins.str] = None,
        migration_project_identifier: typing.Optional[builtins.str] = None,
        migration_project_name: typing.Optional[builtins.str] = None,
        schema_conversion_application_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.SchemaConversionApplicationAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        source_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.DataProviderDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.DataProviderDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        transformation_rules: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnMigrationProject``.

        :param description: A user-friendly description of the migration project.
        :param instance_profile_arn: The Amazon Resource Name (ARN) of the instance profile for your migration project.
        :param instance_profile_identifier: The identifier of the instance profile for your migration project.
        :param instance_profile_name: The name of the associated instance profile.
        :param migration_project_creation_time: (deprecated) The property describes a creating time of the migration project.
        :param migration_project_identifier: The identifier of the migration project. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.
        :param migration_project_name: The name of the migration project.
        :param schema_conversion_application_attributes: The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.
        :param source_data_provider_descriptors: Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.
        :param tags: An array of key-value pairs to apply to this resource.
        :param target_data_provider_descriptors: Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.
        :param transformation_rules: The settings in JSON format for migration rules. Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_migration_project_props = dms.CfnMigrationProjectProps(
                description="description",
                instance_profile_arn="instanceProfileArn",
                instance_profile_identifier="instanceProfileIdentifier",
                instance_profile_name="instanceProfileName",
                migration_project_creation_time="migrationProjectCreationTime",
                migration_project_identifier="migrationProjectIdentifier",
                migration_project_name="migrationProjectName",
                schema_conversion_application_attributes=dms.CfnMigrationProject.SchemaConversionApplicationAttributesProperty(
                    s3_bucket_path="s3BucketPath",
                    s3_bucket_role_arn="s3BucketRoleArn"
                ),
                source_data_provider_descriptors=[dms.CfnMigrationProject.DataProviderDescriptorProperty(
                    data_provider_arn="dataProviderArn",
                    data_provider_identifier="dataProviderIdentifier",
                    data_provider_name="dataProviderName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_data_provider_descriptors=[dms.CfnMigrationProject.DataProviderDescriptorProperty(
                    data_provider_arn="dataProviderArn",
                    data_provider_identifier="dataProviderIdentifier",
                    data_provider_name="dataProviderName",
                    secrets_manager_access_role_arn="secretsManagerAccessRoleArn",
                    secrets_manager_secret_id="secretsManagerSecretId"
                )],
                transformation_rules="transformationRules"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d354515598618d1781b30321646570d53cc9d8150e99820d2ffc982f69de692)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument instance_profile_arn", value=instance_profile_arn, expected_type=type_hints["instance_profile_arn"])
            check_type(argname="argument instance_profile_identifier", value=instance_profile_identifier, expected_type=type_hints["instance_profile_identifier"])
            check_type(argname="argument instance_profile_name", value=instance_profile_name, expected_type=type_hints["instance_profile_name"])
            check_type(argname="argument migration_project_creation_time", value=migration_project_creation_time, expected_type=type_hints["migration_project_creation_time"])
            check_type(argname="argument migration_project_identifier", value=migration_project_identifier, expected_type=type_hints["migration_project_identifier"])
            check_type(argname="argument migration_project_name", value=migration_project_name, expected_type=type_hints["migration_project_name"])
            check_type(argname="argument schema_conversion_application_attributes", value=schema_conversion_application_attributes, expected_type=type_hints["schema_conversion_application_attributes"])
            check_type(argname="argument source_data_provider_descriptors", value=source_data_provider_descriptors, expected_type=type_hints["source_data_provider_descriptors"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_data_provider_descriptors", value=target_data_provider_descriptors, expected_type=type_hints["target_data_provider_descriptors"])
            check_type(argname="argument transformation_rules", value=transformation_rules, expected_type=type_hints["transformation_rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if description is not None:
            self._values["description"] = description
        if instance_profile_arn is not None:
            self._values["instance_profile_arn"] = instance_profile_arn
        if instance_profile_identifier is not None:
            self._values["instance_profile_identifier"] = instance_profile_identifier
        if instance_profile_name is not None:
            self._values["instance_profile_name"] = instance_profile_name
        if migration_project_creation_time is not None:
            self._values["migration_project_creation_time"] = migration_project_creation_time
        if migration_project_identifier is not None:
            self._values["migration_project_identifier"] = migration_project_identifier
        if migration_project_name is not None:
            self._values["migration_project_name"] = migration_project_name
        if schema_conversion_application_attributes is not None:
            self._values["schema_conversion_application_attributes"] = schema_conversion_application_attributes
        if source_data_provider_descriptors is not None:
            self._values["source_data_provider_descriptors"] = source_data_provider_descriptors
        if tags is not None:
            self._values["tags"] = tags
        if target_data_provider_descriptors is not None:
            self._values["target_data_provider_descriptors"] = target_data_provider_descriptors
        if transformation_rules is not None:
            self._values["transformation_rules"] = transformation_rules

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-friendly description of the migration project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the instance profile for your migration project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-instanceprofilearn
        '''
        result = self._values.get("instance_profile_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the instance profile for your migration project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-instanceprofileidentifier
        '''
        result = self._values.get("instance_profile_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_profile_name(self) -> typing.Optional[builtins.str]:
        '''The name of the associated instance profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-instanceprofilename
        '''
        result = self._values.get("instance_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migration_project_creation_time(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The property describes a creating time of the migration project.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-migrationprojectcreationtime
        :stability: deprecated
        '''
        result = self._values.get("migration_project_creation_time")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migration_project_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier of the migration project.

        Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They can't end with a hyphen, or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-migrationprojectidentifier
        '''
        result = self._values.get("migration_project_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def migration_project_name(self) -> typing.Optional[builtins.str]:
        '''The name of the migration project.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-migrationprojectname
        '''
        result = self._values.get("migration_project_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_conversion_application_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.SchemaConversionApplicationAttributesProperty]]:
        '''The schema conversion application attributes, including the Amazon S3 bucket name and Amazon S3 role ARN.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-schemaconversionapplicationattributes
        '''
        result = self._values.get("schema_conversion_application_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.SchemaConversionApplicationAttributesProperty]], result)

    @builtins.property
    def source_data_provider_descriptors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.DataProviderDescriptorProperty]]]]:
        '''Information about the source data provider, including the name or ARN, and AWS Secrets Manager parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-sourcedataproviderdescriptors
        '''
        result = self._values.get("source_data_provider_descriptors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.DataProviderDescriptorProperty]]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_data_provider_descriptors(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.DataProviderDescriptorProperty]]]]:
        '''Information about the target data provider, including the name or ARN, and AWS Secrets Manager parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-targetdataproviderdescriptors
        '''
        result = self._values.get("target_data_provider_descriptors")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.DataProviderDescriptorProperty]]]], result)

    @builtins.property
    def transformation_rules(self) -> typing.Optional[builtins.str]:
        '''The settings in JSON format for migration rules.

        Migration rules make it possible for you to change the object names according to the rules that you specify. For example, you can change an object name to lowercase or uppercase, add or remove a prefix or suffix, or rename objects.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-migrationproject.html#cfn-dms-migrationproject-transformationrules
        '''
        result = self._values.get("transformation_rules")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnMigrationProjectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnReplicationConfig(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationConfig",
):
    '''http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html
    :cloudformationResource: AWS::DMS::ReplicationConfig
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        # replication_settings: Any
        # supplemental_settings: Any
        # table_mappings: Any
        
        cfn_replication_config = dms.CfnReplicationConfig(self, "MyCfnReplicationConfig",
            compute_config=dms.CfnReplicationConfig.ComputeConfigProperty(
                max_capacity_units=123,
        
                # the properties below are optional
                availability_zone="availabilityZone",
                dns_name_servers="dnsNameServers",
                kms_key_id="kmsKeyId",
                min_capacity_units=123,
                multi_az=False,
                preferred_maintenance_window="preferredMaintenanceWindow",
                replication_subnet_group_id="replicationSubnetGroupId",
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            ),
            replication_config_identifier="replicationConfigIdentifier",
            replication_settings=replication_settings,
            replication_type="replicationType",
            resource_identifier="resourceIdentifier",
            source_endpoint_arn="sourceEndpointArn",
            supplemental_settings=supplemental_settings,
            table_mappings=table_mappings,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_endpoint_arn="targetEndpointArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compute_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReplicationConfig.ComputeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        replication_config_identifier: typing.Optional[builtins.str] = None,
        replication_settings: typing.Any = None,
        replication_type: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        source_endpoint_arn: typing.Optional[builtins.str] = None,
        supplemental_settings: typing.Any = None,
        table_mappings: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_endpoint_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param compute_config: Configuration parameters for provisioning an AWS DMS Serverless replication.
        :param replication_config_identifier: A unique identifier that you want to use to create a ``ReplicationConfigArn`` that is returned as part of the output from this action. You can then pass this output ``ReplicationConfigArn`` as the value of the ``ReplicationConfigArn`` option for other actions to identify both AWS DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.
        :param replication_settings: Optional JSON settings for AWS DMS Serverless replications that are provisioned using this replication configuration. For example, see `Change processing tuning settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html>`_ .
        :param replication_type: The type of AWS DMS Serverless replication to provision using this replication configuration. Possible values: - ``"full-load"`` - ``"cdc"`` - ``"full-load-and-cdc"``
        :param resource_identifier: Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource. For more information, see `Fine-grained access control using resource names and tags <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess>`_ .
        :param source_endpoint_arn: The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration.
        :param supplemental_settings: Optional JSON settings for specifying supplemental data. For more information, see `Specifying supplemental data for task settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html>`_ .
        :param table_mappings: JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration. For more information, see `Specifying table selection and transformations rules using JSON <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html>`_ .
        :param tags: One or more optional tags associated with resources used by the AWS DMS Serverless replication. For more information, see `Tagging resources in AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html>`_ .
        :param target_endpoint_arn: The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94680f790d4726b7c801a80c1413457134b08ba7f03ece13365f54d8fea28dbb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationConfigProps(
            compute_config=compute_config,
            replication_config_identifier=replication_config_identifier,
            replication_settings=replication_settings,
            replication_type=replication_type,
            resource_identifier=resource_identifier,
            source_endpoint_arn=source_endpoint_arn,
            supplemental_settings=supplemental_settings,
            table_mappings=table_mappings,
            tags=tags,
            target_endpoint_arn=target_endpoint_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18c39ba6b69d789f0a54c566e579c12f70e70d71e39a03a41e5e74f96e5e064f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__60c2c81b84c37c69f1a05883a3f08b5bac388736e426b8395fe01e4f20bd30af)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrReplicationConfigArn")
    def attr_replication_config_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Replication Config.

        :cloudformationAttribute: ReplicationConfigArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicationConfigArn"))

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
    @jsii.member(jsii_name="computeConfig")
    def compute_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfig.ComputeConfigProperty"]]:
        '''Configuration parameters for provisioning an AWS DMS Serverless replication.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfig.ComputeConfigProperty"]], jsii.get(self, "computeConfig"))

    @compute_config.setter
    def compute_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReplicationConfig.ComputeConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32966575e9a17251f77f3c3fd9f0bb4f54a2ab6b20a6253bb2e3f97654887c8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computeConfig", value)

    @builtins.property
    @jsii.member(jsii_name="replicationConfigIdentifier")
    def replication_config_identifier(self) -> typing.Optional[builtins.str]:
        '''A unique identifier that you want to use to create a ``ReplicationConfigArn`` that is returned as part of the output from this action.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationConfigIdentifier"))

    @replication_config_identifier.setter
    def replication_config_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0eda6e7fe61fa165d7afb96aba6536d12a18d3c374115a7c447ed9d37c61998)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationConfigIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSettings")
    def replication_settings(self) -> typing.Any:
        '''Optional JSON settings for AWS DMS Serverless replications that are provisioned using this replication configuration.'''
        return typing.cast(typing.Any, jsii.get(self, "replicationSettings"))

    @replication_settings.setter
    def replication_settings(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13c1acc7a82f208546609dcf4d8a9e2a00dabcf1c361d10d0f4f3604035d01cc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSettings", value)

    @builtins.property
    @jsii.member(jsii_name="replicationType")
    def replication_type(self) -> typing.Optional[builtins.str]:
        '''The type of AWS DMS Serverless replication to provision using this replication configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationType"))

    @replication_type.setter
    def replication_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__805ebea2610d6a01f26aed0eb893129ec908af9d73cbb47689f5d6c727f01381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationType", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9dfbba127aff370430ba7dccb2539bc163a4dc67c556711d3450abbd5c937247)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArn")
    def source_endpoint_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceEndpointArn"))

    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60be257dd07e3947c2b6c272e0798fe76f69b66051d6c2dfca413c2d616b936)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="supplementalSettings")
    def supplemental_settings(self) -> typing.Any:
        '''Optional JSON settings for specifying supplemental data.'''
        return typing.cast(typing.Any, jsii.get(self, "supplementalSettings"))

    @supplemental_settings.setter
    def supplemental_settings(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bcc39fb53e8639c570621f12a090b2b213567d85d495108a6b12db7f7442ee8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "supplementalSettings", value)

    @builtins.property
    @jsii.member(jsii_name="tableMappings")
    def table_mappings(self) -> typing.Any:
        '''JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration.'''
        return typing.cast(typing.Any, jsii.get(self, "tableMappings"))

    @table_mappings.setter
    def table_mappings(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__727026dd4d118a926dedb1245c81eb2e5065bead645e182231e1258e77153d2b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableMappings", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more optional tags associated with resources used by the AWS DMS Serverless replication.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f7a00e90f9a69724097ed67b1c9d994575c88df02b8ab67e96b098dd2bb1aea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targetEndpointArn")
    def target_endpoint_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "targetEndpointArn"))

    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ca6e7b9ff71eb3a98317ab9f9de43b76c48b035eddf3add1e2ff840fa9af02b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetEndpointArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_dms.CfnReplicationConfig.ComputeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "max_capacity_units": "maxCapacityUnits",
            "availability_zone": "availabilityZone",
            "dns_name_servers": "dnsNameServers",
            "kms_key_id": "kmsKeyId",
            "min_capacity_units": "minCapacityUnits",
            "multi_az": "multiAz",
            "preferred_maintenance_window": "preferredMaintenanceWindow",
            "replication_subnet_group_id": "replicationSubnetGroupId",
            "vpc_security_group_ids": "vpcSecurityGroupIds",
        },
    )
    class ComputeConfigProperty:
        def __init__(
            self,
            *,
            max_capacity_units: jsii.Number,
            availability_zone: typing.Optional[builtins.str] = None,
            dns_name_servers: typing.Optional[builtins.str] = None,
            kms_key_id: typing.Optional[builtins.str] = None,
            min_capacity_units: typing.Optional[jsii.Number] = None,
            multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            preferred_maintenance_window: typing.Optional[builtins.str] = None,
            replication_subnet_group_id: typing.Optional[builtins.str] = None,
            vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''Configuration parameters for provisioning an AWS DMS Serverless replication.

            :param max_capacity_units: Specifies the maximum value of the AWS DMS capacity units (DCUs) for which a given AWS DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the maximum value that you can specify for AWS DMS Serverless is 384. The ``MaxCapacityUnits`` parameter is the only DCU parameter you are required to specify.
            :param availability_zone: The Availability Zone where the AWS DMS Serverless replication using this configuration will run. The default value is a random, system-chosen Availability Zone in the configuration's AWS Region , for example, ``"us-west-2"`` . You can't set this parameter if the ``MultiAZ`` parameter is set to ``true`` .
            :param dns_name_servers: A list of custom DNS name servers supported for the AWS DMS Serverless replication to access your source or target database. This list overrides the default name servers supported by the AWS DMS Serverless replication. You can specify a comma-separated list of internet addresses for up to four DNS name servers. For example: ``"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"``
            :param kms_key_id: An AWS Key Management Service ( AWS KMS ) key Amazon Resource Name (ARN) that is used to encrypt the data during AWS DMS Serverless replication. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your Amazon Web Services account. Your AWS account has a different default encryption key for each AWS Region .
            :param min_capacity_units: Specifies the minimum value of the AWS DMS capacity units (DCUs) for which a given AWS DMS Serverless replication can be provisioned. A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the minimum DCU value that you can specify for AWS DMS Serverless is 1. If you don't set this value, AWS DMS sets this parameter to the minimum DCU value allowed, 1. If there is no current source activity, AWS DMS scales down your replication until it reaches the value specified in ``MinCapacityUnits`` .
            :param multi_az: Specifies whether the AWS DMS Serverless replication is a Multi-AZ deployment. You can't set the ``AvailabilityZone`` parameter if the ``MultiAZ`` parameter is set to ``true`` .
            :param preferred_maintenance_window: The weekly time range during which system maintenance can occur for the AWS DMS Serverless replication, in Universal Coordinated Time (UTC). The format is ``ddd:hh24:mi-ddd:hh24:mi`` . The default is a 30-minute window selected at random from an 8-hour block of time per AWS Region . This maintenance occurs on a random day of the week. Valid values for days of the week include ``Mon`` , ``Tue`` , ``Wed`` , ``Thu`` , ``Fri`` , ``Sat`` , and ``Sun`` . Constraints include a minimum 30-minute window.
            :param replication_subnet_group_id: Specifies a subnet group identifier to associate with the AWS DMS Serverless replication.
            :param vpc_security_group_ids: Specifies the virtual private cloud (VPC) security group to use with the AWS DMS Serverless replication. The VPC security group must work with the VPC containing the replication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_dms as dms
                
                compute_config_property = dms.CfnReplicationConfig.ComputeConfigProperty(
                    max_capacity_units=123,
                
                    # the properties below are optional
                    availability_zone="availabilityZone",
                    dns_name_servers="dnsNameServers",
                    kms_key_id="kmsKeyId",
                    min_capacity_units=123,
                    multi_az=False,
                    preferred_maintenance_window="preferredMaintenanceWindow",
                    replication_subnet_group_id="replicationSubnetGroupId",
                    vpc_security_group_ids=["vpcSecurityGroupIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cccd397fe05dc0de656d261a2e429c3413c0e550cfcb56b8936f9090bd7184f2)
                check_type(argname="argument max_capacity_units", value=max_capacity_units, expected_type=type_hints["max_capacity_units"])
                check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
                check_type(argname="argument dns_name_servers", value=dns_name_servers, expected_type=type_hints["dns_name_servers"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
                check_type(argname="argument min_capacity_units", value=min_capacity_units, expected_type=type_hints["min_capacity_units"])
                check_type(argname="argument multi_az", value=multi_az, expected_type=type_hints["multi_az"])
                check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
                check_type(argname="argument replication_subnet_group_id", value=replication_subnet_group_id, expected_type=type_hints["replication_subnet_group_id"])
                check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_capacity_units": max_capacity_units,
            }
            if availability_zone is not None:
                self._values["availability_zone"] = availability_zone
            if dns_name_servers is not None:
                self._values["dns_name_servers"] = dns_name_servers
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id
            if min_capacity_units is not None:
                self._values["min_capacity_units"] = min_capacity_units
            if multi_az is not None:
                self._values["multi_az"] = multi_az
            if preferred_maintenance_window is not None:
                self._values["preferred_maintenance_window"] = preferred_maintenance_window
            if replication_subnet_group_id is not None:
                self._values["replication_subnet_group_id"] = replication_subnet_group_id
            if vpc_security_group_ids is not None:
                self._values["vpc_security_group_ids"] = vpc_security_group_ids

        @builtins.property
        def max_capacity_units(self) -> jsii.Number:
            '''Specifies the maximum value of the AWS DMS capacity units (DCUs) for which a given AWS DMS Serverless replication can be provisioned.

            A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the maximum value that you can specify for AWS DMS Serverless is 384. The ``MaxCapacityUnits`` parameter is the only DCU parameter you are required to specify.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-maxcapacityunits
            '''
            result = self._values.get("max_capacity_units")
            assert result is not None, "Required property 'max_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def availability_zone(self) -> typing.Optional[builtins.str]:
            '''The Availability Zone where the AWS DMS Serverless replication using this configuration will run.

            The default value is a random, system-chosen Availability Zone in the configuration's AWS Region , for example, ``"us-west-2"`` . You can't set this parameter if the ``MultiAZ`` parameter is set to ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-availabilityzone
            '''
            result = self._values.get("availability_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dns_name_servers(self) -> typing.Optional[builtins.str]:
            '''A list of custom DNS name servers supported for the AWS DMS Serverless replication to access your source or target database.

            This list overrides the default name servers supported by the AWS DMS Serverless replication. You can specify a comma-separated list of internet addresses for up to four DNS name servers. For example: ``"1.1.1.1,2.2.2.2,3.3.3.3,4.4.4.4"``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-dnsnameservers
            '''
            result = self._values.get("dns_name_servers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''An AWS Key Management Service ( AWS KMS ) key Amazon Resource Name (ARN) that is used to encrypt the data during AWS DMS Serverless replication.

            If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

            AWS KMS creates the default encryption key for your Amazon Web Services account. Your AWS account has a different default encryption key for each AWS Region .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def min_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''Specifies the minimum value of the AWS DMS capacity units (DCUs) for which a given AWS DMS Serverless replication can be provisioned.

            A single DCU is 2GB of RAM, with 1 DCU as the minimum value allowed. The list of valid DCU values includes 1, 2, 4, 8, 16, 32, 64, 128, 192, 256, and 384. So, the minimum DCU value that you can specify for AWS DMS Serverless is 1. If you don't set this value, AWS DMS sets this parameter to the minimum DCU value allowed, 1. If there is no current source activity, AWS DMS scales down your replication until it reaches the value specified in ``MinCapacityUnits`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-mincapacityunits
            '''
            result = self._values.get("min_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def multi_az(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether the AWS DMS Serverless replication is a Multi-AZ deployment.

            You can't set the ``AvailabilityZone`` parameter if the ``MultiAZ`` parameter is set to ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-multiaz
            '''
            result = self._values.get("multi_az")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
            '''The weekly time range during which system maintenance can occur for the AWS DMS Serverless replication, in Universal Coordinated Time (UTC).

            The format is ``ddd:hh24:mi-ddd:hh24:mi`` .

            The default is a 30-minute window selected at random from an 8-hour block of time per AWS Region . This maintenance occurs on a random day of the week. Valid values for days of the week include ``Mon`` , ``Tue`` , ``Wed`` , ``Thu`` , ``Fri`` , ``Sat`` , and ``Sun`` .

            Constraints include a minimum 30-minute window.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-preferredmaintenancewindow
            '''
            result = self._values.get("preferred_maintenance_window")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def replication_subnet_group_id(self) -> typing.Optional[builtins.str]:
            '''Specifies a subnet group identifier to associate with the AWS DMS Serverless replication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-replicationsubnetgroupid
            '''
            result = self._values.get("replication_subnet_group_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies the virtual private cloud (VPC) security group to use with the AWS DMS Serverless replication.

            The VPC security group must work with the VPC containing the replication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-dms-replicationconfig-computeconfig.html#cfn-dms-replicationconfig-computeconfig-vpcsecuritygroupids
            '''
            result = self._values.get("vpc_security_group_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationConfigProps",
    jsii_struct_bases=[],
    name_mapping={
        "compute_config": "computeConfig",
        "replication_config_identifier": "replicationConfigIdentifier",
        "replication_settings": "replicationSettings",
        "replication_type": "replicationType",
        "resource_identifier": "resourceIdentifier",
        "source_endpoint_arn": "sourceEndpointArn",
        "supplemental_settings": "supplementalSettings",
        "table_mappings": "tableMappings",
        "tags": "tags",
        "target_endpoint_arn": "targetEndpointArn",
    },
)
class CfnReplicationConfigProps:
    def __init__(
        self,
        *,
        compute_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfig.ComputeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        replication_config_identifier: typing.Optional[builtins.str] = None,
        replication_settings: typing.Any = None,
        replication_type: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        source_endpoint_arn: typing.Optional[builtins.str] = None,
        supplemental_settings: typing.Any = None,
        table_mappings: typing.Any = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_endpoint_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationConfig``.

        :param compute_config: Configuration parameters for provisioning an AWS DMS Serverless replication.
        :param replication_config_identifier: A unique identifier that you want to use to create a ``ReplicationConfigArn`` that is returned as part of the output from this action. You can then pass this output ``ReplicationConfigArn`` as the value of the ``ReplicationConfigArn`` option for other actions to identify both AWS DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.
        :param replication_settings: Optional JSON settings for AWS DMS Serverless replications that are provisioned using this replication configuration. For example, see `Change processing tuning settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html>`_ .
        :param replication_type: The type of AWS DMS Serverless replication to provision using this replication configuration. Possible values: - ``"full-load"`` - ``"cdc"`` - ``"full-load-and-cdc"``
        :param resource_identifier: Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource. For more information, see `Fine-grained access control using resource names and tags <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess>`_ .
        :param source_endpoint_arn: The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration.
        :param supplemental_settings: Optional JSON settings for specifying supplemental data. For more information, see `Specifying supplemental data for task settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html>`_ .
        :param table_mappings: JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration. For more information, see `Specifying table selection and transformations rules using JSON <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html>`_ .
        :param tags: One or more optional tags associated with resources used by the AWS DMS Serverless replication. For more information, see `Tagging resources in AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html>`_ .
        :param target_endpoint_arn: The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            # replication_settings: Any
            # supplemental_settings: Any
            # table_mappings: Any
            
            cfn_replication_config_props = dms.CfnReplicationConfigProps(
                compute_config=dms.CfnReplicationConfig.ComputeConfigProperty(
                    max_capacity_units=123,
            
                    # the properties below are optional
                    availability_zone="availabilityZone",
                    dns_name_servers="dnsNameServers",
                    kms_key_id="kmsKeyId",
                    min_capacity_units=123,
                    multi_az=False,
                    preferred_maintenance_window="preferredMaintenanceWindow",
                    replication_subnet_group_id="replicationSubnetGroupId",
                    vpc_security_group_ids=["vpcSecurityGroupIds"]
                ),
                replication_config_identifier="replicationConfigIdentifier",
                replication_settings=replication_settings,
                replication_type="replicationType",
                resource_identifier="resourceIdentifier",
                source_endpoint_arn="sourceEndpointArn",
                supplemental_settings=supplemental_settings,
                table_mappings=table_mappings,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_endpoint_arn="targetEndpointArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae045521aeb34847358ce5837e2233ae9d158bb9756b046af6dbf7b3db07a492)
            check_type(argname="argument compute_config", value=compute_config, expected_type=type_hints["compute_config"])
            check_type(argname="argument replication_config_identifier", value=replication_config_identifier, expected_type=type_hints["replication_config_identifier"])
            check_type(argname="argument replication_settings", value=replication_settings, expected_type=type_hints["replication_settings"])
            check_type(argname="argument replication_type", value=replication_type, expected_type=type_hints["replication_type"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument source_endpoint_arn", value=source_endpoint_arn, expected_type=type_hints["source_endpoint_arn"])
            check_type(argname="argument supplemental_settings", value=supplemental_settings, expected_type=type_hints["supplemental_settings"])
            check_type(argname="argument table_mappings", value=table_mappings, expected_type=type_hints["table_mappings"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_endpoint_arn", value=target_endpoint_arn, expected_type=type_hints["target_endpoint_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compute_config is not None:
            self._values["compute_config"] = compute_config
        if replication_config_identifier is not None:
            self._values["replication_config_identifier"] = replication_config_identifier
        if replication_settings is not None:
            self._values["replication_settings"] = replication_settings
        if replication_type is not None:
            self._values["replication_type"] = replication_type
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if source_endpoint_arn is not None:
            self._values["source_endpoint_arn"] = source_endpoint_arn
        if supplemental_settings is not None:
            self._values["supplemental_settings"] = supplemental_settings
        if table_mappings is not None:
            self._values["table_mappings"] = table_mappings
        if tags is not None:
            self._values["tags"] = tags
        if target_endpoint_arn is not None:
            self._values["target_endpoint_arn"] = target_endpoint_arn

    @builtins.property
    def compute_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReplicationConfig.ComputeConfigProperty]]:
        '''Configuration parameters for provisioning an AWS DMS Serverless replication.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-computeconfig
        '''
        result = self._values.get("compute_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReplicationConfig.ComputeConfigProperty]], result)

    @builtins.property
    def replication_config_identifier(self) -> typing.Optional[builtins.str]:
        '''A unique identifier that you want to use to create a ``ReplicationConfigArn`` that is returned as part of the output from this action.

        You can then pass this output ``ReplicationConfigArn`` as the value of the ``ReplicationConfigArn`` option for other actions to identify both AWS DMS Serverless replications and replication configurations that you want those actions to operate on. For some actions, you can also use either this unique identifier or a corresponding ARN in action filters to identify the specific replication and replication configuration to operate on.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationconfigidentifier
        '''
        result = self._values.get("replication_config_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_settings(self) -> typing.Any:
        '''Optional JSON settings for AWS DMS Serverless replications that are provisioned using this replication configuration.

        For example, see `Change processing tuning settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.ChangeProcessingTuning.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationsettings
        '''
        result = self._values.get("replication_settings")
        return typing.cast(typing.Any, result)

    @builtins.property
    def replication_type(self) -> typing.Optional[builtins.str]:
        '''The type of AWS DMS Serverless replication to provision using this replication configuration.

        Possible values:

        - ``"full-load"``
        - ``"cdc"``
        - ``"full-load-and-cdc"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-replicationtype
        '''
        result = self._values.get("replication_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''Optional unique value or name that you set for a given resource that can be used to construct an Amazon Resource Name (ARN) for that resource.

        For more information, see `Fine-grained access control using resource names and tags <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#CHAP_Security.FineGrainedAccess>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_endpoint_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the source endpoint for this AWS DMS Serverless replication configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-sourceendpointarn
        '''
        result = self._values.get("source_endpoint_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def supplemental_settings(self) -> typing.Any:
        '''Optional JSON settings for specifying supplemental data.

        For more information, see `Specifying supplemental data for task settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-supplementalsettings
        '''
        result = self._values.get("supplemental_settings")
        return typing.cast(typing.Any, result)

    @builtins.property
    def table_mappings(self) -> typing.Any:
        '''JSON table mappings for AWS DMS Serverless replications that are provisioned using this replication configuration.

        For more information, see `Specifying table selection and transformations rules using JSON <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.SelectionTransformation.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-tablemappings
        '''
        result = self._values.get("table_mappings")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more optional tags associated with resources used by the AWS DMS Serverless replication.

        For more information, see `Tagging resources in AWS Database Migration Service <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tagging.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_endpoint_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the target endpoint for this AWS DMS serverless replication configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationconfig.html#cfn-dms-replicationconfig-targetendpointarn
        '''
        result = self._values.get("target_endpoint_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationConfigProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReplicationInstance(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationInstance",
):
    '''The ``AWS::DMS::ReplicationInstance`` resource creates an AWS DMS replication instance.

    To create a ReplicationInstance, you need permissions to create instances. You'll need similar permissions to terminate instances when you delete stacks with instances.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html
    :cloudformationResource: AWS::DMS::ReplicationInstance
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_replication_instance = dms.CfnReplicationInstance(self, "MyCfnReplicationInstance",
            replication_instance_class="replicationInstanceClass",
        
            # the properties below are optional
            allocated_storage=123,
            allow_major_version_upgrade=False,
            auto_minor_version_upgrade=False,
            availability_zone="availabilityZone",
            engine_version="engineVersion",
            kms_key_id="kmsKeyId",
            multi_az=False,
            preferred_maintenance_window="preferredMaintenanceWindow",
            publicly_accessible=False,
            replication_instance_identifier="replicationInstanceIdentifier",
            replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
            resource_identifier="resourceIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            vpc_security_group_ids=["vpcSecurityGroupIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        replication_instance_class: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        replication_instance_identifier: typing.Optional[builtins.str] = None,
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param replication_instance_class: The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .
        :param allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible. This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.
        :param auto_minor_version_upgrade: A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to ``true`` . Default: ``true``
        :param availability_zone: The Availability Zone that the replication instance will be created in. The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .
        :param engine_version: The engine version number of the replication instance. If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the data on the replication instance. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param multi_az: Specifies whether the replication instance is a Multi-AZ deployment. You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in UTC. *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week. *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun`` *Constraints* : Minimum 30-minute window.
        :param publicly_accessible: Specifies the accessibility options for the replication instance. A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .
        :param replication_instance_identifier: The replication instance identifier. This parameter is stored as a lowercase string. Constraints: - Must contain 1-63 alphanumeric characters or hyphens. - First character must be a letter. - Can't end with a hyphen or contain two consecutive hyphens. Example: ``myrepinstance``
        :param replication_subnet_group_identifier: A subnet group to associate with the replication instance.
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication instance.
        :param vpc_security_group_ids: Specifies the virtual private cloud (VPC) security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77ad0bed39c8ffa41b7998189a1d03defd3bc9e64d11468a83ada78f35f96476)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationInstanceProps(
            replication_instance_class=replication_instance_class,
            allocated_storage=allocated_storage,
            allow_major_version_upgrade=allow_major_version_upgrade,
            auto_minor_version_upgrade=auto_minor_version_upgrade,
            availability_zone=availability_zone,
            engine_version=engine_version,
            kms_key_id=kms_key_id,
            multi_az=multi_az,
            preferred_maintenance_window=preferred_maintenance_window,
            publicly_accessible=publicly_accessible,
            replication_instance_identifier=replication_instance_identifier,
            replication_subnet_group_identifier=replication_subnet_group_identifier,
            resource_identifier=resource_identifier,
            tags=tags,
            vpc_security_group_ids=vpc_security_group_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8de6ada60f039ddabbe587b229323336b1a43acf683484ca8b0e6676b37b42a9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__056481ab7ccb2a78700e9f0580d414c3d64ea31834c5d092596b92107efc2e87)
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
    @jsii.member(jsii_name="attrReplicationInstancePrivateIpAddresses")
    def attr_replication_instance_private_ip_addresses(self) -> builtins.str:
        '''One or more private IP addresses for the replication instance.

        :cloudformationAttribute: ReplicationInstancePrivateIpAddresses
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicationInstancePrivateIpAddresses"))

    @builtins.property
    @jsii.member(jsii_name="attrReplicationInstancePublicIpAddresses")
    def attr_replication_instance_public_ip_addresses(self) -> builtins.str:
        '''One or more public IP addresses for the replication instance.

        :cloudformationAttribute: ReplicationInstancePublicIpAddresses
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrReplicationInstancePublicIpAddresses"))

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
    @jsii.member(jsii_name="replicationInstanceClass")
    def replication_instance_class(self) -> builtins.str:
        '''The compute and memory capacity of the replication instance as defined for the specified replication instance class.'''
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceClass"))

    @replication_instance_class.setter
    def replication_instance_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09832a68a18b219cca2b96430b6178182193c29706dbb315af37a153eca4cdde)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceClass", value)

    @builtins.property
    @jsii.member(jsii_name="allocatedStorage")
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''The amount of storage (in gigabytes) to be initially allocated for the replication instance.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "allocatedStorage"))

    @allocated_storage.setter
    def allocated_storage(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b9e67dd6df4f96e5fbe4476427a0fec05fc31d81e20a170515a3acb1a5d1369)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allocatedStorage", value)

    @builtins.property
    @jsii.member(jsii_name="allowMajorVersionUpgrade")
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates that major version upgrades are allowed.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "allowMajorVersionUpgrade"))

    @allow_major_version_upgrade.setter
    def allow_major_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d542d7160e59f9611ad93908e6070b4d58a40287b9bb64428b6c6fdfd564831b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowMajorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="autoMinorVersionUpgrade")
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoMinorVersionUpgrade"))

    @auto_minor_version_upgrade.setter
    def auto_minor_version_upgrade(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a670c3f6412303c20ee8b484b6db57b09d69fe3bfd90a5002f50a95211ae920d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoMinorVersionUpgrade", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that the replication instance will be created in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee6e53d98bd50e381b61c765da3209f4c1b0aa394cf600eb2ccbafb35ce8af4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="engineVersion")
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The engine version number of the replication instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "engineVersion"))

    @engine_version.setter
    def engine_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d057c8319f7bf4d361b904777f661a4864eb7ad3c9a58d1f9f491601759c9956)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "engineVersion", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the data on the replication instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe6e8b360ba283be066d96a22e1ad4f7808a99bbbeb4988aed6418caf56c7b0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="multiAz")
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the replication instance is a Multi-AZ deployment.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "multiAz"))

    @multi_az.setter
    def multi_az(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15cd762d24a89b64d936fd024f99a77b04a531719743e2b8fc0fe1101c056518)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiAz", value)

    @builtins.property
    @jsii.member(jsii_name="preferredMaintenanceWindow")
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in UTC.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "preferredMaintenanceWindow"))

    @preferred_maintenance_window.setter
    def preferred_maintenance_window(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3624de443f0642843ae64062943a44b0b37d9aaf7365263558a992066fa413)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preferredMaintenanceWindow", value)

    @builtins.property
    @jsii.member(jsii_name="publiclyAccessible")
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies the accessibility options for the replication instance.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "publiclyAccessible"))

    @publicly_accessible.setter
    def publicly_accessible(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47cab327863ed0bd5c6846fe9c62673d11bac796afa3f7043664bf2daed7b5af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "publiclyAccessible", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceIdentifier")
    def replication_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''The replication instance identifier.

        This parameter is stored as a lowercase string.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationInstanceIdentifier"))

    @replication_instance_identifier.setter
    def replication_instance_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__402b46a802ca5d0ff866921876e55cf0e8bd91600bd78100df01d59637c6afa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupIdentifier")
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''A subnet group to associate with the replication instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupIdentifier"))

    @replication_subnet_group_identifier.setter
    def replication_subnet_group_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2553943d04f50c2d328b10b637b470619c78fe30b1745a6502b62a64ad270665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d537376d50c1da10f951999f623055e223ea0ef187139a647b2dc59433351ecf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the replication instance.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e9b076e4deeb27025899867a8af58f94e0b718991df1032113865eea27810a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="vpcSecurityGroupIds")
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the virtual private cloud (VPC) security group to be used with the replication instance.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "vpcSecurityGroupIds"))

    @vpc_security_group_ids.setter
    def vpc_security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2272874fc3b867238f325a525b2ac85dcf4945e3c079e6b738328ca05e4fdeb3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcSecurityGroupIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationInstanceProps",
    jsii_struct_bases=[],
    name_mapping={
        "replication_instance_class": "replicationInstanceClass",
        "allocated_storage": "allocatedStorage",
        "allow_major_version_upgrade": "allowMajorVersionUpgrade",
        "auto_minor_version_upgrade": "autoMinorVersionUpgrade",
        "availability_zone": "availabilityZone",
        "engine_version": "engineVersion",
        "kms_key_id": "kmsKeyId",
        "multi_az": "multiAz",
        "preferred_maintenance_window": "preferredMaintenanceWindow",
        "publicly_accessible": "publiclyAccessible",
        "replication_instance_identifier": "replicationInstanceIdentifier",
        "replication_subnet_group_identifier": "replicationSubnetGroupIdentifier",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
        "vpc_security_group_ids": "vpcSecurityGroupIds",
    },
)
class CfnReplicationInstanceProps:
    def __init__(
        self,
        *,
        replication_instance_class: builtins.str,
        allocated_storage: typing.Optional[jsii.Number] = None,
        allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        availability_zone: typing.Optional[builtins.str] = None,
        engine_version: typing.Optional[builtins.str] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        preferred_maintenance_window: typing.Optional[builtins.str] = None,
        publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        replication_instance_identifier: typing.Optional[builtins.str] = None,
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationInstance``.

        :param replication_instance_class: The compute and memory capacity of the replication instance as defined for the specified replication instance class. For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .
        :param allocated_storage: The amount of storage (in gigabytes) to be initially allocated for the replication instance.
        :param allow_major_version_upgrade: Indicates that major version upgrades are allowed. Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible. This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.
        :param auto_minor_version_upgrade: A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window. This parameter defaults to ``true`` . Default: ``true``
        :param availability_zone: The Availability Zone that the replication instance will be created in. The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .
        :param engine_version: The engine version number of the replication instance. If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.
        :param kms_key_id: An AWS KMS key identifier that is used to encrypt the data on the replication instance. If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .
        :param multi_az: Specifies whether the replication instance is a Multi-AZ deployment. You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .
        :param preferred_maintenance_window: The weekly time range during which system maintenance can occur, in UTC. *Format* : ``ddd:hh24:mi-ddd:hh24:mi`` *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week. *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun`` *Constraints* : Minimum 30-minute window.
        :param publicly_accessible: Specifies the accessibility options for the replication instance. A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .
        :param replication_instance_identifier: The replication instance identifier. This parameter is stored as a lowercase string. Constraints: - Must contain 1-63 alphanumeric characters or hyphens. - First character must be a letter. - Can't end with a hyphen or contain two consecutive hyphens. Example: ``myrepinstance``
        :param replication_subnet_group_identifier: A subnet group to associate with the replication instance.
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication instance.
        :param vpc_security_group_ids: Specifies the virtual private cloud (VPC) security group to be used with the replication instance. The VPC security group must work with the VPC containing the replication instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_replication_instance_props = dms.CfnReplicationInstanceProps(
                replication_instance_class="replicationInstanceClass",
            
                # the properties below are optional
                allocated_storage=123,
                allow_major_version_upgrade=False,
                auto_minor_version_upgrade=False,
                availability_zone="availabilityZone",
                engine_version="engineVersion",
                kms_key_id="kmsKeyId",
                multi_az=False,
                preferred_maintenance_window="preferredMaintenanceWindow",
                publicly_accessible=False,
                replication_instance_identifier="replicationInstanceIdentifier",
                replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                vpc_security_group_ids=["vpcSecurityGroupIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c195b8dd61348ff1d9f7bd70b0a5b897ad23028c6c9ea122bf051cb2a4cec2c7)
            check_type(argname="argument replication_instance_class", value=replication_instance_class, expected_type=type_hints["replication_instance_class"])
            check_type(argname="argument allocated_storage", value=allocated_storage, expected_type=type_hints["allocated_storage"])
            check_type(argname="argument allow_major_version_upgrade", value=allow_major_version_upgrade, expected_type=type_hints["allow_major_version_upgrade"])
            check_type(argname="argument auto_minor_version_upgrade", value=auto_minor_version_upgrade, expected_type=type_hints["auto_minor_version_upgrade"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument engine_version", value=engine_version, expected_type=type_hints["engine_version"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument multi_az", value=multi_az, expected_type=type_hints["multi_az"])
            check_type(argname="argument preferred_maintenance_window", value=preferred_maintenance_window, expected_type=type_hints["preferred_maintenance_window"])
            check_type(argname="argument publicly_accessible", value=publicly_accessible, expected_type=type_hints["publicly_accessible"])
            check_type(argname="argument replication_instance_identifier", value=replication_instance_identifier, expected_type=type_hints["replication_instance_identifier"])
            check_type(argname="argument replication_subnet_group_identifier", value=replication_subnet_group_identifier, expected_type=type_hints["replication_subnet_group_identifier"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument vpc_security_group_ids", value=vpc_security_group_ids, expected_type=type_hints["vpc_security_group_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_instance_class": replication_instance_class,
        }
        if allocated_storage is not None:
            self._values["allocated_storage"] = allocated_storage
        if allow_major_version_upgrade is not None:
            self._values["allow_major_version_upgrade"] = allow_major_version_upgrade
        if auto_minor_version_upgrade is not None:
            self._values["auto_minor_version_upgrade"] = auto_minor_version_upgrade
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if engine_version is not None:
            self._values["engine_version"] = engine_version
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if multi_az is not None:
            self._values["multi_az"] = multi_az
        if preferred_maintenance_window is not None:
            self._values["preferred_maintenance_window"] = preferred_maintenance_window
        if publicly_accessible is not None:
            self._values["publicly_accessible"] = publicly_accessible
        if replication_instance_identifier is not None:
            self._values["replication_instance_identifier"] = replication_instance_identifier
        if replication_subnet_group_identifier is not None:
            self._values["replication_subnet_group_identifier"] = replication_subnet_group_identifier
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags
        if vpc_security_group_ids is not None:
            self._values["vpc_security_group_ids"] = vpc_security_group_ids

    @builtins.property
    def replication_instance_class(self) -> builtins.str:
        '''The compute and memory capacity of the replication instance as defined for the specified replication instance class.

        For example, to specify the instance class dms.c4.large, set this parameter to ``"dms.c4.large"`` . For more information on the settings and capacities for the available replication instance classes, see `Selecting the right AWS DMS replication instance for your migration <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html#CHAP_ReplicationInstance.InDepth>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceclass
        '''
        result = self._values.get("replication_instance_class")
        assert result is not None, "Required property 'replication_instance_class' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allocated_storage(self) -> typing.Optional[jsii.Number]:
        '''The amount of storage (in gigabytes) to be initially allocated for the replication instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allocatedstorage
        '''
        result = self._values.get("allocated_storage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def allow_major_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates that major version upgrades are allowed.

        Changing this parameter does not result in an outage, and the change is asynchronously applied as soon as possible.

        This parameter must be set to ``true`` when specifying a value for the ``EngineVersion`` parameter that is a different major version than the replication instance's current version.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-allowmajorversionupgrade
        '''
        result = self._values.get("allow_major_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def auto_minor_version_upgrade(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''A value that indicates whether minor engine upgrades are applied automatically to the replication instance during the maintenance window.

        This parameter defaults to ``true`` .

        Default: ``true``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-autominorversionupgrade
        '''
        result = self._values.get("auto_minor_version_upgrade")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that the replication instance will be created in.

        The default value is a random, system-chosen Availability Zone in the endpoint's AWS Region , for example ``us-east-1d`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def engine_version(self) -> typing.Optional[builtins.str]:
        '''The engine version number of the replication instance.

        If an engine version number is not specified when a replication instance is created, the default is the latest engine version available.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-engineversion
        '''
        result = self._values.get("engine_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''An AWS KMS key identifier that is used to encrypt the data on the replication instance.

        If you don't specify a value for the ``KmsKeyId`` parameter, AWS DMS uses your default encryption key.

        AWS KMS creates the default encryption key for your AWS account . Your AWS account has a different default encryption key for each AWS Region .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_az(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the replication instance is a Multi-AZ deployment.

        You can't set the ``AvailabilityZone`` parameter if the Multi-AZ parameter is set to ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-multiaz
        '''
        result = self._values.get("multi_az")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def preferred_maintenance_window(self) -> typing.Optional[builtins.str]:
        '''The weekly time range during which system maintenance can occur, in UTC.

        *Format* : ``ddd:hh24:mi-ddd:hh24:mi``

        *Default* : A 30-minute window selected at random from an 8-hour block of time per AWS Region , occurring on a random day of the week.

        *Valid days* ( ``ddd`` ): ``Mon`` | ``Tue`` | ``Wed`` | ``Thu`` | ``Fri`` | ``Sat`` | ``Sun``

        *Constraints* : Minimum 30-minute window.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-preferredmaintenancewindow
        '''
        result = self._values.get("preferred_maintenance_window")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def publicly_accessible(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies the accessibility options for the replication instance.

        A value of ``true`` represents an instance with a public IP address. A value of ``false`` represents an instance with a private IP address. The default value is ``true`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-publiclyaccessible
        '''
        result = self._values.get("publicly_accessible")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def replication_instance_identifier(self) -> typing.Optional[builtins.str]:
        '''The replication instance identifier. This parameter is stored as a lowercase string.

        Constraints:

        - Must contain 1-63 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Can't end with a hyphen or contain two consecutive hyphens.

        Example: ``myrepinstance``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationinstanceidentifier
        '''
        result = self._values.get("replication_instance_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''A subnet group to associate with the replication instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-replicationsubnetgroupidentifier
        '''
        result = self._values.get("replication_subnet_group_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the replication instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def vpc_security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies the virtual private cloud (VPC) security group to be used with the replication instance.

        The VPC security group must work with the VPC containing the replication instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationinstance.html#cfn-dms-replicationinstance-vpcsecuritygroupids
        '''
        result = self._values.get("vpc_security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationInstanceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReplicationSubnetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationSubnetGroup",
):
    '''The ``AWS::DMS::ReplicationSubnetGroup`` resource creates an AWS DMS replication subnet group.

    Subnet groups must contain at least two subnets in two different Availability Zones in the same AWS Region .
    .. epigraph::

       Resource creation fails if the ``dms-vpc-role`` AWS Identity and Access Management ( IAM ) role doesn't already exist. For more information, see `Creating the IAM Roles to Use With the AWS CLI and AWS DMS API <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.APIRole.html>`_ in the *AWS Database Migration Service User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html
    :cloudformationResource: AWS::DMS::ReplicationSubnetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_replication_subnet_group = dms.CfnReplicationSubnetGroup(self, "MyCfnReplicationSubnetGroup",
            replication_subnet_group_description="replicationSubnetGroupDescription",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
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
        replication_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param replication_subnet_group_description: The description for the subnet group.
        :param subnet_ids: One or more subnet IDs to be assigned to the subnet group.
        :param replication_subnet_group_identifier: The identifier for the replication subnet group. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.
        :param tags: One or more tags to be assigned to the subnet group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42a93d0e4d6a84e7b2c7e166a509fe22487d8b2f69197bf1094b7b78e1a08efb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationSubnetGroupProps(
            replication_subnet_group_description=replication_subnet_group_description,
            subnet_ids=subnet_ids,
            replication_subnet_group_identifier=replication_subnet_group_identifier,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cbd6ed2b4c1e1decc7684eacd04461d0d62947a76bcda7ff2e42832c61eaf3d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e74d513a902e5c099bc385283c7b92264fe6f714192dcd0028499c87c0ceec40)
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupDescription")
    def replication_subnet_group_description(self) -> builtins.str:
        '''The description for the subnet group.'''
        return typing.cast(builtins.str, jsii.get(self, "replicationSubnetGroupDescription"))

    @replication_subnet_group_description.setter
    def replication_subnet_group_description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d909c13d7865691ec6500187b62c3440be766838954fdb7f9596c04333f4489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupDescription", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''One or more subnet IDs to be assigned to the subnet group.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39901919e58265bd08c68e7a3020f2c18c1eab151c6e7abc2c36a23e13e4ad87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="replicationSubnetGroupIdentifier")
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier for the replication subnet group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationSubnetGroupIdentifier"))

    @replication_subnet_group_identifier.setter
    def replication_subnet_group_identifier(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5816ca3fba920e525d95f66cb9a6b814a604c65126d99e0ac24793b4b83ff1a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationSubnetGroupIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the subnet group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2c3c4e17f3d3ba3275fed9a1aab23448ad30fccd5e22c0ae03edd65bc8ff2e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationSubnetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "replication_subnet_group_description": "replicationSubnetGroupDescription",
        "subnet_ids": "subnetIds",
        "replication_subnet_group_identifier": "replicationSubnetGroupIdentifier",
        "tags": "tags",
    },
)
class CfnReplicationSubnetGroupProps:
    def __init__(
        self,
        *,
        replication_subnet_group_description: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationSubnetGroup``.

        :param replication_subnet_group_description: The description for the subnet group.
        :param subnet_ids: One or more subnet IDs to be assigned to the subnet group.
        :param replication_subnet_group_identifier: The identifier for the replication subnet group. If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.
        :param tags: One or more tags to be assigned to the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_replication_subnet_group_props = dms.CfnReplicationSubnetGroupProps(
                replication_subnet_group_description="replicationSubnetGroupDescription",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                replication_subnet_group_identifier="replicationSubnetGroupIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3aafd89e16d92c494e27cd4b858bfa30a53c5b4c3ca60c15a5f73d6512b8612)
            check_type(argname="argument replication_subnet_group_description", value=replication_subnet_group_description, expected_type=type_hints["replication_subnet_group_description"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument replication_subnet_group_identifier", value=replication_subnet_group_identifier, expected_type=type_hints["replication_subnet_group_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "replication_subnet_group_description": replication_subnet_group_description,
            "subnet_ids": subnet_ids,
        }
        if replication_subnet_group_identifier is not None:
            self._values["replication_subnet_group_identifier"] = replication_subnet_group_identifier
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def replication_subnet_group_description(self) -> builtins.str:
        '''The description for the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupdescription
        '''
        result = self._values.get("replication_subnet_group_description")
        assert result is not None, "Required property 'replication_subnet_group_description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''One or more subnet IDs to be assigned to the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def replication_subnet_group_identifier(self) -> typing.Optional[builtins.str]:
        '''The identifier for the replication subnet group.

        If you don't specify a name, AWS CloudFormation generates a unique ID and uses that ID for the identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-replicationsubnetgroupidentifier
        '''
        result = self._values.get("replication_subnet_group_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the subnet group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationsubnetgroup.html#cfn-dms-replicationsubnetgroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationSubnetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnReplicationTask(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationTask",
):
    '''The ``AWS::DMS::ReplicationTask`` resource creates an AWS DMS replication task.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html
    :cloudformationResource: AWS::DMS::ReplicationTask
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_dms as dms
        
        cfn_replication_task = dms.CfnReplicationTask(self, "MyCfnReplicationTask",
            migration_type="migrationType",
            replication_instance_arn="replicationInstanceArn",
            source_endpoint_arn="sourceEndpointArn",
            table_mappings="tableMappings",
            target_endpoint_arn="targetEndpointArn",
        
            # the properties below are optional
            cdc_start_position="cdcStartPosition",
            cdc_start_time=123,
            cdc_stop_position="cdcStopPosition",
            replication_task_identifier="replicationTaskIdentifier",
            replication_task_settings="replicationTaskSettings",
            resource_identifier="resourceIdentifier",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            task_data="taskData"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[jsii.Number] = None,
        cdc_stop_position: typing.Optional[builtins.str] = None,
        replication_task_identifier: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param migration_type: The migration type. Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``
        :param replication_instance_arn: The Amazon Resource Name (ARN) of a replication instance.
        :param source_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.
        :param table_mappings: The table mappings for the task, in JSON format. For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .
        :param target_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start. Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error. The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format. Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"`` Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"`` Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”`` .. epigraph:: When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"`` Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``
        :param replication_task_identifier: An identifier for the replication task. Constraints: - Must contain 1-255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param replication_task_settings: Overall settings for the task, in JSON format. For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication task.
        :param task_data: Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see `Specifying Supplemental Data for Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html>`_ in the *AWS Database Migration Service User Guide.*
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd9891907ccbbff1ea14d14a5e54ee5d7bb976ca72f0b8bf69f14ef1b6abfb4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReplicationTaskProps(
            migration_type=migration_type,
            replication_instance_arn=replication_instance_arn,
            source_endpoint_arn=source_endpoint_arn,
            table_mappings=table_mappings,
            target_endpoint_arn=target_endpoint_arn,
            cdc_start_position=cdc_start_position,
            cdc_start_time=cdc_start_time,
            cdc_stop_position=cdc_stop_position,
            replication_task_identifier=replication_task_identifier,
            replication_task_settings=replication_task_settings,
            resource_identifier=resource_identifier,
            tags=tags,
            task_data=task_data,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d192fc1c2266461b88428508a524f5fc5fb09b6b5f8977da7f82655861c432a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fd861071fcb4010750b1aa8d3f1d784b4bdeed7c1127498452cd12f484f4aae)
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
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="migrationType")
    def migration_type(self) -> builtins.str:
        '''The migration type.'''
        return typing.cast(builtins.str, jsii.get(self, "migrationType"))

    @migration_type.setter
    def migration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a2d7db1f375c2eb85289daa210e397195c735edc0594acece968e9e3f82d279)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "migrationType", value)

    @builtins.property
    @jsii.member(jsii_name="replicationInstanceArn")
    def replication_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a replication instance.'''
        return typing.cast(builtins.str, jsii.get(self, "replicationInstanceArn"))

    @replication_instance_arn.setter
    def replication_instance_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e709e027364b9c4aa12a0ec67b3c5c693106edce0f31eac15786bf3e68264fa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationInstanceArn", value)

    @builtins.property
    @jsii.member(jsii_name="sourceEndpointArn")
    def source_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "sourceEndpointArn"))

    @source_endpoint_arn.setter
    def source_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b775185958b0123f87c513439fdb9eda838d692dd012b524dc3fb6ab433f467e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="tableMappings")
    def table_mappings(self) -> builtins.str:
        '''The table mappings for the task, in JSON format.'''
        return typing.cast(builtins.str, jsii.get(self, "tableMappings"))

    @table_mappings.setter
    def table_mappings(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e1554f3f8fac9be6e304509c0164e1677aa1b61b31af49fd7792c8ef5b5dedf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableMappings", value)

    @builtins.property
    @jsii.member(jsii_name="targetEndpointArn")
    def target_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.'''
        return typing.cast(builtins.str, jsii.get(self, "targetEndpointArn"))

    @target_endpoint_arn.setter
    def target_endpoint_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4ca9dfb966142087d009c3e30808a83bbbeb6258daa6ad5c3852d8c4951ab6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetEndpointArn", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStartPosition")
    def cdc_start_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to start.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStartPosition"))

    @cdc_start_position.setter
    def cdc_start_position(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e5b6a190ec7e6fa4d8f098e921e3964e9e278b81e54483059762ae2bedd23d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartPosition", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStartTime")
    def cdc_start_time(self) -> typing.Optional[jsii.Number]:
        '''Indicates the start time for a change data capture (CDC) operation.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "cdcStartTime"))

    @cdc_start_time.setter
    def cdc_start_time(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c0148017c2d95abc8b4f00353f65446218011f3d9d7319a3d4b65d0f4a5da634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStartTime", value)

    @builtins.property
    @jsii.member(jsii_name="cdcStopPosition")
    def cdc_stop_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to stop.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cdcStopPosition"))

    @cdc_stop_position.setter
    def cdc_stop_position(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6117dd7c6cf29911168934ab8376c68f4b18ba2c09744952230e79da9ca035bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cdcStopPosition", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskIdentifier")
    def replication_task_identifier(self) -> typing.Optional[builtins.str]:
        '''An identifier for the replication task.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskIdentifier"))

    @replication_task_identifier.setter
    def replication_task_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79c4c9f366c664854b019827e55c7db32243c996e962557a9eafb7393d43545d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="replicationTaskSettings")
    def replication_task_settings(self) -> typing.Optional[builtins.str]:
        '''Overall settings for the task, in JSON format.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "replicationTaskSettings"))

    @replication_task_settings.setter
    def replication_task_settings(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c154fa2dd4edd39838c39b94653df9e66c95542ef0ea24a97883c7f55608a45)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "replicationTaskSettings", value)

    @builtins.property
    @jsii.member(jsii_name="resourceIdentifier")
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceIdentifier"))

    @resource_identifier.setter
    def resource_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0d4ca56aa921ac8bd069b2f1998ad160a58977be3a22b054aea931d00840b7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the replication task.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a8fadfeae4645d0ebd875d4c0285d22d91319e75b8c434882a51c7205d677cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="taskData")
    def task_data(self) -> typing.Optional[builtins.str]:
        '''Supplemental information that the task requires to migrate the data for certain source and target endpoints.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "taskData"))

    @task_data.setter
    def task_data(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22dc69cf7eb1071bfc83826615b45d1eff66b8eccd5636322983df53e2f5ea82)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "taskData", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_dms.CfnReplicationTaskProps",
    jsii_struct_bases=[],
    name_mapping={
        "migration_type": "migrationType",
        "replication_instance_arn": "replicationInstanceArn",
        "source_endpoint_arn": "sourceEndpointArn",
        "table_mappings": "tableMappings",
        "target_endpoint_arn": "targetEndpointArn",
        "cdc_start_position": "cdcStartPosition",
        "cdc_start_time": "cdcStartTime",
        "cdc_stop_position": "cdcStopPosition",
        "replication_task_identifier": "replicationTaskIdentifier",
        "replication_task_settings": "replicationTaskSettings",
        "resource_identifier": "resourceIdentifier",
        "tags": "tags",
        "task_data": "taskData",
    },
)
class CfnReplicationTaskProps:
    def __init__(
        self,
        *,
        migration_type: builtins.str,
        replication_instance_arn: builtins.str,
        source_endpoint_arn: builtins.str,
        table_mappings: builtins.str,
        target_endpoint_arn: builtins.str,
        cdc_start_position: typing.Optional[builtins.str] = None,
        cdc_start_time: typing.Optional[jsii.Number] = None,
        cdc_stop_position: typing.Optional[builtins.str] = None,
        replication_task_identifier: typing.Optional[builtins.str] = None,
        replication_task_settings: typing.Optional[builtins.str] = None,
        resource_identifier: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        task_data: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnReplicationTask``.

        :param migration_type: The migration type. Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``
        :param replication_instance_arn: The Amazon Resource Name (ARN) of a replication instance.
        :param source_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.
        :param table_mappings: The table mappings for the task, in JSON format. For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .
        :param target_endpoint_arn: An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.
        :param cdc_start_position: Indicates when you want a change data capture (CDC) operation to start. Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error. The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format. Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"`` Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"`` Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”`` .. epigraph:: When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .
        :param cdc_start_time: Indicates the start time for a change data capture (CDC) operation.
        :param cdc_stop_position: Indicates when you want a change data capture (CDC) operation to stop. The value can be either server time or commit time. Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"`` Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``
        :param replication_task_identifier: An identifier for the replication task. Constraints: - Must contain 1-255 alphanumeric characters or hyphens. - First character must be a letter. - Cannot end with a hyphen or contain two consecutive hyphens.
        :param replication_task_settings: Overall settings for the task, in JSON format. For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .
        :param resource_identifier: A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object. The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` . For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .
        :param tags: One or more tags to be assigned to the replication task.
        :param task_data: Supplemental information that the task requires to migrate the data for certain source and target endpoints. For more information, see `Specifying Supplemental Data for Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html>`_ in the *AWS Database Migration Service User Guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_dms as dms
            
            cfn_replication_task_props = dms.CfnReplicationTaskProps(
                migration_type="migrationType",
                replication_instance_arn="replicationInstanceArn",
                source_endpoint_arn="sourceEndpointArn",
                table_mappings="tableMappings",
                target_endpoint_arn="targetEndpointArn",
            
                # the properties below are optional
                cdc_start_position="cdcStartPosition",
                cdc_start_time=123,
                cdc_stop_position="cdcStopPosition",
                replication_task_identifier="replicationTaskIdentifier",
                replication_task_settings="replicationTaskSettings",
                resource_identifier="resourceIdentifier",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                task_data="taskData"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4920f44d880c720b2c02a65d1faf8192932fd28814ace33c249f86ca2fdfed8d)
            check_type(argname="argument migration_type", value=migration_type, expected_type=type_hints["migration_type"])
            check_type(argname="argument replication_instance_arn", value=replication_instance_arn, expected_type=type_hints["replication_instance_arn"])
            check_type(argname="argument source_endpoint_arn", value=source_endpoint_arn, expected_type=type_hints["source_endpoint_arn"])
            check_type(argname="argument table_mappings", value=table_mappings, expected_type=type_hints["table_mappings"])
            check_type(argname="argument target_endpoint_arn", value=target_endpoint_arn, expected_type=type_hints["target_endpoint_arn"])
            check_type(argname="argument cdc_start_position", value=cdc_start_position, expected_type=type_hints["cdc_start_position"])
            check_type(argname="argument cdc_start_time", value=cdc_start_time, expected_type=type_hints["cdc_start_time"])
            check_type(argname="argument cdc_stop_position", value=cdc_stop_position, expected_type=type_hints["cdc_stop_position"])
            check_type(argname="argument replication_task_identifier", value=replication_task_identifier, expected_type=type_hints["replication_task_identifier"])
            check_type(argname="argument replication_task_settings", value=replication_task_settings, expected_type=type_hints["replication_task_settings"])
            check_type(argname="argument resource_identifier", value=resource_identifier, expected_type=type_hints["resource_identifier"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument task_data", value=task_data, expected_type=type_hints["task_data"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "migration_type": migration_type,
            "replication_instance_arn": replication_instance_arn,
            "source_endpoint_arn": source_endpoint_arn,
            "table_mappings": table_mappings,
            "target_endpoint_arn": target_endpoint_arn,
        }
        if cdc_start_position is not None:
            self._values["cdc_start_position"] = cdc_start_position
        if cdc_start_time is not None:
            self._values["cdc_start_time"] = cdc_start_time
        if cdc_stop_position is not None:
            self._values["cdc_stop_position"] = cdc_stop_position
        if replication_task_identifier is not None:
            self._values["replication_task_identifier"] = replication_task_identifier
        if replication_task_settings is not None:
            self._values["replication_task_settings"] = replication_task_settings
        if resource_identifier is not None:
            self._values["resource_identifier"] = resource_identifier
        if tags is not None:
            self._values["tags"] = tags
        if task_data is not None:
            self._values["task_data"] = task_data

    @builtins.property
    def migration_type(self) -> builtins.str:
        '''The migration type.

        Valid values: ``full-load`` | ``cdc`` | ``full-load-and-cdc``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-migrationtype
        '''
        result = self._values.get("migration_type")
        assert result is not None, "Required property 'migration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def replication_instance_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of a replication instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationinstancearn
        '''
        result = self._values.get("replication_instance_arn")
        assert result is not None, "Required property 'replication_instance_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the source endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-sourceendpointarn
        '''
        result = self._values.get("source_endpoint_arn")
        assert result is not None, "Required property 'source_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_mappings(self) -> builtins.str:
        '''The table mappings for the task, in JSON format.

        For more information, see `Using Table Mapping to Specify Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TableMapping.html>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tablemappings
        '''
        result = self._values.get("table_mappings")
        assert result is not None, "Required property 'table_mappings' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def target_endpoint_arn(self) -> builtins.str:
        '''An Amazon Resource Name (ARN) that uniquely identifies the target endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-targetendpointarn
        '''
        result = self._values.get("target_endpoint_arn")
        assert result is not None, "Required property 'target_endpoint_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cdc_start_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to start.

        Use either ``CdcStartPosition`` or ``CdcStartTime`` to specify when you want a CDC operation to start. Specifying both values results in an error.

        The value can be in date, checkpoint, log sequence number (LSN), or system change number (SCN) format.

        Here is a date example: ``--cdc-start-position "2018-03-08T12:12:12"``

        Here is a checkpoint example: ``--cdc-start-position "checkpoint:V1#27#mysql-bin-changelog.157832:1975:-1:2002:677883278264080:mysql-bin-changelog.157832:1876#0#0#*#0#93"``

        Here is an LSN example: ``--cdc-start-position “mysql-bin-changelog.000024:373”``
        .. epigraph::

           When you use this task setting with a source PostgreSQL database, a logical replication slot should already be created and associated with the source endpoint. You can verify this by setting the ``slotName`` extra connection attribute to the name of this logical replication slot. For more information, see `Extra Connection Attributes When Using PostgreSQL as a Source for AWS DMS <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.PostgreSQL.html#CHAP_Source.PostgreSQL.ConnectionAttrib>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstartposition
        '''
        result = self._values.get("cdc_start_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def cdc_start_time(self) -> typing.Optional[jsii.Number]:
        '''Indicates the start time for a change data capture (CDC) operation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstarttime
        '''
        result = self._values.get("cdc_start_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def cdc_stop_position(self) -> typing.Optional[builtins.str]:
        '''Indicates when you want a change data capture (CDC) operation to stop.

        The value can be either server time or commit time.

        Here is a server time example: ``--cdc-stop-position "server_time:2018-02-09T12:12:12"``

        Here is a commit time example: ``--cdc-stop-position "commit_time: 2018-02-09T12:12:12"``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-cdcstopposition
        '''
        result = self._values.get("cdc_stop_position")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_task_identifier(self) -> typing.Optional[builtins.str]:
        '''An identifier for the replication task.

        Constraints:

        - Must contain 1-255 alphanumeric characters or hyphens.
        - First character must be a letter.
        - Cannot end with a hyphen or contain two consecutive hyphens.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtaskidentifier
        '''
        result = self._values.get("replication_task_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def replication_task_settings(self) -> typing.Optional[builtins.str]:
        '''Overall settings for the task, in JSON format.

        For more information, see `Specifying Task Settings for AWS Database Migration Service Tasks <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.CustomizingTasks.TaskSettings.html>`_ in the *AWS Database Migration Service User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-replicationtasksettings
        '''
        result = self._values.get("replication_task_settings")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_identifier(self) -> typing.Optional[builtins.str]:
        '''A display name for the resource identifier at the end of the ``EndpointArn`` response parameter that is returned in the created ``Endpoint`` object.

        The value for this parameter can have up to 31 characters. It can contain only ASCII letters, digits, and hyphen ('-'). Also, it can't end with a hyphen or contain two consecutive hyphens, and can only begin with a letter, such as ``Example-App-ARN1`` .

        For example, this value might result in the ``EndpointArn`` value ``arn:aws:dms:eu-west-1:012345678901:rep:Example-App-ARN1`` . If you don't specify a ``ResourceIdentifier`` value, AWS DMS generates a default identifier value for the end of ``EndpointArn`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-resourceidentifier
        '''
        result = self._values.get("resource_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''One or more tags to be assigned to the replication task.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def task_data(self) -> typing.Optional[builtins.str]:
        '''Supplemental information that the task requires to migrate the data for certain source and target endpoints.

        For more information, see `Specifying Supplemental Data for Task Settings <https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.TaskData.html>`_ in the *AWS Database Migration Service User Guide.*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html#cfn-dms-replicationtask-taskdata
        '''
        result = self._values.get("task_data")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReplicationTaskProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCertificate",
    "CfnCertificateProps",
    "CfnDataProvider",
    "CfnDataProviderProps",
    "CfnEndpoint",
    "CfnEndpointProps",
    "CfnEventSubscription",
    "CfnEventSubscriptionProps",
    "CfnInstanceProfile",
    "CfnInstanceProfileProps",
    "CfnMigrationProject",
    "CfnMigrationProjectProps",
    "CfnReplicationConfig",
    "CfnReplicationConfigProps",
    "CfnReplicationInstance",
    "CfnReplicationInstanceProps",
    "CfnReplicationSubnetGroup",
    "CfnReplicationSubnetGroupProps",
    "CfnReplicationTask",
    "CfnReplicationTaskProps",
]

publication.publish()

def _typecheckingstub__f7c4a44b8a3c02f3f6ada86310479fa26dc0b32d4fba95316eb3faa446936347(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_identifier: typing.Optional[builtins.str] = None,
    certificate_pem: typing.Optional[builtins.str] = None,
    certificate_wallet: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec185f31d9affa5fa834d99f40ff8a27fcf34f84f01e6395782727e60768851f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__156b71bbee83d022775901dd6edb948295c746f554fa1406537af9a5b4771300(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f62a480b92e0600c6f9c24ec065961ca68c8267f28552593ff2bd04d1a6071d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__313faf62724606e0e1418e631be23b5d6929e5f5b5dc81d9efcf33f65b18ee6f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d761187c2ccc6e6454d7cb505d195a8e53d4bc1a28c7f3f46d3c576a1fb0671(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70c99920ee84fe825d1d27715d21a77c22d5de3f61e54de6d533397773981c50(
    *,
    certificate_identifier: typing.Optional[builtins.str] = None,
    certificate_pem: typing.Optional[builtins.str] = None,
    certificate_wallet: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf28699baa8f0b678c6576c66e1c53e33b16d9f9cc37b854d4edbc95bf024780(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    engine: builtins.str,
    data_provider_identifier: typing.Optional[builtins.str] = None,
    data_provider_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    exact_settings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c1b19747788e548c485229450a0322a76649d72c3ccc24727e3a33db1fbdf372(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f3e870b0edacc6af82460cb592fd3d971822bf9675e4fe90ee87e3566e0e6f4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__020de7951d6d70bc9d3efa600e1210f388dcd2776433c31a4e92b6afe9782ff2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05caa8991d8aa025161e83d5ae88c03b5b1d3dc49c14071f0728788a968f2568(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__454cfcd7845bc90fe7e1a58a73587247e646a6372c641c3514ea21f8d6f11777(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ecadd16a9c7e49c8bf8e1b2e26f904f253dbd4bbefc352e35330e2788cb60915(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4d016d92a836fecec39275d37ba39e9b434aac43e0b8d6b9a644a15bfff4ef8(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15d6e40a485e85376660625e14969b38fc293c419cb77e7880107c25ae376134(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97cc3506a599073ab7e0ec6de0479e22078eea7f9108a8ff9c54e506d212555c(
    *,
    engine: builtins.str,
    data_provider_identifier: typing.Optional[builtins.str] = None,
    data_provider_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    exact_settings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__738d71cd2300575c2c6537801f3dede195e2179cefcdceb9d0410340f5b1615e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    endpoint_type: builtins.str,
    engine_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    doc_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.DocDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.DynamoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint_identifier: typing.Optional[builtins.str] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    gcp_my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ibm_db2_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.IbmDb2SettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kafka_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.KafkaSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.KinesisSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    microsoft_sql_server_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MongoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MySqlSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    neptune_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.NeptuneSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    oracle_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.OracleSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    postgre_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.RedisSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.RedshiftSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    s3_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.S3SettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_name: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    sybase_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.SybaseSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f057bd27ac6280cd130ed12f9511a5cdfb108a079b1bda778b1eafc415ee366d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dabdd788a3f89fb25343348143b10c8f247445904b595e33249479bbe047aa2f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eda1263f706197fdf07170ebe2dd59f394f263e412b2d4e5dd097f6126b80995(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63622e2ea94914c36460dc51358529b45a8dccc7d4b2c8b2cd29cfa5a8a292c3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a24a958c0fb12c44c9cb90d3499e73f80f94637351708be30c85163fc7c3694(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7fa111faf4b7852de973ab5c9eef4a2e95048c2fb0e4c4677655ec5b350a002(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__964181ee2a910015024cb3f101a00f9f8185212a583fc0880419c4b8f4665704(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.DocDbSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1e66bdb10c14f72319011edd2b4677a0c649392f33602507802cb167a5121d5(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.DynamoDbSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a06f40e1959e428f7f5c27f542081cd85f979ba31209ebc3fe63da010fddb64(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.ElasticsearchSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92a35632be5509ee14e90879734777fda7c0b08f4db0213ccb6b20ac83182823(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e00122aa6cacf409b94a9e3ae515c70d887464581820b45e08ce367673072c58(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c3a8d92e577dbc9df7cec45318f33c1e0fcbdf463cc7dfd5569ea58f1d00c06(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.GcpMySQLSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44fef44c81ef6b8da87158243f0ccbedc43e7299d8652a35b098afa7a04a61c3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.IbmDb2SettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b7582d27225e5fe52e2294251941bf9c566610655a620a14039a2b6f9e42b21(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.KafkaSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ceccea684f95f5083095044bdbf739f8871dcf9b280587dfc9f741fad0e19969(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.KinesisSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f98695584c46299d7a2dcf051622c328dcc6be01c1ec45e4645a4976755b9b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0d6650a04db2e7248a94227234af24d3685774adf590b885acf6d9a8e46f33c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MicrosoftSqlServerSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c34d02d08d15c9c23ee3acd69fc24c805faf00f28977c15fc4904ad2240ff59(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MongoDbSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33dc654f9976a21468a898b3a1a83eab0b9827d20b4050ca617ac942a51a2bc3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.MySqlSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bf2bf255501ef1ab216d754bda1b21fd5c2d7fa8b9eb7aef6710a3a3486ac0e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.NeptuneSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b582a457202f3791a344c9af49ce79ffaf942cd191b44898b2f3c01b25dcc73(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.OracleSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8fd19a57de2f1cfb856e6db1169b1753391b1b029e1d88babd8e74254c6a135(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc21911fa58b80854e027035398d650995a4315e7a391656d88cbdffe85c10b8(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ae50808797b6c50dc9996fead375c4ab91f2b93a7e63dfb0f24b0eda9b51f9e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.PostgreSqlSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__804bbb4ffca52155c93eb3b6c86a39edc8f1c8e0f7285eed7a57484757768a01(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.RedisSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29371f2c2b4a796793306172c888eba1b4d13b9962006ea4ea55d37fd5168a89(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.RedshiftSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b0c28b3eb52d69409a66690703aa50b58092a39244a75cec0482fe1b15ddf90(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beebfa648d87c594a19d4f5008c375d047ed33feb9cda485735fdfbdf6778832(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.S3SettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47a4f86e530d3114bac695174df1fa4dfd6e883942abff5dbd2860264e4f021d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b43aa7a197c10a98a463aa675a5dab6fedd3c8ab62c561e6c675f9cbf2294ce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8233892017699d61eafcea4f1e10c7e0569b5267219badd590e4c1371d4b6fad(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEndpoint.SybaseSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8deb35cf3c053bed3738b0ba1313a78b00c19fe30ee591619e0da0e7a7a4be5(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b95c2f7591c459e1e407d93e4a7301b1635408431907ffa3cf1c028147952ba(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a8cdb9146705c1a54770bd05f52b51754d3652539f062721a2b89a9e45593717(
    *,
    docs_to_investigate: typing.Optional[jsii.Number] = None,
    extract_doc_id: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    nesting_level: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5fec091a86dd85d23a1c02ae7d2b8611a5b093400587254d7ab8c085313f61e(
    *,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b42a4ad0c21b34a6010425ced42894f16cb42370a9e17e351b058db62751a2c6(
    *,
    endpoint_uri: typing.Optional[builtins.str] = None,
    error_retry_duration: typing.Optional[jsii.Number] = None,
    full_load_error_percentage: typing.Optional[jsii.Number] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c426338e480f2fd367da249eee3d680fa0655f66784733cc1ee66376abd5e2(
    *,
    after_connect_script: typing.Optional[builtins.str] = None,
    clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    database_name: typing.Optional[builtins.str] = None,
    events_poll_interval: typing.Optional[jsii.Number] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parallel_load_threads: typing.Optional[jsii.Number] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    server_timezone: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d6fbc1cf195619dd4c4ec936108c9aa18b32dd75831ce4e5f419f51f377abef(
    *,
    current_lsn: typing.Optional[builtins.str] = None,
    keep_csv_files: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    load_timeout: typing.Optional[jsii.Number] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    max_k_bytes_per_read: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    set_data_capture_changes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    write_buffer_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ef2e1b1010b2e04e20a0f1bedb9c97d4fea3afa8fb07e8b223e6dec6cd661d7(
    *,
    broker: typing.Optional[builtins.str] = None,
    include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message_format: typing.Optional[builtins.str] = None,
    message_max_bytes: typing.Optional[jsii.Number] = None,
    no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    sasl_password: typing.Optional[builtins.str] = None,
    sasl_user_name: typing.Optional[builtins.str] = None,
    security_protocol: typing.Optional[builtins.str] = None,
    ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_client_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_client_key_arn: typing.Optional[builtins.str] = None,
    ssl_client_key_password: typing.Optional[builtins.str] = None,
    topic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5a51439b5e4a710a546672de30983c7b1b763f1ce8451c08fc99623fce9ed6d(
    *,
    include_control_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_null_and_empty: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_partition_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_table_alter_operations: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_transaction_details: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    message_format: typing.Optional[builtins.str] = None,
    no_hex_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    partition_include_schema_table: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    stream_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__200804814bec4b3dcdc4d865d66320326f539657f293b56ba530cb6a08841175(
    *,
    bcp_packet_size: typing.Optional[jsii.Number] = None,
    control_tables_file_group: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    force_lob_lookup: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    query_single_always_on_node: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    read_backup_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    safeguard_policy: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    tlog_access_mode: typing.Optional[builtins.str] = None,
    trim_space_in_char: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_bcp_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    username: typing.Optional[builtins.str] = None,
    use_third_party_backup_device: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f47aa57b2c4073da641cad41ba07cbd9f41d4616eed682a61b712170dcda03e0(
    *,
    auth_mechanism: typing.Optional[builtins.str] = None,
    auth_source: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    docs_to_investigate: typing.Optional[builtins.str] = None,
    extract_doc_id: typing.Optional[builtins.str] = None,
    nesting_level: typing.Optional[builtins.str] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_name: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e498a760044089b042c26e470ecb6641a0808cbad39ca3138efe525c32fd7b4f(
    *,
    after_connect_script: typing.Optional[builtins.str] = None,
    clean_source_metadata_on_mismatch: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    events_poll_interval: typing.Optional[jsii.Number] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parallel_load_threads: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_timezone: typing.Optional[builtins.str] = None,
    target_db_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18643502ff334362a3e0ace1eca2f5044f5a5e4bae5404b7919a779dd4b9da96(
    *,
    error_retry_duration: typing.Optional[jsii.Number] = None,
    iam_auth_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    max_retry_count: typing.Optional[jsii.Number] = None,
    s3_bucket_folder: typing.Optional[builtins.str] = None,
    s3_bucket_name: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7cce1496a9f9494141ae407b9fa752179dcdfea2913cf1fd3d74b79dbdb605c(
    *,
    access_alternate_directly: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    additional_archived_log_dest_id: typing.Optional[jsii.Number] = None,
    add_supplemental_logging: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    allow_select_nested_tables: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    archived_log_dest_id: typing.Optional[jsii.Number] = None,
    archived_logs_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    asm_password: typing.Optional[builtins.str] = None,
    asm_server: typing.Optional[builtins.str] = None,
    asm_user: typing.Optional[builtins.str] = None,
    char_length_semantics: typing.Optional[builtins.str] = None,
    direct_path_no_log: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    direct_path_parallel_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    enable_homogenous_tablespace: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    extra_archived_log_dest_ids: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[jsii.Number]]] = None,
    fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    number_datatype_scale: typing.Optional[jsii.Number] = None,
    oracle_path_prefix: typing.Optional[builtins.str] = None,
    parallel_asm_read_threads: typing.Optional[jsii.Number] = None,
    read_ahead_blocks: typing.Optional[jsii.Number] = None,
    read_table_space_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    replace_path_prefix: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    retry_interval: typing.Optional[jsii.Number] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_oracle_asm_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_oracle_asm_secret_id: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    security_db_encryption: typing.Optional[builtins.str] = None,
    security_db_encryption_name: typing.Optional[builtins.str] = None,
    spatial_data_option_to_geo_json_function_name: typing.Optional[builtins.str] = None,
    standby_delay_time: typing.Optional[jsii.Number] = None,
    use_alternate_folder_for_online: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_b_file: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_direct_path_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_logminer_reader: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_path_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f006252c94d67f9b7da655f75e078cda6ee89974586c55a2d16ba2775091e058(
    *,
    after_connect_script: typing.Optional[builtins.str] = None,
    babelfish_database_name: typing.Optional[builtins.str] = None,
    capture_ddls: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    database_mode: typing.Optional[builtins.str] = None,
    ddl_artifacts_schema: typing.Optional[builtins.str] = None,
    execute_timeout: typing.Optional[jsii.Number] = None,
    fail_tasks_on_lob_truncation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    heartbeat_enable: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    heartbeat_frequency: typing.Optional[jsii.Number] = None,
    heartbeat_schema: typing.Optional[builtins.str] = None,
    map_boolean_as_boolean: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    plugin_name: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    slot_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__011bfd078b664e3e69dd00e5da3734673e821b3644ee94fbbff42c5cd3e5b746(
    *,
    auth_password: typing.Optional[builtins.str] = None,
    auth_type: typing.Optional[builtins.str] = None,
    auth_user_name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    server_name: typing.Optional[builtins.str] = None,
    ssl_ca_certificate_arn: typing.Optional[builtins.str] = None,
    ssl_security_protocol: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__017ba234c381b7c658aebe454c862c9121467fb310463c84973a8df81bb614f1(
    *,
    accept_any_date: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    after_connect_script: typing.Optional[builtins.str] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    case_sensitive_names: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    comp_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    connection_timeout: typing.Optional[jsii.Number] = None,
    date_format: typing.Optional[builtins.str] = None,
    empty_as_null: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    explicit_ids: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    file_transfer_upload_streams: typing.Optional[jsii.Number] = None,
    load_timeout: typing.Optional[jsii.Number] = None,
    map_boolean_as_boolean: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    remove_quotes: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    replace_chars: typing.Optional[builtins.str] = None,
    replace_invalid_chars: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    time_format: typing.Optional[builtins.str] = None,
    trim_blanks: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    truncate_columns: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    write_buffer_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf3699d4ca56a7d5e4abdba623281a4b6de1d7578f7fe1bf3add9c31bb3c33fd(
    *,
    add_column_name: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    add_trailing_padding_character: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    bucket_folder: typing.Optional[builtins.str] = None,
    bucket_name: typing.Optional[builtins.str] = None,
    canned_acl_for_objects: typing.Optional[builtins.str] = None,
    cdc_inserts_and_updates: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cdc_inserts_only: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cdc_max_batch_interval: typing.Optional[jsii.Number] = None,
    cdc_min_file_size: typing.Optional[jsii.Number] = None,
    cdc_path: typing.Optional[builtins.str] = None,
    compression_type: typing.Optional[builtins.str] = None,
    csv_delimiter: typing.Optional[builtins.str] = None,
    csv_no_sup_value: typing.Optional[builtins.str] = None,
    csv_null_value: typing.Optional[builtins.str] = None,
    csv_row_delimiter: typing.Optional[builtins.str] = None,
    data_format: typing.Optional[builtins.str] = None,
    data_page_size: typing.Optional[jsii.Number] = None,
    date_partition_delimiter: typing.Optional[builtins.str] = None,
    date_partition_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    date_partition_sequence: typing.Optional[builtins.str] = None,
    date_partition_timezone: typing.Optional[builtins.str] = None,
    dict_page_size_limit: typing.Optional[jsii.Number] = None,
    enable_statistics: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encoding_type: typing.Optional[builtins.str] = None,
    encryption_mode: typing.Optional[builtins.str] = None,
    expected_bucket_owner: typing.Optional[builtins.str] = None,
    external_table_definition: typing.Optional[builtins.str] = None,
    glue_catalog_generation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ignore_header_rows: typing.Optional[jsii.Number] = None,
    include_op_for_full_load: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    max_file_size: typing.Optional[jsii.Number] = None,
    parquet_timestamp_in_millisecond: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    parquet_version: typing.Optional[builtins.str] = None,
    preserve_transactions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    rfc4180: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    row_group_length: typing.Optional[jsii.Number] = None,
    server_side_encryption_kms_key_id: typing.Optional[builtins.str] = None,
    service_access_role_arn: typing.Optional[builtins.str] = None,
    timestamp_column_name: typing.Optional[builtins.str] = None,
    use_csv_no_sup_value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_task_start_time_for_full_load_timestamp: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0193ec81432f45bd3d781189917549ea6b46383bd54edb4ce2f3cd3f08b07b4(
    *,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f339ae28a930c099a0a813d874222c50e581fbff0c5b98878c1f5ae0871a0236(
    *,
    endpoint_type: builtins.str,
    engine_name: builtins.str,
    certificate_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    doc_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.DocDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.DynamoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.ElasticsearchSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint_identifier: typing.Optional[builtins.str] = None,
    extra_connection_attributes: typing.Optional[builtins.str] = None,
    gcp_my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.GcpMySQLSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ibm_db2_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.IbmDb2SettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kafka_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.KafkaSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.KinesisSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    microsoft_sql_server_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MicrosoftSqlServerSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mongo_db_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MongoDbSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    my_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.MySqlSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    neptune_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.NeptuneSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    oracle_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.OracleSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    postgre_sql_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.PostgreSqlSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redis_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.RedisSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.RedshiftSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    s3_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.S3SettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    server_name: typing.Optional[builtins.str] = None,
    ssl_mode: typing.Optional[builtins.str] = None,
    sybase_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEndpoint.SybaseSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d3042ac05bcc07c1b704196991fd764899b9b67bfb7cba510adb9fdde82fea2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    sns_topic_arn: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_type: typing.Optional[builtins.str] = None,
    subscription_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a520e2d84ac9276dbb4367e25dcf72534a967d6d8ffc82a2a23176413a6d560c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b0fb4580db11b3e885f145de5fc0563bace437ccec3f99cc736c88d07578906(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__593d665e1b397d43ab850799dd046cefd2398ae5f20b75c1c583ffd38e44a267(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f9e6185bdbcfc8331ed5d83bf2fbaa37dd9cb811c4e70a7c8fa3cf2a9f73604(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81aa84e39b9b7bbdb179d4aaaf48fa31beb2f53900fa1922bc6eec95a164d353(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5edd33fe4079b583e104f1f4e62422a4260f4f203418e37a0cf7bcc1966c9565(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df31bd385d9a632c6d6aefb66fd10f1e20bfc574f4166fbdc97e9057812618dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff68707f28923ac91e18c59be07ef7df511b633754f39276fd09448e2df08f91(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80baa3035b4fe50b1e5040583141b0b892965c1bceea423668eba59b6a4693e0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1555cbc21ca1acdd6ec0e2aad881e8c61105a38d2f194a09e644f876547b64e6(
    *,
    sns_topic_arn: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    event_categories: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_type: typing.Optional[builtins.str] = None,
    subscription_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c72f2ad0340026b7e11a2dcfa2f16a6cc0dd6393207ad4c41449ed94d6f4a58(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    instance_profile_identifier: typing.Optional[builtins.str] = None,
    instance_profile_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    subnet_group_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8342c573d42f8c324d79b2e95f84d87e6e369d07fdb8d38ff3910d46a7fdbc9b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d34fee644628abdf39d7679305233b8f3684c6179e63a5b1d72923ca21dc8098(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7805a3c0f395e2f5616503be94a7a3d3a684e843abb549e10dafe313f3b6963e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98de871dda338355afedba4e4db5b2f2d06c3dac29d4225e710c03a257396bda(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__adc46e83492bd9e5c1b2998646230bbfaefa04312834f26a3704ed50fe6d3c73(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e1381637e90360c57a7887d83c6d85fd5d618213f81718da1dcf9c140a95966(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f4d581525fcc739af608fad445ea300f231676aaaddbc1fe7ef970e225bb1f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23bc9a7e8ff96ae22982668c0a90e427cd65f81443fa65b96881009765893978(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bab01c20133942c669cfa6364b41fe2f0884195135cdb484b907cd1d017de096(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dd1328bedaa07486f249a94e5cb045c3d86574e3e0b22d39915c10b0944c77d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18cb1326620745b811df71b6f775ffff322b6d7a24cc629d76bd1a938e4e1e10(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4acb79a955201c074f7475d3a51ea385cae01e682de7bd61381384953fb050e4(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb987e57079646d3b74d43384b58a2e19975492c1f1b317aba746e6fa1f47b4e(
    *,
    availability_zone: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    instance_profile_identifier: typing.Optional[builtins.str] = None,
    instance_profile_name: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    network_type: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    subnet_group_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_groups: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02169f44825ddf8b21ca2acf1c203831f0a34ba053b5b8f4fea59ef921f5b56d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    instance_profile_identifier: typing.Optional[builtins.str] = None,
    instance_profile_name: typing.Optional[builtins.str] = None,
    migration_project_creation_time: typing.Optional[builtins.str] = None,
    migration_project_identifier: typing.Optional[builtins.str] = None,
    migration_project_name: typing.Optional[builtins.str] = None,
    schema_conversion_application_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.SchemaConversionApplicationAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.DataProviderDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.DataProviderDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    transformation_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__065b1cff71013e652903120372025cf335be7540413e4796b5304cc45f7551ff(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca6cab78ffccaad1c9b4efb641e75a6a31291549ab60102fad047e242f4b2e7f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c4df3a27d190edf622a69f5bd243619958a52f12a7a2096b3c8915be11ee0d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb1088337e159a58c057cac4f84e3b23c6881a1c6ead507f336ae854ce449cc0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__69e488dc8697a5afa8fd5ad8a91be36da51b419476ffb73594779e6c292e3cd9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__812b2039dff2aa0cc8cc17107db06bd70989e3fa445f454e3410c74ec7c6255e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b554b998a3f49e6d6edda5123f6f8268659d40c8705e87858e33b1f6edcce8e6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57db7ced3b40ef7d0d29ee5e2525eaa55617b8369a29470dc7866521cffd6b47(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12a0e20b765f80d1bd487470e2ba2e107b2e528e71b3f54206b3fa21f1350973(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8248f02c8a28507c6fd7b69d9078ece62cf902113b4922ac2c3b1eb1efe99e47(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.SchemaConversionApplicationAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a00bd941d6a9f753e2588061a187fa267a4026e4ad4481a8223f35bfb06bc87c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.DataProviderDescriptorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8af1fc70b174a366c98ab2a01a5b731e43ae5aea452d554ac059c8709dc325(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e70fa24655fe3ca5e620c8a935fd467925c600296ae5d6c563060ae2bd7b8ebb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnMigrationProject.DataProviderDescriptorProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b22cebadf8cc06e1152ada0e5ac728f60ae06205a5b8fdd994f6a4353bbae96(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__299742754139f0f8b894350a42e410914b67658b976b2ba7cdd3a1e776217876(
    *,
    data_provider_arn: typing.Optional[builtins.str] = None,
    data_provider_identifier: typing.Optional[builtins.str] = None,
    data_provider_name: typing.Optional[builtins.str] = None,
    secrets_manager_access_role_arn: typing.Optional[builtins.str] = None,
    secrets_manager_secret_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__845461800c57296041434f4d61b34cd11fc19c1e5835ee02c0868f4fc30ae9c0(
    *,
    s3_bucket_path: typing.Optional[builtins.str] = None,
    s3_bucket_role_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d354515598618d1781b30321646570d53cc9d8150e99820d2ffc982f69de692(
    *,
    description: typing.Optional[builtins.str] = None,
    instance_profile_arn: typing.Optional[builtins.str] = None,
    instance_profile_identifier: typing.Optional[builtins.str] = None,
    instance_profile_name: typing.Optional[builtins.str] = None,
    migration_project_creation_time: typing.Optional[builtins.str] = None,
    migration_project_identifier: typing.Optional[builtins.str] = None,
    migration_project_name: typing.Optional[builtins.str] = None,
    schema_conversion_application_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.SchemaConversionApplicationAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.DataProviderDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_data_provider_descriptors: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnMigrationProject.DataProviderDescriptorProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    transformation_rules: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94680f790d4726b7c801a80c1413457134b08ba7f03ece13365f54d8fea28dbb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compute_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfig.ComputeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    replication_config_identifier: typing.Optional[builtins.str] = None,
    replication_settings: typing.Any = None,
    replication_type: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    source_endpoint_arn: typing.Optional[builtins.str] = None,
    supplemental_settings: typing.Any = None,
    table_mappings: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_endpoint_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18c39ba6b69d789f0a54c566e579c12f70e70d71e39a03a41e5e74f96e5e064f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60c2c81b84c37c69f1a05883a3f08b5bac388736e426b8395fe01e4f20bd30af(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32966575e9a17251f77f3c3fd9f0bb4f54a2ab6b20a6253bb2e3f97654887c8e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnReplicationConfig.ComputeConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0eda6e7fe61fa165d7afb96aba6536d12a18d3c374115a7c447ed9d37c61998(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13c1acc7a82f208546609dcf4d8a9e2a00dabcf1c361d10d0f4f3604035d01cc(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__805ebea2610d6a01f26aed0eb893129ec908af9d73cbb47689f5d6c727f01381(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9dfbba127aff370430ba7dccb2539bc163a4dc67c556711d3450abbd5c937247(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60be257dd07e3947c2b6c272e0798fe76f69b66051d6c2dfca413c2d616b936(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bcc39fb53e8639c570621f12a090b2b213567d85d495108a6b12db7f7442ee8(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__727026dd4d118a926dedb1245c81eb2e5065bead645e182231e1258e77153d2b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f7a00e90f9a69724097ed67b1c9d994575c88df02b8ab67e96b098dd2bb1aea(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ca6e7b9ff71eb3a98317ab9f9de43b76c48b035eddf3add1e2ff840fa9af02b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cccd397fe05dc0de656d261a2e429c3413c0e550cfcb56b8936f9090bd7184f2(
    *,
    max_capacity_units: jsii.Number,
    availability_zone: typing.Optional[builtins.str] = None,
    dns_name_servers: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    min_capacity_units: typing.Optional[jsii.Number] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    replication_subnet_group_id: typing.Optional[builtins.str] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae045521aeb34847358ce5837e2233ae9d158bb9756b046af6dbf7b3db07a492(
    *,
    compute_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReplicationConfig.ComputeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    replication_config_identifier: typing.Optional[builtins.str] = None,
    replication_settings: typing.Any = None,
    replication_type: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    source_endpoint_arn: typing.Optional[builtins.str] = None,
    supplemental_settings: typing.Any = None,
    table_mappings: typing.Any = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_endpoint_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77ad0bed39c8ffa41b7998189a1d03defd3bc9e64d11468a83ada78f35f96476(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    replication_instance_class: builtins.str,
    allocated_storage: typing.Optional[jsii.Number] = None,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    replication_instance_identifier: typing.Optional[builtins.str] = None,
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8de6ada60f039ddabbe587b229323336b1a43acf683484ca8b0e6676b37b42a9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__056481ab7ccb2a78700e9f0580d414c3d64ea31834c5d092596b92107efc2e87(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09832a68a18b219cca2b96430b6178182193c29706dbb315af37a153eca4cdde(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b9e67dd6df4f96e5fbe4476427a0fec05fc31d81e20a170515a3acb1a5d1369(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d542d7160e59f9611ad93908e6070b4d58a40287b9bb64428b6c6fdfd564831b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a670c3f6412303c20ee8b484b6db57b09d69fe3bfd90a5002f50a95211ae920d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee6e53d98bd50e381b61c765da3209f4c1b0aa394cf600eb2ccbafb35ce8af4e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d057c8319f7bf4d361b904777f661a4864eb7ad3c9a58d1f9f491601759c9956(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe6e8b360ba283be066d96a22e1ad4f7808a99bbbeb4988aed6418caf56c7b0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15cd762d24a89b64d936fd024f99a77b04a531719743e2b8fc0fe1101c056518(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3624de443f0642843ae64062943a44b0b37d9aaf7365263558a992066fa413(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47cab327863ed0bd5c6846fe9c62673d11bac796afa3f7043664bf2daed7b5af(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__402b46a802ca5d0ff866921876e55cf0e8bd91600bd78100df01d59637c6afa0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2553943d04f50c2d328b10b637b470619c78fe30b1745a6502b62a64ad270665(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d537376d50c1da10f951999f623055e223ea0ef187139a647b2dc59433351ecf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e9b076e4deeb27025899867a8af58f94e0b718991df1032113865eea27810a7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2272874fc3b867238f325a525b2ac85dcf4945e3c079e6b738328ca05e4fdeb3(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c195b8dd61348ff1d9f7bd70b0a5b897ad23028c6c9ea122bf051cb2a4cec2c7(
    *,
    replication_instance_class: builtins.str,
    allocated_storage: typing.Optional[jsii.Number] = None,
    allow_major_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auto_minor_version_upgrade: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    availability_zone: typing.Optional[builtins.str] = None,
    engine_version: typing.Optional[builtins.str] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    multi_az: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    preferred_maintenance_window: typing.Optional[builtins.str] = None,
    publicly_accessible: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    replication_instance_identifier: typing.Optional[builtins.str] = None,
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42a93d0e4d6a84e7b2c7e166a509fe22487d8b2f69197bf1094b7b78e1a08efb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    replication_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cbd6ed2b4c1e1decc7684eacd04461d0d62947a76bcda7ff2e42832c61eaf3d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e74d513a902e5c099bc385283c7b92264fe6f714192dcd0028499c87c0ceec40(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d909c13d7865691ec6500187b62c3440be766838954fdb7f9596c04333f4489(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39901919e58265bd08c68e7a3020f2c18c1eab151c6e7abc2c36a23e13e4ad87(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5816ca3fba920e525d95f66cb9a6b814a604c65126d99e0ac24793b4b83ff1a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2c3c4e17f3d3ba3275fed9a1aab23448ad30fccd5e22c0ae03edd65bc8ff2e7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3aafd89e16d92c494e27cd4b858bfa30a53c5b4c3ca60c15a5f73d6512b8612(
    *,
    replication_subnet_group_description: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    replication_subnet_group_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd9891907ccbbff1ea14d14a5e54ee5d7bb976ca72f0b8bf69f14ef1b6abfb4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    migration_type: builtins.str,
    replication_instance_arn: builtins.str,
    source_endpoint_arn: builtins.str,
    table_mappings: builtins.str,
    target_endpoint_arn: builtins.str,
    cdc_start_position: typing.Optional[builtins.str] = None,
    cdc_start_time: typing.Optional[jsii.Number] = None,
    cdc_stop_position: typing.Optional[builtins.str] = None,
    replication_task_identifier: typing.Optional[builtins.str] = None,
    replication_task_settings: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d192fc1c2266461b88428508a524f5fc5fb09b6b5f8977da7f82655861c432a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fd861071fcb4010750b1aa8d3f1d784b4bdeed7c1127498452cd12f484f4aae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a2d7db1f375c2eb85289daa210e397195c735edc0594acece968e9e3f82d279(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e709e027364b9c4aa12a0ec67b3c5c693106edce0f31eac15786bf3e68264fa8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b775185958b0123f87c513439fdb9eda838d692dd012b524dc3fb6ab433f467e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e1554f3f8fac9be6e304509c0164e1677aa1b61b31af49fd7792c8ef5b5dedf(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4ca9dfb966142087d009c3e30808a83bbbeb6258daa6ad5c3852d8c4951ab6a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e5b6a190ec7e6fa4d8f098e921e3964e9e278b81e54483059762ae2bedd23d1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c0148017c2d95abc8b4f00353f65446218011f3d9d7319a3d4b65d0f4a5da634(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6117dd7c6cf29911168934ab8376c68f4b18ba2c09744952230e79da9ca035bf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79c4c9f366c664854b019827e55c7db32243c996e962557a9eafb7393d43545d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c154fa2dd4edd39838c39b94653df9e66c95542ef0ea24a97883c7f55608a45(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0d4ca56aa921ac8bd069b2f1998ad160a58977be3a22b054aea931d00840b7a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a8fadfeae4645d0ebd875d4c0285d22d91319e75b8c434882a51c7205d677cb(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22dc69cf7eb1071bfc83826615b45d1eff66b8eccd5636322983df53e2f5ea82(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4920f44d880c720b2c02a65d1faf8192932fd28814ace33c249f86ca2fdfed8d(
    *,
    migration_type: builtins.str,
    replication_instance_arn: builtins.str,
    source_endpoint_arn: builtins.str,
    table_mappings: builtins.str,
    target_endpoint_arn: builtins.str,
    cdc_start_position: typing.Optional[builtins.str] = None,
    cdc_start_time: typing.Optional[jsii.Number] = None,
    cdc_stop_position: typing.Optional[builtins.str] = None,
    replication_task_identifier: typing.Optional[builtins.str] = None,
    replication_task_settings: typing.Optional[builtins.str] = None,
    resource_identifier: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    task_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
