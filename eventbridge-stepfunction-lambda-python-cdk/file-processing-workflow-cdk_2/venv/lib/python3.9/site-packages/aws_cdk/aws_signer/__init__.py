'''
# AWS::Signer Construct Library

AWS Signer is a fully managed code-signing service to ensure the trust and integrity of your code. Organizations validate code against
a digital signature to confirm that the code is unaltered and from a trusted publisher. For more information, see [What Is AWS
Signer?](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html)

## Table of Contents

* [Signing Platform](#signing-platform)
* [Signing Profile](#signing-profile)

## Signing Platform

A signing platform is a predefined set of instructions that specifies the signature format and signing algorithms that AWS Signer should use
to sign a zip file. For more information go to [Signing Platforms in AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/gs-platform.html).

AWS Signer provides a pre-defined set of signing platforms. They are available in the CDK as -

```text
Platform.AWS_IOT_DEVICE_MANAGEMENT_SHA256_ECDSA
Platform.AWS_LAMBDA_SHA384_ECDSA
Platform.AMAZON_FREE_RTOS_TI_CC3220SF
Platform.AMAZON_FREE_RTOS_DEFAULT
```

## Signing Profile

A signing profile is a code-signing template that can be used to pre-define the signature specifications for a signing job.
A signing profile includes a signing platform to designate the file type to be signed, the signature format, and the signature algorithms.
For more information, visit [Signing Profiles in AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/gs-profile.html).

The following code sets up a signing profile for signing lambda code bundles -

```python
signing_profile = signer.SigningProfile(self, "SigningProfile",
    platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
)
```

A signing profile is valid by default for 135 months. This can be modified by specifying the `signatureValidityPeriod` property.
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
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnProfilePermission(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_signer.CfnProfilePermission",
):
    '''Adds cross-account permissions to a signing profile.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_signer as signer
        
        cfn_profile_permission = signer.CfnProfilePermission(self, "MyCfnProfilePermission",
            action="action",
            principal="principal",
            profile_name="profileName",
            statement_id="statementId",
        
            # the properties below are optional
            profile_version="profileVersion"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        action: builtins.str,
        principal: builtins.str,
        profile_name: builtins.str,
        statement_id: builtins.str,
        profile_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action: The AWS Signer action permitted as part of cross-account permissions.
        :param principal: The AWS principal receiving cross-account permissions. This may be an IAM role or another AWS account ID.
        :param profile_name: The human-readable name of the signing profile.
        :param statement_id: A unique identifier for the cross-account permission statement.
        :param profile_version: The version of the signing profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b7dd51e7eac664b5afe9a1b7d1972f7da8883244b3f554de5c8d1e0cc84f053)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfilePermissionProps(
            action=action,
            principal=principal,
            profile_name=profile_name,
            statement_id=statement_id,
            profile_version=profile_version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c27c534af2f676e9fe9c9b1c8462b7339b8b65f0c4b9b08f485033feefe4741)
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
            type_hints = typing.get_type_hints(_typecheckingstub__662ce8c205095e7c693616c7c2d43b18432d9c948d131c1a3e91e7b5aafc2323)
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
    @jsii.member(jsii_name="action")
    def action(self) -> builtins.str:
        '''The AWS Signer action permitted as part of cross-account permissions.'''
        return typing.cast(builtins.str, jsii.get(self, "action"))

    @action.setter
    def action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b8c32d87b73fa4fb5094ae3e46175df93629f45d64c0d2b3130d5471eca086e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "action", value)

    @builtins.property
    @jsii.member(jsii_name="principal")
    def principal(self) -> builtins.str:
        '''The AWS principal receiving cross-account permissions.'''
        return typing.cast(builtins.str, jsii.get(self, "principal"))

    @principal.setter
    def principal(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37b3db8c74061df8a65eeda431f6a41091db1cf687f78d71f79a9441f95b0644)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principal", value)

    @builtins.property
    @jsii.member(jsii_name="profileName")
    def profile_name(self) -> builtins.str:
        '''The human-readable name of the signing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "profileName"))

    @profile_name.setter
    def profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0284177166884a4428819ca021ca73daecd877943a7bf90e79aec6e00f5ad07a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileName", value)

    @builtins.property
    @jsii.member(jsii_name="statementId")
    def statement_id(self) -> builtins.str:
        '''A unique identifier for the cross-account permission statement.'''
        return typing.cast(builtins.str, jsii.get(self, "statementId"))

    @statement_id.setter
    def statement_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e8ca5148f26e102d75c04bb95550132d3a29824e2932a98f9f87725df3962fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementId", value)

    @builtins.property
    @jsii.member(jsii_name="profileVersion")
    def profile_version(self) -> typing.Optional[builtins.str]:
        '''The version of the signing profile.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "profileVersion"))

    @profile_version.setter
    def profile_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80bd95afa9c654fc5d026db2cad497a96dc240f466154896c0c5c3cc15b54bdd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "profileVersion", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_signer.CfnProfilePermissionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action": "action",
        "principal": "principal",
        "profile_name": "profileName",
        "statement_id": "statementId",
        "profile_version": "profileVersion",
    },
)
class CfnProfilePermissionProps:
    def __init__(
        self,
        *,
        action: builtins.str,
        principal: builtins.str,
        profile_name: builtins.str,
        statement_id: builtins.str,
        profile_version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfilePermission``.

        :param action: The AWS Signer action permitted as part of cross-account permissions.
        :param principal: The AWS principal receiving cross-account permissions. This may be an IAM role or another AWS account ID.
        :param profile_name: The human-readable name of the signing profile.
        :param statement_id: A unique identifier for the cross-account permission statement.
        :param profile_version: The version of the signing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_signer as signer
            
            cfn_profile_permission_props = signer.CfnProfilePermissionProps(
                action="action",
                principal="principal",
                profile_name="profileName",
                statement_id="statementId",
            
                # the properties below are optional
                profile_version="profileVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc7158edcf57ecc13c1e912574c38dd0ad2f9585f23f02536376f63ed728fe86)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
            check_type(argname="argument profile_name", value=profile_name, expected_type=type_hints["profile_name"])
            check_type(argname="argument statement_id", value=statement_id, expected_type=type_hints["statement_id"])
            check_type(argname="argument profile_version", value=profile_version, expected_type=type_hints["profile_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action": action,
            "principal": principal,
            "profile_name": profile_name,
            "statement_id": statement_id,
        }
        if profile_version is not None:
            self._values["profile_version"] = profile_version

    @builtins.property
    def action(self) -> builtins.str:
        '''The AWS Signer action permitted as part of cross-account permissions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-action
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def principal(self) -> builtins.str:
        '''The AWS principal receiving cross-account permissions.

        This may be an IAM role or another AWS account ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-principal
        '''
        result = self._values.get("principal")
        assert result is not None, "Required property 'principal' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_name(self) -> builtins.str:
        '''The human-readable name of the signing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profilename
        '''
        result = self._values.get("profile_name")
        assert result is not None, "Required property 'profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def statement_id(self) -> builtins.str:
        '''A unique identifier for the cross-account permission statement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-statementid
        '''
        result = self._values.get("statement_id")
        assert result is not None, "Required property 'statement_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def profile_version(self) -> typing.Optional[builtins.str]:
        '''The version of the signing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-profilepermission.html#cfn-signer-profilepermission-profileversion
        '''
        result = self._values.get("profile_version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProfilePermissionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSigningProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_signer.CfnSigningProfile",
):
    '''Creates a signing profile.

    A signing profile is a code-signing template that can be used to carry out a pre-defined signing job.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_signer as signer
        
        cfn_signing_profile = signer.CfnSigningProfile(self, "MyCfnSigningProfile",
            platform_id="platformId",
        
            # the properties below are optional
            signature_validity_period=signer.CfnSigningProfile.SignatureValidityPeriodProperty(
                type="type",
                value=123
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
        platform_id: builtins.str,
        signature_validity_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSigningProfile.SignatureValidityPeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param platform_id: The ID of a platform that is available for use by a signing profile.
        :param signature_validity_period: The validity period override for any signature generated using this signing profile. If unspecified, the default is 135 months.
        :param tags: A list of tags associated with the signing profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d84fe196f81722ce814c09f8bd21719acd97c32e92c1de922d0f04c31912d65b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSigningProfileProps(
            platform_id=platform_id,
            signature_validity_period=signature_validity_period,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__796b31e3d9d2ce1d3b20283186f1c0c54ce0f3bb426633c056466f92264e35b9)
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
            type_hints = typing.get_type_hints(_typecheckingstub__59eb44451cc01c28f44f21713cf6296a564f672edd6fd097e34d4dadad14cdf5)
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
        '''The Amazon Resource Name (ARN) of the signing profile created.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileName")
    def attr_profile_name(self) -> builtins.str:
        '''The name of the signing profile created.

        :cloudformationAttribute: ProfileName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileName"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileVersion")
    def attr_profile_version(self) -> builtins.str:
        '''The version of the signing profile created.

        :cloudformationAttribute: ProfileVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileVersion"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileVersionArn")
    def attr_profile_version_arn(self) -> builtins.str:
        '''The signing profile ARN, including the profile version.

        :cloudformationAttribute: ProfileVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileVersionArn"))

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
    @jsii.member(jsii_name="platformId")
    def platform_id(self) -> builtins.str:
        '''The ID of a platform that is available for use by a signing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "platformId"))

    @platform_id.setter
    def platform_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe4af9baf88789da4f861a18d37152a49a2947c30e555d2e1fff8d9d3f3d5f1a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "platformId", value)

    @builtins.property
    @jsii.member(jsii_name="signatureValidityPeriod")
    def signature_validity_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSigningProfile.SignatureValidityPeriodProperty"]]:
        '''The validity period override for any signature generated using this signing profile.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSigningProfile.SignatureValidityPeriodProperty"]], jsii.get(self, "signatureValidityPeriod"))

    @signature_validity_period.setter
    def signature_validity_period(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSigningProfile.SignatureValidityPeriodProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3142352951a0c8c38151f31fb1da21f644b00a82a7383e211cfa3feb49aaea8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "signatureValidityPeriod", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags associated with the signing profile.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__580ec6652b4c39cad7404de2ec2116ee0ba26fab741371a13d0201ad7c60ad0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_signer.CfnSigningProfile.SignatureValidityPeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class SignatureValidityPeriodProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            value: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The validity period for the signing job.

            :param type: The time unit for signature validity: DAYS | MONTHS | YEARS.
            :param value: The numerical value of the time unit for signature validity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_signer as signer
                
                signature_validity_period_property = signer.CfnSigningProfile.SignatureValidityPeriodProperty(
                    type="type",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3efe44bef5492c74fa08cef22b7e2a158db85808147bf0c6792e238cfdcc5fa4)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''The time unit for signature validity: DAYS | MONTHS | YEARS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html#cfn-signer-signingprofile-signaturevalidityperiod-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[jsii.Number]:
            '''The numerical value of the time unit for signature validity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-signer-signingprofile-signaturevalidityperiod.html#cfn-signer-signingprofile-signaturevalidityperiod-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SignatureValidityPeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_signer.CfnSigningProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "platform_id": "platformId",
        "signature_validity_period": "signatureValidityPeriod",
        "tags": "tags",
    },
)
class CfnSigningProfileProps:
    def __init__(
        self,
        *,
        platform_id: builtins.str,
        signature_validity_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSigningProfile.SignatureValidityPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSigningProfile``.

        :param platform_id: The ID of a platform that is available for use by a signing profile.
        :param signature_validity_period: The validity period override for any signature generated using this signing profile. If unspecified, the default is 135 months.
        :param tags: A list of tags associated with the signing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_signer as signer
            
            cfn_signing_profile_props = signer.CfnSigningProfileProps(
                platform_id="platformId",
            
                # the properties below are optional
                signature_validity_period=signer.CfnSigningProfile.SignatureValidityPeriodProperty(
                    type="type",
                    value=123
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e40d7ccf57c93b4e1db5a4e6b98b562bce8ff86b219931d0d4cfb16a346cb0e)
            check_type(argname="argument platform_id", value=platform_id, expected_type=type_hints["platform_id"])
            check_type(argname="argument signature_validity_period", value=signature_validity_period, expected_type=type_hints["signature_validity_period"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "platform_id": platform_id,
        }
        if signature_validity_period is not None:
            self._values["signature_validity_period"] = signature_validity_period
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def platform_id(self) -> builtins.str:
        '''The ID of a platform that is available for use by a signing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-platformid
        '''
        result = self._values.get("platform_id")
        assert result is not None, "Required property 'platform_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signature_validity_period(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSigningProfile.SignatureValidityPeriodProperty]]:
        '''The validity period override for any signature generated using this signing profile.

        If unspecified, the default is 135 months.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-signaturevalidityperiod
        '''
        result = self._values.get("signature_validity_period")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSigningProfile.SignatureValidityPeriodProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags associated with the signing profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSigningProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_signer.ISigningProfile")
class ISigningProfile(_IResource_c80c4260, typing_extensions.Protocol):
    '''A Signer Profile.'''

    @builtins.property
    @jsii.member(jsii_name="signingProfileArn")
    def signing_profile_arn(self) -> builtins.str:
        '''The ARN of the signing profile.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="signingProfileName")
    def signing_profile_name(self) -> builtins.str:
        '''The name of signing profile.

        :attribute: ProfileName
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersion")
    def signing_profile_version(self) -> builtins.str:
        '''The version of signing profile.

        :attribute: ProfileVersion
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> builtins.str:
        '''The ARN of signing profile version.

        :attribute: ProfileVersionArn
        '''
        ...


class _ISigningProfileProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A Signer Profile.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_signer.ISigningProfile"

    @builtins.property
    @jsii.member(jsii_name="signingProfileArn")
    def signing_profile_arn(self) -> builtins.str:
        '''The ARN of the signing profile.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileName")
    def signing_profile_name(self) -> builtins.str:
        '''The name of signing profile.

        :attribute: ProfileName
        '''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileName"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersion")
    def signing_profile_version(self) -> builtins.str:
        '''The version of signing profile.

        :attribute: ProfileVersion
        '''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileVersion"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> builtins.str:
        '''The ARN of signing profile version.

        :attribute: ProfileVersionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileVersionArn"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ISigningProfile).__jsii_proxy_class__ = lambda : _ISigningProfileProxy


class Platform(metaclass=jsii.JSIIMeta, jsii_type="aws-cdk-lib.aws_signer.Platform"):
    '''Platforms that are allowed with signing config.

    :see: https://docs.aws.amazon.com/signer/latest/developerguide/gs-platform.html
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_signer as signer
        
        
        signing_profile = signer.SigningProfile(self, "SigningProfile",
            platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
        )
        
        code_signing_config = lambda_.CodeSigningConfig(self, "CodeSigningConfig",
            signing_profiles=[signing_profile]
        )
        
        lambda_.Function(self, "Function",
            code_signing_config=code_signing_config,
            runtime=lambda_.Runtime.NODEJS_18_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
        )
    '''

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FREE_RTOS_DEFAULT")
    def AMAZON_FREE_RTOS_DEFAULT(cls) -> "Platform":
        '''Specification of signature format and signing algorithms with SHA256 hash and ECDSA encryption for Amazon FreeRTOS.'''
        return typing.cast("Platform", jsii.sget(cls, "AMAZON_FREE_RTOS_DEFAULT"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AMAZON_FREE_RTOS_TI_CC3220SF")
    def AMAZON_FREE_RTOS_TI_CC3220_SF(cls) -> "Platform":
        '''Specification of signature format and signing algorithms with SHA1 hash and RSA encryption for Amazon FreeRTOS.'''
        return typing.cast("Platform", jsii.sget(cls, "AMAZON_FREE_RTOS_TI_CC3220SF"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_IOT_DEVICE_MANAGEMENT_SHA256_ECDSA")
    def AWS_IOT_DEVICE_MANAGEMENT_SHA256_ECDSA(cls) -> "Platform":
        '''Specification of signature format and signing algorithms for AWS IoT Device.'''
        return typing.cast("Platform", jsii.sget(cls, "AWS_IOT_DEVICE_MANAGEMENT_SHA256_ECDSA"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="AWS_LAMBDA_SHA384_ECDSA")
    def AWS_LAMBDA_SHA384_ECDSA(cls) -> "Platform":
        '''Specification of signature format and signing algorithms for AWS Lambda.'''
        return typing.cast("Platform", jsii.sget(cls, "AWS_LAMBDA_SHA384_ECDSA"))

    @builtins.property
    @jsii.member(jsii_name="platformId")
    def platform_id(self) -> builtins.str:
        '''The id of signing platform.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-signer-signingprofile.html#cfn-signer-signingprofile-platformid
        '''
        return typing.cast(builtins.str, jsii.get(self, "platformId"))


@jsii.implements(ISigningProfile)
class SigningProfile(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_signer.SigningProfile",
):
    '''Defines a Signing Profile.

    :resource: AWS::Signer::SigningProfile
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_signer as signer
        
        
        signing_profile = signer.SigningProfile(self, "SigningProfile",
            platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
        )
        
        code_signing_config = lambda_.CodeSigningConfig(self, "CodeSigningConfig",
            signing_profiles=[signing_profile]
        )
        
        lambda_.Function(self, "Function",
            code_signing_config=code_signing_config,
            runtime=lambda_.Runtime.NODEJS_18_X,
            handler="index.handler",
            code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        platform: Platform,
        signature_validity: typing.Optional[_Duration_4839e8c3] = None,
        signing_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param platform: The Signing Platform available for signing profile.
        :param signature_validity: The validity period for signatures generated using this signing profile. Default: - 135 months
        :param signing_profile_name: Physical name of this Signing Profile. Default: - Assigned by CloudFormation (recommended).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98d9bc1982105f0416e608780fc4048b7d0a29f62734adc8b7c72c6ddb875169)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SigningProfileProps(
            platform=platform,
            signature_validity=signature_validity,
            signing_profile_name=signing_profile_name,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromSigningProfileAttributes")
    @builtins.classmethod
    def from_signing_profile_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        signing_profile_name: builtins.str,
        signing_profile_version: builtins.str,
    ) -> ISigningProfile:
        '''Creates a Signing Profile construct that represents an external Signing Profile.

        :param scope: The parent creating construct (usually ``this``).
        :param id: The construct's name.
        :param signing_profile_name: The name of signing profile.
        :param signing_profile_version: The version of signing profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc8f241831391377f031dff9aa28ccba43b2e0c1261214e4326b1d0b861b1e9e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = SigningProfileAttributes(
            signing_profile_name=signing_profile_name,
            signing_profile_version=signing_profile_version,
        )

        return typing.cast(ISigningProfile, jsii.sinvoke(cls, "fromSigningProfileAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="signingProfileArn")
    def signing_profile_arn(self) -> builtins.str:
        '''The ARN of the signing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileName")
    def signing_profile_name(self) -> builtins.str:
        '''The name of signing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileName"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersion")
    def signing_profile_version(self) -> builtins.str:
        '''The version of signing profile.'''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileVersion"))

    @builtins.property
    @jsii.member(jsii_name="signingProfileVersionArn")
    def signing_profile_version_arn(self) -> builtins.str:
        '''The ARN of signing profile version.'''
        return typing.cast(builtins.str, jsii.get(self, "signingProfileVersionArn"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_signer.SigningProfileAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "signing_profile_name": "signingProfileName",
        "signing_profile_version": "signingProfileVersion",
    },
)
class SigningProfileAttributes:
    def __init__(
        self,
        *,
        signing_profile_name: builtins.str,
        signing_profile_version: builtins.str,
    ) -> None:
        '''A reference to a Signing Profile.

        :param signing_profile_name: The name of signing profile.
        :param signing_profile_version: The version of signing profile.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_signer as signer
            
            signing_profile_attributes = signer.SigningProfileAttributes(
                signing_profile_name="signingProfileName",
                signing_profile_version="signingProfileVersion"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__322df56afb65c36b455aea6e5bb84898157da190e69f2f74001dcb0db998fcca)
            check_type(argname="argument signing_profile_name", value=signing_profile_name, expected_type=type_hints["signing_profile_name"])
            check_type(argname="argument signing_profile_version", value=signing_profile_version, expected_type=type_hints["signing_profile_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "signing_profile_name": signing_profile_name,
            "signing_profile_version": signing_profile_version,
        }

    @builtins.property
    def signing_profile_name(self) -> builtins.str:
        '''The name of signing profile.'''
        result = self._values.get("signing_profile_name")
        assert result is not None, "Required property 'signing_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def signing_profile_version(self) -> builtins.str:
        '''The version of signing profile.'''
        result = self._values.get("signing_profile_version")
        assert result is not None, "Required property 'signing_profile_version' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SigningProfileAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_signer.SigningProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "platform": "platform",
        "signature_validity": "signatureValidity",
        "signing_profile_name": "signingProfileName",
    },
)
class SigningProfileProps:
    def __init__(
        self,
        *,
        platform: Platform,
        signature_validity: typing.Optional[_Duration_4839e8c3] = None,
        signing_profile_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a Signing Profile object.

        :param platform: The Signing Platform available for signing profile.
        :param signature_validity: The validity period for signatures generated using this signing profile. Default: - 135 months
        :param signing_profile_name: Physical name of this Signing Profile. Default: - Assigned by CloudFormation (recommended).

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_signer as signer
            
            
            signing_profile = signer.SigningProfile(self, "SigningProfile",
                platform=signer.Platform.AWS_LAMBDA_SHA384_ECDSA
            )
            
            code_signing_config = lambda_.CodeSigningConfig(self, "CodeSigningConfig",
                signing_profiles=[signing_profile]
            )
            
            lambda_.Function(self, "Function",
                code_signing_config=code_signing_config,
                runtime=lambda_.Runtime.NODEJS_18_X,
                handler="index.handler",
                code=lambda_.Code.from_asset(path.join(__dirname, "lambda-handler"))
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec491d4441d5ea10770b4741a09e04ab0b29fa9f7cfddbbaa4ee950829f0085f)
            check_type(argname="argument platform", value=platform, expected_type=type_hints["platform"])
            check_type(argname="argument signature_validity", value=signature_validity, expected_type=type_hints["signature_validity"])
            check_type(argname="argument signing_profile_name", value=signing_profile_name, expected_type=type_hints["signing_profile_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "platform": platform,
        }
        if signature_validity is not None:
            self._values["signature_validity"] = signature_validity
        if signing_profile_name is not None:
            self._values["signing_profile_name"] = signing_profile_name

    @builtins.property
    def platform(self) -> Platform:
        '''The Signing Platform available for signing profile.

        :see: https://docs.aws.amazon.com/signer/latest/developerguide/gs-platform.html
        '''
        result = self._values.get("platform")
        assert result is not None, "Required property 'platform' is missing"
        return typing.cast(Platform, result)

    @builtins.property
    def signature_validity(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The validity period for signatures generated using this signing profile.

        :default: - 135 months
        '''
        result = self._values.get("signature_validity")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def signing_profile_name(self) -> typing.Optional[builtins.str]:
        '''Physical name of this Signing Profile.

        :default: - Assigned by CloudFormation (recommended).
        '''
        result = self._values.get("signing_profile_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SigningProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnProfilePermission",
    "CfnProfilePermissionProps",
    "CfnSigningProfile",
    "CfnSigningProfileProps",
    "ISigningProfile",
    "Platform",
    "SigningProfile",
    "SigningProfileAttributes",
    "SigningProfileProps",
]

publication.publish()

def _typecheckingstub__7b7dd51e7eac664b5afe9a1b7d1972f7da8883244b3f554de5c8d1e0cc84f053(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action: builtins.str,
    principal: builtins.str,
    profile_name: builtins.str,
    statement_id: builtins.str,
    profile_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c27c534af2f676e9fe9c9b1c8462b7339b8b65f0c4b9b08f485033feefe4741(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__662ce8c205095e7c693616c7c2d43b18432d9c948d131c1a3e91e7b5aafc2323(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b8c32d87b73fa4fb5094ae3e46175df93629f45d64c0d2b3130d5471eca086e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37b3db8c74061df8a65eeda431f6a41091db1cf687f78d71f79a9441f95b0644(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0284177166884a4428819ca021ca73daecd877943a7bf90e79aec6e00f5ad07a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e8ca5148f26e102d75c04bb95550132d3a29824e2932a98f9f87725df3962fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bd95afa9c654fc5d026db2cad497a96dc240f466154896c0c5c3cc15b54bdd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc7158edcf57ecc13c1e912574c38dd0ad2f9585f23f02536376f63ed728fe86(
    *,
    action: builtins.str,
    principal: builtins.str,
    profile_name: builtins.str,
    statement_id: builtins.str,
    profile_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d84fe196f81722ce814c09f8bd21719acd97c32e92c1de922d0f04c31912d65b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    platform_id: builtins.str,
    signature_validity_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSigningProfile.SignatureValidityPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__796b31e3d9d2ce1d3b20283186f1c0c54ce0f3bb426633c056466f92264e35b9(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59eb44451cc01c28f44f21713cf6296a564f672edd6fd097e34d4dadad14cdf5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe4af9baf88789da4f861a18d37152a49a2947c30e555d2e1fff8d9d3f3d5f1a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3142352951a0c8c38151f31fb1da21f644b00a82a7383e211cfa3feb49aaea8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSigningProfile.SignatureValidityPeriodProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__580ec6652b4c39cad7404de2ec2116ee0ba26fab741371a13d0201ad7c60ad0c(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3efe44bef5492c74fa08cef22b7e2a158db85808147bf0c6792e238cfdcc5fa4(
    *,
    type: typing.Optional[builtins.str] = None,
    value: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e40d7ccf57c93b4e1db5a4e6b98b562bce8ff86b219931d0d4cfb16a346cb0e(
    *,
    platform_id: builtins.str,
    signature_validity_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSigningProfile.SignatureValidityPeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98d9bc1982105f0416e608780fc4048b7d0a29f62734adc8b7c72c6ddb875169(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    platform: Platform,
    signature_validity: typing.Optional[_Duration_4839e8c3] = None,
    signing_profile_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc8f241831391377f031dff9aa28ccba43b2e0c1261214e4326b1d0b861b1e9e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    signing_profile_name: builtins.str,
    signing_profile_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322df56afb65c36b455aea6e5bb84898157da190e69f2f74001dcb0db998fcca(
    *,
    signing_profile_name: builtins.str,
    signing_profile_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec491d4441d5ea10770b4741a09e04ab0b29fa9f7cfddbbaa4ee950829f0085f(
    *,
    platform: Platform,
    signature_validity: typing.Optional[_Duration_4839e8c3] = None,
    signing_profile_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
