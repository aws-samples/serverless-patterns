'''
# AWS::AppFlow Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_appflow as appflow
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for AppFlow construct libraries](https://constructs.dev/search?q=appflow)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::AppFlow resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppFlow.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::AppFlow](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_AppFlow.html).

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


@jsii.implements(_IInspectable_c2943556)
class CfnConnector(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appflow.CfnConnector",
):
    '''Creates a new connector profile associated with your AWS account .

    There is a soft quota of 100 connector profiles per AWS account . If you need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow team through the Amazon AppFlow support channel. In each connector profile that you create, you can provide the credentials and properties for only one connector.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html
    :cloudformationResource: AWS::AppFlow::Connector
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appflow as appflow
        
        cfn_connector = appflow.CfnConnector(self, "MyCfnConnector",
            connector_provisioning_config=appflow.CfnConnector.ConnectorProvisioningConfigProperty(
                lambda_=appflow.CfnConnector.LambdaConnectorProvisioningConfigProperty(
                    lambda_arn="lambdaArn"
                )
            ),
            connector_provisioning_type="connectorProvisioningType",
        
            # the properties below are optional
            connector_label="connectorLabel",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        connector_provisioning_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.ConnectorProvisioningConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        connector_provisioning_type: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connector_provisioning_config: The configuration required for registering the connector.
        :param connector_provisioning_type: The provisioning type used to register the connector.
        :param connector_label: The label used for registering the connector.
        :param description: A description about the connector runtime setting.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6bcd4af5099c6e263b309786f40e217a7b9534ca68e65e020a22b581160f7869)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProps(
            connector_provisioning_config=connector_provisioning_config,
            connector_provisioning_type=connector_provisioning_type,
            connector_label=connector_label,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02fe175937a3851291cfe730cc744110fbd6b06062b2f72be6c64c38cb811cc2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14908eefe331e5d6c90e4d41161c6e2df84fc31fc2c80c358aacd6d72b71fdad)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectorArn")
    def attr_connector_arn(self) -> builtins.str:
        '''The arn of the connector.

        The arn is unique for each ConnectorRegistration in your AWS account.

        :cloudformationAttribute: ConnectorArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="connectorProvisioningConfig")
    def connector_provisioning_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConnector.ConnectorProvisioningConfigProperty"]:
        '''The configuration required for registering the connector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConnector.ConnectorProvisioningConfigProperty"], jsii.get(self, "connectorProvisioningConfig"))

    @connector_provisioning_config.setter
    def connector_provisioning_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConnector.ConnectorProvisioningConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9a08650fe9a17324090179ab56d9509e56252c9865e3f2e1fa676c14b6cc03f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProvisioningConfig", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProvisioningType")
    def connector_provisioning_type(self) -> builtins.str:
        '''The provisioning type used to register the connector.'''
        return typing.cast(builtins.str, jsii.get(self, "connectorProvisioningType"))

    @connector_provisioning_type.setter
    def connector_provisioning_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2220ebaf0220a2885b5b9cf115ec38fe35115066c974f84c1b2c720720335fc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProvisioningType", value)

    @builtins.property
    @jsii.member(jsii_name="connectorLabel")
    def connector_label(self) -> typing.Optional[builtins.str]:
        '''The label used for registering the connector.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorLabel"))

    @connector_label.setter
    def connector_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__223722b79e59f7d76338e4d79ccc19e3b7a392375aa34d0c39efd833af999447)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorLabel", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about the connector runtime setting.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5201599f188c2814b1848bd455a0576a0e0a2d098b49d428d52355c42d74246a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnector.ConnectorProvisioningConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_": "lambda"},
    )
    class ConnectorProvisioningConfigProperty:
        def __init__(
            self,
            *,
            lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnector.LambdaConnectorProvisioningConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about the configuration of the connector being registered.

            :param lambda_: Contains information about the configuration of the lambda which is being registered as the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-connectorprovisioningconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                connector_provisioning_config_property = appflow.CfnConnector.ConnectorProvisioningConfigProperty(
                    lambda_=appflow.CfnConnector.LambdaConnectorProvisioningConfigProperty(
                        lambda_arn="lambdaArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f30575b197aa2e677da77a036dc5bfce7d878974062d45e335a7a1ace3bb43fa)
                check_type(argname="argument lambda_", value=lambda_, expected_type=type_hints["lambda_"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_ is not None:
                self._values["lambda_"] = lambda_

        @builtins.property
        def lambda_(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.LambdaConnectorProvisioningConfigProperty"]]:
            '''Contains information about the configuration of the lambda which is being registered as the connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-connectorprovisioningconfig.html#cfn-appflow-connector-connectorprovisioningconfig-lambda
            '''
            result = self._values.get("lambda_")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnector.LambdaConnectorProvisioningConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorProvisioningConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnector.LambdaConnectorProvisioningConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"lambda_arn": "lambdaArn"},
    )
    class LambdaConnectorProvisioningConfigProperty:
        def __init__(self, *, lambda_arn: builtins.str) -> None:
            '''Contains information about the configuration of the lambda which is being registered as the connector.

            :param lambda_arn: Lambda ARN of the connector being registered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-lambdaconnectorprovisioningconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                lambda_connector_provisioning_config_property = appflow.CfnConnector.LambdaConnectorProvisioningConfigProperty(
                    lambda_arn="lambdaArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1eac52f23e3de5229c743187d6ff0c48af0c8b82a08a1bfe7aa685c49794c096)
                check_type(argname="argument lambda_arn", value=lambda_arn, expected_type=type_hints["lambda_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "lambda_arn": lambda_arn,
            }

        @builtins.property
        def lambda_arn(self) -> builtins.str:
            '''Lambda ARN of the connector being registered.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connector-lambdaconnectorprovisioningconfig.html#cfn-appflow-connector-lambdaconnectorprovisioningconfig-lambdaarn
            '''
            result = self._values.get("lambda_arn")
            assert result is not None, "Required property 'lambda_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaConnectorProvisioningConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnConnectorProfile(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile",
):
    '''The ``AWS::AppFlow::ConnectorProfile`` resource is an Amazon AppFlow resource type that specifies the configuration profile for an instance of a connector.

    This includes the provided name, credentials ARN, connection-mode, and so on. The fields that are common to all types of connector profiles are explicitly specified under the ``Properties`` field. The rest of the connector-specific properties are specified under ``Properties/ConnectorProfileConfig`` .
    .. epigraph::

       If you want to use AWS CloudFormation to create a connector profile for connectors that implement OAuth (such as Salesforce, Slack, Zendesk, and Google Analytics), you must fetch the access and refresh tokens. You can do this by implementing your own UI for OAuth, or by retrieving the tokens from elsewhere. Alternatively, you can use the Amazon AppFlow console to create the connector profile, and then use that connector profile in the flow creation CloudFormation template.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html
    :cloudformationResource: AWS::AppFlow::ConnectorProfile
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appflow as appflow
        
        cfn_connector_profile = appflow.CfnConnectorProfile(self, "MyCfnConnectorProfile",
            connection_mode="connectionMode",
            connector_profile_name="connectorProfileName",
            connector_type="connectorType",
        
            # the properties below are optional
            connector_label="connectorLabel",
            connector_profile_config=appflow.CfnConnectorProfile.ConnectorProfileConfigProperty(
                connector_profile_credentials=appflow.CfnConnectorProfile.ConnectorProfileCredentialsProperty(
                    amplitude=appflow.CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty(
                        api_key="apiKey",
                        secret_key="secretKey"
                    ),
                    custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfileCredentialsProperty(
                        authentication_type="authenticationType",
        
                        # the properties below are optional
                        api_key=appflow.CfnConnectorProfile.ApiKeyCredentialsProperty(
                            api_key="apiKey",
        
                            # the properties below are optional
                            api_secret_key="apiSecretKey"
                        ),
                        basic=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        custom=appflow.CfnConnectorProfile.CustomAuthCredentialsProperty(
                            custom_authentication_type="customAuthenticationType",
        
                            # the properties below are optional
                            credentials_map={
                                "credentials_map_key": "credentialsMap"
                            }
                        ),
                        oauth2=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                            access_token="accessToken",
                            client_id="clientId",
                            client_secret="clientSecret",
                            o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        )
                    ),
                    datadog=appflow.CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty(
                        api_key="apiKey",
                        application_key="applicationKey"
                    ),
                    dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty(
                        api_token="apiToken"
                    ),
                    google_analytics=appflow.CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
        
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    ),
                    infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty(
                        access_key_id="accessKeyId",
                        datakey="datakey",
                        secret_access_key="secretAccessKey",
                        user_id="userId"
                    ),
                    marketo=appflow.CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
        
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        )
                    ),
                    pardot=appflow.CfnConnectorProfile.PardotConnectorProfileCredentialsProperty(
                        access_token="accessToken",
                        client_credentials_arn="clientCredentialsArn",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    ),
                    redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty(
                        access_token="accessToken",
                        client_credentials_arn="clientCredentialsArn",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        jwt_token="jwtToken",
                        o_auth2_grant_type="oAuth2GrantType",
                        refresh_token="refreshToken"
                    ),
                    sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty(
                        basic_auth_credentials=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        o_auth_credentials=appflow.CfnConnectorProfile.OAuthCredentialsProperty(
                            access_token="accessToken",
                            client_id="clientId",
                            client_secret="clientSecret",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        )
                    ),
                    service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty(
                        o_auth2_credentials=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                            access_token="accessToken",
                            client_id="clientId",
                            client_secret="clientSecret",
                            o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        ),
                        password="password",
                        username="username"
                    ),
                    singular=appflow.CfnConnectorProfile.SingularConnectorProfileCredentialsProperty(
                        api_key="apiKey"
                    ),
                    slack=appflow.CfnConnectorProfile.SlackConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
        
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        )
                    ),
                    snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    trendmicro=appflow.CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty(
                        api_secret_key="apiSecretKey"
                    ),
                    veeva=appflow.CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
        
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        )
                    )
                ),
                connector_profile_properties=appflow.CfnConnectorProfile.ConnectorProfilePropertiesProperty(
                    custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfilePropertiesProperty(
                        o_auth2_properties=appflow.CfnConnectorProfile.OAuth2PropertiesProperty(
                            o_auth2_grant_type="oAuth2GrantType",
                            token_url="tokenUrl",
                            token_url_custom_properties={
                                "token_url_custom_properties_key": "tokenUrlCustomProperties"
                            }
                        ),
                        profile_properties={
                            "profile_properties_key": "profileProperties"
                        }
                    ),
                    datadog=appflow.CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    marketo=appflow.CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    pardot=appflow.CfnConnectorProfile.PardotConnectorProfilePropertiesProperty(
                        business_unit_id="businessUnitId",
        
                        # the properties below are optional
                        instance_url="instanceUrl",
                        is_sandbox_environment=False
                    ),
                    redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty(
                        bucket_name="bucketName",
                        role_arn="roleArn",
        
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        cluster_identifier="clusterIdentifier",
                        data_api_role_arn="dataApiRoleArn",
                        database_name="databaseName",
                        database_url="databaseUrl",
                        is_redshift_serverless=False,
                        workgroup_name="workgroupName"
                    ),
                    salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl",
                        is_sandbox_environment=False,
                        use_private_link_for_metadata_and_authorization=False
                    ),
                    sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty(
                        application_host_url="applicationHostUrl",
                        application_service_path="applicationServicePath",
                        client_number="clientNumber",
                        disable_sso=False,
                        logon_language="logonLanguage",
                        o_auth_properties=appflow.CfnConnectorProfile.OAuthPropertiesProperty(
                            auth_code_url="authCodeUrl",
                            o_auth_scopes=["oAuthScopes"],
                            token_url="tokenUrl"
                        ),
                        port_number=123,
                        private_link_service_name="privateLinkServiceName"
                    ),
                    service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    slack=appflow.CfnConnectorProfile.SlackConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty(
                        bucket_name="bucketName",
                        stage="stage",
                        warehouse="warehouse",
        
                        # the properties below are optional
                        account_name="accountName",
                        bucket_prefix="bucketPrefix",
                        private_link_service_name="privateLinkServiceName",
                        region="region"
                    ),
                    veeva=appflow.CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    )
                )
            ),
            kms_arn="kmsArn"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        connection_mode: builtins.str,
        connector_profile_name: builtins.str,
        connector_type: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        connector_profile_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorProfileConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param connection_mode: Indicates the connection mode and if it is public or private.
        :param connector_profile_name: The name of the connector profile. The name is unique for each ``ConnectorProfile`` in the AWS account .
        :param connector_type: The type of connector, such as Salesforce, Amplitude, and so on.
        :param connector_label: The label for the connector profile being created.
        :param connector_profile_config: Defines the connector-specific configuration and credentials.
        :param kms_arn: The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fdda7d6a6b65c327fe887afce3342c78cebf6c60dd8655f2dcd7b8281583efc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConnectorProfileProps(
            connection_mode=connection_mode,
            connector_profile_name=connector_profile_name,
            connector_type=connector_type,
            connector_label=connector_label,
            connector_profile_config=connector_profile_config,
            kms_arn=kms_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89b2a22e671284a42946f894ce72068c41b76bb904059c7bed5e45c71d48dc5a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b7b41f256b139e247bf8134c2dd0c80d99ca4ee9371e5685482e353a92d8e09a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrConnectorProfileArn")
    def attr_connector_profile_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connector profile.

        :cloudformationAttribute: ConnectorProfileArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrConnectorProfileArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCredentialsArn")
    def attr_credentials_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the connector profile credentials.

        :cloudformationAttribute: CredentialsArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCredentialsArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="connectionMode")
    def connection_mode(self) -> builtins.str:
        '''Indicates the connection mode and if it is public or private.'''
        return typing.cast(builtins.str, jsii.get(self, "connectionMode"))

    @connection_mode.setter
    def connection_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92b6f068ed3430ff60d5cf2405ae08acfe160b8a4162a018961ac832d027d84a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionMode", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProfileName")
    def connector_profile_name(self) -> builtins.str:
        '''The name of the connector profile.'''
        return typing.cast(builtins.str, jsii.get(self, "connectorProfileName"))

    @connector_profile_name.setter
    def connector_profile_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cb5b0aaad75445c153fba71fd8dbff5d452ea9073e2056f9b9b2deac384c665)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProfileName", value)

    @builtins.property
    @jsii.member(jsii_name="connectorType")
    def connector_type(self) -> builtins.str:
        '''The type of connector, such as Salesforce, Amplitude, and so on.'''
        return typing.cast(builtins.str, jsii.get(self, "connectorType"))

    @connector_type.setter
    def connector_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34d4fdd4dbf7a059cab33b55ce7b81ced574f12c8c437ab87f6a2cd0366b8c27)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorType", value)

    @builtins.property
    @jsii.member(jsii_name="connectorLabel")
    def connector_label(self) -> typing.Optional[builtins.str]:
        '''The label for the connector profile being created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectorLabel"))

    @connector_label.setter
    def connector_label(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__67b7946ef6d997ddf9c382bd294994647bbe3c0ad1aaaceece977af3d6112719)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorLabel", value)

    @builtins.property
    @jsii.member(jsii_name="connectorProfileConfig")
    def connector_profile_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfileConfigProperty"]]:
        '''Defines the connector-specific configuration and credentials.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfileConfigProperty"]], jsii.get(self, "connectorProfileConfig"))

    @connector_profile_config.setter
    def connector_profile_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfileConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3377e00c38f6ec97040c9514a9f9cedd23ba70e3a2b918fb7ef76f04aca7d060)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectorProfileConfig", value)

    @builtins.property
    @jsii.member(jsii_name="kmsArn")
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsArn"))

    @kms_arn.setter
    def kms_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__089ca49f64f5b669f9596470a2fc8cf66e307ab5bdaedd126556de9e245a2adf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsArn", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"api_key": "apiKey", "secret_key": "secretKey"},
    )
    class AmplitudeConnectorProfileCredentialsProperty:
        def __init__(self, *, api_key: builtins.str, secret_key: builtins.str) -> None:
            '''The connector-specific credentials required when using Amplitude.

            :param api_key: A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.
            :param secret_key: The Secret Access Key portion of the credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                amplitude_connector_profile_credentials_property = appflow.CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty(
                    api_key="apiKey",
                    secret_key="secretKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3d3ee1eed190e3c85bb2fe793fa526d58dcb1362575c8447aba2ded28e20cab)
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
                check_type(argname="argument secret_key", value=secret_key, expected_type=type_hints["secret_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_key": api_key,
                "secret_key": secret_key,
            }

        @builtins.property
        def api_key(self) -> builtins.str:
            '''A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-apikey
            '''
            result = self._values.get("api_key")
            assert result is not None, "Required property 'api_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_key(self) -> builtins.str:
            '''The Secret Access Key portion of the credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-amplitudeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-amplitudeconnectorprofilecredentials-secretkey
            '''
            result = self._values.get("secret_key")
            assert result is not None, "Required property 'secret_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmplitudeConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ApiKeyCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"api_key": "apiKey", "api_secret_key": "apiSecretKey"},
    )
    class ApiKeyCredentialsProperty:
        def __init__(
            self,
            *,
            api_key: builtins.str,
            api_secret_key: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The API key credentials required for API key authentication.

            :param api_key: The API key required for API key authentication.
            :param api_secret_key: The API secret key required for API key authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                api_key_credentials_property = appflow.CfnConnectorProfile.ApiKeyCredentialsProperty(
                    api_key="apiKey",
                
                    # the properties below are optional
                    api_secret_key="apiSecretKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7b690cee600d6640a4563f5c3e115b1108274292cca4da2ac3b8e3f9c054518c)
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
                check_type(argname="argument api_secret_key", value=api_secret_key, expected_type=type_hints["api_secret_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_key": api_key,
            }
            if api_secret_key is not None:
                self._values["api_secret_key"] = api_secret_key

        @builtins.property
        def api_key(self) -> builtins.str:
            '''The API key required for API key authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html#cfn-appflow-connectorprofile-apikeycredentials-apikey
            '''
            result = self._values.get("api_key")
            assert result is not None, "Required property 'api_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def api_secret_key(self) -> typing.Optional[builtins.str]:
            '''The API secret key required for API key authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-apikeycredentials.html#cfn-appflow-connectorprofile-apikeycredentials-apisecretkey
            '''
            result = self._values.get("api_secret_key")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiKeyCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.BasicAuthCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "username": "username"},
    )
    class BasicAuthCredentialsProperty:
        def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
            '''The basic auth credentials required for basic authentication.

            :param password: The password to use to connect to a resource.
            :param username: The username to use to connect to a resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                basic_auth_credentials_property = appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5d83b73c68f97257e00fd4a472b5060b923b19bf51a85eac98afa02a948b3f4)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }

        @builtins.property
        def password(self) -> builtins.str:
            '''The password to use to connect to a resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html#cfn-appflow-connectorprofile-basicauthcredentials-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The username to use to connect to a resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-basicauthcredentials.html#cfn-appflow-connectorprofile-basicauthcredentials-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BasicAuthCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty",
        jsii_struct_bases=[],
        name_mapping={"auth_code": "authCode", "redirect_uri": "redirectUri"},
    )
    class ConnectorOAuthRequestProperty:
        def __init__(
            self,
            *,
            auth_code: typing.Optional[builtins.str] = None,
            redirect_uri: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :param auth_code: The code provided by the connector when it has been authenticated via the connected app.
            :param redirect_uri: The URL to which the authentication server redirects the browser after authorization has been granted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                connector_oAuth_request_property = appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                    auth_code="authCode",
                    redirect_uri="redirectUri"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10274e31bef95217811425846919ad5f3013d939461f69d203d5222cb8a6c357)
                check_type(argname="argument auth_code", value=auth_code, expected_type=type_hints["auth_code"])
                check_type(argname="argument redirect_uri", value=redirect_uri, expected_type=type_hints["redirect_uri"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_code is not None:
                self._values["auth_code"] = auth_code
            if redirect_uri is not None:
                self._values["redirect_uri"] = redirect_uri

        @builtins.property
        def auth_code(self) -> typing.Optional[builtins.str]:
            '''The code provided by the connector when it has been authenticated via the connected app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html#cfn-appflow-connectorprofile-connectoroauthrequest-authcode
            '''
            result = self._values.get("auth_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def redirect_uri(self) -> typing.Optional[builtins.str]:
            '''The URL to which the authentication server redirects the browser after authorization has been granted.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectoroauthrequest.html#cfn-appflow-connectorprofile-connectoroauthrequest-redirecturi
            '''
            result = self._values.get("redirect_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorOAuthRequestProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ConnectorProfileConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_profile_credentials": "connectorProfileCredentials",
            "connector_profile_properties": "connectorProfileProperties",
        },
    )
    class ConnectorProfileConfigProperty:
        def __init__(
            self,
            *,
            connector_profile_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            connector_profile_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Defines the connector-specific configuration and credentials for the connector profile.

            :param connector_profile_credentials: The connector-specific credentials required by each connector.
            :param connector_profile_properties: The connector-specific properties of the profile configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                connector_profile_config_property = appflow.CfnConnectorProfile.ConnectorProfileConfigProperty(
                    connector_profile_credentials=appflow.CfnConnectorProfile.ConnectorProfileCredentialsProperty(
                        amplitude=appflow.CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty(
                            api_key="apiKey",
                            secret_key="secretKey"
                        ),
                        custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfileCredentialsProperty(
                            authentication_type="authenticationType",
                
                            # the properties below are optional
                            api_key=appflow.CfnConnectorProfile.ApiKeyCredentialsProperty(
                                api_key="apiKey",
                
                                # the properties below are optional
                                api_secret_key="apiSecretKey"
                            ),
                            basic=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                                password="password",
                                username="username"
                            ),
                            custom=appflow.CfnConnectorProfile.CustomAuthCredentialsProperty(
                                custom_authentication_type="customAuthenticationType",
                
                                # the properties below are optional
                                credentials_map={
                                    "credentials_map_key": "credentialsMap"
                                }
                            ),
                            oauth2=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                                access_token="accessToken",
                                client_id="clientId",
                                client_secret="clientSecret",
                                o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                    auth_code="authCode",
                                    redirect_uri="redirectUri"
                                ),
                                refresh_token="refreshToken"
                            )
                        ),
                        datadog=appflow.CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty(
                            api_key="apiKey",
                            application_key="applicationKey"
                        ),
                        dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty(
                            api_token="apiToken"
                        ),
                        google_analytics=appflow.CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        ),
                        infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty(
                            access_key_id="accessKeyId",
                            datakey="datakey",
                            secret_access_key="secretAccessKey",
                            user_id="userId"
                        ),
                        marketo=appflow.CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            )
                        ),
                        pardot=appflow.CfnConnectorProfile.PardotConnectorProfileCredentialsProperty(
                            access_token="accessToken",
                            client_credentials_arn="clientCredentialsArn",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        ),
                        redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty(
                            access_token="accessToken",
                            client_credentials_arn="clientCredentialsArn",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            jwt_token="jwtToken",
                            o_auth2_grant_type="oAuth2GrantType",
                            refresh_token="refreshToken"
                        ),
                        sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty(
                            basic_auth_credentials=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                                password="password",
                                username="username"
                            ),
                            o_auth_credentials=appflow.CfnConnectorProfile.OAuthCredentialsProperty(
                                access_token="accessToken",
                                client_id="clientId",
                                client_secret="clientSecret",
                                connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                    auth_code="authCode",
                                    redirect_uri="redirectUri"
                                ),
                                refresh_token="refreshToken"
                            )
                        ),
                        service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty(
                            o_auth2_credentials=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                                access_token="accessToken",
                                client_id="clientId",
                                client_secret="clientSecret",
                                o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                    auth_code="authCode",
                                    redirect_uri="redirectUri"
                                ),
                                refresh_token="refreshToken"
                            ),
                            password="password",
                            username="username"
                        ),
                        singular=appflow.CfnConnectorProfile.SingularConnectorProfileCredentialsProperty(
                            api_key="apiKey"
                        ),
                        slack=appflow.CfnConnectorProfile.SlackConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            )
                        ),
                        snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        trendmicro=appflow.CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty(
                            api_secret_key="apiSecretKey"
                        ),
                        veeva=appflow.CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
                
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            )
                        )
                    ),
                    connector_profile_properties=appflow.CfnConnectorProfile.ConnectorProfilePropertiesProperty(
                        custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfilePropertiesProperty(
                            o_auth2_properties=appflow.CfnConnectorProfile.OAuth2PropertiesProperty(
                                o_auth2_grant_type="oAuth2GrantType",
                                token_url="tokenUrl",
                                token_url_custom_properties={
                                    "token_url_custom_properties_key": "tokenUrlCustomProperties"
                                }
                            ),
                            profile_properties={
                                "profile_properties_key": "profileProperties"
                            }
                        ),
                        datadog=appflow.CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        marketo=appflow.CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        pardot=appflow.CfnConnectorProfile.PardotConnectorProfilePropertiesProperty(
                            business_unit_id="businessUnitId",
                
                            # the properties below are optional
                            instance_url="instanceUrl",
                            is_sandbox_environment=False
                        ),
                        redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty(
                            bucket_name="bucketName",
                            role_arn="roleArn",
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            cluster_identifier="clusterIdentifier",
                            data_api_role_arn="dataApiRoleArn",
                            database_name="databaseName",
                            database_url="databaseUrl",
                            is_redshift_serverless=False,
                            workgroup_name="workgroupName"
                        ),
                        salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl",
                            is_sandbox_environment=False,
                            use_private_link_for_metadata_and_authorization=False
                        ),
                        sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty(
                            application_host_url="applicationHostUrl",
                            application_service_path="applicationServicePath",
                            client_number="clientNumber",
                            disable_sso=False,
                            logon_language="logonLanguage",
                            o_auth_properties=appflow.CfnConnectorProfile.OAuthPropertiesProperty(
                                auth_code_url="authCodeUrl",
                                o_auth_scopes=["oAuthScopes"],
                                token_url="tokenUrl"
                            ),
                            port_number=123,
                            private_link_service_name="privateLinkServiceName"
                        ),
                        service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        slack=appflow.CfnConnectorProfile.SlackConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty(
                            bucket_name="bucketName",
                            stage="stage",
                            warehouse="warehouse",
                
                            # the properties below are optional
                            account_name="accountName",
                            bucket_prefix="bucketPrefix",
                            private_link_service_name="privateLinkServiceName",
                            region="region"
                        ),
                        veeva=appflow.CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c79f7beaf2ede6f336bef23f37f62a2315750767926008efbda3f98c15e34f73)
                check_type(argname="argument connector_profile_credentials", value=connector_profile_credentials, expected_type=type_hints["connector_profile_credentials"])
                check_type(argname="argument connector_profile_properties", value=connector_profile_properties, expected_type=type_hints["connector_profile_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if connector_profile_credentials is not None:
                self._values["connector_profile_credentials"] = connector_profile_credentials
            if connector_profile_properties is not None:
                self._values["connector_profile_properties"] = connector_profile_properties

        @builtins.property
        def connector_profile_credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required by each connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html#cfn-appflow-connectorprofile-connectorprofileconfig-connectorprofilecredentials
            '''
            result = self._values.get("connector_profile_credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def connector_profile_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties of the profile configuration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileconfig.html#cfn-appflow-connectorprofile-connectorprofileconfig-connectorprofileproperties
            '''
            result = self._values.get("connector_profile_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorProfilePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorProfileConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amplitude": "amplitude",
            "custom_connector": "customConnector",
            "datadog": "datadog",
            "dynatrace": "dynatrace",
            "google_analytics": "googleAnalytics",
            "infor_nexus": "inforNexus",
            "marketo": "marketo",
            "pardot": "pardot",
            "redshift": "redshift",
            "salesforce": "salesforce",
            "sapo_data": "sapoData",
            "service_now": "serviceNow",
            "singular": "singular",
            "slack": "slack",
            "snowflake": "snowflake",
            "trendmicro": "trendmicro",
            "veeva": "veeva",
            "zendesk": "zendesk",
        },
    )
    class ConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            amplitude: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.CustomConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            google_analytics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            infor_nexus: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pardot: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.PardotConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            singular: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SingularConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SlackConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trendmicro: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            veeva: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific credentials required by a connector.

            :param amplitude: The connector-specific credentials required when using Amplitude.
            :param custom_connector: The connector-specific profile credentials that are required when using the custom connector.
            :param datadog: The connector-specific credentials required when using Datadog.
            :param dynatrace: The connector-specific credentials required when using Dynatrace.
            :param google_analytics: The connector-specific credentials required when using Google Analytics.
            :param infor_nexus: The connector-specific credentials required when using Infor Nexus.
            :param marketo: The connector-specific credentials required when using Marketo.
            :param pardot: The connector-specific credentials required when using Salesforce Pardot.
            :param redshift: The connector-specific credentials required when using Amazon Redshift.
            :param salesforce: The connector-specific credentials required when using Salesforce.
            :param sapo_data: The connector-specific profile credentials required when using SAPOData.
            :param service_now: The connector-specific credentials required when using ServiceNow.
            :param singular: The connector-specific credentials required when using Singular.
            :param slack: The connector-specific credentials required when using Slack.
            :param snowflake: The connector-specific credentials required when using Snowflake.
            :param trendmicro: The connector-specific credentials required when using Trend Micro.
            :param veeva: The connector-specific credentials required when using Veeva.
            :param zendesk: The connector-specific credentials required when using Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                connector_profile_credentials_property = appflow.CfnConnectorProfile.ConnectorProfileCredentialsProperty(
                    amplitude=appflow.CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty(
                        api_key="apiKey",
                        secret_key="secretKey"
                    ),
                    custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfileCredentialsProperty(
                        authentication_type="authenticationType",
                
                        # the properties below are optional
                        api_key=appflow.CfnConnectorProfile.ApiKeyCredentialsProperty(
                            api_key="apiKey",
                
                            # the properties below are optional
                            api_secret_key="apiSecretKey"
                        ),
                        basic=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        custom=appflow.CfnConnectorProfile.CustomAuthCredentialsProperty(
                            custom_authentication_type="customAuthenticationType",
                
                            # the properties below are optional
                            credentials_map={
                                "credentials_map_key": "credentialsMap"
                            }
                        ),
                        oauth2=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                            access_token="accessToken",
                            client_id="clientId",
                            client_secret="clientSecret",
                            o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        )
                    ),
                    datadog=appflow.CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty(
                        api_key="apiKey",
                        application_key="applicationKey"
                    ),
                    dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty(
                        api_token="apiToken"
                    ),
                    google_analytics=appflow.CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    ),
                    infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty(
                        access_key_id="accessKeyId",
                        datakey="datakey",
                        secret_access_key="secretAccessKey",
                        user_id="userId"
                    ),
                    marketo=appflow.CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        )
                    ),
                    pardot=appflow.CfnConnectorProfile.PardotConnectorProfileCredentialsProperty(
                        access_token="accessToken",
                        client_credentials_arn="clientCredentialsArn",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    ),
                    redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty(
                        access_token="accessToken",
                        client_credentials_arn="clientCredentialsArn",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        jwt_token="jwtToken",
                        o_auth2_grant_type="oAuth2GrantType",
                        refresh_token="refreshToken"
                    ),
                    sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty(
                        basic_auth_credentials=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        o_auth_credentials=appflow.CfnConnectorProfile.OAuthCredentialsProperty(
                            access_token="accessToken",
                            client_id="clientId",
                            client_secret="clientSecret",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        )
                    ),
                    service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty(
                        o_auth2_credentials=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                            access_token="accessToken",
                            client_id="clientId",
                            client_secret="clientSecret",
                            o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        ),
                        password="password",
                        username="username"
                    ),
                    singular=appflow.CfnConnectorProfile.SingularConnectorProfileCredentialsProperty(
                        api_key="apiKey"
                    ),
                    slack=appflow.CfnConnectorProfile.SlackConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        )
                    ),
                    snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    trendmicro=appflow.CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty(
                        api_secret_key="apiSecretKey"
                    ),
                    veeva=appflow.CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty(
                        client_id="clientId",
                        client_secret="clientSecret",
                
                        # the properties below are optional
                        access_token="accessToken",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dd35c0b739bcd10a467238169b0d80e4d63f0277bdf37e945f3ea0bb11abbe59)
                check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
                check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
                check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
                check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument pardot", value=pardot, expected_type=type_hints["pardot"])
                check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
                check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
                check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
                check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
                check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amplitude is not None:
                self._values["amplitude"] = amplitude
            if custom_connector is not None:
                self._values["custom_connector"] = custom_connector
            if datadog is not None:
                self._values["datadog"] = datadog
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if google_analytics is not None:
                self._values["google_analytics"] = google_analytics
            if infor_nexus is not None:
                self._values["infor_nexus"] = infor_nexus
            if marketo is not None:
                self._values["marketo"] = marketo
            if pardot is not None:
                self._values["pardot"] = pardot
            if redshift is not None:
                self._values["redshift"] = redshift
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if sapo_data is not None:
                self._values["sapo_data"] = sapo_data
            if service_now is not None:
                self._values["service_now"] = service_now
            if singular is not None:
                self._values["singular"] = singular
            if slack is not None:
                self._values["slack"] = slack
            if snowflake is not None:
                self._values["snowflake"] = snowflake
            if trendmicro is not None:
                self._values["trendmicro"] = trendmicro
            if veeva is not None:
                self._values["veeva"] = veeva
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def amplitude(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Amplitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-amplitude
            '''
            result = self._values.get("amplitude")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def custom_connector(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.CustomConnectorProfileCredentialsProperty"]]:
            '''The connector-specific profile credentials that are required when using the custom connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-customconnector
            '''
            result = self._values.get("custom_connector")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.CustomConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def datadog(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Datadog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-datadog
            '''
            result = self._values.get("datadog")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def dynatrace(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Dynatrace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def google_analytics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Google Analytics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-googleanalytics
            '''
            result = self._values.get("google_analytics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def infor_nexus(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Infor Nexus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-infornexus
            '''
            result = self._values.get("infor_nexus")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Marketo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def pardot(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.PardotConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Salesforce Pardot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-pardot
            '''
            result = self._values.get("pardot")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.PardotConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def redshift(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-redshift
            '''
            result = self._values.get("redshift")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Salesforce.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def sapo_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty"]]:
            '''The connector-specific profile credentials required when using SAPOData.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-sapodata
            '''
            result = self._values.get("sapo_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using ServiceNow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def singular(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SingularConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Singular.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-singular
            '''
            result = self._values.get("singular")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SingularConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def slack(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SlackConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-slack
            '''
            result = self._values.get("slack")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SlackConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def snowflake(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-snowflake
            '''
            result = self._values.get("snowflake")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def trendmicro(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Trend Micro.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-trendmicro
            '''
            result = self._values.get("trendmicro")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def veeva(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Veeva.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-veeva
            '''
            result = self._values.get("veeva")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty"]]:
            '''The connector-specific credentials required when using Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofilecredentials.html#cfn-appflow-connectorprofile-connectorprofilecredentials-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_connector": "customConnector",
            "datadog": "datadog",
            "dynatrace": "dynatrace",
            "infor_nexus": "inforNexus",
            "marketo": "marketo",
            "pardot": "pardot",
            "redshift": "redshift",
            "salesforce": "salesforce",
            "sapo_data": "sapoData",
            "service_now": "serviceNow",
            "slack": "slack",
            "snowflake": "snowflake",
            "veeva": "veeva",
            "zendesk": "zendesk",
        },
    )
    class ConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.CustomConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            infor_nexus: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pardot: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.PardotConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SlackConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            veeva: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific profile properties required by each connector.

            :param custom_connector: The properties required by the custom connector.
            :param datadog: The connector-specific properties required by Datadog.
            :param dynatrace: The connector-specific properties required by Dynatrace.
            :param infor_nexus: The connector-specific properties required by Infor Nexus.
            :param marketo: The connector-specific properties required by Marketo.
            :param pardot: The connector-specific properties required by Salesforce Pardot.
            :param redshift: The connector-specific properties required by Amazon Redshift.
            :param salesforce: The connector-specific properties required by Salesforce.
            :param sapo_data: The connector-specific profile properties required when using SAPOData.
            :param service_now: The connector-specific properties required by serviceNow.
            :param slack: The connector-specific properties required by Slack.
            :param snowflake: The connector-specific properties required by Snowflake.
            :param veeva: The connector-specific properties required by Veeva.
            :param zendesk: The connector-specific properties required by Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                connector_profile_properties_property = appflow.CfnConnectorProfile.ConnectorProfilePropertiesProperty(
                    custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfilePropertiesProperty(
                        o_auth2_properties=appflow.CfnConnectorProfile.OAuth2PropertiesProperty(
                            o_auth2_grant_type="oAuth2GrantType",
                            token_url="tokenUrl",
                            token_url_custom_properties={
                                "token_url_custom_properties_key": "tokenUrlCustomProperties"
                            }
                        ),
                        profile_properties={
                            "profile_properties_key": "profileProperties"
                        }
                    ),
                    datadog=appflow.CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    marketo=appflow.CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    pardot=appflow.CfnConnectorProfile.PardotConnectorProfilePropertiesProperty(
                        business_unit_id="businessUnitId",
                
                        # the properties below are optional
                        instance_url="instanceUrl",
                        is_sandbox_environment=False
                    ),
                    redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty(
                        bucket_name="bucketName",
                        role_arn="roleArn",
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        cluster_identifier="clusterIdentifier",
                        data_api_role_arn="dataApiRoleArn",
                        database_name="databaseName",
                        database_url="databaseUrl",
                        is_redshift_serverless=False,
                        workgroup_name="workgroupName"
                    ),
                    salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl",
                        is_sandbox_environment=False,
                        use_private_link_for_metadata_and_authorization=False
                    ),
                    sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty(
                        application_host_url="applicationHostUrl",
                        application_service_path="applicationServicePath",
                        client_number="clientNumber",
                        disable_sso=False,
                        logon_language="logonLanguage",
                        o_auth_properties=appflow.CfnConnectorProfile.OAuthPropertiesProperty(
                            auth_code_url="authCodeUrl",
                            o_auth_scopes=["oAuthScopes"],
                            token_url="tokenUrl"
                        ),
                        port_number=123,
                        private_link_service_name="privateLinkServiceName"
                    ),
                    service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    slack=appflow.CfnConnectorProfile.SlackConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty(
                        bucket_name="bucketName",
                        stage="stage",
                        warehouse="warehouse",
                
                        # the properties below are optional
                        account_name="accountName",
                        bucket_prefix="bucketPrefix",
                        private_link_service_name="privateLinkServiceName",
                        region="region"
                    ),
                    veeva=appflow.CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    ),
                    zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty(
                        instance_url="instanceUrl"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__65e5865d49e1e2770f8833632ac69e47b3b029c81a4772e3b1c5426bdf879d4b)
                check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
                check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument pardot", value=pardot, expected_type=type_hints["pardot"])
                check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
                check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
                check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_connector is not None:
                self._values["custom_connector"] = custom_connector
            if datadog is not None:
                self._values["datadog"] = datadog
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if infor_nexus is not None:
                self._values["infor_nexus"] = infor_nexus
            if marketo is not None:
                self._values["marketo"] = marketo
            if pardot is not None:
                self._values["pardot"] = pardot
            if redshift is not None:
                self._values["redshift"] = redshift
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if sapo_data is not None:
                self._values["sapo_data"] = sapo_data
            if service_now is not None:
                self._values["service_now"] = service_now
            if slack is not None:
                self._values["slack"] = slack
            if snowflake is not None:
                self._values["snowflake"] = snowflake
            if veeva is not None:
                self._values["veeva"] = veeva
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def custom_connector(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.CustomConnectorProfilePropertiesProperty"]]:
            '''The properties required by the custom connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-customconnector
            '''
            result = self._values.get("custom_connector")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.CustomConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def datadog(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Datadog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-datadog
            '''
            result = self._values.get("datadog")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def dynatrace(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Dynatrace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def infor_nexus(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Infor Nexus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-infornexus
            '''
            result = self._values.get("infor_nexus")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Marketo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def pardot(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.PardotConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Salesforce Pardot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-pardot
            '''
            result = self._values.get("pardot")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.PardotConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def redshift(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-redshift
            '''
            result = self._values.get("redshift")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Salesforce.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def sapo_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty"]]:
            '''The connector-specific profile properties required when using SAPOData.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-sapodata
            '''
            result = self._values.get("sapo_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by serviceNow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def slack(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SlackConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-slack
            '''
            result = self._values.get("slack")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SlackConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def snowflake(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-snowflake
            '''
            result = self._values.get("snowflake")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def veeva(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Veeva.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-veeva
            '''
            result = self._values.get("veeva")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty"]]:
            '''The connector-specific properties required by Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-connectorprofileproperties.html#cfn-appflow-connectorprofile-connectorprofileproperties-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.CustomAuthCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_authentication_type": "customAuthenticationType",
            "credentials_map": "credentialsMap",
        },
    )
    class CustomAuthCredentialsProperty:
        def __init__(
            self,
            *,
            custom_authentication_type: builtins.str,
            credentials_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The custom credentials required for custom authentication.

            :param custom_authentication_type: The custom authentication type that the connector uses.
            :param credentials_map: A map that holds custom authentication credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                custom_auth_credentials_property = appflow.CfnConnectorProfile.CustomAuthCredentialsProperty(
                    custom_authentication_type="customAuthenticationType",
                
                    # the properties below are optional
                    credentials_map={
                        "credentials_map_key": "credentialsMap"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f1703eb3a58b3e6fd9b4a3833c2dc0fda48f2e43ba626529bc4a347a6d456e2)
                check_type(argname="argument custom_authentication_type", value=custom_authentication_type, expected_type=type_hints["custom_authentication_type"])
                check_type(argname="argument credentials_map", value=credentials_map, expected_type=type_hints["credentials_map"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "custom_authentication_type": custom_authentication_type,
            }
            if credentials_map is not None:
                self._values["credentials_map"] = credentials_map

        @builtins.property
        def custom_authentication_type(self) -> builtins.str:
            '''The custom authentication type that the connector uses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html#cfn-appflow-connectorprofile-customauthcredentials-customauthenticationtype
            '''
            result = self._values.get("custom_authentication_type")
            assert result is not None, "Required property 'custom_authentication_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def credentials_map(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A map that holds custom authentication credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customauthcredentials.html#cfn-appflow-connectorprofile-customauthcredentials-credentialsmap
            '''
            result = self._values.get("credentials_map")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomAuthCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.CustomConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authentication_type": "authenticationType",
            "api_key": "apiKey",
            "basic": "basic",
            "custom": "custom",
            "oauth2": "oauth2",
        },
    )
    class CustomConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            authentication_type: builtins.str,
            api_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ApiKeyCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            basic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.BasicAuthCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.CustomAuthCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            oauth2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.OAuth2CredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific profile credentials that are required when using the custom connector.

            :param authentication_type: The authentication type that the custom connector uses for authenticating while creating a connector profile.
            :param api_key: The API keys required for the authentication of the user.
            :param basic: The basic credentials that are required for the authentication of the user.
            :param custom: If the connector uses the custom authentication mechanism, this holds the required credentials.
            :param oauth2: The OAuth 2.0 credentials required for the authentication of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                custom_connector_profile_credentials_property = appflow.CfnConnectorProfile.CustomConnectorProfileCredentialsProperty(
                    authentication_type="authenticationType",
                
                    # the properties below are optional
                    api_key=appflow.CfnConnectorProfile.ApiKeyCredentialsProperty(
                        api_key="apiKey",
                
                        # the properties below are optional
                        api_secret_key="apiSecretKey"
                    ),
                    basic=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    custom=appflow.CfnConnectorProfile.CustomAuthCredentialsProperty(
                        custom_authentication_type="customAuthenticationType",
                
                        # the properties below are optional
                        credentials_map={
                            "credentials_map_key": "credentialsMap"
                        }
                    ),
                    oauth2=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                        access_token="accessToken",
                        client_id="clientId",
                        client_secret="clientSecret",
                        o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__706a9d527abbd20fd254cc98e3158ee9239289a3d14735ef9c32c2c9b41893ee)
                check_type(argname="argument authentication_type", value=authentication_type, expected_type=type_hints["authentication_type"])
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
                check_type(argname="argument basic", value=basic, expected_type=type_hints["basic"])
                check_type(argname="argument custom", value=custom, expected_type=type_hints["custom"])
                check_type(argname="argument oauth2", value=oauth2, expected_type=type_hints["oauth2"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "authentication_type": authentication_type,
            }
            if api_key is not None:
                self._values["api_key"] = api_key
            if basic is not None:
                self._values["basic"] = basic
            if custom is not None:
                self._values["custom"] = custom
            if oauth2 is not None:
                self._values["oauth2"] = oauth2

        @builtins.property
        def authentication_type(self) -> builtins.str:
            '''The authentication type that the custom connector uses for authenticating while creating a connector profile.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-authenticationtype
            '''
            result = self._values.get("authentication_type")
            assert result is not None, "Required property 'authentication_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def api_key(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ApiKeyCredentialsProperty"]]:
            '''The API keys required for the authentication of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-apikey
            '''
            result = self._values.get("api_key")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ApiKeyCredentialsProperty"]], result)

        @builtins.property
        def basic(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.BasicAuthCredentialsProperty"]]:
            '''The basic credentials that are required for the authentication of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-basic
            '''
            result = self._values.get("basic")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.BasicAuthCredentialsProperty"]], result)

        @builtins.property
        def custom(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.CustomAuthCredentialsProperty"]]:
            '''If the connector uses the custom authentication mechanism, this holds the required credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-custom
            '''
            result = self._values.get("custom")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.CustomAuthCredentialsProperty"]], result)

        @builtins.property
        def oauth2(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuth2CredentialsProperty"]]:
            '''The OAuth 2.0 credentials required for the authentication of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofilecredentials.html#cfn-appflow-connectorprofile-customconnectorprofilecredentials-oauth2
            '''
            result = self._values.get("oauth2")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuth2CredentialsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.CustomConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "o_auth2_properties": "oAuth2Properties",
            "profile_properties": "profileProperties",
        },
    )
    class CustomConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            o_auth2_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.OAuth2PropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            profile_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The profile properties required by the custom connector.

            :param o_auth2_properties: The OAuth 2.0 properties required for OAuth 2.0 authentication.
            :param profile_properties: A map of properties that are required to create a profile for the custom connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                custom_connector_profile_properties_property = appflow.CfnConnectorProfile.CustomConnectorProfilePropertiesProperty(
                    o_auth2_properties=appflow.CfnConnectorProfile.OAuth2PropertiesProperty(
                        o_auth2_grant_type="oAuth2GrantType",
                        token_url="tokenUrl",
                        token_url_custom_properties={
                            "token_url_custom_properties_key": "tokenUrlCustomProperties"
                        }
                    ),
                    profile_properties={
                        "profile_properties_key": "profileProperties"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cdb89c4d5019ae54344a6656863ce47417e2890bffc90e8167ec429bcb73d3b5)
                check_type(argname="argument o_auth2_properties", value=o_auth2_properties, expected_type=type_hints["o_auth2_properties"])
                check_type(argname="argument profile_properties", value=profile_properties, expected_type=type_hints["profile_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if o_auth2_properties is not None:
                self._values["o_auth2_properties"] = o_auth2_properties
            if profile_properties is not None:
                self._values["profile_properties"] = profile_properties

        @builtins.property
        def o_auth2_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuth2PropertiesProperty"]]:
            '''The OAuth 2.0 properties required for OAuth 2.0 authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html#cfn-appflow-connectorprofile-customconnectorprofileproperties-oauth2properties
            '''
            result = self._values.get("o_auth2_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuth2PropertiesProperty"]], result)

        @builtins.property
        def profile_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''A map of properties that are required to create a profile for the custom connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-customconnectorprofileproperties.html#cfn-appflow-connectorprofile-customconnectorprofileproperties-profileproperties
            '''
            result = self._values.get("profile_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"api_key": "apiKey", "application_key": "applicationKey"},
    )
    class DatadogConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            api_key: builtins.str,
            application_key: builtins.str,
        ) -> None:
            '''The connector-specific credentials required by Datadog.

            :param api_key: A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.
            :param application_key: Application keys, in conjunction with your API key, give you full access to Datadog’s programmatic API. Application keys are associated with the user account that created them. The application key is used to log all requests made to the API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                datadog_connector_profile_credentials_property = appflow.CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty(
                    api_key="apiKey",
                    application_key="applicationKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b5405a79a636a3a984fb01f6d21584050057edd8e02c32d2521ce746189892e2)
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
                check_type(argname="argument application_key", value=application_key, expected_type=type_hints["application_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_key": api_key,
                "application_key": application_key,
            }

        @builtins.property
        def api_key(self) -> builtins.str:
            '''A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-apikey
            '''
            result = self._values.get("api_key")
            assert result is not None, "Required property 'api_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def application_key(self) -> builtins.str:
            '''Application keys, in conjunction with your API key, give you full access to Datadog’s programmatic API.

            Application keys are associated with the user account that created them. The application key is used to log all requests made to the API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofilecredentials.html#cfn-appflow-connectorprofile-datadogconnectorprofilecredentials-applicationkey
            '''
            result = self._values.get("application_key")
            assert result is not None, "Required property 'application_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatadogConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class DatadogConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required by Datadog.

            :param instance_url: The location of the Datadog resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                datadog_connector_profile_properties_property = appflow.CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0659a9b67dc2853fedfdb11c94408d52cccb2ed20597bf42f6fb15b29415e87c)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Datadog resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-datadogconnectorprofileproperties.html#cfn-appflow-connectorprofile-datadogconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatadogConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"api_token": "apiToken"},
    )
    class DynatraceConnectorProfileCredentialsProperty:
        def __init__(self, *, api_token: builtins.str) -> None:
            '''The connector-specific profile credentials required by Dynatrace.

            :param api_token: The API tokens used by Dynatrace API to authenticate various API calls.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                dynatrace_connector_profile_credentials_property = appflow.CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty(
                    api_token="apiToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__020dbb7eb0377d6f0d6ff989b7f0dca2eac8bc5293fb8b927d656f980b21f044)
                check_type(argname="argument api_token", value=api_token, expected_type=type_hints["api_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_token": api_token,
            }

        @builtins.property
        def api_token(self) -> builtins.str:
            '''The API tokens used by Dynatrace API to authenticate various API calls.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-dynatraceconnectorprofilecredentials-apitoken
            '''
            result = self._values.get("api_token")
            assert result is not None, "Required property 'api_token' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynatraceConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class DynatraceConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required by Dynatrace.

            :param instance_url: The location of the Dynatrace resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                dynatrace_connector_profile_properties_property = appflow.CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29ed8163fe5b7ed49fedb68b059a96f0281b5f5f2c1bc08329d34386502b27b0)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Dynatrace resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-dynatraceconnectorprofileproperties.html#cfn-appflow-connectorprofile-dynatraceconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynatraceConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "access_token": "accessToken",
            "connector_o_auth_request": "connectorOAuthRequest",
            "refresh_token": "refreshToken",
        },
    )
    class GoogleAnalyticsConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            access_token: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            refresh_token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile credentials required by Google Analytics.

            :param client_id: The identifier for the desired client.
            :param client_secret: The client secret used by the OAuth client to authenticate to the authorization server.
            :param access_token: The credentials used to access protected Google Analytics resources.
            :param connector_o_auth_request: Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
            :param refresh_token: The credentials used to acquire new access tokens. This is required only for OAuth2 access tokens, and is not required for OAuth1 access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                google_analytics_connector_profile_credentials_property = appflow.CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                
                    # the properties below are optional
                    access_token="accessToken",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    ),
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f33ae7fdb815fdbe41d4a4e9dc65db0eaa088f28c686524272747ffdfa411dd)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
            }
            if access_token is not None:
                self._values["access_token"] = access_token
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request
            if refresh_token is not None:
                self._values["refresh_token"] = refresh_token

        @builtins.property
        def client_id(self) -> builtins.str:
            '''The identifier for the desired client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''The client secret used by the OAuth client to authenticate to the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to access protected Google Analytics resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        @builtins.property
        def refresh_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to acquire new access tokens.

            This is required only for OAuth2 access tokens, and is not required for OAuth1 access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials.html#cfn-appflow-connectorprofile-googleanalyticsconnectorprofilecredentials-refreshtoken
            '''
            result = self._values.get("refresh_token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GoogleAnalyticsConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_key_id": "accessKeyId",
            "datakey": "datakey",
            "secret_access_key": "secretAccessKey",
            "user_id": "userId",
        },
    )
    class InforNexusConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            access_key_id: builtins.str,
            datakey: builtins.str,
            secret_access_key: builtins.str,
            user_id: builtins.str,
        ) -> None:
            '''The connector-specific profile credentials required by Infor Nexus.

            :param access_key_id: The Access Key portion of the credentials.
            :param datakey: The encryption keys used to encrypt data.
            :param secret_access_key: The secret key used to sign requests.
            :param user_id: The identifier for the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                infor_nexus_connector_profile_credentials_property = appflow.CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty(
                    access_key_id="accessKeyId",
                    datakey="datakey",
                    secret_access_key="secretAccessKey",
                    user_id="userId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b0896c3f041be47a1346b6586c9961c6fddd408caca37ab78b69e2dbf3947b95)
                check_type(argname="argument access_key_id", value=access_key_id, expected_type=type_hints["access_key_id"])
                check_type(argname="argument datakey", value=datakey, expected_type=type_hints["datakey"])
                check_type(argname="argument secret_access_key", value=secret_access_key, expected_type=type_hints["secret_access_key"])
                check_type(argname="argument user_id", value=user_id, expected_type=type_hints["user_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "access_key_id": access_key_id,
                "datakey": datakey,
                "secret_access_key": secret_access_key,
                "user_id": user_id,
            }

        @builtins.property
        def access_key_id(self) -> builtins.str:
            '''The Access Key portion of the credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-accesskeyid
            '''
            result = self._values.get("access_key_id")
            assert result is not None, "Required property 'access_key_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def datakey(self) -> builtins.str:
            '''The encryption keys used to encrypt data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-datakey
            '''
            result = self._values.get("datakey")
            assert result is not None, "Required property 'datakey' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_access_key(self) -> builtins.str:
            '''The secret key used to sign requests.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-secretaccesskey
            '''
            result = self._values.get("secret_access_key")
            assert result is not None, "Required property 'secret_access_key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_id(self) -> builtins.str:
            '''The identifier for the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofilecredentials.html#cfn-appflow-connectorprofile-infornexusconnectorprofilecredentials-userid
            '''
            result = self._values.get("user_id")
            assert result is not None, "Required property 'user_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InforNexusConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class InforNexusConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required by Infor Nexus.

            :param instance_url: The location of the Infor Nexus resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                infor_nexus_connector_profile_properties_property = appflow.CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__121e8f6f0112eff36febf9235f6ad930186b1adfe295e513385c5ba69795c179)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Infor Nexus resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-infornexusconnectorprofileproperties.html#cfn-appflow-connectorprofile-infornexusconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InforNexusConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "access_token": "accessToken",
            "connector_o_auth_request": "connectorOAuthRequest",
        },
    )
    class MarketoConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            access_token: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific profile credentials required by Marketo.

            :param client_id: The identifier for the desired client.
            :param client_secret: The client secret used by the OAuth client to authenticate to the authorization server.
            :param access_token: The credentials used to access protected Marketo resources.
            :param connector_o_auth_request: Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                marketo_connector_profile_credentials_property = appflow.CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                
                    # the properties below are optional
                    access_token="accessToken",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__319f8014bd5324a2f4dc144886a8f0e7be1951f564c0fbd5badf8555b0d5263d)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
            }
            if access_token is not None:
                self._values["access_token"] = access_token
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request

        @builtins.property
        def client_id(self) -> builtins.str:
            '''The identifier for the desired client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''The client secret used by the OAuth client to authenticate to the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to access protected Marketo resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofilecredentials.html#cfn-appflow-connectorprofile-marketoconnectorprofilecredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class MarketoConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required when using Marketo.

            :param instance_url: The location of the Marketo resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                marketo_connector_profile_properties_property = appflow.CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__79733216203bc37d79a7396313a11957f92d7188cf5cc3a157352ceaa4b6202b)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Marketo resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-marketoconnectorprofileproperties.html#cfn-appflow-connectorprofile-marketoconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.OAuth2CredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_token": "accessToken",
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "o_auth_request": "oAuthRequest",
            "refresh_token": "refreshToken",
        },
    )
    class OAuth2CredentialsProperty:
        def __init__(
            self,
            *,
            access_token: typing.Optional[builtins.str] = None,
            client_id: typing.Optional[builtins.str] = None,
            client_secret: typing.Optional[builtins.str] = None,
            o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            refresh_token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The OAuth 2.0 credentials required for OAuth 2.0 authentication.

            :param access_token: The access token used to access the connector on your behalf.
            :param client_id: The identifier for the desired client.
            :param client_secret: The client secret used by the OAuth client to authenticate to the authorization server.
            :param o_auth_request: 
            :param refresh_token: The refresh token used to refresh an expired access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                o_auth2_credentials_property = appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                    access_token="accessToken",
                    client_id="clientId",
                    client_secret="clientSecret",
                    o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    ),
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b23a5882bc69b9efde3f028d1f4180011380cc10767444f52981ddf4ad39fa3)
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument o_auth_request", value=o_auth_request, expected_type=type_hints["o_auth_request"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_token is not None:
                self._values["access_token"] = access_token
            if client_id is not None:
                self._values["client_id"] = client_id
            if client_secret is not None:
                self._values["client_secret"] = client_secret
            if o_auth_request is not None:
                self._values["o_auth_request"] = o_auth_request
            if refresh_token is not None:
                self._values["refresh_token"] = refresh_token

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The access token used to access the connector on your behalf.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the desired client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-clientid
            '''
            result = self._values.get("client_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_secret(self) -> typing.Optional[builtins.str]:
            '''The client secret used by the OAuth client to authenticate to the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-clientsecret
            '''
            result = self._values.get("client_secret")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-oauthrequest
            '''
            result = self._values.get("o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        @builtins.property
        def refresh_token(self) -> typing.Optional[builtins.str]:
            '''The refresh token used to refresh an expired access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2credentials.html#cfn-appflow-connectorprofile-oauth2credentials-refreshtoken
            '''
            result = self._values.get("refresh_token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuth2CredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.OAuth2PropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "o_auth2_grant_type": "oAuth2GrantType",
            "token_url": "tokenUrl",
            "token_url_custom_properties": "tokenUrlCustomProperties",
        },
    )
    class OAuth2PropertiesProperty:
        def __init__(
            self,
            *,
            o_auth2_grant_type: typing.Optional[builtins.str] = None,
            token_url: typing.Optional[builtins.str] = None,
            token_url_custom_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        ) -> None:
            '''The OAuth 2.0 properties required for OAuth 2.0 authentication.

            :param o_auth2_grant_type: The OAuth 2.0 grant type used by connector for OAuth 2.0 authentication.
            :param token_url: The token URL required for OAuth 2.0 authentication.
            :param token_url_custom_properties: Associates your token URL with a map of properties that you define. Use this parameter to provide any additional details that the connector requires to authenticate your request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                o_auth2_properties_property = appflow.CfnConnectorProfile.OAuth2PropertiesProperty(
                    o_auth2_grant_type="oAuth2GrantType",
                    token_url="tokenUrl",
                    token_url_custom_properties={
                        "token_url_custom_properties_key": "tokenUrlCustomProperties"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__12b3508701004e181ac97abfefbe0c0e2c32f353cdc4077fc915d1e79059ded1)
                check_type(argname="argument o_auth2_grant_type", value=o_auth2_grant_type, expected_type=type_hints["o_auth2_grant_type"])
                check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
                check_type(argname="argument token_url_custom_properties", value=token_url_custom_properties, expected_type=type_hints["token_url_custom_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if o_auth2_grant_type is not None:
                self._values["o_auth2_grant_type"] = o_auth2_grant_type
            if token_url is not None:
                self._values["token_url"] = token_url
            if token_url_custom_properties is not None:
                self._values["token_url_custom_properties"] = token_url_custom_properties

        @builtins.property
        def o_auth2_grant_type(self) -> typing.Optional[builtins.str]:
            '''The OAuth 2.0 grant type used by connector for OAuth 2.0 authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html#cfn-appflow-connectorprofile-oauth2properties-oauth2granttype
            '''
            result = self._values.get("o_auth2_grant_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token_url(self) -> typing.Optional[builtins.str]:
            '''The token URL required for OAuth 2.0 authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html#cfn-appflow-connectorprofile-oauth2properties-tokenurl
            '''
            result = self._values.get("token_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def token_url_custom_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Associates your token URL with a map of properties that you define.

            Use this parameter to provide any additional details that the connector requires to authenticate your request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauth2properties.html#cfn-appflow-connectorprofile-oauth2properties-tokenurlcustomproperties
            '''
            result = self._values.get("token_url_custom_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuth2PropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.OAuthCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_token": "accessToken",
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "connector_o_auth_request": "connectorOAuthRequest",
            "refresh_token": "refreshToken",
        },
    )
    class OAuthCredentialsProperty:
        def __init__(
            self,
            *,
            access_token: typing.Optional[builtins.str] = None,
            client_id: typing.Optional[builtins.str] = None,
            client_secret: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            refresh_token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The OAuth credentials required for OAuth type authentication.

            :param access_token: The access token used to access protected SAPOData resources.
            :param client_id: The identifier for the desired client.
            :param client_secret: The client secret used by the OAuth client to authenticate to the authorization server.
            :param connector_o_auth_request: 
            :param refresh_token: The refresh token used to refresh expired access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                o_auth_credentials_property = appflow.CfnConnectorProfile.OAuthCredentialsProperty(
                    access_token="accessToken",
                    client_id="clientId",
                    client_secret="clientSecret",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    ),
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7da4be883f6a7b1d3ca824e7af71520a4dc18eb0c5c299a47adef3ced4c33b77)
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_token is not None:
                self._values["access_token"] = access_token
            if client_id is not None:
                self._values["client_id"] = client_id
            if client_secret is not None:
                self._values["client_secret"] = client_secret
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request
            if refresh_token is not None:
                self._values["refresh_token"] = refresh_token

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The access token used to access protected SAPOData resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_id(self) -> typing.Optional[builtins.str]:
            '''The identifier for the desired client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-clientid
            '''
            result = self._values.get("client_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_secret(self) -> typing.Optional[builtins.str]:
            '''The client secret used by the OAuth client to authenticate to the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-clientsecret
            '''
            result = self._values.get("client_secret")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        @builtins.property
        def refresh_token(self) -> typing.Optional[builtins.str]:
            '''The refresh token used to refresh expired access token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthcredentials.html#cfn-appflow-connectorprofile-oauthcredentials-refreshtoken
            '''
            result = self._values.get("refresh_token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuthCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.OAuthPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_code_url": "authCodeUrl",
            "o_auth_scopes": "oAuthScopes",
            "token_url": "tokenUrl",
        },
    )
    class OAuthPropertiesProperty:
        def __init__(
            self,
            *,
            auth_code_url: typing.Optional[builtins.str] = None,
            o_auth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            token_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The OAuth properties required for OAuth type authentication.

            :param auth_code_url: The authorization code url required to redirect to SAP Login Page to fetch authorization code for OAuth type authentication.
            :param o_auth_scopes: The OAuth scopes required for OAuth type authentication.
            :param token_url: The token url required to fetch access/refresh tokens using authorization code and also to refresh expired access token using refresh token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                o_auth_properties_property = appflow.CfnConnectorProfile.OAuthPropertiesProperty(
                    auth_code_url="authCodeUrl",
                    o_auth_scopes=["oAuthScopes"],
                    token_url="tokenUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__269c069da81422f6673236a4320be612c0558af7fe900035e4f46e91d169ce84)
                check_type(argname="argument auth_code_url", value=auth_code_url, expected_type=type_hints["auth_code_url"])
                check_type(argname="argument o_auth_scopes", value=o_auth_scopes, expected_type=type_hints["o_auth_scopes"])
                check_type(argname="argument token_url", value=token_url, expected_type=type_hints["token_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if auth_code_url is not None:
                self._values["auth_code_url"] = auth_code_url
            if o_auth_scopes is not None:
                self._values["o_auth_scopes"] = o_auth_scopes
            if token_url is not None:
                self._values["token_url"] = token_url

        @builtins.property
        def auth_code_url(self) -> typing.Optional[builtins.str]:
            '''The authorization code url required to redirect to SAP Login Page to fetch authorization code for OAuth type authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html#cfn-appflow-connectorprofile-oauthproperties-authcodeurl
            '''
            result = self._values.get("auth_code_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def o_auth_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The OAuth scopes required for OAuth type authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html#cfn-appflow-connectorprofile-oauthproperties-oauthscopes
            '''
            result = self._values.get("o_auth_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def token_url(self) -> typing.Optional[builtins.str]:
            '''The token url required to fetch access/refresh tokens using authorization code and also to refresh expired access token using refresh token.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-oauthproperties.html#cfn-appflow-connectorprofile-oauthproperties-tokenurl
            '''
            result = self._values.get("token_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "OAuthPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.PardotConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_token": "accessToken",
            "client_credentials_arn": "clientCredentialsArn",
            "connector_o_auth_request": "connectorOAuthRequest",
            "refresh_token": "refreshToken",
        },
    )
    class PardotConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            access_token: typing.Optional[builtins.str] = None,
            client_credentials_arn: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            refresh_token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using Salesforce Pardot.

            :param access_token: The credentials used to access protected Salesforce Pardot resources.
            :param client_credentials_arn: The secret manager ARN, which contains the client ID and client secret of the connected app.
            :param connector_o_auth_request: 
            :param refresh_token: The credentials used to acquire new access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                pardot_connector_profile_credentials_property = appflow.CfnConnectorProfile.PardotConnectorProfileCredentialsProperty(
                    access_token="accessToken",
                    client_credentials_arn="clientCredentialsArn",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    ),
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39a512cdf635aa9981165b275367a20430c45c0c4a601e102d0cdf5e10430e12)
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument client_credentials_arn", value=client_credentials_arn, expected_type=type_hints["client_credentials_arn"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_token is not None:
                self._values["access_token"] = access_token
            if client_credentials_arn is not None:
                self._values["client_credentials_arn"] = client_credentials_arn
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request
            if refresh_token is not None:
                self._values["refresh_token"] = refresh_token

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to access protected Salesforce Pardot resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_credentials_arn(self) -> typing.Optional[builtins.str]:
            '''The secret manager ARN, which contains the client ID and client secret of the connected app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-clientcredentialsarn
            '''
            result = self._values.get("client_credentials_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        @builtins.property
        def refresh_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to acquire new access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofilecredentials.html#cfn-appflow-connectorprofile-pardotconnectorprofilecredentials-refreshtoken
            '''
            result = self._values.get("refresh_token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PardotConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.PardotConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "business_unit_id": "businessUnitId",
            "instance_url": "instanceUrl",
            "is_sandbox_environment": "isSandboxEnvironment",
        },
    )
    class PardotConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            business_unit_id: builtins.str,
            instance_url: typing.Optional[builtins.str] = None,
            is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The connector-specific profile properties required when using Salesforce Pardot.

            :param business_unit_id: The business unit id of Salesforce Pardot instance.
            :param instance_url: The location of the Salesforce Pardot resource.
            :param is_sandbox_environment: Indicates whether the connector profile applies to a sandbox or production environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                pardot_connector_profile_properties_property = appflow.CfnConnectorProfile.PardotConnectorProfilePropertiesProperty(
                    business_unit_id="businessUnitId",
                
                    # the properties below are optional
                    instance_url="instanceUrl",
                    is_sandbox_environment=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a3e6a4fb1f0111e07cf857d2ee3ad46142f3b374d08c97bb704c89fa233cd47)
                check_type(argname="argument business_unit_id", value=business_unit_id, expected_type=type_hints["business_unit_id"])
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
                check_type(argname="argument is_sandbox_environment", value=is_sandbox_environment, expected_type=type_hints["is_sandbox_environment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "business_unit_id": business_unit_id,
            }
            if instance_url is not None:
                self._values["instance_url"] = instance_url
            if is_sandbox_environment is not None:
                self._values["is_sandbox_environment"] = is_sandbox_environment

        @builtins.property
        def business_unit_id(self) -> builtins.str:
            '''The business unit id of Salesforce Pardot instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-businessunitid
            '''
            result = self._values.get("business_unit_id")
            assert result is not None, "Required property 'business_unit_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def instance_url(self) -> typing.Optional[builtins.str]:
            '''The location of the Salesforce Pardot resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_sandbox_environment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the connector profile applies to a sandbox or production environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-pardotconnectorprofileproperties.html#cfn-appflow-connectorprofile-pardotconnectorprofileproperties-issandboxenvironment
            '''
            result = self._values.get("is_sandbox_environment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PardotConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "username": "username"},
    )
    class RedshiftConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            password: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using Amazon Redshift.

            :param password: The password that corresponds to the user name.
            :param username: The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                redshift_connector_profile_credentials_property = appflow.CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty(
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a07d7a6959f8151e74abf74abadc91dd5c9f7a16d911f5db0bc2f66e4f25e24)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if password is not None:
                self._values["password"] = password
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password that corresponds to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html#cfn-appflow-connectorprofile-redshiftconnectorprofilecredentials-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofilecredentials.html#cfn-appflow-connectorprofile-redshiftconnectorprofilecredentials-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "role_arn": "roleArn",
            "bucket_prefix": "bucketPrefix",
            "cluster_identifier": "clusterIdentifier",
            "data_api_role_arn": "dataApiRoleArn",
            "database_name": "databaseName",
            "database_url": "databaseUrl",
            "is_redshift_serverless": "isRedshiftServerless",
            "workgroup_name": "workgroupName",
        },
    )
    class RedshiftConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            role_arn: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            cluster_identifier: typing.Optional[builtins.str] = None,
            data_api_role_arn: typing.Optional[builtins.str] = None,
            database_name: typing.Optional[builtins.str] = None,
            database_url: typing.Optional[builtins.str] = None,
            is_redshift_serverless: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            workgroup_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile properties when using Amazon Redshift.

            :param bucket_name: A name for the associated Amazon S3 bucket.
            :param role_arn: The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3. For more information, and for the polices that you attach to this role, see `Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3 <https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3>`_ .
            :param bucket_prefix: The object key for the destination bucket in which Amazon AppFlow places the files.
            :param cluster_identifier: The unique ID that's assigned to an Amazon Redshift cluster.
            :param data_api_role_arn: The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API. For more information, and for the polices that you attach to this role, see `Allow Amazon AppFlow to access Amazon Redshift databases with the Data API <https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift>`_ .
            :param database_name: The name of an Amazon Redshift database.
            :param database_url: The JDBC URL of the Amazon Redshift cluster.
            :param is_redshift_serverless: Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.
            :param workgroup_name: The name of an Amazon Redshift workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                redshift_connector_profile_properties_property = appflow.CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty(
                    bucket_name="bucketName",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    cluster_identifier="clusterIdentifier",
                    data_api_role_arn="dataApiRoleArn",
                    database_name="databaseName",
                    database_url="databaseUrl",
                    is_redshift_serverless=False,
                    workgroup_name="workgroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b095f01640a40304a0331c41ae7ab321ae12f0c106bbb47ef402aac9840f90f7)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument cluster_identifier", value=cluster_identifier, expected_type=type_hints["cluster_identifier"])
                check_type(argname="argument data_api_role_arn", value=data_api_role_arn, expected_type=type_hints["data_api_role_arn"])
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument database_url", value=database_url, expected_type=type_hints["database_url"])
                check_type(argname="argument is_redshift_serverless", value=is_redshift_serverless, expected_type=type_hints["is_redshift_serverless"])
                check_type(argname="argument workgroup_name", value=workgroup_name, expected_type=type_hints["workgroup_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "role_arn": role_arn,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if cluster_identifier is not None:
                self._values["cluster_identifier"] = cluster_identifier
            if data_api_role_arn is not None:
                self._values["data_api_role_arn"] = data_api_role_arn
            if database_name is not None:
                self._values["database_name"] = database_name
            if database_url is not None:
                self._values["database_url"] = database_url
            if is_redshift_serverless is not None:
                self._values["is_redshift_serverless"] = is_redshift_serverless
            if workgroup_name is not None:
                self._values["workgroup_name"] = workgroup_name

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''A name for the associated Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3.

            For more information, and for the polices that you attach to this role, see `Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3 <https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the destination bucket in which Amazon AppFlow places the files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cluster_identifier(self) -> typing.Optional[builtins.str]:
            '''The unique ID that's assigned to an Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-clusteridentifier
            '''
            result = self._values.get("cluster_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def data_api_role_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API.

            For more information, and for the polices that you attach to this role, see `Allow Amazon AppFlow to access Amazon Redshift databases with the Data API <https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-dataapirolearn
            '''
            result = self._values.get("data_api_role_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_name(self) -> typing.Optional[builtins.str]:
            '''The name of an Amazon Redshift database.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databasename
            '''
            result = self._values.get("database_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def database_url(self) -> typing.Optional[builtins.str]:
            '''The JDBC URL of the Amazon Redshift cluster.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-databaseurl
            '''
            result = self._values.get("database_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_redshift_serverless(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-isredshiftserverless
            '''
            result = self._values.get("is_redshift_serverless")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def workgroup_name(self) -> typing.Optional[builtins.str]:
            '''The name of an Amazon Redshift workgroup.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-redshiftconnectorprofileproperties.html#cfn-appflow-connectorprofile-redshiftconnectorprofileproperties-workgroupname
            '''
            result = self._values.get("workgroup_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "basic_auth_credentials": "basicAuthCredentials",
            "o_auth_credentials": "oAuthCredentials",
        },
    )
    class SAPODataConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            basic_auth_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.BasicAuthCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            o_auth_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.OAuthCredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using SAPOData.

            :param basic_auth_credentials: The SAPOData basic authentication credentials.
            :param o_auth_credentials: The SAPOData OAuth type authentication credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s_aPOData_connector_profile_credentials_property = appflow.CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty(
                    basic_auth_credentials=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                        password="password",
                        username="username"
                    ),
                    o_auth_credentials=appflow.CfnConnectorProfile.OAuthCredentialsProperty(
                        access_token="accessToken",
                        client_id="clientId",
                        client_secret="clientSecret",
                        connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e721304f58add999e91a5094b626deadf6f42ca2e0e3744b0e313380bc540b00)
                check_type(argname="argument basic_auth_credentials", value=basic_auth_credentials, expected_type=type_hints["basic_auth_credentials"])
                check_type(argname="argument o_auth_credentials", value=o_auth_credentials, expected_type=type_hints["o_auth_credentials"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if basic_auth_credentials is not None:
                self._values["basic_auth_credentials"] = basic_auth_credentials
            if o_auth_credentials is not None:
                self._values["o_auth_credentials"] = o_auth_credentials

        @builtins.property
        def basic_auth_credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.BasicAuthCredentialsProperty"]]:
            '''The SAPOData basic authentication credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-basicauthcredentials
            '''
            result = self._values.get("basic_auth_credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.BasicAuthCredentialsProperty"]], result)

        @builtins.property
        def o_auth_credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuthCredentialsProperty"]]:
            '''The SAPOData OAuth type authentication credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofilecredentials.html#cfn-appflow-connectorprofile-sapodataconnectorprofilecredentials-oauthcredentials
            '''
            result = self._values.get("o_auth_credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuthCredentialsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAPODataConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_host_url": "applicationHostUrl",
            "application_service_path": "applicationServicePath",
            "client_number": "clientNumber",
            "disable_sso": "disableSso",
            "logon_language": "logonLanguage",
            "o_auth_properties": "oAuthProperties",
            "port_number": "portNumber",
            "private_link_service_name": "privateLinkServiceName",
        },
    )
    class SAPODataConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            application_host_url: typing.Optional[builtins.str] = None,
            application_service_path: typing.Optional[builtins.str] = None,
            client_number: typing.Optional[builtins.str] = None,
            disable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            logon_language: typing.Optional[builtins.str] = None,
            o_auth_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.OAuthPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            port_number: typing.Optional[jsii.Number] = None,
            private_link_service_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile properties required when using SAPOData.

            :param application_host_url: The location of the SAPOData resource.
            :param application_service_path: The application path to catalog service.
            :param client_number: The client number for the client creating the connection.
            :param disable_sso: If you set this parameter to true, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.
            :param logon_language: The logon language of SAPOData instance.
            :param o_auth_properties: The SAPOData OAuth properties required for OAuth type authentication.
            :param port_number: The port number of the SAPOData instance.
            :param private_link_service_name: The SAPOData Private Link service name to be used for private data transfers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s_aPOData_connector_profile_properties_property = appflow.CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty(
                    application_host_url="applicationHostUrl",
                    application_service_path="applicationServicePath",
                    client_number="clientNumber",
                    disable_sso=False,
                    logon_language="logonLanguage",
                    o_auth_properties=appflow.CfnConnectorProfile.OAuthPropertiesProperty(
                        auth_code_url="authCodeUrl",
                        o_auth_scopes=["oAuthScopes"],
                        token_url="tokenUrl"
                    ),
                    port_number=123,
                    private_link_service_name="privateLinkServiceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fa0bde147a80d4f5be2e3a0a92803dcbc8bf7a7949aaf97c980a8be44a261244)
                check_type(argname="argument application_host_url", value=application_host_url, expected_type=type_hints["application_host_url"])
                check_type(argname="argument application_service_path", value=application_service_path, expected_type=type_hints["application_service_path"])
                check_type(argname="argument client_number", value=client_number, expected_type=type_hints["client_number"])
                check_type(argname="argument disable_sso", value=disable_sso, expected_type=type_hints["disable_sso"])
                check_type(argname="argument logon_language", value=logon_language, expected_type=type_hints["logon_language"])
                check_type(argname="argument o_auth_properties", value=o_auth_properties, expected_type=type_hints["o_auth_properties"])
                check_type(argname="argument port_number", value=port_number, expected_type=type_hints["port_number"])
                check_type(argname="argument private_link_service_name", value=private_link_service_name, expected_type=type_hints["private_link_service_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if application_host_url is not None:
                self._values["application_host_url"] = application_host_url
            if application_service_path is not None:
                self._values["application_service_path"] = application_service_path
            if client_number is not None:
                self._values["client_number"] = client_number
            if disable_sso is not None:
                self._values["disable_sso"] = disable_sso
            if logon_language is not None:
                self._values["logon_language"] = logon_language
            if o_auth_properties is not None:
                self._values["o_auth_properties"] = o_auth_properties
            if port_number is not None:
                self._values["port_number"] = port_number
            if private_link_service_name is not None:
                self._values["private_link_service_name"] = private_link_service_name

        @builtins.property
        def application_host_url(self) -> typing.Optional[builtins.str]:
            '''The location of the SAPOData resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationhosturl
            '''
            result = self._values.get("application_host_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def application_service_path(self) -> typing.Optional[builtins.str]:
            '''The application path to catalog service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-applicationservicepath
            '''
            result = self._values.get("application_service_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_number(self) -> typing.Optional[builtins.str]:
            '''The client number for the client creating the connection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-clientnumber
            '''
            result = self._values.get("client_number")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def disable_sso(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If you set this parameter to true, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-disablesso
            '''
            result = self._values.get("disable_sso")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def logon_language(self) -> typing.Optional[builtins.str]:
            '''The logon language of SAPOData instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-logonlanguage
            '''
            result = self._values.get("logon_language")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def o_auth_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuthPropertiesProperty"]]:
            '''The SAPOData OAuth properties required for OAuth type authentication.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-oauthproperties
            '''
            result = self._values.get("o_auth_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuthPropertiesProperty"]], result)

        @builtins.property
        def port_number(self) -> typing.Optional[jsii.Number]:
            '''The port number of the SAPOData instance.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-portnumber
            '''
            result = self._values.get("port_number")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def private_link_service_name(self) -> typing.Optional[builtins.str]:
            '''The SAPOData Private Link service name to be used for private data transfers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-sapodataconnectorprofileproperties.html#cfn-appflow-connectorprofile-sapodataconnectorprofileproperties-privatelinkservicename
            '''
            result = self._values.get("private_link_service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAPODataConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_token": "accessToken",
            "client_credentials_arn": "clientCredentialsArn",
            "connector_o_auth_request": "connectorOAuthRequest",
            "jwt_token": "jwtToken",
            "o_auth2_grant_type": "oAuth2GrantType",
            "refresh_token": "refreshToken",
        },
    )
    class SalesforceConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            access_token: typing.Optional[builtins.str] = None,
            client_credentials_arn: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            jwt_token: typing.Optional[builtins.str] = None,
            o_auth2_grant_type: typing.Optional[builtins.str] = None,
            refresh_token: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using Salesforce.

            :param access_token: The credentials used to access protected Salesforce resources.
            :param client_credentials_arn: The secret manager ARN, which contains the client ID and client secret of the connected app.
            :param connector_o_auth_request: Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.
            :param jwt_token: A JSON web token (JWT) that authorizes Amazon AppFlow to access your Salesforce records.
            :param o_auth2_grant_type: Specifies the OAuth 2.0 grant type that Amazon AppFlow uses when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records. You can specify one of the following values: - **AUTHORIZATION_CODE** - Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records. - **CLIENT_CREDENTIALS** - Amazon AppFlow passes client credentials (a client ID and client secret) when it requests the access token from Salesforce. You provide these credentials to Amazon AppFlow when you define the connection to your Salesforce account. - **JWT_BEARER** - Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.
            :param refresh_token: The credentials used to acquire new access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                salesforce_connector_profile_credentials_property = appflow.CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty(
                    access_token="accessToken",
                    client_credentials_arn="clientCredentialsArn",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    ),
                    jwt_token="jwtToken",
                    o_auth2_grant_type="oAuth2GrantType",
                    refresh_token="refreshToken"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96f1396ecd411968fa6dcd8be1e9a9cbc6d0f02f80c0d4e9acc547f44564e4cb)
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument client_credentials_arn", value=client_credentials_arn, expected_type=type_hints["client_credentials_arn"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
                check_type(argname="argument jwt_token", value=jwt_token, expected_type=type_hints["jwt_token"])
                check_type(argname="argument o_auth2_grant_type", value=o_auth2_grant_type, expected_type=type_hints["o_auth2_grant_type"])
                check_type(argname="argument refresh_token", value=refresh_token, expected_type=type_hints["refresh_token"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_token is not None:
                self._values["access_token"] = access_token
            if client_credentials_arn is not None:
                self._values["client_credentials_arn"] = client_credentials_arn
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request
            if jwt_token is not None:
                self._values["jwt_token"] = jwt_token
            if o_auth2_grant_type is not None:
                self._values["o_auth2_grant_type"] = o_auth2_grant_type
            if refresh_token is not None:
                self._values["refresh_token"] = refresh_token

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to access protected Salesforce resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def client_credentials_arn(self) -> typing.Optional[builtins.str]:
            '''The secret manager ARN, which contains the client ID and client secret of the connected app.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-clientcredentialsarn
            '''
            result = self._values.get("client_credentials_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        @builtins.property
        def jwt_token(self) -> typing.Optional[builtins.str]:
            '''A JSON web token (JWT) that authorizes Amazon AppFlow to access your Salesforce records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-jwttoken
            '''
            result = self._values.get("jwt_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def o_auth2_grant_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the OAuth 2.0 grant type that Amazon AppFlow uses when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.

            You can specify one of the following values:

            - **AUTHORIZATION_CODE** - Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.
            - **CLIENT_CREDENTIALS** - Amazon AppFlow passes client credentials (a client ID and client secret) when it requests the access token from Salesforce. You provide these credentials to Amazon AppFlow when you define the connection to your Salesforce account.
            - **JWT_BEARER** - Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you don't need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-oauth2granttype
            '''
            result = self._values.get("o_auth2_grant_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def refresh_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to acquire new access tokens.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofilecredentials.html#cfn-appflow-connectorprofile-salesforceconnectorprofilecredentials-refreshtoken
            '''
            result = self._values.get("refresh_token")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_url": "instanceUrl",
            "is_sandbox_environment": "isSandboxEnvironment",
            "use_private_link_for_metadata_and_authorization": "usePrivateLinkForMetadataAndAuthorization",
        },
    )
    class SalesforceConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            instance_url: typing.Optional[builtins.str] = None,
            is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_private_link_for_metadata_and_authorization: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The connector-specific profile properties required when using Salesforce.

            :param instance_url: The location of the Salesforce resource.
            :param is_sandbox_environment: Indicates whether the connector profile applies to a sandbox or production environment.
            :param use_private_link_for_metadata_and_authorization: If the connection mode for the connector profile is private, this parameter sets whether Amazon AppFlow uses the private network to send metadata and authorization calls to Salesforce. Amazon AppFlow sends private calls through AWS PrivateLink . These calls travel through AWS infrastructure without being exposed to the public internet. Set either of the following values: - **true** - Amazon AppFlow sends all calls to Salesforce over the private network. These private calls are: - Calls to get metadata about your Salesforce records. This metadata describes your Salesforce objects and their fields. - Calls to get or refresh access tokens that allow Amazon AppFlow to access your Salesforce records. - Calls to transfer your Salesforce records as part of a flow run. - **false** - The default value. Amazon AppFlow sends some calls to Salesforce privately and other calls over the public internet. The public calls are: - Calls to get metadata about your Salesforce records. - Calls to get or refresh access tokens. The private calls are: - Calls to transfer your Salesforce records as part of a flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                salesforce_connector_profile_properties_property = appflow.CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl",
                    is_sandbox_environment=False,
                    use_private_link_for_metadata_and_authorization=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e02155b4dbffca160c7213611f0f005432320f081cac130c77c180517e637a2f)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
                check_type(argname="argument is_sandbox_environment", value=is_sandbox_environment, expected_type=type_hints["is_sandbox_environment"])
                check_type(argname="argument use_private_link_for_metadata_and_authorization", value=use_private_link_for_metadata_and_authorization, expected_type=type_hints["use_private_link_for_metadata_and_authorization"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if instance_url is not None:
                self._values["instance_url"] = instance_url
            if is_sandbox_environment is not None:
                self._values["is_sandbox_environment"] = is_sandbox_environment
            if use_private_link_for_metadata_and_authorization is not None:
                self._values["use_private_link_for_metadata_and_authorization"] = use_private_link_for_metadata_and_authorization

        @builtins.property
        def instance_url(self) -> typing.Optional[builtins.str]:
            '''The location of the Salesforce resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html#cfn-appflow-connectorprofile-salesforceconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def is_sandbox_environment(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether the connector profile applies to a sandbox or production environment.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html#cfn-appflow-connectorprofile-salesforceconnectorprofileproperties-issandboxenvironment
            '''
            result = self._values.get("is_sandbox_environment")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_private_link_for_metadata_and_authorization(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If the connection mode for the connector profile is private, this parameter sets whether Amazon AppFlow uses the private network to send metadata and authorization calls to Salesforce.

            Amazon AppFlow sends private calls through AWS PrivateLink . These calls travel through AWS infrastructure without being exposed to the public internet.

            Set either of the following values:

            - **true** - Amazon AppFlow sends all calls to Salesforce over the private network.

            These private calls are:

            - Calls to get metadata about your Salesforce records. This metadata describes your Salesforce objects and their fields.
            - Calls to get or refresh access tokens that allow Amazon AppFlow to access your Salesforce records.
            - Calls to transfer your Salesforce records as part of a flow run.
            - **false** - The default value. Amazon AppFlow sends some calls to Salesforce privately and other calls over the public internet.

            The public calls are:

            - Calls to get metadata about your Salesforce records.
            - Calls to get or refresh access tokens.

            The private calls are:

            - Calls to transfer your Salesforce records as part of a flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-salesforceconnectorprofileproperties.html#cfn-appflow-connectorprofile-salesforceconnectorprofileproperties-useprivatelinkformetadataandauthorization
            '''
            result = self._values.get("use_private_link_for_metadata_and_authorization")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "o_auth2_credentials": "oAuth2Credentials",
            "password": "password",
            "username": "username",
        },
    )
    class ServiceNowConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            o_auth2_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.OAuth2CredentialsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            password: typing.Optional[builtins.str] = None,
            username: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using ServiceNow.

            :param o_auth2_credentials: 
            :param password: The password that corresponds to the user name.
            :param username: The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                service_now_connector_profile_credentials_property = appflow.CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty(
                    o_auth2_credentials=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                        access_token="accessToken",
                        client_id="clientId",
                        client_secret="clientSecret",
                        o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                            auth_code="authCode",
                            redirect_uri="redirectUri"
                        ),
                        refresh_token="refreshToken"
                    ),
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9300511337a4bb1851f11ae6d27ff1f49d05843818e90659f8938653677148dc)
                check_type(argname="argument o_auth2_credentials", value=o_auth2_credentials, expected_type=type_hints["o_auth2_credentials"])
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if o_auth2_credentials is not None:
                self._values["o_auth2_credentials"] = o_auth2_credentials
            if password is not None:
                self._values["password"] = password
            if username is not None:
                self._values["username"] = username

        @builtins.property
        def o_auth2_credentials(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuth2CredentialsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-oauth2credentials
            '''
            result = self._values.get("o_auth2_credentials")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.OAuth2CredentialsProperty"]], result)

        @builtins.property
        def password(self) -> typing.Optional[builtins.str]:
            '''The password that corresponds to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-password
            '''
            result = self._values.get("password")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def username(self) -> typing.Optional[builtins.str]:
            '''The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofilecredentials.html#cfn-appflow-connectorprofile-servicenowconnectorprofilecredentials-username
            '''
            result = self._values.get("username")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class ServiceNowConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required when using ServiceNow.

            :param instance_url: The location of the ServiceNow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                service_now_connector_profile_properties_property = appflow.CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__efce9f1c1c228e65efb350a33320672ebf6907ec78b01471e88a2f3115b49969)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the ServiceNow resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-servicenowconnectorprofileproperties.html#cfn-appflow-connectorprofile-servicenowconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SingularConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"api_key": "apiKey"},
    )
    class SingularConnectorProfileCredentialsProperty:
        def __init__(self, *, api_key: builtins.str) -> None:
            '''The connector-specific profile credentials required when using Singular.

            :param api_key: A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                singular_connector_profile_credentials_property = appflow.CfnConnectorProfile.SingularConnectorProfileCredentialsProperty(
                    api_key="apiKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bc42a25a4870da865c4d31df2ea94435f79afd8cd9830a7292d2927bd728c89)
                check_type(argname="argument api_key", value=api_key, expected_type=type_hints["api_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_key": api_key,
            }

        @builtins.property
        def api_key(self) -> builtins.str:
            '''A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-singularconnectorprofilecredentials.html#cfn-appflow-connectorprofile-singularconnectorprofilecredentials-apikey
            '''
            result = self._values.get("api_key")
            assert result is not None, "Required property 'api_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingularConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SlackConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "access_token": "accessToken",
            "connector_o_auth_request": "connectorOAuthRequest",
        },
    )
    class SlackConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            access_token: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using Slack.

            :param client_id: The identifier for the client.
            :param client_secret: The client secret used by the OAuth client to authenticate to the authorization server.
            :param access_token: The credentials used to access protected Slack resources.
            :param connector_o_auth_request: Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                slack_connector_profile_credentials_property = appflow.CfnConnectorProfile.SlackConnectorProfileCredentialsProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                
                    # the properties below are optional
                    access_token="accessToken",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33f7d201cd92c3241e76eeef7aa8154f9c19884178d71dfffea8c0db939343da)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
            }
            if access_token is not None:
                self._values["access_token"] = access_token
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request

        @builtins.property
        def client_id(self) -> builtins.str:
            '''The identifier for the client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''The client secret used by the OAuth client to authenticate to the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to access protected Slack resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofilecredentials.html#cfn-appflow-connectorprofile-slackconnectorprofilecredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlackConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SlackConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class SlackConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required when using Slack.

            :param instance_url: The location of the Slack resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                slack_connector_profile_properties_property = appflow.CfnConnectorProfile.SlackConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7fa78e2f74e28f73bdd0a0a5b4498cd51ac364dea787eb69eca7836013e38578)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Slack resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-slackconnectorprofileproperties.html#cfn-appflow-connectorprofile-slackconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlackConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "username": "username"},
    )
    class SnowflakeConnectorProfileCredentialsProperty:
        def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
            '''The connector-specific profile credentials required when using Snowflake.

            :param password: The password that corresponds to the user name.
            :param username: The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                snowflake_connector_profile_credentials_property = appflow.CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty(
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__78ab8cbf4a57bfd8e44a5e9c1239be3df998e064aa70bc8d688ee7b7448d6b85)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }

        @builtins.property
        def password(self) -> builtins.str:
            '''The password that corresponds to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-snowflakeconnectorprofilecredentials-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofilecredentials.html#cfn-appflow-connectorprofile-snowflakeconnectorprofilecredentials-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "stage": "stage",
            "warehouse": "warehouse",
            "account_name": "accountName",
            "bucket_prefix": "bucketPrefix",
            "private_link_service_name": "privateLinkServiceName",
            "region": "region",
        },
    )
    class SnowflakeConnectorProfilePropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            stage: builtins.str,
            warehouse: builtins.str,
            account_name: typing.Optional[builtins.str] = None,
            bucket_prefix: typing.Optional[builtins.str] = None,
            private_link_service_name: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The connector-specific profile properties required when using Snowflake.

            :param bucket_name: The name of the Amazon S3 bucket associated with Snowflake.
            :param stage: The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the Snowflake account. This is written in the following format: < Database>< Schema>.
            :param warehouse: The name of the Snowflake warehouse.
            :param account_name: The name of the account.
            :param bucket_prefix: The bucket path that refers to the Amazon S3 bucket associated with Snowflake.
            :param private_link_service_name: The Snowflake Private Link service name to be used for private data transfers.
            :param region: The AWS Region of the Snowflake account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                snowflake_connector_profile_properties_property = appflow.CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty(
                    bucket_name="bucketName",
                    stage="stage",
                    warehouse="warehouse",
                
                    # the properties below are optional
                    account_name="accountName",
                    bucket_prefix="bucketPrefix",
                    private_link_service_name="privateLinkServiceName",
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b4f80ae6d0ba98546835743a752b0ca92f9ee74d525a2d9048e10cb2e431bef1)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
                check_type(argname="argument warehouse", value=warehouse, expected_type=type_hints["warehouse"])
                check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument private_link_service_name", value=private_link_service_name, expected_type=type_hints["private_link_service_name"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "stage": stage,
                "warehouse": warehouse,
            }
            if account_name is not None:
                self._values["account_name"] = account_name
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if private_link_service_name is not None:
                self._values["private_link_service_name"] = private_link_service_name
            if region is not None:
                self._values["region"] = region

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the Amazon S3 bucket associated with Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stage(self) -> builtins.str:
            '''The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the Snowflake account.

            This is written in the following format: < Database>< Schema>.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-stage
            '''
            result = self._values.get("stage")
            assert result is not None, "Required property 'stage' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def warehouse(self) -> builtins.str:
            '''The name of the Snowflake warehouse.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-warehouse
            '''
            result = self._values.get("warehouse")
            assert result is not None, "Required property 'warehouse' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def account_name(self) -> typing.Optional[builtins.str]:
            '''The name of the account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-accountname
            '''
            result = self._values.get("account_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The bucket path that refers to the Amazon S3 bucket associated with Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def private_link_service_name(self) -> typing.Optional[builtins.str]:
            '''The Snowflake Private Link service name to be used for private data transfers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-privatelinkservicename
            '''
            result = self._values.get("private_link_service_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region of the Snowflake account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-snowflakeconnectorprofileproperties.html#cfn-appflow-connectorprofile-snowflakeconnectorprofileproperties-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"api_secret_key": "apiSecretKey"},
    )
    class TrendmicroConnectorProfileCredentialsProperty:
        def __init__(self, *, api_secret_key: builtins.str) -> None:
            '''The connector-specific profile credentials required when using Trend Micro.

            :param api_secret_key: The Secret Access Key portion of the credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                trendmicro_connector_profile_credentials_property = appflow.CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty(
                    api_secret_key="apiSecretKey"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f95a9d334e1f47f62231dbcb8790eabf066eadb9f788be0eade7c40e427fbfd)
                check_type(argname="argument api_secret_key", value=api_secret_key, expected_type=type_hints["api_secret_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "api_secret_key": api_secret_key,
            }

        @builtins.property
        def api_secret_key(self) -> builtins.str:
            '''The Secret Access Key portion of the credentials.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-trendmicroconnectorprofilecredentials.html#cfn-appflow-connectorprofile-trendmicroconnectorprofilecredentials-apisecretkey
            '''
            result = self._values.get("api_secret_key")
            assert result is not None, "Required property 'api_secret_key' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrendmicroConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={"password": "password", "username": "username"},
    )
    class VeevaConnectorProfileCredentialsProperty:
        def __init__(self, *, password: builtins.str, username: builtins.str) -> None:
            '''The connector-specific profile credentials required when using Veeva.

            :param password: The password that corresponds to the user name.
            :param username: The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                veeva_connector_profile_credentials_property = appflow.CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty(
                    password="password",
                    username="username"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8f8ef2a02ea3e3deaf9f4972c986d189157161d79719d8e6cc32bc591af0417d)
                check_type(argname="argument password", value=password, expected_type=type_hints["password"])
                check_type(argname="argument username", value=username, expected_type=type_hints["username"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "password": password,
                "username": username,
            }

        @builtins.property
        def password(self) -> builtins.str:
            '''The password that corresponds to the user name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-password
            '''
            result = self._values.get("password")
            assert result is not None, "Required property 'password' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def username(self) -> builtins.str:
            '''The name of the user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofilecredentials.html#cfn-appflow-connectorprofile-veevaconnectorprofilecredentials-username
            '''
            result = self._values.get("username")
            assert result is not None, "Required property 'username' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VeevaConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class VeevaConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required when using Veeva.

            :param instance_url: The location of the Veeva resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                veeva_connector_profile_properties_property = appflow.CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2bcf7976bdceaf015e653ef6a1d5de1fe1a0bac8d7acc3bacd57ea35f47af45d)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Veeva resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-veevaconnectorprofileproperties.html#cfn-appflow-connectorprofile-veevaconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VeevaConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "client_id": "clientId",
            "client_secret": "clientSecret",
            "access_token": "accessToken",
            "connector_o_auth_request": "connectorOAuthRequest",
        },
    )
    class ZendeskConnectorProfileCredentialsProperty:
        def __init__(
            self,
            *,
            client_id: builtins.str,
            client_secret: builtins.str,
            access_token: typing.Optional[builtins.str] = None,
            connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConnectorProfile.ConnectorOAuthRequestProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The connector-specific profile credentials required when using Zendesk.

            :param client_id: The identifier for the desired client.
            :param client_secret: The client secret used by the OAuth client to authenticate to the authorization server.
            :param access_token: The credentials used to access protected Zendesk resources.
            :param connector_o_auth_request: Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                zendesk_connector_profile_credentials_property = appflow.CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty(
                    client_id="clientId",
                    client_secret="clientSecret",
                
                    # the properties below are optional
                    access_token="accessToken",
                    connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                        auth_code="authCode",
                        redirect_uri="redirectUri"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__23cdb025a23f9fe29cc4cc49eb6c3c171c1c23d9f0bf22702b88df0eb1e9b477)
                check_type(argname="argument client_id", value=client_id, expected_type=type_hints["client_id"])
                check_type(argname="argument client_secret", value=client_secret, expected_type=type_hints["client_secret"])
                check_type(argname="argument access_token", value=access_token, expected_type=type_hints["access_token"])
                check_type(argname="argument connector_o_auth_request", value=connector_o_auth_request, expected_type=type_hints["connector_o_auth_request"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "client_id": client_id,
                "client_secret": client_secret,
            }
            if access_token is not None:
                self._values["access_token"] = access_token
            if connector_o_auth_request is not None:
                self._values["connector_o_auth_request"] = connector_o_auth_request

        @builtins.property
        def client_id(self) -> builtins.str:
            '''The identifier for the desired client.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-clientid
            '''
            result = self._values.get("client_id")
            assert result is not None, "Required property 'client_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def client_secret(self) -> builtins.str:
            '''The client secret used by the OAuth client to authenticate to the authorization server.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-clientsecret
            '''
            result = self._values.get("client_secret")
            assert result is not None, "Required property 'client_secret' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def access_token(self) -> typing.Optional[builtins.str]:
            '''The credentials used to access protected Zendesk resources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-accesstoken
            '''
            result = self._values.get("access_token")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_o_auth_request(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]]:
            '''Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofilecredentials.html#cfn-appflow-connectorprofile-zendeskconnectorprofilecredentials-connectoroauthrequest
            '''
            result = self._values.get("connector_o_auth_request")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConnectorProfile.ConnectorOAuthRequestProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskConnectorProfileCredentialsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"instance_url": "instanceUrl"},
    )
    class ZendeskConnectorProfilePropertiesProperty:
        def __init__(self, *, instance_url: builtins.str) -> None:
            '''The connector-specific profile properties required when using Zendesk.

            :param instance_url: The location of the Zendesk resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofileproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                zendesk_connector_profile_properties_property = appflow.CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty(
                    instance_url="instanceUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__deb62e66d965f0e26ff87d16ee4c48a202e9421055030e74ae433cbf772a681a)
                check_type(argname="argument instance_url", value=instance_url, expected_type=type_hints["instance_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_url": instance_url,
            }

        @builtins.property
        def instance_url(self) -> builtins.str:
            '''The location of the Zendesk resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-connectorprofile-zendeskconnectorprofileproperties.html#cfn-appflow-connectorprofile-zendeskconnectorprofileproperties-instanceurl
            '''
            result = self._values.get("instance_url")
            assert result is not None, "Required property 'instance_url' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskConnectorProfilePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProfileProps",
    jsii_struct_bases=[],
    name_mapping={
        "connection_mode": "connectionMode",
        "connector_profile_name": "connectorProfileName",
        "connector_type": "connectorType",
        "connector_label": "connectorLabel",
        "connector_profile_config": "connectorProfileConfig",
        "kms_arn": "kmsArn",
    },
)
class CfnConnectorProfileProps:
    def __init__(
        self,
        *,
        connection_mode: builtins.str,
        connector_profile_name: builtins.str,
        connector_type: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        connector_profile_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorProfileConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        kms_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnectorProfile``.

        :param connection_mode: Indicates the connection mode and if it is public or private.
        :param connector_profile_name: The name of the connector profile. The name is unique for each ``ConnectorProfile`` in the AWS account .
        :param connector_type: The type of connector, such as Salesforce, Amplitude, and so on.
        :param connector_label: The label for the connector profile being created.
        :param connector_profile_config: Defines the connector-specific configuration and credentials.
        :param kms_arn: The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appflow as appflow
            
            cfn_connector_profile_props = appflow.CfnConnectorProfileProps(
                connection_mode="connectionMode",
                connector_profile_name="connectorProfileName",
                connector_type="connectorType",
            
                # the properties below are optional
                connector_label="connectorLabel",
                connector_profile_config=appflow.CfnConnectorProfile.ConnectorProfileConfigProperty(
                    connector_profile_credentials=appflow.CfnConnectorProfile.ConnectorProfileCredentialsProperty(
                        amplitude=appflow.CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty(
                            api_key="apiKey",
                            secret_key="secretKey"
                        ),
                        custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfileCredentialsProperty(
                            authentication_type="authenticationType",
            
                            # the properties below are optional
                            api_key=appflow.CfnConnectorProfile.ApiKeyCredentialsProperty(
                                api_key="apiKey",
            
                                # the properties below are optional
                                api_secret_key="apiSecretKey"
                            ),
                            basic=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                                password="password",
                                username="username"
                            ),
                            custom=appflow.CfnConnectorProfile.CustomAuthCredentialsProperty(
                                custom_authentication_type="customAuthenticationType",
            
                                # the properties below are optional
                                credentials_map={
                                    "credentials_map_key": "credentialsMap"
                                }
                            ),
                            oauth2=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                                access_token="accessToken",
                                client_id="clientId",
                                client_secret="clientSecret",
                                o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                    auth_code="authCode",
                                    redirect_uri="redirectUri"
                                ),
                                refresh_token="refreshToken"
                            )
                        ),
                        datadog=appflow.CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty(
                            api_key="apiKey",
                            application_key="applicationKey"
                        ),
                        dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty(
                            api_token="apiToken"
                        ),
                        google_analytics=appflow.CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
            
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        ),
                        infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty(
                            access_key_id="accessKeyId",
                            datakey="datakey",
                            secret_access_key="secretAccessKey",
                            user_id="userId"
                        ),
                        marketo=appflow.CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
            
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            )
                        ),
                        pardot=appflow.CfnConnectorProfile.PardotConnectorProfileCredentialsProperty(
                            access_token="accessToken",
                            client_credentials_arn="clientCredentialsArn",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            refresh_token="refreshToken"
                        ),
                        redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty(
                            access_token="accessToken",
                            client_credentials_arn="clientCredentialsArn",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            ),
                            jwt_token="jwtToken",
                            o_auth2_grant_type="oAuth2GrantType",
                            refresh_token="refreshToken"
                        ),
                        sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty(
                            basic_auth_credentials=appflow.CfnConnectorProfile.BasicAuthCredentialsProperty(
                                password="password",
                                username="username"
                            ),
                            o_auth_credentials=appflow.CfnConnectorProfile.OAuthCredentialsProperty(
                                access_token="accessToken",
                                client_id="clientId",
                                client_secret="clientSecret",
                                connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                    auth_code="authCode",
                                    redirect_uri="redirectUri"
                                ),
                                refresh_token="refreshToken"
                            )
                        ),
                        service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty(
                            o_auth2_credentials=appflow.CfnConnectorProfile.OAuth2CredentialsProperty(
                                access_token="accessToken",
                                client_id="clientId",
                                client_secret="clientSecret",
                                o_auth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                    auth_code="authCode",
                                    redirect_uri="redirectUri"
                                ),
                                refresh_token="refreshToken"
                            ),
                            password="password",
                            username="username"
                        ),
                        singular=appflow.CfnConnectorProfile.SingularConnectorProfileCredentialsProperty(
                            api_key="apiKey"
                        ),
                        slack=appflow.CfnConnectorProfile.SlackConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
            
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            )
                        ),
                        snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        trendmicro=appflow.CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty(
                            api_secret_key="apiSecretKey"
                        ),
                        veeva=appflow.CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty(
                            password="password",
                            username="username"
                        ),
                        zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty(
                            client_id="clientId",
                            client_secret="clientSecret",
            
                            # the properties below are optional
                            access_token="accessToken",
                            connector_oAuth_request=appflow.CfnConnectorProfile.ConnectorOAuthRequestProperty(
                                auth_code="authCode",
                                redirect_uri="redirectUri"
                            )
                        )
                    ),
                    connector_profile_properties=appflow.CfnConnectorProfile.ConnectorProfilePropertiesProperty(
                        custom_connector=appflow.CfnConnectorProfile.CustomConnectorProfilePropertiesProperty(
                            o_auth2_properties=appflow.CfnConnectorProfile.OAuth2PropertiesProperty(
                                o_auth2_grant_type="oAuth2GrantType",
                                token_url="tokenUrl",
                                token_url_custom_properties={
                                    "token_url_custom_properties_key": "tokenUrlCustomProperties"
                                }
                            ),
                            profile_properties={
                                "profile_properties_key": "profileProperties"
                            }
                        ),
                        datadog=appflow.CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        dynatrace=appflow.CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        infor_nexus=appflow.CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        marketo=appflow.CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        pardot=appflow.CfnConnectorProfile.PardotConnectorProfilePropertiesProperty(
                            business_unit_id="businessUnitId",
            
                            # the properties below are optional
                            instance_url="instanceUrl",
                            is_sandbox_environment=False
                        ),
                        redshift=appflow.CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty(
                            bucket_name="bucketName",
                            role_arn="roleArn",
            
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            cluster_identifier="clusterIdentifier",
                            data_api_role_arn="dataApiRoleArn",
                            database_name="databaseName",
                            database_url="databaseUrl",
                            is_redshift_serverless=False,
                            workgroup_name="workgroupName"
                        ),
                        salesforce=appflow.CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl",
                            is_sandbox_environment=False,
                            use_private_link_for_metadata_and_authorization=False
                        ),
                        sapo_data=appflow.CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty(
                            application_host_url="applicationHostUrl",
                            application_service_path="applicationServicePath",
                            client_number="clientNumber",
                            disable_sso=False,
                            logon_language="logonLanguage",
                            o_auth_properties=appflow.CfnConnectorProfile.OAuthPropertiesProperty(
                                auth_code_url="authCodeUrl",
                                o_auth_scopes=["oAuthScopes"],
                                token_url="tokenUrl"
                            ),
                            port_number=123,
                            private_link_service_name="privateLinkServiceName"
                        ),
                        service_now=appflow.CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        slack=appflow.CfnConnectorProfile.SlackConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        snowflake=appflow.CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty(
                            bucket_name="bucketName",
                            stage="stage",
                            warehouse="warehouse",
            
                            # the properties below are optional
                            account_name="accountName",
                            bucket_prefix="bucketPrefix",
                            private_link_service_name="privateLinkServiceName",
                            region="region"
                        ),
                        veeva=appflow.CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        ),
                        zendesk=appflow.CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty(
                            instance_url="instanceUrl"
                        )
                    )
                ),
                kms_arn="kmsArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__032712d85c2f8c1992ce0b706fc9b7992da5970e1c4b25cc48b86d35fbf104bb)
            check_type(argname="argument connection_mode", value=connection_mode, expected_type=type_hints["connection_mode"])
            check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
            check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
            check_type(argname="argument connector_label", value=connector_label, expected_type=type_hints["connector_label"])
            check_type(argname="argument connector_profile_config", value=connector_profile_config, expected_type=type_hints["connector_profile_config"])
            check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connection_mode": connection_mode,
            "connector_profile_name": connector_profile_name,
            "connector_type": connector_type,
        }
        if connector_label is not None:
            self._values["connector_label"] = connector_label
        if connector_profile_config is not None:
            self._values["connector_profile_config"] = connector_profile_config
        if kms_arn is not None:
            self._values["kms_arn"] = kms_arn

    @builtins.property
    def connection_mode(self) -> builtins.str:
        '''Indicates the connection mode and if it is public or private.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectionmode
        '''
        result = self._values.get("connection_mode")
        assert result is not None, "Required property 'connection_mode' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_profile_name(self) -> builtins.str:
        '''The name of the connector profile.

        The name is unique for each ``ConnectorProfile`` in the AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofilename
        '''
        result = self._values.get("connector_profile_name")
        assert result is not None, "Required property 'connector_profile_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_type(self) -> builtins.str:
        '''The type of connector, such as Salesforce, Amplitude, and so on.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectortype
        '''
        result = self._values.get("connector_type")
        assert result is not None, "Required property 'connector_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_label(self) -> typing.Optional[builtins.str]:
        '''The label for the connector profile being created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorlabel
        '''
        result = self._values.get("connector_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connector_profile_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectorProfile.ConnectorProfileConfigProperty]]:
        '''Defines the connector-specific configuration and credentials.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-connectorprofileconfig
        '''
        result = self._values.get("connector_profile_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectorProfile.ConnectorProfileConfigProperty]], result)

    @builtins.property
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption.

        This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connectorprofile.html#cfn-appflow-connectorprofile-kmsarn
        '''
        result = self._values.get("kms_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProfileProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appflow.CfnConnectorProps",
    jsii_struct_bases=[],
    name_mapping={
        "connector_provisioning_config": "connectorProvisioningConfig",
        "connector_provisioning_type": "connectorProvisioningType",
        "connector_label": "connectorLabel",
        "description": "description",
    },
)
class CfnConnectorProps:
    def __init__(
        self,
        *,
        connector_provisioning_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ConnectorProvisioningConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        connector_provisioning_type: builtins.str,
        connector_label: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnConnector``.

        :param connector_provisioning_config: The configuration required for registering the connector.
        :param connector_provisioning_type: The provisioning type used to register the connector.
        :param connector_label: The label used for registering the connector.
        :param description: A description about the connector runtime setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appflow as appflow
            
            cfn_connector_props = appflow.CfnConnectorProps(
                connector_provisioning_config=appflow.CfnConnector.ConnectorProvisioningConfigProperty(
                    lambda_=appflow.CfnConnector.LambdaConnectorProvisioningConfigProperty(
                        lambda_arn="lambdaArn"
                    )
                ),
                connector_provisioning_type="connectorProvisioningType",
            
                # the properties below are optional
                connector_label="connectorLabel",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__204ab8f1f508d34470db08010b45b65c1aa7d47e66c5fb91f90cdeb633b5eb9b)
            check_type(argname="argument connector_provisioning_config", value=connector_provisioning_config, expected_type=type_hints["connector_provisioning_config"])
            check_type(argname="argument connector_provisioning_type", value=connector_provisioning_type, expected_type=type_hints["connector_provisioning_type"])
            check_type(argname="argument connector_label", value=connector_label, expected_type=type_hints["connector_label"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "connector_provisioning_config": connector_provisioning_config,
            "connector_provisioning_type": connector_provisioning_type,
        }
        if connector_label is not None:
            self._values["connector_label"] = connector_label
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def connector_provisioning_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConnector.ConnectorProvisioningConfigProperty]:
        '''The configuration required for registering the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-connectorprovisioningconfig
        '''
        result = self._values.get("connector_provisioning_config")
        assert result is not None, "Required property 'connector_provisioning_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConnector.ConnectorProvisioningConfigProperty], result)

    @builtins.property
    def connector_provisioning_type(self) -> builtins.str:
        '''The provisioning type used to register the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-connectorprovisioningtype
        '''
        result = self._values.get("connector_provisioning_type")
        assert result is not None, "Required property 'connector_provisioning_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connector_label(self) -> typing.Optional[builtins.str]:
        '''The label used for registering the connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-connectorlabel
        '''
        result = self._values.get("connector_label")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description about the connector runtime setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-connector.html#cfn-appflow-connector-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConnectorProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFlow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_appflow.CfnFlow",
):
    '''The ``AWS::AppFlow::Flow`` resource is an Amazon AppFlow resource type that specifies a new flow.

    .. epigraph::

       If you want to use AWS CloudFormation to create a connector profile for connectors that implement OAuth (such as Salesforce, Slack, Zendesk, and Google Analytics), you must fetch the access and refresh tokens. You can do this by implementing your own UI for OAuth, or by retrieving the tokens from elsewhere. Alternatively, you can use the Amazon AppFlow console to create the connector profile, and then use that connector profile in the flow creation CloudFormation template.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html
    :cloudformationResource: AWS::AppFlow::Flow
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_appflow as appflow
        
        cfn_flow = appflow.CfnFlow(self, "MyCfnFlow",
            destination_flow_config_list=[appflow.CfnFlow.DestinationFlowConfigProperty(
                connector_type="connectorType",
                destination_connector_properties=appflow.CfnFlow.DestinationConnectorPropertiesProperty(
                    custom_connector=appflow.CfnFlow.CustomConnectorDestinationPropertiesProperty(
                        entity_name="entityName",
        
                        # the properties below are optional
                        custom_properties={
                            "custom_properties_key": "customProperties"
                        },
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        write_operation_type="writeOperationType"
                    ),
                    event_bridge=appflow.CfnFlow.EventBridgeDestinationPropertiesProperty(
                        object="object",
        
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    lookout_metrics=appflow.CfnFlow.LookoutMetricsDestinationPropertiesProperty(
                        object="object"
                    ),
                    marketo=appflow.CfnFlow.MarketoDestinationPropertiesProperty(
                        object="object",
        
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    redshift=appflow.CfnFlow.RedshiftDestinationPropertiesProperty(
                        intermediate_bucket_name="intermediateBucketName",
                        object="object",
        
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    s3=appflow.CfnFlow.S3DestinationPropertiesProperty(
                        bucket_name="bucketName",
        
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        s3_output_format_config=appflow.CfnFlow.S3OutputFormatConfigProperty(
                            aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                aggregation_type="aggregationType",
                                target_file_size=123
                            ),
                            file_type="fileType",
                            prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                path_prefix_hierarchy=["pathPrefixHierarchy"],
                                prefix_format="prefixFormat",
                                prefix_type="prefixType"
                            ),
                            preserve_source_data_typing=False
                        )
                    ),
                    salesforce=appflow.CfnFlow.SalesforceDestinationPropertiesProperty(
                        object="object",
        
                        # the properties below are optional
                        data_transfer_api="dataTransferApi",
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        write_operation_type="writeOperationType"
                    ),
                    sapo_data=appflow.CfnFlow.SAPODataDestinationPropertiesProperty(
                        object_path="objectPath",
        
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        success_response_handling_config=appflow.CfnFlow.SuccessResponseHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix"
                        ),
                        write_operation_type="writeOperationType"
                    ),
                    snowflake=appflow.CfnFlow.SnowflakeDestinationPropertiesProperty(
                        intermediate_bucket_name="intermediateBucketName",
                        object="object",
        
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    upsolver=appflow.CfnFlow.UpsolverDestinationPropertiesProperty(
                        bucket_name="bucketName",
                        s3_output_format_config=appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty(
                            prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                path_prefix_hierarchy=["pathPrefixHierarchy"],
                                prefix_format="prefixFormat",
                                prefix_type="prefixType"
                            ),
        
                            # the properties below are optional
                            aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                aggregation_type="aggregationType",
                                target_file_size=123
                            ),
                            file_type="fileType"
                        ),
        
                        # the properties below are optional
                        bucket_prefix="bucketPrefix"
                    ),
                    zendesk=appflow.CfnFlow.ZendeskDestinationPropertiesProperty(
                        object="object",
        
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        write_operation_type="writeOperationType"
                    )
                ),
        
                # the properties below are optional
                api_version="apiVersion",
                connector_profile_name="connectorProfileName"
            )],
            flow_name="flowName",
            source_flow_config=appflow.CfnFlow.SourceFlowConfigProperty(
                connector_type="connectorType",
                source_connector_properties=appflow.CfnFlow.SourceConnectorPropertiesProperty(
                    amplitude=appflow.CfnFlow.AmplitudeSourcePropertiesProperty(
                        object="object"
                    ),
                    custom_connector=appflow.CfnFlow.CustomConnectorSourcePropertiesProperty(
                        entity_name="entityName",
        
                        # the properties below are optional
                        custom_properties={
                            "custom_properties_key": "customProperties"
                        },
                        data_transfer_api=appflow.CfnFlow.DataTransferApiProperty(
                            name="name",
                            type="type"
                        )
                    ),
                    datadog=appflow.CfnFlow.DatadogSourcePropertiesProperty(
                        object="object"
                    ),
                    dynatrace=appflow.CfnFlow.DynatraceSourcePropertiesProperty(
                        object="object"
                    ),
                    google_analytics=appflow.CfnFlow.GoogleAnalyticsSourcePropertiesProperty(
                        object="object"
                    ),
                    infor_nexus=appflow.CfnFlow.InforNexusSourcePropertiesProperty(
                        object="object"
                    ),
                    marketo=appflow.CfnFlow.MarketoSourcePropertiesProperty(
                        object="object"
                    ),
                    pardot=appflow.CfnFlow.PardotSourcePropertiesProperty(
                        object="object"
                    ),
                    s3=appflow.CfnFlow.S3SourcePropertiesProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
        
                        # the properties below are optional
                        s3_input_format_config=appflow.CfnFlow.S3InputFormatConfigProperty(
                            s3_input_file_type="s3InputFileType"
                        )
                    ),
                    salesforce=appflow.CfnFlow.SalesforceSourcePropertiesProperty(
                        object="object",
        
                        # the properties below are optional
                        data_transfer_api="dataTransferApi",
                        enable_dynamic_field_update=False,
                        include_deleted_records=False
                    ),
                    sapo_data=appflow.CfnFlow.SAPODataSourcePropertiesProperty(
                        object_path="objectPath",
        
                        # the properties below are optional
                        pagination_config=appflow.CfnFlow.SAPODataPaginationConfigProperty(
                            max_page_size=123
                        ),
                        parallelism_config=appflow.CfnFlow.SAPODataParallelismConfigProperty(
                            max_parallelism=123
                        )
                    ),
                    service_now=appflow.CfnFlow.ServiceNowSourcePropertiesProperty(
                        object="object"
                    ),
                    singular=appflow.CfnFlow.SingularSourcePropertiesProperty(
                        object="object"
                    ),
                    slack=appflow.CfnFlow.SlackSourcePropertiesProperty(
                        object="object"
                    ),
                    trendmicro=appflow.CfnFlow.TrendmicroSourcePropertiesProperty(
                        object="object"
                    ),
                    veeva=appflow.CfnFlow.VeevaSourcePropertiesProperty(
                        object="object",
        
                        # the properties below are optional
                        document_type="documentType",
                        include_all_versions=False,
                        include_renditions=False,
                        include_source_files=False
                    ),
                    zendesk=appflow.CfnFlow.ZendeskSourcePropertiesProperty(
                        object="object"
                    )
                ),
        
                # the properties below are optional
                api_version="apiVersion",
                connector_profile_name="connectorProfileName",
                incremental_pull_config=appflow.CfnFlow.IncrementalPullConfigProperty(
                    datetime_type_field_name="datetimeTypeFieldName"
                )
            ),
            tasks=[appflow.CfnFlow.TaskProperty(
                source_fields=["sourceFields"],
                task_type="taskType",
        
                # the properties below are optional
                connector_operator=appflow.CfnFlow.ConnectorOperatorProperty(
                    amplitude="amplitude",
                    custom_connector="customConnector",
                    datadog="datadog",
                    dynatrace="dynatrace",
                    google_analytics="googleAnalytics",
                    infor_nexus="inforNexus",
                    marketo="marketo",
                    pardot="pardot",
                    s3="s3",
                    salesforce="salesforce",
                    sapo_data="sapoData",
                    service_now="serviceNow",
                    singular="singular",
                    slack="slack",
                    trendmicro="trendmicro",
                    veeva="veeva",
                    zendesk="zendesk"
                ),
                destination_field="destinationField",
                task_properties=[appflow.CfnFlow.TaskPropertiesObjectProperty(
                    key="key",
                    value="value"
                )]
            )],
            trigger_config=appflow.CfnFlow.TriggerConfigProperty(
                trigger_type="triggerType",
        
                # the properties below are optional
                trigger_properties=appflow.CfnFlow.ScheduledTriggerPropertiesProperty(
                    schedule_expression="scheduleExpression",
        
                    # the properties below are optional
                    data_pull_mode="dataPullMode",
                    first_execution_from=123,
                    flow_error_deactivation_threshold=123,
                    schedule_end_time=123,
                    schedule_offset=123,
                    schedule_start_time=123,
                    time_zone="timeZone"
                )
            ),
        
            # the properties below are optional
            description="description",
            flow_status="flowStatus",
            kms_arn="kmsArn",
            metadata_catalog_config=appflow.CfnFlow.MetadataCatalogConfigProperty(
                glue_data_catalog=appflow.CfnFlow.GlueDataCatalogProperty(
                    database_name="databaseName",
                    role_arn="roleArn",
                    table_prefix="tablePrefix"
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
        destination_flow_config_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.DestinationFlowConfigProperty", typing.Dict[builtins.str, typing.Any]]]]],
        flow_name: builtins.str,
        source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SourceFlowConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.TaskProperty", typing.Dict[builtins.str, typing.Any]]]]],
        trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.TriggerConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        flow_status: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
        metadata_catalog_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.MetadataCatalogConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param destination_flow_config_list: The configuration that controls how Amazon AppFlow places data in the destination connector.
        :param flow_name: The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only.
        :param source_flow_config: Contains information about the configuration of the source connector used in the flow.
        :param tasks: A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.
        :param trigger_config: The trigger settings that determine how and when Amazon AppFlow runs the specified flow.
        :param description: A user-entered description of the flow.
        :param flow_status: Sets the status of the flow. You can specify one of the following values:. - **Active** - The flow runs based on the trigger settings that you defined. Active scheduled flows run as scheduled, and active event-triggered flows run when the specified change event occurs. However, active on-demand flows run only when you manually start them by using Amazon AppFlow. - **Suspended** - You can use this option to deactivate an active flow. Scheduled and event-triggered flows will cease to run until you reactive them. This value only affects scheduled and event-triggered flows. It has no effect for on-demand flows. If you omit the FlowStatus parameter, Amazon AppFlow creates the flow with a default status. The default status for on-demand flows is Active. The default status for scheduled and event-triggered flows is Draft, which means they’re not yet active.
        :param kms_arn: The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        :param metadata_catalog_config: Specifies the configuration that Amazon AppFlow uses when it catalogs your data. When Amazon AppFlow catalogs your data, it stores metadata in a data catalog.
        :param tags: The tags used to organize, track, or control access for your flow.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76b6ef95e5f4f4d7b82746abb1435c9e6f43a91ed656c1dd9c1a02064f00a78a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowProps(
            destination_flow_config_list=destination_flow_config_list,
            flow_name=flow_name,
            source_flow_config=source_flow_config,
            tasks=tasks,
            trigger_config=trigger_config,
            description=description,
            flow_status=flow_status,
            kms_arn=kms_arn,
            metadata_catalog_config=metadata_catalog_config,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a0903a5b0777541e9478e23854a85d5a2c4808c0983bf165d70ab1b5449fca1)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2dc3a4aea78f4e89fd86f1b0a95c6b628a20b040c6bc400fdee8c2c4456dbec4)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrFlowArn")
    def attr_flow_arn(self) -> builtins.str:
        '''The flow's Amazon Resource Name (ARN).

        :cloudformationAttribute: FlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowArn"))

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
    @jsii.member(jsii_name="destinationFlowConfigList")
    def destination_flow_config_list(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.DestinationFlowConfigProperty"]]]:
        '''The configuration that controls how Amazon AppFlow places data in the destination connector.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.DestinationFlowConfigProperty"]]], jsii.get(self, "destinationFlowConfigList"))

    @destination_flow_config_list.setter
    def destination_flow_config_list(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.DestinationFlowConfigProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6e790e910559e7c5bdcd3b94ffbcee395c9ebca3506e34c7dc5849e4cc2f22e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFlowConfigList", value)

    @builtins.property
    @jsii.member(jsii_name="flowName")
    def flow_name(self) -> builtins.str:
        '''The specified name of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "flowName"))

    @flow_name.setter
    def flow_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04271ee51cb938fbf314abcbe8001536684e210ea83443e61da82559f654fcfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowName", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFlowConfig")
    def source_flow_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceFlowConfigProperty"]:
        '''Contains information about the configuration of the source connector used in the flow.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceFlowConfigProperty"], jsii.get(self, "sourceFlowConfig"))

    @source_flow_config.setter
    def source_flow_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceFlowConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af0fe8bf747f64f1d7f670168d2b21f389c54a57af38e982865d5ff46125027c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFlowConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tasks")
    def tasks(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.TaskProperty"]]]:
        '''A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.TaskProperty"]]], jsii.get(self, "tasks"))

    @tasks.setter
    def tasks(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.TaskProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6be845445f663cd529fe7ed672afb9293c81c28e04a68e7cffb28e49f904b1cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tasks", value)

    @builtins.property
    @jsii.member(jsii_name="triggerConfig")
    def trigger_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.TriggerConfigProperty"]:
        '''The trigger settings that determine how and when Amazon AppFlow runs the specified flow.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.TriggerConfigProperty"], jsii.get(self, "triggerConfig"))

    @trigger_config.setter
    def trigger_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFlow.TriggerConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb7ecca2b731f1a7b7e2f3e1002382bb5d5b42e9ff425b98984717cf715b0473)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "triggerConfig", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-entered description of the flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76ecbc6111b3b15ac62ef5211231c35103879fefecb75334c74f80f8c9df5e0b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="flowStatus")
    def flow_status(self) -> typing.Optional[builtins.str]:
        '''Sets the status of the flow.

        You can specify one of the following values:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowStatus"))

    @flow_status.setter
    def flow_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea530c7cd48e3e434bd34b8ab9dabb719427831263b04557da3d03e82acbebce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowStatus", value)

    @builtins.property
    @jsii.member(jsii_name="kmsArn")
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsArn"))

    @kms_arn.setter
    def kms_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__587868dddc78d2790162bd179ba67212276001fbdd8c989c9e3b837c1ef2b252)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsArn", value)

    @builtins.property
    @jsii.member(jsii_name="metadataCatalogConfig")
    def metadata_catalog_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MetadataCatalogConfigProperty"]]:
        '''Specifies the configuration that Amazon AppFlow uses when it catalogs your data.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MetadataCatalogConfigProperty"]], jsii.get(self, "metadataCatalogConfig"))

    @metadata_catalog_config.setter
    def metadata_catalog_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MetadataCatalogConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a474740c338d02b5c3e7ece5ad8097d97710078550a9f34157e3e053142f0c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "metadataCatalogConfig", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for your flow.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac44925e55be2d561241744a9491ec33e37633d5ea9a74479066fc80e01dab99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.AggregationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_type": "aggregationType",
            "target_file_size": "targetFileSize",
        },
    )
    class AggregationConfigProperty:
        def __init__(
            self,
            *,
            aggregation_type: typing.Optional[builtins.str] = None,
            target_file_size: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The aggregation settings that you can use to customize the output format of your flow data.

            :param aggregation_type: Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated.
            :param target_file_size: The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination. For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                aggregation_config_property = appflow.CfnFlow.AggregationConfigProperty(
                    aggregation_type="aggregationType",
                    target_file_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__328b80ffe3ee9a0256b74806b514d92bc909f03f004bc1072bd9eb46b96579f9)
                check_type(argname="argument aggregation_type", value=aggregation_type, expected_type=type_hints["aggregation_type"])
                check_type(argname="argument target_file_size", value=target_file_size, expected_type=type_hints["target_file_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aggregation_type is not None:
                self._values["aggregation_type"] = aggregation_type
            if target_file_size is not None:
                self._values["target_file_size"] = target_file_size

        @builtins.property
        def aggregation_type(self) -> typing.Optional[builtins.str]:
            '''Specifies whether Amazon AppFlow aggregates the flow records into a single file, or leave them unaggregated.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html#cfn-appflow-flow-aggregationconfig-aggregationtype
            '''
            result = self._values.get("aggregation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target_file_size(self) -> typing.Optional[jsii.Number]:
            '''The desired file size, in MB, for each output file that Amazon AppFlow writes to the flow destination.

            For each file, Amazon AppFlow attempts to achieve the size that you specify. The actual file sizes might differ from this target based on the number and size of the records that each file contains.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-aggregationconfig.html#cfn-appflow-flow-aggregationconfig-targetfilesize
            '''
            result = self._values.get("target_file_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AggregationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.AmplitudeSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class AmplitudeSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Amplitude is being used as a source.

            :param object: The object specified in the Amplitude flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-amplitudesourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                amplitude_source_properties_property = appflow.CfnFlow.AmplitudeSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c79a354a2904c1f043a53640b1e199ce326ebe0583ec664b1b5a5e01b1141585)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Amplitude flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-amplitudesourceproperties.html#cfn-appflow-flow-amplitudesourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AmplitudeSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.ConnectorOperatorProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amplitude": "amplitude",
            "custom_connector": "customConnector",
            "datadog": "datadog",
            "dynatrace": "dynatrace",
            "google_analytics": "googleAnalytics",
            "infor_nexus": "inforNexus",
            "marketo": "marketo",
            "pardot": "pardot",
            "s3": "s3",
            "salesforce": "salesforce",
            "sapo_data": "sapoData",
            "service_now": "serviceNow",
            "singular": "singular",
            "slack": "slack",
            "trendmicro": "trendmicro",
            "veeva": "veeva",
            "zendesk": "zendesk",
        },
    )
    class ConnectorOperatorProperty:
        def __init__(
            self,
            *,
            amplitude: typing.Optional[builtins.str] = None,
            custom_connector: typing.Optional[builtins.str] = None,
            datadog: typing.Optional[builtins.str] = None,
            dynatrace: typing.Optional[builtins.str] = None,
            google_analytics: typing.Optional[builtins.str] = None,
            infor_nexus: typing.Optional[builtins.str] = None,
            marketo: typing.Optional[builtins.str] = None,
            pardot: typing.Optional[builtins.str] = None,
            s3: typing.Optional[builtins.str] = None,
            salesforce: typing.Optional[builtins.str] = None,
            sapo_data: typing.Optional[builtins.str] = None,
            service_now: typing.Optional[builtins.str] = None,
            singular: typing.Optional[builtins.str] = None,
            slack: typing.Optional[builtins.str] = None,
            trendmicro: typing.Optional[builtins.str] = None,
            veeva: typing.Optional[builtins.str] = None,
            zendesk: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The operation to be performed on the provided source fields.

            :param amplitude: The operation to be performed on the provided Amplitude source fields.
            :param custom_connector: Operators supported by the custom connector.
            :param datadog: The operation to be performed on the provided Datadog source fields.
            :param dynatrace: The operation to be performed on the provided Dynatrace source fields.
            :param google_analytics: The operation to be performed on the provided Google Analytics source fields.
            :param infor_nexus: The operation to be performed on the provided Infor Nexus source fields.
            :param marketo: The operation to be performed on the provided Marketo source fields.
            :param pardot: The operation to be performed on the provided Salesforce Pardot source fields.
            :param s3: The operation to be performed on the provided Amazon S3 source fields.
            :param salesforce: The operation to be performed on the provided Salesforce source fields.
            :param sapo_data: The operation to be performed on the provided SAPOData source fields.
            :param service_now: The operation to be performed on the provided ServiceNow source fields.
            :param singular: The operation to be performed on the provided Singular source fields.
            :param slack: The operation to be performed on the provided Slack source fields.
            :param trendmicro: The operation to be performed on the provided Trend Micro source fields.
            :param veeva: The operation to be performed on the provided Veeva source fields.
            :param zendesk: The operation to be performed on the provided Zendesk source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                connector_operator_property = appflow.CfnFlow.ConnectorOperatorProperty(
                    amplitude="amplitude",
                    custom_connector="customConnector",
                    datadog="datadog",
                    dynatrace="dynatrace",
                    google_analytics="googleAnalytics",
                    infor_nexus="inforNexus",
                    marketo="marketo",
                    pardot="pardot",
                    s3="s3",
                    salesforce="salesforce",
                    sapo_data="sapoData",
                    service_now="serviceNow",
                    singular="singular",
                    slack="slack",
                    trendmicro="trendmicro",
                    veeva="veeva",
                    zendesk="zendesk"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d0948b4cb879f7f09a0ff8663e81bf08fbed9c98d8935ce5ea10cae90d1a8030)
                check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
                check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
                check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
                check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument pardot", value=pardot, expected_type=type_hints["pardot"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
                check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
                check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
                check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amplitude is not None:
                self._values["amplitude"] = amplitude
            if custom_connector is not None:
                self._values["custom_connector"] = custom_connector
            if datadog is not None:
                self._values["datadog"] = datadog
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if google_analytics is not None:
                self._values["google_analytics"] = google_analytics
            if infor_nexus is not None:
                self._values["infor_nexus"] = infor_nexus
            if marketo is not None:
                self._values["marketo"] = marketo
            if pardot is not None:
                self._values["pardot"] = pardot
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if sapo_data is not None:
                self._values["sapo_data"] = sapo_data
            if service_now is not None:
                self._values["service_now"] = service_now
            if singular is not None:
                self._values["singular"] = singular
            if slack is not None:
                self._values["slack"] = slack
            if trendmicro is not None:
                self._values["trendmicro"] = trendmicro
            if veeva is not None:
                self._values["veeva"] = veeva
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def amplitude(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Amplitude source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-amplitude
            '''
            result = self._values.get("amplitude")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def custom_connector(self) -> typing.Optional[builtins.str]:
            '''Operators supported by the custom connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-customconnector
            '''
            result = self._values.get("custom_connector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def datadog(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Datadog source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-datadog
            '''
            result = self._values.get("datadog")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def dynatrace(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Dynatrace source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def google_analytics(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Google Analytics source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-googleanalytics
            '''
            result = self._values.get("google_analytics")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def infor_nexus(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Infor Nexus source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-infornexus
            '''
            result = self._values.get("infor_nexus")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def marketo(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Marketo source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pardot(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Salesforce Pardot source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-pardot
            '''
            result = self._values.get("pardot")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Amazon S3 source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def salesforce(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Salesforce source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sapo_data(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided SAPOData source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-sapodata
            '''
            result = self._values.get("sapo_data")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def service_now(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided ServiceNow source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def singular(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Singular source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-singular
            '''
            result = self._values.get("singular")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def slack(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Slack source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-slack
            '''
            result = self._values.get("slack")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def trendmicro(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Trend Micro source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-trendmicro
            '''
            result = self._values.get("trendmicro")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def veeva(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Veeva source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-veeva
            '''
            result = self._values.get("veeva")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def zendesk(self) -> typing.Optional[builtins.str]:
            '''The operation to be performed on the provided Zendesk source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-connectoroperator.html#cfn-appflow-flow-connectoroperator-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConnectorOperatorProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.CustomConnectorDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entity_name": "entityName",
            "custom_properties": "customProperties",
            "error_handling_config": "errorHandlingConfig",
            "id_field_names": "idFieldNames",
            "write_operation_type": "writeOperationType",
        },
    )
    class CustomConnectorDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            entity_name: builtins.str,
            custom_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            write_operation_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when the custom connector is being used as a destination.

            :param entity_name: The entity specified in the custom connector as a destination in the flow.
            :param custom_properties: The custom properties that are specific to the connector when it's used as a destination in the flow.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the custom connector as destination.
            :param id_field_names: The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update, delete, or upsert.
            :param write_operation_type: Specifies the type of write operation to be performed in the custom connector when it's used as destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                custom_connector_destination_properties_property = appflow.CfnFlow.CustomConnectorDestinationPropertiesProperty(
                    entity_name="entityName",
                
                    # the properties below are optional
                    custom_properties={
                        "custom_properties_key": "customProperties"
                    },
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    ),
                    id_field_names=["idFieldNames"],
                    write_operation_type="writeOperationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c9546f78b7b6588933605f813de3303d240c8a8ea3ec8140f299a55377383a6d)
                check_type(argname="argument entity_name", value=entity_name, expected_type=type_hints["entity_name"])
                check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
                check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
                check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entity_name": entity_name,
            }
            if custom_properties is not None:
                self._values["custom_properties"] = custom_properties
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config
            if id_field_names is not None:
                self._values["id_field_names"] = id_field_names
            if write_operation_type is not None:
                self._values["write_operation_type"] = write_operation_type

        @builtins.property
        def entity_name(self) -> builtins.str:
            '''The entity specified in the custom connector as a destination in the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-entityname
            '''
            result = self._values.get("entity_name")
            assert result is not None, "Required property 'entity_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''The custom properties that are specific to the connector when it's used as a destination in the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-customproperties
            '''
            result = self._values.get("custom_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the custom connector as destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        @builtins.property
        def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update, delete, or upsert.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-idfieldnames
            '''
            result = self._values.get("id_field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def write_operation_type(self) -> typing.Optional[builtins.str]:
            '''Specifies the type of write operation to be performed in the custom connector when it's used as destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectordestinationproperties.html#cfn-appflow-flow-customconnectordestinationproperties-writeoperationtype
            '''
            result = self._values.get("write_operation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomConnectorDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.CustomConnectorSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "entity_name": "entityName",
            "custom_properties": "customProperties",
            "data_transfer_api": "dataTransferApi",
        },
    )
    class CustomConnectorSourcePropertiesProperty:
        def __init__(
            self,
            *,
            entity_name: builtins.str,
            custom_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            data_transfer_api: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.DataTransferApiProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when the custom connector is being used as a source.

            :param entity_name: The entity specified in the custom connector as a source in the flow.
            :param custom_properties: Custom properties that are required to use the custom connector as a source.
            :param data_transfer_api: The API of the connector application that Amazon AppFlow uses to transfer your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                custom_connector_source_properties_property = appflow.CfnFlow.CustomConnectorSourcePropertiesProperty(
                    entity_name="entityName",
                
                    # the properties below are optional
                    custom_properties={
                        "custom_properties_key": "customProperties"
                    },
                    data_transfer_api=appflow.CfnFlow.DataTransferApiProperty(
                        name="name",
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dca7f6a437784e099abbe4b67b153f5f8442b7f8bf74f61a2961a5fe146e546b)
                check_type(argname="argument entity_name", value=entity_name, expected_type=type_hints["entity_name"])
                check_type(argname="argument custom_properties", value=custom_properties, expected_type=type_hints["custom_properties"])
                check_type(argname="argument data_transfer_api", value=data_transfer_api, expected_type=type_hints["data_transfer_api"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "entity_name": entity_name,
            }
            if custom_properties is not None:
                self._values["custom_properties"] = custom_properties
            if data_transfer_api is not None:
                self._values["data_transfer_api"] = data_transfer_api

        @builtins.property
        def entity_name(self) -> builtins.str:
            '''The entity specified in the custom connector as a source in the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html#cfn-appflow-flow-customconnectorsourceproperties-entityname
            '''
            result = self._values.get("entity_name")
            assert result is not None, "Required property 'entity_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def custom_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''Custom properties that are required to use the custom connector as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html#cfn-appflow-flow-customconnectorsourceproperties-customproperties
            '''
            result = self._values.get("custom_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def data_transfer_api(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.DataTransferApiProperty"]]:
            '''The API of the connector application that Amazon AppFlow uses to transfer your data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-customconnectorsourceproperties.html#cfn-appflow-flow-customconnectorsourceproperties-datatransferapi
            '''
            result = self._values.get("data_transfer_api")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.DataTransferApiProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomConnectorSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.DataTransferApiProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "type": "type"},
    )
    class DataTransferApiProperty:
        def __init__(self, *, name: builtins.str, type: builtins.str) -> None:
            '''The API of the connector application that Amazon AppFlow uses to transfer your data.

            :param name: The name of the connector application API.
            :param type: You can specify one of the following types:. - **AUTOMATIC** - The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers. - **SYNC** - A synchronous API. This type of API optimizes a flow for small to medium-sized datasets. - **ASYNC** - An asynchronous API. This type of API optimizes a flow for large datasets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datatransferapi.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                data_transfer_api_property = appflow.CfnFlow.DataTransferApiProperty(
                    name="name",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fd0d04f9159d73850b9ed3d57b9d06d47be4e67aac70dac24b01272bce3eea51)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the connector application API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datatransferapi.html#cfn-appflow-flow-datatransferapi-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''You can specify one of the following types:.

            - **AUTOMATIC** - The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers.
            - **SYNC** - A synchronous API. This type of API optimizes a flow for small to medium-sized datasets.
            - **ASYNC** - An asynchronous API. This type of API optimizes a flow for large datasets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datatransferapi.html#cfn-appflow-flow-datatransferapi-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DataTransferApiProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.DatadogSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class DatadogSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Datadog is being used as a source.

            :param object: The object specified in the Datadog flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datadogsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                datadog_source_properties_property = appflow.CfnFlow.DatadogSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5b267c7bbc073ff7038f9afd92bea1a5aa8e3ce6c87cce7601e1a5c613842541)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Datadog flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-datadogsourceproperties.html#cfn-appflow-flow-datadogsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DatadogSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.DestinationConnectorPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "custom_connector": "customConnector",
            "event_bridge": "eventBridge",
            "lookout_metrics": "lookoutMetrics",
            "marketo": "marketo",
            "redshift": "redshift",
            "s3": "s3",
            "salesforce": "salesforce",
            "sapo_data": "sapoData",
            "snowflake": "snowflake",
            "upsolver": "upsolver",
            "zendesk": "zendesk",
        },
    )
    class DestinationConnectorPropertiesProperty:
        def __init__(
            self,
            *,
            custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.CustomConnectorDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            event_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.EventBridgeDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lookout_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.LookoutMetricsDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.MarketoDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            redshift: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.RedshiftDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.S3DestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SalesforceDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SAPODataDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SnowflakeDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            upsolver: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.UpsolverDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ZendeskDestinationPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''This stores the information that is required to query a particular connector.

            :param custom_connector: The properties that are required to query the custom Connector.
            :param event_bridge: The properties required to query Amazon EventBridge.
            :param lookout_metrics: The properties required to query Amazon Lookout for Metrics.
            :param marketo: The properties required to query Marketo.
            :param redshift: The properties required to query Amazon Redshift.
            :param s3: The properties required to query Amazon S3.
            :param salesforce: The properties required to query Salesforce.
            :param sapo_data: The properties required to query SAPOData.
            :param snowflake: The properties required to query Snowflake.
            :param upsolver: The properties required to query Upsolver.
            :param zendesk: The properties required to query Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                destination_connector_properties_property = appflow.CfnFlow.DestinationConnectorPropertiesProperty(
                    custom_connector=appflow.CfnFlow.CustomConnectorDestinationPropertiesProperty(
                        entity_name="entityName",
                
                        # the properties below are optional
                        custom_properties={
                            "custom_properties_key": "customProperties"
                        },
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        write_operation_type="writeOperationType"
                    ),
                    event_bridge=appflow.CfnFlow.EventBridgeDestinationPropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    lookout_metrics=appflow.CfnFlow.LookoutMetricsDestinationPropertiesProperty(
                        object="object"
                    ),
                    marketo=appflow.CfnFlow.MarketoDestinationPropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    redshift=appflow.CfnFlow.RedshiftDestinationPropertiesProperty(
                        intermediate_bucket_name="intermediateBucketName",
                        object="object",
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    s3=appflow.CfnFlow.S3DestinationPropertiesProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        s3_output_format_config=appflow.CfnFlow.S3OutputFormatConfigProperty(
                            aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                aggregation_type="aggregationType",
                                target_file_size=123
                            ),
                            file_type="fileType",
                            prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                path_prefix_hierarchy=["pathPrefixHierarchy"],
                                prefix_format="prefixFormat",
                                prefix_type="prefixType"
                            ),
                            preserve_source_data_typing=False
                        )
                    ),
                    salesforce=appflow.CfnFlow.SalesforceDestinationPropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        data_transfer_api="dataTransferApi",
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        write_operation_type="writeOperationType"
                    ),
                    sapo_data=appflow.CfnFlow.SAPODataDestinationPropertiesProperty(
                        object_path="objectPath",
                
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        success_response_handling_config=appflow.CfnFlow.SuccessResponseHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix"
                        ),
                        write_operation_type="writeOperationType"
                    ),
                    snowflake=appflow.CfnFlow.SnowflakeDestinationPropertiesProperty(
                        intermediate_bucket_name="intermediateBucketName",
                        object="object",
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix",
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        )
                    ),
                    upsolver=appflow.CfnFlow.UpsolverDestinationPropertiesProperty(
                        bucket_name="bucketName",
                        s3_output_format_config=appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty(
                            prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                path_prefix_hierarchy=["pathPrefixHierarchy"],
                                prefix_format="prefixFormat",
                                prefix_type="prefixType"
                            ),
                
                            # the properties below are optional
                            aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                aggregation_type="aggregationType",
                                target_file_size=123
                            ),
                            file_type="fileType"
                        ),
                
                        # the properties below are optional
                        bucket_prefix="bucketPrefix"
                    ),
                    zendesk=appflow.CfnFlow.ZendeskDestinationPropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                            fail_on_first_error=False
                        ),
                        id_field_names=["idFieldNames"],
                        write_operation_type="writeOperationType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__61c1007c034c653922497591ce4be08935eae99b8eb4651428db4cd63bfbe836)
                check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
                check_type(argname="argument event_bridge", value=event_bridge, expected_type=type_hints["event_bridge"])
                check_type(argname="argument lookout_metrics", value=lookout_metrics, expected_type=type_hints["lookout_metrics"])
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument redshift", value=redshift, expected_type=type_hints["redshift"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
                check_type(argname="argument snowflake", value=snowflake, expected_type=type_hints["snowflake"])
                check_type(argname="argument upsolver", value=upsolver, expected_type=type_hints["upsolver"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_connector is not None:
                self._values["custom_connector"] = custom_connector
            if event_bridge is not None:
                self._values["event_bridge"] = event_bridge
            if lookout_metrics is not None:
                self._values["lookout_metrics"] = lookout_metrics
            if marketo is not None:
                self._values["marketo"] = marketo
            if redshift is not None:
                self._values["redshift"] = redshift
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if sapo_data is not None:
                self._values["sapo_data"] = sapo_data
            if snowflake is not None:
                self._values["snowflake"] = snowflake
            if upsolver is not None:
                self._values["upsolver"] = upsolver
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def custom_connector(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.CustomConnectorDestinationPropertiesProperty"]]:
            '''The properties that are required to query the custom Connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-customconnector
            '''
            result = self._values.get("custom_connector")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.CustomConnectorDestinationPropertiesProperty"]], result)

        @builtins.property
        def event_bridge(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.EventBridgeDestinationPropertiesProperty"]]:
            '''The properties required to query Amazon EventBridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-eventbridge
            '''
            result = self._values.get("event_bridge")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.EventBridgeDestinationPropertiesProperty"]], result)

        @builtins.property
        def lookout_metrics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.LookoutMetricsDestinationPropertiesProperty"]]:
            '''The properties required to query Amazon Lookout for Metrics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-lookoutmetrics
            '''
            result = self._values.get("lookout_metrics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.LookoutMetricsDestinationPropertiesProperty"]], result)

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MarketoDestinationPropertiesProperty"]]:
            '''The properties required to query Marketo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MarketoDestinationPropertiesProperty"]], result)

        @builtins.property
        def redshift(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.RedshiftDestinationPropertiesProperty"]]:
            '''The properties required to query Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-redshift
            '''
            result = self._values.get("redshift")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.RedshiftDestinationPropertiesProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3DestinationPropertiesProperty"]]:
            '''The properties required to query Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3DestinationPropertiesProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SalesforceDestinationPropertiesProperty"]]:
            '''The properties required to query Salesforce.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SalesforceDestinationPropertiesProperty"]], result)

        @builtins.property
        def sapo_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataDestinationPropertiesProperty"]]:
            '''The properties required to query SAPOData.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-sapodata
            '''
            result = self._values.get("sapo_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataDestinationPropertiesProperty"]], result)

        @builtins.property
        def snowflake(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SnowflakeDestinationPropertiesProperty"]]:
            '''The properties required to query Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-snowflake
            '''
            result = self._values.get("snowflake")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SnowflakeDestinationPropertiesProperty"]], result)

        @builtins.property
        def upsolver(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.UpsolverDestinationPropertiesProperty"]]:
            '''The properties required to query Upsolver.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-upsolver
            '''
            result = self._values.get("upsolver")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.UpsolverDestinationPropertiesProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ZendeskDestinationPropertiesProperty"]]:
            '''The properties required to query Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationconnectorproperties.html#cfn-appflow-flow-destinationconnectorproperties-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ZendeskDestinationPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConnectorPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.DestinationFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_type": "connectorType",
            "destination_connector_properties": "destinationConnectorProperties",
            "api_version": "apiVersion",
            "connector_profile_name": "connectorProfileName",
        },
    )
    class DestinationFlowConfigProperty:
        def __init__(
            self,
            *,
            connector_type: builtins.str,
            destination_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.DestinationConnectorPropertiesProperty", typing.Dict[builtins.str, typing.Any]]],
            api_version: typing.Optional[builtins.str] = None,
            connector_profile_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contains information about the configuration of destination connectors present in the flow.

            :param connector_type: The type of destination connector, such as Sales force, Amazon S3, and so on.
            :param destination_connector_properties: This stores the information that is required to query a particular connector.
            :param api_version: The API version that the destination connector uses.
            :param connector_profile_name: The name of the connector profile. This name must be unique for each connector profile in the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                destination_flow_config_property = appflow.CfnFlow.DestinationFlowConfigProperty(
                    connector_type="connectorType",
                    destination_connector_properties=appflow.CfnFlow.DestinationConnectorPropertiesProperty(
                        custom_connector=appflow.CfnFlow.CustomConnectorDestinationPropertiesProperty(
                            entity_name="entityName",
                
                            # the properties below are optional
                            custom_properties={
                                "custom_properties_key": "customProperties"
                            },
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            write_operation_type="writeOperationType"
                        ),
                        event_bridge=appflow.CfnFlow.EventBridgeDestinationPropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        lookout_metrics=appflow.CfnFlow.LookoutMetricsDestinationPropertiesProperty(
                            object="object"
                        ),
                        marketo=appflow.CfnFlow.MarketoDestinationPropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        redshift=appflow.CfnFlow.RedshiftDestinationPropertiesProperty(
                            intermediate_bucket_name="intermediateBucketName",
                            object="object",
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        s3=appflow.CfnFlow.S3DestinationPropertiesProperty(
                            bucket_name="bucketName",
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            s3_output_format_config=appflow.CfnFlow.S3OutputFormatConfigProperty(
                                aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                    aggregation_type="aggregationType",
                                    target_file_size=123
                                ),
                                file_type="fileType",
                                prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                    path_prefix_hierarchy=["pathPrefixHierarchy"],
                                    prefix_format="prefixFormat",
                                    prefix_type="prefixType"
                                ),
                                preserve_source_data_typing=False
                            )
                        ),
                        salesforce=appflow.CfnFlow.SalesforceDestinationPropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            data_transfer_api="dataTransferApi",
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            write_operation_type="writeOperationType"
                        ),
                        sapo_data=appflow.CfnFlow.SAPODataDestinationPropertiesProperty(
                            object_path="objectPath",
                
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            success_response_handling_config=appflow.CfnFlow.SuccessResponseHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix"
                            ),
                            write_operation_type="writeOperationType"
                        ),
                        snowflake=appflow.CfnFlow.SnowflakeDestinationPropertiesProperty(
                            intermediate_bucket_name="intermediateBucketName",
                            object="object",
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        upsolver=appflow.CfnFlow.UpsolverDestinationPropertiesProperty(
                            bucket_name="bucketName",
                            s3_output_format_config=appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty(
                                prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                    path_prefix_hierarchy=["pathPrefixHierarchy"],
                                    prefix_format="prefixFormat",
                                    prefix_type="prefixType"
                                ),
                
                                # the properties below are optional
                                aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                    aggregation_type="aggregationType",
                                    target_file_size=123
                                ),
                                file_type="fileType"
                            ),
                
                            # the properties below are optional
                            bucket_prefix="bucketPrefix"
                        ),
                        zendesk=appflow.CfnFlow.ZendeskDestinationPropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            write_operation_type="writeOperationType"
                        )
                    ),
                
                    # the properties below are optional
                    api_version="apiVersion",
                    connector_profile_name="connectorProfileName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a402951d4f07b94704bb13f3e3d06a8b6b9d77e06e6fc1d84977f9517982e7f1)
                check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
                check_type(argname="argument destination_connector_properties", value=destination_connector_properties, expected_type=type_hints["destination_connector_properties"])
                check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
                check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_type": connector_type,
                "destination_connector_properties": destination_connector_properties,
            }
            if api_version is not None:
                self._values["api_version"] = api_version
            if connector_profile_name is not None:
                self._values["connector_profile_name"] = connector_profile_name

        @builtins.property
        def connector_type(self) -> builtins.str:
            '''The type of destination connector, such as Sales force, Amazon S3, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-connectortype
            '''
            result = self._values.get("connector_type")
            assert result is not None, "Required property 'connector_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def destination_connector_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.DestinationConnectorPropertiesProperty"]:
            '''This stores the information that is required to query a particular connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-destinationconnectorproperties
            '''
            result = self._values.get("destination_connector_properties")
            assert result is not None, "Required property 'destination_connector_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.DestinationConnectorPropertiesProperty"], result)

        @builtins.property
        def api_version(self) -> typing.Optional[builtins.str]:
            '''The API version that the destination connector uses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-apiversion
            '''
            result = self._values.get("api_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_profile_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connector profile.

            This name must be unique for each connector profile in the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-destinationflowconfig.html#cfn-appflow-flow-destinationflowconfig-connectorprofilename
            '''
            result = self._values.get("connector_profile_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.DynatraceSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class DynatraceSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Dynatrace is being used as a source.

            :param object: The object specified in the Dynatrace flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-dynatracesourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                dynatrace_source_properties_property = appflow.CfnFlow.DynatraceSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd31c39eceb7e8f9ff83abe7bdead9c7600418ea846aab5ebf0753342629880b)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Dynatrace flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-dynatracesourceproperties.html#cfn-appflow-flow-dynatracesourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynatraceSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.ErrorHandlingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_prefix": "bucketPrefix",
            "fail_on_first_error": "failOnFirstError",
        },
    )
    class ErrorHandlingConfigProperty:
        def __init__(
            self,
            *,
            bucket_name: typing.Optional[builtins.str] = None,
            bucket_prefix: typing.Optional[builtins.str] = None,
            fail_on_first_error: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :param bucket_name: Specifies the name of the Amazon S3 bucket.
            :param bucket_prefix: Specifies the Amazon S3 bucket prefix.
            :param fail_on_first_error: Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                error_handling_config_property = appflow.CfnFlow.ErrorHandlingConfigProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix",
                    fail_on_first_error=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__078888996b9eead8bfd345f5605ec71018981578c357cd612506905b30ac521b)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument fail_on_first_error", value=fail_on_first_error, expected_type=type_hints["fail_on_first_error"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if fail_on_first_error is not None:
                self._values["fail_on_first_error"] = fail_on_first_error

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''Specifies the name of the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html#cfn-appflow-flow-errorhandlingconfig-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''Specifies the Amazon S3 bucket prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html#cfn-appflow-flow-errorhandlingconfig-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def fail_on_first_error(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies if the flow should fail after the first instance of a failure when attempting to place data in the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-errorhandlingconfig.html#cfn-appflow-flow-errorhandlingconfig-failonfirsterror
            '''
            result = self._values.get("fail_on_first_error")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ErrorHandlingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.EventBridgeDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "error_handling_config": "errorHandlingConfig",
        },
    )
    class EventBridgeDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when Amazon EventBridge is being used as a destination.

            :param object: The object specified in the Amazon EventBridge flow destination.
            :param error_handling_config: The object specified in the Amplitude flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                event_bridge_destination_properties_property = appflow.CfnFlow.EventBridgeDestinationPropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c8e03b85b4f5295b92ede3385edaa38289164ed2e7ce6906b31d4ed43261f2a5)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Amazon EventBridge flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html#cfn-appflow-flow-eventbridgedestinationproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The object specified in the Amplitude flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-eventbridgedestinationproperties.html#cfn-appflow-flow-eventbridgedestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.GlueDataCatalogProperty",
        jsii_struct_bases=[],
        name_mapping={
            "database_name": "databaseName",
            "role_arn": "roleArn",
            "table_prefix": "tablePrefix",
        },
    )
    class GlueDataCatalogProperty:
        def __init__(
            self,
            *,
            database_name: builtins.str,
            role_arn: builtins.str,
            table_prefix: builtins.str,
        ) -> None:
            '''Trigger settings of the flow.

            :param database_name: A string containing the value for the tag.
            :param role_arn: A string containing the value for the tag.
            :param table_prefix: A string containing the value for the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                glue_data_catalog_property = appflow.CfnFlow.GlueDataCatalogProperty(
                    database_name="databaseName",
                    role_arn="roleArn",
                    table_prefix="tablePrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d54128401eb4f1071ae36d8a94740a8609f3a83c599e4ae134e5f639093b263)
                check_type(argname="argument database_name", value=database_name, expected_type=type_hints["database_name"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument table_prefix", value=table_prefix, expected_type=type_hints["table_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "database_name": database_name,
                "role_arn": role_arn,
                "table_prefix": table_prefix,
            }

        @builtins.property
        def database_name(self) -> builtins.str:
            '''A string containing the value for the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html#cfn-appflow-flow-gluedatacatalog-databasename
            '''
            result = self._values.get("database_name")
            assert result is not None, "Required property 'database_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''A string containing the value for the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html#cfn-appflow-flow-gluedatacatalog-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_prefix(self) -> builtins.str:
            '''A string containing the value for the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-gluedatacatalog.html#cfn-appflow-flow-gluedatacatalog-tableprefix
            '''
            result = self._values.get("table_prefix")
            assert result is not None, "Required property 'table_prefix' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GlueDataCatalogProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.GoogleAnalyticsSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class GoogleAnalyticsSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Google Analytics is being used as a source.

            :param object: The object specified in the Google Analytics flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-googleanalyticssourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                google_analytics_source_properties_property = appflow.CfnFlow.GoogleAnalyticsSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d4ed31a66518065602d2b82ead4f74719971927fbbbde987b8775f8e657f0f2f)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Google Analytics flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-googleanalyticssourceproperties.html#cfn-appflow-flow-googleanalyticssourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GoogleAnalyticsSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.IncrementalPullConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"datetime_type_field_name": "datetimeTypeFieldName"},
    )
    class IncrementalPullConfigProperty:
        def __init__(
            self,
            *,
            datetime_type_field_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration used when importing incremental records from the source.

            :param datetime_type_field_name: A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-incrementalpullconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                incremental_pull_config_property = appflow.CfnFlow.IncrementalPullConfigProperty(
                    datetime_type_field_name="datetimeTypeFieldName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__759935a3bf8f161ab3b60afdbbe4f58242c6c5bd495d8f4c8769f330422ea6f8)
                check_type(argname="argument datetime_type_field_name", value=datetime_type_field_name, expected_type=type_hints["datetime_type_field_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if datetime_type_field_name is not None:
                self._values["datetime_type_field_name"] = datetime_type_field_name

        @builtins.property
        def datetime_type_field_name(self) -> typing.Optional[builtins.str]:
            '''A field that specifies the date time or timestamp field as the criteria to use when importing incremental records from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-incrementalpullconfig.html#cfn-appflow-flow-incrementalpullconfig-datetimetypefieldname
            '''
            result = self._values.get("datetime_type_field_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IncrementalPullConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.InforNexusSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class InforNexusSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Infor Nexus is being used as a source.

            :param object: The object specified in the Infor Nexus flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-infornexussourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                infor_nexus_source_properties_property = appflow.CfnFlow.InforNexusSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3d7abfd8dee53e8d72b6717b22ce7f7090bff56556455f268445e608bbd34946)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Infor Nexus flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-infornexussourceproperties.html#cfn-appflow-flow-infornexussourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "InforNexusSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.LookoutMetricsDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class LookoutMetricsDestinationPropertiesProperty:
        def __init__(self, *, object: typing.Optional[builtins.str] = None) -> None:
            '''The properties that are applied when Amazon Lookout for Metrics is used as a destination.

            :param object: The object specified in the Amazon Lookout for Metrics flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-lookoutmetricsdestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                lookout_metrics_destination_properties_property = appflow.CfnFlow.LookoutMetricsDestinationPropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__060702aed5019190a6b199aad5e66f61768453c8fbe7c5549752dea9c79a361b)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if object is not None:
                self._values["object"] = object

        @builtins.property
        def object(self) -> typing.Optional[builtins.str]:
            '''The object specified in the Amazon Lookout for Metrics flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-lookoutmetricsdestinationproperties.html#cfn-appflow-flow-lookoutmetricsdestinationproperties-object
            '''
            result = self._values.get("object")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LookoutMetricsDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.MarketoDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "error_handling_config": "errorHandlingConfig",
        },
    )
    class MarketoDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that Amazon AppFlow applies when you use Marketo as a flow destination.

            :param object: The object specified in the Marketo flow destination.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketodestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                marketo_destination_properties_property = appflow.CfnFlow.MarketoDestinationPropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0d081ec2d0308a134ab532b76aa1b67bd5dc34d931782456f9384ab6bee329ba)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Marketo flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketodestinationproperties.html#cfn-appflow-flow-marketodestinationproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketodestinationproperties.html#cfn-appflow-flow-marketodestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.MarketoSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class MarketoSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Marketo is being used as a source.

            :param object: The object specified in the Marketo flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketosourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                marketo_source_properties_property = appflow.CfnFlow.MarketoSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8bd9aa6a3e0dbdbe51c141292970fcab641b368bdfcedea085461c81262a471b)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Marketo flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-marketosourceproperties.html#cfn-appflow-flow-marketosourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MarketoSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.MetadataCatalogConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"glue_data_catalog": "glueDataCatalog"},
    )
    class MetadataCatalogConfigProperty:
        def __init__(
            self,
            *,
            glue_data_catalog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.GlueDataCatalogProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the configuration that Amazon AppFlow uses when it catalogs your data.

            When Amazon AppFlow catalogs your data, it stores metadata in a data catalog.

            :param glue_data_catalog: Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-metadatacatalogconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                metadata_catalog_config_property = appflow.CfnFlow.MetadataCatalogConfigProperty(
                    glue_data_catalog=appflow.CfnFlow.GlueDataCatalogProperty(
                        database_name="databaseName",
                        role_arn="roleArn",
                        table_prefix="tablePrefix"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4d6c8a679bd51537f9a83827157b0794271255d4346540c24884c78865854859)
                check_type(argname="argument glue_data_catalog", value=glue_data_catalog, expected_type=type_hints["glue_data_catalog"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if glue_data_catalog is not None:
                self._values["glue_data_catalog"] = glue_data_catalog

        @builtins.property
        def glue_data_catalog(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.GlueDataCatalogProperty"]]:
            '''Specifies the configuration that Amazon AppFlow uses when it catalogs your data with the AWS Glue Data Catalog .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-metadatacatalogconfig.html#cfn-appflow-flow-metadatacatalogconfig-gluedatacatalog
            '''
            result = self._values.get("glue_data_catalog")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.GlueDataCatalogProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MetadataCatalogConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.PardotSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class PardotSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Salesforce Pardot is being used as a source.

            :param object: The object specified in the Salesforce Pardot flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-pardotsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                pardot_source_properties_property = appflow.CfnFlow.PardotSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57187f77b7b8cbe02dd1d2d2689e5d019ac5a329b434d4e64e52142ee8f22c96)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Salesforce Pardot flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-pardotsourceproperties.html#cfn-appflow-flow-pardotsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PardotSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.PrefixConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "path_prefix_hierarchy": "pathPrefixHierarchy",
            "prefix_format": "prefixFormat",
            "prefix_type": "prefixType",
        },
    )
    class PrefixConfigProperty:
        def __init__(
            self,
            *,
            path_prefix_hierarchy: typing.Optional[typing.Sequence[builtins.str]] = None,
            prefix_format: typing.Optional[builtins.str] = None,
            prefix_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies elements that Amazon AppFlow includes in the file and folder names in the flow destination.

            :param path_prefix_hierarchy: Specifies whether the destination file path includes either or both of the following elements:. - **EXECUTION_ID** - The ID that Amazon AppFlow assigns to the flow run. - **SCHEMA_VERSION** - The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration: - Source-to-destination field mappings - Field data types - Partition keys
            :param prefix_format: Determines the level of granularity for the date and time that's included in the prefix.
            :param prefix_type: Determines the format of the prefix, and whether it applies to the file name, file path, or both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                prefix_config_property = appflow.CfnFlow.PrefixConfigProperty(
                    path_prefix_hierarchy=["pathPrefixHierarchy"],
                    prefix_format="prefixFormat",
                    prefix_type="prefixType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ca7d146b99555e5990a83482ad7afa30c6b2871a7c5597b99e2b425052d5572)
                check_type(argname="argument path_prefix_hierarchy", value=path_prefix_hierarchy, expected_type=type_hints["path_prefix_hierarchy"])
                check_type(argname="argument prefix_format", value=prefix_format, expected_type=type_hints["prefix_format"])
                check_type(argname="argument prefix_type", value=prefix_type, expected_type=type_hints["prefix_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if path_prefix_hierarchy is not None:
                self._values["path_prefix_hierarchy"] = path_prefix_hierarchy
            if prefix_format is not None:
                self._values["prefix_format"] = prefix_format
            if prefix_type is not None:
                self._values["prefix_type"] = prefix_type

        @builtins.property
        def path_prefix_hierarchy(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Specifies whether the destination file path includes either or both of the following elements:.

            - **EXECUTION_ID** - The ID that Amazon AppFlow assigns to the flow run.
            - **SCHEMA_VERSION** - The version number of your data schema. Amazon AppFlow assigns this version number. The version number increases by one when you change any of the following settings in your flow configuration:
            - Source-to-destination field mappings
            - Field data types
            - Partition keys

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html#cfn-appflow-flow-prefixconfig-pathprefixhierarchy
            '''
            result = self._values.get("path_prefix_hierarchy")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def prefix_format(self) -> typing.Optional[builtins.str]:
            '''Determines the level of granularity for the date and time that's included in the prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html#cfn-appflow-flow-prefixconfig-prefixformat
            '''
            result = self._values.get("prefix_format")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix_type(self) -> typing.Optional[builtins.str]:
            '''Determines the format of the prefix, and whether it applies to the file name, file path, or both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-prefixconfig.html#cfn-appflow-flow-prefixconfig-prefixtype
            '''
            result = self._values.get("prefix_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrefixConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.RedshiftDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "intermediate_bucket_name": "intermediateBucketName",
            "object": "object",
            "bucket_prefix": "bucketPrefix",
            "error_handling_config": "errorHandlingConfig",
        },
    )
    class RedshiftDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            intermediate_bucket_name: builtins.str,
            object: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when Amazon Redshift is being used as a destination.

            :param intermediate_bucket_name: The intermediate bucket that Amazon AppFlow uses when moving data into Amazon Redshift.
            :param object: The object specified in the Amazon Redshift flow destination.
            :param bucket_prefix: The object key for the bucket in which Amazon AppFlow places the destination files.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the Amazon Redshift destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                redshift_destination_properties_property = appflow.CfnFlow.RedshiftDestinationPropertiesProperty(
                    intermediate_bucket_name="intermediateBucketName",
                    object="object",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f3402bfecb762ab7eeca84836d4541ecb34ac1e9bf357d0aca15d57bfbab3ef9)
                check_type(argname="argument intermediate_bucket_name", value=intermediate_bucket_name, expected_type=type_hints["intermediate_bucket_name"])
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "intermediate_bucket_name": intermediate_bucket_name,
                "object": object,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config

        @builtins.property
        def intermediate_bucket_name(self) -> builtins.str:
            '''The intermediate bucket that Amazon AppFlow uses when moving data into Amazon Redshift.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-intermediatebucketname
            '''
            result = self._values.get("intermediate_bucket_name")
            assert result is not None, "Required property 'intermediate_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Amazon Redshift flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the bucket in which Amazon AppFlow places the destination files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the Amazon Redshift destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-redshiftdestinationproperties.html#cfn-appflow-flow-redshiftdestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RedshiftDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.S3DestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_prefix": "bucketPrefix",
            "s3_output_format_config": "s3OutputFormatConfig",
        },
    )
    class S3DestinationPropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            s3_output_format_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.S3OutputFormatConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when Amazon S3 is used as a destination.

            :param bucket_name: The Amazon S3 bucket name in which Amazon AppFlow places the transferred data.
            :param bucket_prefix: The object key for the destination bucket in which Amazon AppFlow places the files.
            :param s3_output_format_config: The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s3_destination_properties_property = appflow.CfnFlow.S3DestinationPropertiesProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    s3_output_format_config=appflow.CfnFlow.S3OutputFormatConfigProperty(
                        aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                            aggregation_type="aggregationType",
                            target_file_size=123
                        ),
                        file_type="fileType",
                        prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                            path_prefix_hierarchy=["pathPrefixHierarchy"],
                            prefix_format="prefixFormat",
                            prefix_type="prefixType"
                        ),
                        preserve_source_data_typing=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ec0528e9590b2bddf1b9031aadc143a8f3989afde0772669ab454e92b157ce68)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument s3_output_format_config", value=s3_output_format_config, expected_type=type_hints["s3_output_format_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if s3_output_format_config is not None:
                self._values["s3_output_format_config"] = s3_output_format_config

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket name in which Amazon AppFlow places the transferred data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html#cfn-appflow-flow-s3destinationproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the destination bucket in which Amazon AppFlow places the files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html#cfn-appflow-flow-s3destinationproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def s3_output_format_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3OutputFormatConfigProperty"]]:
            '''The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3destinationproperties.html#cfn-appflow-flow-s3destinationproperties-s3outputformatconfig
            '''
            result = self._values.get("s3_output_format_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3OutputFormatConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3DestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.S3InputFormatConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_input_file_type": "s3InputFileType"},
    )
    class S3InputFormatConfigProperty:
        def __init__(
            self,
            *,
            s3_input_file_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When you use Amazon S3 as the source, the configuration format that you provide the flow input data.

            :param s3_input_file_type: The file type that Amazon AppFlow gets from your Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3inputformatconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s3_input_format_config_property = appflow.CfnFlow.S3InputFormatConfigProperty(
                    s3_input_file_type="s3InputFileType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3026ab7181af509228fef339c10aee815ccd500d0b0ab562d0a601451f151fe5)
                check_type(argname="argument s3_input_file_type", value=s3_input_file_type, expected_type=type_hints["s3_input_file_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if s3_input_file_type is not None:
                self._values["s3_input_file_type"] = s3_input_file_type

        @builtins.property
        def s3_input_file_type(self) -> typing.Optional[builtins.str]:
            '''The file type that Amazon AppFlow gets from your Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3inputformatconfig.html#cfn-appflow-flow-s3inputformatconfig-s3inputfiletype
            '''
            result = self._values.get("s3_input_file_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3InputFormatConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.S3OutputFormatConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aggregation_config": "aggregationConfig",
            "file_type": "fileType",
            "prefix_config": "prefixConfig",
            "preserve_source_data_typing": "preserveSourceDataTyping",
        },
    )
    class S3OutputFormatConfigProperty:
        def __init__(
            self,
            *,
            aggregation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.AggregationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            file_type: typing.Optional[builtins.str] = None,
            prefix_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.PrefixConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            preserve_source_data_typing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.

            :param aggregation_config: The aggregation settings that you can use to customize the output format of your flow data.
            :param file_type: Indicates the file type that Amazon AppFlow places in the Amazon S3 bucket.
            :param prefix_config: Determines the prefix that Amazon AppFlow applies to the folder name in the Amazon S3 bucket. You can name folders according to the flow frequency and date.
            :param preserve_source_data_typing: If your file output format is Parquet, use this parameter to set whether Amazon AppFlow preserves the data types in your source data when it writes the output to Amazon S3. - ``true`` : Amazon AppFlow preserves the data types when it writes to Amazon S3. For example, an integer or ``1`` in your source data is still an integer in your output. - ``false`` : Amazon AppFlow converts all of the source data into strings when it writes to Amazon S3. For example, an integer of ``1`` in your source data becomes the string ``"1"`` in the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s3_output_format_config_property = appflow.CfnFlow.S3OutputFormatConfigProperty(
                    aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                        aggregation_type="aggregationType",
                        target_file_size=123
                    ),
                    file_type="fileType",
                    prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                        path_prefix_hierarchy=["pathPrefixHierarchy"],
                        prefix_format="prefixFormat",
                        prefix_type="prefixType"
                    ),
                    preserve_source_data_typing=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__407430b2021e0200bc72876aac4ff684f0d8799c206a3a9414a422d1117ad9e3)
                check_type(argname="argument aggregation_config", value=aggregation_config, expected_type=type_hints["aggregation_config"])
                check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
                check_type(argname="argument prefix_config", value=prefix_config, expected_type=type_hints["prefix_config"])
                check_type(argname="argument preserve_source_data_typing", value=preserve_source_data_typing, expected_type=type_hints["preserve_source_data_typing"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aggregation_config is not None:
                self._values["aggregation_config"] = aggregation_config
            if file_type is not None:
                self._values["file_type"] = file_type
            if prefix_config is not None:
                self._values["prefix_config"] = prefix_config
            if preserve_source_data_typing is not None:
                self._values["preserve_source_data_typing"] = preserve_source_data_typing

        @builtins.property
        def aggregation_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.AggregationConfigProperty"]]:
            '''The aggregation settings that you can use to customize the output format of your flow data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-aggregationconfig
            '''
            result = self._values.get("aggregation_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.AggregationConfigProperty"]], result)

        @builtins.property
        def file_type(self) -> typing.Optional[builtins.str]:
            '''Indicates the file type that Amazon AppFlow places in the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-filetype
            '''
            result = self._values.get("file_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def prefix_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.PrefixConfigProperty"]]:
            '''Determines the prefix that Amazon AppFlow applies to the folder name in the Amazon S3 bucket.

            You can name folders according to the flow frequency and date.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-prefixconfig
            '''
            result = self._values.get("prefix_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.PrefixConfigProperty"]], result)

        @builtins.property
        def preserve_source_data_typing(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If your file output format is Parquet, use this parameter to set whether Amazon AppFlow preserves the data types in your source data when it writes the output to Amazon S3.

            - ``true`` : Amazon AppFlow preserves the data types when it writes to Amazon S3. For example, an integer or ``1`` in your source data is still an integer in your output.
            - ``false`` : Amazon AppFlow converts all of the source data into strings when it writes to Amazon S3. For example, an integer of ``1`` in your source data becomes the string ``"1"`` in the output.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3outputformatconfig.html#cfn-appflow-flow-s3outputformatconfig-preservesourcedatatyping
            '''
            result = self._values.get("preserve_source_data_typing")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3OutputFormatConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.S3SourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "bucket_prefix": "bucketPrefix",
            "s3_input_format_config": "s3InputFormatConfig",
        },
    )
    class S3SourcePropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            bucket_prefix: builtins.str,
            s3_input_format_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.S3InputFormatConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when Amazon S3 is being used as the flow source.

            :param bucket_name: The Amazon S3 bucket name where the source files are stored.
            :param bucket_prefix: The object key for the Amazon S3 bucket in which the source files are stored.
            :param s3_input_format_config: When you use Amazon S3 as the source, the configuration format that you provide the flow input data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s3_source_properties_property = appflow.CfnFlow.S3SourcePropertiesProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix",
                
                    # the properties below are optional
                    s3_input_format_config=appflow.CfnFlow.S3InputFormatConfigProperty(
                        s3_input_file_type="s3InputFileType"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fceba990c11a1dcac2ffb6444971b0e2f656ef344ffa30a7be490d7934960b27)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument s3_input_format_config", value=s3_input_format_config, expected_type=type_hints["s3_input_format_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "bucket_prefix": bucket_prefix,
            }
            if s3_input_format_config is not None:
                self._values["s3_input_format_config"] = s3_input_format_config

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Amazon S3 bucket name where the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html#cfn-appflow-flow-s3sourceproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> builtins.str:
            '''The object key for the Amazon S3 bucket in which the source files are stored.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html#cfn-appflow-flow-s3sourceproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            assert result is not None, "Required property 'bucket_prefix' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_input_format_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3InputFormatConfigProperty"]]:
            '''When you use Amazon S3 as the source, the configuration format that you provide the flow input data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-s3sourceproperties.html#cfn-appflow-flow-s3sourceproperties-s3inputformatconfig
            '''
            result = self._values.get("s3_input_format_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3InputFormatConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3SourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SAPODataDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object_path": "objectPath",
            "error_handling_config": "errorHandlingConfig",
            "id_field_names": "idFieldNames",
            "success_response_handling_config": "successResponseHandlingConfig",
            "write_operation_type": "writeOperationType",
        },
    )
    class SAPODataDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            object_path: builtins.str,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            success_response_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SuccessResponseHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            write_operation_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when using SAPOData as a flow destination.

            :param object_path: The object path specified in the SAPOData flow destination.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.
            :param id_field_names: A list of field names that can be used as an ID field when performing a write operation.
            :param success_response_handling_config: Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data. For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.
            :param write_operation_type: The possible write operations in the destination connector. When this value is not provided, this defaults to the ``INSERT`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s_aPOData_destination_properties_property = appflow.CfnFlow.SAPODataDestinationPropertiesProperty(
                    object_path="objectPath",
                
                    # the properties below are optional
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    ),
                    id_field_names=["idFieldNames"],
                    success_response_handling_config=appflow.CfnFlow.SuccessResponseHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix"
                    ),
                    write_operation_type="writeOperationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe430f8a0b8fb0ec38ccedbd370e2c15756d92142c80a33db63467c251bf746f)
                check_type(argname="argument object_path", value=object_path, expected_type=type_hints["object_path"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
                check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
                check_type(argname="argument success_response_handling_config", value=success_response_handling_config, expected_type=type_hints["success_response_handling_config"])
                check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_path": object_path,
            }
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config
            if id_field_names is not None:
                self._values["id_field_names"] = id_field_names
            if success_response_handling_config is not None:
                self._values["success_response_handling_config"] = success_response_handling_config
            if write_operation_type is not None:
                self._values["write_operation_type"] = write_operation_type

        @builtins.property
        def object_path(self) -> builtins.str:
            '''The object path specified in the SAPOData flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-objectpath
            '''
            result = self._values.get("object_path")
            assert result is not None, "Required property 'object_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        @builtins.property
        def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of field names that can be used as an ID field when performing a write operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-idfieldnames
            '''
            result = self._values.get("id_field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def success_response_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SuccessResponseHandlingConfigProperty"]]:
            '''Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.

            For example, this setting would determine where to write the response from a destination connector upon a successful insert operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-successresponsehandlingconfig
            '''
            result = self._values.get("success_response_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SuccessResponseHandlingConfigProperty"]], result)

        @builtins.property
        def write_operation_type(self) -> typing.Optional[builtins.str]:
            '''The possible write operations in the destination connector.

            When this value is not provided, this defaults to the ``INSERT`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatadestinationproperties.html#cfn-appflow-flow-sapodatadestinationproperties-writeoperationtype
            '''
            result = self._values.get("write_operation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAPODataDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SAPODataPaginationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"max_page_size": "maxPageSize"},
    )
    class SAPODataPaginationConfigProperty:
        def __init__(self, *, max_page_size: jsii.Number) -> None:
            '''SAP Source connector page size.

            :param max_page_size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatapaginationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s_aPOData_pagination_config_property = appflow.CfnFlow.SAPODataPaginationConfigProperty(
                    max_page_size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__70a1b148320f618d1580608aea44a877c958797e9cc86024259d3c016c8971c1)
                check_type(argname="argument max_page_size", value=max_page_size, expected_type=type_hints["max_page_size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_page_size": max_page_size,
            }

        @builtins.property
        def max_page_size(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatapaginationconfig.html#cfn-appflow-flow-sapodatapaginationconfig-maxpagesize
            '''
            result = self._values.get("max_page_size")
            assert result is not None, "Required property 'max_page_size' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAPODataPaginationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SAPODataParallelismConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"max_parallelism": "maxParallelism"},
    )
    class SAPODataParallelismConfigProperty:
        def __init__(self, *, max_parallelism: jsii.Number) -> None:
            '''SAP Source connector parallelism factor.

            :param max_parallelism: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodataparallelismconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s_aPOData_parallelism_config_property = appflow.CfnFlow.SAPODataParallelismConfigProperty(
                    max_parallelism=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__668e98c80d12ecf0f0b6848ebbd4e31684d00592bad96c5d718f04567a36d867)
                check_type(argname="argument max_parallelism", value=max_parallelism, expected_type=type_hints["max_parallelism"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_parallelism": max_parallelism,
            }

        @builtins.property
        def max_parallelism(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodataparallelismconfig.html#cfn-appflow-flow-sapodataparallelismconfig-maxparallelism
            '''
            result = self._values.get("max_parallelism")
            assert result is not None, "Required property 'max_parallelism' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAPODataParallelismConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SAPODataSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object_path": "objectPath",
            "pagination_config": "paginationConfig",
            "parallelism_config": "parallelismConfig",
        },
    )
    class SAPODataSourcePropertiesProperty:
        def __init__(
            self,
            *,
            object_path: builtins.str,
            pagination_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SAPODataPaginationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            parallelism_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SAPODataParallelismConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when using SAPOData as a flow source.

            :param object_path: The object path specified in the SAPOData flow source.
            :param pagination_config: SAP Source connector page size.
            :param parallelism_config: SAP Source connector parallelism factor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                s_aPOData_source_properties_property = appflow.CfnFlow.SAPODataSourcePropertiesProperty(
                    object_path="objectPath",
                
                    # the properties below are optional
                    pagination_config=appflow.CfnFlow.SAPODataPaginationConfigProperty(
                        max_page_size=123
                    ),
                    parallelism_config=appflow.CfnFlow.SAPODataParallelismConfigProperty(
                        max_parallelism=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1c4e8d48237678f7dc3ac8c9c540e8c8080066daee936538208a6c98c0bd5b8e)
                check_type(argname="argument object_path", value=object_path, expected_type=type_hints["object_path"])
                check_type(argname="argument pagination_config", value=pagination_config, expected_type=type_hints["pagination_config"])
                check_type(argname="argument parallelism_config", value=parallelism_config, expected_type=type_hints["parallelism_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object_path": object_path,
            }
            if pagination_config is not None:
                self._values["pagination_config"] = pagination_config
            if parallelism_config is not None:
                self._values["parallelism_config"] = parallelism_config

        @builtins.property
        def object_path(self) -> builtins.str:
            '''The object path specified in the SAPOData flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html#cfn-appflow-flow-sapodatasourceproperties-objectpath
            '''
            result = self._values.get("object_path")
            assert result is not None, "Required property 'object_path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def pagination_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataPaginationConfigProperty"]]:
            '''SAP Source connector page size.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html#cfn-appflow-flow-sapodatasourceproperties-paginationconfig
            '''
            result = self._values.get("pagination_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataPaginationConfigProperty"]], result)

        @builtins.property
        def parallelism_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataParallelismConfigProperty"]]:
            '''SAP Source connector parallelism factor.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sapodatasourceproperties.html#cfn-appflow-flow-sapodatasourceproperties-parallelismconfig
            '''
            result = self._values.get("parallelism_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataParallelismConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAPODataSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SalesforceDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "data_transfer_api": "dataTransferApi",
            "error_handling_config": "errorHandlingConfig",
            "id_field_names": "idFieldNames",
            "write_operation_type": "writeOperationType",
        },
    )
    class SalesforceDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            data_transfer_api: typing.Optional[builtins.str] = None,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            write_operation_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when Salesforce is being used as a destination.

            :param object: The object specified in the Salesforce flow destination.
            :param data_transfer_api: Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data to Salesforce. - **AUTOMATIC** - The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers to Salesforce. If your flow transfers fewer than 1,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0. Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900 records, and it might use Bulk API 2.0 on the next day to transfer 1,100 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields. By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output. - **BULKV2** - Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers. Note that Bulk API 2.0 does not transfer Salesforce compound fields. - **REST_SYNC** - Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail with a timed out error.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the Salesforce destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.
            :param id_field_names: The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update or delete.
            :param write_operation_type: This specifies the type of write operation to be performed in Salesforce. When the value is ``UPSERT`` , then ``idFieldNames`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                salesforce_destination_properties_property = appflow.CfnFlow.SalesforceDestinationPropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    data_transfer_api="dataTransferApi",
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    ),
                    id_field_names=["idFieldNames"],
                    write_operation_type="writeOperationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fb5fca2c002782d42209e79c110151b3808d3c3603d8ea4038a9950700201881)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument data_transfer_api", value=data_transfer_api, expected_type=type_hints["data_transfer_api"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
                check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
                check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if data_transfer_api is not None:
                self._values["data_transfer_api"] = data_transfer_api
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config
            if id_field_names is not None:
                self._values["id_field_names"] = id_field_names
            if write_operation_type is not None:
                self._values["write_operation_type"] = write_operation_type

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Salesforce flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_transfer_api(self) -> typing.Optional[builtins.str]:
            '''Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data to Salesforce.

            - **AUTOMATIC** - The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers to Salesforce. If your flow transfers fewer than 1,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.

            Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900 records, and it might use Bulk API 2.0 on the next day to transfer 1,100 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields.

            By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.

            - **BULKV2** - Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.

            Note that Bulk API 2.0 does not transfer Salesforce compound fields.

            - **REST_SYNC** - Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail with a timed out error.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-datatransferapi
            '''
            result = self._values.get("data_transfer_api")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the Salesforce destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        @builtins.property
        def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The name of the field that Amazon AppFlow uses as an ID when performing a write operation such as update or delete.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-idfieldnames
            '''
            result = self._values.get("id_field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def write_operation_type(self) -> typing.Optional[builtins.str]:
            '''This specifies the type of write operation to be performed in Salesforce.

            When the value is ``UPSERT`` , then ``idFieldNames`` is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcedestinationproperties.html#cfn-appflow-flow-salesforcedestinationproperties-writeoperationtype
            '''
            result = self._values.get("write_operation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SalesforceSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "data_transfer_api": "dataTransferApi",
            "enable_dynamic_field_update": "enableDynamicFieldUpdate",
            "include_deleted_records": "includeDeletedRecords",
        },
    )
    class SalesforceSourcePropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            data_transfer_api: typing.Optional[builtins.str] = None,
            enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_deleted_records: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The properties that are applied when Salesforce is being used as a source.

            :param object: The object specified in the Salesforce flow source.
            :param data_transfer_api: Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data from Salesforce. - **AUTOMATIC** - The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers from Salesforce. If your flow transfers fewer than 1,000,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0. Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900,000 records, and it might use Bulk API 2.0 on the next day to transfer 1,100,000 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields. By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output. - **BULKV2** - Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers. Note that Bulk API 2.0 does not transfer Salesforce compound fields. - **REST_SYNC** - Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail wituh a timed out error.
            :param enable_dynamic_field_update: The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.
            :param include_deleted_records: Indicates whether Amazon AppFlow includes deleted files in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                salesforce_source_properties_property = appflow.CfnFlow.SalesforceSourcePropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    data_transfer_api="dataTransferApi",
                    enable_dynamic_field_update=False,
                    include_deleted_records=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__697f1bdf553e40b76d835a0032b4929b29e8c8e62c21e52cbc4d6e184f47fe5b)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument data_transfer_api", value=data_transfer_api, expected_type=type_hints["data_transfer_api"])
                check_type(argname="argument enable_dynamic_field_update", value=enable_dynamic_field_update, expected_type=type_hints["enable_dynamic_field_update"])
                check_type(argname="argument include_deleted_records", value=include_deleted_records, expected_type=type_hints["include_deleted_records"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if data_transfer_api is not None:
                self._values["data_transfer_api"] = data_transfer_api
            if enable_dynamic_field_update is not None:
                self._values["enable_dynamic_field_update"] = enable_dynamic_field_update
            if include_deleted_records is not None:
                self._values["include_deleted_records"] = include_deleted_records

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Salesforce flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_transfer_api(self) -> typing.Optional[builtins.str]:
            '''Specifies which Salesforce API is used by Amazon AppFlow when your flow transfers data from Salesforce.

            - **AUTOMATIC** - The default. Amazon AppFlow selects which API to use based on the number of records that your flow transfers from Salesforce. If your flow transfers fewer than 1,000,000 records, Amazon AppFlow uses Salesforce REST API. If your flow transfers 1,000,000 records or more, Amazon AppFlow uses Salesforce Bulk API 2.0.

            Each of these Salesforce APIs structures data differently. If Amazon AppFlow selects the API automatically, be aware that, for recurring flows, the data output might vary from one flow run to the next. For example, if a flow runs daily, it might use REST API on one day to transfer 900,000 records, and it might use Bulk API 2.0 on the next day to transfer 1,100,000 records. For each of these flow runs, the respective Salesforce API formats the data differently. Some of the differences include how dates are formatted and null values are represented. Also, Bulk API 2.0 doesn't transfer Salesforce compound fields.

            By choosing this option, you optimize flow performance for both small and large data transfers, but the tradeoff is inconsistent formatting in the output.

            - **BULKV2** - Amazon AppFlow uses only Salesforce Bulk API 2.0. This API runs asynchronous data transfers, and it's optimal for large sets of data. By choosing this option, you ensure that your flow writes consistent output, but you optimize performance only for large data transfers.

            Note that Bulk API 2.0 does not transfer Salesforce compound fields.

            - **REST_SYNC** - Amazon AppFlow uses only Salesforce REST API. By choosing this option, you ensure that your flow writes consistent output, but you decrease performance for large data transfers that are better suited for Bulk API 2.0. In some cases, if your flow attempts to transfer a vary large set of data, it might fail wituh a timed out error.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-datatransferapi
            '''
            result = self._values.get("data_transfer_api")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enable_dynamic_field_update(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-enabledynamicfieldupdate
            '''
            result = self._values.get("enable_dynamic_field_update")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_deleted_records(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether Amazon AppFlow includes deleted files in the flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-salesforcesourceproperties.html#cfn-appflow-flow-salesforcesourceproperties-includedeletedrecords
            '''
            result = self._values.get("include_deleted_records")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SalesforceSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.ScheduledTriggerPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule_expression": "scheduleExpression",
            "data_pull_mode": "dataPullMode",
            "first_execution_from": "firstExecutionFrom",
            "flow_error_deactivation_threshold": "flowErrorDeactivationThreshold",
            "schedule_end_time": "scheduleEndTime",
            "schedule_offset": "scheduleOffset",
            "schedule_start_time": "scheduleStartTime",
            "time_zone": "timeZone",
        },
    )
    class ScheduledTriggerPropertiesProperty:
        def __init__(
            self,
            *,
            schedule_expression: builtins.str,
            data_pull_mode: typing.Optional[builtins.str] = None,
            first_execution_from: typing.Optional[jsii.Number] = None,
            flow_error_deactivation_threshold: typing.Optional[jsii.Number] = None,
            schedule_end_time: typing.Optional[jsii.Number] = None,
            schedule_offset: typing.Optional[jsii.Number] = None,
            schedule_start_time: typing.Optional[jsii.Number] = None,
            time_zone: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies the configuration details of a schedule-triggered flow as defined by the user.

            Currently, these settings only apply to the ``Scheduled`` trigger type.

            :param schedule_expression: The scheduling expression that determines the rate at which the schedule will run, for example ``rate(5minutes)`` .
            :param data_pull_mode: Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.
            :param first_execution_from: Specifies the date range for the records to import from the connector in the first flow run.
            :param flow_error_deactivation_threshold: Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.
            :param schedule_end_time: The time at which the scheduled flow ends. The time is formatted as a timestamp that follows the ISO 8601 standard, such as ``2022-04-27T13:00:00-07:00`` .
            :param schedule_offset: Specifies the optional offset that is added to the time interval for a schedule-triggered flow.
            :param schedule_start_time: The time at which the scheduled flow starts. The time is formatted as a timestamp that follows the ISO 8601 standard, such as ``2022-04-26T13:00:00-07:00`` .
            :param time_zone: Specifies the time zone used when referring to the dates and times of a scheduled flow, such as ``America/New_York`` . This time zone is only a descriptive label. It doesn't affect how Amazon AppFlow interprets the timestamps that you specify to schedule the flow. If you want to schedule a flow by using times in a particular time zone, indicate the time zone as a UTC offset in your timestamps. For example, the UTC offsets for the ``America/New_York`` timezone are ``-04:00`` EDT and ``-05:00 EST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                scheduled_trigger_properties_property = appflow.CfnFlow.ScheduledTriggerPropertiesProperty(
                    schedule_expression="scheduleExpression",
                
                    # the properties below are optional
                    data_pull_mode="dataPullMode",
                    first_execution_from=123,
                    flow_error_deactivation_threshold=123,
                    schedule_end_time=123,
                    schedule_offset=123,
                    schedule_start_time=123,
                    time_zone="timeZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__432f0b4ecbd08bb1fea8eaf3541e9eea15562f2a97861fe29276031c796d986b)
                check_type(argname="argument schedule_expression", value=schedule_expression, expected_type=type_hints["schedule_expression"])
                check_type(argname="argument data_pull_mode", value=data_pull_mode, expected_type=type_hints["data_pull_mode"])
                check_type(argname="argument first_execution_from", value=first_execution_from, expected_type=type_hints["first_execution_from"])
                check_type(argname="argument flow_error_deactivation_threshold", value=flow_error_deactivation_threshold, expected_type=type_hints["flow_error_deactivation_threshold"])
                check_type(argname="argument schedule_end_time", value=schedule_end_time, expected_type=type_hints["schedule_end_time"])
                check_type(argname="argument schedule_offset", value=schedule_offset, expected_type=type_hints["schedule_offset"])
                check_type(argname="argument schedule_start_time", value=schedule_start_time, expected_type=type_hints["schedule_start_time"])
                check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule_expression": schedule_expression,
            }
            if data_pull_mode is not None:
                self._values["data_pull_mode"] = data_pull_mode
            if first_execution_from is not None:
                self._values["first_execution_from"] = first_execution_from
            if flow_error_deactivation_threshold is not None:
                self._values["flow_error_deactivation_threshold"] = flow_error_deactivation_threshold
            if schedule_end_time is not None:
                self._values["schedule_end_time"] = schedule_end_time
            if schedule_offset is not None:
                self._values["schedule_offset"] = schedule_offset
            if schedule_start_time is not None:
                self._values["schedule_start_time"] = schedule_start_time
            if time_zone is not None:
                self._values["time_zone"] = time_zone

        @builtins.property
        def schedule_expression(self) -> builtins.str:
            '''The scheduling expression that determines the rate at which the schedule will run, for example ``rate(5minutes)`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-scheduleexpression
            '''
            result = self._values.get("schedule_expression")
            assert result is not None, "Required property 'schedule_expression' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def data_pull_mode(self) -> typing.Optional[builtins.str]:
            '''Specifies whether a scheduled flow has an incremental data transfer or a complete data transfer for each flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-datapullmode
            '''
            result = self._values.get("data_pull_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def first_execution_from(self) -> typing.Optional[jsii.Number]:
            '''Specifies the date range for the records to import from the connector in the first flow run.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-firstexecutionfrom
            '''
            result = self._values.get("first_execution_from")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def flow_error_deactivation_threshold(self) -> typing.Optional[jsii.Number]:
            '''Defines how many times a scheduled flow fails consecutively before Amazon AppFlow deactivates it.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-flowerrordeactivationthreshold
            '''
            result = self._values.get("flow_error_deactivation_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_end_time(self) -> typing.Optional[jsii.Number]:
            '''The time at which the scheduled flow ends.

            The time is formatted as a timestamp that follows the ISO 8601 standard, such as ``2022-04-27T13:00:00-07:00`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-scheduleendtime
            '''
            result = self._values.get("schedule_end_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_offset(self) -> typing.Optional[jsii.Number]:
            '''Specifies the optional offset that is added to the time interval for a schedule-triggered flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-scheduleoffset
            '''
            result = self._values.get("schedule_offset")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def schedule_start_time(self) -> typing.Optional[jsii.Number]:
            '''The time at which the scheduled flow starts.

            The time is formatted as a timestamp that follows the ISO 8601 standard, such as ``2022-04-26T13:00:00-07:00`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-schedulestarttime
            '''
            result = self._values.get("schedule_start_time")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def time_zone(self) -> typing.Optional[builtins.str]:
            '''Specifies the time zone used when referring to the dates and times of a scheduled flow, such as ``America/New_York`` .

            This time zone is only a descriptive label. It doesn't affect how Amazon AppFlow interprets the timestamps that you specify to schedule the flow.

            If you want to schedule a flow by using times in a particular time zone, indicate the time zone as a UTC offset in your timestamps. For example, the UTC offsets for the ``America/New_York`` timezone are ``-04:00`` EDT and ``-05:00 EST`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-scheduledtriggerproperties.html#cfn-appflow-flow-scheduledtriggerproperties-timezone
            '''
            result = self._values.get("time_zone")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduledTriggerPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.ServiceNowSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ServiceNowSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when ServiceNow is being used as a source.

            :param object: The object specified in the ServiceNow flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-servicenowsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                service_now_source_properties_property = appflow.CfnFlow.ServiceNowSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f28c53e5a211cf01809013da71c5a7157f26d88b8459970752b72684cd630e2)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the ServiceNow flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-servicenowsourceproperties.html#cfn-appflow-flow-servicenowsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ServiceNowSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SingularSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class SingularSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Singular is being used as a source.

            :param object: The object specified in the Singular flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-singularsourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                singular_source_properties_property = appflow.CfnFlow.SingularSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__72f1fe6d35e37b171c76f4e32614f4188012e4108d512909e54f1c611343926e)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Singular flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-singularsourceproperties.html#cfn-appflow-flow-singularsourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SingularSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SlackSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class SlackSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when Slack is being used as a source.

            :param object: The object specified in the Slack flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-slacksourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                slack_source_properties_property = appflow.CfnFlow.SlackSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d3df173883e334f5de644d5ad1d7c83004e6b6ba99b20efe1bf8b36be60a5a6d)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Slack flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-slacksourceproperties.html#cfn-appflow-flow-slacksourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SlackSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SnowflakeDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "intermediate_bucket_name": "intermediateBucketName",
            "object": "object",
            "bucket_prefix": "bucketPrefix",
            "error_handling_config": "errorHandlingConfig",
        },
    )
    class SnowflakeDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            intermediate_bucket_name: builtins.str,
            object: builtins.str,
            bucket_prefix: typing.Optional[builtins.str] = None,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The properties that are applied when Snowflake is being used as a destination.

            :param intermediate_bucket_name: The intermediate bucket that Amazon AppFlow uses when moving data into Snowflake.
            :param object: The object specified in the Snowflake flow destination.
            :param bucket_prefix: The object key for the destination bucket in which Amazon AppFlow places the files.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the Snowflake destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                snowflake_destination_properties_property = appflow.CfnFlow.SnowflakeDestinationPropertiesProperty(
                    intermediate_bucket_name="intermediateBucketName",
                    object="object",
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix",
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__861db013349794673cd44026c51c9186e9b48c189f3d2f897e96326cf9022abd)
                check_type(argname="argument intermediate_bucket_name", value=intermediate_bucket_name, expected_type=type_hints["intermediate_bucket_name"])
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "intermediate_bucket_name": intermediate_bucket_name,
                "object": object,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config

        @builtins.property
        def intermediate_bucket_name(self) -> builtins.str:
            '''The intermediate bucket that Amazon AppFlow uses when moving data into Snowflake.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-intermediatebucketname
            '''
            result = self._values.get("intermediate_bucket_name")
            assert result is not None, "Required property 'intermediate_bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Snowflake flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the destination bucket in which Amazon AppFlow places the files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the Snowflake destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-snowflakedestinationproperties.html#cfn-appflow-flow-snowflakedestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnowflakeDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SourceConnectorPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "amplitude": "amplitude",
            "custom_connector": "customConnector",
            "datadog": "datadog",
            "dynatrace": "dynatrace",
            "google_analytics": "googleAnalytics",
            "infor_nexus": "inforNexus",
            "marketo": "marketo",
            "pardot": "pardot",
            "s3": "s3",
            "salesforce": "salesforce",
            "sapo_data": "sapoData",
            "service_now": "serviceNow",
            "singular": "singular",
            "slack": "slack",
            "trendmicro": "trendmicro",
            "veeva": "veeva",
            "zendesk": "zendesk",
        },
    )
    class SourceConnectorPropertiesProperty:
        def __init__(
            self,
            *,
            amplitude: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.AmplitudeSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.CustomConnectorSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.DatadogSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.DynatraceSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            google_analytics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.GoogleAnalyticsSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            infor_nexus: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.InforNexusSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.MarketoSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            pardot: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.PardotSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.S3SourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SalesforceSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SAPODataSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ServiceNowSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            singular: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SingularSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SlackSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            trendmicro: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.TrendmicroSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            veeva: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.VeevaSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ZendeskSourcePropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Specifies the information that is required to query a particular connector.

            :param amplitude: Specifies the information that is required for querying Amplitude.
            :param custom_connector: The properties that are applied when the custom connector is being used as a source.
            :param datadog: Specifies the information that is required for querying Datadog.
            :param dynatrace: Specifies the information that is required for querying Dynatrace.
            :param google_analytics: Specifies the information that is required for querying Google Analytics.
            :param infor_nexus: Specifies the information that is required for querying Infor Nexus.
            :param marketo: Specifies the information that is required for querying Marketo.
            :param pardot: Specifies the information that is required for querying Salesforce Pardot.
            :param s3: Specifies the information that is required for querying Amazon S3.
            :param salesforce: Specifies the information that is required for querying Salesforce.
            :param sapo_data: The properties that are applied when using SAPOData as a flow source.
            :param service_now: Specifies the information that is required for querying ServiceNow.
            :param singular: Specifies the information that is required for querying Singular.
            :param slack: Specifies the information that is required for querying Slack.
            :param trendmicro: Specifies the information that is required for querying Trend Micro.
            :param veeva: Specifies the information that is required for querying Veeva.
            :param zendesk: Specifies the information that is required for querying Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                source_connector_properties_property = appflow.CfnFlow.SourceConnectorPropertiesProperty(
                    amplitude=appflow.CfnFlow.AmplitudeSourcePropertiesProperty(
                        object="object"
                    ),
                    custom_connector=appflow.CfnFlow.CustomConnectorSourcePropertiesProperty(
                        entity_name="entityName",
                
                        # the properties below are optional
                        custom_properties={
                            "custom_properties_key": "customProperties"
                        },
                        data_transfer_api=appflow.CfnFlow.DataTransferApiProperty(
                            name="name",
                            type="type"
                        )
                    ),
                    datadog=appflow.CfnFlow.DatadogSourcePropertiesProperty(
                        object="object"
                    ),
                    dynatrace=appflow.CfnFlow.DynatraceSourcePropertiesProperty(
                        object="object"
                    ),
                    google_analytics=appflow.CfnFlow.GoogleAnalyticsSourcePropertiesProperty(
                        object="object"
                    ),
                    infor_nexus=appflow.CfnFlow.InforNexusSourcePropertiesProperty(
                        object="object"
                    ),
                    marketo=appflow.CfnFlow.MarketoSourcePropertiesProperty(
                        object="object"
                    ),
                    pardot=appflow.CfnFlow.PardotSourcePropertiesProperty(
                        object="object"
                    ),
                    s3=appflow.CfnFlow.S3SourcePropertiesProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                
                        # the properties below are optional
                        s3_input_format_config=appflow.CfnFlow.S3InputFormatConfigProperty(
                            s3_input_file_type="s3InputFileType"
                        )
                    ),
                    salesforce=appflow.CfnFlow.SalesforceSourcePropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        data_transfer_api="dataTransferApi",
                        enable_dynamic_field_update=False,
                        include_deleted_records=False
                    ),
                    sapo_data=appflow.CfnFlow.SAPODataSourcePropertiesProperty(
                        object_path="objectPath",
                
                        # the properties below are optional
                        pagination_config=appflow.CfnFlow.SAPODataPaginationConfigProperty(
                            max_page_size=123
                        ),
                        parallelism_config=appflow.CfnFlow.SAPODataParallelismConfigProperty(
                            max_parallelism=123
                        )
                    ),
                    service_now=appflow.CfnFlow.ServiceNowSourcePropertiesProperty(
                        object="object"
                    ),
                    singular=appflow.CfnFlow.SingularSourcePropertiesProperty(
                        object="object"
                    ),
                    slack=appflow.CfnFlow.SlackSourcePropertiesProperty(
                        object="object"
                    ),
                    trendmicro=appflow.CfnFlow.TrendmicroSourcePropertiesProperty(
                        object="object"
                    ),
                    veeva=appflow.CfnFlow.VeevaSourcePropertiesProperty(
                        object="object",
                
                        # the properties below are optional
                        document_type="documentType",
                        include_all_versions=False,
                        include_renditions=False,
                        include_source_files=False
                    ),
                    zendesk=appflow.CfnFlow.ZendeskSourcePropertiesProperty(
                        object="object"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bfca05ac628581510d78eb8880099b2c8d67e6218aeca321ae975f0979bb85af)
                check_type(argname="argument amplitude", value=amplitude, expected_type=type_hints["amplitude"])
                check_type(argname="argument custom_connector", value=custom_connector, expected_type=type_hints["custom_connector"])
                check_type(argname="argument datadog", value=datadog, expected_type=type_hints["datadog"])
                check_type(argname="argument dynatrace", value=dynatrace, expected_type=type_hints["dynatrace"])
                check_type(argname="argument google_analytics", value=google_analytics, expected_type=type_hints["google_analytics"])
                check_type(argname="argument infor_nexus", value=infor_nexus, expected_type=type_hints["infor_nexus"])
                check_type(argname="argument marketo", value=marketo, expected_type=type_hints["marketo"])
                check_type(argname="argument pardot", value=pardot, expected_type=type_hints["pardot"])
                check_type(argname="argument s3", value=s3, expected_type=type_hints["s3"])
                check_type(argname="argument salesforce", value=salesforce, expected_type=type_hints["salesforce"])
                check_type(argname="argument sapo_data", value=sapo_data, expected_type=type_hints["sapo_data"])
                check_type(argname="argument service_now", value=service_now, expected_type=type_hints["service_now"])
                check_type(argname="argument singular", value=singular, expected_type=type_hints["singular"])
                check_type(argname="argument slack", value=slack, expected_type=type_hints["slack"])
                check_type(argname="argument trendmicro", value=trendmicro, expected_type=type_hints["trendmicro"])
                check_type(argname="argument veeva", value=veeva, expected_type=type_hints["veeva"])
                check_type(argname="argument zendesk", value=zendesk, expected_type=type_hints["zendesk"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if amplitude is not None:
                self._values["amplitude"] = amplitude
            if custom_connector is not None:
                self._values["custom_connector"] = custom_connector
            if datadog is not None:
                self._values["datadog"] = datadog
            if dynatrace is not None:
                self._values["dynatrace"] = dynatrace
            if google_analytics is not None:
                self._values["google_analytics"] = google_analytics
            if infor_nexus is not None:
                self._values["infor_nexus"] = infor_nexus
            if marketo is not None:
                self._values["marketo"] = marketo
            if pardot is not None:
                self._values["pardot"] = pardot
            if s3 is not None:
                self._values["s3"] = s3
            if salesforce is not None:
                self._values["salesforce"] = salesforce
            if sapo_data is not None:
                self._values["sapo_data"] = sapo_data
            if service_now is not None:
                self._values["service_now"] = service_now
            if singular is not None:
                self._values["singular"] = singular
            if slack is not None:
                self._values["slack"] = slack
            if trendmicro is not None:
                self._values["trendmicro"] = trendmicro
            if veeva is not None:
                self._values["veeva"] = veeva
            if zendesk is not None:
                self._values["zendesk"] = zendesk

        @builtins.property
        def amplitude(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.AmplitudeSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Amplitude.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-amplitude
            '''
            result = self._values.get("amplitude")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.AmplitudeSourcePropertiesProperty"]], result)

        @builtins.property
        def custom_connector(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.CustomConnectorSourcePropertiesProperty"]]:
            '''The properties that are applied when the custom connector is being used as a source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-customconnector
            '''
            result = self._values.get("custom_connector")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.CustomConnectorSourcePropertiesProperty"]], result)

        @builtins.property
        def datadog(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.DatadogSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Datadog.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-datadog
            '''
            result = self._values.get("datadog")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.DatadogSourcePropertiesProperty"]], result)

        @builtins.property
        def dynatrace(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.DynatraceSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Dynatrace.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-dynatrace
            '''
            result = self._values.get("dynatrace")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.DynatraceSourcePropertiesProperty"]], result)

        @builtins.property
        def google_analytics(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.GoogleAnalyticsSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Google Analytics.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-googleanalytics
            '''
            result = self._values.get("google_analytics")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.GoogleAnalyticsSourcePropertiesProperty"]], result)

        @builtins.property
        def infor_nexus(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.InforNexusSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Infor Nexus.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-infornexus
            '''
            result = self._values.get("infor_nexus")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.InforNexusSourcePropertiesProperty"]], result)

        @builtins.property
        def marketo(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MarketoSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Marketo.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-marketo
            '''
            result = self._values.get("marketo")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.MarketoSourcePropertiesProperty"]], result)

        @builtins.property
        def pardot(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.PardotSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Salesforce Pardot.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-pardot
            '''
            result = self._values.get("pardot")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.PardotSourcePropertiesProperty"]], result)

        @builtins.property
        def s3(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3SourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Amazon S3.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-s3
            '''
            result = self._values.get("s3")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.S3SourcePropertiesProperty"]], result)

        @builtins.property
        def salesforce(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SalesforceSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Salesforce.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-salesforce
            '''
            result = self._values.get("salesforce")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SalesforceSourcePropertiesProperty"]], result)

        @builtins.property
        def sapo_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataSourcePropertiesProperty"]]:
            '''The properties that are applied when using SAPOData as a flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-sapodata
            '''
            result = self._values.get("sapo_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SAPODataSourcePropertiesProperty"]], result)

        @builtins.property
        def service_now(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ServiceNowSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying ServiceNow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-servicenow
            '''
            result = self._values.get("service_now")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ServiceNowSourcePropertiesProperty"]], result)

        @builtins.property
        def singular(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SingularSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Singular.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-singular
            '''
            result = self._values.get("singular")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SingularSourcePropertiesProperty"]], result)

        @builtins.property
        def slack(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SlackSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Slack.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-slack
            '''
            result = self._values.get("slack")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SlackSourcePropertiesProperty"]], result)

        @builtins.property
        def trendmicro(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.TrendmicroSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Trend Micro.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-trendmicro
            '''
            result = self._values.get("trendmicro")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.TrendmicroSourcePropertiesProperty"]], result)

        @builtins.property
        def veeva(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.VeevaSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Veeva.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-veeva
            '''
            result = self._values.get("veeva")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.VeevaSourcePropertiesProperty"]], result)

        @builtins.property
        def zendesk(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ZendeskSourcePropertiesProperty"]]:
            '''Specifies the information that is required for querying Zendesk.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceconnectorproperties.html#cfn-appflow-flow-sourceconnectorproperties-zendesk
            '''
            result = self._values.get("zendesk")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ZendeskSourcePropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceConnectorPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SourceFlowConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "connector_type": "connectorType",
            "source_connector_properties": "sourceConnectorProperties",
            "api_version": "apiVersion",
            "connector_profile_name": "connectorProfileName",
            "incremental_pull_config": "incrementalPullConfig",
        },
    )
    class SourceFlowConfigProperty:
        def __init__(
            self,
            *,
            connector_type: builtins.str,
            source_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SourceConnectorPropertiesProperty", typing.Dict[builtins.str, typing.Any]]],
            api_version: typing.Optional[builtins.str] = None,
            connector_profile_name: typing.Optional[builtins.str] = None,
            incremental_pull_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.IncrementalPullConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about the configuration of the source connector used in the flow.

            :param connector_type: The type of connector, such as Salesforce, Amplitude, and so on.
            :param source_connector_properties: Specifies the information that is required to query a particular source connector.
            :param api_version: The API version of the connector when it's used as a source in the flow.
            :param connector_profile_name: The name of the connector profile. This name must be unique for each connector profile in the AWS account .
            :param incremental_pull_config: Defines the configuration for a scheduled incremental data pull. If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                source_flow_config_property = appflow.CfnFlow.SourceFlowConfigProperty(
                    connector_type="connectorType",
                    source_connector_properties=appflow.CfnFlow.SourceConnectorPropertiesProperty(
                        amplitude=appflow.CfnFlow.AmplitudeSourcePropertiesProperty(
                            object="object"
                        ),
                        custom_connector=appflow.CfnFlow.CustomConnectorSourcePropertiesProperty(
                            entity_name="entityName",
                
                            # the properties below are optional
                            custom_properties={
                                "custom_properties_key": "customProperties"
                            },
                            data_transfer_api=appflow.CfnFlow.DataTransferApiProperty(
                                name="name",
                                type="type"
                            )
                        ),
                        datadog=appflow.CfnFlow.DatadogSourcePropertiesProperty(
                            object="object"
                        ),
                        dynatrace=appflow.CfnFlow.DynatraceSourcePropertiesProperty(
                            object="object"
                        ),
                        google_analytics=appflow.CfnFlow.GoogleAnalyticsSourcePropertiesProperty(
                            object="object"
                        ),
                        infor_nexus=appflow.CfnFlow.InforNexusSourcePropertiesProperty(
                            object="object"
                        ),
                        marketo=appflow.CfnFlow.MarketoSourcePropertiesProperty(
                            object="object"
                        ),
                        pardot=appflow.CfnFlow.PardotSourcePropertiesProperty(
                            object="object"
                        ),
                        s3=appflow.CfnFlow.S3SourcePropertiesProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
                
                            # the properties below are optional
                            s3_input_format_config=appflow.CfnFlow.S3InputFormatConfigProperty(
                                s3_input_file_type="s3InputFileType"
                            )
                        ),
                        salesforce=appflow.CfnFlow.SalesforceSourcePropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            data_transfer_api="dataTransferApi",
                            enable_dynamic_field_update=False,
                            include_deleted_records=False
                        ),
                        sapo_data=appflow.CfnFlow.SAPODataSourcePropertiesProperty(
                            object_path="objectPath",
                
                            # the properties below are optional
                            pagination_config=appflow.CfnFlow.SAPODataPaginationConfigProperty(
                                max_page_size=123
                            ),
                            parallelism_config=appflow.CfnFlow.SAPODataParallelismConfigProperty(
                                max_parallelism=123
                            )
                        ),
                        service_now=appflow.CfnFlow.ServiceNowSourcePropertiesProperty(
                            object="object"
                        ),
                        singular=appflow.CfnFlow.SingularSourcePropertiesProperty(
                            object="object"
                        ),
                        slack=appflow.CfnFlow.SlackSourcePropertiesProperty(
                            object="object"
                        ),
                        trendmicro=appflow.CfnFlow.TrendmicroSourcePropertiesProperty(
                            object="object"
                        ),
                        veeva=appflow.CfnFlow.VeevaSourcePropertiesProperty(
                            object="object",
                
                            # the properties below are optional
                            document_type="documentType",
                            include_all_versions=False,
                            include_renditions=False,
                            include_source_files=False
                        ),
                        zendesk=appflow.CfnFlow.ZendeskSourcePropertiesProperty(
                            object="object"
                        )
                    ),
                
                    # the properties below are optional
                    api_version="apiVersion",
                    connector_profile_name="connectorProfileName",
                    incremental_pull_config=appflow.CfnFlow.IncrementalPullConfigProperty(
                        datetime_type_field_name="datetimeTypeFieldName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__82f2b5bbb1f4a6eab214e7cfa4059986076879090f1ee5604886d749c25bc0af)
                check_type(argname="argument connector_type", value=connector_type, expected_type=type_hints["connector_type"])
                check_type(argname="argument source_connector_properties", value=source_connector_properties, expected_type=type_hints["source_connector_properties"])
                check_type(argname="argument api_version", value=api_version, expected_type=type_hints["api_version"])
                check_type(argname="argument connector_profile_name", value=connector_profile_name, expected_type=type_hints["connector_profile_name"])
                check_type(argname="argument incremental_pull_config", value=incremental_pull_config, expected_type=type_hints["incremental_pull_config"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "connector_type": connector_type,
                "source_connector_properties": source_connector_properties,
            }
            if api_version is not None:
                self._values["api_version"] = api_version
            if connector_profile_name is not None:
                self._values["connector_profile_name"] = connector_profile_name
            if incremental_pull_config is not None:
                self._values["incremental_pull_config"] = incremental_pull_config

        @builtins.property
        def connector_type(self) -> builtins.str:
            '''The type of connector, such as Salesforce, Amplitude, and so on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-connectortype
            '''
            result = self._values.get("connector_type")
            assert result is not None, "Required property 'connector_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_connector_properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceConnectorPropertiesProperty"]:
            '''Specifies the information that is required to query a particular source connector.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-sourceconnectorproperties
            '''
            result = self._values.get("source_connector_properties")
            assert result is not None, "Required property 'source_connector_properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceConnectorPropertiesProperty"], result)

        @builtins.property
        def api_version(self) -> typing.Optional[builtins.str]:
            '''The API version of the connector when it's used as a source in the flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-apiversion
            '''
            result = self._values.get("api_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def connector_profile_name(self) -> typing.Optional[builtins.str]:
            '''The name of the connector profile.

            This name must be unique for each connector profile in the AWS account .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-connectorprofilename
            '''
            result = self._values.get("connector_profile_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def incremental_pull_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.IncrementalPullConfigProperty"]]:
            '''Defines the configuration for a scheduled incremental data pull.

            If a valid configuration is provided, the fields specified in the configuration are used when querying for the incremental data pull.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-sourceflowconfig.html#cfn-appflow-flow-sourceflowconfig-incrementalpullconfig
            '''
            result = self._values.get("incremental_pull_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.IncrementalPullConfigProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourceFlowConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.SuccessResponseHandlingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName", "bucket_prefix": "bucketPrefix"},
    )
    class SuccessResponseHandlingConfigProperty:
        def __init__(
            self,
            *,
            bucket_name: typing.Optional[builtins.str] = None,
            bucket_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Determines how Amazon AppFlow handles the success response that it gets from the connector after placing data.

            For example, this setting would determine where to write the response from the destination connector upon a successful insert operation.

            :param bucket_name: The name of the Amazon S3 bucket.
            :param bucket_prefix: The Amazon S3 bucket prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                success_response_handling_config_property = appflow.CfnFlow.SuccessResponseHandlingConfigProperty(
                    bucket_name="bucketName",
                    bucket_prefix="bucketPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2abacd16b8046f3cf4c6b41305e1a136113c378aa704f9caf9caf85babd687f3)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket_name is not None:
                self._values["bucket_name"] = bucket_name
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix

        @builtins.property
        def bucket_name(self) -> typing.Optional[builtins.str]:
            '''The name of the Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html#cfn-appflow-flow-successresponsehandlingconfig-bucketname
            '''
            result = self._values.get("bucket_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The Amazon S3 bucket prefix.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-successresponsehandlingconfig.html#cfn-appflow-flow-successresponsehandlingconfig-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuccessResponseHandlingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.TaskPropertiesObjectProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class TaskPropertiesObjectProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A map used to store task-related information.

            The execution service looks for particular information based on the ``TaskType`` .

            :param key: The task property key.
            :param value: The task property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                task_properties_object_property = appflow.CfnFlow.TaskPropertiesObjectProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__979dcfb4514caff045d16804e80e950a4b994c418d975bfda1b058b9b48fced4)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The task property key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html#cfn-appflow-flow-taskpropertiesobject-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The task property value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-taskpropertiesobject.html#cfn-appflow-flow-taskpropertiesobject-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskPropertiesObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.TaskProperty",
        jsii_struct_bases=[],
        name_mapping={
            "source_fields": "sourceFields",
            "task_type": "taskType",
            "connector_operator": "connectorOperator",
            "destination_field": "destinationField",
            "task_properties": "taskProperties",
        },
    )
    class TaskProperty:
        def __init__(
            self,
            *,
            source_fields: typing.Sequence[builtins.str],
            task_type: builtins.str,
            connector_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ConnectorOperatorProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            destination_field: typing.Optional[builtins.str] = None,
            task_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.TaskPropertiesObjectProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''A class for modeling different type of tasks.

            Task implementation varies based on the ``TaskType`` .

            :param source_fields: The source fields to which a particular task is applied.
            :param task_type: Specifies the particular task implementation that Amazon AppFlow performs. *Allowed values* : ``Arithmetic`` | ``Filter`` | ``Map`` | ``Map_all`` | ``Mask`` | ``Merge`` | ``Truncate`` | ``Validate``
            :param connector_operator: The operation to be performed on the provided source fields.
            :param destination_field: A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.
            :param task_properties: A map used to store task-related information. The execution service looks for particular information based on the ``TaskType`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                task_property = appflow.CfnFlow.TaskProperty(
                    source_fields=["sourceFields"],
                    task_type="taskType",
                
                    # the properties below are optional
                    connector_operator=appflow.CfnFlow.ConnectorOperatorProperty(
                        amplitude="amplitude",
                        custom_connector="customConnector",
                        datadog="datadog",
                        dynatrace="dynatrace",
                        google_analytics="googleAnalytics",
                        infor_nexus="inforNexus",
                        marketo="marketo",
                        pardot="pardot",
                        s3="s3",
                        salesforce="salesforce",
                        sapo_data="sapoData",
                        service_now="serviceNow",
                        singular="singular",
                        slack="slack",
                        trendmicro="trendmicro",
                        veeva="veeva",
                        zendesk="zendesk"
                    ),
                    destination_field="destinationField",
                    task_properties=[appflow.CfnFlow.TaskPropertiesObjectProperty(
                        key="key",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__72c004cc65bad7fca9bee2b8e49d510b504af527bc9f31cdca10692f130cda87)
                check_type(argname="argument source_fields", value=source_fields, expected_type=type_hints["source_fields"])
                check_type(argname="argument task_type", value=task_type, expected_type=type_hints["task_type"])
                check_type(argname="argument connector_operator", value=connector_operator, expected_type=type_hints["connector_operator"])
                check_type(argname="argument destination_field", value=destination_field, expected_type=type_hints["destination_field"])
                check_type(argname="argument task_properties", value=task_properties, expected_type=type_hints["task_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "source_fields": source_fields,
                "task_type": task_type,
            }
            if connector_operator is not None:
                self._values["connector_operator"] = connector_operator
            if destination_field is not None:
                self._values["destination_field"] = destination_field
            if task_properties is not None:
                self._values["task_properties"] = task_properties

        @builtins.property
        def source_fields(self) -> typing.List[builtins.str]:
            '''The source fields to which a particular task is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-sourcefields
            '''
            result = self._values.get("source_fields")
            assert result is not None, "Required property 'source_fields' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def task_type(self) -> builtins.str:
            '''Specifies the particular task implementation that Amazon AppFlow performs.

            *Allowed values* : ``Arithmetic`` | ``Filter`` | ``Map`` | ``Map_all`` | ``Mask`` | ``Merge`` | ``Truncate`` | ``Validate``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-tasktype
            '''
            result = self._values.get("task_type")
            assert result is not None, "Required property 'task_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def connector_operator(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ConnectorOperatorProperty"]]:
            '''The operation to be performed on the provided source fields.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-connectoroperator
            '''
            result = self._values.get("connector_operator")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ConnectorOperatorProperty"]], result)

        @builtins.property
        def destination_field(self) -> typing.Optional[builtins.str]:
            '''A field in a destination connector, or a field value against which Amazon AppFlow validates a source field.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-destinationfield
            '''
            result = self._values.get("destination_field")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def task_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.TaskPropertiesObjectProperty"]]]]:
            '''A map used to store task-related information.

            The execution service looks for particular information based on the ``TaskType`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-task.html#cfn-appflow-flow-task-taskproperties
            '''
            result = self._values.get("task_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFlow.TaskPropertiesObjectProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TaskProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.TrendmicroSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class TrendmicroSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when using Trend Micro as a flow source.

            :param object: The object specified in the Trend Micro flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-trendmicrosourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                trendmicro_source_properties_property = appflow.CfnFlow.TrendmicroSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__41cf6b7146e8303d1b50511d2818edd5e3c2dfa0eab59171dd6d9b24f3cbfa80)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Trend Micro flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-trendmicrosourceproperties.html#cfn-appflow-flow-trendmicrosourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrendmicroSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.TriggerConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "trigger_type": "triggerType",
            "trigger_properties": "triggerProperties",
        },
    )
    class TriggerConfigProperty:
        def __init__(
            self,
            *,
            trigger_type: builtins.str,
            trigger_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ScheduledTriggerPropertiesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The trigger settings that determine how and when Amazon AppFlow runs the specified flow.

            :param trigger_type: Specifies the type of flow trigger. This can be ``OnDemand`` , ``Scheduled`` , or ``Event`` .
            :param trigger_properties: Specifies the configuration details of a schedule-triggered flow as defined by the user. Currently, these settings only apply to the ``Scheduled`` trigger type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                trigger_config_property = appflow.CfnFlow.TriggerConfigProperty(
                    trigger_type="triggerType",
                
                    # the properties below are optional
                    trigger_properties=appflow.CfnFlow.ScheduledTriggerPropertiesProperty(
                        schedule_expression="scheduleExpression",
                
                        # the properties below are optional
                        data_pull_mode="dataPullMode",
                        first_execution_from=123,
                        flow_error_deactivation_threshold=123,
                        schedule_end_time=123,
                        schedule_offset=123,
                        schedule_start_time=123,
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cd28ca462b3e9e4f32cc44aec4e8810188f62b59f8d2642880f795974ed7aabc)
                check_type(argname="argument trigger_type", value=trigger_type, expected_type=type_hints["trigger_type"])
                check_type(argname="argument trigger_properties", value=trigger_properties, expected_type=type_hints["trigger_properties"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "trigger_type": trigger_type,
            }
            if trigger_properties is not None:
                self._values["trigger_properties"] = trigger_properties

        @builtins.property
        def trigger_type(self) -> builtins.str:
            '''Specifies the type of flow trigger.

            This can be ``OnDemand`` , ``Scheduled`` , or ``Event`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html#cfn-appflow-flow-triggerconfig-triggertype
            '''
            result = self._values.get("trigger_type")
            assert result is not None, "Required property 'trigger_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def trigger_properties(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ScheduledTriggerPropertiesProperty"]]:
            '''Specifies the configuration details of a schedule-triggered flow as defined by the user.

            Currently, these settings only apply to the ``Scheduled`` trigger type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-triggerconfig.html#cfn-appflow-flow-triggerconfig-triggerproperties
            '''
            result = self._values.get("trigger_properties")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ScheduledTriggerPropertiesProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TriggerConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.UpsolverDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "s3_output_format_config": "s3OutputFormatConfig",
            "bucket_prefix": "bucketPrefix",
        },
    )
    class UpsolverDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            s3_output_format_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.UpsolverS3OutputFormatConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            bucket_prefix: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when Upsolver is used as a destination.

            :param bucket_name: The Upsolver Amazon S3 bucket name in which Amazon AppFlow places the transferred data.
            :param s3_output_format_config: The configuration that determines how data is formatted when Upsolver is used as the flow destination.
            :param bucket_prefix: The object key for the destination Upsolver Amazon S3 bucket in which Amazon AppFlow places the files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                upsolver_destination_properties_property = appflow.CfnFlow.UpsolverDestinationPropertiesProperty(
                    bucket_name="bucketName",
                    s3_output_format_config=appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty(
                        prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                            path_prefix_hierarchy=["pathPrefixHierarchy"],
                            prefix_format="prefixFormat",
                            prefix_type="prefixType"
                        ),
                
                        # the properties below are optional
                        aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                            aggregation_type="aggregationType",
                            target_file_size=123
                        ),
                        file_type="fileType"
                    ),
                
                    # the properties below are optional
                    bucket_prefix="bucketPrefix"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__05785a870fff4b04759a9e76167dfd9a3a7b02a191fa2a196cf1fcf2f10cc020)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument s3_output_format_config", value=s3_output_format_config, expected_type=type_hints["s3_output_format_config"])
                check_type(argname="argument bucket_prefix", value=bucket_prefix, expected_type=type_hints["bucket_prefix"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
                "s3_output_format_config": s3_output_format_config,
            }
            if bucket_prefix is not None:
                self._values["bucket_prefix"] = bucket_prefix

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The Upsolver Amazon S3 bucket name in which Amazon AppFlow places the transferred data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html#cfn-appflow-flow-upsolverdestinationproperties-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def s3_output_format_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.UpsolverS3OutputFormatConfigProperty"]:
            '''The configuration that determines how data is formatted when Upsolver is used as the flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html#cfn-appflow-flow-upsolverdestinationproperties-s3outputformatconfig
            '''
            result = self._values.get("s3_output_format_config")
            assert result is not None, "Required property 's3_output_format_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.UpsolverS3OutputFormatConfigProperty"], result)

        @builtins.property
        def bucket_prefix(self) -> typing.Optional[builtins.str]:
            '''The object key for the destination Upsolver Amazon S3 bucket in which Amazon AppFlow places the files.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolverdestinationproperties.html#cfn-appflow-flow-upsolverdestinationproperties-bucketprefix
            '''
            result = self._values.get("bucket_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpsolverDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "prefix_config": "prefixConfig",
            "aggregation_config": "aggregationConfig",
            "file_type": "fileType",
        },
    )
    class UpsolverS3OutputFormatConfigProperty:
        def __init__(
            self,
            *,
            prefix_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.PrefixConfigProperty", typing.Dict[builtins.str, typing.Any]]],
            aggregation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.AggregationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            file_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration that determines how Amazon AppFlow formats the flow output data when Upsolver is used as the destination.

            :param prefix_config: Specifies elements that Amazon AppFlow includes in the file and folder names in the flow destination.
            :param aggregation_config: The aggregation settings that you can use to customize the output format of your flow data.
            :param file_type: Indicates the file type that Amazon AppFlow places in the Upsolver Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                upsolver_s3_output_format_config_property = appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty(
                    prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                        path_prefix_hierarchy=["pathPrefixHierarchy"],
                        prefix_format="prefixFormat",
                        prefix_type="prefixType"
                    ),
                
                    # the properties below are optional
                    aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                        aggregation_type="aggregationType",
                        target_file_size=123
                    ),
                    file_type="fileType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc27a8a1f41dd89c26ea1554f69fb21c1553a7bdaf514ef9f0b77024672f8e1f)
                check_type(argname="argument prefix_config", value=prefix_config, expected_type=type_hints["prefix_config"])
                check_type(argname="argument aggregation_config", value=aggregation_config, expected_type=type_hints["aggregation_config"])
                check_type(argname="argument file_type", value=file_type, expected_type=type_hints["file_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "prefix_config": prefix_config,
            }
            if aggregation_config is not None:
                self._values["aggregation_config"] = aggregation_config
            if file_type is not None:
                self._values["file_type"] = file_type

        @builtins.property
        def prefix_config(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.PrefixConfigProperty"]:
            '''Specifies elements that Amazon AppFlow includes in the file and folder names in the flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html#cfn-appflow-flow-upsolvers3outputformatconfig-prefixconfig
            '''
            result = self._values.get("prefix_config")
            assert result is not None, "Required property 'prefix_config' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.PrefixConfigProperty"], result)

        @builtins.property
        def aggregation_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.AggregationConfigProperty"]]:
            '''The aggregation settings that you can use to customize the output format of your flow data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html#cfn-appflow-flow-upsolvers3outputformatconfig-aggregationconfig
            '''
            result = self._values.get("aggregation_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.AggregationConfigProperty"]], result)

        @builtins.property
        def file_type(self) -> typing.Optional[builtins.str]:
            '''Indicates the file type that Amazon AppFlow places in the Upsolver Amazon S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-upsolvers3outputformatconfig.html#cfn-appflow-flow-upsolvers3outputformatconfig-filetype
            '''
            result = self._values.get("file_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UpsolverS3OutputFormatConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.VeevaSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "document_type": "documentType",
            "include_all_versions": "includeAllVersions",
            "include_renditions": "includeRenditions",
            "include_source_files": "includeSourceFiles",
        },
    )
    class VeevaSourcePropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            document_type: typing.Optional[builtins.str] = None,
            include_all_versions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_renditions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_source_files: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The properties that are applied when using Veeva as a flow source.

            :param object: The object specified in the Veeva flow source.
            :param document_type: The document type specified in the Veeva document extract flow.
            :param include_all_versions: Boolean value to include All Versions of files in Veeva document extract flow.
            :param include_renditions: Boolean value to include file renditions in Veeva document extract flow.
            :param include_source_files: Boolean value to include source files in Veeva document extract flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                veeva_source_properties_property = appflow.CfnFlow.VeevaSourcePropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    document_type="documentType",
                    include_all_versions=False,
                    include_renditions=False,
                    include_source_files=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33eb5d9916f4bbfdcb7645bab52a5e8a99175f5473686f4922323cb792470b88)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument document_type", value=document_type, expected_type=type_hints["document_type"])
                check_type(argname="argument include_all_versions", value=include_all_versions, expected_type=type_hints["include_all_versions"])
                check_type(argname="argument include_renditions", value=include_renditions, expected_type=type_hints["include_renditions"])
                check_type(argname="argument include_source_files", value=include_source_files, expected_type=type_hints["include_source_files"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if document_type is not None:
                self._values["document_type"] = document_type
            if include_all_versions is not None:
                self._values["include_all_versions"] = include_all_versions
            if include_renditions is not None:
                self._values["include_renditions"] = include_renditions
            if include_source_files is not None:
                self._values["include_source_files"] = include_source_files

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Veeva flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def document_type(self) -> typing.Optional[builtins.str]:
            '''The document type specified in the Veeva document extract flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-documenttype
            '''
            result = self._values.get("document_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def include_all_versions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean value to include All Versions of files in Veeva document extract flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-includeallversions
            '''
            result = self._values.get("include_all_versions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_renditions(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean value to include file renditions in Veeva document extract flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-includerenditions
            '''
            result = self._values.get("include_renditions")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_source_files(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Boolean value to include source files in Veeva document extract flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-veevasourceproperties.html#cfn-appflow-flow-veevasourceproperties-includesourcefiles
            '''
            result = self._values.get("include_source_files")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VeevaSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.ZendeskDestinationPropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "object": "object",
            "error_handling_config": "errorHandlingConfig",
            "id_field_names": "idFieldNames",
            "write_operation_type": "writeOperationType",
        },
    )
    class ZendeskDestinationPropertiesProperty:
        def __init__(
            self,
            *,
            object: builtins.str,
            error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.ErrorHandlingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
            write_operation_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The properties that are applied when Zendesk is used as a destination.

            :param object: The object specified in the Zendesk flow destination.
            :param error_handling_config: The settings that determine how Amazon AppFlow handles an error when placing data in the destination. For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.
            :param id_field_names: A list of field names that can be used as an ID field when performing a write operation.
            :param write_operation_type: The possible write operations in the destination connector. When this value is not provided, this defaults to the ``INSERT`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                zendesk_destination_properties_property = appflow.CfnFlow.ZendeskDestinationPropertiesProperty(
                    object="object",
                
                    # the properties below are optional
                    error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                        bucket_name="bucketName",
                        bucket_prefix="bucketPrefix",
                        fail_on_first_error=False
                    ),
                    id_field_names=["idFieldNames"],
                    write_operation_type="writeOperationType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b408dbbead0815b59be3690c6532ce03b6ccc36638f38661f96d1b80187c2dd4)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
                check_type(argname="argument error_handling_config", value=error_handling_config, expected_type=type_hints["error_handling_config"])
                check_type(argname="argument id_field_names", value=id_field_names, expected_type=type_hints["id_field_names"])
                check_type(argname="argument write_operation_type", value=write_operation_type, expected_type=type_hints["write_operation_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }
            if error_handling_config is not None:
                self._values["error_handling_config"] = error_handling_config
            if id_field_names is not None:
                self._values["id_field_names"] = id_field_names
            if write_operation_type is not None:
                self._values["write_operation_type"] = write_operation_type

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Zendesk flow destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def error_handling_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]]:
            '''The settings that determine how Amazon AppFlow handles an error when placing data in the destination.

            For example, this setting would determine if the flow should fail after one insertion error, or continue and attempt to insert every record regardless of the initial failure. ``ErrorHandlingConfig`` is a part of the destination connector details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-errorhandlingconfig
            '''
            result = self._values.get("error_handling_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.ErrorHandlingConfigProperty"]], result)

        @builtins.property
        def id_field_names(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of field names that can be used as an ID field when performing a write operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-idfieldnames
            '''
            result = self._values.get("id_field_names")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def write_operation_type(self) -> typing.Optional[builtins.str]:
            '''The possible write operations in the destination connector.

            When this value is not provided, this defaults to the ``INSERT`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendeskdestinationproperties.html#cfn-appflow-flow-zendeskdestinationproperties-writeoperationtype
            '''
            result = self._values.get("write_operation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskDestinationPropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_appflow.CfnFlow.ZendeskSourcePropertiesProperty",
        jsii_struct_bases=[],
        name_mapping={"object": "object"},
    )
    class ZendeskSourcePropertiesProperty:
        def __init__(self, *, object: builtins.str) -> None:
            '''The properties that are applied when using Zendesk as a flow source.

            :param object: The object specified in the Zendesk flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendesksourceproperties.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_appflow as appflow
                
                zendesk_source_properties_property = appflow.CfnFlow.ZendeskSourcePropertiesProperty(
                    object="object"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__97d56d701da8e030ea893f9e410a42eda76f5e8d95fbaeafd8ab06b3ff38829a)
                check_type(argname="argument object", value=object, expected_type=type_hints["object"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "object": object,
            }

        @builtins.property
        def object(self) -> builtins.str:
            '''The object specified in the Zendesk flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-appflow-flow-zendesksourceproperties.html#cfn-appflow-flow-zendesksourceproperties-object
            '''
            result = self._values.get("object")
            assert result is not None, "Required property 'object' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ZendeskSourcePropertiesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_appflow.CfnFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "destination_flow_config_list": "destinationFlowConfigList",
        "flow_name": "flowName",
        "source_flow_config": "sourceFlowConfig",
        "tasks": "tasks",
        "trigger_config": "triggerConfig",
        "description": "description",
        "flow_status": "flowStatus",
        "kms_arn": "kmsArn",
        "metadata_catalog_config": "metadataCatalogConfig",
        "tags": "tags",
    },
)
class CfnFlowProps:
    def __init__(
        self,
        *,
        destination_flow_config_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DestinationFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
        flow_name: builtins.str,
        source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TaskProperty, typing.Dict[builtins.str, typing.Any]]]]],
        trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        description: typing.Optional[builtins.str] = None,
        flow_status: typing.Optional[builtins.str] = None,
        kms_arn: typing.Optional[builtins.str] = None,
        metadata_catalog_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MetadataCatalogConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlow``.

        :param destination_flow_config_list: The configuration that controls how Amazon AppFlow places data in the destination connector.
        :param flow_name: The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only.
        :param source_flow_config: Contains information about the configuration of the source connector used in the flow.
        :param tasks: A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.
        :param trigger_config: The trigger settings that determine how and when Amazon AppFlow runs the specified flow.
        :param description: A user-entered description of the flow.
        :param flow_status: Sets the status of the flow. You can specify one of the following values:. - **Active** - The flow runs based on the trigger settings that you defined. Active scheduled flows run as scheduled, and active event-triggered flows run when the specified change event occurs. However, active on-demand flows run only when you manually start them by using Amazon AppFlow. - **Suspended** - You can use this option to deactivate an active flow. Scheduled and event-triggered flows will cease to run until you reactive them. This value only affects scheduled and event-triggered flows. It has no effect for on-demand flows. If you omit the FlowStatus parameter, Amazon AppFlow creates the flow with a default status. The default status for on-demand flows is Active. The default status for scheduled and event-triggered flows is Draft, which means they’re not yet active.
        :param kms_arn: The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.
        :param metadata_catalog_config: Specifies the configuration that Amazon AppFlow uses when it catalogs your data. When Amazon AppFlow catalogs your data, it stores metadata in a data catalog.
        :param tags: The tags used to organize, track, or control access for your flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_appflow as appflow
            
            cfn_flow_props = appflow.CfnFlowProps(
                destination_flow_config_list=[appflow.CfnFlow.DestinationFlowConfigProperty(
                    connector_type="connectorType",
                    destination_connector_properties=appflow.CfnFlow.DestinationConnectorPropertiesProperty(
                        custom_connector=appflow.CfnFlow.CustomConnectorDestinationPropertiesProperty(
                            entity_name="entityName",
            
                            # the properties below are optional
                            custom_properties={
                                "custom_properties_key": "customProperties"
                            },
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            write_operation_type="writeOperationType"
                        ),
                        event_bridge=appflow.CfnFlow.EventBridgeDestinationPropertiesProperty(
                            object="object",
            
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        lookout_metrics=appflow.CfnFlow.LookoutMetricsDestinationPropertiesProperty(
                            object="object"
                        ),
                        marketo=appflow.CfnFlow.MarketoDestinationPropertiesProperty(
                            object="object",
            
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        redshift=appflow.CfnFlow.RedshiftDestinationPropertiesProperty(
                            intermediate_bucket_name="intermediateBucketName",
                            object="object",
            
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        s3=appflow.CfnFlow.S3DestinationPropertiesProperty(
                            bucket_name="bucketName",
            
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            s3_output_format_config=appflow.CfnFlow.S3OutputFormatConfigProperty(
                                aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                    aggregation_type="aggregationType",
                                    target_file_size=123
                                ),
                                file_type="fileType",
                                prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                    path_prefix_hierarchy=["pathPrefixHierarchy"],
                                    prefix_format="prefixFormat",
                                    prefix_type="prefixType"
                                ),
                                preserve_source_data_typing=False
                            )
                        ),
                        salesforce=appflow.CfnFlow.SalesforceDestinationPropertiesProperty(
                            object="object",
            
                            # the properties below are optional
                            data_transfer_api="dataTransferApi",
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            write_operation_type="writeOperationType"
                        ),
                        sapo_data=appflow.CfnFlow.SAPODataDestinationPropertiesProperty(
                            object_path="objectPath",
            
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            success_response_handling_config=appflow.CfnFlow.SuccessResponseHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix"
                            ),
                            write_operation_type="writeOperationType"
                        ),
                        snowflake=appflow.CfnFlow.SnowflakeDestinationPropertiesProperty(
                            intermediate_bucket_name="intermediateBucketName",
                            object="object",
            
                            # the properties below are optional
                            bucket_prefix="bucketPrefix",
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            )
                        ),
                        upsolver=appflow.CfnFlow.UpsolverDestinationPropertiesProperty(
                            bucket_name="bucketName",
                            s3_output_format_config=appflow.CfnFlow.UpsolverS3OutputFormatConfigProperty(
                                prefix_config=appflow.CfnFlow.PrefixConfigProperty(
                                    path_prefix_hierarchy=["pathPrefixHierarchy"],
                                    prefix_format="prefixFormat",
                                    prefix_type="prefixType"
                                ),
            
                                # the properties below are optional
                                aggregation_config=appflow.CfnFlow.AggregationConfigProperty(
                                    aggregation_type="aggregationType",
                                    target_file_size=123
                                ),
                                file_type="fileType"
                            ),
            
                            # the properties below are optional
                            bucket_prefix="bucketPrefix"
                        ),
                        zendesk=appflow.CfnFlow.ZendeskDestinationPropertiesProperty(
                            object="object",
            
                            # the properties below are optional
                            error_handling_config=appflow.CfnFlow.ErrorHandlingConfigProperty(
                                bucket_name="bucketName",
                                bucket_prefix="bucketPrefix",
                                fail_on_first_error=False
                            ),
                            id_field_names=["idFieldNames"],
                            write_operation_type="writeOperationType"
                        )
                    ),
            
                    # the properties below are optional
                    api_version="apiVersion",
                    connector_profile_name="connectorProfileName"
                )],
                flow_name="flowName",
                source_flow_config=appflow.CfnFlow.SourceFlowConfigProperty(
                    connector_type="connectorType",
                    source_connector_properties=appflow.CfnFlow.SourceConnectorPropertiesProperty(
                        amplitude=appflow.CfnFlow.AmplitudeSourcePropertiesProperty(
                            object="object"
                        ),
                        custom_connector=appflow.CfnFlow.CustomConnectorSourcePropertiesProperty(
                            entity_name="entityName",
            
                            # the properties below are optional
                            custom_properties={
                                "custom_properties_key": "customProperties"
                            },
                            data_transfer_api=appflow.CfnFlow.DataTransferApiProperty(
                                name="name",
                                type="type"
                            )
                        ),
                        datadog=appflow.CfnFlow.DatadogSourcePropertiesProperty(
                            object="object"
                        ),
                        dynatrace=appflow.CfnFlow.DynatraceSourcePropertiesProperty(
                            object="object"
                        ),
                        google_analytics=appflow.CfnFlow.GoogleAnalyticsSourcePropertiesProperty(
                            object="object"
                        ),
                        infor_nexus=appflow.CfnFlow.InforNexusSourcePropertiesProperty(
                            object="object"
                        ),
                        marketo=appflow.CfnFlow.MarketoSourcePropertiesProperty(
                            object="object"
                        ),
                        pardot=appflow.CfnFlow.PardotSourcePropertiesProperty(
                            object="object"
                        ),
                        s3=appflow.CfnFlow.S3SourcePropertiesProperty(
                            bucket_name="bucketName",
                            bucket_prefix="bucketPrefix",
            
                            # the properties below are optional
                            s3_input_format_config=appflow.CfnFlow.S3InputFormatConfigProperty(
                                s3_input_file_type="s3InputFileType"
                            )
                        ),
                        salesforce=appflow.CfnFlow.SalesforceSourcePropertiesProperty(
                            object="object",
            
                            # the properties below are optional
                            data_transfer_api="dataTransferApi",
                            enable_dynamic_field_update=False,
                            include_deleted_records=False
                        ),
                        sapo_data=appflow.CfnFlow.SAPODataSourcePropertiesProperty(
                            object_path="objectPath",
            
                            # the properties below are optional
                            pagination_config=appflow.CfnFlow.SAPODataPaginationConfigProperty(
                                max_page_size=123
                            ),
                            parallelism_config=appflow.CfnFlow.SAPODataParallelismConfigProperty(
                                max_parallelism=123
                            )
                        ),
                        service_now=appflow.CfnFlow.ServiceNowSourcePropertiesProperty(
                            object="object"
                        ),
                        singular=appflow.CfnFlow.SingularSourcePropertiesProperty(
                            object="object"
                        ),
                        slack=appflow.CfnFlow.SlackSourcePropertiesProperty(
                            object="object"
                        ),
                        trendmicro=appflow.CfnFlow.TrendmicroSourcePropertiesProperty(
                            object="object"
                        ),
                        veeva=appflow.CfnFlow.VeevaSourcePropertiesProperty(
                            object="object",
            
                            # the properties below are optional
                            document_type="documentType",
                            include_all_versions=False,
                            include_renditions=False,
                            include_source_files=False
                        ),
                        zendesk=appflow.CfnFlow.ZendeskSourcePropertiesProperty(
                            object="object"
                        )
                    ),
            
                    # the properties below are optional
                    api_version="apiVersion",
                    connector_profile_name="connectorProfileName",
                    incremental_pull_config=appflow.CfnFlow.IncrementalPullConfigProperty(
                        datetime_type_field_name="datetimeTypeFieldName"
                    )
                ),
                tasks=[appflow.CfnFlow.TaskProperty(
                    source_fields=["sourceFields"],
                    task_type="taskType",
            
                    # the properties below are optional
                    connector_operator=appflow.CfnFlow.ConnectorOperatorProperty(
                        amplitude="amplitude",
                        custom_connector="customConnector",
                        datadog="datadog",
                        dynatrace="dynatrace",
                        google_analytics="googleAnalytics",
                        infor_nexus="inforNexus",
                        marketo="marketo",
                        pardot="pardot",
                        s3="s3",
                        salesforce="salesforce",
                        sapo_data="sapoData",
                        service_now="serviceNow",
                        singular="singular",
                        slack="slack",
                        trendmicro="trendmicro",
                        veeva="veeva",
                        zendesk="zendesk"
                    ),
                    destination_field="destinationField",
                    task_properties=[appflow.CfnFlow.TaskPropertiesObjectProperty(
                        key="key",
                        value="value"
                    )]
                )],
                trigger_config=appflow.CfnFlow.TriggerConfigProperty(
                    trigger_type="triggerType",
            
                    # the properties below are optional
                    trigger_properties=appflow.CfnFlow.ScheduledTriggerPropertiesProperty(
                        schedule_expression="scheduleExpression",
            
                        # the properties below are optional
                        data_pull_mode="dataPullMode",
                        first_execution_from=123,
                        flow_error_deactivation_threshold=123,
                        schedule_end_time=123,
                        schedule_offset=123,
                        schedule_start_time=123,
                        time_zone="timeZone"
                    )
                ),
            
                # the properties below are optional
                description="description",
                flow_status="flowStatus",
                kms_arn="kmsArn",
                metadata_catalog_config=appflow.CfnFlow.MetadataCatalogConfigProperty(
                    glue_data_catalog=appflow.CfnFlow.GlueDataCatalogProperty(
                        database_name="databaseName",
                        role_arn="roleArn",
                        table_prefix="tablePrefix"
                    )
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85045c56f5ed71ad46fec6374ddad0e03a173028630204629542088fb8766ae9)
            check_type(argname="argument destination_flow_config_list", value=destination_flow_config_list, expected_type=type_hints["destination_flow_config_list"])
            check_type(argname="argument flow_name", value=flow_name, expected_type=type_hints["flow_name"])
            check_type(argname="argument source_flow_config", value=source_flow_config, expected_type=type_hints["source_flow_config"])
            check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
            check_type(argname="argument trigger_config", value=trigger_config, expected_type=type_hints["trigger_config"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flow_status", value=flow_status, expected_type=type_hints["flow_status"])
            check_type(argname="argument kms_arn", value=kms_arn, expected_type=type_hints["kms_arn"])
            check_type(argname="argument metadata_catalog_config", value=metadata_catalog_config, expected_type=type_hints["metadata_catalog_config"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination_flow_config_list": destination_flow_config_list,
            "flow_name": flow_name,
            "source_flow_config": source_flow_config,
            "tasks": tasks,
            "trigger_config": trigger_config,
        }
        if description is not None:
            self._values["description"] = description
        if flow_status is not None:
            self._values["flow_status"] = flow_status
        if kms_arn is not None:
            self._values["kms_arn"] = kms_arn
        if metadata_catalog_config is not None:
            self._values["metadata_catalog_config"] = metadata_catalog_config
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def destination_flow_config_list(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.DestinationFlowConfigProperty]]]:
        '''The configuration that controls how Amazon AppFlow places data in the destination connector.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-destinationflowconfiglist
        '''
        result = self._values.get("destination_flow_config_list")
        assert result is not None, "Required property 'destination_flow_config_list' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.DestinationFlowConfigProperty]]], result)

    @builtins.property
    def flow_name(self) -> builtins.str:
        '''The specified name of the flow.

        Spaces are not allowed. Use underscores (_) or hyphens (-) only.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-flowname
        '''
        result = self._values.get("flow_name")
        assert result is not None, "Required property 'flow_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_flow_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFlow.SourceFlowConfigProperty]:
        '''Contains information about the configuration of the source connector used in the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-sourceflowconfig
        '''
        result = self._values.get("source_flow_config")
        assert result is not None, "Required property 'source_flow_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFlow.SourceFlowConfigProperty], result)

    @builtins.property
    def tasks(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.TaskProperty]]]:
        '''A list of tasks that Amazon AppFlow performs while transferring the data in the flow run.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-tasks
        '''
        result = self._values.get("tasks")
        assert result is not None, "Required property 'tasks' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.TaskProperty]]], result)

    @builtins.property
    def trigger_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFlow.TriggerConfigProperty]:
        '''The trigger settings that determine how and when Amazon AppFlow runs the specified flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-triggerconfig
        '''
        result = self._values.get("trigger_config")
        assert result is not None, "Required property 'trigger_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFlow.TriggerConfigProperty], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A user-entered description of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_status(self) -> typing.Optional[builtins.str]:
        '''Sets the status of the flow. You can specify one of the following values:.

        - **Active** - The flow runs based on the trigger settings that you defined. Active scheduled flows run as scheduled, and active event-triggered flows run when the specified change event occurs. However, active on-demand flows run only when you manually start them by using Amazon AppFlow.
        - **Suspended** - You can use this option to deactivate an active flow. Scheduled and event-triggered flows will cease to run until you reactive them. This value only affects scheduled and event-triggered flows. It has no effect for on-demand flows.

        If you omit the FlowStatus parameter, Amazon AppFlow creates the flow with a default status. The default status for on-demand flows is Active. The default status for scheduled and event-triggered flows is Draft, which means they’re not yet active.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-flowstatus
        '''
        result = self._values.get("flow_status")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption.

        This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you don't provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-kmsarn
        '''
        result = self._values.get("kms_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def metadata_catalog_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.MetadataCatalogConfigProperty]]:
        '''Specifies the configuration that Amazon AppFlow uses when it catalogs your data.

        When Amazon AppFlow catalogs your data, it stores metadata in a data catalog.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-metadatacatalogconfig
        '''
        result = self._values.get("metadata_catalog_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.MetadataCatalogConfigProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags used to organize, track, or control access for your flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-appflow-flow.html#cfn-appflow-flow-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnConnector",
    "CfnConnectorProfile",
    "CfnConnectorProfileProps",
    "CfnConnectorProps",
    "CfnFlow",
    "CfnFlowProps",
]

publication.publish()

def _typecheckingstub__6bcd4af5099c6e263b309786f40e217a7b9534ca68e65e020a22b581160f7869(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connector_provisioning_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ConnectorProvisioningConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    connector_provisioning_type: builtins.str,
    connector_label: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02fe175937a3851291cfe730cc744110fbd6b06062b2f72be6c64c38cb811cc2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14908eefe331e5d6c90e4d41161c6e2df84fc31fc2c80c358aacd6d72b71fdad(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9a08650fe9a17324090179ab56d9509e56252c9865e3f2e1fa676c14b6cc03f(
    value: typing.Union[_IResolvable_da3f097b, CfnConnector.ConnectorProvisioningConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2220ebaf0220a2885b5b9cf115ec38fe35115066c974f84c1b2c720720335fc(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__223722b79e59f7d76338e4d79ccc19e3b7a392375aa34d0c39efd833af999447(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5201599f188c2814b1848bd455a0576a0e0a2d098b49d428d52355c42d74246a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f30575b197aa2e677da77a036dc5bfce7d878974062d45e335a7a1ace3bb43fa(
    *,
    lambda_: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.LambdaConnectorProvisioningConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1eac52f23e3de5229c743187d6ff0c48af0c8b82a08a1bfe7aa685c49794c096(
    *,
    lambda_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fdda7d6a6b65c327fe887afce3342c78cebf6c60dd8655f2dcd7b8281583efc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    connection_mode: builtins.str,
    connector_profile_name: builtins.str,
    connector_type: builtins.str,
    connector_label: typing.Optional[builtins.str] = None,
    connector_profile_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorProfileConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89b2a22e671284a42946f894ce72068c41b76bb904059c7bed5e45c71d48dc5a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7b41f256b139e247bf8134c2dd0c80d99ca4ee9371e5685482e353a92d8e09a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92b6f068ed3430ff60d5cf2405ae08acfe160b8a4162a018961ac832d027d84a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cb5b0aaad75445c153fba71fd8dbff5d452ea9073e2056f9b9b2deac384c665(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34d4fdd4dbf7a059cab33b55ce7b81ced574f12c8c437ab87f6a2cd0366b8c27(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__67b7946ef6d997ddf9c382bd294994647bbe3c0ad1aaaceece977af3d6112719(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3377e00c38f6ec97040c9514a9f9cedd23ba70e3a2b918fb7ef76f04aca7d060(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConnectorProfile.ConnectorProfileConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__089ca49f64f5b669f9596470a2fc8cf66e307ab5bdaedd126556de9e245a2adf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3d3ee1eed190e3c85bb2fe793fa526d58dcb1362575c8447aba2ded28e20cab(
    *,
    api_key: builtins.str,
    secret_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b690cee600d6640a4563f5c3e115b1108274292cca4da2ac3b8e3f9c054518c(
    *,
    api_key: builtins.str,
    api_secret_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5d83b73c68f97257e00fd4a472b5060b923b19bf51a85eac98afa02a948b3f4(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10274e31bef95217811425846919ad5f3013d939461f69d203d5222cb8a6c357(
    *,
    auth_code: typing.Optional[builtins.str] = None,
    redirect_uri: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c79f7beaf2ede6f336bef23f37f62a2315750767926008efbda3f98c15e34f73(
    *,
    connector_profile_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    connector_profile_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd35c0b739bcd10a467238169b0d80e4d63f0277bdf37e945f3ea0bb11abbe59(
    *,
    amplitude: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.AmplitudeConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.CustomConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.DatadogConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.DynatraceConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    google_analytics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.GoogleAnalyticsConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    infor_nexus: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.InforNexusConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.MarketoConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pardot: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.PardotConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.RedshiftConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SalesforceConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SAPODataConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ServiceNowConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    singular: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SingularConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SlackConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SnowflakeConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trendmicro: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.TrendmicroConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    veeva: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.VeevaConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ZendeskConnectorProfileCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65e5865d49e1e2770f8833632ac69e47b3b029c81a4772e3b1c5426bdf879d4b(
    *,
    custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.CustomConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.DatadogConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.DynatraceConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    infor_nexus: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.InforNexusConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.MarketoConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pardot: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.PardotConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.RedshiftConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SalesforceConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SAPODataConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ServiceNowConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SlackConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.SnowflakeConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    veeva: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.VeevaConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ZendeskConnectorProfilePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f1703eb3a58b3e6fd9b4a3833c2dc0fda48f2e43ba626529bc4a347a6d456e2(
    *,
    custom_authentication_type: builtins.str,
    credentials_map: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__706a9d527abbd20fd254cc98e3158ee9239289a3d14735ef9c32c2c9b41893ee(
    *,
    authentication_type: builtins.str,
    api_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ApiKeyCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    basic: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.BasicAuthCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.CustomAuthCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    oauth2: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.OAuth2CredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdb89c4d5019ae54344a6656863ce47417e2890bffc90e8167ec429bcb73d3b5(
    *,
    o_auth2_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.OAuth2PropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    profile_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5405a79a636a3a984fb01f6d21584050057edd8e02c32d2521ce746189892e2(
    *,
    api_key: builtins.str,
    application_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0659a9b67dc2853fedfdb11c94408d52cccb2ed20597bf42f6fb15b29415e87c(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__020dbb7eb0377d6f0d6ff989b7f0dca2eac8bc5293fb8b927d656f980b21f044(
    *,
    api_token: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29ed8163fe5b7ed49fedb68b059a96f0281b5f5f2c1bc08329d34386502b27b0(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f33ae7fdb815fdbe41d4a4e9dc65db0eaa088f28c686524272747ffdfa411dd(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0896c3f041be47a1346b6586c9961c6fddd408caca37ab78b69e2dbf3947b95(
    *,
    access_key_id: builtins.str,
    datakey: builtins.str,
    secret_access_key: builtins.str,
    user_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__121e8f6f0112eff36febf9235f6ad930186b1adfe295e513385c5ba69795c179(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__319f8014bd5324a2f4dc144886a8f0e7be1951f564c0fbd5badf8555b0d5263d(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79733216203bc37d79a7396313a11957f92d7188cf5cc3a157352ceaa4b6202b(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b23a5882bc69b9efde3f028d1f4180011380cc10767444f52981ddf4ad39fa3(
    *,
    access_token: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12b3508701004e181ac97abfefbe0c0e2c32f353cdc4077fc915d1e79059ded1(
    *,
    o_auth2_grant_type: typing.Optional[builtins.str] = None,
    token_url: typing.Optional[builtins.str] = None,
    token_url_custom_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7da4be883f6a7b1d3ca824e7af71520a4dc18eb0c5c299a47adef3ced4c33b77(
    *,
    access_token: typing.Optional[builtins.str] = None,
    client_id: typing.Optional[builtins.str] = None,
    client_secret: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__269c069da81422f6673236a4320be612c0558af7fe900035e4f46e91d169ce84(
    *,
    auth_code_url: typing.Optional[builtins.str] = None,
    o_auth_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    token_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39a512cdf635aa9981165b275367a20430c45c0c4a601e102d0cdf5e10430e12(
    *,
    access_token: typing.Optional[builtins.str] = None,
    client_credentials_arn: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a3e6a4fb1f0111e07cf857d2ee3ad46142f3b374d08c97bb704c89fa233cd47(
    *,
    business_unit_id: builtins.str,
    instance_url: typing.Optional[builtins.str] = None,
    is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a07d7a6959f8151e74abf74abadc91dd5c9f7a16d911f5db0bc2f66e4f25e24(
    *,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b095f01640a40304a0331c41ae7ab321ae12f0c106bbb47ef402aac9840f90f7(
    *,
    bucket_name: builtins.str,
    role_arn: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    cluster_identifier: typing.Optional[builtins.str] = None,
    data_api_role_arn: typing.Optional[builtins.str] = None,
    database_name: typing.Optional[builtins.str] = None,
    database_url: typing.Optional[builtins.str] = None,
    is_redshift_serverless: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    workgroup_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e721304f58add999e91a5094b626deadf6f42ca2e0e3744b0e313380bc540b00(
    *,
    basic_auth_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.BasicAuthCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    o_auth_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.OAuthCredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa0bde147a80d4f5be2e3a0a92803dcbc8bf7a7949aaf97c980a8be44a261244(
    *,
    application_host_url: typing.Optional[builtins.str] = None,
    application_service_path: typing.Optional[builtins.str] = None,
    client_number: typing.Optional[builtins.str] = None,
    disable_sso: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    logon_language: typing.Optional[builtins.str] = None,
    o_auth_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.OAuthPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    port_number: typing.Optional[jsii.Number] = None,
    private_link_service_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f1396ecd411968fa6dcd8be1e9a9cbc6d0f02f80c0d4e9acc547f44564e4cb(
    *,
    access_token: typing.Optional[builtins.str] = None,
    client_credentials_arn: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    jwt_token: typing.Optional[builtins.str] = None,
    o_auth2_grant_type: typing.Optional[builtins.str] = None,
    refresh_token: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e02155b4dbffca160c7213611f0f005432320f081cac130c77c180517e637a2f(
    *,
    instance_url: typing.Optional[builtins.str] = None,
    is_sandbox_environment: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_private_link_for_metadata_and_authorization: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9300511337a4bb1851f11ae6d27ff1f49d05843818e90659f8938653677148dc(
    *,
    o_auth2_credentials: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.OAuth2CredentialsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    password: typing.Optional[builtins.str] = None,
    username: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__efce9f1c1c228e65efb350a33320672ebf6907ec78b01471e88a2f3115b49969(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bc42a25a4870da865c4d31df2ea94435f79afd8cd9830a7292d2927bd728c89(
    *,
    api_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33f7d201cd92c3241e76eeef7aa8154f9c19884178d71dfffea8c0db939343da(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7fa78e2f74e28f73bdd0a0a5b4498cd51ac364dea787eb69eca7836013e38578(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78ab8cbf4a57bfd8e44a5e9c1239be3df998e064aa70bc8d688ee7b7448d6b85(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f80ae6d0ba98546835743a752b0ca92f9ee74d525a2d9048e10cb2e431bef1(
    *,
    bucket_name: builtins.str,
    stage: builtins.str,
    warehouse: builtins.str,
    account_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    private_link_service_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f95a9d334e1f47f62231dbcb8790eabf066eadb9f788be0eade7c40e427fbfd(
    *,
    api_secret_key: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f8ef2a02ea3e3deaf9f4972c986d189157161d79719d8e6cc32bc591af0417d(
    *,
    password: builtins.str,
    username: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bcf7976bdceaf015e653ef6a1d5de1fe1a0bac8d7acc3bacd57ea35f47af45d(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__23cdb025a23f9fe29cc4cc49eb6c3c171c1c23d9f0bf22702b88df0eb1e9b477(
    *,
    client_id: builtins.str,
    client_secret: builtins.str,
    access_token: typing.Optional[builtins.str] = None,
    connector_o_auth_request: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorOAuthRequestProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__deb62e66d965f0e26ff87d16ee4c48a202e9421055030e74ae433cbf772a681a(
    *,
    instance_url: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__032712d85c2f8c1992ce0b706fc9b7992da5970e1c4b25cc48b86d35fbf104bb(
    *,
    connection_mode: builtins.str,
    connector_profile_name: builtins.str,
    connector_type: builtins.str,
    connector_label: typing.Optional[builtins.str] = None,
    connector_profile_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnectorProfile.ConnectorProfileConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__204ab8f1f508d34470db08010b45b65c1aa7d47e66c5fb91f90cdeb633b5eb9b(
    *,
    connector_provisioning_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConnector.ConnectorProvisioningConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    connector_provisioning_type: builtins.str,
    connector_label: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76b6ef95e5f4f4d7b82746abb1435c9e6f43a91ed656c1dd9c1a02064f00a78a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    destination_flow_config_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DestinationFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    flow_name: builtins.str,
    source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TaskProperty, typing.Dict[builtins.str, typing.Any]]]]],
    trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    flow_status: typing.Optional[builtins.str] = None,
    kms_arn: typing.Optional[builtins.str] = None,
    metadata_catalog_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MetadataCatalogConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a0903a5b0777541e9478e23854a85d5a2c4808c0983bf165d70ab1b5449fca1(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2dc3a4aea78f4e89fd86f1b0a95c6b628a20b040c6bc400fdee8c2c4456dbec4(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6e790e910559e7c5bdcd3b94ffbcee395c9ebca3506e34c7dc5849e4cc2f22e(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.DestinationFlowConfigProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04271ee51cb938fbf314abcbe8001536684e210ea83443e61da82559f654fcfa(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af0fe8bf747f64f1d7f670168d2b21f389c54a57af38e982865d5ff46125027c(
    value: typing.Union[_IResolvable_da3f097b, CfnFlow.SourceFlowConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6be845445f663cd529fe7ed672afb9293c81c28e04a68e7cffb28e49f904b1cf(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFlow.TaskProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb7ecca2b731f1a7b7e2f3e1002382bb5d5b42e9ff425b98984717cf715b0473(
    value: typing.Union[_IResolvable_da3f097b, CfnFlow.TriggerConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76ecbc6111b3b15ac62ef5211231c35103879fefecb75334c74f80f8c9df5e0b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea530c7cd48e3e434bd34b8ab9dabb719427831263b04557da3d03e82acbebce(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__587868dddc78d2790162bd179ba67212276001fbdd8c989c9e3b837c1ef2b252(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a474740c338d02b5c3e7ece5ad8097d97710078550a9f34157e3e053142f0c9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.MetadataCatalogConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac44925e55be2d561241744a9491ec33e37633d5ea9a74479066fc80e01dab99(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__328b80ffe3ee9a0256b74806b514d92bc909f03f004bc1072bd9eb46b96579f9(
    *,
    aggregation_type: typing.Optional[builtins.str] = None,
    target_file_size: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c79a354a2904c1f043a53640b1e199ce326ebe0583ec664b1b5a5e01b1141585(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0948b4cb879f7f09a0ff8663e81bf08fbed9c98d8935ce5ea10cae90d1a8030(
    *,
    amplitude: typing.Optional[builtins.str] = None,
    custom_connector: typing.Optional[builtins.str] = None,
    datadog: typing.Optional[builtins.str] = None,
    dynatrace: typing.Optional[builtins.str] = None,
    google_analytics: typing.Optional[builtins.str] = None,
    infor_nexus: typing.Optional[builtins.str] = None,
    marketo: typing.Optional[builtins.str] = None,
    pardot: typing.Optional[builtins.str] = None,
    s3: typing.Optional[builtins.str] = None,
    salesforce: typing.Optional[builtins.str] = None,
    sapo_data: typing.Optional[builtins.str] = None,
    service_now: typing.Optional[builtins.str] = None,
    singular: typing.Optional[builtins.str] = None,
    slack: typing.Optional[builtins.str] = None,
    trendmicro: typing.Optional[builtins.str] = None,
    veeva: typing.Optional[builtins.str] = None,
    zendesk: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c9546f78b7b6588933605f813de3303d240c8a8ea3ec8140f299a55377383a6d(
    *,
    entity_name: builtins.str,
    custom_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dca7f6a437784e099abbe4b67b153f5f8442b7f8bf74f61a2961a5fe146e546b(
    *,
    entity_name: builtins.str,
    custom_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    data_transfer_api: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DataTransferApiProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fd0d04f9159d73850b9ed3d57b9d06d47be4e67aac70dac24b01272bce3eea51(
    *,
    name: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b267c7bbc073ff7038f9afd92bea1a5aa8e3ce6c87cce7601e1a5c613842541(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__61c1007c034c653922497591ce4be08935eae99b8eb4651428db4cd63bfbe836(
    *,
    custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.CustomConnectorDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.EventBridgeDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lookout_metrics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.LookoutMetricsDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MarketoDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    redshift: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.RedshiftDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.S3DestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SalesforceDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SAPODataDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    snowflake: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SnowflakeDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    upsolver: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.UpsolverDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ZendeskDestinationPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a402951d4f07b94704bb13f3e3d06a8b6b9d77e06e6fc1d84977f9517982e7f1(
    *,
    connector_type: builtins.str,
    destination_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DestinationConnectorPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
    api_version: typing.Optional[builtins.str] = None,
    connector_profile_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd31c39eceb7e8f9ff83abe7bdead9c7600418ea846aab5ebf0753342629880b(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__078888996b9eead8bfd345f5605ec71018981578c357cd612506905b30ac521b(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
    fail_on_first_error: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e03b85b4f5295b92ede3385edaa38289164ed2e7ce6906b31d4ed43261f2a5(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d54128401eb4f1071ae36d8a94740a8609f3a83c599e4ae134e5f639093b263(
    *,
    database_name: builtins.str,
    role_arn: builtins.str,
    table_prefix: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4ed31a66518065602d2b82ead4f74719971927fbbbde987b8775f8e657f0f2f(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__759935a3bf8f161ab3b60afdbbe4f58242c6c5bd495d8f4c8769f330422ea6f8(
    *,
    datetime_type_field_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d7abfd8dee53e8d72b6717b22ce7f7090bff56556455f268445e608bbd34946(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__060702aed5019190a6b199aad5e66f61768453c8fbe7c5549752dea9c79a361b(
    *,
    object: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d081ec2d0308a134ab532b76aa1b67bd5dc34d931782456f9384ab6bee329ba(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bd9aa6a3e0dbdbe51c141292970fcab641b368bdfcedea085461c81262a471b(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6c8a679bd51537f9a83827157b0794271255d4346540c24884c78865854859(
    *,
    glue_data_catalog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.GlueDataCatalogProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57187f77b7b8cbe02dd1d2d2689e5d019ac5a329b434d4e64e52142ee8f22c96(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ca7d146b99555e5990a83482ad7afa30c6b2871a7c5597b99e2b425052d5572(
    *,
    path_prefix_hierarchy: typing.Optional[typing.Sequence[builtins.str]] = None,
    prefix_format: typing.Optional[builtins.str] = None,
    prefix_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3402bfecb762ab7eeca84836d4541ecb34ac1e9bf357d0aca15d57bfbab3ef9(
    *,
    intermediate_bucket_name: builtins.str,
    object: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec0528e9590b2bddf1b9031aadc143a8f3989afde0772669ab454e92b157ce68(
    *,
    bucket_name: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    s3_output_format_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.S3OutputFormatConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3026ab7181af509228fef339c10aee815ccd500d0b0ab562d0a601451f151fe5(
    *,
    s3_input_file_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__407430b2021e0200bc72876aac4ff684f0d8799c206a3a9414a422d1117ad9e3(
    *,
    aggregation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.AggregationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_type: typing.Optional[builtins.str] = None,
    prefix_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.PrefixConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    preserve_source_data_typing: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fceba990c11a1dcac2ffb6444971b0e2f656ef344ffa30a7be490d7934960b27(
    *,
    bucket_name: builtins.str,
    bucket_prefix: builtins.str,
    s3_input_format_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.S3InputFormatConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe430f8a0b8fb0ec38ccedbd370e2c15756d92142c80a33db63467c251bf746f(
    *,
    object_path: builtins.str,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    success_response_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SuccessResponseHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a1b148320f618d1580608aea44a877c958797e9cc86024259d3c016c8971c1(
    *,
    max_page_size: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__668e98c80d12ecf0f0b6848ebbd4e31684d00592bad96c5d718f04567a36d867(
    *,
    max_parallelism: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4e8d48237678f7dc3ac8c9c540e8c8080066daee936538208a6c98c0bd5b8e(
    *,
    object_path: builtins.str,
    pagination_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SAPODataPaginationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    parallelism_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SAPODataParallelismConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb5fca2c002782d42209e79c110151b3808d3c3603d8ea4038a9950700201881(
    *,
    object: builtins.str,
    data_transfer_api: typing.Optional[builtins.str] = None,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__697f1bdf553e40b76d835a0032b4929b29e8c8e62c21e52cbc4d6e184f47fe5b(
    *,
    object: builtins.str,
    data_transfer_api: typing.Optional[builtins.str] = None,
    enable_dynamic_field_update: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_deleted_records: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__432f0b4ecbd08bb1fea8eaf3541e9eea15562f2a97861fe29276031c796d986b(
    *,
    schedule_expression: builtins.str,
    data_pull_mode: typing.Optional[builtins.str] = None,
    first_execution_from: typing.Optional[jsii.Number] = None,
    flow_error_deactivation_threshold: typing.Optional[jsii.Number] = None,
    schedule_end_time: typing.Optional[jsii.Number] = None,
    schedule_offset: typing.Optional[jsii.Number] = None,
    schedule_start_time: typing.Optional[jsii.Number] = None,
    time_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f28c53e5a211cf01809013da71c5a7157f26d88b8459970752b72684cd630e2(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f1fe6d35e37b171c76f4e32614f4188012e4108d512909e54f1c611343926e(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3df173883e334f5de644d5ad1d7c83004e6b6ba99b20efe1bf8b36be60a5a6d(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__861db013349794673cd44026c51c9186e9b48c189f3d2f897e96326cf9022abd(
    *,
    intermediate_bucket_name: builtins.str,
    object: builtins.str,
    bucket_prefix: typing.Optional[builtins.str] = None,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfca05ac628581510d78eb8880099b2c8d67e6218aeca321ae975f0979bb85af(
    *,
    amplitude: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.AmplitudeSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_connector: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.CustomConnectorSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    datadog: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DatadogSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynatrace: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DynatraceSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    google_analytics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.GoogleAnalyticsSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    infor_nexus: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.InforNexusSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    marketo: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MarketoSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    pardot: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.PardotSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.S3SourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    salesforce: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SalesforceSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sapo_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SAPODataSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    service_now: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ServiceNowSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    singular: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SingularSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    slack: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SlackSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    trendmicro: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TrendmicroSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    veeva: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.VeevaSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    zendesk: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ZendeskSourcePropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82f2b5bbb1f4a6eab214e7cfa4059986076879090f1ee5604886d749c25bc0af(
    *,
    connector_type: builtins.str,
    source_connector_properties: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceConnectorPropertiesProperty, typing.Dict[builtins.str, typing.Any]]],
    api_version: typing.Optional[builtins.str] = None,
    connector_profile_name: typing.Optional[builtins.str] = None,
    incremental_pull_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.IncrementalPullConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2abacd16b8046f3cf4c6b41305e1a136113c378aa704f9caf9caf85babd687f3(
    *,
    bucket_name: typing.Optional[builtins.str] = None,
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__979dcfb4514caff045d16804e80e950a4b994c418d975bfda1b058b9b48fced4(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72c004cc65bad7fca9bee2b8e49d510b504af527bc9f31cdca10692f130cda87(
    *,
    source_fields: typing.Sequence[builtins.str],
    task_type: builtins.str,
    connector_operator: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ConnectorOperatorProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    destination_field: typing.Optional[builtins.str] = None,
    task_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TaskPropertiesObjectProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41cf6b7146e8303d1b50511d2818edd5e3c2dfa0eab59171dd6d9b24f3cbfa80(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd28ca462b3e9e4f32cc44aec4e8810188f62b59f8d2642880f795974ed7aabc(
    *,
    trigger_type: builtins.str,
    trigger_properties: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ScheduledTriggerPropertiesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05785a870fff4b04759a9e76167dfd9a3a7b02a191fa2a196cf1fcf2f10cc020(
    *,
    bucket_name: builtins.str,
    s3_output_format_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.UpsolverS3OutputFormatConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    bucket_prefix: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc27a8a1f41dd89c26ea1554f69fb21c1553a7bdaf514ef9f0b77024672f8e1f(
    *,
    prefix_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.PrefixConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    aggregation_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.AggregationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    file_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33eb5d9916f4bbfdcb7645bab52a5e8a99175f5473686f4922323cb792470b88(
    *,
    object: builtins.str,
    document_type: typing.Optional[builtins.str] = None,
    include_all_versions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_renditions: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_source_files: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b408dbbead0815b59be3690c6532ce03b6ccc36638f38661f96d1b80187c2dd4(
    *,
    object: builtins.str,
    error_handling_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.ErrorHandlingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    id_field_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    write_operation_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97d56d701da8e030ea893f9e410a42eda76f5e8d95fbaeafd8ab06b3ff38829a(
    *,
    object: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85045c56f5ed71ad46fec6374ddad0e03a173028630204629542088fb8766ae9(
    *,
    destination_flow_config_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.DestinationFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]]]],
    flow_name: builtins.str,
    source_flow_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceFlowConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    tasks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TaskProperty, typing.Dict[builtins.str, typing.Any]]]]],
    trigger_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.TriggerConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    description: typing.Optional[builtins.str] = None,
    flow_status: typing.Optional[builtins.str] = None,
    kms_arn: typing.Optional[builtins.str] = None,
    metadata_catalog_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.MetadataCatalogConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
