'''
# AWS::FinSpace Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_finspace as finspace
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for FinSpace construct libraries](https://constructs.dev/search?q=finspace)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::FinSpace resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FinSpace.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::FinSpace](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_FinSpace.html).

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
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_finspace.CfnEnvironment",
):
    '''The ``AWS::FinSpace::Environment`` resource represents an Amazon FinSpace environment.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_finspace as finspace
        
        cfn_environment = finspace.CfnEnvironment(self, "MyCfnEnvironment",
            name="name",
        
            # the properties below are optional
            data_bundles=["dataBundles"],
            description="description",
            federation_mode="federationMode",
            federation_parameters=finspace.CfnEnvironment.FederationParametersProperty(
                application_call_back_url="applicationCallBackUrl",
                attribute_map=[finspace.CfnEnvironment.AttributeMapItemsProperty(
                    key="key",
                    value="value"
                )],
                federation_provider_name="federationProviderName",
                federation_urn="federationUrn",
                saml_metadata_document="samlMetadataDocument",
                saml_metadata_url="samlMetadataUrl"
            ),
            kms_key_id="kmsKeyId",
            superuser_parameters=finspace.CfnEnvironment.SuperuserParametersProperty(
                email_address="emailAddress",
                first_name="firstName",
                last_name="lastName"
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
        name: builtins.str,
        data_bundles: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        federation_mode: typing.Optional[builtins.str] = None,
        federation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.FederationParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        superuser_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.SuperuserParametersProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the FinSpace environment.
        :param data_bundles: (deprecated) ARNs of FinSpace Data Bundles to install.
        :param description: The description of the FinSpace environment.
        :param federation_mode: The authentication mode for the environment.
        :param federation_parameters: Configuration information when authentication mode is FEDERATED.
        :param kms_key_id: The KMS key id used to encrypt in the FinSpace environment.
        :param superuser_parameters: Configuration information for the superuser.
        :param tags: An array of key-value pairs to apply to this resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f57ac69116cda232b57cc77dd248367e34b3decfb4cc4cd606394bbf0afc629)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            name=name,
            data_bundles=data_bundles,
            description=description,
            federation_mode=federation_mode,
            federation_parameters=federation_parameters,
            kms_key_id=kms_key_id,
            superuser_parameters=superuser_parameters,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f5d0b1b73afeaee7185b654d27df42d0dbc9a9ffc19dfc7b89de95cb1b73263f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7d8a6132b285fca7a1395881be5f6bb87ccef46183c2e359af4f3536994a26a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsAccountId")
    def attr_aws_account_id(self) -> builtins.str:
        '''The ID of the AWS account in which the FinSpace environment is created.

        :cloudformationAttribute: AwsAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAwsAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrDedicatedServiceAccountId")
    def attr_dedicated_service_account_id(self) -> builtins.str:
        '''The AWS account ID of the dedicated service account associated with your FinSpace environment.

        :cloudformationAttribute: DedicatedServiceAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDedicatedServiceAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentArn")
    def attr_environment_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of your FinSpace environment.

        :cloudformationAttribute: EnvironmentArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentId")
    def attr_environment_id(self) -> builtins.str:
        '''The identifier of the FinSpace environment.

        :cloudformationAttribute: EnvironmentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentId"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentUrl")
    def attr_environment_url(self) -> builtins.str:
        '''The sign-in url for the web application of your FinSpace environment.

        :cloudformationAttribute: EnvironmentUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrSageMakerStudioDomainUrl")
    def attr_sage_maker_studio_domain_url(self) -> builtins.str:
        '''The url of the integrated FinSpace notebook environment in your web application.

        :cloudformationAttribute: SageMakerStudioDomainUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSageMakerStudioDomainUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The current status of creation of the FinSpace environment.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
        '''The name of the FinSpace environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__860fff0651bca3c119a16e47c1a3f46c146ecb823b9d700ccac98d3840d1fc35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="dataBundles")
    def data_bundles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) ARNs of FinSpace Data Bundles to install.

        :deprecated: this property has been deprecated

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "dataBundles"))

    @data_bundles.setter
    def data_bundles(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57ab0a0c1f1d83aaa81471315d4997899f5373567d02d2bfe1ff01b795a6c19b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataBundles", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the FinSpace environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b587720e33bbfed6cdec09f6eaf823330533e5ec920a19a167a59df1be1ceb04)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="federationMode")
    def federation_mode(self) -> typing.Optional[builtins.str]:
        '''The authentication mode for the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "federationMode"))

    @federation_mode.setter
    def federation_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__698ca730d63538f9ab600b8c12223be75f649f38fea3601360e8c5f6e823c88d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "federationMode", value)

    @builtins.property
    @jsii.member(jsii_name="federationParameters")
    def federation_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.FederationParametersProperty"]]:
        '''Configuration information when authentication mode is FEDERATED.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.FederationParametersProperty"]], jsii.get(self, "federationParameters"))

    @federation_parameters.setter
    def federation_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.FederationParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cca90468c4b1d8a076ea02e32a24ca04ce7d592d32ea406233dd210b7eaa423)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "federationParameters", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyId")
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The KMS key id used to encrypt in the FinSpace environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyId"))

    @kms_key_id.setter
    def kms_key_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__852fed3236b85f6d2b00ea193818d85950ae107536a7f50a2486ccc8b6f5381b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyId", value)

    @builtins.property
    @jsii.member(jsii_name="superuserParameters")
    def superuser_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.SuperuserParametersProperty"]]:
        '''Configuration information for the superuser.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.SuperuserParametersProperty"]], jsii.get(self, "superuserParameters"))

    @superuser_parameters.setter
    def superuser_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.SuperuserParametersProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f6516c69c8c2885eb602c5a32e8226805adc98ac19c7289e214f05c0825e6ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "superuserParameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6df014d0d715549eb062b878e03daf791b461fc8b0696c22784f904bd8c4fc9f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_finspace.CfnEnvironment.AttributeMapItemsProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class AttributeMapItemsProperty:
        def __init__(
            self,
            *,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param key: The key name of the tag. You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.
            :param value: The value for the tag. You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_finspace as finspace
                
                attribute_map_items_property = finspace.CfnEnvironment.AttributeMapItemsProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80f6184c649d0ba535c7ea6ce515aad13f895ec1d4a0746e2ad918a6c0d5ebfd)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key name of the tag.

            You can specify a value that is 1 to 128 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html#cfn-finspace-environment-attributemapitems-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The value for the tag.

            You can specify a value that is 0 to 256 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-attributemapitems.html#cfn-finspace-environment-attributemapitems-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AttributeMapItemsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_finspace.CfnEnvironment.FederationParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_call_back_url": "applicationCallBackUrl",
            "attribute_map": "attributeMap",
            "federation_provider_name": "federationProviderName",
            "federation_urn": "federationUrn",
            "saml_metadata_document": "samlMetadataDocument",
            "saml_metadata_url": "samlMetadataUrl",
        },
    )
    class FederationParametersProperty:
        def __init__(
            self,
            *,
            application_call_back_url: typing.Optional[builtins.str] = None,
            attribute_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEnvironment.AttributeMapItemsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            federation_provider_name: typing.Optional[builtins.str] = None,
            federation_urn: typing.Optional[builtins.str] = None,
            saml_metadata_document: typing.Optional[builtins.str] = None,
            saml_metadata_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration information when authentication mode is FEDERATED.

            :param application_call_back_url: The redirect or sign-in URL that should be entered into the SAML 2.0 compliant identity provider configuration (IdP).
            :param attribute_map: SAML attribute name and value. The name must always be ``Email`` and the value should be set to the attribute definition in which user email is set. For example, name would be ``Email`` and value ``http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`` . Please check your SAML 2.0 compliant identity provider (IdP) documentation for details.
            :param federation_provider_name: Name of the identity provider (IdP).
            :param federation_urn: The Uniform Resource Name (URN). Also referred as Service Provider URN or Audience URI or Service Provider Entity ID.
            :param saml_metadata_document: SAML 2.0 Metadata document from identity provider (IdP).
            :param saml_metadata_url: Provide the metadata URL from your SAML 2.0 compliant identity provider (IdP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_finspace as finspace
                
                federation_parameters_property = finspace.CfnEnvironment.FederationParametersProperty(
                    application_call_back_url="applicationCallBackUrl",
                    attribute_map=[finspace.CfnEnvironment.AttributeMapItemsProperty(
                        key="key",
                        value="value"
                    )],
                    federation_provider_name="federationProviderName",
                    federation_urn="federationUrn",
                    saml_metadata_document="samlMetadataDocument",
                    saml_metadata_url="samlMetadataUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94390d852a9fb25c0e9bf6a36878414124539d8bfebd99d35d44c2b338fa1cce)
                check_type(argname="argument application_call_back_url", value=application_call_back_url, expected_type=type_hints["application_call_back_url"])
                check_type(argname="argument attribute_map", value=attribute_map, expected_type=type_hints["attribute_map"])
                check_type(argname="argument federation_provider_name", value=federation_provider_name, expected_type=type_hints["federation_provider_name"])
                check_type(argname="argument federation_urn", value=federation_urn, expected_type=type_hints["federation_urn"])
                check_type(argname="argument saml_metadata_document", value=saml_metadata_document, expected_type=type_hints["saml_metadata_document"])
                check_type(argname="argument saml_metadata_url", value=saml_metadata_url, expected_type=type_hints["saml_metadata_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_call_back_url is not None:
                self._values["application_call_back_url"] = application_call_back_url
            if attribute_map is not None:
                self._values["attribute_map"] = attribute_map
            if federation_provider_name is not None:
                self._values["federation_provider_name"] = federation_provider_name
            if federation_urn is not None:
                self._values["federation_urn"] = federation_urn
            if saml_metadata_document is not None:
                self._values["saml_metadata_document"] = saml_metadata_document
            if saml_metadata_url is not None:
                self._values["saml_metadata_url"] = saml_metadata_url

        @builtins.property
        def application_call_back_url(self) -> typing.Optional[builtins.str]:
            '''The redirect or sign-in URL that should be entered into the SAML 2.0 compliant identity provider configuration (IdP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-applicationcallbackurl
            '''
            result = self._values.get("application_call_back_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def attribute_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.AttributeMapItemsProperty"]]]]:
            '''SAML attribute name and value.

            The name must always be ``Email`` and the value should be set to the attribute definition in which user email is set. For example, name would be ``Email`` and value ``http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress`` . Please check your SAML 2.0 compliant identity provider (IdP) documentation for details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-attributemap
            '''
            result = self._values.get("attribute_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnEnvironment.AttributeMapItemsProperty"]]]], result)

        @builtins.property
        def federation_provider_name(self) -> typing.Optional[builtins.str]:
            '''Name of the identity provider (IdP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationprovidername
            '''
            result = self._values.get("federation_provider_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def federation_urn(self) -> typing.Optional[builtins.str]:
            '''The Uniform Resource Name (URN).

            Also referred as Service Provider URN or Audience URI or Service Provider Entity ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-federationurn
            '''
            result = self._values.get("federation_urn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def saml_metadata_document(self) -> typing.Optional[builtins.str]:
            '''SAML 2.0 Metadata document from identity provider (IdP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadatadocument
            '''
            result = self._values.get("saml_metadata_document")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def saml_metadata_url(self) -> typing.Optional[builtins.str]:
            '''Provide the metadata URL from your SAML 2.0 compliant identity provider (IdP).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-federationparameters.html#cfn-finspace-environment-federationparameters-samlmetadataurl
            '''
            result = self._values.get("saml_metadata_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FederationParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_finspace.CfnEnvironment.SuperuserParametersProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email_address": "emailAddress",
            "first_name": "firstName",
            "last_name": "lastName",
        },
    )
    class SuperuserParametersProperty:
        def __init__(
            self,
            *,
            email_address: typing.Optional[builtins.str] = None,
            first_name: typing.Optional[builtins.str] = None,
            last_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Configuration information for the superuser.

            :param email_address: The email address of the superuser.
            :param first_name: The first name of the superuser.
            :param last_name: The last name of the superuser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_finspace as finspace
                
                superuser_parameters_property = finspace.CfnEnvironment.SuperuserParametersProperty(
                    email_address="emailAddress",
                    first_name="firstName",
                    last_name="lastName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30a1d9568bcc8c25bfd4568d72ee1d13dea0ac6eb1eeaac5c76a6db3d081ce9b)
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument first_name", value=first_name, expected_type=type_hints["first_name"])
                check_type(argname="argument last_name", value=last_name, expected_type=type_hints["last_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email_address is not None:
                self._values["email_address"] = email_address
            if first_name is not None:
                self._values["first_name"] = first_name
            if last_name is not None:
                self._values["last_name"] = last_name

        @builtins.property
        def email_address(self) -> typing.Optional[builtins.str]:
            '''The email address of the superuser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-emailaddress
            '''
            result = self._values.get("email_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_name(self) -> typing.Optional[builtins.str]:
            '''The first name of the superuser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-firstname
            '''
            result = self._values.get("first_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def last_name(self) -> typing.Optional[builtins.str]:
            '''The last name of the superuser.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-finspace-environment-superuserparameters.html#cfn-finspace-environment-superuserparameters-lastname
            '''
            result = self._values.get("last_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuperuserParametersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_finspace.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "data_bundles": "dataBundles",
        "description": "description",
        "federation_mode": "federationMode",
        "federation_parameters": "federationParameters",
        "kms_key_id": "kmsKeyId",
        "superuser_parameters": "superuserParameters",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        data_bundles: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        federation_mode: typing.Optional[builtins.str] = None,
        federation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.FederationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_key_id: typing.Optional[builtins.str] = None,
        superuser_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.SuperuserParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param name: The name of the FinSpace environment.
        :param data_bundles: (deprecated) ARNs of FinSpace Data Bundles to install.
        :param description: The description of the FinSpace environment.
        :param federation_mode: The authentication mode for the environment.
        :param federation_parameters: Configuration information when authentication mode is FEDERATED.
        :param kms_key_id: The KMS key id used to encrypt in the FinSpace environment.
        :param superuser_parameters: Configuration information for the superuser.
        :param tags: An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_finspace as finspace
            
            cfn_environment_props = finspace.CfnEnvironmentProps(
                name="name",
            
                # the properties below are optional
                data_bundles=["dataBundles"],
                description="description",
                federation_mode="federationMode",
                federation_parameters=finspace.CfnEnvironment.FederationParametersProperty(
                    application_call_back_url="applicationCallBackUrl",
                    attribute_map=[finspace.CfnEnvironment.AttributeMapItemsProperty(
                        key="key",
                        value="value"
                    )],
                    federation_provider_name="federationProviderName",
                    federation_urn="federationUrn",
                    saml_metadata_document="samlMetadataDocument",
                    saml_metadata_url="samlMetadataUrl"
                ),
                kms_key_id="kmsKeyId",
                superuser_parameters=finspace.CfnEnvironment.SuperuserParametersProperty(
                    email_address="emailAddress",
                    first_name="firstName",
                    last_name="lastName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7911e58237794983de7a2bf4de8d169915a752d95d989dc00d660b43f515bfa3)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument data_bundles", value=data_bundles, expected_type=type_hints["data_bundles"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument federation_mode", value=federation_mode, expected_type=type_hints["federation_mode"])
            check_type(argname="argument federation_parameters", value=federation_parameters, expected_type=type_hints["federation_parameters"])
            check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            check_type(argname="argument superuser_parameters", value=superuser_parameters, expected_type=type_hints["superuser_parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if data_bundles is not None:
            self._values["data_bundles"] = data_bundles
        if description is not None:
            self._values["description"] = description
        if federation_mode is not None:
            self._values["federation_mode"] = federation_mode
        if federation_parameters is not None:
            self._values["federation_parameters"] = federation_parameters
        if kms_key_id is not None:
            self._values["kms_key_id"] = kms_key_id
        if superuser_parameters is not None:
            self._values["superuser_parameters"] = superuser_parameters
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the FinSpace environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def data_bundles(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(deprecated) ARNs of FinSpace Data Bundles to install.

        :deprecated: this property has been deprecated

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-databundles
        :stability: deprecated
        '''
        result = self._values.get("data_bundles")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the FinSpace environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def federation_mode(self) -> typing.Optional[builtins.str]:
        '''The authentication mode for the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationmode
        '''
        result = self._values.get("federation_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def federation_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.FederationParametersProperty]]:
        '''Configuration information when authentication mode is FEDERATED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-federationparameters
        '''
        result = self._values.get("federation_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.FederationParametersProperty]], result)

    @builtins.property
    def kms_key_id(self) -> typing.Optional[builtins.str]:
        '''The KMS key id used to encrypt in the FinSpace environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-kmskeyid
        '''
        result = self._values.get("kms_key_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def superuser_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.SuperuserParametersProperty]]:
        '''Configuration information for the superuser.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-superuserparameters
        '''
        result = self._values.get("superuser_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.SuperuserParametersProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-finspace-environment.html#cfn-finspace-environment-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEnvironmentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnEnvironment",
    "CfnEnvironmentProps",
]

publication.publish()

def _typecheckingstub__9f57ac69116cda232b57cc77dd248367e34b3decfb4cc4cd606394bbf0afc629(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    data_bundles: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    federation_mode: typing.Optional[builtins.str] = None,
    federation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.FederationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    superuser_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.SuperuserParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5d0b1b73afeaee7185b654d27df42d0dbc9a9ffc19dfc7b89de95cb1b73263f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7d8a6132b285fca7a1395881be5f6bb87ccef46183c2e359af4f3536994a26a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__860fff0651bca3c119a16e47c1a3f46c146ecb823b9d700ccac98d3840d1fc35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57ab0a0c1f1d83aaa81471315d4997899f5373567d02d2bfe1ff01b795a6c19b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b587720e33bbfed6cdec09f6eaf823330533e5ec920a19a167a59df1be1ceb04(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__698ca730d63538f9ab600b8c12223be75f649f38fea3601360e8c5f6e823c88d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cca90468c4b1d8a076ea02e32a24ca04ce7d592d32ea406233dd210b7eaa423(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.FederationParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__852fed3236b85f6d2b00ea193818d85950ae107536a7f50a2486ccc8b6f5381b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f6516c69c8c2885eb602c5a32e8226805adc98ac19c7289e214f05c0825e6ef(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEnvironment.SuperuserParametersProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6df014d0d715549eb062b878e03daf791b461fc8b0696c22784f904bd8c4fc9f(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80f6184c649d0ba535c7ea6ce515aad13f895ec1d4a0746e2ad918a6c0d5ebfd(
    *,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94390d852a9fb25c0e9bf6a36878414124539d8bfebd99d35d44c2b338fa1cce(
    *,
    application_call_back_url: typing.Optional[builtins.str] = None,
    attribute_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.AttributeMapItemsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    federation_provider_name: typing.Optional[builtins.str] = None,
    federation_urn: typing.Optional[builtins.str] = None,
    saml_metadata_document: typing.Optional[builtins.str] = None,
    saml_metadata_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30a1d9568bcc8c25bfd4568d72ee1d13dea0ac6eb1eeaac5c76a6db3d081ce9b(
    *,
    email_address: typing.Optional[builtins.str] = None,
    first_name: typing.Optional[builtins.str] = None,
    last_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7911e58237794983de7a2bf4de8d169915a752d95d989dc00d660b43f515bfa3(
    *,
    name: builtins.str,
    data_bundles: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    federation_mode: typing.Optional[builtins.str] = None,
    federation_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.FederationParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_key_id: typing.Optional[builtins.str] = None,
    superuser_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEnvironment.SuperuserParametersProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
