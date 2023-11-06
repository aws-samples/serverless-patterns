'''
# Alexa Skills Kit Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.alexa_ask as alexa_ask
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ASK construct libraries](https://constructs.dev/search?q=ask)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation Alexa::ASK resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Alexa_ASK.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for Alexa::ASK](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Alexa_ASK.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnSkill(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.alexa_ask.CfnSkill",
):
    '''The ``Alexa::ASK::Skill`` resource creates an Alexa skill that enables customers to access new abilities.

    For more information about developing a skill, see the  .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import alexa_ask
        
        # manifest: Any
        
        cfn_skill = alexa_ask.CfnSkill(self, "MyCfnSkill",
            authentication_configuration=alexa_ask.CfnSkill.AuthenticationConfigurationProperty(
                client_id="clientId",
                client_secret="clientSecret",
                refresh_token="refreshToken"
            ),
            skill_package=alexa_ask.CfnSkill.SkillPackageProperty(
                s3_bucket="s3Bucket",
                s3_key="s3Key",
        
                # the properties below are optional
                overrides=alexa_ask.CfnSkill.OverridesProperty(
                    manifest=manifest
                ),
                s3_bucket_role="s3BucketRole",
                s3_object_version="s3ObjectVersion"
            ),
            vendor_id="vendorId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSkill.AuthenticationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        skill_package: typing.Union[_IResolvable_da3f097b, typing.Union["CfnSkill.SkillPackageProperty", typing.Dict[builtins.str, typing.Any]]],
        vendor_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param authentication_configuration: Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the are supported. The client ID, client secret, and refresh token are required.
        :param skill_package: Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the .
        :param vendor_id: The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in . The provided LWA credentials must be linked to the developer account associated with this vendor ID.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d78aeecda8ab7b4c5c33f0fcee213f02875f3e3b528db0fdd0278c4f3e29d0c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSkillProps(
            authentication_configuration=authentication_configuration,
            skill_package=skill_package,
            vendor_id=vendor_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d237b06ab57352cf7e8d1c4072d35efe097487a04851896ab60f8ca5d016dcf7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e003e0dd9b27e4ebcf016a5753a786b7abc1d6e5c77e28c8c2afd4d9aa0b9e00)
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
    @jsii.member(jsii_name="authenticationConfiguration")
    def authentication_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSkill.AuthenticationConfigurationProperty"]:
        '''Login with Amazon (LWA) configuration used to authenticate with the Alexa service.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSkill.AuthenticationConfigurationProperty"], jsii.get(self, "authenticationConfiguration"))

    @authentication_configuration.setter
    def authentication_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSkill.AuthenticationConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f79ad56de5a233709bfa180b3886229464b9d28a88416bdaabab40400468843)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="skillPackage")
    def skill_package(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnSkill.SkillPackageProperty"]:
        '''Configuration for the skill package that contains the components of the Alexa skill.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnSkill.SkillPackageProperty"], jsii.get(self, "skillPackage"))

    @skill_package.setter
    def skill_package(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnSkill.SkillPackageProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1160f84c06aa4769b57c3cf0e89867f1c310c0c73387afad6e0e174defac367a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skillPackage", value)

    @builtins.property
    @jsii.member(jsii_name="vendorId")
    def vendor_id(self) -> builtins.str:
        '''The vendor ID associated with the Amazon developer account that will host the skill.'''
        return typing.cast(builtins.str, jsii.get(self, "vendorId"))

    @vendor_id.setter
    def vendor_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e19323a763e3e7ce004953363ef3f20809f72e8931c75312b88fc85064e5d44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vendorId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.alexa_ask.CfnSkill.AuthenticationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "refresh_token": "refreshToken",
        },
    )
    class AuthenticationConfigurationProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            refresh_token: builtins.str,
        ) -> None:
            '''The ``AuthenticationConfiguration`` property type specifies the Login with Amazon (LWA) configuration used to authenticate with the Alexa service.

            Only Login with Amazon security profiles created through the  are supported for authentication. A client ID, client secret, and refresh token are required. You can generate a client ID and client secret by creating a new  on the Amazon Developer Portal or you can retrieve them from an existing profile. You can then retrieve the refresh token using the Alexa Skills Kit CLI. For instructions, see  in the  .

            ``AuthenticationConfiguration`` is a property of the ``Alexa::ASK::Skill`` resource.

            :param client_id: Client ID from Login with Amazon (LWA).
            :param client_secret: Client secret from Login with Amazon (LWA).
            :param refresh_token: Refresh token from Login with Amazon (LWA). This token is secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import alexa_ask
                
                authentication_configuration_property = alexa_ask.CfnSkill.AuthenticationConfigurationProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__754dd5f6039927c2e90b090339b3fb0321a11d25eeaf62d4c24a24dc6d93e784)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
                "refresh_token": refresh_token,
            }

        @builtins.property
        def client_id(self) -> builtins.str:
            '''Client ID from Login with Amazon (LWA).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''Client secret from Login with Amazon (LWA).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def refresh_token(self) -> builtins.str:
            '''Refresh token from Login with Amazon (LWA).

            This token is secret.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-authenticationconfiguration.html#cfn-ask-skill-authenticationconfiguration-refreshtoken
            '''
            result = self._values.get("refresh_token")
            assert result is not None, "Required property 'refresh_token' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthenticationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.alexa_ask.CfnSkill.OverridesProperty",
        jsii_struct_bases=[],
        name_mapping={"manifest": "manifest"},
    )
    class OverridesProperty:
        def __init__(self, *, manifest: typing.Any = None) -> None:
            '''The ``Overrides`` property type provides overrides to the skill package to apply when creating or updating the skill.

            Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.

            ``Overrides`` is a property of the ``Alexa::ASK::Skill SkillPackage`` property type.

            :param manifest: Overrides to apply to the skill manifest inside of the skill package. The skill manifest contains metadata about the skill. For more information, see .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import alexa_ask
                
                # manifest: Any
                
                overrides_property = alexa_ask.CfnSkill.OverridesProperty(
                    manifest=manifest
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fab72aad4fe72a79ab52407ef75f2025944fa0bd45192ece25e9a3bf7f9107f)
                check_type(argname="argument manifest", value=manifest, expected_type=type_hints["manifest"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if manifest is not None:
                self._values["manifest"] = manifest

        @builtins.property
        def manifest(self) -> typing.Any:
            '''Overrides to apply to the skill manifest inside of the skill package.

            The skill manifest contains metadata about the skill. For more information, see  .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-overrides.html#cfn-ask-skill-overrides-manifest
            '''
            result = self._values.get("manifest")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.alexa_ask.CfnSkill.SkillPackageProperty",
        jsii_struct_bases=[],
        name_mapping={
            "s3_bucket": "s3Bucket",
            "s3_key": "s3Key",
            "overrides": "overrides",
            "s3_bucket_role": "s3BucketRole",
            "s3_object_version": "s3ObjectVersion",
        },
    )
    class SkillPackageProperty:
        def __init__(
            self,
            *,
            s3_bucket: builtins.str,
            s3_key: builtins.str,
            overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSkill.OverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_bucket_role: typing.Optional[builtins.str] = None,
            s3_object_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``SkillPackage`` property type contains configuration details for the skill package that contains the components of the Alexa skill.

            Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. More details about the skill package format are located in the  .

            ``SkillPackage`` is a property of the ``Alexa::ASK::Skill`` resource.

            :param s3_bucket: The name of the Amazon S3 bucket where the .zip file that contains the skill package is stored.
            :param s3_key: The location and name of the skill package .zip file.
            :param overrides: Overrides to the skill package to apply when creating or updating the skill. Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.
            :param s3_bucket_role: ARN of the IAM role that grants the Alexa service ( ``alexa-appkit.amazon.com`` ) permission to access the bucket and retrieve the skill package. This property is optional. If you do not provide it, the bucket must be publicly accessible or configured with a policy that allows this access. Otherwise, AWS CloudFormation cannot create the skill.
            :param s3_object_version: If you have S3 versioning enabled, the version ID of the skill package.zip file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import alexa_ask
                
                # manifest: Any
                
                skill_package_property = alexa_ask.CfnSkill.SkillPackageProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
                
                    # the properties below are optional
                    overrides=alexa_ask.CfnSkill.OverridesProperty(
                        manifest=manifest
                    ),
                    s3_bucket_role="s3BucketRole",
                    s3_object_version="s3ObjectVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bd0d7fb4b090c6708f33e9e5a779b9bd5c8080853d2ec8486346a494e853b60)
                check_type(argname="argument s3_bucket", value=s3_bucket, expected_type=type_hints["s3_bucket"])
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
                check_type(argname="argument overrides", value=overrides, expected_type=type_hints["overrides"])
                check_type(argname="argument s3_bucket_role", value=s3_bucket_role, expected_type=type_hints["s3_bucket_role"])
                check_type(argname="argument s3_object_version", value=s3_object_version, expected_type=type_hints["s3_object_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_bucket": s3_bucket,
                "s3_key": s3_key,
            }
            if overrides is not None:
                self._values["overrides"] = overrides
            if s3_bucket_role is not None:
                self._values["s3_bucket_role"] = s3_bucket_role
            if s3_object_version is not None:
                self._values["s3_object_version"] = s3_object_version

        @builtins.property
        def s3_bucket(self) -> builtins.str:
            '''The name of the Amazon S3 bucket where the .zip file that contains the skill package is stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucket
            '''
            result = self._values.get("s3_bucket")
            assert result is not None, "Required property 's3_bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_key(self) -> builtins.str:
            '''The location and name of the skill package .zip file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSkill.OverridesProperty"]]:
            '''Overrides to the skill package to apply when creating or updating the skill.

            Values provided here do not modify the contents of the original skill package. Currently, only overriding values inside of the skill manifest component of the package is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-overrides
            '''
            result = self._values.get("overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSkill.OverridesProperty"]], result)

        @builtins.property
        def s3_bucket_role(self) -> typing.Optional[builtins.str]:
            '''ARN of the IAM role that grants the Alexa service ( ``alexa-appkit.amazon.com`` ) permission to access the bucket and retrieve the skill package. This property is optional. If you do not provide it, the bucket must be publicly accessible or configured with a policy that allows this access. Otherwise, AWS CloudFormation cannot create the skill.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3bucketrole
            '''
            result = self._values.get("s3_bucket_role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_object_version(self) -> typing.Optional[builtins.str]:
            '''If you have S3 versioning enabled, the version ID of the skill package.zip file.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ask-skill-skillpackage.html#cfn-ask-skill-skillpackage-s3objectversion
            '''
            result = self._values.get("s3_object_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SkillPackageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.alexa_ask.CfnSkillProps",
    jsii_struct_bases=[],
    name_mapping={
        "authentication_configuration": "authenticationConfiguration",
        "skill_package": "skillPackage",
        "vendor_id": "vendorId",
    },
)
class CfnSkillProps:
    def __init__(
        self,
        *,
        authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        skill_package: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.SkillPackageProperty, typing.Dict[builtins.str, typing.Any]]],
        vendor_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnSkill``.

        :param authentication_configuration: Login with Amazon (LWA) configuration used to authenticate with the Alexa service. Only Login with Amazon clients created through the are supported. The client ID, client secret, and refresh token are required.
        :param skill_package: Configuration for the skill package that contains the components of the Alexa skill. Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the .
        :param vendor_id: The vendor ID associated with the Amazon developer account that will host the skill. Details for retrieving the vendor ID are in . The provided LWA credentials must be linked to the developer account associated with this vendor ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import alexa_ask
            
            # manifest: Any
            
            cfn_skill_props = alexa_ask.CfnSkillProps(
                authentication_configuration=alexa_ask.CfnSkill.AuthenticationConfigurationProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                    refresh_token="refreshToken"
                ),
                skill_package=alexa_ask.CfnSkill.SkillPackageProperty(
                    s3_bucket="s3Bucket",
                    s3_key="s3Key",
            
                    # the properties below are optional
                    overrides=alexa_ask.CfnSkill.OverridesProperty(
                        manifest=manifest
                    ),
                    s3_bucket_role="s3BucketRole",
                    s3_object_version="s3ObjectVersion"
                ),
                vendor_id="vendorId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18a03c0ba6c20d17a037e17f3d48ad3d5175e42d1b4d42294067c2c25cdf6e08)
            check_type(argname="argument authentication_configuration", value=authentication_configuration, expected_type=type_hints["authentication_configuration"])
            check_type(argname="argument skill_package", value=skill_package, expected_type=type_hints["skill_package"])
            check_type(argname="argument vendor_id", value=vendor_id, expected_type=type_hints["vendor_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "authentication_configuration": authentication_configuration,
            "skill_package": skill_package,
            "vendor_id": vendor_id,
        }

    @builtins.property
    def authentication_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSkill.AuthenticationConfigurationProperty]:
        '''Login with Amazon (LWA) configuration used to authenticate with the Alexa service.

        Only Login with Amazon clients created through the  are supported. The client ID, client secret, and refresh token are required.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-authenticationconfiguration
        '''
        result = self._values.get("authentication_configuration")
        assert result is not None, "Required property 'authentication_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSkill.AuthenticationConfigurationProperty], result)

    @builtins.property
    def skill_package(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnSkill.SkillPackageProperty]:
        '''Configuration for the skill package that contains the components of the Alexa skill.

        Skill packages are retrieved from an Amazon S3 bucket and key and used to create and update the skill. For more information about the skill package format, see the  .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-skillpackage
        '''
        result = self._values.get("skill_package")
        assert result is not None, "Required property 'skill_package' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnSkill.SkillPackageProperty], result)

    @builtins.property
    def vendor_id(self) -> builtins.str:
        '''The vendor ID associated with the Amazon developer account that will host the skill.

        Details for retrieving the vendor ID are in  . The provided LWA credentials must be linked to the developer account associated with this vendor ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ask-skill.html#cfn-ask-skill-vendorid
        '''
        result = self._values.get("vendor_id")
        assert result is not None, "Required property 'vendor_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSkillProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnSkill",
    "CfnSkillProps",
]

publication.publish()

def _typecheckingstub__0d78aeecda8ab7b4c5c33f0fcee213f02875f3e3b528db0fdd0278c4f3e29d0c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    skill_package: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.SkillPackageProperty, typing.Dict[builtins.str, typing.Any]]],
    vendor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d237b06ab57352cf7e8d1c4072d35efe097487a04851896ab60f8ca5d016dcf7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e003e0dd9b27e4ebcf016a5753a786b7abc1d6e5c77e28c8c2afd4d9aa0b9e00(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f79ad56de5a233709bfa180b3886229464b9d28a88416bdaabab40400468843(
    value: typing.Union[_IResolvable_da3f097b, CfnSkill.AuthenticationConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1160f84c06aa4769b57c3cf0e89867f1c310c0c73387afad6e0e174defac367a(
    value: typing.Union[_IResolvable_da3f097b, CfnSkill.SkillPackageProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e19323a763e3e7ce004953363ef3f20809f72e8931c75312b88fc85064e5d44(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__754dd5f6039927c2e90b090339b3fb0321a11d25eeaf62d4c24a24dc6d93e784(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    refresh_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fab72aad4fe72a79ab52407ef75f2025944fa0bd45192ece25e9a3bf7f9107f(
    *,
    manifest: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bd0d7fb4b090c6708f33e9e5a779b9bd5c8080853d2ec8486346a494e853b60(
    *,
    s3_bucket: builtins.str,
    s3_key: builtins.str,
    overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.OverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_bucket_role: typing.Optional[builtins.str] = None,
    s3_object_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18a03c0ba6c20d17a037e17f3d48ad3d5175e42d1b4d42294067c2c25cdf6e08(
    *,
    authentication_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.AuthenticationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    skill_package: typing.Union[_IResolvable_da3f097b, typing.Union[CfnSkill.SkillPackageProperty, typing.Dict[builtins.str, typing.Any]]],
    vendor_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
