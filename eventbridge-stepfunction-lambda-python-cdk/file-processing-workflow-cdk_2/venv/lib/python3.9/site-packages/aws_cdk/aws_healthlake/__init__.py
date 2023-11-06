'''
# AWS::HealthLake Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_healthlake as healthlake
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for HealthLake construct libraries](https://constructs.dev/search?q=healthlake)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::HealthLake resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthLake.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::HealthLake](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_HealthLake.html).

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
class CfnFHIRDatastore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore",
):
    '''Creates a Data Store that can ingest and export FHIR formatted data.

    .. epigraph::

       Please note that when a user tries to do an Update operation via CloudFormation, changes to the Data Store name, Type Version, PreloadDataConfig, or SSEConfiguration will delete their existing Data Store for the stack and create a new one. This will lead to potential loss of data.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_healthlake as healthlake
        
        cfn_fHIRDatastore = healthlake.CfnFHIRDatastore(self, "MyCfnFHIRDatastore",
            datastore_type_version="datastoreTypeVersion",
        
            # the properties below are optional
            datastore_name="datastoreName",
            identity_provider_configuration=healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(
                authorization_strategy="authorizationStrategy",
        
                # the properties below are optional
                fine_grained_authorization_enabled=False,
                idp_lambda_arn="idpLambdaArn",
                metadata="metadata"
            ),
            preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                preload_data_type="preloadDataType"
            ),
            sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                    cmk_type="cmkType",
        
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
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
        datastore_type_version: builtins.str,
        datastore_name: typing.Optional[builtins.str] = None,
        identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFHIRDatastore.IdentityProviderConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        preload_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFHIRDatastore.PreloadDataConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFHIRDatastore.SseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param datastore_type_version: The FHIR version of the data store. The only supported version is R4.
        :param datastore_name: The user generated name for the data store.
        :param identity_provider_configuration: The identity provider configuration for the datastore.
        :param preload_data_config: The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.
        :param sse_configuration: The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a84066c5df4c48a34d687987d48edfe8b65e8bda26e4da5f30db9c938e54b90)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFHIRDatastoreProps(
            datastore_type_version=datastore_type_version,
            datastore_name=datastore_name,
            identity_provider_configuration=identity_provider_configuration,
            preload_data_config=preload_data_config,
            sse_configuration=sse_configuration,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f9041dc50c8109815f2c8dd04e804c6471002a65ab5f8f21a4695f6a237e3703)
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
            type_hints = typing.get_type_hints(_typecheckingstub__98c34e70b6ec2df3b888529b3c31e66d8c6bede9b01bd8e9f59661918d44ba4f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAt")
    def attr_created_at(self) -> _IResolvable_da3f097b:
        '''The time that a Data Store was created.

        :cloudformationAttribute: CreatedAt
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrCreatedAt"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAtNanos")
    def attr_created_at_nanos(self) -> jsii.Number:
        '''Nanoseconds.

        :cloudformationAttribute: CreatedAt.Nanos
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreatedAtNanos"))

    @builtins.property
    @jsii.member(jsii_name="attrCreatedAtSeconds")
    def attr_created_at_seconds(self) -> builtins.str:
        '''Seconds since epoch.

        :cloudformationAttribute: CreatedAt.Seconds
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCreatedAtSeconds"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreArn")
    def attr_datastore_arn(self) -> builtins.str:
        '''The Data Store ARN is generated during the creation of the Data Store and can be found in the output from the initial Data Store creation request.

        :cloudformationAttribute: DatastoreArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreArn"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreEndpoint")
    def attr_datastore_endpoint(self) -> builtins.str:
        '''The endpoint for the created Data Store.

        :cloudformationAttribute: DatastoreEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreId")
    def attr_datastore_id(self) -> builtins.str:
        '''The Amazon generated Data Store id.

        This id is in the output from the initial Data Store creation call.

        :cloudformationAttribute: DatastoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreId"))

    @builtins.property
    @jsii.member(jsii_name="attrDatastoreStatus")
    def attr_datastore_status(self) -> builtins.str:
        '''The status of the FHIR Data Store.

        Possible statuses are ‘CREATING’, ‘ACTIVE’, ‘DELETING’, ‘DELETED’.

        :cloudformationAttribute: DatastoreStatus
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDatastoreStatus"))

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
    @jsii.member(jsii_name="datastoreTypeVersion")
    def datastore_type_version(self) -> builtins.str:
        '''The FHIR version of the data store.'''
        return typing.cast(builtins.str, jsii.get(self, "datastoreTypeVersion"))

    @datastore_type_version.setter
    def datastore_type_version(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5808500ce498cbcd60021c25c05f2f5ec6982551bc42bc79b3964a61257718e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreTypeVersion", value)

    @builtins.property
    @jsii.member(jsii_name="datastoreName")
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The user generated name for the data store.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datastoreName"))

    @datastore_name.setter
    def datastore_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3d86ac6fd32fffececf8454df94145383c2e779b9b5f1a30896102278cd1a9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datastoreName", value)

    @builtins.property
    @jsii.member(jsii_name="identityProviderConfiguration")
    def identity_provider_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]]:
        '''The identity provider configuration for the datastore.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]], jsii.get(self, "identityProviderConfiguration"))

    @identity_provider_configuration.setter
    def identity_provider_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.IdentityProviderConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__612b8cf4bba44e8e4744db8a7c2eaefe0b9bd601172c067d2c5a9feeb75cb14f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityProviderConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="preloadDataConfig")
    def preload_data_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.PreloadDataConfigProperty"]]:
        '''The preloaded data configuration for the data store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.PreloadDataConfigProperty"]], jsii.get(self, "preloadDataConfig"))

    @preload_data_config.setter
    def preload_data_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.PreloadDataConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b4d362bc0e9c9065e9f83741b0f46cfc52f253212d6a4551c7a2d9e4fd7e630)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "preloadDataConfig", value)

    @builtins.property
    @jsii.member(jsii_name="sseConfiguration")
    def sse_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.SseConfigurationProperty"]]:
        '''The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.SseConfigurationProperty"]], jsii.get(self, "sseConfiguration"))

    @sse_configuration.setter
    def sse_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.SseConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d21d284c17f3b1e178b27b28fe912e0eaebeaa7ca9612eff81512c42f71c29d2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28ffa2ce0bad1140b8ffa060738f5e180bc7033b7f2e9f274ce2d1d871b5d620)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.CreatedAtProperty",
        jsii_struct_bases=[],
        name_mapping={"nanos": "nanos", "seconds": "seconds"},
    )
    class CreatedAtProperty:
        def __init__(self, *, nanos: jsii.Number, seconds: builtins.str) -> None:
            '''The time that a Data Store was created.

            :param nanos: Nanoseconds.
            :param seconds: Seconds since epoch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                created_at_property = healthlake.CfnFHIRDatastore.CreatedAtProperty(
                    nanos=123,
                    seconds="seconds"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__914232fa94e4874b18f9fa312fe19be92103d3c527212c1cc7038dd05916c72f)
                check_type(argname="argument nanos", value=nanos, expected_type=type_hints["nanos"])
                check_type(argname="argument seconds", value=seconds, expected_type=type_hints["seconds"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "nanos": nanos,
                "seconds": seconds,
            }

        @builtins.property
        def nanos(self) -> jsii.Number:
            '''Nanoseconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-nanos
            '''
            result = self._values.get("nanos")
            assert result is not None, "Required property 'nanos' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def seconds(self) -> builtins.str:
            '''Seconds since epoch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-createdat.html#cfn-healthlake-fhirdatastore-createdat-seconds
            '''
            result = self._values.get("seconds")
            assert result is not None, "Required property 'seconds' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CreatedAtProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_strategy": "authorizationStrategy",
            "fine_grained_authorization_enabled": "fineGrainedAuthorizationEnabled",
            "idp_lambda_arn": "idpLambdaArn",
            "metadata": "metadata",
        },
    )
    class IdentityProviderConfigurationProperty:
        def __init__(
            self,
            *,
            authorization_strategy: builtins.str,
            fine_grained_authorization_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            idp_lambda_arn: typing.Optional[builtins.str] = None,
            metadata: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The identity provider configuration for the datastore.

            :param authorization_strategy: Type of Authorization Strategy. The two types of supported Authorization strategies are SMART_ON_FHIR_V1 and AWS_AUTH.
            :param fine_grained_authorization_enabled: Flag to indicate if fine-grained authorization will be enabled for the datastore.
            :param idp_lambda_arn: The Amazon Resource Name (ARN) of the Lambda function that will be used to decode the access token created by the authorization server.
            :param metadata: The JSON metadata elements for identity provider configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                identity_provider_configuration_property = healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(
                    authorization_strategy="authorizationStrategy",
                
                    # the properties below are optional
                    fine_grained_authorization_enabled=False,
                    idp_lambda_arn="idpLambdaArn",
                    metadata="metadata"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f028d556a7a738b78a7fbfb130c7243f69ba20b6367ea5c21f2e6bcc60445fb)
                check_type(argname="argument authorization_strategy", value=authorization_strategy, expected_type=type_hints["authorization_strategy"])
                check_type(argname="argument fine_grained_authorization_enabled", value=fine_grained_authorization_enabled, expected_type=type_hints["fine_grained_authorization_enabled"])
                check_type(argname="argument idp_lambda_arn", value=idp_lambda_arn, expected_type=type_hints["idp_lambda_arn"])
                check_type(argname="argument metadata", value=metadata, expected_type=type_hints["metadata"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authorization_strategy": authorization_strategy,
            }
            if fine_grained_authorization_enabled is not None:
                self._values["fine_grained_authorization_enabled"] = fine_grained_authorization_enabled
            if idp_lambda_arn is not None:
                self._values["idp_lambda_arn"] = idp_lambda_arn
            if metadata is not None:
                self._values["metadata"] = metadata

        @builtins.property
        def authorization_strategy(self) -> builtins.str:
            '''Type of Authorization Strategy.

            The two types of supported Authorization strategies are SMART_ON_FHIR_V1 and AWS_AUTH.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-authorizationstrategy
            '''
            result = self._values.get("authorization_strategy")
            assert result is not None, "Required property 'authorization_strategy' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def fine_grained_authorization_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Flag to indicate if fine-grained authorization will be enabled for the datastore.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-finegrainedauthorizationenabled
            '''
            result = self._values.get("fine_grained_authorization_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def idp_lambda_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Lambda function that will be used to decode the access token created by the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-idplambdaarn
            '''
            result = self._values.get("idp_lambda_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def metadata(self) -> typing.Optional[builtins.str]:
            '''The JSON metadata elements for identity provider configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-identityproviderconfiguration.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration-metadata
            '''
            result = self._values.get("metadata")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentityProviderConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cmk_type": "cmkType", "kms_key_id": "kmsKeyId"},
    )
    class KmsEncryptionConfigProperty:
        def __init__(
            self,
            *,
            cmk_type: builtins.str,
            kms_key_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The customer-managed-key(CMK) used when creating a Data Store.

            If a customer owned key is not specified, an Amazon owned key will be used for encryption.

            :param cmk_type: The type of customer-managed-key(CMK) used for encryption. The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .
            :param kms_key_id: The KMS encryption key id/alias used to encrypt the data store contents at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                kms_encryption_config_property = healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                    cmk_type="cmkType",
                
                    # the properties below are optional
                    kms_key_id="kmsKeyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a204f0ae0d6b5a9246c0ce66e5f12f0873c70941743ebe67b84b3bf96c81207a)
                check_type(argname="argument cmk_type", value=cmk_type, expected_type=type_hints["cmk_type"])
                check_type(argname="argument kms_key_id", value=kms_key_id, expected_type=type_hints["kms_key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cmk_type": cmk_type,
            }
            if kms_key_id is not None:
                self._values["kms_key_id"] = kms_key_id

        @builtins.property
        def cmk_type(self) -> builtins.str:
            '''The type of customer-managed-key(CMK) used for encryption.

            The two types of supported CMKs are customer owned CMKs and Amazon owned CMKs. For more information on CMK types, see `KmsEncryptionConfig <https://docs.aws.amazon.com/healthlake/latest/APIReference/API_KmsEncryptionConfig.html#HealthLake-Type-KmsEncryptionConfig-CmkType>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-cmktype
            '''
            result = self._values.get("cmk_type")
            assert result is not None, "Required property 'cmk_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_id(self) -> typing.Optional[builtins.str]:
            '''The KMS encryption key id/alias used to encrypt the data store contents at rest.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-kmsencryptionconfig.html#cfn-healthlake-fhirdatastore-kmsencryptionconfig-kmskeyid
            '''
            result = self._values.get("kms_key_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KmsEncryptionConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.PreloadDataConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"preload_data_type": "preloadDataType"},
    )
    class PreloadDataConfigProperty:
        def __init__(self, *, preload_data_type: builtins.str) -> None:
            '''Optional parameter to preload data upon creation of the data store.

            Currently, the only supported preloaded data is synthetic data generated from Synthea.

            :param preload_data_type: The type of preloaded data. Only Synthea preloaded data is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                preload_data_config_property = healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                    preload_data_type="preloadDataType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2807add39d82212bb123d916748097e974e9ff969a2403ee51221376730abb77)
                check_type(argname="argument preload_data_type", value=preload_data_type, expected_type=type_hints["preload_data_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "preload_data_type": preload_data_type,
            }

        @builtins.property
        def preload_data_type(self) -> builtins.str:
            '''The type of preloaded data.

            Only Synthea preloaded data is supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-preloaddataconfig.html#cfn-healthlake-fhirdatastore-preloaddataconfig-preloaddatatype
            '''
            result = self._values.get("preload_data_type")
            assert result is not None, "Required property 'preload_data_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PreloadDataConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastore.SseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"kms_encryption_config": "kmsEncryptionConfig"},
    )
    class SseConfigurationProperty:
        def __init__(
            self,
            *,
            kms_encryption_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFHIRDatastore.KmsEncryptionConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''The server-side encryption key configuration for a customer provided encryption key.

            :param kms_encryption_config: The server-side encryption key configuration for a customer provided encryption key (CMK).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_healthlake as healthlake
                
                sse_configuration_property = healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                    kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                        cmk_type="cmkType",
                
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ddeddf28afa132e70cf3cdeca1b03ad8c2e5de2f7786f5db94037eb39e61032d)
                check_type(argname="argument kms_encryption_config", value=kms_encryption_config, expected_type=type_hints["kms_encryption_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "kms_encryption_config": kms_encryption_config,
            }

        @builtins.property
        def kms_encryption_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.KmsEncryptionConfigProperty"]:
            '''The server-side encryption key configuration for a customer provided encryption key (CMK).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-healthlake-fhirdatastore-sseconfiguration.html#cfn-healthlake-fhirdatastore-sseconfiguration-kmsencryptionconfig
            '''
            result = self._values.get("kms_encryption_config")
            assert result is not None, "Required property 'kms_encryption_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFHIRDatastore.KmsEncryptionConfigProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_healthlake.CfnFHIRDatastoreProps",
    jsii_struct_bases=[],
    name_mapping={
        "datastore_type_version": "datastoreTypeVersion",
        "datastore_name": "datastoreName",
        "identity_provider_configuration": "identityProviderConfiguration",
        "preload_data_config": "preloadDataConfig",
        "sse_configuration": "sseConfiguration",
        "tags": "tags",
    },
)
class CfnFHIRDatastoreProps:
    def __init__(
        self,
        *,
        datastore_type_version: builtins.str,
        datastore_name: typing.Optional[builtins.str] = None,
        identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        preload_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFHIRDatastore``.

        :param datastore_type_version: The FHIR version of the data store. The only supported version is R4.
        :param datastore_name: The user generated name for the data store.
        :param identity_provider_configuration: The identity provider configuration for the datastore.
        :param preload_data_config: The preloaded data configuration for the data store. Only data preloaded from Synthea is supported.
        :param sse_configuration: The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.
        :param tags: An array of key-value pairs to apply to this resource. For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_healthlake as healthlake
            
            cfn_fHIRDatastore_props = healthlake.CfnFHIRDatastoreProps(
                datastore_type_version="datastoreTypeVersion",
            
                # the properties below are optional
                datastore_name="datastoreName",
                identity_provider_configuration=healthlake.CfnFHIRDatastore.IdentityProviderConfigurationProperty(
                    authorization_strategy="authorizationStrategy",
            
                    # the properties below are optional
                    fine_grained_authorization_enabled=False,
                    idp_lambda_arn="idpLambdaArn",
                    metadata="metadata"
                ),
                preload_data_config=healthlake.CfnFHIRDatastore.PreloadDataConfigProperty(
                    preload_data_type="preloadDataType"
                ),
                sse_configuration=healthlake.CfnFHIRDatastore.SseConfigurationProperty(
                    kms_encryption_config=healthlake.CfnFHIRDatastore.KmsEncryptionConfigProperty(
                        cmk_type="cmkType",
            
                        # the properties below are optional
                        kms_key_id="kmsKeyId"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f7e172077b0d6f3f4825d2eeb030b9523f0239350078a907c09cabc7ce33420)
            check_type(argname="argument datastore_type_version", value=datastore_type_version, expected_type=type_hints["datastore_type_version"])
            check_type(argname="argument datastore_name", value=datastore_name, expected_type=type_hints["datastore_name"])
            check_type(argname="argument identity_provider_configuration", value=identity_provider_configuration, expected_type=type_hints["identity_provider_configuration"])
            check_type(argname="argument preload_data_config", value=preload_data_config, expected_type=type_hints["preload_data_config"])
            check_type(argname="argument sse_configuration", value=sse_configuration, expected_type=type_hints["sse_configuration"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "datastore_type_version": datastore_type_version,
        }
        if datastore_name is not None:
            self._values["datastore_name"] = datastore_name
        if identity_provider_configuration is not None:
            self._values["identity_provider_configuration"] = identity_provider_configuration
        if preload_data_config is not None:
            self._values["preload_data_config"] = preload_data_config
        if sse_configuration is not None:
            self._values["sse_configuration"] = sse_configuration
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def datastore_type_version(self) -> builtins.str:
        '''The FHIR version of the data store.

        The only supported version is R4.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastoretypeversion
        '''
        result = self._values.get("datastore_type_version")
        assert result is not None, "Required property 'datastore_type_version' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def datastore_name(self) -> typing.Optional[builtins.str]:
        '''The user generated name for the data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-datastorename
        '''
        result = self._values.get("datastore_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def identity_provider_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.IdentityProviderConfigurationProperty]]:
        '''The identity provider configuration for the datastore.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-identityproviderconfiguration
        '''
        result = self._values.get("identity_provider_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.IdentityProviderConfigurationProperty]], result)

    @builtins.property
    def preload_data_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.PreloadDataConfigProperty]]:
        '''The preloaded data configuration for the data store.

        Only data preloaded from Synthea is supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-preloaddataconfig
        '''
        result = self._values.get("preload_data_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.PreloadDataConfigProperty]], result)

    @builtins.property
    def sse_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.SseConfigurationProperty]]:
        '''The server-side encryption key configuration for a customer provided encryption key specified for creating a data store.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-sseconfiguration
        '''
        result = self._values.get("sse_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.SseConfigurationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''An array of key-value pairs to apply to this resource.

        For more information, see `Tag <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-healthlake-fhirdatastore.html#cfn-healthlake-fhirdatastore-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFHIRDatastoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnFHIRDatastore",
    "CfnFHIRDatastoreProps",
]

publication.publish()

def _typecheckingstub__5a84066c5df4c48a34d687987d48edfe8b65e8bda26e4da5f30db9c938e54b90(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    datastore_type_version: builtins.str,
    datastore_name: typing.Optional[builtins.str] = None,
    identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    preload_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f9041dc50c8109815f2c8dd04e804c6471002a65ab5f8f21a4695f6a237e3703(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98c34e70b6ec2df3b888529b3c31e66d8c6bede9b01bd8e9f59661918d44ba4f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5808500ce498cbcd60021c25c05f2f5ec6982551bc42bc79b3964a61257718e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3d86ac6fd32fffececf8454df94145383c2e779b9b5f1a30896102278cd1a9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__612b8cf4bba44e8e4744db8a7c2eaefe0b9bd601172c067d2c5a9feeb75cb14f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.IdentityProviderConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b4d362bc0e9c9065e9f83741b0f46cfc52f253212d6a4551c7a2d9e4fd7e630(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.PreloadDataConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d21d284c17f3b1e178b27b28fe912e0eaebeaa7ca9612eff81512c42f71c29d2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFHIRDatastore.SseConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28ffa2ce0bad1140b8ffa060738f5e180bc7033b7f2e9f274ce2d1d871b5d620(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__914232fa94e4874b18f9fa312fe19be92103d3c527212c1cc7038dd05916c72f(
    *,
    nanos: jsii.Number,
    seconds: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f028d556a7a738b78a7fbfb130c7243f69ba20b6367ea5c21f2e6bcc60445fb(
    *,
    authorization_strategy: builtins.str,
    fine_grained_authorization_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    idp_lambda_arn: typing.Optional[builtins.str] = None,
    metadata: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a204f0ae0d6b5a9246c0ce66e5f12f0873c70941743ebe67b84b3bf96c81207a(
    *,
    cmk_type: builtins.str,
    kms_key_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2807add39d82212bb123d916748097e974e9ff969a2403ee51221376730abb77(
    *,
    preload_data_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddeddf28afa132e70cf3cdeca1b03ad8c2e5de2f7786f5db94037eb39e61032d(
    *,
    kms_encryption_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.KmsEncryptionConfigProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f7e172077b0d6f3f4825d2eeb030b9523f0239350078a907c09cabc7ce33420(
    *,
    datastore_type_version: builtins.str,
    datastore_name: typing.Optional[builtins.str] = None,
    identity_provider_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.IdentityProviderConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    preload_data_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.PreloadDataConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFHIRDatastore.SseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
