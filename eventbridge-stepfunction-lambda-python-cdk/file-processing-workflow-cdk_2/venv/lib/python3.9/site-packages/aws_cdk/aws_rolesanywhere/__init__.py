'''
# AWS::RolesAnywhere Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_rolesanywhere as rolesanywhere
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RolesAnywhere construct libraries](https://constructs.dev/search?q=rolesanywhere)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RolesAnywhere resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RolesAnywhere.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RolesAnywhere](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RolesAnywhere.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCRL(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnCRL",
):
    '''Imports the certificate revocation list (CRL).

    A CRL is a list of certificates that have been revoked by the issuing certificate Authority (CA). IAM Roles Anywhere validates against the CRL before issuing credentials.

    *Required permissions:* ``rolesanywhere:ImportCrl`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rolesanywhere as rolesanywhere
        
        cfn_cRL = rolesanywhere.CfnCRL(self, "MyCfnCRL",
            crl_data="crlData",
            name="name",
        
            # the properties below are optional
            enabled=False,
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trust_anchor_arn="trustAnchorArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        crl_data: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trust_anchor_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param crl_data: The x509 v3 specified certificate revocation list (CRL).
        :param name: The name of the certificate revocation list (CRL).
        :param enabled: Specifies whether the certificate revocation list (CRL) is enabled.
        :param tags: A list of tags to attach to the certificate revocation list (CRL).
        :param trust_anchor_arn: The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f35b45debe8136e3de3e7d231f09e2d880d31e3c89eb1adb6a8c5613dbf5fb7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCRLProps(
            crl_data=crl_data,
            name=name,
            enabled=enabled,
            tags=tags,
            trust_anchor_arn=trust_anchor_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8dd9193cb33ddf82dba5396e1ae096cc9b451b4296ca2900997bdae6a30a6f44)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4d10b773e20eed62703f59de20a71328b2e79ce6922709bd59397acc4f352a08)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCrlId")
    def attr_crl_id(self) -> builtins.str:
        '''The unique primary identifier of the Crl.

        :cloudformationAttribute: CrlId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCrlId"))

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
    @jsii.member(jsii_name="crlData")
    def crl_data(self) -> builtins.str:
        '''The x509 v3 specified certificate revocation list (CRL).'''
        return typing.cast(builtins.str, jsii.get(self, "crlData"))

    @crl_data.setter
    def crl_data(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed66d9ba863eea6d35e2d4cbfd1edf02e98c56dc7dda3b94fc817d6daca3df97)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "crlData", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the certificate revocation list (CRL).'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1d928fdb432014275751561985f35592cf848df677c7665616a8cf2fa5d2c60)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the certificate revocation list (CRL) is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67f67da1cd6496f50acb69ea70845c06791dc58959676ea4d9ad986cf862e13d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to attach to the certificate revocation list (CRL).'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3f1ac51324ba6d6018ab752309c8b3267919f50018712dd42bc06bee1676aaa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="trustAnchorArn")
    def trust_anchor_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustAnchorArn"))

    @trust_anchor_arn.setter
    def trust_anchor_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48d0f45de99868389bb39fb7a554a49b731bd29a705766a60e1905c74ce60268)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustAnchorArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnCRLProps",
    jsii_struct_bases=[],
    name_mapping={
        "crl_data": "crlData",
        "name": "name",
        "enabled": "enabled",
        "tags": "tags",
        "trust_anchor_arn": "trustAnchorArn",
    },
)
class CfnCRLProps:
    def __init__(
        self,
        *,
        crl_data: builtins.str,
        name: builtins.str,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trust_anchor_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCRL``.

        :param crl_data: The x509 v3 specified certificate revocation list (CRL).
        :param name: The name of the certificate revocation list (CRL).
        :param enabled: Specifies whether the certificate revocation list (CRL) is enabled.
        :param tags: A list of tags to attach to the certificate revocation list (CRL).
        :param trust_anchor_arn: The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rolesanywhere as rolesanywhere
            
            cfn_cRLProps = rolesanywhere.CfnCRLProps(
                crl_data="crlData",
                name="name",
            
                # the properties below are optional
                enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trust_anchor_arn="trustAnchorArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ed3f37f3e9f738359624c3a5f785fbec8dcaa72621769f31c49a2195c66440)
            check_type(argname="argument crl_data", value=crl_data, expected_type=type_hints["crl_data"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trust_anchor_arn", value=trust_anchor_arn, expected_type=type_hints["trust_anchor_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "crl_data": crl_data,
            "name": name,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if tags is not None:
            self._values["tags"] = tags
        if trust_anchor_arn is not None:
            self._values["trust_anchor_arn"] = trust_anchor_arn

    @builtins.property
    def crl_data(self) -> builtins.str:
        '''The x509 v3 specified certificate revocation list (CRL).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-crldata
        '''
        result = self._values.get("crl_data")
        assert result is not None, "Required property 'crl_data' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the certificate revocation list (CRL).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether the certificate revocation list (CRL) is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags to attach to the certificate revocation list (CRL).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trust_anchor_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the TrustAnchor the certificate revocation list (CRL) will provide revocation for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-crl.html#cfn-rolesanywhere-crl-trustanchorarn
        '''
        result = self._values.get("trust_anchor_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCRLProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnProfile",
):
    '''Creates a *profile* , a list of the roles that Roles Anywhere service is trusted to assume.

    You use profiles to intersect permissions with IAM managed policies.

    *Required permissions:* ``rolesanywhere:CreateProfile`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rolesanywhere as rolesanywhere
        
        cfn_profile = rolesanywhere.CfnProfile(self, "MyCfnProfile",
            name="name",
            role_arns=["roleArns"],
        
            # the properties below are optional
            duration_seconds=123,
            enabled=False,
            managed_policy_arns=["managedPolicyArns"],
            require_instance_properties=False,
            session_policy="sessionPolicy",
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
        role_arns: typing.Sequence[builtins.str],
        duration_seconds: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_instance_properties: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        session_policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the profile.
        :param role_arns: A list of IAM role ARNs. During ``CreateSession`` , if a matching role ARN is provided, the properties in this profile will be applied to the intersection session policy.
        :param duration_seconds: Sets the maximum number of seconds that vended temporary credentials through `CreateSession <https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html>`_ will be valid for, between 900 and 3600.
        :param enabled: Indicates whether the profile is enabled.
        :param managed_policy_arns: A list of managed policy ARNs that apply to the vended session credentials.
        :param require_instance_properties: Specifies whether instance properties are required in temporary credential requests with this profile.
        :param session_policy: A session policy that applies to the trust boundary of the vended session credentials.
        :param tags: The tags to attach to the profile.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15739ec913066dea67815f6297a7c4e3ed351b4df22323a7b46fa138af1a7af8)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProfileProps(
            name=name,
            role_arns=role_arns,
            duration_seconds=duration_seconds,
            enabled=enabled,
            managed_policy_arns=managed_policy_arns,
            require_instance_properties=require_instance_properties,
            session_policy=session_policy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__108c1e464f03498a2ed8b024d67deacffc0a29dab3268a255ff590ab8cbd851c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8cb05bcea72d90681099a28c06fa9c65e9ac5ce9903be5b037d5bc2f939acd98)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileArn")
    def attr_profile_arn(self) -> builtins.str:
        '''The ARN of the profile.

        :cloudformationAttribute: ProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProfileId")
    def attr_profile_id(self) -> builtins.str:
        '''The unique primary identifier of the Profile.

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the profile.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__688802799b2e2e92a74275812390344e30681aca3a945368a5aefaa1ba56cb2c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArns")
    def role_arns(self) -> typing.List[builtins.str]:
        '''A list of IAM role ARNs.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "roleArns"))

    @role_arns.setter
    def role_arns(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8d24089a88ab86238c5340434a58996a10c5d047049180f8bfea3a52c48d03c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArns", value)

    @builtins.property
    @jsii.member(jsii_name="durationSeconds")
    def duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Sets the maximum number of seconds that vended temporary credentials through `CreateSession <https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html>`_ will be valid for, between 900 and 3600.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "durationSeconds"))

    @duration_seconds.setter
    def duration_seconds(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c198b2977e47134c474ca242dadf9d96676c95614df55d34d80a89658dbb1f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "durationSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the profile is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c15a55f732285f57f742ed7762ed5a0b7ee11c61c9fe4d09dae35efacf487f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="managedPolicyArns")
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of managed policy ARNs that apply to the vended session credentials.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "managedPolicyArns"))

    @managed_policy_arns.setter
    def managed_policy_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3a5ba76ab9b068fc7d546e708f8eb49f1139ea08824b7940db1ecc46d892581)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "managedPolicyArns", value)

    @builtins.property
    @jsii.member(jsii_name="requireInstanceProperties")
    def require_instance_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether instance properties are required in temporary credential requests with this profile.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "requireInstanceProperties"))

    @require_instance_properties.setter
    def require_instance_properties(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0e912d03975c81c39b553f40f759c521d19500722ee88d157ee1f254cbba4b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requireInstanceProperties", value)

    @builtins.property
    @jsii.member(jsii_name="sessionPolicy")
    def session_policy(self) -> typing.Optional[builtins.str]:
        '''A session policy that applies to the trust boundary of the vended session credentials.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sessionPolicy"))

    @session_policy.setter
    def session_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e9dc15859e3e9704568f9e80b68a145d23ee9b43107d5f48098e5dc7f40af7f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sessionPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the profile.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99305adebaa684e99f5f2849196087f9cc1788f2b87af7300c436a0feeab285b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "role_arns": "roleArns",
        "duration_seconds": "durationSeconds",
        "enabled": "enabled",
        "managed_policy_arns": "managedPolicyArns",
        "require_instance_properties": "requireInstanceProperties",
        "session_policy": "sessionPolicy",
        "tags": "tags",
    },
)
class CfnProfileProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        role_arns: typing.Sequence[builtins.str],
        duration_seconds: typing.Optional[jsii.Number] = None,
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        require_instance_properties: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        session_policy: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProfile``.

        :param name: The name of the profile.
        :param role_arns: A list of IAM role ARNs. During ``CreateSession`` , if a matching role ARN is provided, the properties in this profile will be applied to the intersection session policy.
        :param duration_seconds: Sets the maximum number of seconds that vended temporary credentials through `CreateSession <https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html>`_ will be valid for, between 900 and 3600.
        :param enabled: Indicates whether the profile is enabled.
        :param managed_policy_arns: A list of managed policy ARNs that apply to the vended session credentials.
        :param require_instance_properties: Specifies whether instance properties are required in temporary credential requests with this profile.
        :param session_policy: A session policy that applies to the trust boundary of the vended session credentials.
        :param tags: The tags to attach to the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rolesanywhere as rolesanywhere
            
            cfn_profile_props = rolesanywhere.CfnProfileProps(
                name="name",
                role_arns=["roleArns"],
            
                # the properties below are optional
                duration_seconds=123,
                enabled=False,
                managed_policy_arns=["managedPolicyArns"],
                require_instance_properties=False,
                session_policy="sessionPolicy",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc8a99a4d25c139ca779820c498d07ef2292a040188712d06b21830cb9c3d764)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arns", value=role_arns, expected_type=type_hints["role_arns"])
            check_type(argname="argument duration_seconds", value=duration_seconds, expected_type=type_hints["duration_seconds"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument managed_policy_arns", value=managed_policy_arns, expected_type=type_hints["managed_policy_arns"])
            check_type(argname="argument require_instance_properties", value=require_instance_properties, expected_type=type_hints["require_instance_properties"])
            check_type(argname="argument session_policy", value=session_policy, expected_type=type_hints["session_policy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "role_arns": role_arns,
        }
        if duration_seconds is not None:
            self._values["duration_seconds"] = duration_seconds
        if enabled is not None:
            self._values["enabled"] = enabled
        if managed_policy_arns is not None:
            self._values["managed_policy_arns"] = managed_policy_arns
        if require_instance_properties is not None:
            self._values["require_instance_properties"] = require_instance_properties
        if session_policy is not None:
            self._values["session_policy"] = session_policy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arns(self) -> typing.List[builtins.str]:
        '''A list of IAM role ARNs.

        During ``CreateSession`` , if a matching role ARN is provided, the properties in this profile will be applied to the intersection session policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-rolearns
        '''
        result = self._values.get("role_arns")
        assert result is not None, "Required property 'role_arns' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def duration_seconds(self) -> typing.Optional[jsii.Number]:
        '''Sets the maximum number of seconds that vended temporary credentials through `CreateSession <https://docs.aws.amazon.com/rolesanywhere/latest/userguide/authentication-create-session.html>`_ will be valid for, between 900 and 3600.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-durationseconds
        '''
        result = self._values.get("duration_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the profile is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def managed_policy_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of managed policy ARNs that apply to the vended session credentials.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-managedpolicyarns
        '''
        result = self._values.get("managed_policy_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def require_instance_properties(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether instance properties are required in temporary credential requests with this profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-requireinstanceproperties
        '''
        result = self._values.get("require_instance_properties")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def session_policy(self) -> typing.Optional[builtins.str]:
        '''A session policy that applies to the trust boundary of the vended session credentials.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-sessionpolicy
        '''
        result = self._values.get("session_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the profile.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-profile.html#cfn-rolesanywhere-profile-tags
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
class CfnTrustAnchor(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnTrustAnchor",
):
    '''Creates a trust anchor to establish trust between IAM Roles Anywhere and your certificate authority (CA).

    You can define a trust anchor as a reference to an AWS Private Certificate Authority ( AWS Private CA ) or by uploading a CA certificate. Your AWS workloads can authenticate with the trust anchor using certificates issued by the CA in exchange for temporary AWS credentials.

    *Required permissions:* ``rolesanywhere:CreateTrustAnchor`` .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_rolesanywhere as rolesanywhere
        
        cfn_trust_anchor = rolesanywhere.CfnTrustAnchor(self, "MyCfnTrustAnchor",
            name="name",
            source=rolesanywhere.CfnTrustAnchor.SourceProperty(
                source_data=rolesanywhere.CfnTrustAnchor.SourceDataProperty(
                    acm_pca_arn="acmPcaArn",
                    x509_certificate_data="x509CertificateData"
                ),
                source_type="sourceType"
            ),
        
            # the properties below are optional
            enabled=False,
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
        source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrustAnchor.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the trust anchor.
        :param source: The trust anchor type and its related certificate data.
        :param enabled: Indicates whether the trust anchor is enabled.
        :param tags: The tags to attach to the trust anchor.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fba7372f75a907053dd110f3529fe09fcae6182a22a6de9556840fb3ef45a7e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrustAnchorProps(
            name=name, source=source, enabled=enabled, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b9cfbe10bfdb6cef935d4ff153ccc2bfa14f7d75a5fc9e9b33a6065c5f889fb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1a446ba97f46d9e40a872fe9e5c8ab9a29d412e3abddb5a083f90ceb444714e1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrTrustAnchorArn")
    def attr_trust_anchor_arn(self) -> builtins.str:
        '''The ARN of the trust anchor.

        :cloudformationAttribute: TrustAnchorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrustAnchorArn"))

    @builtins.property
    @jsii.member(jsii_name="attrTrustAnchorId")
    def attr_trust_anchor_id(self) -> builtins.str:
        '''The unique identifier of the trust anchor.

        :cloudformationAttribute: TrustAnchorId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrustAnchorId"))

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
        '''The name of the trust anchor.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__265c9ab39383974ed99c7175f30b9a4ceb5f22cd577edbe2f82df8bf06a4b9a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnTrustAnchor.SourceProperty"]:
        '''The trust anchor type and its related certificate data.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnTrustAnchor.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnTrustAnchor.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b96b35b1c2f1a1254cda56368cc47ef0b688766951d9ea203e33c12867524fc6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="enabled")
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the trust anchor is enabled.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enabled"))

    @enabled.setter
    def enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71c1dcfb08f1fa865b29567c29660256ff1249099dfa782cfa24a3d18aa3505b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enabled", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the trust anchor.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d275a36ee2ff1f9512bd9df7c7f4cb41f4083d1e9467ade7c410954159920c6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnTrustAnchor.SourceDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "acm_pca_arn": "acmPcaArn",
            "x509_certificate_data": "x509CertificateData",
        },
    )
    class SourceDataProperty:
        def __init__(
            self,
            *,
            acm_pca_arn: typing.Optional[builtins.str] = None,
            x509_certificate_data: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The data field of the trust anchor depending on its type.

            :param acm_pca_arn: The root certificate of the AWS Private Certificate Authority specified by this ARN is used in trust validation for temporary credential requests. Included for trust anchors of type ``AWS_ACM_PCA`` . .. epigraph:: This field is not supported in your region.
            :param x509_certificate_data: The PEM-encoded data for the certificate anchor. Included for trust anchors of type ``CERTIFICATE_BUNDLE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rolesanywhere as rolesanywhere
                
                source_data_property = rolesanywhere.CfnTrustAnchor.SourceDataProperty(
                    acm_pca_arn="acmPcaArn",
                    x509_certificate_data="x509CertificateData"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__aa369b3cbba73a987e4f4a9a410e56c8fdd5c7ce2300cda6a55e4ec9a19a6745)
                check_type(argname="argument acm_pca_arn", value=acm_pca_arn, expected_type=type_hints["acm_pca_arn"])
                check_type(argname="argument x509_certificate_data", value=x509_certificate_data, expected_type=type_hints["x509_certificate_data"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if acm_pca_arn is not None:
                self._values["acm_pca_arn"] = acm_pca_arn
            if x509_certificate_data is not None:
                self._values["x509_certificate_data"] = x509_certificate_data

        @builtins.property
        def acm_pca_arn(self) -> typing.Optional[builtins.str]:
            '''The root certificate of the AWS Private Certificate Authority specified by this ARN is used in trust validation for temporary credential requests.

            Included for trust anchors of type ``AWS_ACM_PCA`` .
            .. epigraph::

               This field is not supported in your region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html#cfn-rolesanywhere-trustanchor-sourcedata-acmpcaarn
            '''
            result = self._values.get("acm_pca_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def x509_certificate_data(self) -> typing.Optional[builtins.str]:
            '''The PEM-encoded data for the certificate anchor.

            Included for trust anchors of type ``CERTIFICATE_BUNDLE`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-sourcedata.html#cfn-rolesanywhere-trustanchor-sourcedata-x509certificatedata
            '''
            result = self._values.get("x509_certificate_data")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnTrustAnchor.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={"source_data": "sourceData", "source_type": "sourceType"},
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            source_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTrustAnchor.SourceDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The trust anchor type and its related certificate data.

            :param source_data: The data field of the trust anchor depending on its type.
            :param source_type: The type of the TrustAnchor. .. epigraph:: ``AWS_ACM_PCA`` is not an allowed value in your region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_rolesanywhere as rolesanywhere
                
                source_property = rolesanywhere.CfnTrustAnchor.SourceProperty(
                    source_data=rolesanywhere.CfnTrustAnchor.SourceDataProperty(
                        acm_pca_arn="acmPcaArn",
                        x509_certificate_data="x509CertificateData"
                    ),
                    source_type="sourceType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d423be7ff47fcc8761e7797ad37aac03811962bc633d561f5c9c8721dd3e77df)
                check_type(argname="argument source_data", value=source_data, expected_type=type_hints["source_data"])
                check_type(argname="argument source_type", value=source_type, expected_type=type_hints["source_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if source_data is not None:
                self._values["source_data"] = source_data
            if source_type is not None:
                self._values["source_type"] = source_type

        @builtins.property
        def source_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrustAnchor.SourceDataProperty"]]:
            '''The data field of the trust anchor depending on its type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html#cfn-rolesanywhere-trustanchor-source-sourcedata
            '''
            result = self._values.get("source_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTrustAnchor.SourceDataProperty"]], result)

        @builtins.property
        def source_type(self) -> typing.Optional[builtins.str]:
            '''The type of the TrustAnchor.

            .. epigraph::

               ``AWS_ACM_PCA`` is not an allowed value in your region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-rolesanywhere-trustanchor-source.html#cfn-rolesanywhere-trustanchor-source-sourcetype
            '''
            result = self._values.get("source_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_rolesanywhere.CfnTrustAnchorProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source": "source",
        "enabled": "enabled",
        "tags": "tags",
    },
)
class CfnTrustAnchorProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrustAnchor.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
        enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrustAnchor``.

        :param name: The name of the trust anchor.
        :param source: The trust anchor type and its related certificate data.
        :param enabled: Indicates whether the trust anchor is enabled.
        :param tags: The tags to attach to the trust anchor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_rolesanywhere as rolesanywhere
            
            cfn_trust_anchor_props = rolesanywhere.CfnTrustAnchorProps(
                name="name",
                source=rolesanywhere.CfnTrustAnchor.SourceProperty(
                    source_data=rolesanywhere.CfnTrustAnchor.SourceDataProperty(
                        acm_pca_arn="acmPcaArn",
                        x509_certificate_data="x509CertificateData"
                    ),
                    source_type="sourceType"
                ),
            
                # the properties below are optional
                enabled=False,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aecfaf7030b586bd60e26cea2bf3123c06c4f75b114eeece3ea9fa0b08526da7)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "source": source,
        }
        if enabled is not None:
            self._values["enabled"] = enabled
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the trust anchor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnTrustAnchor.SourceProperty]:
        '''The trust anchor type and its related certificate data.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnTrustAnchor.SourceProperty], result)

    @builtins.property
    def enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Indicates whether the trust anchor is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-enabled
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to attach to the trust anchor.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rolesanywhere-trustanchor.html#cfn-rolesanywhere-trustanchor-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrustAnchorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCRL",
    "CfnCRLProps",
    "CfnProfile",
    "CfnProfileProps",
    "CfnTrustAnchor",
    "CfnTrustAnchorProps",
]

publication.publish()

def _typecheckingstub__f35b45debe8136e3de3e7d231f09e2d880d31e3c89eb1adb6a8c5613dbf5fb7f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    crl_data: builtins.str,
    name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trust_anchor_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dd9193cb33ddf82dba5396e1ae096cc9b451b4296ca2900997bdae6a30a6f44(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d10b773e20eed62703f59de20a71328b2e79ce6922709bd59397acc4f352a08(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed66d9ba863eea6d35e2d4cbfd1edf02e98c56dc7dda3b94fc817d6daca3df97(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1d928fdb432014275751561985f35592cf848df677c7665616a8cf2fa5d2c60(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67f67da1cd6496f50acb69ea70845c06791dc58959676ea4d9ad986cf862e13d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3f1ac51324ba6d6018ab752309c8b3267919f50018712dd42bc06bee1676aaa(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48d0f45de99868389bb39fb7a554a49b731bd29a705766a60e1905c74ce60268(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ed3f37f3e9f738359624c3a5f785fbec8dcaa72621769f31c49a2195c66440(
    *,
    crl_data: builtins.str,
    name: builtins.str,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trust_anchor_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15739ec913066dea67815f6297a7c4e3ed351b4df22323a7b46fa138af1a7af8(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    role_arns: typing.Sequence[builtins.str],
    duration_seconds: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    require_instance_properties: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    session_policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__108c1e464f03498a2ed8b024d67deacffc0a29dab3268a255ff590ab8cbd851c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cb05bcea72d90681099a28c06fa9c65e9ac5ce9903be5b037d5bc2f939acd98(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__688802799b2e2e92a74275812390344e30681aca3a945368a5aefaa1ba56cb2c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d24089a88ab86238c5340434a58996a10c5d047049180f8bfea3a52c48d03c(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c198b2977e47134c474ca242dadf9d96676c95614df55d34d80a89658dbb1f75(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c15a55f732285f57f742ed7762ed5a0b7ee11c61c9fe4d09dae35efacf487f6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3a5ba76ab9b068fc7d546e708f8eb49f1139ea08824b7940db1ecc46d892581(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0e912d03975c81c39b553f40f759c521d19500722ee88d157ee1f254cbba4b8(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e9dc15859e3e9704568f9e80b68a145d23ee9b43107d5f48098e5dc7f40af7f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99305adebaa684e99f5f2849196087f9cc1788f2b87af7300c436a0feeab285b(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc8a99a4d25c139ca779820c498d07ef2292a040188712d06b21830cb9c3d764(
    *,
    name: builtins.str,
    role_arns: typing.Sequence[builtins.str],
    duration_seconds: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    managed_policy_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    require_instance_properties: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    session_policy: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fba7372f75a907053dd110f3529fe09fcae6182a22a6de9556840fb3ef45a7e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrustAnchor.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b9cfbe10bfdb6cef935d4ff153ccc2bfa14f7d75a5fc9e9b33a6065c5f889fb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a446ba97f46d9e40a872fe9e5c8ab9a29d412e3abddb5a083f90ceb444714e1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__265c9ab39383974ed99c7175f30b9a4ceb5f22cd577edbe2f82df8bf06a4b9a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b96b35b1c2f1a1254cda56368cc47ef0b688766951d9ea203e33c12867524fc6(
    value: typing.Union[_IResolvable_da3f097b, CfnTrustAnchor.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71c1dcfb08f1fa865b29567c29660256ff1249099dfa782cfa24a3d18aa3505b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d275a36ee2ff1f9512bd9df7c7f4cb41f4083d1e9467ade7c410954159920c6(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa369b3cbba73a987e4f4a9a410e56c8fdd5c7ce2300cda6a55e4ec9a19a6745(
    *,
    acm_pca_arn: typing.Optional[builtins.str] = None,
    x509_certificate_data: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d423be7ff47fcc8761e7797ad37aac03811962bc633d561f5c9c8721dd3e77df(
    *,
    source_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrustAnchor.SourceDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aecfaf7030b586bd60e26cea2bf3123c06c4f75b114eeece3ea9fa0b08526da7(
    *,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnTrustAnchor.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
