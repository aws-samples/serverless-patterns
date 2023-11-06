'''
# AWS::VerifiedPermissions Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_verifiedpermissions as verifiedpermissions
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for VerifiedPermissions construct libraries](https://constructs.dev/search?q=verifiedpermissions)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::VerifiedPermissions resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_VerifiedPermissions.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::VerifiedPermissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_VerifiedPermissions.html).

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
class CfnIdentitySource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnIdentitySource",
):
    '''Creates or updates a reference to Amazon Cognito as an external identity provider.

    If you are creating a new identity source, then you must specify a ``Configuration`` . If you are updating an existing identity source, then you must specify an ``UpdateConfiguration`` .

    After you create an identity source, you can use the identities provided by the IdP as proxies for the principal in authorization queries that use the `IsAuthorizedWithToken <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_IsAuthorizedWithToken.html>`_ operation. These identities take the form of tokens that contain claims about the user, such as IDs, attributes and group memberships. Amazon Cognito provides both identity tokens and access tokens, and Verified Permissions can use either or both. Any combination of identity and access tokens results in the same Cedar principal. Verified Permissions automatically translates the information about the identities into the standard Cedar attributes that can be evaluated by your policies. Because the Amazon Cognito identity and access tokens can contain different information, the tokens you choose to use determine the attributes that are available to access in the Cedar principal from your policies.

    Amazon Cognito Identity is not available in all of the same AWS Regions as Amazon Verified Permissions . Because of this, the ``AWS::VerifiedPermissions::IdentitySource`` type is not available to create from AWS CloudFormation in Regions where Amazon Cognito Identity is not currently available. Users can still create ``AWS::VerifiedPermissions::IdentitySource`` in those Regions, but only from the AWS CLI , Amazon Verified Permissions SDK, or from the AWS console.
    .. epigraph::

       To reference a user from this identity source in your Cedar policies, use the following syntax.

       *IdentityType::"|*

       Where ``IdentityType`` is the string that you provide to the ``PrincipalEntityType`` parameter for this operation. The ``CognitoUserPoolId`` and ``CognitoClientId`` are defined by the Amazon Cognito user pool.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_verifiedpermissions as verifiedpermissions
        
        cfn_identity_source = verifiedpermissions.CfnIdentitySource(self, "MyCfnIdentitySource",
            configuration=verifiedpermissions.CfnIdentitySource.IdentitySourceConfigurationProperty(
                cognito_user_pool_configuration=verifiedpermissions.CfnIdentitySource.CognitoUserPoolConfigurationProperty(
                    user_pool_arn="userPoolArn",
        
                    # the properties below are optional
                    client_ids=["clientIds"]
                )
            ),
        
            # the properties below are optional
            policy_store_id="policyStoreId",
            principal_entity_type="principalEntityType"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdentitySource.IdentitySourceConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        policy_store_id: typing.Optional[builtins.str] = None,
        principal_entity_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration: Contains configuration information used when creating or updating an identity source. .. epigraph:: At this time, the only valid member of this structure is a Amazon Cognito user pool configuration. You must specify a ``userPoolArn`` , and optionally, a ``ClientId`` .
        :param policy_store_id: Specifies the ID of the policy store in which you want to store this identity source. Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.
        :param principal_entity_type: Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07eaeca96a1d003d022bfe00d6c5c32734ab27136e499f6e8156e663df49ac9c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIdentitySourceProps(
            configuration=configuration,
            policy_store_id=policy_store_id,
            principal_entity_type=principal_entity_type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__95a2edb04b43b1618d587b15e2cf074997623461e1244c6c2fbb3b742d793b2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__24686eaf77005bef822114d3afe28e8d764e87194252fe8e60283944b2e0742c)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDetails")
    def attr_details(self) -> _IResolvable_da3f097b:
        '''A structure that contains information about the configuration of the identity source.

        :cloudformationAttribute: Details
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrDetails"))

    @builtins.property
    @jsii.member(jsii_name="attrDetailsClientIds")
    def attr_details_client_ids(self) -> typing.List[builtins.str]:
        '''The application client IDs associated with the specified Amazon Cognito user pool that are enabled for this identity source.

        :cloudformationAttribute: Details.ClientIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrDetailsClientIds"))

    @builtins.property
    @jsii.member(jsii_name="attrDetailsDiscoveryUrl")
    def attr_details_discovery_url(self) -> builtins.str:
        '''The well-known URL that points to this user pool's OIDC discovery endpoint.

        This is a URL string in the following format. This URL replaces the placeholders for both the AWS Region and the user pool identifier with those appropriate for this user pool.

        ``https://cognito-idp.<region>.amazonaws.com/<user-pool-id>/.well-known/openid-configuration``

        :cloudformationAttribute: Details.DiscoveryUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDetailsDiscoveryUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrDetailsOpenIdIssuer")
    def attr_details_open_id_issuer(self) -> builtins.str:
        '''A string that identifies the type of OIDC service represented by this identity source.

        At this time, the only valid value is ``cognito`` .

        :cloudformationAttribute: Details.OpenIdIssuer
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDetailsOpenIdIssuer"))

    @builtins.property
    @jsii.member(jsii_name="attrDetailsUserPoolArn")
    def attr_details_user_pool_arn(self) -> builtins.str:
        '''The `Amazon Resource Name (ARN) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the Amazon Cognito user pool whose identities are accessible to this Verified Permissions policy store.

        :cloudformationAttribute: Details.UserPoolArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDetailsUserPoolArn"))

    @builtins.property
    @jsii.member(jsii_name="attrIdentitySourceId")
    def attr_identity_source_id(self) -> builtins.str:
        '''The unique ID of the new or updated identity store.

        :cloudformationAttribute: IdentitySourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIdentitySourceId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="configuration")
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IdentitySourceConfigurationProperty"]:
        '''Contains configuration information used when creating or updating an identity source.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IdentitySourceConfigurationProperty"], jsii.get(self, "configuration"))

    @configuration.setter
    def configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.IdentitySourceConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4a4151d5edcacd46d57d191db8fc897a1618f6b6c43e1f07f119ab8f8b421c0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configuration", value)

    @builtins.property
    @jsii.member(jsii_name="policyStoreId")
    def policy_store_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ID of the policy store in which you want to store this identity source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyStoreId"))

    @policy_store_id.setter
    def policy_store_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f391fc07d87adb5874b1e9c3274f87754ce8643942edb0e42ae4d9a25e1608a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyStoreId", value)

    @builtins.property
    @jsii.member(jsii_name="principalEntityType")
    def principal_entity_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "principalEntityType"))

    @principal_entity_type.setter
    def principal_entity_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a223458d7b26a527452b756a4160058ec95241630d285690b62ec99c8b0f981)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "principalEntityType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnIdentitySource.CognitoUserPoolConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"user_pool_arn": "userPoolArn", "client_ids": "clientIds"},
    )
    class CognitoUserPoolConfigurationProperty:
        def __init__(
            self,
            *,
            user_pool_arn: builtins.str,
            client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A structure that contains configuration information used when creating or updating an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions .

            :param user_pool_arn: The `Amazon Resource Name (ARN) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the Amazon Cognito user pool that contains the identities to be authorized.
            :param client_ids: The unique application client IDs that are associated with the specified Amazon Cognito user pool. Example: ``"ClientIds": ["&ExampleCogClientId;"]``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                cognito_user_pool_configuration_property = verifiedpermissions.CfnIdentitySource.CognitoUserPoolConfigurationProperty(
                    user_pool_arn="userPoolArn",
                
                    # the properties below are optional
                    client_ids=["clientIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__75fd393134ee256da001941239770b4cb04ba63bc1c52b04b0d0a17fc493bed8)
                check_type(argname="argument user_pool_arn", value=user_pool_arn, expected_type=type_hints["user_pool_arn"])
                check_type(argname="argument client_ids", value=client_ids, expected_type=type_hints["client_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "user_pool_arn": user_pool_arn,
            }
            if client_ids is not None:
                self._values["client_ids"] = client_ids

        @builtins.property
        def user_pool_arn(self) -> builtins.str:
            '''The `Amazon Resource Name (ARN) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the Amazon Cognito user pool that contains the identities to be authorized.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-userpoolarn
            '''
            result = self._values.get("user_pool_arn")
            assert result is not None, "Required property 'user_pool_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The unique application client IDs that are associated with the specified Amazon Cognito user pool.

            Example: ``"ClientIds": ["&ExampleCogClientId;"]``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-cognitouserpoolconfiguration.html#cfn-verifiedpermissions-identitysource-cognitouserpoolconfiguration-clientids
            '''
            result = self._values.get("client_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoUserPoolConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnIdentitySource.IdentitySourceConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "cognito_user_pool_configuration": "cognitoUserPoolConfiguration",
        },
    )
    class IdentitySourceConfigurationProperty:
        def __init__(
            self,
            *,
            cognito_user_pool_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnIdentitySource.CognitoUserPoolConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A structure that contains configuration information used when creating or updating a new identity source.

            .. epigraph::

               At this time, the only valid member of this structure is a Amazon Cognito user pool configuration.

               You must specify a ``userPoolArn`` , and optionally, a ``ClientId`` .

            :param cognito_user_pool_configuration: A structure that contains configuration information used when creating or updating an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                identity_source_configuration_property = verifiedpermissions.CfnIdentitySource.IdentitySourceConfigurationProperty(
                    cognito_user_pool_configuration=verifiedpermissions.CfnIdentitySource.CognitoUserPoolConfigurationProperty(
                        user_pool_arn="userPoolArn",
                
                        # the properties below are optional
                        client_ids=["clientIds"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cb8ac8b859528aa35f38e7ba0f1da77e89bd8aa3f424fb5dcd81661032e5a44e)
                check_type(argname="argument cognito_user_pool_configuration", value=cognito_user_pool_configuration, expected_type=type_hints["cognito_user_pool_configuration"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cognito_user_pool_configuration": cognito_user_pool_configuration,
            }

        @builtins.property
        def cognito_user_pool_configuration(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.CognitoUserPoolConfigurationProperty"]:
            '''A structure that contains configuration information used when creating or updating an identity source that represents a connection to an Amazon Cognito user pool used as an identity provider for Verified Permissions .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourceconfiguration.html#cfn-verifiedpermissions-identitysource-identitysourceconfiguration-cognitouserpoolconfiguration
            '''
            result = self._values.get("cognito_user_pool_configuration")
            assert result is not None, "Required property 'cognito_user_pool_configuration' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnIdentitySource.CognitoUserPoolConfigurationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentitySourceConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnIdentitySource.IdentitySourceDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_ids": "clientIds",
            "discovery_url": "discoveryUrl",
            "open_id_issuer": "openIdIssuer",
            "user_pool_arn": "userPoolArn",
        },
    )
    class IdentitySourceDetailsProperty:
        def __init__(
            self,
            *,
            client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
            discovery_url: typing.Optional[builtins.str] = None,
            open_id_issuer: typing.Optional[builtins.str] = None,
            user_pool_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that contains configuration of the identity source.

            :param client_ids: The application client IDs associated with the specified Amazon Cognito user pool that are enabled for this identity source.
            :param discovery_url: The well-known URL that points to this user pool's OIDC discovery endpoint. This is a URL string in the following format. This URL replaces the placeholders for both the AWS Region and the user pool identifier with those appropriate for this user pool. ``https://cognito-idp. *<region>* .amazonaws.com/ *<user-pool-id>* /.well-known/openid-configuration``
            :param open_id_issuer: A string that identifies the type of OIDC service represented by this identity source. At this time, the only valid value is ``cognito`` .
            :param user_pool_arn: The `Amazon Resource Name (ARN) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the Amazon Cognito user pool whose identities are accessible to this Verified Permissions policy store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                identity_source_details_property = verifiedpermissions.CfnIdentitySource.IdentitySourceDetailsProperty(
                    client_ids=["clientIds"],
                    discovery_url="discoveryUrl",
                    open_id_issuer="openIdIssuer",
                    user_pool_arn="userPoolArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7de43a4292ffc2c919be30326e38112109b1f65de4681523bb84b29e2c91ea1d)
                check_type(argname="argument client_ids", value=client_ids, expected_type=type_hints["client_ids"])
                check_type(argname="argument discovery_url", value=discovery_url, expected_type=type_hints["discovery_url"])
                check_type(argname="argument open_id_issuer", value=open_id_issuer, expected_type=type_hints["open_id_issuer"])
                check_type(argname="argument user_pool_arn", value=user_pool_arn, expected_type=type_hints["user_pool_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if client_ids is not None:
                self._values["client_ids"] = client_ids
            if discovery_url is not None:
                self._values["discovery_url"] = discovery_url
            if open_id_issuer is not None:
                self._values["open_id_issuer"] = open_id_issuer
            if user_pool_arn is not None:
                self._values["user_pool_arn"] = user_pool_arn

        @builtins.property
        def client_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The application client IDs associated with the specified Amazon Cognito user pool that are enabled for this identity source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-clientids
            '''
            result = self._values.get("client_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def discovery_url(self) -> typing.Optional[builtins.str]:
            '''The well-known URL that points to this user pool's OIDC discovery endpoint.

            This is a URL string in the following format. This URL replaces the placeholders for both the AWS Region and the user pool identifier with those appropriate for this user pool.

            ``https://cognito-idp. *<region>* .amazonaws.com/ *<user-pool-id>* /.well-known/openid-configuration``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-discoveryurl
            '''
            result = self._values.get("discovery_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def open_id_issuer(self) -> typing.Optional[builtins.str]:
            '''A string that identifies the type of OIDC service represented by this identity source.

            At this time, the only valid value is ``cognito`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-openidissuer
            '''
            result = self._values.get("open_id_issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def user_pool_arn(self) -> typing.Optional[builtins.str]:
            '''The `Amazon Resource Name (ARN) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the Amazon Cognito user pool whose identities are accessible to this Verified Permissions policy store.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-identitysource-identitysourcedetails.html#cfn-verifiedpermissions-identitysource-identitysourcedetails-userpoolarn
            '''
            result = self._values.get("user_pool_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentitySourceDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnIdentitySourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration": "configuration",
        "policy_store_id": "policyStoreId",
        "principal_entity_type": "principalEntityType",
    },
)
class CfnIdentitySourceProps:
    def __init__(
        self,
        *,
        configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IdentitySourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
        policy_store_id: typing.Optional[builtins.str] = None,
        principal_entity_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIdentitySource``.

        :param configuration: Contains configuration information used when creating or updating an identity source. .. epigraph:: At this time, the only valid member of this structure is a Amazon Cognito user pool configuration. You must specify a ``userPoolArn`` , and optionally, a ``ClientId`` .
        :param policy_store_id: Specifies the ID of the policy store in which you want to store this identity source. Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.
        :param principal_entity_type: Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_verifiedpermissions as verifiedpermissions
            
            cfn_identity_source_props = verifiedpermissions.CfnIdentitySourceProps(
                configuration=verifiedpermissions.CfnIdentitySource.IdentitySourceConfigurationProperty(
                    cognito_user_pool_configuration=verifiedpermissions.CfnIdentitySource.CognitoUserPoolConfigurationProperty(
                        user_pool_arn="userPoolArn",
            
                        # the properties below are optional
                        client_ids=["clientIds"]
                    )
                ),
            
                # the properties below are optional
                policy_store_id="policyStoreId",
                principal_entity_type="principalEntityType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c26583940e2aa6e9d220c2c5b1722091a1344919725a0cfeb5b794a1ef3dc30)
            check_type(argname="argument configuration", value=configuration, expected_type=type_hints["configuration"])
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
            check_type(argname="argument principal_entity_type", value=principal_entity_type, expected_type=type_hints["principal_entity_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration": configuration,
        }
        if policy_store_id is not None:
            self._values["policy_store_id"] = policy_store_id
        if principal_entity_type is not None:
            self._values["principal_entity_type"] = principal_entity_type

    @builtins.property
    def configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnIdentitySource.IdentitySourceConfigurationProperty]:
        '''Contains configuration information used when creating or updating an identity source.

        .. epigraph::

           At this time, the only valid member of this structure is a Amazon Cognito user pool configuration.

           You must specify a ``userPoolArn`` , and optionally, a ``ClientId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html#cfn-verifiedpermissions-identitysource-configuration
        '''
        result = self._values.get("configuration")
        assert result is not None, "Required property 'configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnIdentitySource.IdentitySourceConfigurationProperty], result)

    @builtins.property
    def policy_store_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ID of the policy store in which you want to store this identity source.

        Only policies and requests made using this policy store can reference identities from the identity provider configured in the new identity source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html#cfn-verifiedpermissions-identitysource-policystoreid
        '''
        result = self._values.get("policy_store_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def principal_entity_type(self) -> typing.Optional[builtins.str]:
        '''Specifies the namespace and data type of the principals generated for identities authenticated by the new identity source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-identitysource.html#cfn-verifiedpermissions-identitysource-principalentitytype
        '''
        result = self._values.get("principal_entity_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIdentitySourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicy",
):
    '''Creates or updates a Cedar policy and saves it in the specified policy store.

    You can create either a static policy or a policy linked to a policy template.

    You can directly update only static policies. To update a template-linked policy, you must update it's linked policy template instead.

    - To create a static policy, in the ``Definition`` include a ``Static`` element that includes the Cedar policy text in the ``Statement`` element.
    - To create a policy that is dynamically linked to a policy template, in the ``Definition`` include a ``Templatelinked`` element that specifies the policy template ID and the principal and resource to associate with this policy. If the policy template is ever updated, any policies linked to the policy template automatically use the updated template.

    .. epigraph::

       - If policy validation is enabled in the policy store, then updating a static policy causes Verified Permissions to validate the policy against the schema in the policy store. If the updated static policy doesn't pass validation, the operation fails and the update isn't stored.
       - When you edit a static policy, You can change only certain elements of a static policy:
       - The action referenced by the policy.
       - A condition clause, such as when and unless.

       You can't change these elements of a static policy:

       - Changing a policy from a static policy to a template-linked policy.
       - Changing the effect of a static policy from permit or forbid.
       - The principal referenced by a static policy.
       - The resource referenced by a static policy.
       - To update a template-linked policy, you must update the template instead.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_verifiedpermissions as verifiedpermissions
        
        cfn_policy = verifiedpermissions.CfnPolicy(self, "MyCfnPolicy",
            definition=verifiedpermissions.CfnPolicy.PolicyDefinitionProperty(
                static=verifiedpermissions.CfnPolicy.StaticPolicyDefinitionProperty(
                    statement="statement",
        
                    # the properties below are optional
                    description="description"
                ),
                template_linked=verifiedpermissions.CfnPolicy.TemplateLinkedPolicyDefinitionProperty(
                    policy_template_id="policyTemplateId",
        
                    # the properties below are optional
                    principal=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                        entity_id="entityId",
                        entity_type="entityType"
                    ),
                    resource=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                        entity_id="entityId",
                        entity_type="entityType"
                    )
                )
            ),
        
            # the properties below are optional
            policy_store_id="policyStoreId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.PolicyDefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        policy_store_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param definition: Specifies the policy type and content to use for the new or updated policy. The definition structure must include either a ``Static`` or a ``TemplateLinked`` element.
        :param policy_store_id: Specifies the ``PolicyStoreId`` of the policy store you want to store the policy in.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__932d37260f4c95ce0d4cfb6f5e3796b8f66e65d7a495df114c5b4f584fdfede3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(definition=definition, policy_store_id=policy_store_id)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__941ceea3378ade839831427d12e7c8edbd4a6b88709411e8a8b124a45c8ef2cc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d9ac1d010ed46520e3576ca5acdf1d52fc8bb97ecdb8126f2a568dedf4a88486)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyId")
    def attr_policy_id(self) -> builtins.str:
        '''The unique ID of the new or updated policy.

        :cloudformationAttribute: PolicyId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyId"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyType")
    def attr_policy_type(self) -> builtins.str:
        '''The type of the policy. This is one of the following values:.

        - Static
        - TemplateLinked

        :cloudformationAttribute: PolicyType
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyType"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPolicy.PolicyDefinitionProperty"]:
        '''Specifies the policy type and content to use for the new or updated policy.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPolicy.PolicyDefinitionProperty"], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPolicy.PolicyDefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0e3117111907b9eabd5104f9c3da934606ecead2cc1dd472a311797c17559e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="policyStoreId")
    def policy_store_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ``PolicyStoreId`` of the policy store you want to store the policy in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyStoreId"))

    @policy_store_id.setter
    def policy_store_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af5f964efa4eebd0aad31a50c66d1e8fb17861ac0f6d2918c9fae4d65ae3ed65)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyStoreId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicy.EntityIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"entity_id": "entityId", "entity_type": "entityType"},
    )
    class EntityIdentifierProperty:
        def __init__(
            self,
            *,
            entity_id: builtins.str,
            entity_type: builtins.str,
        ) -> None:
            '''Contains the identifier of an entity in a policy, including its ID and type.

            :param entity_id: The identifier of an entity. ``"entityId":" *identifier* "``
            :param entity_type: The type of an entity. Example: ``"entityType":" *typeName* "``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                entity_identifier_property = verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                    entity_id="entityId",
                    entity_type="entityType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80b68e962a54d074af7b3cc892cd08c282113791cd81d634b97dcbaee8d7aada)
                check_type(argname="argument entity_id", value=entity_id, expected_type=type_hints["entity_id"])
                check_type(argname="argument entity_type", value=entity_type, expected_type=type_hints["entity_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entity_id": entity_id,
                "entity_type": entity_type,
            }

        @builtins.property
        def entity_id(self) -> builtins.str:
            '''The identifier of an entity.

            ``"entityId":" *identifier* "``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html#cfn-verifiedpermissions-policy-entityidentifier-entityid
            '''
            result = self._values.get("entity_id")
            assert result is not None, "Required property 'entity_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def entity_type(self) -> builtins.str:
            '''The type of an entity.

            Example: ``"entityType":" *typeName* "``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-entityidentifier.html#cfn-verifiedpermissions-policy-entityidentifier-entitytype
            '''
            result = self._values.get("entity_type")
            assert result is not None, "Required property 'entity_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EntityIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicy.PolicyDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"static": "static", "template_linked": "templateLinked"},
    )
    class PolicyDefinitionProperty:
        def __init__(
            self,
            *,
            static: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.StaticPolicyDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            template_linked: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.TemplateLinkedPolicyDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that defines a Cedar policy.

            It includes the policy type, a description, and a policy body. This is a top level data type used to create a policy.

            This data type is used as a request parameter for the `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`_ operation. This structure must always have either an ``Static`` or a ``TemplateLinked`` element.

            :param static: A structure that describes a static policy. An static policy doesn't use a template or allow placeholders for entities.
            :param template_linked: A structure that describes a policy that was instantiated from a template. The template can specify placeholders for ``principal`` and ``resource`` . When you use `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`_ to create a policy from a template, you specify the exact principal and resource to use for the instantiated policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                policy_definition_property = verifiedpermissions.CfnPolicy.PolicyDefinitionProperty(
                    static=verifiedpermissions.CfnPolicy.StaticPolicyDefinitionProperty(
                        statement="statement",
                
                        # the properties below are optional
                        description="description"
                    ),
                    template_linked=verifiedpermissions.CfnPolicy.TemplateLinkedPolicyDefinitionProperty(
                        policy_template_id="policyTemplateId",
                
                        # the properties below are optional
                        principal=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                            entity_id="entityId",
                            entity_type="entityType"
                        ),
                        resource=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                            entity_id="entityId",
                            entity_type="entityType"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ea9a1b2ab442fa75d466be41a62425f1446eca0e49776ab3d4f403ef3bff659)
                check_type(argname="argument static", value=static, expected_type=type_hints["static"])
                check_type(argname="argument template_linked", value=template_linked, expected_type=type_hints["template_linked"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if static is not None:
                self._values["static"] = static
            if template_linked is not None:
                self._values["template_linked"] = template_linked

        @builtins.property
        def static(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.StaticPolicyDefinitionProperty"]]:
            '''A structure that describes a static policy.

            An static policy doesn't use a template or allow placeholders for entities.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html#cfn-verifiedpermissions-policy-policydefinition-static
            '''
            result = self._values.get("static")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.StaticPolicyDefinitionProperty"]], result)

        @builtins.property
        def template_linked(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.TemplateLinkedPolicyDefinitionProperty"]]:
            '''A structure that describes a policy that was instantiated from a template.

            The template can specify placeholders for ``principal`` and ``resource`` . When you use `CreatePolicy <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_CreatePolicy.html>`_ to create a policy from a template, you specify the exact principal and resource to use for the instantiated policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-policydefinition.html#cfn-verifiedpermissions-policy-policydefinition-templatelinked
            '''
            result = self._values.get("template_linked")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.TemplateLinkedPolicyDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PolicyDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicy.StaticPolicyDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"statement": "statement", "description": "description"},
    )
    class StaticPolicyDefinitionProperty:
        def __init__(
            self,
            *,
            statement: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A structure that defines a static policy.

            :param statement: The policy content of the static policy, written in the Cedar policy language.
            :param description: The description of the static policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                static_policy_definition_property = verifiedpermissions.CfnPolicy.StaticPolicyDefinitionProperty(
                    statement="statement",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bcb0e793d5e3d11db3246b9052c13e0334a5da5ebe6fb7e0e9816a96d6e56f2a)
                check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "statement": statement,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def statement(self) -> builtins.str:
            '''The policy content of the static policy, written in the Cedar policy language.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html#cfn-verifiedpermissions-policy-staticpolicydefinition-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the static policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-staticpolicydefinition.html#cfn-verifiedpermissions-policy-staticpolicydefinition-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StaticPolicyDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicy.TemplateLinkedPolicyDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_template_id": "policyTemplateId",
            "principal": "principal",
            "resource": "resource",
        },
    )
    class TemplateLinkedPolicyDefinitionProperty:
        def __init__(
            self,
            *,
            policy_template_id: builtins.str,
            principal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.EntityIdentifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicy.EntityIdentifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''A structure that describes a policy created by instantiating a policy template.

            .. epigraph::

               You can't directly update a template-linked policy. You must update the associated policy template instead.

            :param policy_template_id: The unique identifier of the policy template used to create this policy.
            :param principal: The principal associated with this template-linked policy. Verified Permissions substitutes this principal for the ``?principal`` placeholder in the policy template when it evaluates an authorization request.
            :param resource: The resource associated with this template-linked policy. Verified Permissions substitutes this resource for the ``?resource`` placeholder in the policy template when it evaluates an authorization request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                template_linked_policy_definition_property = verifiedpermissions.CfnPolicy.TemplateLinkedPolicyDefinitionProperty(
                    policy_template_id="policyTemplateId",
                
                    # the properties below are optional
                    principal=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                        entity_id="entityId",
                        entity_type="entityType"
                    ),
                    resource=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                        entity_id="entityId",
                        entity_type="entityType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f08e3c5c1bd2311fdc752e1698cc9e3c43df4329919de529435361b36fd06b51)
                check_type(argname="argument policy_template_id", value=policy_template_id, expected_type=type_hints["policy_template_id"])
                check_type(argname="argument principal", value=principal, expected_type=type_hints["principal"])
                check_type(argname="argument resource", value=resource, expected_type=type_hints["resource"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_template_id": policy_template_id,
            }
            if principal is not None:
                self._values["principal"] = principal
            if resource is not None:
                self._values["resource"] = resource

        @builtins.property
        def policy_template_id(self) -> builtins.str:
            '''The unique identifier of the policy template used to create this policy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-policytemplateid
            '''
            result = self._values.get("policy_template_id")
            assert result is not None, "Required property 'policy_template_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def principal(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.EntityIdentifierProperty"]]:
            '''The principal associated with this template-linked policy.

            Verified Permissions substitutes this principal for the ``?principal`` placeholder in the policy template when it evaluates an authorization request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-principal
            '''
            result = self._values.get("principal")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.EntityIdentifierProperty"]], result)

        @builtins.property
        def resource(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.EntityIdentifierProperty"]]:
            '''The resource associated with this template-linked policy.

            Verified Permissions substitutes this resource for the ``?resource`` placeholder in the policy template when it evaluates an authorization request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policy-templatelinkedpolicydefinition.html#cfn-verifiedpermissions-policy-templatelinkedpolicydefinition-resource
            '''
            result = self._values.get("resource")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicy.EntityIdentifierProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateLinkedPolicyDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={"definition": "definition", "policy_store_id": "policyStoreId"},
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
        policy_store_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param definition: Specifies the policy type and content to use for the new or updated policy. The definition structure must include either a ``Static`` or a ``TemplateLinked`` element.
        :param policy_store_id: Specifies the ``PolicyStoreId`` of the policy store you want to store the policy in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_verifiedpermissions as verifiedpermissions
            
            cfn_policy_props = verifiedpermissions.CfnPolicyProps(
                definition=verifiedpermissions.CfnPolicy.PolicyDefinitionProperty(
                    static=verifiedpermissions.CfnPolicy.StaticPolicyDefinitionProperty(
                        statement="statement",
            
                        # the properties below are optional
                        description="description"
                    ),
                    template_linked=verifiedpermissions.CfnPolicy.TemplateLinkedPolicyDefinitionProperty(
                        policy_template_id="policyTemplateId",
            
                        # the properties below are optional
                        principal=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                            entity_id="entityId",
                            entity_type="entityType"
                        ),
                        resource=verifiedpermissions.CfnPolicy.EntityIdentifierProperty(
                            entity_id="entityId",
                            entity_type="entityType"
                        )
                    )
                ),
            
                # the properties below are optional
                policy_store_id="policyStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__191bbebc841c99122e08daf1974076e79203748010138391f8f044b50c7f6a8b)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "definition": definition,
        }
        if policy_store_id is not None:
            self._values["policy_store_id"] = policy_store_id

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPolicy.PolicyDefinitionProperty]:
        '''Specifies the policy type and content to use for the new or updated policy.

        The definition structure must include either a ``Static`` or a ``TemplateLinked`` element.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html#cfn-verifiedpermissions-policy-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPolicy.PolicyDefinitionProperty], result)

    @builtins.property
    def policy_store_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ``PolicyStoreId`` of the policy store you want to store the policy in.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policy.html#cfn-verifiedpermissions-policy-policystoreid
        '''
        result = self._values.get("policy_store_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPolicyStore(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyStore",
):
    '''Creates a policy store.

    A policy store is a container for policy resources. You can create a separate policy store for each of your applications.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_verifiedpermissions as verifiedpermissions
        
        cfn_policy_store = verifiedpermissions.CfnPolicyStore(self, "MyCfnPolicyStore",
            validation_settings=verifiedpermissions.CfnPolicyStore.ValidationSettingsProperty(
                mode="mode"
            ),
        
            # the properties below are optional
            schema=verifiedpermissions.CfnPolicyStore.SchemaDefinitionProperty(
                cedar_json="cedarJson"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        validation_settings: typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicyStore.ValidationSettingsProperty", typing.Dict[builtins.str, typing.Any]]],
        schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPolicyStore.SchemaDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param validation_settings: Specifies the validation setting for this policy store. Currently, the only valid and required value is ``Mode`` . .. epigraph:: We recommend that you turn on ``STRICT`` mode only after you define a schema. If a schema doesn't exist, then ``STRICT`` mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore>`_ . Then, when you have a schema defined, use `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore>`_ again to turn validation back on.
        :param schema: Creates or updates the policy schema in a policy store. Cedar can use the schema to validate any Cedar policies and policy templates submitted to the policy store. Any changes to the schema validate only policies and templates submitted after the schema change. Existing policies and templates are not re-evaluated against the changed schema. If you later update a policy, then it is evaluated against the new schema at that time.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cc0f2986096a74fa71e43f21c340737b2abb3e3f40afbfe29ca3f0bd9b39ee9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyStoreProps(
            validation_settings=validation_settings, schema=schema
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ad1782ca771d54cb918458c633b77eb8f22d4fb4325e8039ddc8db9486e906f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b9483ea9f7344dfa4c582224fff74146950ba16baba14583540ed9d88481f08d)
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
        '''The `Amazon Resource Name (ARN) <https://docs.aws.amazon.com//general/latest/gr/aws-arns-and-namespaces.html>`_ of the new or updated policy store.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyStoreId")
    def attr_policy_store_id(self) -> builtins.str:
        '''The unique ID of the new or updated policy store.

        :cloudformationAttribute: PolicyStoreId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyStoreId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="validationSettings")
    def validation_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnPolicyStore.ValidationSettingsProperty"]:
        '''Specifies the validation setting for this policy store.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnPolicyStore.ValidationSettingsProperty"], jsii.get(self, "validationSettings"))

    @validation_settings.setter
    def validation_settings(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnPolicyStore.ValidationSettingsProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f75a45bc8d480e61f7e4827904f9e4cfad1881a595a32bf1bebfb6efb618e30f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationSettings", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicyStore.SchemaDefinitionProperty"]]:
        '''Creates or updates the policy schema in a policy store.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicyStore.SchemaDefinitionProperty"]], jsii.get(self, "schema"))

    @schema.setter
    def schema(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPolicyStore.SchemaDefinitionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59218b40bcf4539ad10409fa2f065ad910ceb568598b66b8276c1d8844d45901)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyStore.SchemaDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"cedar_json": "cedarJson"},
    )
    class SchemaDefinitionProperty:
        def __init__(self, *, cedar_json: typing.Optional[builtins.str] = None) -> None:
            '''Contains a list of principal types, resource types, and actions that can be specified in policies stored in the same policy store.

            If the validation mode for the policy store is set to ``STRICT`` , then policies that can't be validated by this schema are rejected by Verified Permissions and can't be stored in the policy store.

            :param cedar_json: A JSON string representation of the schema supported by applications that use this policy store. For more information, see `Policy store schema <https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html>`_ in the *Amazon Verified Permissions User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-schemadefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                schema_definition_property = verifiedpermissions.CfnPolicyStore.SchemaDefinitionProperty(
                    cedar_json="cedarJson"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__40c95b318ee977eff43d9078495fc0215bd302506cf821187fe6998b1a04ee9f)
                check_type(argname="argument cedar_json", value=cedar_json, expected_type=type_hints["cedar_json"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if cedar_json is not None:
                self._values["cedar_json"] = cedar_json

        @builtins.property
        def cedar_json(self) -> typing.Optional[builtins.str]:
            '''A JSON string representation of the schema supported by applications that use this policy store.

            For more information, see `Policy store schema <https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/schema.html>`_ in the *Amazon Verified Permissions User Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-schemadefinition.html#cfn-verifiedpermissions-policystore-schemadefinition-cedarjson
            '''
            result = self._values.get("cedar_json")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SchemaDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyStore.ValidationSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"mode": "mode"},
    )
    class ValidationSettingsProperty:
        def __init__(self, *, mode: builtins.str) -> None:
            '''A structure that contains Cedar policy validation settings for the policy store.

            The validation mode determines which validation failures that Cedar considers serious enough to block acceptance of a new or edited static policy or policy template.

            :param mode: The validation mode currently configured for this policy store. The valid values are:. - *OFF* – Neither Verified Permissions nor Cedar perform any validation on policies. No validation errors are reported by either service. - *STRICT* – Requires a schema to be present in the policy store. Cedar performs validation on all submitted new or updated static policies and policy templates. Any that fail validation are rejected and Cedar doesn't store them in the policy store. .. epigraph:: If ``Mode=STRICT`` and the policy store doesn't contain a schema, Verified Permissions rejects all static policies and policy templates because there is no schema to validate against. To submit a static policy or policy template without a schema, you must turn off validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-validationsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_verifiedpermissions as verifiedpermissions
                
                validation_settings_property = verifiedpermissions.CfnPolicyStore.ValidationSettingsProperty(
                    mode="mode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__441c781d6c8944f199761ac7a1433da41be4b40fc2d3cbb5df9ccf86001008fa)
                check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "mode": mode,
            }

        @builtins.property
        def mode(self) -> builtins.str:
            '''The validation mode currently configured for this policy store. The valid values are:.

            - *OFF* – Neither Verified Permissions nor Cedar perform any validation on policies. No validation errors are reported by either service.
            - *STRICT* – Requires a schema to be present in the policy store. Cedar performs validation on all submitted new or updated static policies and policy templates. Any that fail validation are rejected and Cedar doesn't store them in the policy store.

            .. epigraph::

               If ``Mode=STRICT`` and the policy store doesn't contain a schema, Verified Permissions rejects all static policies and policy templates because there is no schema to validate against.

               To submit a static policy or policy template without a schema, you must turn off validation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-verifiedpermissions-policystore-validationsettings.html#cfn-verifiedpermissions-policystore-validationsettings-mode
            '''
            result = self._values.get("mode")
            assert result is not None, "Required property 'mode' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ValidationSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyStoreProps",
    jsii_struct_bases=[],
    name_mapping={"validation_settings": "validationSettings", "schema": "schema"},
)
class CfnPolicyStoreProps:
    def __init__(
        self,
        *,
        validation_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicyStore.ValidationSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
        schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicyStore.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicyStore``.

        :param validation_settings: Specifies the validation setting for this policy store. Currently, the only valid and required value is ``Mode`` . .. epigraph:: We recommend that you turn on ``STRICT`` mode only after you define a schema. If a schema doesn't exist, then ``STRICT`` mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore>`_ . Then, when you have a schema defined, use `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore>`_ again to turn validation back on.
        :param schema: Creates or updates the policy schema in a policy store. Cedar can use the schema to validate any Cedar policies and policy templates submitted to the policy store. Any changes to the schema validate only policies and templates submitted after the schema change. Existing policies and templates are not re-evaluated against the changed schema. If you later update a policy, then it is evaluated against the new schema at that time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_verifiedpermissions as verifiedpermissions
            
            cfn_policy_store_props = verifiedpermissions.CfnPolicyStoreProps(
                validation_settings=verifiedpermissions.CfnPolicyStore.ValidationSettingsProperty(
                    mode="mode"
                ),
            
                # the properties below are optional
                schema=verifiedpermissions.CfnPolicyStore.SchemaDefinitionProperty(
                    cedar_json="cedarJson"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f8a612a98cf26f16f9e9de3e5b0a5faaf9ae49bfb39376380ab1ee24d31ca9f)
            check_type(argname="argument validation_settings", value=validation_settings, expected_type=type_hints["validation_settings"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "validation_settings": validation_settings,
        }
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def validation_settings(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnPolicyStore.ValidationSettingsProperty]:
        '''Specifies the validation setting for this policy store.

        Currently, the only valid and required value is ``Mode`` .
        .. epigraph::

           We recommend that you turn on ``STRICT`` mode only after you define a schema. If a schema doesn't exist, then ``STRICT`` mode causes any policy to fail validation, and Verified Permissions rejects the policy. You can turn off validation by using the `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore>`_ . Then, when you have a schema defined, use `UpdatePolicyStore <https://docs.aws.amazon.com/verifiedpermissions/latest/apireference/API_UpdatePolicyStore>`_ again to turn validation back on.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html#cfn-verifiedpermissions-policystore-validationsettings
        '''
        result = self._values.get("validation_settings")
        assert result is not None, "Required property 'validation_settings' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnPolicyStore.ValidationSettingsProperty], result)

    @builtins.property
    def schema(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicyStore.SchemaDefinitionProperty]]:
        '''Creates or updates the policy schema in a policy store.

        Cedar can use the schema to validate any Cedar policies and policy templates submitted to the policy store. Any changes to the schema validate only policies and templates submitted after the schema change. Existing policies and templates are not re-evaluated against the changed schema. If you later update a policy, then it is evaluated against the new schema at that time.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policystore.html#cfn-verifiedpermissions-policystore-schema
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicyStore.SchemaDefinitionProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyStoreProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnPolicyTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyTemplate",
):
    '''Creates a policy template.

    A template can use placeholders for the principal and resource. A template must be instantiated into a policy by associating it with specific principals and resources to use for the placeholders. That instantiated policy can then be considered in authorization decisions. The instantiated policy works identically to any other policy, except that it is dynamically linked to the template. If the template changes, then any policies that are linked to that template are immediately updated as well.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_verifiedpermissions as verifiedpermissions
        
        cfn_policy_template = verifiedpermissions.CfnPolicyTemplate(self, "MyCfnPolicyTemplate",
            statement="statement",
        
            # the properties below are optional
            description="description",
            policy_store_id="policyStoreId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        statement: builtins.str,
        description: typing.Optional[builtins.str] = None,
        policy_store_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param statement: Specifies the content that you want to use for the new policy template, written in the Cedar policy language.
        :param description: The description to attach to the new or updated policy template.
        :param policy_store_id: The unique identifier of the policy store that contains the template.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed3e86dfb81e6515352391c646d690df7f34c6022cd94a51863a664c57bd434a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyTemplateProps(
            statement=statement,
            description=description,
            policy_store_id=policy_store_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__661112d1510f801966b9b8210dd49eeb935d2ee1bd962f58256fe5b51ba7cc98)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f04b9de9a49ca424d4dfad33bb18952b7d2283d300474f1320ab9feff69400ea)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrPolicyTemplateId")
    def attr_policy_template_id(self) -> builtins.str:
        '''The unique identifier of the new or modified policy template.

        :cloudformationAttribute: PolicyTemplateId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPolicyTemplateId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="statement")
    def statement(self) -> builtins.str:
        '''Specifies the content that you want to use for the new policy template, written in the Cedar policy language.'''
        return typing.cast(builtins.str, jsii.get(self, "statement"))

    @statement.setter
    def statement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592231050c584a4ecea5c3d0c9f03326be29cadce389428dbc9a25bed277efe4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statement", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to attach to the new or updated policy template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c58edfa87a5f12d9679dc9e906de042ce6fb26dbf1811d4fbdfc9c7e8b898830)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="policyStoreId")
    def policy_store_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the policy store that contains the template.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "policyStoreId"))

    @policy_store_id.setter
    def policy_store_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__582eca241418301fd48556f1bb838d7697b3f7ff23d57252d2d783d4532bcbae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policyStoreId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_verifiedpermissions.CfnPolicyTemplateProps",
    jsii_struct_bases=[],
    name_mapping={
        "statement": "statement",
        "description": "description",
        "policy_store_id": "policyStoreId",
    },
)
class CfnPolicyTemplateProps:
    def __init__(
        self,
        *,
        statement: builtins.str,
        description: typing.Optional[builtins.str] = None,
        policy_store_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicyTemplate``.

        :param statement: Specifies the content that you want to use for the new policy template, written in the Cedar policy language.
        :param description: The description to attach to the new or updated policy template.
        :param policy_store_id: The unique identifier of the policy store that contains the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_verifiedpermissions as verifiedpermissions
            
            cfn_policy_template_props = verifiedpermissions.CfnPolicyTemplateProps(
                statement="statement",
            
                # the properties below are optional
                description="description",
                policy_store_id="policyStoreId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__075de1d4e460af7b2858245a89bb9d63ffdb6f2cd0276b3d8b519fb35d765a82)
            check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument policy_store_id", value=policy_store_id, expected_type=type_hints["policy_store_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "statement": statement,
        }
        if description is not None:
            self._values["description"] = description
        if policy_store_id is not None:
            self._values["policy_store_id"] = policy_store_id

    @builtins.property
    def statement(self) -> builtins.str:
        '''Specifies the content that you want to use for the new policy template, written in the Cedar policy language.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html#cfn-verifiedpermissions-policytemplate-statement
        '''
        result = self._values.get("statement")
        assert result is not None, "Required property 'statement' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description to attach to the new or updated policy template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html#cfn-verifiedpermissions-policytemplate-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy_store_id(self) -> typing.Optional[builtins.str]:
        '''The unique identifier of the policy store that contains the template.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-verifiedpermissions-policytemplate.html#cfn-verifiedpermissions-policytemplate-policystoreid
        '''
        result = self._values.get("policy_store_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnIdentitySource",
    "CfnIdentitySourceProps",
    "CfnPolicy",
    "CfnPolicyProps",
    "CfnPolicyStore",
    "CfnPolicyStoreProps",
    "CfnPolicyTemplate",
    "CfnPolicyTemplateProps",
]

publication.publish()

def _typecheckingstub__07eaeca96a1d003d022bfe00d6c5c32734ab27136e499f6e8156e663df49ac9c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IdentitySourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    policy_store_id: typing.Optional[builtins.str] = None,
    principal_entity_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__95a2edb04b43b1618d587b15e2cf074997623461e1244c6c2fbb3b742d793b2a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24686eaf77005bef822114d3afe28e8d764e87194252fe8e60283944b2e0742c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4a4151d5edcacd46d57d191db8fc897a1618f6b6c43e1f07f119ab8f8b421c0(
    value: typing.Union[_IResolvable_da3f097b, CfnIdentitySource.IdentitySourceConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f391fc07d87adb5874b1e9c3274f87754ce8643942edb0e42ae4d9a25e1608a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a223458d7b26a527452b756a4160058ec95241630d285690b62ec99c8b0f981(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75fd393134ee256da001941239770b4cb04ba63bc1c52b04b0d0a17fc493bed8(
    *,
    user_pool_arn: builtins.str,
    client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb8ac8b859528aa35f38e7ba0f1da77e89bd8aa3f424fb5dcd81661032e5a44e(
    *,
    cognito_user_pool_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.CognitoUserPoolConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7de43a4292ffc2c919be30326e38112109b1f65de4681523bb84b29e2c91ea1d(
    *,
    client_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    discovery_url: typing.Optional[builtins.str] = None,
    open_id_issuer: typing.Optional[builtins.str] = None,
    user_pool_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c26583940e2aa6e9d220c2c5b1722091a1344919725a0cfeb5b794a1ef3dc30(
    *,
    configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnIdentitySource.IdentitySourceConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    policy_store_id: typing.Optional[builtins.str] = None,
    principal_entity_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__932d37260f4c95ce0d4cfb6f5e3796b8f66e65d7a495df114c5b4f584fdfede3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    policy_store_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__941ceea3378ade839831427d12e7c8edbd4a6b88709411e8a8b124a45c8ef2cc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9ac1d010ed46520e3576ca5acdf1d52fc8bb97ecdb8126f2a568dedf4a88486(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0e3117111907b9eabd5104f9c3da934606ecead2cc1dd472a311797c17559e5(
    value: typing.Union[_IResolvable_da3f097b, CfnPolicy.PolicyDefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af5f964efa4eebd0aad31a50c66d1e8fb17861ac0f6d2918c9fae4d65ae3ed65(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b68e962a54d074af7b3cc892cd08c282113791cd81d634b97dcbaee8d7aada(
    *,
    entity_id: builtins.str,
    entity_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ea9a1b2ab442fa75d466be41a62425f1446eca0e49776ab3d4f403ef3bff659(
    *,
    static: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.StaticPolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    template_linked: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.TemplateLinkedPolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bcb0e793d5e3d11db3246b9052c13e0334a5da5ebe6fb7e0e9816a96d6e56f2a(
    *,
    statement: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f08e3c5c1bd2311fdc752e1698cc9e3c43df4329919de529435361b36fd06b51(
    *,
    policy_template_id: builtins.str,
    principal: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.EntityIdentifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    resource: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.EntityIdentifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__191bbebc841c99122e08daf1974076e79203748010138391f8f044b50c7f6a8b(
    *,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicy.PolicyDefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    policy_store_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cc0f2986096a74fa71e43f21c340737b2abb3e3f40afbfe29ca3f0bd9b39ee9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    validation_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicyStore.ValidationSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicyStore.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ad1782ca771d54cb918458c633b77eb8f22d4fb4325e8039ddc8db9486e906f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9483ea9f7344dfa4c582224fff74146950ba16baba14583540ed9d88481f08d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f75a45bc8d480e61f7e4827904f9e4cfad1881a595a32bf1bebfb6efb618e30f(
    value: typing.Union[_IResolvable_da3f097b, CfnPolicyStore.ValidationSettingsProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59218b40bcf4539ad10409fa2f065ad910ceb568598b66b8276c1d8844d45901(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPolicyStore.SchemaDefinitionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40c95b318ee977eff43d9078495fc0215bd302506cf821187fe6998b1a04ee9f(
    *,
    cedar_json: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__441c781d6c8944f199761ac7a1433da41be4b40fc2d3cbb5df9ccf86001008fa(
    *,
    mode: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f8a612a98cf26f16f9e9de3e5b0a5faaf9ae49bfb39376380ab1ee24d31ca9f(
    *,
    validation_settings: typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicyStore.ValidationSettingsProperty, typing.Dict[builtins.str, typing.Any]]],
    schema: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPolicyStore.SchemaDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed3e86dfb81e6515352391c646d690df7f34c6022cd94a51863a664c57bd434a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    statement: builtins.str,
    description: typing.Optional[builtins.str] = None,
    policy_store_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__661112d1510f801966b9b8210dd49eeb935d2ee1bd962f58256fe5b51ba7cc98(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f04b9de9a49ca424d4dfad33bb18952b7d2283d300474f1320ab9feff69400ea(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592231050c584a4ecea5c3d0c9f03326be29cadce389428dbc9a25bed277efe4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c58edfa87a5f12d9679dc9e906de042ce6fb26dbf1811d4fbdfc9c7e8b898830(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__582eca241418301fd48556f1bb838d7697b3f7ff23d57252d2d783d4532bcbae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__075de1d4e460af7b2858245a89bb9d63ffdb6f2cd0276b3d8b519fb35d765a82(
    *,
    statement: builtins.str,
    description: typing.Optional[builtins.str] = None,
    policy_store_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
