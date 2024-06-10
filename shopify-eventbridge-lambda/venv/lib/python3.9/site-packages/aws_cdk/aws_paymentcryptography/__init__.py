'''
# AWS::PaymentCryptography Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_paymentcryptography as paymentcryptography
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for PaymentCryptography construct libraries](https://constructs.dev/search?q=paymentcryptography)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::PaymentCryptography resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PaymentCryptography.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::PaymentCryptography](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_PaymentCryptography.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnAlias(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_paymentcryptography.CfnAlias",
):
    '''Creates an *alias* , or a friendly name, for an AWS Payment Cryptography key.

    You can use an alias to identify a key in the console and when you call cryptographic operations such as `EncryptData <https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_EncryptData.html>`_ or `DecryptData <https://docs.aws.amazon.com/payment-cryptography/latest/DataAPIReference/API_DecryptData.html>`_ .

    You can associate the alias with any key in the same AWS Region . Each alias is associated with only one key at a time, but a key can have multiple aliases. You can't create an alias without a key. The alias must be unique in the account and AWS Region , but you can create another alias with the same name in a different AWS Region .

    To change the key that's associated with the alias, call `UpdateAlias <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html>`_ . To delete the alias, call `DeleteAlias <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html>`_ . These operations don't affect the underlying key. To get the alias that you created, call `ListAliases <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html>`_ .

    *Cross-account use* : This operation can't be used across different AWS accounts.

    *Related operations:*

    - `DeleteAlias <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html>`_
    - `GetAlias <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html>`_
    - `ListAliases <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html>`_
    - `UpdateAlias <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-alias.html
    :cloudformationResource: AWS::PaymentCryptography::Alias
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_paymentcryptography as paymentcryptography
        
        cfn_alias = paymentcryptography.CfnAlias(self, "MyCfnAlias",
            alias_name="aliasName",
        
            # the properties below are optional
            key_arn="keyArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        alias_name: builtins.str,
        key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param alias_name: A friendly name that you can use to refer to a key. The value must begin with ``alias/`` . .. epigraph:: Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
        :param key_arn: The ``KeyARN`` of the key associated with the alias.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03e3543c569149d753dcca4f9aa62f90766372bafcd1f94b89e73d5b425564e5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAliasProps(alias_name=alias_name, key_arn=key_arn)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4ff200923cccd5fdae928ff708195bbced1ef4f7d50f668b5c73f249ed90f28f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b8f80ee3646838aabf7e90939e0251f8840c956ccf920965fde8a918b4cbf79b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aliasName")
    def alias_name(self) -> builtins.str:
        '''A friendly name that you can use to refer to a key.

        The value must begin with ``alias/`` .
        '''
        return typing.cast(builtins.str, jsii.get(self, "aliasName"))

    @alias_name.setter
    def alias_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbda40ab380bdefcb4b1f97fbdfb383ed08815fcaf1d136e881314e872f7e42b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasName", value)

    @builtins.property
    @jsii.member(jsii_name="keyArn")
    def key_arn(self) -> typing.Optional[builtins.str]:
        '''The ``KeyARN`` of the key associated with the alias.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyArn"))

    @key_arn.setter
    def key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fbafef3a7fe6a4ee77cdd86bde1df29b8df0e985f7099527ccce1ce9c0fb18d5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_paymentcryptography.CfnAliasProps",
    jsii_struct_bases=[],
    name_mapping={"alias_name": "aliasName", "key_arn": "keyArn"},
)
class CfnAliasProps:
    def __init__(
        self,
        *,
        alias_name: builtins.str,
        key_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnAlias``.

        :param alias_name: A friendly name that you can use to refer to a key. The value must begin with ``alias/`` . .. epigraph:: Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
        :param key_arn: The ``KeyARN`` of the key associated with the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-alias.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_paymentcryptography as paymentcryptography
            
            cfn_alias_props = paymentcryptography.CfnAliasProps(
                alias_name="aliasName",
            
                # the properties below are optional
                key_arn="keyArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0461ccf0903c4c242ef15c5e4bc2830b51a5cf5ebc2b326557f67cfef92bc428)
            check_type(argname="argument alias_name", value=alias_name, expected_type=type_hints["alias_name"])
            check_type(argname="argument key_arn", value=key_arn, expected_type=type_hints["key_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "alias_name": alias_name,
        }
        if key_arn is not None:
            self._values["key_arn"] = key_arn

    @builtins.property
    def alias_name(self) -> builtins.str:
        '''A friendly name that you can use to refer to a key. The value must begin with ``alias/`` .

        .. epigraph::

           Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-alias.html#cfn-paymentcryptography-alias-aliasname
        '''
        result = self._values.get("alias_name")
        assert result is not None, "Required property 'alias_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_arn(self) -> typing.Optional[builtins.str]:
        '''The ``KeyARN`` of the key associated with the alias.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-alias.html#cfn-paymentcryptography-alias-keyarn
        '''
        result = self._values.get("key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAliasProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_paymentcryptography.CfnKey",
):
    '''Creates an AWS Payment Cryptography key, a logical representation of a cryptographic key, that is unique in your account and AWS Region .

    You use keys for cryptographic functions such as encryption and decryption.

    In addition to the key material used in cryptographic operations, an AWS Payment Cryptography key includes metadata such as the key ARN, key usage, key origin, creation date, description, and key state.

    When you create a key, you specify both immutable and mutable data about the key. The immutable data contains key attributes that define the scope and cryptographic operations that you can perform using the key, for example key class (example: ``SYMMETRIC_KEY`` ), key algorithm (example: ``TDES_2KEY`` ), key usage (example: ``TR31_P0_PIN_ENCRYPTION_KEY`` ) and key modes of use (example: ``Encrypt`` ). For information about valid combinations of key attributes, see `Understanding key attributes <https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-validattributes.html>`_ in the *AWS Payment Cryptography User Guide* . The mutable data contained within a key includes usage timestamp and key deletion timestamp and can be modified after creation.

    AWS Payment Cryptography binds key attributes to keys using key blocks when you store or export them. AWS Payment Cryptography stores the key contents wrapped and never stores or transmits them in the clear.

    *Cross-account use* : This operation can't be used across different AWS accounts.

    *Related operations:*

    - `DeleteKey <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteKey.html>`_
    - `GetKey <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetKey.html>`_
    - `ListKeys <https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListKeys.html>`_

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html
    :cloudformationResource: AWS::PaymentCryptography::Key
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_paymentcryptography as paymentcryptography
        
        cfn_key = paymentcryptography.CfnKey(self, "MyCfnKey",
            exportable=False,
            key_attributes=paymentcryptography.CfnKey.KeyAttributesProperty(
                key_algorithm="keyAlgorithm",
                key_class="keyClass",
                key_modes_of_use=paymentcryptography.CfnKey.KeyModesOfUseProperty(
                    decrypt=False,
                    derive_key=False,
                    encrypt=False,
                    generate=False,
                    no_restrictions=False,
                    sign=False,
                    unwrap=False,
                    verify=False,
                    wrap=False
                ),
                key_usage="keyUsage"
            ),
        
            # the properties below are optional
            enabled=False,
            key_check_value_algorithm="keyCheckValueAlgorithm",
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
        exportable: typing.Union[builtins.bool, _IResolvable_da3f097b],
        key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union["CfnKey.KeyAttributesProperty", typing.Dict[builtins.str, typing.Any]]],
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        key_check_value_algorithm: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param exportable: Specifies whether the key is exportable. This data is immutable after the key is created.
        :param key_attributes: The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
        :param enabled: Specifies whether the key is enabled.
        :param key_check_value_algorithm: The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity. For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eae3f8af01ec3a496044e22e7d1ce2b96cf8f20736ded57ce899a918f81a9596)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKeyProps(
            exportable=exportable,
            key_attributes=key_attributes,
            enabled=enabled,
            key_check_value_algorithm=key_check_value_algorithm,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d0701d054ede99cce0d90b76ac7d1ff4eb40159e6fd502b56930a0b0a1cb63c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__67d0864ea174d57204bcc36c049839be306d7849f2c1c3dc30e1a6292d6885fd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyIdentifier")
    def attr_key_identifier(self) -> builtins.str:
        '''
        :cloudformationAttribute: KeyIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyOrigin")
    def attr_key_origin(self) -> builtins.str:
        '''The source of the key material.

        For keys created within AWS Payment Cryptography, the value is ``AWS_PAYMENT_CRYPTOGRAPHY`` . For keys imported into AWS Payment Cryptography, the value is ``EXTERNAL`` .

        :cloudformationAttribute: KeyOrigin
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyOrigin"))

    @builtins.property
    @jsii.member(jsii_name="attrKeyState")
    def attr_key_state(self) -> builtins.str:
        '''The state of key that is being created or deleted.

        :cloudformationAttribute: KeyState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrKeyState"))

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
    @jsii.member(jsii_name="exportable")
    def exportable(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Specifies whether the key is exportable.'''
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], jsii.get(self, "exportable"))

    @exportable.setter
    def exportable(
        self,
        value: typing.Union[builtins.bool, _IResolvable_da3f097b],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f21c25b942e06e9156561ac93e6371242b5b4ddbcb85077df885feaa89b2b2a6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "exportable", value)

    @builtins.property
    @jsii.member(jsii_name="keyAttributes")
    def key_attributes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnKey.KeyAttributesProperty"]:
        '''The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnKey.KeyAttributesProperty"], jsii.get(self, "keyAttributes"))

    @key_attributes.setter
    def key_attributes(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnKey.KeyAttributesProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__509385bb900abd87d7e9680c46b008a76766e5f51864d21972df261f9db73156)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the key is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1defb803536cf97ac83055a5760a6073dfc007fbfe2b34f9a774538091a30ef3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="keyCheckValueAlgorithm")
    def key_check_value_algorithm(self) -> typing.Optional[builtins.str]:
        '''The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyCheckValueAlgorithm"))

    @key_check_value_algorithm.setter
    def key_check_value_algorithm(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__197ab67a28372d3c264e1414d929d0c2287a028faf7915197718c789307d1350)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyCheckValueAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78d5368ca44b0ca5acba26b914716e9d9e8bb1acb0511f4f2a701cf6fcdd968d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_paymentcryptography.CfnKey.KeyAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "key_algorithm": "keyAlgorithm",
            "key_class": "keyClass",
            "key_modes_of_use": "keyModesOfUse",
            "key_usage": "keyUsage",
        },
    )
    class KeyAttributesProperty:
        def __init__(
            self,
            *,
            key_algorithm: builtins.str,
            key_class: builtins.str,
            key_modes_of_use: typing.Union[_IResolvable_da3f097b, typing.Union["CfnKey.KeyModesOfUseProperty", typing.Dict[builtins.str, typing.Any]]],
            key_usage: builtins.str,
        ) -> None:
            '''The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key.

            This data is immutable after the key is created.

            :param key_algorithm: The key algorithm to be use during creation of an AWS Payment Cryptography key. For symmetric keys, AWS Payment Cryptography supports ``AES`` and ``TDES`` algorithms. For asymmetric keys, AWS Payment Cryptography supports ``RSA`` and ``ECC_NIST`` algorithms.
            :param key_class: The type of AWS Payment Cryptography key to create, which determines the classiﬁcation of the cryptographic method and whether AWS Payment Cryptography key contains a symmetric key or an asymmetric key pair.
            :param key_modes_of_use: The list of cryptographic operations that you can perform using the key.
            :param key_usage: The cryptographic usage of an AWS Payment Cryptography key as deﬁned in section A.5.2 of the TR-31 spec.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keyattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_paymentcryptography as paymentcryptography
                
                key_attributes_property = paymentcryptography.CfnKey.KeyAttributesProperty(
                    key_algorithm="keyAlgorithm",
                    key_class="keyClass",
                    key_modes_of_use=paymentcryptography.CfnKey.KeyModesOfUseProperty(
                        decrypt=False,
                        derive_key=False,
                        encrypt=False,
                        generate=False,
                        no_restrictions=False,
                        sign=False,
                        unwrap=False,
                        verify=False,
                        wrap=False
                    ),
                    key_usage="keyUsage"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b75d16f6c2607cb760edf67dc96a26bed574dca4a5534dd5e3593befcc5f0a6)
                check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
                check_type(argname="argument key_class", value=key_class, expected_type=type_hints["key_class"])
                check_type(argname="argument key_modes_of_use", value=key_modes_of_use, expected_type=type_hints["key_modes_of_use"])
                check_type(argname="argument key_usage", value=key_usage, expected_type=type_hints["key_usage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_algorithm": key_algorithm,
                "key_class": key_class,
                "key_modes_of_use": key_modes_of_use,
                "key_usage": key_usage,
            }

        @builtins.property
        def key_algorithm(self) -> builtins.str:
            '''The key algorithm to be use during creation of an AWS Payment Cryptography key.

            For symmetric keys, AWS Payment Cryptography supports ``AES`` and ``TDES`` algorithms. For asymmetric keys, AWS Payment Cryptography supports ``RSA`` and ``ECC_NIST`` algorithms.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keyattributes.html#cfn-paymentcryptography-key-keyattributes-keyalgorithm
            '''
            result = self._values.get("key_algorithm")
            assert result is not None, "Required property 'key_algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_class(self) -> builtins.str:
            '''The type of AWS Payment Cryptography key to create, which determines the classiﬁcation of the cryptographic method and whether AWS Payment Cryptography key contains a symmetric key or an asymmetric key pair.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keyattributes.html#cfn-paymentcryptography-key-keyattributes-keyclass
            '''
            result = self._values.get("key_class")
            assert result is not None, "Required property 'key_class' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key_modes_of_use(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnKey.KeyModesOfUseProperty"]:
            '''The list of cryptographic operations that you can perform using the key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keyattributes.html#cfn-paymentcryptography-key-keyattributes-keymodesofuse
            '''
            result = self._values.get("key_modes_of_use")
            assert result is not None, "Required property 'key_modes_of_use' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnKey.KeyModesOfUseProperty"], result)

        @builtins.property
        def key_usage(self) -> builtins.str:
            '''The cryptographic usage of an AWS Payment Cryptography key as deﬁned in section A.5.2 of the TR-31 spec.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keyattributes.html#cfn-paymentcryptography-key-keyattributes-keyusage
            '''
            result = self._values.get("key_usage")
            assert result is not None, "Required property 'key_usage' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_paymentcryptography.CfnKey.KeyModesOfUseProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decrypt": "decrypt",
            "derive_key": "deriveKey",
            "encrypt": "encrypt",
            "generate": "generate",
            "no_restrictions": "noRestrictions",
            "sign": "sign",
            "unwrap": "unwrap",
            "verify": "verify",
            "wrap": "wrap",
        },
    )
    class KeyModesOfUseProperty:
        def __init__(
            self,
            *,
            decrypt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            derive_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            encrypt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            generate: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            no_restrictions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            unwrap: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            verify: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            wrap: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The list of cryptographic operations that you can perform using the key.

            The modes of use are deﬁned in section A.5.3 of the TR-31 spec.

            :param decrypt: Speciﬁes whether an AWS Payment Cryptography key can be used to decrypt data. Default: - false
            :param derive_key: Speciﬁes whether an AWS Payment Cryptography key can be used to derive new keys. Default: - false
            :param encrypt: Speciﬁes whether an AWS Payment Cryptography key can be used to encrypt data. Default: - false
            :param generate: Speciﬁes whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys. Default: - false
            :param no_restrictions: Speciﬁes whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by ``KeyUsage`` . Default: - false
            :param sign: Speciﬁes whether an AWS Payment Cryptography key can be used for signing. Default: - false
            :param unwrap: Default: - false
            :param verify: Speciﬁes whether an AWS Payment Cryptography key can be used to verify signatures. Default: - false
            :param wrap: Speciﬁes whether an AWS Payment Cryptography key can be used to wrap other keys. Default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_paymentcryptography as paymentcryptography
                
                key_modes_of_use_property = paymentcryptography.CfnKey.KeyModesOfUseProperty(
                    decrypt=False,
                    derive_key=False,
                    encrypt=False,
                    generate=False,
                    no_restrictions=False,
                    sign=False,
                    unwrap=False,
                    verify=False,
                    wrap=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19bb5a67c0e2112fa91ea214bcd53a4406d0b3e006c09d38e9c0cd851824cb05)
                check_type(argname="argument decrypt", value=decrypt, expected_type=type_hints["decrypt"])
                check_type(argname="argument derive_key", value=derive_key, expected_type=type_hints["derive_key"])
                check_type(argname="argument encrypt", value=encrypt, expected_type=type_hints["encrypt"])
                check_type(argname="argument generate", value=generate, expected_type=type_hints["generate"])
                check_type(argname="argument no_restrictions", value=no_restrictions, expected_type=type_hints["no_restrictions"])
                check_type(argname="argument sign", value=sign, expected_type=type_hints["sign"])
                check_type(argname="argument unwrap", value=unwrap, expected_type=type_hints["unwrap"])
                check_type(argname="argument verify", value=verify, expected_type=type_hints["verify"])
                check_type(argname="argument wrap", value=wrap, expected_type=type_hints["wrap"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if decrypt is not None:
                self._values["decrypt"] = decrypt
            if derive_key is not None:
                self._values["derive_key"] = derive_key
            if encrypt is not None:
                self._values["encrypt"] = encrypt
            if generate is not None:
                self._values["generate"] = generate
            if no_restrictions is not None:
                self._values["no_restrictions"] = no_restrictions
            if sign is not None:
                self._values["sign"] = sign
            if unwrap is not None:
                self._values["unwrap"] = unwrap
            if verify is not None:
                self._values["verify"] = verify
            if wrap is not None:
                self._values["wrap"] = wrap

        @builtins.property
        def decrypt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used to decrypt data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-decrypt
            '''
            result = self._values.get("decrypt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def derive_key(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used to derive new keys.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-derivekey
            '''
            result = self._values.get("derive_key")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def encrypt(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used to encrypt data.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-encrypt
            '''
            result = self._values.get("encrypt")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def generate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used to generate and verify other card and PIN verification keys.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-generate
            '''
            result = self._values.get("generate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def no_restrictions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key has no special restrictions other than the restrictions implied by ``KeyUsage`` .

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-norestrictions
            '''
            result = self._values.get("no_restrictions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def sign(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used for signing.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-sign
            '''
            result = self._values.get("sign")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def unwrap(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-unwrap
            '''
            result = self._values.get("unwrap")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def verify(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used to verify signatures.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-verify
            '''
            result = self._values.get("verify")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def wrap(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Speciﬁes whether an AWS Payment Cryptography key can be used to wrap other keys.

            :default: - false

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-paymentcryptography-key-keymodesofuse.html#cfn-paymentcryptography-key-keymodesofuse-wrap
            '''
            result = self._values.get("wrap")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeyModesOfUseProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_paymentcryptography.CfnKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "exportable": "exportable",
        "key_attributes": "keyAttributes",
        "enabled": "enabled",
        "key_check_value_algorithm": "keyCheckValueAlgorithm",
        "tags": "tags",
    },
)
class CfnKeyProps:
    def __init__(
        self,
        *,
        exportable: typing.Union[builtins.bool, _IResolvable_da3f097b],
        key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKey.KeyAttributesProperty, typing.Dict[builtins.str, typing.Any]]],
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        key_check_value_algorithm: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnKey``.

        :param exportable: Specifies whether the key is exportable. This data is immutable after the key is created.
        :param key_attributes: The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key. This data is immutable after the key is created.
        :param enabled: Specifies whether the key is enabled.
        :param key_check_value_algorithm: The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV). It is used to validate the key integrity. For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_paymentcryptography as paymentcryptography
            
            cfn_key_props = paymentcryptography.CfnKeyProps(
                exportable=False,
                key_attributes=paymentcryptography.CfnKey.KeyAttributesProperty(
                    key_algorithm="keyAlgorithm",
                    key_class="keyClass",
                    key_modes_of_use=paymentcryptography.CfnKey.KeyModesOfUseProperty(
                        decrypt=False,
                        derive_key=False,
                        encrypt=False,
                        generate=False,
                        no_restrictions=False,
                        sign=False,
                        unwrap=False,
                        verify=False,
                        wrap=False
                    ),
                    key_usage="keyUsage"
                ),
            
                # the properties below are optional
                enabled=False,
                key_check_value_algorithm="keyCheckValueAlgorithm",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ba44ca0d377189c3fde668037b0b7a8a9ee19fc052286d570ba26e888b2cf78)
            check_type(argname="argument exportable", value=exportable, expected_type=type_hints["exportable"])
            check_type(argname="argument key_attributes", value=key_attributes, expected_type=type_hints["key_attributes"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument key_check_value_algorithm", value=key_check_value_algorithm, expected_type=type_hints["key_check_value_algorithm"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "exportable": exportable,
            "key_attributes": key_attributes,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if key_check_value_algorithm is not None:
            self._values["key_check_value_algorithm"] = key_check_value_algorithm
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def exportable(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
        '''Specifies whether the key is exportable.

        This data is immutable after the key is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html#cfn-paymentcryptography-key-exportable
        '''
        result = self._values.get("exportable")
        assert result is not None, "Required property 'exportable' is missing"
        return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

    @builtins.property
    def key_attributes(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnKey.KeyAttributesProperty]:
        '''The role of the key, the algorithm it supports, and the cryptographic operations allowed with the key.

        This data is immutable after the key is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html#cfn-paymentcryptography-key-keyattributes
        '''
        result = self._values.get("key_attributes")
        assert result is not None, "Required property 'key_attributes' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnKey.KeyAttributesProperty], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the key is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html#cfn-paymentcryptography-key-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def key_check_value_algorithm(self) -> typing.Optional[builtins.str]:
        '''The algorithm that AWS Payment Cryptography uses to calculate the key check value (KCV).

        It is used to validate the key integrity.

        For TDES keys, the KCV is computed by encrypting 8 bytes, each with value of zero, with the key to be checked and retaining the 3 highest order bytes of the encrypted result. For AES keys, the KCV is computed using a CMAC algorithm where the input data is 16 bytes of zero and retaining the 3 highest order bytes of the encrypted result.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html#cfn-paymentcryptography-key-keycheckvaluealgorithm
        '''
        result = self._values.get("key_check_value_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-paymentcryptography-key.html#cfn-paymentcryptography-key-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAlias",
    "CfnAliasProps",
    "CfnKey",
    "CfnKeyProps",
]

publication.publish()

def _typecheckingstub__03e3543c569149d753dcca4f9aa62f90766372bafcd1f94b89e73d5b425564e5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    alias_name: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ff200923cccd5fdae928ff708195bbced1ef4f7d50f668b5c73f249ed90f28f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8f80ee3646838aabf7e90939e0251f8840c956ccf920965fde8a918b4cbf79b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbda40ab380bdefcb4b1f97fbdfb383ed08815fcaf1d136e881314e872f7e42b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fbafef3a7fe6a4ee77cdd86bde1df29b8df0e985f7099527ccce1ce9c0fb18d5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0461ccf0903c4c242ef15c5e4bc2830b51a5cf5ebc2b326557f67cfef92bc428(
    *,
    alias_name: builtins.str,
    key_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eae3f8af01ec3a496044e22e7d1ce2b96cf8f20736ded57ce899a918f81a9596(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    exportable: typing.Union[builtins.bool, _IResolvable_da3f097b],
    key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKey.KeyAttributesProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_check_value_algorithm: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d0701d054ede99cce0d90b76ac7d1ff4eb40159e6fd502b56930a0b0a1cb63c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67d0864ea174d57204bcc36c049839be306d7849f2c1c3dc30e1a6292d6885fd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f21c25b942e06e9156561ac93e6371242b5b4ddbcb85077df885feaa89b2b2a6(
    value: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__509385bb900abd87d7e9680c46b008a76766e5f51864d21972df261f9db73156(
    value: typing.Union[_IResolvable_da3f097b, CfnKey.KeyAttributesProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1defb803536cf97ac83055a5760a6073dfc007fbfe2b34f9a774538091a30ef3(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__197ab67a28372d3c264e1414d929d0c2287a028faf7915197718c789307d1350(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78d5368ca44b0ca5acba26b914716e9d9e8bb1acb0511f4f2a701cf6fcdd968d(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b75d16f6c2607cb760edf67dc96a26bed574dca4a5534dd5e3593befcc5f0a6(
    *,
    key_algorithm: builtins.str,
    key_class: builtins.str,
    key_modes_of_use: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKey.KeyModesOfUseProperty, typing.Dict[builtins.str, typing.Any]]],
    key_usage: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19bb5a67c0e2112fa91ea214bcd53a4406d0b3e006c09d38e9c0cd851824cb05(
    *,
    decrypt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    derive_key: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    encrypt: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    generate: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    no_restrictions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    sign: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    unwrap: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    verify: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    wrap: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ba44ca0d377189c3fde668037b0b7a8a9ee19fc052286d570ba26e888b2cf78(
    *,
    exportable: typing.Union[builtins.bool, _IResolvable_da3f097b],
    key_attributes: typing.Union[_IResolvable_da3f097b, typing.Union[CfnKey.KeyAttributesProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    key_check_value_algorithm: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
