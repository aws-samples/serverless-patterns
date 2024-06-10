'''
# AWS::WorkSpacesWeb Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_workspacesweb as workspacesweb
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for WorkSpacesWeb construct libraries](https://constructs.dev/search?q=workspacesweb)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::WorkSpacesWeb resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesWeb.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::WorkSpacesWeb](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_WorkSpacesWeb.html).

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


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnBrowserSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnBrowserSettings",
):
    '''This resource specifies browser settings that can be associated with a web portal.

    Once associated with a web portal, browser settings control how the browser will behave once a user starts a streaming session for the web portal.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html
    :cloudformationResource: AWS::WorkSpacesWeb::BrowserSettings
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_browser_settings = workspacesweb.CfnBrowserSettings(self, "MyCfnBrowserSettings",
            additional_encryption_context={
                "additional_encryption_context_key": "additionalEncryptionContext"
            },
            browser_policy="browserPolicy",
            customer_managed_key="customerManagedKey",
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
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        browser_policy: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param additional_encryption_context: Additional encryption context of the browser settings.
        :param browser_policy: A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.
        :param customer_managed_key: The custom managed key of the browser settings. *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``
        :param tags: The tags to add to the browser settings resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bddcc45afa30e005718c5da3d3034bff6b9c0453326851818da6294dc041bb0f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBrowserSettingsProps(
            additional_encryption_context=additional_encryption_context,
            browser_policy=browser_policy,
            customer_managed_key=customer_managed_key,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d4203cdc61a30c217fc2abe263c4776ac7f7dc3efdc691f65b8b0f98c469206)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4cab7e5af66cb2aa7162f6b46ea25dc53695260ce84c6550f897b70bab862ee)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPortalArns")
    def attr_associated_portal_arns(self) -> typing.List[builtins.str]:
        '''A list of web portal ARNs that the browser settings resource is associated with.

        :cloudformationAttribute: AssociatedPortalArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAssociatedPortalArns"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserSettingsArn")
    def attr_browser_settings_arn(self) -> builtins.str:
        '''The ARN of the browser settings.

        :cloudformationAttribute: BrowserSettingsArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserSettingsArn"))

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
    @jsii.member(jsii_name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional encryption context of the browser settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "additionalEncryptionContext"))

    @additional_encryption_context.setter
    def additional_encryption_context(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70de4dee5d14f114274fd7960c64b6accb0ec49e02c002b5521af87f035095c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalEncryptionContext", value)

    @builtins.property
    @jsii.member(jsii_name="browserPolicy")
    def browser_policy(self) -> typing.Optional[builtins.str]:
        '''A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "browserPolicy"))

    @browser_policy.setter
    def browser_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1ed58b3fc2a2966bf9a096153c9b38b0a594ab0c629bf8b97e6011a61ebfb79)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserPolicy", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The custom managed key of the browser settings.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKey"))

    @customer_managed_key.setter
    def customer_managed_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eed13ab23af9a957ff225aff9f958ae8f40efe7f9c0aa02be45034aa22a364c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKey", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the browser settings resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__488a7e6081f5fbb5bf5af995cdb747f920d592e19ef88a222e5aa2f1c21d8a53)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnBrowserSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "additional_encryption_context": "additionalEncryptionContext",
        "browser_policy": "browserPolicy",
        "customer_managed_key": "customerManagedKey",
        "tags": "tags",
    },
)
class CfnBrowserSettingsProps:
    def __init__(
        self,
        *,
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        browser_policy: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBrowserSettings``.

        :param additional_encryption_context: Additional encryption context of the browser settings.
        :param browser_policy: A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.
        :param customer_managed_key: The custom managed key of the browser settings. *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``
        :param tags: The tags to add to the browser settings resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_browser_settings_props = workspacesweb.CfnBrowserSettingsProps(
                additional_encryption_context={
                    "additional_encryption_context_key": "additionalEncryptionContext"
                },
                browser_policy="browserPolicy",
                customer_managed_key="customerManagedKey",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f99c227d497f6d51d01cc19398b94784835fab55afca7c6488466bb1cc1420b3)
            check_type(argname="argument additional_encryption_context", value=additional_encryption_context, expected_type=type_hints["additional_encryption_context"])
            check_type(argname="argument browser_policy", value=browser_policy, expected_type=type_hints["browser_policy"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_encryption_context is not None:
            self._values["additional_encryption_context"] = additional_encryption_context
        if browser_policy is not None:
            self._values["browser_policy"] = browser_policy
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional encryption context of the browser settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-additionalencryptioncontext
        '''
        result = self._values.get("additional_encryption_context")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def browser_policy(self) -> typing.Optional[builtins.str]:
        '''A JSON string containing Chrome Enterprise policies that will be applied to all streaming sessions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-browserpolicy
        '''
        result = self._values.get("browser_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The custom managed key of the browser settings.

        *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-customermanagedkey
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the browser settings resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-browsersettings.html#cfn-workspacesweb-browsersettings-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBrowserSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIdentityProvider(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnIdentityProvider",
):
    '''This resource specifies an identity provider that is then associated with a web portal.

    This resource is not required if your portal's ``AuthenticationType`` is IAM Identity Center.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html
    :cloudformationResource: AWS::WorkSpacesWeb::IdentityProvider
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_identity_provider = workspacesweb.CfnIdentityProvider(self, "MyCfnIdentityProvider",
            identity_provider_details={
                "identity_provider_details_key": "identityProviderDetails"
            },
            identity_provider_name="identityProviderName",
            identity_provider_type="identityProviderType",
        
            # the properties below are optional
            portal_arn="portalArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        identity_provider_details: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        identity_provider_name: builtins.str,
        identity_provider_type: builtins.str,
        portal_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param identity_provider_details: The identity provider details. The following list describes the provider detail keys for each identity provider type. - For Google and Login with Amazon: - ``client_id`` - ``client_secret`` - ``authorize_scopes`` - For Facebook: - ``client_id`` - ``client_secret`` - ``authorize_scopes`` - ``api_version`` - For Sign in with Apple: - ``client_id`` - ``team_id`` - ``key_id`` - ``private_key`` - ``authorize_scopes`` - For OIDC providers: - ``client_id`` - ``client_secret`` - ``attributes_request_method`` - ``oidc_issuer`` - ``authorize_scopes`` - ``authorize_url`` *if not available from discovery URL specified by oidc_issuer key* - ``token_url`` *if not available from discovery URL specified by oidc_issuer key* - ``attributes_url`` *if not available from discovery URL specified by oidc_issuer key* - ``jwks_uri`` *if not available from discovery URL specified by oidc_issuer key* - For SAML providers: - ``MetadataFile`` OR ``MetadataURL`` - ``IDPSignout`` (boolean) *optional* - ``IDPInit`` (boolean) *optional* - ``RequestSigningAlgorithm`` (string) *optional* - Only accepts ``rsa-sha256`` - ``EncryptedResponses`` (boolean) *optional*
        :param identity_provider_name: The identity provider name.
        :param identity_provider_type: The identity provider type.
        :param portal_arn: The ARN of the identity provider.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__439cd32d129b1f0a69c13fb5a494170084be122497b619a7175debec51c3635e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdentityProviderProps(
            identity_provider_details=identity_provider_details,
            identity_provider_name=identity_provider_name,
            identity_provider_type=identity_provider_type,
            portal_arn=portal_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ace0da6a7e7e7a968ac58e8be1ce9dcb15a96bae8fad93e7c341ff5392bed56c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ec876abe2e87a8e0cb2641e36f36bd29bb0a19b65cc2d8f6be54a630a22b3af8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentityProviderArn")
    def attr_identity_provider_arn(self) -> builtins.str:
        '''The ARN of the identity provider.

        :cloudformationAttribute: IdentityProviderArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentityProviderArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="identityProviderDetails")
    def identity_provider_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
        '''The identity provider details.

        The following list describes the provider detail keys for each identity provider type.
        '''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "identityProviderDetails"))

    @identity_provider_details.setter
    def identity_provider_details(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ae08bcbb1d55c54b06801705e4c1effec06173b9d5c1ab7d0301258d84aa63a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderDetails", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderName")
    def identity_provider_name(self) -> builtins.str:
        '''The identity provider name.'''
        return typing.cast(builtins.str, jsii.get(self, "identityProviderName"))

    @identity_provider_name.setter
    def identity_provider_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__47d337423f7a1ca0a276c2a641c1f67e69f1933efe04994ab3be413955030b14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderName", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderType")
    def identity_provider_type(self) -> builtins.str:
        '''The identity provider type.'''
        return typing.cast(builtins.str, jsii.get(self, "identityProviderType"))

    @identity_provider_type.setter
    def identity_provider_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72551994233ed9e106da8e5840c9077e96c1a7cafc63617736585c1eb83fd2da)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderType", value)

    @builtins.property
    @jsii.member(jsii_name="portalArn")
    def portal_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the identity provider.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "portalArn"))

    @portal_arn.setter
    def portal_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17f07edd6f61424250e1f5f7df6f6cee024beb494ee700c6419c5642ebe36e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "portalArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnIdentityProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity_provider_details": "identityProviderDetails",
        "identity_provider_name": "identityProviderName",
        "identity_provider_type": "identityProviderType",
        "portal_arn": "portalArn",
    },
)
class CfnIdentityProviderProps:
    def __init__(
        self,
        *,
        identity_provider_details: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        identity_provider_name: builtins.str,
        identity_provider_type: builtins.str,
        portal_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdentityProvider``.

        :param identity_provider_details: The identity provider details. The following list describes the provider detail keys for each identity provider type. - For Google and Login with Amazon: - ``client_id`` - ``client_secret`` - ``authorize_scopes`` - For Facebook: - ``client_id`` - ``client_secret`` - ``authorize_scopes`` - ``api_version`` - For Sign in with Apple: - ``client_id`` - ``team_id`` - ``key_id`` - ``private_key`` - ``authorize_scopes`` - For OIDC providers: - ``client_id`` - ``client_secret`` - ``attributes_request_method`` - ``oidc_issuer`` - ``authorize_scopes`` - ``authorize_url`` *if not available from discovery URL specified by oidc_issuer key* - ``token_url`` *if not available from discovery URL specified by oidc_issuer key* - ``attributes_url`` *if not available from discovery URL specified by oidc_issuer key* - ``jwks_uri`` *if not available from discovery URL specified by oidc_issuer key* - For SAML providers: - ``MetadataFile`` OR ``MetadataURL`` - ``IDPSignout`` (boolean) *optional* - ``IDPInit`` (boolean) *optional* - ``RequestSigningAlgorithm`` (string) *optional* - Only accepts ``rsa-sha256`` - ``EncryptedResponses`` (boolean) *optional*
        :param identity_provider_name: The identity provider name.
        :param identity_provider_type: The identity provider type.
        :param portal_arn: The ARN of the identity provider.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_identity_provider_props = workspacesweb.CfnIdentityProviderProps(
                identity_provider_details={
                    "identity_provider_details_key": "identityProviderDetails"
                },
                identity_provider_name="identityProviderName",
                identity_provider_type="identityProviderType",
            
                # the properties below are optional
                portal_arn="portalArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc73238ea7aab35d7f7ec21a88a98c698e64b413b81129270666c830ae963a4d)
            check_type(argname="argument identity_provider_details", value=identity_provider_details, expected_type=type_hints["identity_provider_details"])
            check_type(argname="argument identity_provider_name", value=identity_provider_name, expected_type=type_hints["identity_provider_name"])
            check_type(argname="argument identity_provider_type", value=identity_provider_type, expected_type=type_hints["identity_provider_type"])
            check_type(argname="argument portal_arn", value=portal_arn, expected_type=type_hints["portal_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity_provider_details": identity_provider_details,
            "identity_provider_name": identity_provider_name,
            "identity_provider_type": identity_provider_type,
        }
        if portal_arn is not None:
            self._values["portal_arn"] = portal_arn

    @builtins.property
    def identity_provider_details(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
        '''The identity provider details. The following list describes the provider detail keys for each identity provider type.

        - For Google and Login with Amazon:
        - ``client_id``
        - ``client_secret``
        - ``authorize_scopes``
        - For Facebook:
        - ``client_id``
        - ``client_secret``
        - ``authorize_scopes``
        - ``api_version``
        - For Sign in with Apple:
        - ``client_id``
        - ``team_id``
        - ``key_id``
        - ``private_key``
        - ``authorize_scopes``
        - For OIDC providers:
        - ``client_id``
        - ``client_secret``
        - ``attributes_request_method``
        - ``oidc_issuer``
        - ``authorize_scopes``
        - ``authorize_url`` *if not available from discovery URL specified by oidc_issuer key*
        - ``token_url`` *if not available from discovery URL specified by oidc_issuer key*
        - ``attributes_url`` *if not available from discovery URL specified by oidc_issuer key*
        - ``jwks_uri`` *if not available from discovery URL specified by oidc_issuer key*
        - For SAML providers:
        - ``MetadataFile`` OR ``MetadataURL``
        - ``IDPSignout`` (boolean) *optional*
        - ``IDPInit`` (boolean) *optional*
        - ``RequestSigningAlgorithm`` (string) *optional* - Only accepts ``rsa-sha256``
        - ``EncryptedResponses`` (boolean) *optional*

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-identityproviderdetails
        '''
        result = self._values.get("identity_provider_details")
        assert result is not None, "Required property 'identity_provider_details' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def identity_provider_name(self) -> builtins.str:
        '''The identity provider name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-identityprovidername
        '''
        result = self._values.get("identity_provider_name")
        assert result is not None, "Required property 'identity_provider_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def identity_provider_type(self) -> builtins.str:
        '''The identity provider type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-identityprovidertype
        '''
        result = self._values.get("identity_provider_type")
        assert result is not None, "Required property 'identity_provider_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def portal_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the identity provider.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-identityprovider.html#cfn-workspacesweb-identityprovider-portalarn
        '''
        result = self._values.get("portal_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdentityProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnIpAccessSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnIpAccessSettings",
):
    '''This resource specifies IP access settings that can be associated with a web portal.

    For more information, see `Set up IP access controls (optional) <https://docs.aws.amazon.com/workspaces-web/latest/adminguide/ip-access-controls.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html
    :cloudformationResource: AWS::WorkSpacesWeb::IpAccessSettings
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_ip_access_settings = workspacesweb.CfnIpAccessSettings(self, "MyCfnIpAccessSettings",
            ip_rules=[workspacesweb.CfnIpAccessSettings.IpRuleProperty(
                ip_range="ipRange",
        
                # the properties below are optional
                description="description"
            )],
        
            # the properties below are optional
            additional_encryption_context={
                "additional_encryption_context_key": "additionalEncryptionContext"
            },
            customer_managed_key="customerManagedKey",
            description="description",
            display_name="displayName",
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
        ip_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIpAccessSettings.IpRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param ip_rules: The IP rules of the IP access settings.
        :param additional_encryption_context: Additional encryption context of the IP access settings.
        :param customer_managed_key: The custom managed key of the IP access settings. *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``
        :param description: The description of the IP access settings.
        :param display_name: The display name of the IP access settings.
        :param tags: The tags to add to the browser settings resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e3f00304b675ee88c29734b1fad40f8e448afe808a4226188c1c74e8ed82fe0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIpAccessSettingsProps(
            ip_rules=ip_rules,
            additional_encryption_context=additional_encryption_context,
            customer_managed_key=customer_managed_key,
            description=description,
            display_name=display_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__522d314ff55f65afebb67835c03df17342b3167bed24e30c591f5aef150973f0)
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
            type_hints = typing.get_type_hints(_typecheckingstub__dd4736646712efdcfa8ece881cd4fa733fb537f01432db179870ed0f95ff0512)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPortalArns")
    def attr_associated_portal_arns(self) -> typing.List[builtins.str]:
        '''A list of web portal ARNs that this IP access settings resource is associated with.

        :cloudformationAttribute: AssociatedPortalArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAssociatedPortalArns"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The creation date timestamp of the IP access settings.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrIpAccessSettingsArn")
    def attr_ip_access_settings_arn(self) -> builtins.str:
        '''The ARN of the IP access settings resource.

        :cloudformationAttribute: IpAccessSettingsArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIpAccessSettingsArn"))

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
    @jsii.member(jsii_name="ipRules")
    def ip_rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIpAccessSettings.IpRuleProperty"]]]:
        '''The IP rules of the IP access settings.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIpAccessSettings.IpRuleProperty"]]], jsii.get(self, "ipRules"))

    @ip_rules.setter
    def ip_rules(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIpAccessSettings.IpRuleProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc300ade0369b0ab447aa7806a51ee2809fea6ffd0fffc0129fb173b7f3886cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipRules", value)

    @builtins.property
    @jsii.member(jsii_name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional encryption context of the IP access settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "additionalEncryptionContext"))

    @additional_encryption_context.setter
    def additional_encryption_context(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f120862dd3a18b3da3624f1bbb9a6b2ec04ea91c5a0d22f1306ab87a46a1e28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalEncryptionContext", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The custom managed key of the IP access settings.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKey"))

    @customer_managed_key.setter
    def customer_managed_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__057facdda1fc071bcb0a19a16cf182f52ac2a874ba9674ab1e2f710144816eae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKey", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the IP access settings.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6b724cabf90e359bbb06c7a32f43432bf7cb19a46eb5e9f240789471612d5b8b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the IP access settings.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98ac230b64daa6cce74b4ea14502d07e7a0dcc81bb5bd7c233a62ad5907f6083)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the browser settings resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6ebcd54b862693c4f7d257e8db3f90e6315f91bc32c16e7865b2e93f91ff381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesweb.CfnIpAccessSettings.IpRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_range": "ipRange", "description": "description"},
    )
    class IpRuleProperty:
        def __init__(
            self,
            *,
            ip_range: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The IP rules of the IP access settings.

            :param ip_range: The IP range of the IP rule. This can either be a single IP address or a range using CIDR notation.
            :param description: The description of the IP rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-ipaccesssettings-iprule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesweb as workspacesweb
                
                ip_rule_property = workspacesweb.CfnIpAccessSettings.IpRuleProperty(
                    ip_range="ipRange",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ef91a56d003f837ee2a6f8431647b2dcdd5ff9d72afb0d6f7cb1c50cc1a6890)
                check_type(argname="argument ip_range", value=ip_range, expected_type=type_hints["ip_range"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip_range": ip_range,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def ip_range(self) -> builtins.str:
            '''The IP range of the IP rule.

            This can either be a single IP address or a range using CIDR notation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-ipaccesssettings-iprule.html#cfn-workspacesweb-ipaccesssettings-iprule-iprange
            '''
            result = self._values.get("ip_range")
            assert result is not None, "Required property 'ip_range' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the IP rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-ipaccesssettings-iprule.html#cfn-workspacesweb-ipaccesssettings-iprule-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnIpAccessSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "ip_rules": "ipRules",
        "additional_encryption_context": "additionalEncryptionContext",
        "customer_managed_key": "customerManagedKey",
        "description": "description",
        "display_name": "displayName",
        "tags": "tags",
    },
)
class CfnIpAccessSettingsProps:
    def __init__(
        self,
        *,
        ip_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIpAccessSettings.IpRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIpAccessSettings``.

        :param ip_rules: The IP rules of the IP access settings.
        :param additional_encryption_context: Additional encryption context of the IP access settings.
        :param customer_managed_key: The custom managed key of the IP access settings. *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``
        :param description: The description of the IP access settings.
        :param display_name: The display name of the IP access settings.
        :param tags: The tags to add to the browser settings resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_ip_access_settings_props = workspacesweb.CfnIpAccessSettingsProps(
                ip_rules=[workspacesweb.CfnIpAccessSettings.IpRuleProperty(
                    ip_range="ipRange",
            
                    # the properties below are optional
                    description="description"
                )],
            
                # the properties below are optional
                additional_encryption_context={
                    "additional_encryption_context_key": "additionalEncryptionContext"
                },
                customer_managed_key="customerManagedKey",
                description="description",
                display_name="displayName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__332b0cacbcd242c5add5b067133a69e3ee9f775e64856bf6ae48c84e34d0b475)
            check_type(argname="argument ip_rules", value=ip_rules, expected_type=type_hints["ip_rules"])
            check_type(argname="argument additional_encryption_context", value=additional_encryption_context, expected_type=type_hints["additional_encryption_context"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ip_rules": ip_rules,
        }
        if additional_encryption_context is not None:
            self._values["additional_encryption_context"] = additional_encryption_context
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if description is not None:
            self._values["description"] = description
        if display_name is not None:
            self._values["display_name"] = display_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def ip_rules(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIpAccessSettings.IpRuleProperty]]]:
        '''The IP rules of the IP access settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-iprules
        '''
        result = self._values.get("ip_rules")
        assert result is not None, "Required property 'ip_rules' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIpAccessSettings.IpRuleProperty]]], result)

    @builtins.property
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''Additional encryption context of the IP access settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-additionalencryptioncontext
        '''
        result = self._values.get("additional_encryption_context")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The custom managed key of the IP access settings.

        *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-customermanagedkey
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the IP access settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The display name of the IP access settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the browser settings resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-ipaccesssettings.html#cfn-workspacesweb-ipaccesssettings-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIpAccessSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnNetworkSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnNetworkSettings",
):
    '''This resource specifies network settings that can be associated with a web portal.

    Once associated with a web portal, network settings define how streaming instances will connect with your specified VPC.

    The VPC must have default tenancy. VPCs with dedicated tenancy are not supported.

    For availability consideration, you must have at least two subnets created in two different Availability Zones. WorkSpaces Web is available in a subset of the Availability Zones for each supported Region. For more information, see `Supported Availability Zones <https://docs.aws.amazon.com/workspaces-web/latest/adminguide/availability-zones.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html
    :cloudformationResource: AWS::WorkSpacesWeb::NetworkSettings
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_network_settings = workspacesweb.CfnNetworkSettings(self, "MyCfnNetworkSettings",
            security_group_ids=["securityGroupIds"],
            subnet_ids=["subnetIds"],
            vpc_id="vpcId",
        
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
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param security_group_ids: One or more security groups used to control access from streaming instances to your VPC. *Pattern* : ``^[\\w+\\-]+$``
        :param subnet_ids: The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones. *Pattern* : ``^subnet-([0-9a-f]{8}|[0-9a-f]{17})$``
        :param vpc_id: The VPC that streaming instances will connect to. *Pattern* : ``^vpc-[0-9a-z]*$``
        :param tags: The tags to add to the network settings resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95a61d7b0b1452fb7a5fdde6d41bbab0a1737a4628bbe5a201c16ce50a3e8a67)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnNetworkSettingsProps(
            security_group_ids=security_group_ids,
            subnet_ids=subnet_ids,
            vpc_id=vpc_id,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b18b2266ad8a399dab2a39759ddd4f261e866f9af5f84bd2281d2d5717327fc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e59ed5f61334e6922894c4c8b1588d6af1336b159abb632a02c51a1b16724fd0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPortalArns")
    def attr_associated_portal_arns(self) -> typing.List[builtins.str]:
        '''A list of web portal ARNs that this network settings is associated with.

        :cloudformationAttribute: AssociatedPortalArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAssociatedPortalArns"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkSettingsArn")
    def attr_network_settings_arn(self) -> builtins.str:
        '''The ARN of the network settings.

        :cloudformationAttribute: NetworkSettingsArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNetworkSettingsArn"))

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
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''One or more security groups used to control access from streaming instances to your VPC.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3554fe26b5fd797fb5730682ce023c2460621ebeec517b2840620081484a64ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The subnets in which network interfaces are created to connect streaming instances to your VPC.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b27a5b7c5de5fd73e2955aa73ff7e658050d13d9e84df9804b230c062f75d81)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The VPC that streaming instances will connect to.'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e298ee4542dc4160ff007ee478b4d24dff6a5105564e454a0eacb28ac7aeab52)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the network settings resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07819661df503a5395aeb2f48e629b4742564eaa4d650197b66c74bb51c0efc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnNetworkSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "security_group_ids": "securityGroupIds",
        "subnet_ids": "subnetIds",
        "vpc_id": "vpcId",
        "tags": "tags",
    },
)
class CfnNetworkSettingsProps:
    def __init__(
        self,
        *,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_ids: typing.Sequence[builtins.str],
        vpc_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnNetworkSettings``.

        :param security_group_ids: One or more security groups used to control access from streaming instances to your VPC. *Pattern* : ``^[\\w+\\-]+$``
        :param subnet_ids: The subnets in which network interfaces are created to connect streaming instances to your VPC. At least two of these subnets must be in different availability zones. *Pattern* : ``^subnet-([0-9a-f]{8}|[0-9a-f]{17})$``
        :param vpc_id: The VPC that streaming instances will connect to. *Pattern* : ``^vpc-[0-9a-z]*$``
        :param tags: The tags to add to the network settings resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_network_settings_props = workspacesweb.CfnNetworkSettingsProps(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"],
                vpc_id="vpcId",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a17459072d5b9aee15fcf087fb12a82a751a074de0d02647ae22fed9a82fb2cb)
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "security_group_ids": security_group_ids,
            "subnet_ids": subnet_ids,
            "vpc_id": vpc_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''One or more security groups used to control access from streaming instances to your VPC.

        *Pattern* : ``^[\\w+\\-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''The subnets in which network interfaces are created to connect streaming instances to your VPC.

        At least two of these subnets must be in different availability zones.

        *Pattern* : ``^subnet-([0-9a-f]{8}|[0-9a-f]{17})$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The VPC that streaming instances will connect to.

        *Pattern* : ``^vpc-[0-9a-z]*$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the network settings resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-networksettings.html#cfn-workspacesweb-networksettings-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnNetworkSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnPortal(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnPortal",
):
    '''This resource specifies a web portal, which users use to start browsing sessions.

    A ``Standard`` web portal can't start browsing sessions unless you have at defined and associated an ``IdentityProvider`` and ``NetworkSettings`` resource. An ``IAM Identity Center`` web portal does not require an ``IdentityProvider`` resource.

    For more information about web portals, see `What is Amazon WorkSpaces Web? <https://docs.aws.amazon.com/workspaces-web/latest/adminguide/what-is-workspaces-web.html.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html
    :cloudformationResource: AWS::WorkSpacesWeb::Portal
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_portal = workspacesweb.CfnPortal(self, "MyCfnPortal",
            additional_encryption_context={
                "additional_encryption_context_key": "additionalEncryptionContext"
            },
            authentication_type="authenticationType",
            browser_settings_arn="browserSettingsArn",
            customer_managed_key="customerManagedKey",
            display_name="displayName",
            instance_type="instanceType",
            ip_access_settings_arn="ipAccessSettingsArn",
            max_concurrent_sessions=123,
            network_settings_arn="networkSettingsArn",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            trust_store_arn="trustStoreArn",
            user_access_logging_settings_arn="userAccessLoggingSettingsArn",
            user_settings_arn="userSettingsArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        authentication_type: typing.Optional[builtins.str] = None,
        browser_settings_arn: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ip_access_settings_arn: typing.Optional[builtins.str] = None,
        max_concurrent_sessions: typing.Optional[jsii.Number] = None,
        network_settings_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trust_store_arn: typing.Optional[builtins.str] = None,
        user_access_logging_settings_arn: typing.Optional[builtins.str] = None,
        user_settings_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param additional_encryption_context: The additional encryption context of the portal.
        :param authentication_type: The type of authentication integration points used when signing into the web portal. Defaults to ``Standard`` . ``Standard`` web portals are authenticated directly through your identity provider (IdP). User and group access to your web portal is controlled through your IdP. You need to include an IdP resource in your template to integrate your IdP with your web portal. Completing the configuration for your IdP requires exchanging WorkSpaces Web’s SP metadata with your IdP’s IdP metadata. If your IdP requires the SP metadata first before returning the IdP metadata, you should follow these steps: 1. Create and deploy a CloudFormation template with a ``Standard`` portal with no ``IdentityProvider`` resource. 2. Retrieve the SP metadata using ``Fn:GetAtt`` , the WorkSpaces Web console, or by the calling the ``GetPortalServiceProviderMetadata`` API. 3. Submit the data to your IdP. 4. Add an ``IdentityProvider`` resource to your CloudFormation template. ``IAM Identity Center`` web portals are authenticated through AWS IAM Identity Center . They provide additional features, such as IdP-initiated authentication. Identity sources (including external identity provider integration) and other identity provider information must be configured in IAM Identity Center . User and group assignment must be done through the WorkSpaces Web console. These cannot be configured in CloudFormation.
        :param browser_settings_arn: The ARN of the browser settings that is associated with this web portal.
        :param customer_managed_key: The customer managed key of the web portal. *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``
        :param display_name: The name of the web portal.
        :param instance_type: The type and resources of the underlying instance.
        :param ip_access_settings_arn: The ARN of the IP access settings that is associated with the web portal.
        :param max_concurrent_sessions: The maximum number of concurrent sessions for the portal.
        :param network_settings_arn: The ARN of the network settings that is associated with the web portal.
        :param tags: The tags to add to the web portal. A tag is a key-value pair.
        :param trust_store_arn: The ARN of the trust store that is associated with the web portal.
        :param user_access_logging_settings_arn: The ARN of the user access logging settings that is associated with the web portal.
        :param user_settings_arn: The ARN of the user settings that is associated with the web portal.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__239c61bc87a1a693f01a28198d2d3000f7ef790e9684279e807a890b0beba6f5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPortalProps(
            additional_encryption_context=additional_encryption_context,
            authentication_type=authentication_type,
            browser_settings_arn=browser_settings_arn,
            customer_managed_key=customer_managed_key,
            display_name=display_name,
            instance_type=instance_type,
            ip_access_settings_arn=ip_access_settings_arn,
            max_concurrent_sessions=max_concurrent_sessions,
            network_settings_arn=network_settings_arn,
            tags=tags,
            trust_store_arn=trust_store_arn,
            user_access_logging_settings_arn=user_access_logging_settings_arn,
            user_settings_arn=user_settings_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c60cd0cfa36720b34c125e3c88b5da82ebb6f29c673cdccf4de8f3e9c20d4191)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5081fb673d60a8535462986536cbc12cbdb7c5238378c64aaee6592cb850e9f5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBrowserType")
    def attr_browser_type(self) -> builtins.str:
        '''The browser that users see when using a streaming session.

        :cloudformationAttribute: BrowserType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBrowserType"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationDate")
    def attr_creation_date(self) -> builtins.str:
        '''The creation date of the web portal.

        :cloudformationAttribute: CreationDate
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreationDate"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalArn")
    def attr_portal_arn(self) -> builtins.str:
        '''The ARN of the web portal.

        :cloudformationAttribute: PortalArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalEndpoint")
    def attr_portal_endpoint(self) -> builtins.str:
        '''The endpoint URL of the web portal that users access in order to start streaming sessions.

        :cloudformationAttribute: PortalEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrPortalStatus")
    def attr_portal_status(self) -> builtins.str:
        '''The status of the web portal.

        :cloudformationAttribute: PortalStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPortalStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrRendererType")
    def attr_renderer_type(self) -> builtins.str:
        '''The renderer that is used in streaming sessions.

        :cloudformationAttribute: RendererType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRendererType"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceProviderSamlMetadata")
    def attr_service_provider_saml_metadata(self) -> builtins.str:
        '''The SAML metadata of the service provider.

        :cloudformationAttribute: ServiceProviderSamlMetadata
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceProviderSamlMetadata"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''A message that explains why the web portal is in its current status.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

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
    @jsii.member(jsii_name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The additional encryption context of the portal.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "additionalEncryptionContext"))

    @additional_encryption_context.setter
    def additional_encryption_context(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e96df37d1cd0e854d8d279f26233ce4f30ad6bd4d9de076905b0443b8c425f03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalEncryptionContext", value)

    @builtins.property
    @jsii.member(jsii_name="authenticationType")
    def authentication_type(self) -> typing.Optional[builtins.str]:
        '''The type of authentication integration points used when signing into the web portal.

        Defaults to ``Standard`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authenticationType"))

    @authentication_type.setter
    def authentication_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dff3b0f7b3f0ee0596a800c3994102823f6531aeb797b09198a5a79ed8d25e0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authenticationType", value)

    @builtins.property
    @jsii.member(jsii_name="browserSettingsArn")
    def browser_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the browser settings that is associated with this web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "browserSettingsArn"))

    @browser_settings_arn.setter
    def browser_settings_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__393d4ac20d540d6ed107a37a5f0ced856767591929eb053c3784984567584127)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "browserSettingsArn", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The customer managed key of the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKey"))

    @customer_managed_key.setter
    def customer_managed_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__319e821fe7e2a17153f7832a389ae0c48e1f0517453d29fa3e26fa73232a46bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKey", value)

    @builtins.property
    @jsii.member(jsii_name="displayName")
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The name of the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "displayName"))

    @display_name.setter
    def display_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd1b9794e835c2ffeb3dc42a40224afa89d92cb7704c5a59dd75c1d3dd4ef495)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "displayName", value)

    @builtins.property
    @jsii.member(jsii_name="instanceType")
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''The type and resources of the underlying instance.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "instanceType"))

    @instance_type.setter
    def instance_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2707a9d7f008c455546b27a146dac5ed1d57c34aff9249e7561ee09fdc92f357)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "instanceType", value)

    @builtins.property
    @jsii.member(jsii_name="ipAccessSettingsArn")
    def ip_access_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IP access settings that is associated with the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ipAccessSettingsArn"))

    @ip_access_settings_arn.setter
    def ip_access_settings_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40134000fc007f2c29ea771d442eb2b959d8d3cccfedc0efa83e152c13cf3bda)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ipAccessSettingsArn", value)

    @builtins.property
    @jsii.member(jsii_name="maxConcurrentSessions")
    def max_concurrent_sessions(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of concurrent sessions for the portal.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxConcurrentSessions"))

    @max_concurrent_sessions.setter
    def max_concurrent_sessions(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5dad94379f446f44b9f9dfc0281e9cf4564c37b144b841df727ed7e762cb1a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxConcurrentSessions", value)

    @builtins.property
    @jsii.member(jsii_name="networkSettingsArn")
    def network_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the network settings that is associated with the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "networkSettingsArn"))

    @network_settings_arn.setter
    def network_settings_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beaa575cd54d9de94a0201b4213524db5df052dd0b9e1605b88d4487f6acbbcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSettingsArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the web portal.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__30535a8dcd75eba19481865deda3eac2505afe537e0650db0a95162feb2563e2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="trustStoreArn")
    def trust_store_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the trust store that is associated with the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "trustStoreArn"))

    @trust_store_arn.setter
    def trust_store_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__839ba627519ce26d936d0b859d31cf9abe67bf78df232cea362df9240c350edd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trustStoreArn", value)

    @builtins.property
    @jsii.member(jsii_name="userAccessLoggingSettingsArn")
    def user_access_logging_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the user access logging settings that is associated with the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userAccessLoggingSettingsArn"))

    @user_access_logging_settings_arn.setter
    def user_access_logging_settings_arn(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__225a01b45ee800a55ed118589c7eb5a4961d42af39924c022ca704030557cf15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userAccessLoggingSettingsArn", value)

    @builtins.property
    @jsii.member(jsii_name="userSettingsArn")
    def user_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the user settings that is associated with the web portal.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "userSettingsArn"))

    @user_settings_arn.setter
    def user_settings_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3c9a5aba1f82c8cb8d06dba7c424aabe0b4a862dd045ea1515145403fc27767)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "userSettingsArn", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnPortalProps",
    jsii_struct_bases=[],
    name_mapping={
        "additional_encryption_context": "additionalEncryptionContext",
        "authentication_type": "authenticationType",
        "browser_settings_arn": "browserSettingsArn",
        "customer_managed_key": "customerManagedKey",
        "display_name": "displayName",
        "instance_type": "instanceType",
        "ip_access_settings_arn": "ipAccessSettingsArn",
        "max_concurrent_sessions": "maxConcurrentSessions",
        "network_settings_arn": "networkSettingsArn",
        "tags": "tags",
        "trust_store_arn": "trustStoreArn",
        "user_access_logging_settings_arn": "userAccessLoggingSettingsArn",
        "user_settings_arn": "userSettingsArn",
    },
)
class CfnPortalProps:
    def __init__(
        self,
        *,
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        authentication_type: typing.Optional[builtins.str] = None,
        browser_settings_arn: typing.Optional[builtins.str] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        display_name: typing.Optional[builtins.str] = None,
        instance_type: typing.Optional[builtins.str] = None,
        ip_access_settings_arn: typing.Optional[builtins.str] = None,
        max_concurrent_sessions: typing.Optional[jsii.Number] = None,
        network_settings_arn: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        trust_store_arn: typing.Optional[builtins.str] = None,
        user_access_logging_settings_arn: typing.Optional[builtins.str] = None,
        user_settings_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPortal``.

        :param additional_encryption_context: The additional encryption context of the portal.
        :param authentication_type: The type of authentication integration points used when signing into the web portal. Defaults to ``Standard`` . ``Standard`` web portals are authenticated directly through your identity provider (IdP). User and group access to your web portal is controlled through your IdP. You need to include an IdP resource in your template to integrate your IdP with your web portal. Completing the configuration for your IdP requires exchanging WorkSpaces Web’s SP metadata with your IdP’s IdP metadata. If your IdP requires the SP metadata first before returning the IdP metadata, you should follow these steps: 1. Create and deploy a CloudFormation template with a ``Standard`` portal with no ``IdentityProvider`` resource. 2. Retrieve the SP metadata using ``Fn:GetAtt`` , the WorkSpaces Web console, or by the calling the ``GetPortalServiceProviderMetadata`` API. 3. Submit the data to your IdP. 4. Add an ``IdentityProvider`` resource to your CloudFormation template. ``IAM Identity Center`` web portals are authenticated through AWS IAM Identity Center . They provide additional features, such as IdP-initiated authentication. Identity sources (including external identity provider integration) and other identity provider information must be configured in IAM Identity Center . User and group assignment must be done through the WorkSpaces Web console. These cannot be configured in CloudFormation.
        :param browser_settings_arn: The ARN of the browser settings that is associated with this web portal.
        :param customer_managed_key: The customer managed key of the web portal. *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``
        :param display_name: The name of the web portal.
        :param instance_type: The type and resources of the underlying instance.
        :param ip_access_settings_arn: The ARN of the IP access settings that is associated with the web portal.
        :param max_concurrent_sessions: The maximum number of concurrent sessions for the portal.
        :param network_settings_arn: The ARN of the network settings that is associated with the web portal.
        :param tags: The tags to add to the web portal. A tag is a key-value pair.
        :param trust_store_arn: The ARN of the trust store that is associated with the web portal.
        :param user_access_logging_settings_arn: The ARN of the user access logging settings that is associated with the web portal.
        :param user_settings_arn: The ARN of the user settings that is associated with the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_portal_props = workspacesweb.CfnPortalProps(
                additional_encryption_context={
                    "additional_encryption_context_key": "additionalEncryptionContext"
                },
                authentication_type="authenticationType",
                browser_settings_arn="browserSettingsArn",
                customer_managed_key="customerManagedKey",
                display_name="displayName",
                instance_type="instanceType",
                ip_access_settings_arn="ipAccessSettingsArn",
                max_concurrent_sessions=123,
                network_settings_arn="networkSettingsArn",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                trust_store_arn="trustStoreArn",
                user_access_logging_settings_arn="userAccessLoggingSettingsArn",
                user_settings_arn="userSettingsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa147912cdfb0d9ea5356fccc59e7ae5b02c822d1e3f5ae2e4826ae39e89f283)
            check_type(argname="argument additional_encryption_context", value=additional_encryption_context, expected_type=type_hints["additional_encryption_context"])
            check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
            check_type(argname="argument browser_settings_arn", value=browser_settings_arn, expected_type=type_hints["browser_settings_arn"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
            check_type(argname="argument instance_type", value=instance_type, expected_type=type_hints["instance_type"])
            check_type(argname="argument ip_access_settings_arn", value=ip_access_settings_arn, expected_type=type_hints["ip_access_settings_arn"])
            check_type(argname="argument max_concurrent_sessions", value=max_concurrent_sessions, expected_type=type_hints["max_concurrent_sessions"])
            check_type(argname="argument network_settings_arn", value=network_settings_arn, expected_type=type_hints["network_settings_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument trust_store_arn", value=trust_store_arn, expected_type=type_hints["trust_store_arn"])
            check_type(argname="argument user_access_logging_settings_arn", value=user_access_logging_settings_arn, expected_type=type_hints["user_access_logging_settings_arn"])
            check_type(argname="argument user_settings_arn", value=user_settings_arn, expected_type=type_hints["user_settings_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if additional_encryption_context is not None:
            self._values["additional_encryption_context"] = additional_encryption_context
        if authentication_type is not None:
            self._values["authentication_type"] = authentication_type
        if browser_settings_arn is not None:
            self._values["browser_settings_arn"] = browser_settings_arn
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if display_name is not None:
            self._values["display_name"] = display_name
        if instance_type is not None:
            self._values["instance_type"] = instance_type
        if ip_access_settings_arn is not None:
            self._values["ip_access_settings_arn"] = ip_access_settings_arn
        if max_concurrent_sessions is not None:
            self._values["max_concurrent_sessions"] = max_concurrent_sessions
        if network_settings_arn is not None:
            self._values["network_settings_arn"] = network_settings_arn
        if tags is not None:
            self._values["tags"] = tags
        if trust_store_arn is not None:
            self._values["trust_store_arn"] = trust_store_arn
        if user_access_logging_settings_arn is not None:
            self._values["user_access_logging_settings_arn"] = user_access_logging_settings_arn
        if user_settings_arn is not None:
            self._values["user_settings_arn"] = user_settings_arn

    @builtins.property
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The additional encryption context of the portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-additionalencryptioncontext
        '''
        result = self._values.get("additional_encryption_context")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def authentication_type(self) -> typing.Optional[builtins.str]:
        '''The type of authentication integration points used when signing into the web portal. Defaults to ``Standard`` .

        ``Standard`` web portals are authenticated directly through your identity provider (IdP). User and group access to your web portal is controlled through your IdP. You need to include an IdP resource in your template to integrate your IdP with your web portal. Completing the configuration for your IdP requires exchanging WorkSpaces Web’s SP metadata with your IdP’s IdP metadata. If your IdP requires the SP metadata first before returning the IdP metadata, you should follow these steps:

        1. Create and deploy a CloudFormation template with a ``Standard`` portal with no ``IdentityProvider`` resource.
        2. Retrieve the SP metadata using ``Fn:GetAtt`` , the WorkSpaces Web console, or by the calling the ``GetPortalServiceProviderMetadata`` API.
        3. Submit the data to your IdP.
        4. Add an ``IdentityProvider`` resource to your CloudFormation template.

        ``IAM Identity Center`` web portals are authenticated through AWS IAM Identity Center . They provide additional features, such as IdP-initiated authentication. Identity sources (including external identity provider integration) and other identity provider information must be configured in IAM Identity Center . User and group assignment must be done through the WorkSpaces Web console. These cannot be configured in CloudFormation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-authenticationtype
        '''
        result = self._values.get("authentication_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def browser_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the browser settings that is associated with this web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-browsersettingsarn
        '''
        result = self._values.get("browser_settings_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The customer managed key of the web portal.

        *Pattern* : ``^arn:[\\w+=\\/,.@-]+:kms:[a-zA-Z0-9\\-]*:[a-zA-Z0-9]{1,12}:key\\/[a-zA-Z0-9-]+$``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-customermanagedkey
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def display_name(self) -> typing.Optional[builtins.str]:
        '''The name of the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-displayname
        '''
        result = self._values.get("display_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def instance_type(self) -> typing.Optional[builtins.str]:
        '''The type and resources of the underlying instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-instancetype
        '''
        result = self._values.get("instance_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ip_access_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the IP access settings that is associated with the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-ipaccesssettingsarn
        '''
        result = self._values.get("ip_access_settings_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_concurrent_sessions(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of concurrent sessions for the portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-maxconcurrentsessions
        '''
        result = self._values.get("max_concurrent_sessions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def network_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the network settings that is associated with the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-networksettingsarn
        '''
        result = self._values.get("network_settings_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the web portal.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def trust_store_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the trust store that is associated with the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-truststorearn
        '''
        result = self._values.get("trust_store_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_access_logging_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the user access logging settings that is associated with the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-useraccessloggingsettingsarn
        '''
        result = self._values.get("user_access_logging_settings_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def user_settings_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the user settings that is associated with the web portal.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-portal.html#cfn-workspacesweb-portal-usersettingsarn
        '''
        result = self._values.get("user_settings_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPortalProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnTrustStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnTrustStore",
):
    '''This resource specifies a trust store that can be associated with a web portal.

    A trust store contains certificate authority (CA) certificates. Once associated with a web portal, the browser in a streaming session will recognize certificates that have been issued using any of the CAs in the trust store. If your organization has internal websites that use certificates issued by private CAs, you should add the private CA certificate to the trust store.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html
    :cloudformationResource: AWS::WorkSpacesWeb::TrustStore
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_trust_store = workspacesweb.CfnTrustStore(self, "MyCfnTrustStore",
            certificate_list=["certificateList"],
        
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
        certificate_list: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param certificate_list: A list of CA certificates to be added to the trust store.
        :param tags: The tags to add to the trust store. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9c8ead0938c5ad416a02ff1511be2c3cbf2519166e43c80e65e581fac2cab7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTrustStoreProps(certificate_list=certificate_list, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5fb3d54892745fdc13234075ce86bd3f8d4acfe9ec88a393309766bcf833012b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__836cb2ee4e300cb4cb603faf540c0c6dad36379e65dad6d178875cdc39e56603)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPortalArns")
    def attr_associated_portal_arns(self) -> typing.List[builtins.str]:
        '''A list of web portal ARNs that this trust store is associated with.

        :cloudformationAttribute: AssociatedPortalArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAssociatedPortalArns"))

    @builtins.property
    @jsii.member(jsii_name="attrTrustStoreArn")
    def attr_trust_store_arn(self) -> builtins.str:
        '''The ARN of the trust store.

        :cloudformationAttribute: TrustStoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTrustStoreArn"))

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
    @jsii.member(jsii_name="certificateList")
    def certificate_list(self) -> typing.List[builtins.str]:
        '''A list of CA certificates to be added to the trust store.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "certificateList"))

    @certificate_list.setter
    def certificate_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6c348f8d89e15637f5e7f299791ad808bd6fadfe67032f77e095b03cb3b19f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateList", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the trust store.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__413cb334bb35253edc995584173eeea4b9dcaddccf8f42db23cff1eb1c57eba2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnTrustStoreProps",
    jsii_struct_bases=[],
    name_mapping={"certificate_list": "certificateList", "tags": "tags"},
)
class CfnTrustStoreProps:
    def __init__(
        self,
        *,
        certificate_list: typing.Sequence[builtins.str],
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTrustStore``.

        :param certificate_list: A list of CA certificates to be added to the trust store.
        :param tags: The tags to add to the trust store. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_trust_store_props = workspacesweb.CfnTrustStoreProps(
                certificate_list=["certificateList"],
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f61f2140f6607d292f5333bbaa4cf73f35e92dd28f8d49fc35bdca25eb8fa18)
            check_type(argname="argument certificate_list", value=certificate_list, expected_type=type_hints["certificate_list"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_list": certificate_list,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def certificate_list(self) -> typing.List[builtins.str]:
        '''A list of CA certificates to be added to the trust store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html#cfn-workspacesweb-truststore-certificatelist
        '''
        result = self._values.get("certificate_list")
        assert result is not None, "Required property 'certificate_list' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the trust store.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-truststore.html#cfn-workspacesweb-truststore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTrustStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnUserAccessLoggingSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnUserAccessLoggingSettings",
):
    '''This resource specifies user access logging settings that can be associated with a web portal.

    In order to receive logs from WorkSpaces Web, you must have an Amazon Kinesis Data Stream that starts with "amazon-workspaces-web-*". Your Amazon Kinesis data stream must either have server-side encryption turned off, or must use AWS managed keys for server-side encryption.

    For more information about setting server-side encryption in Amazon Kinesis , see `How Do I Get Started with Server-Side Encryption? <https://docs.aws.amazon.com/streams/latest/dev/getting-started-with-sse.html>`_ .

    For more information about setting up user access logging, see `Set up user access logging <https://docs.aws.amazon.com/workspaces-web/latest/adminguide/user-logging.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html
    :cloudformationResource: AWS::WorkSpacesWeb::UserAccessLoggingSettings
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_user_access_logging_settings = workspacesweb.CfnUserAccessLoggingSettings(self, "MyCfnUserAccessLoggingSettings",
            kinesis_stream_arn="kinesisStreamArn",
        
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
        kinesis_stream_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param kinesis_stream_arn: The ARN of the Kinesis stream.
        :param tags: The tags to add to the user access logging settings resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aad2c57d166d3f137cf451bac17a21ea9bd59a5dafc004c63b60db12312c6ea6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserAccessLoggingSettingsProps(
            kinesis_stream_arn=kinesis_stream_arn, tags=tags
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9529f157bb0a06f8719fcc35be65d3271950825bff8e93dc8a42d103439e05ac)
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
            type_hints = typing.get_type_hints(_typecheckingstub__696773979e88a009f291e28c35e0a9e8ca5f167e930af7cd1cdfeedbab8c2264)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPortalArns")
    def attr_associated_portal_arns(self) -> typing.List[builtins.str]:
        '''A list of web portal ARNs that this user access logging settings is associated with.

        :cloudformationAttribute: AssociatedPortalArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAssociatedPortalArns"))

    @builtins.property
    @jsii.member(jsii_name="attrUserAccessLoggingSettingsArn")
    def attr_user_access_logging_settings_arn(self) -> builtins.str:
        '''The ARN of the user access logging settings.

        :cloudformationAttribute: UserAccessLoggingSettingsArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserAccessLoggingSettingsArn"))

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
    @jsii.member(jsii_name="kinesisStreamArn")
    def kinesis_stream_arn(self) -> builtins.str:
        '''The ARN of the Kinesis stream.'''
        return typing.cast(builtins.str, jsii.get(self, "kinesisStreamArn"))

    @kinesis_stream_arn.setter
    def kinesis_stream_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c9da0f05e734af1b537d4f6612a6e7f940d1c43dfc9bbc4879e3d92578ed0614)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kinesisStreamArn", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the user access logging settings resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5891d11f0a657ca8579858eed7e0c8861e02aad2584f2928aa6f75f7966d4830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnUserAccessLoggingSettingsProps",
    jsii_struct_bases=[],
    name_mapping={"kinesis_stream_arn": "kinesisStreamArn", "tags": "tags"},
)
class CfnUserAccessLoggingSettingsProps:
    def __init__(
        self,
        *,
        kinesis_stream_arn: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserAccessLoggingSettings``.

        :param kinesis_stream_arn: The ARN of the Kinesis stream.
        :param tags: The tags to add to the user access logging settings resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_user_access_logging_settings_props = workspacesweb.CfnUserAccessLoggingSettingsProps(
                kinesis_stream_arn="kinesisStreamArn",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fbbe0ac8cc8b93ca9250852f294b49e6126c8e1f9bcbdc057c5f6fbfcc7115a)
            check_type(argname="argument kinesis_stream_arn", value=kinesis_stream_arn, expected_type=type_hints["kinesis_stream_arn"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kinesis_stream_arn": kinesis_stream_arn,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def kinesis_stream_arn(self) -> builtins.str:
        '''The ARN of the Kinesis stream.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html#cfn-workspacesweb-useraccessloggingsettings-kinesisstreamarn
        '''
        result = self._values.get("kinesis_stream_arn")
        assert result is not None, "Required property 'kinesis_stream_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the user access logging settings resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-useraccessloggingsettings.html#cfn-workspacesweb-useraccessloggingsettings-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserAccessLoggingSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnUserSettings(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnUserSettings",
):
    '''This resource specifies user settings that can be associated with a web portal.

    Once associated with a web portal, user settings control how users can transfer data between a streaming session and the their local devices.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html
    :cloudformationResource: AWS::WorkSpacesWeb::UserSettings
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_workspacesweb as workspacesweb
        
        cfn_user_settings = workspacesweb.CfnUserSettings(self, "MyCfnUserSettings",
            copy_allowed="copyAllowed",
            download_allowed="downloadAllowed",
            paste_allowed="pasteAllowed",
            print_allowed="printAllowed",
            upload_allowed="uploadAllowed",
        
            # the properties below are optional
            additional_encryption_context={
                "additional_encryption_context_key": "additionalEncryptionContext"
            },
            cookie_synchronization_configuration=workspacesweb.CfnUserSettings.CookieSynchronizationConfigurationProperty(
                allowlist=[workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                    domain="domain",
        
                    # the properties below are optional
                    name="name",
                    path="path"
                )],
        
                # the properties below are optional
                blocklist=[workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                    domain="domain",
        
                    # the properties below are optional
                    name="name",
                    path="path"
                )]
            ),
            customer_managed_key="customerManagedKey",
            disconnect_timeout_in_minutes=123,
            idle_disconnect_timeout_in_minutes=123,
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
        copy_allowed: builtins.str,
        download_allowed: builtins.str,
        paste_allowed: builtins.str,
        print_allowed: builtins.str,
        upload_allowed: builtins.str,
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        cookie_synchronization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserSettings.CookieSynchronizationConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        idle_disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param copy_allowed: Specifies whether the user can copy text from the streaming session to the local device.
        :param download_allowed: Specifies whether the user can download files from the streaming session to the local device.
        :param paste_allowed: Specifies whether the user can paste text from the local device to the streaming session.
        :param print_allowed: Specifies whether the user can print to the local device.
        :param upload_allowed: Specifies whether the user can upload files from the local device to the streaming session.
        :param additional_encryption_context: The additional encryption context of the user settings.
        :param cookie_synchronization_configuration: The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.
        :param customer_managed_key: The customer managed key used to encrypt sensitive information in the user settings.
        :param disconnect_timeout_in_minutes: The amount of time that a streaming session remains active after users disconnect.
        :param idle_disconnect_timeout_in_minutes: The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.
        :param tags: The tags to add to the user settings resource. A tag is a key-value pair.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75a973eee52af75d8440f76e110a255d358bfa0d721a06403da3f4b3da691630)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnUserSettingsProps(
            copy_allowed=copy_allowed,
            download_allowed=download_allowed,
            paste_allowed=paste_allowed,
            print_allowed=print_allowed,
            upload_allowed=upload_allowed,
            additional_encryption_context=additional_encryption_context,
            cookie_synchronization_configuration=cookie_synchronization_configuration,
            customer_managed_key=customer_managed_key,
            disconnect_timeout_in_minutes=disconnect_timeout_in_minutes,
            idle_disconnect_timeout_in_minutes=idle_disconnect_timeout_in_minutes,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__244f1fe2bee12ec9da43df9e03b84c572087c943a751c03dfad95754868e16bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d19192b77523bcab841bc3482080fb0b612b4a9432071dcb0bdcee59129de93e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPortalArns")
    def attr_associated_portal_arns(self) -> typing.List[builtins.str]:
        '''A list of web portal ARNs that this user settings resource is associated with.

        :cloudformationAttribute: AssociatedPortalArns
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrAssociatedPortalArns"))

    @builtins.property
    @jsii.member(jsii_name="attrUserSettingsArn")
    def attr_user_settings_arn(self) -> builtins.str:
        '''The ARN of the user settings.

        :cloudformationAttribute: UserSettingsArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrUserSettingsArn"))

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
    @jsii.member(jsii_name="copyAllowed")
    def copy_allowed(self) -> builtins.str:
        '''Specifies whether the user can copy text from the streaming session to the local device.'''
        return typing.cast(builtins.str, jsii.get(self, "copyAllowed"))

    @copy_allowed.setter
    def copy_allowed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__246f5760229c3a961575cf587c3b4f4860166572ed6c563578054c49d5e3f491)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "copyAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="downloadAllowed")
    def download_allowed(self) -> builtins.str:
        '''Specifies whether the user can download files from the streaming session to the local device.'''
        return typing.cast(builtins.str, jsii.get(self, "downloadAllowed"))

    @download_allowed.setter
    def download_allowed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f9bc1f80036b3272572fd6a61db383c0f9a108ae4361245d67c2310033f6aca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "downloadAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="pasteAllowed")
    def paste_allowed(self) -> builtins.str:
        '''Specifies whether the user can paste text from the local device to the streaming session.'''
        return typing.cast(builtins.str, jsii.get(self, "pasteAllowed"))

    @paste_allowed.setter
    def paste_allowed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b079c9f6c24d953ad04e32e9f5a560c7a3b8dfdcbd3fa9b20983ed520609684a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pasteAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="printAllowed")
    def print_allowed(self) -> builtins.str:
        '''Specifies whether the user can print to the local device.'''
        return typing.cast(builtins.str, jsii.get(self, "printAllowed"))

    @print_allowed.setter
    def print_allowed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc2a40c59165855fc23939973d9bb8df39156dfc828b8f1c2c799acc9e9c534b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "printAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="uploadAllowed")
    def upload_allowed(self) -> builtins.str:
        '''Specifies whether the user can upload files from the local device to the streaming session.'''
        return typing.cast(builtins.str, jsii.get(self, "uploadAllowed"))

    @upload_allowed.setter
    def upload_allowed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab95c6b32fc019924a90410af98fcff3bd60af47435e3704bf57b385408f198c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uploadAllowed", value)

    @builtins.property
    @jsii.member(jsii_name="additionalEncryptionContext")
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The additional encryption context of the user settings.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "additionalEncryptionContext"))

    @additional_encryption_context.setter
    def additional_encryption_context(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fca2cad6e9c549a52ed27d6e7203a4dde55fdf1eed387d37637b922c0743a318)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "additionalEncryptionContext", value)

    @builtins.property
    @jsii.member(jsii_name="cookieSynchronizationConfiguration")
    def cookie_synchronization_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSynchronizationConfigurationProperty"]]:
        '''The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSynchronizationConfigurationProperty"]], jsii.get(self, "cookieSynchronizationConfiguration"))

    @cookie_synchronization_configuration.setter
    def cookie_synchronization_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSynchronizationConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc519f4ed3ec11d3fe8c755f39fd066c05ebbf23ec90ba109c399972617b76b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cookieSynchronizationConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="customerManagedKey")
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The customer managed key used to encrypt sensitive information in the user settings.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "customerManagedKey"))

    @customer_managed_key.setter
    def customer_managed_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33cbfd7d3c9ffee2a9508bf9733029fbcbc3bd298fd568503ef46ec94dde23df)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customerManagedKey", value)

    @builtins.property
    @jsii.member(jsii_name="disconnectTimeoutInMinutes")
    def disconnect_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that a streaming session remains active after users disconnect.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "disconnectTimeoutInMinutes"))

    @disconnect_timeout_in_minutes.setter
    def disconnect_timeout_in_minutes(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65c3d8570299b47cbfe2eac0be79eb57ec6ded28c76cb13fec1237f2daa26542)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disconnectTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="idleDisconnectTimeoutInMinutes")
    def idle_disconnect_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "idleDisconnectTimeoutInMinutes"))

    @idle_disconnect_timeout_in_minutes.setter
    def idle_disconnect_timeout_in_minutes(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e6ab43a1a32df42c47c0c8bf18b29db28c2b3d27d8be082f9408d80c09059346)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "idleDisconnectTimeoutInMinutes", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the user settings resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e18af2707e3cbec353505ab884854a52028ac4039d4d38b2b7aff300b7e63b8a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesweb.CfnUserSettings.CookieSpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"domain": "domain", "name": "name", "path": "path"},
    )
    class CookieSpecificationProperty:
        def __init__(
            self,
            *,
            domain: builtins.str,
            name: typing.Optional[builtins.str] = None,
            path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies a single cookie or set of cookies in an end user's browser.

            :param domain: The domain of the cookie.
            :param name: The name of the cookie.
            :param path: The path of the cookie.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesweb as workspacesweb
                
                cookie_specification_property = workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                    domain="domain",
                
                    # the properties below are optional
                    name="name",
                    path="path"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__967130a98f5e1732af04891ba925fd71a0043477b770e4d98d817b932c896a45)
                check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "domain": domain,
            }
            if name is not None:
                self._values["name"] = name
            if path is not None:
                self._values["path"] = path

        @builtins.property
        def domain(self) -> builtins.str:
            '''The domain of the cookie.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html#cfn-workspacesweb-usersettings-cookiespecification-domain
            '''
            result = self._values.get("domain")
            assert result is not None, "Required property 'domain' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the cookie.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html#cfn-workspacesweb-usersettings-cookiespecification-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''The path of the cookie.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiespecification.html#cfn-workspacesweb-usersettings-cookiespecification-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CookieSpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_workspacesweb.CfnUserSettings.CookieSynchronizationConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"allowlist": "allowlist", "blocklist": "blocklist"},
    )
    class CookieSynchronizationConfigurationProperty:
        def __init__(
            self,
            *,
            allowlist: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserSettings.CookieSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            blocklist: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnUserSettings.CookieSpecificationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.

            :param allowlist: The list of cookie specifications that are allowed to be synchronized to the remote browser.
            :param blocklist: The list of cookie specifications that are blocked from being synchronized to the remote browser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_workspacesweb as workspacesweb
                
                cookie_synchronization_configuration_property = workspacesweb.CfnUserSettings.CookieSynchronizationConfigurationProperty(
                    allowlist=[workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                        domain="domain",
                
                        # the properties below are optional
                        name="name",
                        path="path"
                    )],
                
                    # the properties below are optional
                    blocklist=[workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                        domain="domain",
                
                        # the properties below are optional
                        name="name",
                        path="path"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b03a784924e11f4debd206efd14cca98aa8e8242e4e834629b834539bd06258f)
                check_type(argname="argument allowlist", value=allowlist, expected_type=type_hints["allowlist"])
                check_type(argname="argument blocklist", value=blocklist, expected_type=type_hints["blocklist"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allowlist": allowlist,
            }
            if blocklist is not None:
                self._values["blocklist"] = blocklist

        @builtins.property
        def allowlist(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSpecificationProperty"]]]:
            '''The list of cookie specifications that are allowed to be synchronized to the remote browser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-allowlist
            '''
            result = self._values.get("allowlist")
            assert result is not None, "Required property 'allowlist' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSpecificationProperty"]]], result)

        @builtins.property
        def blocklist(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSpecificationProperty"]]]]:
            '''The list of cookie specifications that are blocked from being synchronized to the remote browser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-workspacesweb-usersettings-cookiesynchronizationconfiguration.html#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration-blocklist
            '''
            result = self._values.get("blocklist")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnUserSettings.CookieSpecificationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CookieSynchronizationConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_workspacesweb.CfnUserSettingsProps",
    jsii_struct_bases=[],
    name_mapping={
        "copy_allowed": "copyAllowed",
        "download_allowed": "downloadAllowed",
        "paste_allowed": "pasteAllowed",
        "print_allowed": "printAllowed",
        "upload_allowed": "uploadAllowed",
        "additional_encryption_context": "additionalEncryptionContext",
        "cookie_synchronization_configuration": "cookieSynchronizationConfiguration",
        "customer_managed_key": "customerManagedKey",
        "disconnect_timeout_in_minutes": "disconnectTimeoutInMinutes",
        "idle_disconnect_timeout_in_minutes": "idleDisconnectTimeoutInMinutes",
        "tags": "tags",
    },
)
class CfnUserSettingsProps:
    def __init__(
        self,
        *,
        copy_allowed: builtins.str,
        download_allowed: builtins.str,
        paste_allowed: builtins.str,
        print_allowed: builtins.str,
        upload_allowed: builtins.str,
        additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        cookie_synchronization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserSettings.CookieSynchronizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        customer_managed_key: typing.Optional[builtins.str] = None,
        disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        idle_disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnUserSettings``.

        :param copy_allowed: Specifies whether the user can copy text from the streaming session to the local device.
        :param download_allowed: Specifies whether the user can download files from the streaming session to the local device.
        :param paste_allowed: Specifies whether the user can paste text from the local device to the streaming session.
        :param print_allowed: Specifies whether the user can print to the local device.
        :param upload_allowed: Specifies whether the user can upload files from the local device to the streaming session.
        :param additional_encryption_context: The additional encryption context of the user settings.
        :param cookie_synchronization_configuration: The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.
        :param customer_managed_key: The customer managed key used to encrypt sensitive information in the user settings.
        :param disconnect_timeout_in_minutes: The amount of time that a streaming session remains active after users disconnect.
        :param idle_disconnect_timeout_in_minutes: The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.
        :param tags: The tags to add to the user settings resource. A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_workspacesweb as workspacesweb
            
            cfn_user_settings_props = workspacesweb.CfnUserSettingsProps(
                copy_allowed="copyAllowed",
                download_allowed="downloadAllowed",
                paste_allowed="pasteAllowed",
                print_allowed="printAllowed",
                upload_allowed="uploadAllowed",
            
                # the properties below are optional
                additional_encryption_context={
                    "additional_encryption_context_key": "additionalEncryptionContext"
                },
                cookie_synchronization_configuration=workspacesweb.CfnUserSettings.CookieSynchronizationConfigurationProperty(
                    allowlist=[workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                        domain="domain",
            
                        # the properties below are optional
                        name="name",
                        path="path"
                    )],
            
                    # the properties below are optional
                    blocklist=[workspacesweb.CfnUserSettings.CookieSpecificationProperty(
                        domain="domain",
            
                        # the properties below are optional
                        name="name",
                        path="path"
                    )]
                ),
                customer_managed_key="customerManagedKey",
                disconnect_timeout_in_minutes=123,
                idle_disconnect_timeout_in_minutes=123,
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5fdddc739ee6575c152d4edd4b1958f0aed7897d0804077cf3ed5b5829d55a4)
            check_type(argname="argument copy_allowed", value=copy_allowed, expected_type=type_hints["copy_allowed"])
            check_type(argname="argument download_allowed", value=download_allowed, expected_type=type_hints["download_allowed"])
            check_type(argname="argument paste_allowed", value=paste_allowed, expected_type=type_hints["paste_allowed"])
            check_type(argname="argument print_allowed", value=print_allowed, expected_type=type_hints["print_allowed"])
            check_type(argname="argument upload_allowed", value=upload_allowed, expected_type=type_hints["upload_allowed"])
            check_type(argname="argument additional_encryption_context", value=additional_encryption_context, expected_type=type_hints["additional_encryption_context"])
            check_type(argname="argument cookie_synchronization_configuration", value=cookie_synchronization_configuration, expected_type=type_hints["cookie_synchronization_configuration"])
            check_type(argname="argument customer_managed_key", value=customer_managed_key, expected_type=type_hints["customer_managed_key"])
            check_type(argname="argument disconnect_timeout_in_minutes", value=disconnect_timeout_in_minutes, expected_type=type_hints["disconnect_timeout_in_minutes"])
            check_type(argname="argument idle_disconnect_timeout_in_minutes", value=idle_disconnect_timeout_in_minutes, expected_type=type_hints["idle_disconnect_timeout_in_minutes"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "copy_allowed": copy_allowed,
            "download_allowed": download_allowed,
            "paste_allowed": paste_allowed,
            "print_allowed": print_allowed,
            "upload_allowed": upload_allowed,
        }
        if additional_encryption_context is not None:
            self._values["additional_encryption_context"] = additional_encryption_context
        if cookie_synchronization_configuration is not None:
            self._values["cookie_synchronization_configuration"] = cookie_synchronization_configuration
        if customer_managed_key is not None:
            self._values["customer_managed_key"] = customer_managed_key
        if disconnect_timeout_in_minutes is not None:
            self._values["disconnect_timeout_in_minutes"] = disconnect_timeout_in_minutes
        if idle_disconnect_timeout_in_minutes is not None:
            self._values["idle_disconnect_timeout_in_minutes"] = idle_disconnect_timeout_in_minutes
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def copy_allowed(self) -> builtins.str:
        '''Specifies whether the user can copy text from the streaming session to the local device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-copyallowed
        '''
        result = self._values.get("copy_allowed")
        assert result is not None, "Required property 'copy_allowed' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def download_allowed(self) -> builtins.str:
        '''Specifies whether the user can download files from the streaming session to the local device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-downloadallowed
        '''
        result = self._values.get("download_allowed")
        assert result is not None, "Required property 'download_allowed' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def paste_allowed(self) -> builtins.str:
        '''Specifies whether the user can paste text from the local device to the streaming session.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-pasteallowed
        '''
        result = self._values.get("paste_allowed")
        assert result is not None, "Required property 'paste_allowed' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def print_allowed(self) -> builtins.str:
        '''Specifies whether the user can print to the local device.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-printallowed
        '''
        result = self._values.get("print_allowed")
        assert result is not None, "Required property 'print_allowed' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def upload_allowed(self) -> builtins.str:
        '''Specifies whether the user can upload files from the local device to the streaming session.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-uploadallowed
        '''
        result = self._values.get("upload_allowed")
        assert result is not None, "Required property 'upload_allowed' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def additional_encryption_context(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''The additional encryption context of the user settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-additionalencryptioncontext
        '''
        result = self._values.get("additional_encryption_context")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def cookie_synchronization_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUserSettings.CookieSynchronizationConfigurationProperty]]:
        '''The configuration that specifies which cookies should be synchronized from the end user's local browser to the remote browser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-cookiesynchronizationconfiguration
        '''
        result = self._values.get("cookie_synchronization_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUserSettings.CookieSynchronizationConfigurationProperty]], result)

    @builtins.property
    def customer_managed_key(self) -> typing.Optional[builtins.str]:
        '''The customer managed key used to encrypt sensitive information in the user settings.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-customermanagedkey
        '''
        result = self._values.get("customer_managed_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disconnect_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that a streaming session remains active after users disconnect.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-disconnecttimeoutinminutes
        '''
        result = self._values.get("disconnect_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def idle_disconnect_timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''The amount of time that users can be idle (inactive) before they are disconnected from their streaming session and the disconnect timeout interval begins.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-idledisconnecttimeoutinminutes
        '''
        result = self._values.get("idle_disconnect_timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags to add to the user settings resource.

        A tag is a key-value pair.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-workspacesweb-usersettings.html#cfn-workspacesweb-usersettings-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnUserSettingsProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBrowserSettings",
    "CfnBrowserSettingsProps",
    "CfnIdentityProvider",
    "CfnIdentityProviderProps",
    "CfnIpAccessSettings",
    "CfnIpAccessSettingsProps",
    "CfnNetworkSettings",
    "CfnNetworkSettingsProps",
    "CfnPortal",
    "CfnPortalProps",
    "CfnTrustStore",
    "CfnTrustStoreProps",
    "CfnUserAccessLoggingSettings",
    "CfnUserAccessLoggingSettingsProps",
    "CfnUserSettings",
    "CfnUserSettingsProps",
]

publication.publish()

def _typecheckingstub__bddcc45afa30e005718c5da3d3034bff6b9c0453326851818da6294dc041bb0f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    browser_policy: typing.Optional[builtins.str] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d4203cdc61a30c217fc2abe263c4776ac7f7dc3efdc691f65b8b0f98c469206(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4cab7e5af66cb2aa7162f6b46ea25dc53695260ce84c6550f897b70bab862ee(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70de4dee5d14f114274fd7960c64b6accb0ec49e02c002b5521af87f035095c2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1ed58b3fc2a2966bf9a096153c9b38b0a594ab0c629bf8b97e6011a61ebfb79(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eed13ab23af9a957ff225aff9f958ae8f40efe7f9c0aa02be45034aa22a364c4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__488a7e6081f5fbb5bf5af995cdb747f920d592e19ef88a222e5aa2f1c21d8a53(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f99c227d497f6d51d01cc19398b94784835fab55afca7c6488466bb1cc1420b3(
    *,
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    browser_policy: typing.Optional[builtins.str] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__439cd32d129b1f0a69c13fb5a494170084be122497b619a7175debec51c3635e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity_provider_details: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    identity_provider_name: builtins.str,
    identity_provider_type: builtins.str,
    portal_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ace0da6a7e7e7a968ac58e8be1ce9dcb15a96bae8fad93e7c341ff5392bed56c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec876abe2e87a8e0cb2641e36f36bd29bb0a19b65cc2d8f6be54a630a22b3af8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ae08bcbb1d55c54b06801705e4c1effec06173b9d5c1ab7d0301258d84aa63a(
    value: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47d337423f7a1ca0a276c2a641c1f67e69f1933efe04994ab3be413955030b14(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72551994233ed9e106da8e5840c9077e96c1a7cafc63617736585c1eb83fd2da(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17f07edd6f61424250e1f5f7df6f6cee024beb494ee700c6419c5642ebe36e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc73238ea7aab35d7f7ec21a88a98c698e64b413b81129270666c830ae963a4d(
    *,
    identity_provider_details: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
    identity_provider_name: builtins.str,
    identity_provider_type: builtins.str,
    portal_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e3f00304b675ee88c29734b1fad40f8e448afe808a4226188c1c74e8ed82fe0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ip_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIpAccessSettings.IpRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__522d314ff55f65afebb67835c03df17342b3167bed24e30c591f5aef150973f0(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd4736646712efdcfa8ece881cd4fa733fb537f01432db179870ed0f95ff0512(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc300ade0369b0ab447aa7806a51ee2809fea6ffd0fffc0129fb173b7f3886cf(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnIpAccessSettings.IpRuleProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f120862dd3a18b3da3624f1bbb9a6b2ec04ea91c5a0d22f1306ab87a46a1e28(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__057facdda1fc071bcb0a19a16cf182f52ac2a874ba9674ab1e2f710144816eae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b724cabf90e359bbb06c7a32f43432bf7cb19a46eb5e9f240789471612d5b8b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98ac230b64daa6cce74b4ea14502d07e7a0dcc81bb5bd7c233a62ad5907f6083(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6ebcd54b862693c4f7d257e8db3f90e6315f91bc32c16e7865b2e93f91ff381(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ef91a56d003f837ee2a6f8431647b2dcdd5ff9d72afb0d6f7cb1c50cc1a6890(
    *,
    ip_range: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__332b0cacbcd242c5add5b067133a69e3ee9f775e64856bf6ae48c84e34d0b475(
    *,
    ip_rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIpAccessSettings.IpRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95a61d7b0b1452fb7a5fdde6d41bbab0a1737a4628bbe5a201c16ce50a3e8a67(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18b2266ad8a399dab2a39759ddd4f261e866f9af5f84bd2281d2d5717327fc7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e59ed5f61334e6922894c4c8b1588d6af1336b159abb632a02c51a1b16724fd0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3554fe26b5fd797fb5730682ce023c2460621ebeec517b2840620081484a64ab(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b27a5b7c5de5fd73e2955aa73ff7e658050d13d9e84df9804b230c062f75d81(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e298ee4542dc4160ff007ee478b4d24dff6a5105564e454a0eacb28ac7aeab52(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07819661df503a5395aeb2f48e629b4742564eaa4d650197b66c74bb51c0efc3(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a17459072d5b9aee15fcf087fb12a82a751a074de0d02647ae22fed9a82fb2cb(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
    vpc_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__239c61bc87a1a693f01a28198d2d3000f7ef790e9684279e807a890b0beba6f5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    authentication_type: typing.Optional[builtins.str] = None,
    browser_settings_arn: typing.Optional[builtins.str] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ip_access_settings_arn: typing.Optional[builtins.str] = None,
    max_concurrent_sessions: typing.Optional[jsii.Number] = None,
    network_settings_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trust_store_arn: typing.Optional[builtins.str] = None,
    user_access_logging_settings_arn: typing.Optional[builtins.str] = None,
    user_settings_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c60cd0cfa36720b34c125e3c88b5da82ebb6f29c673cdccf4de8f3e9c20d4191(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5081fb673d60a8535462986536cbc12cbdb7c5238378c64aaee6592cb850e9f5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e96df37d1cd0e854d8d279f26233ce4f30ad6bd4d9de076905b0443b8c425f03(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff3b0f7b3f0ee0596a800c3994102823f6531aeb797b09198a5a79ed8d25e0f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__393d4ac20d540d6ed107a37a5f0ced856767591929eb053c3784984567584127(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__319e821fe7e2a17153f7832a389ae0c48e1f0517453d29fa3e26fa73232a46bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd1b9794e835c2ffeb3dc42a40224afa89d92cb7704c5a59dd75c1d3dd4ef495(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2707a9d7f008c455546b27a146dac5ed1d57c34aff9249e7561ee09fdc92f357(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40134000fc007f2c29ea771d442eb2b959d8d3cccfedc0efa83e152c13cf3bda(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5dad94379f446f44b9f9dfc0281e9cf4564c37b144b841df727ed7e762cb1a19(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beaa575cd54d9de94a0201b4213524db5df052dd0b9e1605b88d4487f6acbbcd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30535a8dcd75eba19481865deda3eac2505afe537e0650db0a95162feb2563e2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__839ba627519ce26d936d0b859d31cf9abe67bf78df232cea362df9240c350edd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__225a01b45ee800a55ed118589c7eb5a4961d42af39924c022ca704030557cf15(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3c9a5aba1f82c8cb8d06dba7c424aabe0b4a862dd045ea1515145403fc27767(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa147912cdfb0d9ea5356fccc59e7ae5b02c822d1e3f5ae2e4826ae39e89f283(
    *,
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    authentication_type: typing.Optional[builtins.str] = None,
    browser_settings_arn: typing.Optional[builtins.str] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    display_name: typing.Optional[builtins.str] = None,
    instance_type: typing.Optional[builtins.str] = None,
    ip_access_settings_arn: typing.Optional[builtins.str] = None,
    max_concurrent_sessions: typing.Optional[jsii.Number] = None,
    network_settings_arn: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    trust_store_arn: typing.Optional[builtins.str] = None,
    user_access_logging_settings_arn: typing.Optional[builtins.str] = None,
    user_settings_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9c8ead0938c5ad416a02ff1511be2c3cbf2519166e43c80e65e581fac2cab7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_list: typing.Sequence[builtins.str],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5fb3d54892745fdc13234075ce86bd3f8d4acfe9ec88a393309766bcf833012b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__836cb2ee4e300cb4cb603faf540c0c6dad36379e65dad6d178875cdc39e56603(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6c348f8d89e15637f5e7f299791ad808bd6fadfe67032f77e095b03cb3b19f1(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__413cb334bb35253edc995584173eeea4b9dcaddccf8f42db23cff1eb1c57eba2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f61f2140f6607d292f5333bbaa4cf73f35e92dd28f8d49fc35bdca25eb8fa18(
    *,
    certificate_list: typing.Sequence[builtins.str],
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aad2c57d166d3f137cf451bac17a21ea9bd59a5dafc004c63b60db12312c6ea6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    kinesis_stream_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9529f157bb0a06f8719fcc35be65d3271950825bff8e93dc8a42d103439e05ac(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__696773979e88a009f291e28c35e0a9e8ca5f167e930af7cd1cdfeedbab8c2264(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9da0f05e734af1b537d4f6612a6e7f940d1c43dfc9bbc4879e3d92578ed0614(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5891d11f0a657ca8579858eed7e0c8861e02aad2584f2928aa6f75f7966d4830(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fbbe0ac8cc8b93ca9250852f294b49e6126c8e1f9bcbdc057c5f6fbfcc7115a(
    *,
    kinesis_stream_arn: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75a973eee52af75d8440f76e110a255d358bfa0d721a06403da3f4b3da691630(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    copy_allowed: builtins.str,
    download_allowed: builtins.str,
    paste_allowed: builtins.str,
    print_allowed: builtins.str,
    upload_allowed: builtins.str,
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    cookie_synchronization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserSettings.CookieSynchronizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    idle_disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__244f1fe2bee12ec9da43df9e03b84c572087c943a751c03dfad95754868e16bf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d19192b77523bcab841bc3482080fb0b612b4a9432071dcb0bdcee59129de93e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__246f5760229c3a961575cf587c3b4f4860166572ed6c563578054c49d5e3f491(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f9bc1f80036b3272572fd6a61db383c0f9a108ae4361245d67c2310033f6aca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b079c9f6c24d953ad04e32e9f5a560c7a3b8dfdcbd3fa9b20983ed520609684a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2a40c59165855fc23939973d9bb8df39156dfc828b8f1c2c799acc9e9c534b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab95c6b32fc019924a90410af98fcff3bd60af47435e3704bf57b385408f198c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fca2cad6e9c549a52ed27d6e7203a4dde55fdf1eed387d37637b922c0743a318(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc519f4ed3ec11d3fe8c755f39fd066c05ebbf23ec90ba109c399972617b76b4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnUserSettings.CookieSynchronizationConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33cbfd7d3c9ffee2a9508bf9733029fbcbc3bd298fd568503ef46ec94dde23df(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65c3d8570299b47cbfe2eac0be79eb57ec6ded28c76cb13fec1237f2daa26542(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6ab43a1a32df42c47c0c8bf18b29db28c2b3d27d8be082f9408d80c09059346(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e18af2707e3cbec353505ab884854a52028ac4039d4d38b2b7aff300b7e63b8a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__967130a98f5e1732af04891ba925fd71a0043477b770e4d98d817b932c896a45(
    *,
    domain: builtins.str,
    name: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b03a784924e11f4debd206efd14cca98aa8e8242e4e834629b834539bd06258f(
    *,
    allowlist: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserSettings.CookieSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    blocklist: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserSettings.CookieSpecificationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5fdddc739ee6575c152d4edd4b1958f0aed7897d0804077cf3ed5b5829d55a4(
    *,
    copy_allowed: builtins.str,
    download_allowed: builtins.str,
    paste_allowed: builtins.str,
    print_allowed: builtins.str,
    upload_allowed: builtins.str,
    additional_encryption_context: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    cookie_synchronization_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnUserSettings.CookieSynchronizationConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    customer_managed_key: typing.Optional[builtins.str] = None,
    disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    idle_disconnect_timeout_in_minutes: typing.Optional[jsii.Number] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
