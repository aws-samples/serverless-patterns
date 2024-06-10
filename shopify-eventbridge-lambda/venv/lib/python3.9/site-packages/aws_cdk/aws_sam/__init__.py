'''
# AWS Serverless Application Model Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_sam as serverless
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Serverless construct libraries](https://constructs.dev/search?q=serverless)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Serverless resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Serverless.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Serverless](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Serverless.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApi(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnApi",
):
    '''https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapi.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html
    :cloudformationResource: AWS::Serverless::Api
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        # authorizers: Any
        # definition_body: Any
        # gateway_responses: Any
        # method_settings: Any
        # models: Any
        
        cfn_api = sam.CfnApi(self, "MyCfnApi",
            stage_name="stageName",
        
            # the properties below are optional
            access_log_setting=sam.CfnApi.AccessLogSettingProperty(
                destination_arn="destinationArn",
                format="format"
            ),
            always_deploy=False,
            auth=sam.CfnApi.AuthProperty(
                add_default_authorizer_to_cors_preflight=False,
                authorizers=authorizers,
                default_authorizer="defaultAuthorizer"
            ),
            binary_media_types=["binaryMediaTypes"],
            cache_cluster_enabled=False,
            cache_cluster_size="cacheClusterSize",
            canary_setting=sam.CfnApi.CanarySettingProperty(
                deployment_id="deploymentId",
                percent_traffic=123,
                stage_variable_overrides={
                    "stage_variable_overrides_key": "stageVariableOverrides"
                },
                use_stage_cache=False
            ),
            cors="cors",
            definition_body=definition_body,
            definition_uri="definitionUri",
            description="description",
            disable_execute_api_endpoint=False,
            domain=sam.CfnApi.DomainConfigurationProperty(
                certificate_arn="certificateArn",
                domain_name="domainName",
        
                # the properties below are optional
                base_path=["basePath"],
                endpoint_configuration="endpointConfiguration",
                mutual_tls_authentication=sam.CfnApi.MutualTlsAuthenticationProperty(
                    truststore_uri="truststoreUri",
                    truststore_version="truststoreVersion"
                ),
                ownership_verification_certificate_arn="ownershipVerificationCertificateArn",
                route53=sam.CfnApi.Route53ConfigurationProperty(
                    distributed_domain_name="distributedDomainName",
                    evaluate_target_health=False,
                    hosted_zone_id="hostedZoneId",
                    hosted_zone_name="hostedZoneName",
                    ip_v6=False
                ),
                security_policy="securityPolicy"
            ),
            endpoint_configuration="endpointConfiguration",
            gateway_responses=gateway_responses,
            method_settings=[method_settings],
            minimum_compression_size=123,
            models=models,
            name="name",
            open_api_version="openApiVersion",
            tags={
                "tags_key": "tags"
            },
            tracing_enabled=False,
            variables={
                "variables_key": "variables"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        stage_name: builtins.str,
        access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.AccessLogSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        always_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.AuthProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        binary_media_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_cluster_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cache_cluster_size: typing.Optional[builtins.str] = None,
        canary_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.CanarySettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cors: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnApi.CorsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_body: typing.Any = None,
        definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnApi.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.DomainConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        endpoint_configuration: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnApi.EndpointConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        gateway_responses: typing.Any = None,
        method_settings: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
        minimum_compression_size: typing.Optional[jsii.Number] = None,
        models: typing.Any = None,
        name: typing.Optional[builtins.str] = None,
        open_api_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tracing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param stage_name: 
        :param access_log_setting: 
        :param always_deploy: 
        :param auth: 
        :param binary_media_types: 
        :param cache_cluster_enabled: 
        :param cache_cluster_size: 
        :param canary_setting: 
        :param cors: 
        :param definition_body: 
        :param definition_uri: 
        :param description: 
        :param disable_execute_api_endpoint: 
        :param domain: 
        :param endpoint_configuration: 
        :param gateway_responses: 
        :param method_settings: 
        :param minimum_compression_size: 
        :param models: 
        :param name: 
        :param open_api_version: 
        :param tags: 
        :param tracing_enabled: 
        :param variables: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3135996bb5e2b67d63a2144c699a4377166e2b1ebabc180e4c43b45b5c59afc6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiProps(
            stage_name=stage_name,
            access_log_setting=access_log_setting,
            always_deploy=always_deploy,
            auth=auth,
            binary_media_types=binary_media_types,
            cache_cluster_enabled=cache_cluster_enabled,
            cache_cluster_size=cache_cluster_size,
            canary_setting=canary_setting,
            cors=cors,
            definition_body=definition_body,
            definition_uri=definition_uri,
            description=description,
            disable_execute_api_endpoint=disable_execute_api_endpoint,
            domain=domain,
            endpoint_configuration=endpoint_configuration,
            gateway_responses=gateway_responses,
            method_settings=method_settings,
            minimum_compression_size=minimum_compression_size,
            models=models,
            name=name,
            open_api_version=open_api_version,
            tags=tags,
            tracing_enabled=tracing_enabled,
            variables=variables,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__980c536039534f411567f6cf0cb008380fdcc0e98538bc3e291702cbf9a9759a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__4c6e7bfcfbe140d0e280964b4302aeb918e0c0bef723f5038b4e83865f2137a2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

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
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stageName"))

    @stage_name.setter
    def stage_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ed0b67619cb13cee60979ea07bab7433a9a3aac2c3381b9e76293bd8a4acbc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageName", value)

    @builtins.property
    @jsii.member(jsii_name="accessLogSetting")
    def access_log_setting(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.AccessLogSettingProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.AccessLogSettingProperty"]], jsii.get(self, "accessLogSetting"))

    @access_log_setting.setter
    def access_log_setting(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.AccessLogSettingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3419ac45d5962e11eb2db0565d8366156554a528cc08dbac9e2dd50637f617de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLogSetting", value)

    @builtins.property
    @jsii.member(jsii_name="alwaysDeploy")
    def always_deploy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "alwaysDeploy"))

    @always_deploy.setter
    def always_deploy(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64308e272be1e8e8f200c8877ef85bc40f951d1580772db49e31028cd9e144f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "alwaysDeploy", value)

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.AuthProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.AuthProperty"]], jsii.get(self, "auth"))

    @auth.setter
    def auth(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.AuthProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b7899a6959fd44c06397e5419ff9b1ac5cc6f9086b4b8ebd3f8cdc094286e5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auth", value)

    @builtins.property
    @jsii.member(jsii_name="binaryMediaTypes")
    def binary_media_types(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "binaryMediaTypes"))

    @binary_media_types.setter
    def binary_media_types(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8373fadf34e7203e351433b382ba203e1a684129fb26aa8b16985168b4775ba8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "binaryMediaTypes", value)

    @builtins.property
    @jsii.member(jsii_name="cacheClusterEnabled")
    def cache_cluster_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "cacheClusterEnabled"))

    @cache_cluster_enabled.setter
    def cache_cluster_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6db99bca07f874422ccf27bae4b332d73412b5b284607e77cca4cf711315d689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheClusterEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="cacheClusterSize")
    def cache_cluster_size(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "cacheClusterSize"))

    @cache_cluster_size.setter
    def cache_cluster_size(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3feeb5c18554c7f510db8100d0cb77b1a824a847babeb1c247dc68e3e3eeb8bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cacheClusterSize", value)

    @builtins.property
    @jsii.member(jsii_name="canarySetting")
    def canary_setting(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.CanarySettingProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.CanarySettingProperty"]], jsii.get(self, "canarySetting"))

    @canary_setting.setter
    def canary_setting(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.CanarySettingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e835d60486fa1350fa728f5e35beef29325f8745ffd51ac4d8d10ded0065ea83)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "canarySetting", value)

    @builtins.property
    @jsii.member(jsii_name="cors")
    def cors(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.CorsConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.CorsConfigurationProperty"]], jsii.get(self, "cors"))

    @cors.setter
    def cors(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.CorsConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21dbab6598d5847bc72ec62c28426fe0408db8682d5127fe28a05b213dc8b26a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cors", value)

    @builtins.property
    @jsii.member(jsii_name="definitionBody")
    def definition_body(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "definitionBody"))

    @definition_body.setter
    def definition_body(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd38f5bcc3b8f3fac0bbdfb5d5e3af45744e24319a5d1d7e28038ee4bdfb281)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionBody", value)

    @builtins.property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.S3LocationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.S3LocationProperty"]], jsii.get(self, "definitionUri"))

    @definition_uri.setter
    def definition_uri(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f2e92449b9c950f501c430abd84aa43a5df516a6602172d17f1558ebe2fea14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionUri", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__353032891306086a17e2ae218e03d18455f1ba6f7127e6fefb12def15f0da51c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableExecuteApiEndpoint"))

    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da75fbe1266a65afaa78ba97bcf585c32f11bacc0c752250a64bb1bdec2930f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableExecuteApiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.DomainConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.DomainConfigurationProperty"]], jsii.get(self, "domain"))

    @domain.setter
    def domain(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.DomainConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff6672be629c8cc80fa0f0b711bf815d7d7e9a5fee9699f73a5b9e844ba8b3b1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="endpointConfiguration")
    def endpoint_configuration(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.EndpointConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.EndpointConfigurationProperty"]], jsii.get(self, "endpointConfiguration"))

    @endpoint_configuration.setter
    def endpoint_configuration(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApi.EndpointConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966627515263d6c2176ac06d97124210d55dfafc260439f62393f93e44921771)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayResponses")
    def gateway_responses(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "gatewayResponses"))

    @gateway_responses.setter
    def gateway_responses(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8484ea00d921c99afaacbd03cc62295f32910b5df7d96ca8db6a13dc54d28f6a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayResponses", value)

    @builtins.property
    @jsii.member(jsii_name="methodSettings")
    def method_settings(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], jsii.get(self, "methodSettings"))

    @method_settings.setter
    def method_settings(
        self,
        value: typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89314956b349bc8e1c3bc352780728615074b16dbe9e899a681b4d3fe381dec7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "methodSettings", value)

    @builtins.property
    @jsii.member(jsii_name="minimumCompressionSize")
    def minimum_compression_size(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minimumCompressionSize"))

    @minimum_compression_size.setter
    def minimum_compression_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1347fd00b71a6087fdb38700bc130ac87aa76321596ad0a55c2ce78a266a0942)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minimumCompressionSize", value)

    @builtins.property
    @jsii.member(jsii_name="models")
    def models(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "models"))

    @models.setter
    def models(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c11bc94dea5aec21ef52c13c5f4551cc63138a4c4b4f582d2fb6ace3a82483)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "models", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbbe4108d9afb71eb640322c267e8e750561d165eff7247edc582f829e3cf088)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="openApiVersion")
    def open_api_version(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "openApiVersion"))

    @open_api_version.setter
    def open_api_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2751c6279da41aa599812d74ed6dc4408a3f0805176952a12d00f84ae79a1385)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "openApiVersion", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50f4bb3d61c77c677d99cdcdff136faa1b17e44d9a17165841d93e999613f334)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tracingEnabled")
    def tracing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "tracingEnabled"))

    @tracing_enabled.setter
    def tracing_enabled(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__381be80448e4bb2d0dfa01f12de99215cac54995a787d289c523b6d8bae92a6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tracingEnabled", value)

    @builtins.property
    @jsii.member(jsii_name="variables")
    def variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "variables"))

    @variables.setter
    def variables(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e18d5b2f60202118ae9b46b2c208eab95ae644832c6148e75937bc7ad0ae9622)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "variables", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.AccessLogSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn", "format": "format"},
    )
    class AccessLogSettingProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination_arn: 
            :param format: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-accesslogsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                access_log_setting_property = sam.CfnApi.AccessLogSettingProperty(
                    destination_arn="destinationArn",
                    format="format"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__de360432e84693b1344e24631c0725f17fe9270f6be8fe45212ab38ec786134f)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn
            if format is not None:
                self._values["format"] = format

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-accesslogsetting.html#cfn-serverless-api-accesslogsetting-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-accesslogsetting.html#cfn-serverless-api-accesslogsetting-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessLogSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.AuthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_default_authorizer_to_cors_preflight": "addDefaultAuthorizerToCorsPreflight",
            "authorizers": "authorizers",
            "default_authorizer": "defaultAuthorizer",
        },
    )
    class AuthProperty:
        def __init__(
            self,
            *,
            add_default_authorizer_to_cors_preflight: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            authorizers: typing.Any = None,
            default_authorizer: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param add_default_authorizer_to_cors_preflight: 
            :param authorizers: 
            :param default_authorizer: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-auth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # authorizers: Any
                
                auth_property = sam.CfnApi.AuthProperty(
                    add_default_authorizer_to_cors_preflight=False,
                    authorizers=authorizers,
                    default_authorizer="defaultAuthorizer"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3fa398b1d1629ec063ca30c8b836b8fd210cb478aeb0e7e717a65aa88f949c58)
                check_type(argname="argument add_default_authorizer_to_cors_preflight", value=add_default_authorizer_to_cors_preflight, expected_type=type_hints["add_default_authorizer_to_cors_preflight"])
                check_type(argname="argument authorizers", value=authorizers, expected_type=type_hints["authorizers"])
                check_type(argname="argument default_authorizer", value=default_authorizer, expected_type=type_hints["default_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_default_authorizer_to_cors_preflight is not None:
                self._values["add_default_authorizer_to_cors_preflight"] = add_default_authorizer_to_cors_preflight
            if authorizers is not None:
                self._values["authorizers"] = authorizers
            if default_authorizer is not None:
                self._values["default_authorizer"] = default_authorizer

        @builtins.property
        def add_default_authorizer_to_cors_preflight(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-auth.html#cfn-serverless-api-auth-adddefaultauthorizertocorspreflight
            '''
            result = self._values.get("add_default_authorizer_to_cors_preflight")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def authorizers(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-auth.html#cfn-serverless-api-auth-authorizers
            '''
            result = self._values.get("authorizers")
            return typing.cast(typing.Any, result)

        @builtins.property
        def default_authorizer(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-auth.html#cfn-serverless-api-auth-defaultauthorizer
            '''
            result = self._values.get("default_authorizer")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.CanarySettingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "deployment_id": "deploymentId",
            "percent_traffic": "percentTraffic",
            "stage_variable_overrides": "stageVariableOverrides",
            "use_stage_cache": "useStageCache",
        },
    )
    class CanarySettingProperty:
        def __init__(
            self,
            *,
            deployment_id: typing.Optional[builtins.str] = None,
            percent_traffic: typing.Optional[jsii.Number] = None,
            stage_variable_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
            use_stage_cache: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param deployment_id: 
            :param percent_traffic: 
            :param stage_variable_overrides: 
            :param use_stage_cache: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-canarysetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                canary_setting_property = sam.CfnApi.CanarySettingProperty(
                    deployment_id="deploymentId",
                    percent_traffic=123,
                    stage_variable_overrides={
                        "stage_variable_overrides_key": "stageVariableOverrides"
                    },
                    use_stage_cache=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a04c0e58764c2325f15e42a28ebefd2c7e52c177703a95e3b0742576c53e8499)
                check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
                check_type(argname="argument percent_traffic", value=percent_traffic, expected_type=type_hints["percent_traffic"])
                check_type(argname="argument stage_variable_overrides", value=stage_variable_overrides, expected_type=type_hints["stage_variable_overrides"])
                check_type(argname="argument use_stage_cache", value=use_stage_cache, expected_type=type_hints["use_stage_cache"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if deployment_id is not None:
                self._values["deployment_id"] = deployment_id
            if percent_traffic is not None:
                self._values["percent_traffic"] = percent_traffic
            if stage_variable_overrides is not None:
                self._values["stage_variable_overrides"] = stage_variable_overrides
            if use_stage_cache is not None:
                self._values["use_stage_cache"] = use_stage_cache

        @builtins.property
        def deployment_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-canarysetting.html#cfn-serverless-api-canarysetting-deploymentid
            '''
            result = self._values.get("deployment_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def percent_traffic(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-canarysetting.html#cfn-serverless-api-canarysetting-percenttraffic
            '''
            result = self._values.get("percent_traffic")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stage_variable_overrides(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-canarysetting.html#cfn-serverless-api-canarysetting-stagevariableoverrides
            '''
            result = self._values.get("stage_variable_overrides")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

        @builtins.property
        def use_stage_cache(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-canarysetting.html#cfn-serverless-api-canarysetting-usestagecache
            '''
            result = self._values.get("use_stage_cache")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CanarySettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.CorsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_origin": "allowOrigin",
            "allow_credentials": "allowCredentials",
            "allow_headers": "allowHeaders",
            "allow_methods": "allowMethods",
            "max_age": "maxAge",
        },
    )
    class CorsConfigurationProperty:
        def __init__(
            self,
            *,
            allow_origin: builtins.str,
            allow_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            allow_headers: typing.Optional[builtins.str] = None,
            allow_methods: typing.Optional[builtins.str] = None,
            max_age: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param allow_origin: 
            :param allow_credentials: 
            :param allow_headers: 
            :param allow_methods: 
            :param max_age: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-corsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                cors_configuration_property = sam.CfnApi.CorsConfigurationProperty(
                    allow_origin="allowOrigin",
                
                    # the properties below are optional
                    allow_credentials=False,
                    allow_headers="allowHeaders",
                    allow_methods="allowMethods",
                    max_age="maxAge"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__414d627674291aa30dac0b91f4404e6642cfb76656455ab0d5ac92d71982b33a)
                check_type(argname="argument allow_origin", value=allow_origin, expected_type=type_hints["allow_origin"])
                check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
                check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
                check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
                check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_origin": allow_origin,
            }
            if allow_credentials is not None:
                self._values["allow_credentials"] = allow_credentials
            if allow_headers is not None:
                self._values["allow_headers"] = allow_headers
            if allow_methods is not None:
                self._values["allow_methods"] = allow_methods
            if max_age is not None:
                self._values["max_age"] = max_age

        @builtins.property
        def allow_origin(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-corsconfiguration.html#cfn-serverless-api-corsconfiguration-alloworigin
            '''
            result = self._values.get("allow_origin")
            assert result is not None, "Required property 'allow_origin' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allow_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-corsconfiguration.html#cfn-serverless-api-corsconfiguration-allowcredentials
            '''
            result = self._values.get("allow_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def allow_headers(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-corsconfiguration.html#cfn-serverless-api-corsconfiguration-allowheaders
            '''
            result = self._values.get("allow_headers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def allow_methods(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-corsconfiguration.html#cfn-serverless-api-corsconfiguration-allowmethods
            '''
            result = self._values.get("allow_methods")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_age(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-corsconfiguration.html#cfn-serverless-api-corsconfiguration-maxage
            '''
            result = self._values.get("max_age")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CorsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.DomainConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "domain_name": "domainName",
            "base_path": "basePath",
            "endpoint_configuration": "endpointConfiguration",
            "mutual_tls_authentication": "mutualTlsAuthentication",
            "ownership_verification_certificate_arn": "ownershipVerificationCertificateArn",
            "route53": "route53",
            "security_policy": "securityPolicy",
        },
    )
    class DomainConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_arn: builtins.str,
            domain_name: builtins.str,
            base_path: typing.Optional[typing.Sequence[builtins.str]] = None,
            endpoint_configuration: typing.Optional[builtins.str] = None,
            mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.MutualTlsAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
            route53: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.Route53ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            security_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param certificate_arn: 
            :param domain_name: 
            :param base_path: 
            :param endpoint_configuration: 
            :param mutual_tls_authentication: 
            :param ownership_verification_certificate_arn: 
            :param route53: 
            :param security_policy: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                domain_configuration_property = sam.CfnApi.DomainConfigurationProperty(
                    certificate_arn="certificateArn",
                    domain_name="domainName",
                
                    # the properties below are optional
                    base_path=["basePath"],
                    endpoint_configuration="endpointConfiguration",
                    mutual_tls_authentication=sam.CfnApi.MutualTlsAuthenticationProperty(
                        truststore_uri="truststoreUri",
                        truststore_version="truststoreVersion"
                    ),
                    ownership_verification_certificate_arn="ownershipVerificationCertificateArn",
                    route53=sam.CfnApi.Route53ConfigurationProperty(
                        distributed_domain_name="distributedDomainName",
                        evaluate_target_health=False,
                        hosted_zone_id="hostedZoneId",
                        hosted_zone_name="hostedZoneName",
                        ip_v6=False
                    ),
                    security_policy="securityPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f0f6b4af2fa09b8ccef31dbe8c276532aaa162a75dff7ddbd02a008f9fc5bfdd)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument base_path", value=base_path, expected_type=type_hints["base_path"])
                check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
                check_type(argname="argument mutual_tls_authentication", value=mutual_tls_authentication, expected_type=type_hints["mutual_tls_authentication"])
                check_type(argname="argument ownership_verification_certificate_arn", value=ownership_verification_certificate_arn, expected_type=type_hints["ownership_verification_certificate_arn"])
                check_type(argname="argument route53", value=route53, expected_type=type_hints["route53"])
                check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_arn": certificate_arn,
                "domain_name": domain_name,
            }
            if base_path is not None:
                self._values["base_path"] = base_path
            if endpoint_configuration is not None:
                self._values["endpoint_configuration"] = endpoint_configuration
            if mutual_tls_authentication is not None:
                self._values["mutual_tls_authentication"] = mutual_tls_authentication
            if ownership_verification_certificate_arn is not None:
                self._values["ownership_verification_certificate_arn"] = ownership_verification_certificate_arn
            if route53 is not None:
                self._values["route53"] = route53
            if security_policy is not None:
                self._values["security_policy"] = security_policy

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def domain_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-domainname
            '''
            result = self._values.get("domain_name")
            assert result is not None, "Required property 'domain_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_path(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-basepath
            '''
            result = self._values.get("base_path")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def endpoint_configuration(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-endpointconfiguration
            '''
            result = self._values.get("endpoint_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mutual_tls_authentication(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.MutualTlsAuthenticationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-mutualtlsauthentication
            '''
            result = self._values.get("mutual_tls_authentication")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.MutualTlsAuthenticationProperty"]], result)

        @builtins.property
        def ownership_verification_certificate_arn(
            self,
        ) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-ownershipverificationcertificatearn
            '''
            result = self._values.get("ownership_verification_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def route53(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.Route53ConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-route53
            '''
            result = self._values.get("route53")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.Route53ConfigurationProperty"]], result)

        @builtins.property
        def security_policy(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-domainconfiguration.html#cfn-serverless-api-domainconfiguration-securitypolicy
            '''
            result = self._values.get("security_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.EndpointConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "vpc_endpoint_ids": "vpcEndpointIds"},
    )
    class EndpointConfigurationProperty:
        def __init__(
            self,
            *,
            type: typing.Optional[builtins.str] = None,
            vpc_endpoint_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param type: 
            :param vpc_endpoint_ids: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-endpointconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                endpoint_configuration_property = sam.CfnApi.EndpointConfigurationProperty(
                    type="type",
                    vpc_endpoint_ids=["vpcEndpointIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c5c7e18fd130e51b8b9ea76b2bcd48c7975a71dbfb0d2ad44746bc76e20bd62)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument vpc_endpoint_ids", value=vpc_endpoint_ids, expected_type=type_hints["vpc_endpoint_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if type is not None:
                self._values["type"] = type
            if vpc_endpoint_ids is not None:
                self._values["vpc_endpoint_ids"] = vpc_endpoint_ids

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-endpointconfiguration.html#cfn-serverless-api-endpointconfiguration-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_endpoint_ids(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-endpointconfiguration.html#cfn-serverless-api-endpointconfiguration-vpcendpointids
            '''
            result = self._values.get("vpc_endpoint_ids")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EndpointConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.MutualTlsAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "truststore_uri": "truststoreUri",
            "truststore_version": "truststoreVersion",
        },
    )
    class MutualTlsAuthenticationProperty:
        def __init__(
            self,
            *,
            truststore_uri: typing.Optional[builtins.str] = None,
            truststore_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param truststore_uri: 
            :param truststore_version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-mutualtlsauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                mutual_tls_authentication_property = sam.CfnApi.MutualTlsAuthenticationProperty(
                    truststore_uri="truststoreUri",
                    truststore_version="truststoreVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6a1c2641cdeae9cf6962a20881f31e2146da63ab3ee69f6cf60f458d943b69df)
                check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
                check_type(argname="argument truststore_version", value=truststore_version, expected_type=type_hints["truststore_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if truststore_uri is not None:
                self._values["truststore_uri"] = truststore_uri
            if truststore_version is not None:
                self._values["truststore_version"] = truststore_version

        @builtins.property
        def truststore_uri(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-mutualtlsauthentication.html#cfn-serverless-api-mutualtlsauthentication-truststoreuri
            '''
            result = self._values.get("truststore_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def truststore_version(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-mutualtlsauthentication.html#cfn-serverless-api-mutualtlsauthentication-truststoreversion
            '''
            result = self._values.get("truststore_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MutualTlsAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.Route53ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "distributed_domain_name": "distributedDomainName",
            "evaluate_target_health": "evaluateTargetHealth",
            "hosted_zone_id": "hostedZoneId",
            "hosted_zone_name": "hostedZoneName",
            "ip_v6": "ipV6",
        },
    )
    class Route53ConfigurationProperty:
        def __init__(
            self,
            *,
            distributed_domain_name: typing.Optional[builtins.str] = None,
            evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            hosted_zone_id: typing.Optional[builtins.str] = None,
            hosted_zone_name: typing.Optional[builtins.str] = None,
            ip_v6: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param distributed_domain_name: 
            :param evaluate_target_health: 
            :param hosted_zone_id: 
            :param hosted_zone_name: 
            :param ip_v6: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-route53configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                route53_configuration_property = sam.CfnApi.Route53ConfigurationProperty(
                    distributed_domain_name="distributedDomainName",
                    evaluate_target_health=False,
                    hosted_zone_id="hostedZoneId",
                    hosted_zone_name="hostedZoneName",
                    ip_v6=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f36a5c3a1241146402681a4c7202b049f3e90d3934d1bc88f8dbe5add7348851)
                check_type(argname="argument distributed_domain_name", value=distributed_domain_name, expected_type=type_hints["distributed_domain_name"])
                check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
                check_type(argname="argument ip_v6", value=ip_v6, expected_type=type_hints["ip_v6"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if distributed_domain_name is not None:
                self._values["distributed_domain_name"] = distributed_domain_name
            if evaluate_target_health is not None:
                self._values["evaluate_target_health"] = evaluate_target_health
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id
            if hosted_zone_name is not None:
                self._values["hosted_zone_name"] = hosted_zone_name
            if ip_v6 is not None:
                self._values["ip_v6"] = ip_v6

        @builtins.property
        def distributed_domain_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-route53configuration.html#cfn-serverless-api-route53configuration-distributeddomainname
            '''
            result = self._values.get("distributed_domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def evaluate_target_health(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-route53configuration.html#cfn-serverless-api-route53configuration-evaluatetargethealth
            '''
            result = self._values.get("evaluate_target_health")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-route53configuration.html#cfn-serverless-api-route53configuration-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-route53configuration.html#cfn-serverless-api-route53configuration-hostedzonename
            '''
            result = self._values.get("hosted_zone_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ip_v6(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-route53configuration.html#cfn-serverless-api-route53configuration-ipv6
            '''
            result = self._values.get("ip_v6")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Route53ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApi.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key", "version": "version"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            version: jsii.Number,
        ) -> None:
            '''
            :param bucket: 
            :param key: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_location_property = sam.CfnApi.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__64d64a8ff239842e276cc5e9a2d2aa0f5e33af73e03496183475271e84846c22)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "version": version,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-s3location.html#cfn-serverless-api-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-s3location.html#cfn-serverless-api-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-api-s3location.html#cfn-serverless-api-s3location-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "stage_name": "stageName",
        "access_log_setting": "accessLogSetting",
        "always_deploy": "alwaysDeploy",
        "auth": "auth",
        "binary_media_types": "binaryMediaTypes",
        "cache_cluster_enabled": "cacheClusterEnabled",
        "cache_cluster_size": "cacheClusterSize",
        "canary_setting": "canarySetting",
        "cors": "cors",
        "definition_body": "definitionBody",
        "definition_uri": "definitionUri",
        "description": "description",
        "disable_execute_api_endpoint": "disableExecuteApiEndpoint",
        "domain": "domain",
        "endpoint_configuration": "endpointConfiguration",
        "gateway_responses": "gatewayResponses",
        "method_settings": "methodSettings",
        "minimum_compression_size": "minimumCompressionSize",
        "models": "models",
        "name": "name",
        "open_api_version": "openApiVersion",
        "tags": "tags",
        "tracing_enabled": "tracingEnabled",
        "variables": "variables",
    },
)
class CfnApiProps:
    def __init__(
        self,
        *,
        stage_name: builtins.str,
        access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.AccessLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        always_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.AuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        binary_media_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        cache_cluster_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        cache_cluster_size: typing.Optional[builtins.str] = None,
        canary_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.CanarySettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cors: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.CorsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_body: typing.Any = None,
        definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.DomainConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        endpoint_configuration: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.EndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        gateway_responses: typing.Any = None,
        method_settings: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
        minimum_compression_size: typing.Optional[jsii.Number] = None,
        models: typing.Any = None,
        name: typing.Optional[builtins.str] = None,
        open_api_version: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tracing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApi``.

        :param stage_name: 
        :param access_log_setting: 
        :param always_deploy: 
        :param auth: 
        :param binary_media_types: 
        :param cache_cluster_enabled: 
        :param cache_cluster_size: 
        :param canary_setting: 
        :param cors: 
        :param definition_body: 
        :param definition_uri: 
        :param description: 
        :param disable_execute_api_endpoint: 
        :param domain: 
        :param endpoint_configuration: 
        :param gateway_responses: 
        :param method_settings: 
        :param minimum_compression_size: 
        :param models: 
        :param name: 
        :param open_api_version: 
        :param tags: 
        :param tracing_enabled: 
        :param variables: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            # authorizers: Any
            # definition_body: Any
            # gateway_responses: Any
            # method_settings: Any
            # models: Any
            
            cfn_api_props = sam.CfnApiProps(
                stage_name="stageName",
            
                # the properties below are optional
                access_log_setting=sam.CfnApi.AccessLogSettingProperty(
                    destination_arn="destinationArn",
                    format="format"
                ),
                always_deploy=False,
                auth=sam.CfnApi.AuthProperty(
                    add_default_authorizer_to_cors_preflight=False,
                    authorizers=authorizers,
                    default_authorizer="defaultAuthorizer"
                ),
                binary_media_types=["binaryMediaTypes"],
                cache_cluster_enabled=False,
                cache_cluster_size="cacheClusterSize",
                canary_setting=sam.CfnApi.CanarySettingProperty(
                    deployment_id="deploymentId",
                    percent_traffic=123,
                    stage_variable_overrides={
                        "stage_variable_overrides_key": "stageVariableOverrides"
                    },
                    use_stage_cache=False
                ),
                cors="cors",
                definition_body=definition_body,
                definition_uri="definitionUri",
                description="description",
                disable_execute_api_endpoint=False,
                domain=sam.CfnApi.DomainConfigurationProperty(
                    certificate_arn="certificateArn",
                    domain_name="domainName",
            
                    # the properties below are optional
                    base_path=["basePath"],
                    endpoint_configuration="endpointConfiguration",
                    mutual_tls_authentication=sam.CfnApi.MutualTlsAuthenticationProperty(
                        truststore_uri="truststoreUri",
                        truststore_version="truststoreVersion"
                    ),
                    ownership_verification_certificate_arn="ownershipVerificationCertificateArn",
                    route53=sam.CfnApi.Route53ConfigurationProperty(
                        distributed_domain_name="distributedDomainName",
                        evaluate_target_health=False,
                        hosted_zone_id="hostedZoneId",
                        hosted_zone_name="hostedZoneName",
                        ip_v6=False
                    ),
                    security_policy="securityPolicy"
                ),
                endpoint_configuration="endpointConfiguration",
                gateway_responses=gateway_responses,
                method_settings=[method_settings],
                minimum_compression_size=123,
                models=models,
                name="name",
                open_api_version="openApiVersion",
                tags={
                    "tags_key": "tags"
                },
                tracing_enabled=False,
                variables={
                    "variables_key": "variables"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c3541ced1e3b9f417bf5019481767d1f0ed3628dc1464b54b8ea1849ea8aa47)
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
            check_type(argname="argument access_log_setting", value=access_log_setting, expected_type=type_hints["access_log_setting"])
            check_type(argname="argument always_deploy", value=always_deploy, expected_type=type_hints["always_deploy"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument binary_media_types", value=binary_media_types, expected_type=type_hints["binary_media_types"])
            check_type(argname="argument cache_cluster_enabled", value=cache_cluster_enabled, expected_type=type_hints["cache_cluster_enabled"])
            check_type(argname="argument cache_cluster_size", value=cache_cluster_size, expected_type=type_hints["cache_cluster_size"])
            check_type(argname="argument canary_setting", value=canary_setting, expected_type=type_hints["canary_setting"])
            check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
            check_type(argname="argument definition_body", value=definition_body, expected_type=type_hints["definition_body"])
            check_type(argname="argument definition_uri", value=definition_uri, expected_type=type_hints["definition_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_execute_api_endpoint", value=disable_execute_api_endpoint, expected_type=type_hints["disable_execute_api_endpoint"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
            check_type(argname="argument gateway_responses", value=gateway_responses, expected_type=type_hints["gateway_responses"])
            check_type(argname="argument method_settings", value=method_settings, expected_type=type_hints["method_settings"])
            check_type(argname="argument minimum_compression_size", value=minimum_compression_size, expected_type=type_hints["minimum_compression_size"])
            check_type(argname="argument models", value=models, expected_type=type_hints["models"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument open_api_version", value=open_api_version, expected_type=type_hints["open_api_version"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tracing_enabled", value=tracing_enabled, expected_type=type_hints["tracing_enabled"])
            check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "stage_name": stage_name,
        }
        if access_log_setting is not None:
            self._values["access_log_setting"] = access_log_setting
        if always_deploy is not None:
            self._values["always_deploy"] = always_deploy
        if auth is not None:
            self._values["auth"] = auth
        if binary_media_types is not None:
            self._values["binary_media_types"] = binary_media_types
        if cache_cluster_enabled is not None:
            self._values["cache_cluster_enabled"] = cache_cluster_enabled
        if cache_cluster_size is not None:
            self._values["cache_cluster_size"] = cache_cluster_size
        if canary_setting is not None:
            self._values["canary_setting"] = canary_setting
        if cors is not None:
            self._values["cors"] = cors
        if definition_body is not None:
            self._values["definition_body"] = definition_body
        if definition_uri is not None:
            self._values["definition_uri"] = definition_uri
        if description is not None:
            self._values["description"] = description
        if disable_execute_api_endpoint is not None:
            self._values["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if domain is not None:
            self._values["domain"] = domain
        if endpoint_configuration is not None:
            self._values["endpoint_configuration"] = endpoint_configuration
        if gateway_responses is not None:
            self._values["gateway_responses"] = gateway_responses
        if method_settings is not None:
            self._values["method_settings"] = method_settings
        if minimum_compression_size is not None:
            self._values["minimum_compression_size"] = minimum_compression_size
        if models is not None:
            self._values["models"] = models
        if name is not None:
            self._values["name"] = name
        if open_api_version is not None:
            self._values["open_api_version"] = open_api_version
        if tags is not None:
            self._values["tags"] = tags
        if tracing_enabled is not None:
            self._values["tracing_enabled"] = tracing_enabled
        if variables is not None:
            self._values["variables"] = variables

    @builtins.property
    def stage_name(self) -> builtins.str:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-stagename
        '''
        result = self._values.get("stage_name")
        assert result is not None, "Required property 'stage_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_log_setting(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.AccessLogSettingProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-accesslogsetting
        '''
        result = self._values.get("access_log_setting")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.AccessLogSettingProperty]], result)

    @builtins.property
    def always_deploy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-alwaysdeploy
        '''
        result = self._values.get("always_deploy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def auth(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.AuthProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-auth
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.AuthProperty]], result)

    @builtins.property
    def binary_media_types(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-binarymediatypes
        '''
        result = self._values.get("binary_media_types")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def cache_cluster_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-cacheclusterenabled
        '''
        result = self._values.get("cache_cluster_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def cache_cluster_size(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-cacheclustersize
        '''
        result = self._values.get("cache_cluster_size")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def canary_setting(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.CanarySettingProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-canarysetting
        '''
        result = self._values.get("canary_setting")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.CanarySettingProperty]], result)

    @builtins.property
    def cors(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.CorsConfigurationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-cors
        '''
        result = self._values.get("cors")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.CorsConfigurationProperty]], result)

    @builtins.property
    def definition_body(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-definitionbody
        '''
        result = self._values.get("definition_body")
        return typing.cast(typing.Any, result)

    @builtins.property
    def definition_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.S3LocationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-definitionuri
        '''
        result = self._values.get("definition_uri")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.S3LocationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_execute_api_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-disableexecuteapiendpoint
        '''
        result = self._values.get("disable_execute_api_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def domain(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.DomainConfigurationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.DomainConfigurationProperty]], result)

    @builtins.property
    def endpoint_configuration(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.EndpointConfigurationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-endpointconfiguration
        '''
        result = self._values.get("endpoint_configuration")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.EndpointConfigurationProperty]], result)

    @builtins.property
    def gateway_responses(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-gatewayresponses
        '''
        result = self._values.get("gateway_responses")
        return typing.cast(typing.Any, result)

    @builtins.property
    def method_settings(
        self,
    ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-methodsettings
        '''
        result = self._values.get("method_settings")
        return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], result)

    @builtins.property
    def minimum_compression_size(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-minimumcompressionsize
        '''
        result = self._values.get("minimum_compression_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def models(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-models
        '''
        result = self._values.get("models")
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def open_api_version(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-openapiversion
        '''
        result = self._values.get("open_api_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tracing_enabled(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-tracingenabled
        '''
        result = self._values.get("tracing_enabled")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-api.html#cfn-serverless-api-variables
        '''
        result = self._values.get("variables")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnApplication",
):
    '''https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessapplication.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html
    :cloudformationResource: AWS::Serverless::Application
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        cfn_application = sam.CfnApplication(self, "MyCfnApplication",
            location="location",
        
            # the properties below are optional
            notification_arns=["notificationArns"],
            parameters={
                "parameters_key": "parameters"
            },
            tags={
                "tags_key": "tags"
            },
            timeout_in_minutes=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        location: typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnApplication.ApplicationLocationProperty", typing.Dict[builtins.str, typing.Any]]],
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param location: 
        :param notification_arns: 
        :param parameters: 
        :param tags: 
        :param timeout_in_minutes: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64c7803062c8244dab10c00b85c3ab7470f7dfeddb1993dc04852359393beb15)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            location=location,
            notification_arns=notification_arns,
            parameters=parameters,
            tags=tags,
            timeout_in_minutes=timeout_in_minutes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3cfb8ff6c6b925c585f554d1d6674947d33c737cdcd2d16d29336a09fb2af11)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d4faa051f2c7e79e7f0b8a01c67414bff6de09f387a519833619276f21769af3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

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
    @jsii.member(jsii_name="location")
    def location(
        self,
    ) -> typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApplication.ApplicationLocationProperty"]:
        return typing.cast(typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApplication.ApplicationLocationProperty"], jsii.get(self, "location"))

    @location.setter
    def location(
        self,
        value: typing.Union[builtins.str, _IResolvable_da3f097b, "CfnApplication.ApplicationLocationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bea2e888b58c031cfd3e0c09e3a28062b4857ad0468afb21392d872ac2d42fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="notificationArns")
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "notificationArns"))

    @notification_arns.setter
    def notification_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fdba732f0fdb414d7b870bb171355caae720f58a2e5c1495b6c5a846dfb2a30d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationArns", value)

    @builtins.property
    @jsii.member(jsii_name="parameters")
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "parameters"))

    @parameters.setter
    def parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05c9df790cddd4512e3cf1277ea55b48b4d5ddfef54d5b82a13d917e4712e8d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameters", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0fe9f2d4319340e068aa84c98f1764850903463360c677f6dc11f74a9577151f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInMinutes")
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMinutes"))

    @timeout_in_minutes.setter
    def timeout_in_minutes(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afbf7f8fe9ecd7f281a8700abae88f7369951bf8e9137d2c282937a3bd700912)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInMinutes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnApplication.ApplicationLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "application_id": "applicationId",
            "semantic_version": "semanticVersion",
        },
    )
    class ApplicationLocationProperty:
        def __init__(
            self,
            *,
            application_id: builtins.str,
            semantic_version: builtins.str,
        ) -> None:
            '''
            :param application_id: 
            :param semantic_version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-application-applicationlocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                application_location_property = sam.CfnApplication.ApplicationLocationProperty(
                    application_id="applicationId",
                    semantic_version="semanticVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__397227b947496de6fb046a0031f35d134a16d78a2e12e88cce0ddcbadcb03021)
                check_type(argname="argument application_id", value=application_id, expected_type=type_hints["application_id"])
                check_type(argname="argument semantic_version", value=semantic_version, expected_type=type_hints["semantic_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "application_id": application_id,
                "semantic_version": semantic_version,
            }

        @builtins.property
        def application_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-application-applicationlocation.html#cfn-serverless-application-applicationlocation-applicationid
            '''
            result = self._values.get("application_id")
            assert result is not None, "Required property 'application_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def semantic_version(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-application-applicationlocation.html#cfn-serverless-application-applicationlocation-semanticversion
            '''
            result = self._values.get("semantic_version")
            assert result is not None, "Required property 'semantic_version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "location": "location",
        "notification_arns": "notificationArns",
        "parameters": "parameters",
        "tags": "tags",
        "timeout_in_minutes": "timeoutInMinutes",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        location: typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationLocationProperty, typing.Dict[builtins.str, typing.Any]]],
        notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout_in_minutes: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param location: 
        :param notification_arns: 
        :param parameters: 
        :param tags: 
        :param timeout_in_minutes: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            cfn_application_props = sam.CfnApplicationProps(
                location="location",
            
                # the properties below are optional
                notification_arns=["notificationArns"],
                parameters={
                    "parameters_key": "parameters"
                },
                tags={
                    "tags_key": "tags"
                },
                timeout_in_minutes=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5cdd3da86c77e72e8f53daca88bd679d2d41f1881eeba6c4c20c6c5e7f670253)
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument notification_arns", value=notification_arns, expected_type=type_hints["notification_arns"])
            check_type(argname="argument parameters", value=parameters, expected_type=type_hints["parameters"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout_in_minutes", value=timeout_in_minutes, expected_type=type_hints["timeout_in_minutes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "location": location,
        }
        if notification_arns is not None:
            self._values["notification_arns"] = notification_arns
        if parameters is not None:
            self._values["parameters"] = parameters
        if tags is not None:
            self._values["tags"] = tags
        if timeout_in_minutes is not None:
            self._values["timeout_in_minutes"] = timeout_in_minutes

    @builtins.property
    def location(
        self,
    ) -> typing.Union[builtins.str, _IResolvable_da3f097b, CfnApplication.ApplicationLocationProperty]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html#cfn-serverless-application-location
        '''
        result = self._values.get("location")
        assert result is not None, "Required property 'location' is missing"
        return typing.cast(typing.Union[builtins.str, _IResolvable_da3f097b, CfnApplication.ApplicationLocationProperty], result)

    @builtins.property
    def notification_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html#cfn-serverless-application-notificationarns
        '''
        result = self._values.get("notification_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html#cfn-serverless-application-parameters
        '''
        result = self._values.get("parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html#cfn-serverless-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout_in_minutes(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-application.html#cfn-serverless-application-timeoutinminutes
        '''
        result = self._values.get("timeout_in_minutes")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnFunction(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnFunction",
):
    '''https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlessfunction.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html
    :cloudformationResource: AWS::Serverless::Function
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        # assume_role_policy_document: Any
        
        cfn_function = sam.CfnFunction(self, "MyCfnFunction",
            architectures=["architectures"],
            assume_role_policy_document=assume_role_policy_document,
            auto_publish_alias="autoPublishAlias",
            auto_publish_code_sha256="autoPublishCodeSha256",
            code_signing_config_arn="codeSigningConfigArn",
            code_uri="codeUri",
            dead_letter_queue=sam.CfnFunction.DeadLetterQueueProperty(
                target_arn="targetArn",
                type="type"
            ),
            deployment_preference=sam.CfnFunction.DeploymentPreferenceProperty(
                alarms=["alarms"],
                enabled=False,
                hooks=sam.CfnFunction.HooksProperty(
                    post_traffic="postTraffic",
                    pre_traffic="preTraffic"
                ),
                role="role",
                type="type"
            ),
            description="description",
            environment=sam.CfnFunction.FunctionEnvironmentProperty(
                variables={
                    "variables_key": "variables"
                }
            ),
            ephemeral_storage=sam.CfnFunction.EphemeralStorageProperty(
                size=123
            ),
            event_invoke_config=sam.CfnFunction.EventInvokeConfigProperty(
                destination_config=sam.CfnFunction.EventInvokeDestinationConfigProperty(
                    on_failure=sam.CfnFunction.DestinationProperty(
                        destination="destination",
        
                        # the properties below are optional
                        type="type"
                    ),
                    on_success=sam.CfnFunction.DestinationProperty(
                        destination="destination",
        
                        # the properties below are optional
                        type="type"
                    )
                ),
                maximum_event_age_in_seconds=123,
                maximum_retry_attempts=123
            ),
            events={
                "events_key": sam.CfnFunction.EventSourceProperty(
                    properties=sam.CfnFunction.AlexaSkillEventProperty(
                        skill_id="skillId"
                    ),
                    type="type"
                )
            },
            file_system_configs=[sam.CfnFunction.FileSystemConfigProperty(
                arn="arn",
                local_mount_path="localMountPath"
            )],
            function_name="functionName",
            function_url_config=sam.CfnFunction.FunctionUrlConfigProperty(
                auth_type="authType",
        
                # the properties below are optional
                cors="cors",
                invoke_mode="invokeMode"
            ),
            handler="handler",
            image_config=sam.CfnFunction.ImageConfigProperty(
                command=["command"],
                entry_point=["entryPoint"],
                working_directory="workingDirectory"
            ),
            image_uri="imageUri",
            inline_code="inlineCode",
            kms_key_arn="kmsKeyArn",
            layers=["layers"],
            memory_size=123,
            package_type="packageType",
            permissions_boundary="permissionsBoundary",
            policies="policies",
            provisioned_concurrency_config=sam.CfnFunction.ProvisionedConcurrencyConfigProperty(
                provisioned_concurrent_executions="provisionedConcurrentExecutions"
            ),
            reserved_concurrent_executions=123,
            role="role",
            runtime="runtime",
            tags={
                "tags_key": "tags"
            },
            timeout=123,
            tracing="tracing",
            version_description="versionDescription",
            vpc_config=sam.CfnFunction.VpcConfigProperty(
                security_group_ids=["securityGroupIds"],
                subnet_ids=["subnetIds"]
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
        assume_role_policy_document: typing.Any = None,
        auto_publish_alias: typing.Optional[builtins.str] = None,
        auto_publish_code_sha256: typing.Optional[builtins.str] = None,
        code_signing_config_arn: typing.Optional[builtins.str] = None,
        code_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnFunction.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dead_letter_queue: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DeadLetterQueueProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DeploymentPreferenceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.FunctionEnvironmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EphemeralStorageProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        event_invoke_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EventInvokeConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EventSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        file_system_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.FileSystemConfigProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        function_name: typing.Optional[builtins.str] = None,
        function_url_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.FunctionUrlConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        handler: typing.Optional[builtins.str] = None,
        image_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.ImageConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        inline_code: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        layers: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        package_type: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnFunction.IAMPolicyDocumentProperty", typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnFunction.IAMPolicyDocumentProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.SAMPolicyTemplateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        provisioned_concurrency_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.ProvisionedConcurrencyConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        tracing: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.VpcConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param architectures: 
        :param assume_role_policy_document: 
        :param auto_publish_alias: 
        :param auto_publish_code_sha256: 
        :param code_signing_config_arn: 
        :param code_uri: 
        :param dead_letter_queue: 
        :param deployment_preference: 
        :param description: 
        :param environment: 
        :param ephemeral_storage: 
        :param event_invoke_config: 
        :param events: 
        :param file_system_configs: 
        :param function_name: 
        :param function_url_config: 
        :param handler: 
        :param image_config: 
        :param image_uri: 
        :param inline_code: 
        :param kms_key_arn: 
        :param layers: 
        :param memory_size: 
        :param package_type: 
        :param permissions_boundary: 
        :param policies: 
        :param provisioned_concurrency_config: 
        :param reserved_concurrent_executions: 
        :param role: 
        :param runtime: 
        :param tags: 
        :param timeout: 
        :param tracing: 
        :param version_description: 
        :param vpc_config: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da820696f032573ba53a3fb82221aa76870f3c6257f7de23fa48e9c11fdc3f08)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFunctionProps(
            architectures=architectures,
            assume_role_policy_document=assume_role_policy_document,
            auto_publish_alias=auto_publish_alias,
            auto_publish_code_sha256=auto_publish_code_sha256,
            code_signing_config_arn=code_signing_config_arn,
            code_uri=code_uri,
            dead_letter_queue=dead_letter_queue,
            deployment_preference=deployment_preference,
            description=description,
            environment=environment,
            ephemeral_storage=ephemeral_storage,
            event_invoke_config=event_invoke_config,
            events=events,
            file_system_configs=file_system_configs,
            function_name=function_name,
            function_url_config=function_url_config,
            handler=handler,
            image_config=image_config,
            image_uri=image_uri,
            inline_code=inline_code,
            kms_key_arn=kms_key_arn,
            layers=layers,
            memory_size=memory_size,
            package_type=package_type,
            permissions_boundary=permissions_boundary,
            policies=policies,
            provisioned_concurrency_config=provisioned_concurrency_config,
            reserved_concurrent_executions=reserved_concurrent_executions,
            role=role,
            runtime=runtime,
            tags=tags,
            timeout=timeout,
            tracing=tracing,
            version_description=version_description,
            vpc_config=vpc_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e45cd8ce55983e9ade3f7d3db7401329aa94c3de47100e451bd25c652fc8de8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__5d8539381db7c34f023921a302ec379417ffbf36402294f5eb3096b31814951f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

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
    @jsii.member(jsii_name="architectures")
    def architectures(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "architectures"))

    @architectures.setter
    def architectures(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__961f66d7c1974b43320280bf59275bb9f65d08936dd9d10f4bb6bd856765683b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "architectures", value)

    @builtins.property
    @jsii.member(jsii_name="assumeRolePolicyDocument")
    def assume_role_policy_document(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "assumeRolePolicyDocument"))

    @assume_role_policy_document.setter
    def assume_role_policy_document(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d24caacf917d9eb83fd84a13970be6e1524465e06595fa482fd7e7a9ec270bbf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "assumeRolePolicyDocument", value)

    @builtins.property
    @jsii.member(jsii_name="autoPublishAlias")
    def auto_publish_alias(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoPublishAlias"))

    @auto_publish_alias.setter
    def auto_publish_alias(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928c74644f46c5a0366f7094096db9442d7f036bff4056876fdf442aae89329f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoPublishAlias", value)

    @builtins.property
    @jsii.member(jsii_name="autoPublishCodeSha256")
    def auto_publish_code_sha256(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "autoPublishCodeSha256"))

    @auto_publish_code_sha256.setter
    def auto_publish_code_sha256(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a62a2ab953ee75469cf466d51df213fadfd7c1799b0c5c15f75c8fa97f63ef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoPublishCodeSha256", value)

    @builtins.property
    @jsii.member(jsii_name="codeSigningConfigArn")
    def code_signing_config_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "codeSigningConfigArn"))

    @code_signing_config_arn.setter
    def code_signing_config_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__462f250f21efb27dfe8ec5ab212e7a371eb77ae2d2cff5e42b415fe85501e28c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeSigningConfigArn", value)

    @builtins.property
    @jsii.member(jsii_name="codeUri")
    def code_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.S3LocationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.S3LocationProperty"]], jsii.get(self, "codeUri"))

    @code_uri.setter
    def code_uri(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cd8c7343e03b00e454847a98b74d6c18757a798061a0ddaf9a40e957581ac4a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "codeUri", value)

    @builtins.property
    @jsii.member(jsii_name="deadLetterQueue")
    def dead_letter_queue(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DeadLetterQueueProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DeadLetterQueueProperty"]], jsii.get(self, "deadLetterQueue"))

    @dead_letter_queue.setter
    def dead_letter_queue(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DeadLetterQueueProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1602c0ac23686b7e1ab4aa81450903e569d8e163f1f83becee2385582866bbe1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deadLetterQueue", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentPreference")
    def deployment_preference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DeploymentPreferenceProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DeploymentPreferenceProperty"]], jsii.get(self, "deploymentPreference"))

    @deployment_preference.setter
    def deployment_preference(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DeploymentPreferenceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__434662ed37f7d673963a8e62cf6926339c0b7fcb88c58f9dd34b3bd32ef97ba4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentPreference", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b6f7788ac06b74276f6901acf24ecaf6ddabedbb85d96bb18cf3dc5cb0d8297)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="environment")
    def environment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionEnvironmentProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionEnvironmentProperty"]], jsii.get(self, "environment"))

    @environment.setter
    def environment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionEnvironmentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__428eed8cc97b122d6d3fcf1bf8472333306140ea5618f5d11b4469437f630916)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environment", value)

    @builtins.property
    @jsii.member(jsii_name="ephemeralStorage")
    def ephemeral_storage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EphemeralStorageProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EphemeralStorageProperty"]], jsii.get(self, "ephemeralStorage"))

    @ephemeral_storage.setter
    def ephemeral_storage(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EphemeralStorageProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9011531a438d2eaca67b7717924c213173db335f957acba46c544dd74b4ebb72)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ephemeralStorage", value)

    @builtins.property
    @jsii.member(jsii_name="eventInvokeConfig")
    def event_invoke_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EventInvokeConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EventInvokeConfigProperty"]], jsii.get(self, "eventInvokeConfig"))

    @event_invoke_config.setter
    def event_invoke_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EventInvokeConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9204c789f9d6e39e76d74025d5c69e0df77fbfa07d0e171d4cecae9f820841dd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventInvokeConfig", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFunction.EventSourceProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFunction.EventSourceProperty"]]]], jsii.get(self, "events"))

    @events.setter
    def events(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnFunction.EventSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2245995f969ab359206105cc502e300f6696f9fd12878fe4d42221d1797d638e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="fileSystemConfigs")
    def file_system_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunction.FileSystemConfigProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunction.FileSystemConfigProperty"]]]], jsii.get(self, "fileSystemConfigs"))

    @file_system_configs.setter
    def file_system_configs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunction.FileSystemConfigProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85d9a64fa00484d8a57b4834aad1164c5c67d396a62327b84d9334439033a987)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileSystemConfigs", value)

    @builtins.property
    @jsii.member(jsii_name="functionName")
    def function_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "functionName"))

    @function_name.setter
    def function_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cab4b037257cf0675e6835048a9e6cfb3e5cd6acdb3b55b490c89baed365f5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionName", value)

    @builtins.property
    @jsii.member(jsii_name="functionUrlConfig")
    def function_url_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionUrlConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionUrlConfigProperty"]], jsii.get(self, "functionUrlConfig"))

    @function_url_config.setter
    def function_url_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionUrlConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ab14c2ec03c7a9a455a90ea2ef0ddc230f820b134925767451df0b7a7c86933b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "functionUrlConfig", value)

    @builtins.property
    @jsii.member(jsii_name="handler")
    def handler(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "handler"))

    @handler.setter
    def handler(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__377c21e52d013c50d30d5fea093cdec36f68ad854d28d8167a3783f4a9325031)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "handler", value)

    @builtins.property
    @jsii.member(jsii_name="imageConfig")
    def image_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ImageConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ImageConfigProperty"]], jsii.get(self, "imageConfig"))

    @image_config.setter
    def image_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ImageConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54089d0977582d5c52fe11343780afa92a8e83a310df8e70688fea8475dbd769)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageConfig", value)

    @builtins.property
    @jsii.member(jsii_name="imageUri")
    def image_uri(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "imageUri"))

    @image_uri.setter
    def image_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25165da87e6cfd066042bc2056dd24babd47eea0ae440928a841b2bf58331a15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "imageUri", value)

    @builtins.property
    @jsii.member(jsii_name="inlineCode")
    def inline_code(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inlineCode"))

    @inline_code.setter
    def inline_code(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2929da0c5428b1fb11c1c65e03c66d9973c6e3dd0d780359dacfe5a2540e4abe)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inlineCode", value)

    @builtins.property
    @jsii.member(jsii_name="kmsKeyArn")
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyArn"))

    @kms_key_arn.setter
    def kms_key_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9997d0fe87f5763b8f89c3f2e9a29cdb0fc9b631403c7494015279c18e6296e9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyArn", value)

    @builtins.property
    @jsii.member(jsii_name="layers")
    def layers(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "layers"))

    @layers.setter
    def layers(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e4befefb0525c722a39ef1e0102f0459a29f5e5356c132aee49997615b8748d1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layers", value)

    @builtins.property
    @jsii.member(jsii_name="memorySize")
    def memory_size(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "memorySize"))

    @memory_size.setter
    def memory_size(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6af5e2bf43488197cc6f5b04bb14d08efd37e9d60d192cb173bc23214be102f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "memorySize", value)

    @builtins.property
    @jsii.member(jsii_name="packageType")
    def package_type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "packageType"))

    @package_type.setter
    def package_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cd8147db2aefc22ae6b434ed65a87a0ff8e7c7136999239199804af637649806)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "packageType", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundary")
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsBoundary"))

    @permissions_boundary.setter
    def permissions_boundary(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a8715a4cc2adf7439e44f16517420c3a8100bcd7e4f87112ec67554facec1af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundary", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.IAMPolicyDocumentProperty", typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.IAMPolicyDocumentProperty", "CfnFunction.SAMPolicyTemplateProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.IAMPolicyDocumentProperty", typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.IAMPolicyDocumentProperty", "CfnFunction.SAMPolicyTemplateProperty"]]]], jsii.get(self, "policies"))

    @policies.setter
    def policies(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.IAMPolicyDocumentProperty", typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.IAMPolicyDocumentProperty", "CfnFunction.SAMPolicyTemplateProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__723515eaec195d558c2b0a94039b44d2f6f71b663c26fc9b10e22ed013d700f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="provisionedConcurrencyConfig")
    def provisioned_concurrency_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ProvisionedConcurrencyConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ProvisionedConcurrencyConfigProperty"]], jsii.get(self, "provisionedConcurrencyConfig"))

    @provisioned_concurrency_config.setter
    def provisioned_concurrency_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ProvisionedConcurrencyConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ae3ba871bdb92769cd518d31fe5feb386d450634d533562571e0615487f99895)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedConcurrencyConfig", value)

    @builtins.property
    @jsii.member(jsii_name="reservedConcurrentExecutions")
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "reservedConcurrentExecutions"))

    @reserved_concurrent_executions.setter
    def reserved_concurrent_executions(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c2b977ba94a4c4945498cbd322fabf09517286f8ac213e5c731e705341c92e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reservedConcurrentExecutions", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "role"))

    @role.setter
    def role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0043d107bb7948c568b884ae4373072e04967fa286a3683b7ff122face99e23d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="runtime")
    def runtime(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "runtime"))

    @runtime.setter
    def runtime(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cc251e6ad3743a7b8ec0db51b707d68db1077bce8c40f0750bbefa772191aa8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "runtime", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a812fb883340d42ee86b3177bf56d4cbad4fe39e7ebdee880b6444f84b71912a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="timeout")
    def timeout(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeout"))

    @timeout.setter
    def timeout(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72a6bef8ed2bad0c1bae6b02c41c93b4e95c2bfc799e03db9e219bda13907d10)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeout", value)

    @builtins.property
    @jsii.member(jsii_name="tracing")
    def tracing(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tracing"))

    @tracing.setter
    def tracing(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba0c5501cb85e810b59d3660e5b8e6c48fb00cc9ff1d8d6e3a86dd424d0bf9ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tracing", value)

    @builtins.property
    @jsii.member(jsii_name="versionDescription")
    def version_description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "versionDescription"))

    @version_description.setter
    def version_description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2050e867f2d1878cd72f006d40acf5a093399cd84485570dc3134fad0c9b3a5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "versionDescription", value)

    @builtins.property
    @jsii.member(jsii_name="vpcConfig")
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.VpcConfigProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.VpcConfigProperty"]], jsii.get(self, "vpcConfig"))

    @vpc_config.setter
    def vpc_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.VpcConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f964396263820171d9c1edb021bcf4380c3bed41a2e424da67596989c6e18b94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.AlexaSkillEventProperty",
        jsii_struct_bases=[],
        name_mapping={"skill_id": "skillId"},
    )
    class AlexaSkillEventProperty:
        def __init__(self, *, skill_id: builtins.str) -> None:
            '''
            :param skill_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-alexaskillevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                alexa_skill_event_property = sam.CfnFunction.AlexaSkillEventProperty(
                    skill_id="skillId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3124f40a27e9cf66ff11c883916bf49e663187b79e9133aa89ceb6611bca8300)
                check_type(argname="argument skill_id", value=skill_id, expected_type=type_hints["skill_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "skill_id": skill_id,
            }

        @builtins.property
        def skill_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-alexaskillevent.html#cfn-serverless-function-alexaskillevent-skillid
            '''
            result = self._values.get("skill_id")
            assert result is not None, "Required property 'skill_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlexaSkillEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.ApiEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "method": "method",
            "path": "path",
            "auth": "auth",
            "request_model": "requestModel",
            "request_parameters": "requestParameters",
            "rest_api_id": "restApiId",
        },
    )
    class ApiEventProperty:
        def __init__(
            self,
            *,
            method: builtins.str,
            path: builtins.str,
            auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.AuthProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            request_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.RequestModelProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            request_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnFunction.RequestParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            rest_api_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param method: 
            :param path: 
            :param auth: 
            :param request_model: 
            :param request_parameters: 
            :param rest_api_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # custom_statements: Any
                
                api_event_property = sam.CfnFunction.ApiEventProperty(
                    method="method",
                    path="path",
                
                    # the properties below are optional
                    auth=sam.CfnFunction.AuthProperty(
                        api_key_required=False,
                        authorization_scopes=["authorizationScopes"],
                        authorizer="authorizer",
                        resource_policy=sam.CfnFunction.AuthResourcePolicyProperty(
                            aws_account_blacklist=["awsAccountBlacklist"],
                            aws_account_whitelist=["awsAccountWhitelist"],
                            custom_statements=[custom_statements],
                            intrinsic_vpc_blacklist=["intrinsicVpcBlacklist"],
                            intrinsic_vpce_blacklist=["intrinsicVpceBlacklist"],
                            intrinsic_vpce_whitelist=["intrinsicVpceWhitelist"],
                            intrinsic_vpc_whitelist=["intrinsicVpcWhitelist"],
                            ip_range_blacklist=["ipRangeBlacklist"],
                            ip_range_whitelist=["ipRangeWhitelist"],
                            source_vpc_blacklist=["sourceVpcBlacklist"],
                            source_vpc_whitelist=["sourceVpcWhitelist"]
                        )
                    ),
                    request_model=sam.CfnFunction.RequestModelProperty(
                        model="model",
                
                        # the properties below are optional
                        required=False,
                        validate_body=False,
                        validate_parameters=False
                    ),
                    request_parameters=["requestParameters"],
                    rest_api_id="restApiId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4f431b22ab6809e259ce2cfa0a8d8ae7ab76c9c0e9197b6defd75f8427566d0d)
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
                check_type(argname="argument request_model", value=request_model, expected_type=type_hints["request_model"])
                check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
                check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "method": method,
                "path": path,
            }
            if auth is not None:
                self._values["auth"] = auth
            if request_model is not None:
                self._values["request_model"] = request_model
            if request_parameters is not None:
                self._values["request_parameters"] = request_parameters
            if rest_api_id is not None:
                self._values["rest_api_id"] = rest_api_id

        @builtins.property
        def method(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html#cfn-serverless-function-apievent-method
            '''
            result = self._values.get("method")
            assert result is not None, "Required property 'method' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html#cfn-serverless-function-apievent-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auth(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.AuthProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html#cfn-serverless-function-apievent-auth
            '''
            result = self._values.get("auth")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.AuthProperty"]], result)

        @builtins.property
        def request_model(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.RequestModelProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html#cfn-serverless-function-apievent-requestmodel
            '''
            result = self._values.get("request_model")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.RequestModelProperty"]], result)

        @builtins.property
        def request_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.RequestParameterProperty"]]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html#cfn-serverless-function-apievent-requestparameters
            '''
            result = self._values.get("request_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.RequestParameterProperty"]]]], result)

        @builtins.property
        def rest_api_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-apievent.html#cfn-serverless-function-apievent-restapiid
            '''
            result = self._values.get("rest_api_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.AuthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_key_required": "apiKeyRequired",
            "authorization_scopes": "authorizationScopes",
            "authorizer": "authorizer",
            "resource_policy": "resourcePolicy",
        },
    )
    class AuthProperty:
        def __init__(
            self,
            *,
            api_key_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            authorizer: typing.Optional[builtins.str] = None,
            resource_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.AuthResourcePolicyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param api_key_required: 
            :param authorization_scopes: 
            :param authorizer: 
            :param resource_policy: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-auth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # custom_statements: Any
                
                auth_property = sam.CfnFunction.AuthProperty(
                    api_key_required=False,
                    authorization_scopes=["authorizationScopes"],
                    authorizer="authorizer",
                    resource_policy=sam.CfnFunction.AuthResourcePolicyProperty(
                        aws_account_blacklist=["awsAccountBlacklist"],
                        aws_account_whitelist=["awsAccountWhitelist"],
                        custom_statements=[custom_statements],
                        intrinsic_vpc_blacklist=["intrinsicVpcBlacklist"],
                        intrinsic_vpce_blacklist=["intrinsicVpceBlacklist"],
                        intrinsic_vpce_whitelist=["intrinsicVpceWhitelist"],
                        intrinsic_vpc_whitelist=["intrinsicVpcWhitelist"],
                        ip_range_blacklist=["ipRangeBlacklist"],
                        ip_range_whitelist=["ipRangeWhitelist"],
                        source_vpc_blacklist=["sourceVpcBlacklist"],
                        source_vpc_whitelist=["sourceVpcWhitelist"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__996c871f7db703ff8a44473691cb09158b2791e2346716a2043c81e40cb18878)
                check_type(argname="argument api_key_required", value=api_key_required, expected_type=type_hints["api_key_required"])
                check_type(argname="argument authorization_scopes", value=authorization_scopes, expected_type=type_hints["authorization_scopes"])
                check_type(argname="argument authorizer", value=authorizer, expected_type=type_hints["authorizer"])
                check_type(argname="argument resource_policy", value=resource_policy, expected_type=type_hints["resource_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if api_key_required is not None:
                self._values["api_key_required"] = api_key_required
            if authorization_scopes is not None:
                self._values["authorization_scopes"] = authorization_scopes
            if authorizer is not None:
                self._values["authorizer"] = authorizer
            if resource_policy is not None:
                self._values["resource_policy"] = resource_policy

        @builtins.property
        def api_key_required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-auth.html#cfn-serverless-function-auth-apikeyrequired
            '''
            result = self._values.get("api_key_required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def authorization_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-auth.html#cfn-serverless-function-auth-authorizationscopes
            '''
            result = self._values.get("authorization_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def authorizer(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-auth.html#cfn-serverless-function-auth-authorizer
            '''
            result = self._values.get("authorizer")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.AuthResourcePolicyProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-auth.html#cfn-serverless-function-auth-resourcepolicy
            '''
            result = self._values.get("resource_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.AuthResourcePolicyProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.AuthResourcePolicyProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_account_blacklist": "awsAccountBlacklist",
            "aws_account_whitelist": "awsAccountWhitelist",
            "custom_statements": "customStatements",
            "intrinsic_vpc_blacklist": "intrinsicVpcBlacklist",
            "intrinsic_vpce_blacklist": "intrinsicVpceBlacklist",
            "intrinsic_vpce_whitelist": "intrinsicVpceWhitelist",
            "intrinsic_vpc_whitelist": "intrinsicVpcWhitelist",
            "ip_range_blacklist": "ipRangeBlacklist",
            "ip_range_whitelist": "ipRangeWhitelist",
            "source_vpc_blacklist": "sourceVpcBlacklist",
            "source_vpc_whitelist": "sourceVpcWhitelist",
        },
    )
    class AuthResourcePolicyProperty:
        def __init__(
            self,
            *,
            aws_account_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
            aws_account_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
            custom_statements: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
            intrinsic_vpc_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
            intrinsic_vpce_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
            intrinsic_vpce_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
            intrinsic_vpc_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
            ip_range_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
            ip_range_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
            source_vpc_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
            source_vpc_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param aws_account_blacklist: 
            :param aws_account_whitelist: 
            :param custom_statements: 
            :param intrinsic_vpc_blacklist: 
            :param intrinsic_vpce_blacklist: 
            :param intrinsic_vpce_whitelist: 
            :param intrinsic_vpc_whitelist: 
            :param ip_range_blacklist: 
            :param ip_range_whitelist: 
            :param source_vpc_blacklist: 
            :param source_vpc_whitelist: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # custom_statements: Any
                
                auth_resource_policy_property = sam.CfnFunction.AuthResourcePolicyProperty(
                    aws_account_blacklist=["awsAccountBlacklist"],
                    aws_account_whitelist=["awsAccountWhitelist"],
                    custom_statements=[custom_statements],
                    intrinsic_vpc_blacklist=["intrinsicVpcBlacklist"],
                    intrinsic_vpce_blacklist=["intrinsicVpceBlacklist"],
                    intrinsic_vpce_whitelist=["intrinsicVpceWhitelist"],
                    intrinsic_vpc_whitelist=["intrinsicVpcWhitelist"],
                    ip_range_blacklist=["ipRangeBlacklist"],
                    ip_range_whitelist=["ipRangeWhitelist"],
                    source_vpc_blacklist=["sourceVpcBlacklist"],
                    source_vpc_whitelist=["sourceVpcWhitelist"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f4e76793befb0779e1b3791b310b700b6dd4dc94bfc2025141c8541ac674d43)
                check_type(argname="argument aws_account_blacklist", value=aws_account_blacklist, expected_type=type_hints["aws_account_blacklist"])
                check_type(argname="argument aws_account_whitelist", value=aws_account_whitelist, expected_type=type_hints["aws_account_whitelist"])
                check_type(argname="argument custom_statements", value=custom_statements, expected_type=type_hints["custom_statements"])
                check_type(argname="argument intrinsic_vpc_blacklist", value=intrinsic_vpc_blacklist, expected_type=type_hints["intrinsic_vpc_blacklist"])
                check_type(argname="argument intrinsic_vpce_blacklist", value=intrinsic_vpce_blacklist, expected_type=type_hints["intrinsic_vpce_blacklist"])
                check_type(argname="argument intrinsic_vpce_whitelist", value=intrinsic_vpce_whitelist, expected_type=type_hints["intrinsic_vpce_whitelist"])
                check_type(argname="argument intrinsic_vpc_whitelist", value=intrinsic_vpc_whitelist, expected_type=type_hints["intrinsic_vpc_whitelist"])
                check_type(argname="argument ip_range_blacklist", value=ip_range_blacklist, expected_type=type_hints["ip_range_blacklist"])
                check_type(argname="argument ip_range_whitelist", value=ip_range_whitelist, expected_type=type_hints["ip_range_whitelist"])
                check_type(argname="argument source_vpc_blacklist", value=source_vpc_blacklist, expected_type=type_hints["source_vpc_blacklist"])
                check_type(argname="argument source_vpc_whitelist", value=source_vpc_whitelist, expected_type=type_hints["source_vpc_whitelist"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_account_blacklist is not None:
                self._values["aws_account_blacklist"] = aws_account_blacklist
            if aws_account_whitelist is not None:
                self._values["aws_account_whitelist"] = aws_account_whitelist
            if custom_statements is not None:
                self._values["custom_statements"] = custom_statements
            if intrinsic_vpc_blacklist is not None:
                self._values["intrinsic_vpc_blacklist"] = intrinsic_vpc_blacklist
            if intrinsic_vpce_blacklist is not None:
                self._values["intrinsic_vpce_blacklist"] = intrinsic_vpce_blacklist
            if intrinsic_vpce_whitelist is not None:
                self._values["intrinsic_vpce_whitelist"] = intrinsic_vpce_whitelist
            if intrinsic_vpc_whitelist is not None:
                self._values["intrinsic_vpc_whitelist"] = intrinsic_vpc_whitelist
            if ip_range_blacklist is not None:
                self._values["ip_range_blacklist"] = ip_range_blacklist
            if ip_range_whitelist is not None:
                self._values["ip_range_whitelist"] = ip_range_whitelist
            if source_vpc_blacklist is not None:
                self._values["source_vpc_blacklist"] = source_vpc_blacklist
            if source_vpc_whitelist is not None:
                self._values["source_vpc_whitelist"] = source_vpc_whitelist

        @builtins.property
        def aws_account_blacklist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-awsaccountblacklist
            '''
            result = self._values.get("aws_account_blacklist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def aws_account_whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-awsaccountwhitelist
            '''
            result = self._values.get("aws_account_whitelist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def custom_statements(
            self,
        ) -> typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-customstatements
            '''
            result = self._values.get("custom_statements")
            return typing.cast(typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]], result)

        @builtins.property
        def intrinsic_vpc_blacklist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-intrinsicvpcblacklist
            '''
            result = self._values.get("intrinsic_vpc_blacklist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def intrinsic_vpce_blacklist(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-intrinsicvpceblacklist
            '''
            result = self._values.get("intrinsic_vpce_blacklist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def intrinsic_vpce_whitelist(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-intrinsicvpcewhitelist
            '''
            result = self._values.get("intrinsic_vpce_whitelist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def intrinsic_vpc_whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-intrinsicvpcwhitelist
            '''
            result = self._values.get("intrinsic_vpc_whitelist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def ip_range_blacklist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-iprangeblacklist
            '''
            result = self._values.get("ip_range_blacklist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def ip_range_whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-iprangewhitelist
            '''
            result = self._values.get("ip_range_whitelist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def source_vpc_blacklist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-sourcevpcblacklist
            '''
            result = self._values.get("source_vpc_blacklist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def source_vpc_whitelist(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-authresourcepolicy.html#cfn-serverless-function-authresourcepolicy-sourcevpcwhitelist
            '''
            result = self._values.get("source_vpc_whitelist")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AuthResourcePolicyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.BucketSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket_name": "bucketName"},
    )
    class BucketSAMPTProperty:
        def __init__(self, *, bucket_name: builtins.str) -> None:
            '''
            :param bucket_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-bucketsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                bucket_sAMPTProperty = sam.CfnFunction.BucketSAMPTProperty(
                    bucket_name="bucketName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e32c5d57ac6183e9b983ffee717a883834c6cd8abc9cff6eafc5dd3db50076f)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-bucketsampt.html#cfn-serverless-function-bucketsampt-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BucketSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.CloudWatchEventEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pattern": "pattern",
            "input": "input",
            "input_path": "inputPath",
        },
    )
    class CloudWatchEventEventProperty:
        def __init__(
            self,
            *,
            pattern: typing.Any,
            input: typing.Optional[builtins.str] = None,
            input_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param pattern: 
            :param input: 
            :param input_path: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatcheventevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # pattern: Any
                
                cloud_watch_event_event_property = sam.CfnFunction.CloudWatchEventEventProperty(
                    pattern=pattern,
                
                    # the properties below are optional
                    input="input",
                    input_path="inputPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be8ac98ed839a6bf585f926df5cfdc585e188fadadb59d1f1ab3b400f4f5b8dc)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pattern": pattern,
            }
            if input is not None:
                self._values["input"] = input
            if input_path is not None:
                self._values["input_path"] = input_path

        @builtins.property
        def pattern(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatcheventevent.html#cfn-serverless-function-cloudwatcheventevent-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatcheventevent.html#cfn-serverless-function-cloudwatcheventevent-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatcheventevent.html#cfn-serverless-function-cloudwatcheventevent-inputpath
            '''
            result = self._values.get("input_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchEventEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.CloudWatchLogsEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "filter_pattern": "filterPattern",
            "log_group_name": "logGroupName",
        },
    )
    class CloudWatchLogsEventProperty:
        def __init__(
            self,
            *,
            filter_pattern: builtins.str,
            log_group_name: builtins.str,
        ) -> None:
            '''
            :param filter_pattern: 
            :param log_group_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatchlogsevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                cloud_watch_logs_event_property = sam.CfnFunction.CloudWatchLogsEventProperty(
                    filter_pattern="filterPattern",
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d94fbed6c1c504c6a4078c8680333fcee8b6484a9ee431feaed212bfc5d4b139)
                check_type(argname="argument filter_pattern", value=filter_pattern, expected_type=type_hints["filter_pattern"])
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "filter_pattern": filter_pattern,
                "log_group_name": log_group_name,
            }

        @builtins.property
        def filter_pattern(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatchlogsevent.html#cfn-serverless-function-cloudwatchlogsevent-filterpattern
            '''
            result = self._values.get("filter_pattern")
            assert result is not None, "Required property 'filter_pattern' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cloudwatchlogsevent.html#cfn-serverless-function-cloudwatchlogsevent-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.CognitoEventProperty",
        jsii_struct_bases=[],
        name_mapping={"trigger": "trigger", "user_pool": "userPool"},
    )
    class CognitoEventProperty:
        def __init__(self, *, trigger: builtins.str, user_pool: builtins.str) -> None:
            '''
            :param trigger: 
            :param user_pool: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cognitoevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                cognito_event_property = sam.CfnFunction.CognitoEventProperty(
                    trigger="trigger",
                    user_pool="userPool"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__32d7960cc4b1211bf60468d1f1ecd9519efe3f5ed0542d2fd8e57411f28e2c6e)
                check_type(argname="argument trigger", value=trigger, expected_type=type_hints["trigger"])
                check_type(argname="argument user_pool", value=user_pool, expected_type=type_hints["user_pool"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "trigger": trigger,
                "user_pool": user_pool,
            }

        @builtins.property
        def trigger(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cognitoevent.html#cfn-serverless-function-cognitoevent-trigger
            '''
            result = self._values.get("trigger")
            assert result is not None, "Required property 'trigger' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def user_pool(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-cognitoevent.html#cfn-serverless-function-cognitoevent-userpool
            '''
            result = self._values.get("user_pool")
            assert result is not None, "Required property 'user_pool' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CognitoEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.CollectionSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"collection_id": "collectionId"},
    )
    class CollectionSAMPTProperty:
        def __init__(self, *, collection_id: builtins.str) -> None:
            '''
            :param collection_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-collectionsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                collection_sAMPTProperty = sam.CfnFunction.CollectionSAMPTProperty(
                    collection_id="collectionId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91c13b6a4fa04c2fd214ebd4f9d5faa0504e553c9c177f43a0a91c75576b6355)
                check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "collection_id": collection_id,
            }

        @builtins.property
        def collection_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-collectionsampt.html#cfn-serverless-function-collectionsampt-collectionid
            '''
            result = self._values.get("collection_id")
            assert result is not None, "Required property 'collection_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CollectionSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.CorsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_origin": "allowOrigin",
            "allow_credentials": "allowCredentials",
            "allow_headers": "allowHeaders",
            "allow_methods": "allowMethods",
            "max_age": "maxAge",
        },
    )
    class CorsConfigurationProperty:
        def __init__(
            self,
            *,
            allow_origin: builtins.str,
            allow_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            allow_headers: typing.Optional[builtins.str] = None,
            allow_methods: typing.Optional[builtins.str] = None,
            max_age: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param allow_origin: 
            :param allow_credentials: 
            :param allow_headers: 
            :param allow_methods: 
            :param max_age: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-corsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                cors_configuration_property = sam.CfnFunction.CorsConfigurationProperty(
                    allow_origin="allowOrigin",
                
                    # the properties below are optional
                    allow_credentials=False,
                    allow_headers="allowHeaders",
                    allow_methods="allowMethods",
                    max_age="maxAge"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1fac2265244f6246045fce25da128ba28a1ecb08ded9209e8645ac8803baf502)
                check_type(argname="argument allow_origin", value=allow_origin, expected_type=type_hints["allow_origin"])
                check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
                check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
                check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
                check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "allow_origin": allow_origin,
            }
            if allow_credentials is not None:
                self._values["allow_credentials"] = allow_credentials
            if allow_headers is not None:
                self._values["allow_headers"] = allow_headers
            if allow_methods is not None:
                self._values["allow_methods"] = allow_methods
            if max_age is not None:
                self._values["max_age"] = max_age

        @builtins.property
        def allow_origin(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-corsconfiguration.html#cfn-serverless-function-corsconfiguration-alloworigin
            '''
            result = self._values.get("allow_origin")
            assert result is not None, "Required property 'allow_origin' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def allow_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-corsconfiguration.html#cfn-serverless-function-corsconfiguration-allowcredentials
            '''
            result = self._values.get("allow_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def allow_headers(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-corsconfiguration.html#cfn-serverless-function-corsconfiguration-allowheaders
            '''
            result = self._values.get("allow_headers")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def allow_methods(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-corsconfiguration.html#cfn-serverless-function-corsconfiguration-allowmethods
            '''
            result = self._values.get("allow_methods")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def max_age(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-corsconfiguration.html#cfn-serverless-function-corsconfiguration-maxage
            '''
            result = self._values.get("max_age")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CorsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.DeadLetterQueueProperty",
        jsii_struct_bases=[],
        name_mapping={"target_arn": "targetArn", "type": "type"},
    )
    class DeadLetterQueueProperty:
        def __init__(self, *, target_arn: builtins.str, type: builtins.str) -> None:
            '''
            :param target_arn: 
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deadletterqueue.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                dead_letter_queue_property = sam.CfnFunction.DeadLetterQueueProperty(
                    target_arn="targetArn",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__143f4d03feab04a8091259025b7001d0b3a0ff69ed51079f2b5c3fb6ea308d0e)
                check_type(argname="argument target_arn", value=target_arn, expected_type=type_hints["target_arn"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "target_arn": target_arn,
                "type": type,
            }

        @builtins.property
        def target_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deadletterqueue.html#cfn-serverless-function-deadletterqueue-targetarn
            '''
            result = self._values.get("target_arn")
            assert result is not None, "Required property 'target_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deadletterqueue.html#cfn-serverless-function-deadletterqueue-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeadLetterQueueProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.DeploymentPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "alarms": "alarms",
            "enabled": "enabled",
            "hooks": "hooks",
            "role": "role",
            "type": "type",
        },
    )
    class DeploymentPreferenceProperty:
        def __init__(
            self,
            *,
            alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            hooks: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.HooksProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            role: typing.Optional[builtins.str] = None,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param alarms: 
            :param enabled: 
            :param hooks: 
            :param role: 
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deploymentpreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                deployment_preference_property = sam.CfnFunction.DeploymentPreferenceProperty(
                    alarms=["alarms"],
                    enabled=False,
                    hooks=sam.CfnFunction.HooksProperty(
                        post_traffic="postTraffic",
                        pre_traffic="preTraffic"
                    ),
                    role="role",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__80ec550d24f9c572e123af872fcbd1cc14c85c62218fcfd842baa9ea0c19457a)
                check_type(argname="argument alarms", value=alarms, expected_type=type_hints["alarms"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument hooks", value=hooks, expected_type=type_hints["hooks"])
                check_type(argname="argument role", value=role, expected_type=type_hints["role"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if alarms is not None:
                self._values["alarms"] = alarms
            if enabled is not None:
                self._values["enabled"] = enabled
            if hooks is not None:
                self._values["hooks"] = hooks
            if role is not None:
                self._values["role"] = role
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def alarms(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deploymentpreference.html#cfn-serverless-function-deploymentpreference-alarms
            '''
            result = self._values.get("alarms")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deploymentpreference.html#cfn-serverless-function-deploymentpreference-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def hooks(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.HooksProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deploymentpreference.html#cfn-serverless-function-deploymentpreference-hooks
            '''
            result = self._values.get("hooks")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.HooksProperty"]], result)

        @builtins.property
        def role(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deploymentpreference.html#cfn-serverless-function-deploymentpreference-role
            '''
            result = self._values.get("role")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-deploymentpreference.html#cfn-serverless-function-deploymentpreference-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeploymentPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.DestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"on_failure": "onFailure"},
    )
    class DestinationConfigProperty:
        def __init__(
            self,
            *,
            on_failure: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param on_failure: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-destinationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                destination_config_property = sam.CfnFunction.DestinationConfigProperty(
                    on_failure=sam.CfnFunction.DestinationProperty(
                        destination="destination",
                
                        # the properties below are optional
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e4e6834826ec418bf7cb40a517aefae406afe2f01b87c594e8231af7ef2d44d)
                check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "on_failure": on_failure,
            }

        @builtins.property
        def on_failure(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-destinationconfig.html#cfn-serverless-function-destinationconfig-onfailure
            '''
            result = self._values.get("on_failure")
            assert result is not None, "Required property 'on_failure' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.DestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "type": "type"},
    )
    class DestinationProperty:
        def __init__(
            self,
            *,
            destination: builtins.str,
            type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination: 
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-destination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                destination_property = sam.CfnFunction.DestinationProperty(
                    destination="destination",
                
                    # the properties below are optional
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__19a984fddac7f5aa6614ba358e496e5c6a3d64eafb7a8830156d75413789877b)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
            }
            if type is not None:
                self._values["type"] = type

        @builtins.property
        def destination(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-destination.html#cfn-serverless-function-destination-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-destination.html#cfn-serverless-function-destination-type
            '''
            result = self._values.get("type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.DomainSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"domain_name": "domainName"},
    )
    class DomainSAMPTProperty:
        def __init__(self, *, domain_name: builtins.str) -> None:
            '''
            :param domain_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-domainsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                domain_sAMPTProperty = sam.CfnFunction.DomainSAMPTProperty(
                    domain_name="domainName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3416f800b26e4a4b713814421c02a5eb690455ce925e56586a4b9cc295c379de)
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "domain_name": domain_name,
            }

        @builtins.property
        def domain_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-domainsampt.html#cfn-serverless-function-domainsampt-domainname
            '''
            result = self._values.get("domain_name")
            assert result is not None, "Required property 'domain_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.DynamoDBEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "starting_position": "startingPosition",
            "stream": "stream",
            "batch_size": "batchSize",
            "bisect_batch_on_function_error": "bisectBatchOnFunctionError",
            "destination_config": "destinationConfig",
            "enabled": "enabled",
            "maximum_batching_window_in_seconds": "maximumBatchingWindowInSeconds",
            "maximum_record_age_in_seconds": "maximumRecordAgeInSeconds",
            "maximum_retry_attempts": "maximumRetryAttempts",
            "parallelization_factor": "parallelizationFactor",
        },
    )
    class DynamoDBEventProperty:
        def __init__(
            self,
            *,
            starting_position: builtins.str,
            stream: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            destination_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DestinationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_retry_attempts: typing.Optional[jsii.Number] = None,
            parallelization_factor: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param starting_position: 
            :param stream: 
            :param batch_size: 
            :param bisect_batch_on_function_error: 
            :param destination_config: 
            :param enabled: 
            :param maximum_batching_window_in_seconds: 
            :param maximum_record_age_in_seconds: 
            :param maximum_retry_attempts: 
            :param parallelization_factor: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                dynamo_dBEvent_property = sam.CfnFunction.DynamoDBEventProperty(
                    starting_position="startingPosition",
                    stream="stream",
                
                    # the properties below are optional
                    batch_size=123,
                    bisect_batch_on_function_error=False,
                    destination_config=sam.CfnFunction.DestinationConfigProperty(
                        on_failure=sam.CfnFunction.DestinationProperty(
                            destination="destination",
                
                            # the properties below are optional
                            type="type"
                        )
                    ),
                    enabled=False,
                    maximum_batching_window_in_seconds=123,
                    maximum_record_age_in_seconds=123,
                    maximum_retry_attempts=123,
                    parallelization_factor=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7994f805931bd9f33200b9289406ebe947e1aced753b2b63caa991acbaf8375c)
                check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
                check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument bisect_batch_on_function_error", value=bisect_batch_on_function_error, expected_type=type_hints["bisect_batch_on_function_error"])
                check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument maximum_batching_window_in_seconds", value=maximum_batching_window_in_seconds, expected_type=type_hints["maximum_batching_window_in_seconds"])
                check_type(argname="argument maximum_record_age_in_seconds", value=maximum_record_age_in_seconds, expected_type=type_hints["maximum_record_age_in_seconds"])
                check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
                check_type(argname="argument parallelization_factor", value=parallelization_factor, expected_type=type_hints["parallelization_factor"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "starting_position": starting_position,
                "stream": stream,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if bisect_batch_on_function_error is not None:
                self._values["bisect_batch_on_function_error"] = bisect_batch_on_function_error
            if destination_config is not None:
                self._values["destination_config"] = destination_config
            if enabled is not None:
                self._values["enabled"] = enabled
            if maximum_batching_window_in_seconds is not None:
                self._values["maximum_batching_window_in_seconds"] = maximum_batching_window_in_seconds
            if maximum_record_age_in_seconds is not None:
                self._values["maximum_record_age_in_seconds"] = maximum_record_age_in_seconds
            if maximum_retry_attempts is not None:
                self._values["maximum_retry_attempts"] = maximum_retry_attempts
            if parallelization_factor is not None:
                self._values["parallelization_factor"] = parallelization_factor

        @builtins.property
        def starting_position(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-startingposition
            '''
            result = self._values.get("starting_position")
            assert result is not None, "Required property 'starting_position' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stream(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-stream
            '''
            result = self._values.get("stream")
            assert result is not None, "Required property 'stream' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def bisect_batch_on_function_error(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-bisectbatchonfunctionerror
            '''
            result = self._values.get("bisect_batch_on_function_error")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def destination_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-destinationconfig
            '''
            result = self._values.get("destination_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationConfigProperty"]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def maximum_batching_window_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-maximumbatchingwindowinseconds
            '''
            result = self._values.get("maximum_batching_window_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_record_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-maximumrecordageinseconds
            '''
            result = self._values.get("maximum_record_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-maximumretryattempts
            '''
            result = self._values.get("maximum_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def parallelization_factor(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-dynamodbevent.html#cfn-serverless-function-dynamodbevent-parallelizationfactor
            '''
            result = self._values.get("parallelization_factor")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DynamoDBEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.EmptySAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={},
    )
    class EmptySAMPTProperty:
        def __init__(self) -> None:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-emptysampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                empty_sAMPTProperty = sam.CfnFunction.EmptySAMPTProperty()
            '''
            self._values: typing.Dict[builtins.str, typing.Any] = {}

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmptySAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.EphemeralStorageProperty",
        jsii_struct_bases=[],
        name_mapping={"size": "size"},
    )
    class EphemeralStorageProperty:
        def __init__(self, *, size: jsii.Number) -> None:
            '''
            :param size: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-ephemeralstorage.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                ephemeral_storage_property = sam.CfnFunction.EphemeralStorageProperty(
                    size=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__45ce4e684ab9f5b3cf6bc040b2591caf92efd3e71ca512561d8aadf333956351)
                check_type(argname="argument size", value=size, expected_type=type_hints["size"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "size": size,
            }

        @builtins.property
        def size(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-ephemeralstorage.html#cfn-serverless-function-ephemeralstorage-size
            '''
            result = self._values.get("size")
            assert result is not None, "Required property 'size' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EphemeralStorageProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.EventBridgeRuleEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pattern": "pattern",
            "event_bus_name": "eventBusName",
            "input": "input",
            "input_path": "inputPath",
        },
    )
    class EventBridgeRuleEventProperty:
        def __init__(
            self,
            *,
            pattern: typing.Any,
            event_bus_name: typing.Optional[builtins.str] = None,
            input: typing.Optional[builtins.str] = None,
            input_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param pattern: 
            :param event_bus_name: 
            :param input: 
            :param input_path: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventbridgeruleevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # pattern: Any
                
                event_bridge_rule_event_property = sam.CfnFunction.EventBridgeRuleEventProperty(
                    pattern=pattern,
                
                    # the properties below are optional
                    event_bus_name="eventBusName",
                    input="input",
                    input_path="inputPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d21280faa223e5cbaf484b31b1a54c1e27952496279e4371dd37068f58de2e84)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pattern": pattern,
            }
            if event_bus_name is not None:
                self._values["event_bus_name"] = event_bus_name
            if input is not None:
                self._values["input"] = input
            if input_path is not None:
                self._values["input_path"] = input_path

        @builtins.property
        def pattern(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventbridgeruleevent.html#cfn-serverless-function-eventbridgeruleevent-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_bus_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventbridgeruleevent.html#cfn-serverless-function-eventbridgeruleevent-eventbusname
            '''
            result = self._values.get("event_bus_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventbridgeruleevent.html#cfn-serverless-function-eventbridgeruleevent-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventbridgeruleevent.html#cfn-serverless-function-eventbridgeruleevent-inputpath
            '''
            result = self._values.get("input_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeRuleEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.EventInvokeConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destination_config": "destinationConfig",
            "maximum_event_age_in_seconds": "maximumEventAgeInSeconds",
            "maximum_retry_attempts": "maximumRetryAttempts",
        },
    )
    class EventInvokeConfigProperty:
        def __init__(
            self,
            *,
            destination_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EventInvokeDestinationConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
            maximum_retry_attempts: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param destination_config: 
            :param maximum_event_age_in_seconds: 
            :param maximum_retry_attempts: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokeconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                event_invoke_config_property = sam.CfnFunction.EventInvokeConfigProperty(
                    destination_config=sam.CfnFunction.EventInvokeDestinationConfigProperty(
                        on_failure=sam.CfnFunction.DestinationProperty(
                            destination="destination",
                
                            # the properties below are optional
                            type="type"
                        ),
                        on_success=sam.CfnFunction.DestinationProperty(
                            destination="destination",
                
                            # the properties below are optional
                            type="type"
                        )
                    ),
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8ffdd8314f781fb14b52a4e1dcbd551aaa143d3be4ebfc91835e84610c1a8221)
                check_type(argname="argument destination_config", value=destination_config, expected_type=type_hints["destination_config"])
                check_type(argname="argument maximum_event_age_in_seconds", value=maximum_event_age_in_seconds, expected_type=type_hints["maximum_event_age_in_seconds"])
                check_type(argname="argument maximum_retry_attempts", value=maximum_retry_attempts, expected_type=type_hints["maximum_retry_attempts"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_config is not None:
                self._values["destination_config"] = destination_config
            if maximum_event_age_in_seconds is not None:
                self._values["maximum_event_age_in_seconds"] = maximum_event_age_in_seconds
            if maximum_retry_attempts is not None:
                self._values["maximum_retry_attempts"] = maximum_retry_attempts

        @builtins.property
        def destination_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EventInvokeDestinationConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokeconfig.html#cfn-serverless-function-eventinvokeconfig-destinationconfig
            '''
            result = self._values.get("destination_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EventInvokeDestinationConfigProperty"]], result)

        @builtins.property
        def maximum_event_age_in_seconds(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokeconfig.html#cfn-serverless-function-eventinvokeconfig-maximumeventageinseconds
            '''
            result = self._values.get("maximum_event_age_in_seconds")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def maximum_retry_attempts(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokeconfig.html#cfn-serverless-function-eventinvokeconfig-maximumretryattempts
            '''
            result = self._values.get("maximum_retry_attempts")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventInvokeConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.EventInvokeDestinationConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"on_failure": "onFailure", "on_success": "onSuccess"},
    )
    class EventInvokeDestinationConfigProperty:
        def __init__(
            self,
            *,
            on_failure: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
            on_success: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DestinationProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param on_failure: 
            :param on_success: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokedestinationconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                event_invoke_destination_config_property = sam.CfnFunction.EventInvokeDestinationConfigProperty(
                    on_failure=sam.CfnFunction.DestinationProperty(
                        destination="destination",
                
                        # the properties below are optional
                        type="type"
                    ),
                    on_success=sam.CfnFunction.DestinationProperty(
                        destination="destination",
                
                        # the properties below are optional
                        type="type"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__824278198c661e967b66f4eb4f6fbf05437a14c87c92ad92b09b58ec2b9430b4)
                check_type(argname="argument on_failure", value=on_failure, expected_type=type_hints["on_failure"])
                check_type(argname="argument on_success", value=on_success, expected_type=type_hints["on_success"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "on_failure": on_failure,
                "on_success": on_success,
            }

        @builtins.property
        def on_failure(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokedestinationconfig.html#cfn-serverless-function-eventinvokedestinationconfig-onfailure
            '''
            result = self._values.get("on_failure")
            assert result is not None, "Required property 'on_failure' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationProperty"], result)

        @builtins.property
        def on_success(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventinvokedestinationconfig.html#cfn-serverless-function-eventinvokedestinationconfig-onsuccess
            '''
            result = self._values.get("on_success")
            assert result is not None, "Required property 'on_success' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunction.DestinationProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventInvokeDestinationConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.EventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"properties": "properties", "type": "type"},
    )
    class EventSourceProperty:
        def __init__(
            self,
            *,
            properties: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.AlexaSkillEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.ApiEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.CloudWatchEventEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.CloudWatchLogsEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.CognitoEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.DynamoDBEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.EventBridgeRuleEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.HttpApiEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.IoTRuleEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.KinesisEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.S3EventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.ScheduleEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.SNSEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnFunction.SQSEventProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''
            :param properties: 
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                event_source_property = sam.CfnFunction.EventSourceProperty(
                    properties=sam.CfnFunction.AlexaSkillEventProperty(
                        skill_id="skillId"
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__46dbad2fdf51b82abf61512b482e040cb7a9cad1c34fcb57e442b94e170227ba)
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "properties": properties,
                "type": type,
            }

        @builtins.property
        def properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunction.AlexaSkillEventProperty", "CfnFunction.ApiEventProperty", "CfnFunction.CloudWatchEventEventProperty", "CfnFunction.CloudWatchLogsEventProperty", "CfnFunction.CognitoEventProperty", "CfnFunction.DynamoDBEventProperty", "CfnFunction.EventBridgeRuleEventProperty", "CfnFunction.HttpApiEventProperty", "CfnFunction.IoTRuleEventProperty", "CfnFunction.KinesisEventProperty", "CfnFunction.S3EventProperty", "CfnFunction.ScheduleEventProperty", "CfnFunction.SNSEventProperty", "CfnFunction.SQSEventProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventsource.html#cfn-serverless-function-eventsource-properties
            '''
            result = self._values.get("properties")
            assert result is not None, "Required property 'properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunction.AlexaSkillEventProperty", "CfnFunction.ApiEventProperty", "CfnFunction.CloudWatchEventEventProperty", "CfnFunction.CloudWatchLogsEventProperty", "CfnFunction.CognitoEventProperty", "CfnFunction.DynamoDBEventProperty", "CfnFunction.EventBridgeRuleEventProperty", "CfnFunction.HttpApiEventProperty", "CfnFunction.IoTRuleEventProperty", "CfnFunction.KinesisEventProperty", "CfnFunction.S3EventProperty", "CfnFunction.ScheduleEventProperty", "CfnFunction.SNSEventProperty", "CfnFunction.SQSEventProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-eventsource.html#cfn-serverless-function-eventsource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.FileSystemConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn", "local_mount_path": "localMountPath"},
    )
    class FileSystemConfigProperty:
        def __init__(
            self,
            *,
            arn: typing.Optional[builtins.str] = None,
            local_mount_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param arn: 
            :param local_mount_path: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-filesystemconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                file_system_config_property = sam.CfnFunction.FileSystemConfigProperty(
                    arn="arn",
                    local_mount_path="localMountPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__042927e3bdc41bb37d7a425bbdfe932f3c1c939361ff5d3c2e6aecdc7fa434c9)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
                check_type(argname="argument local_mount_path", value=local_mount_path, expected_type=type_hints["local_mount_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if arn is not None:
                self._values["arn"] = arn
            if local_mount_path is not None:
                self._values["local_mount_path"] = local_mount_path

        @builtins.property
        def arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-filesystemconfig.html#cfn-serverless-function-filesystemconfig-arn
            '''
            result = self._values.get("arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def local_mount_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-filesystemconfig.html#cfn-serverless-function-filesystemconfig-localmountpath
            '''
            result = self._values.get("local_mount_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FileSystemConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.FunctionEnvironmentProperty",
        jsii_struct_bases=[],
        name_mapping={"variables": "variables"},
    )
    class FunctionEnvironmentProperty:
        def __init__(
            self,
            *,
            variables: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
        ) -> None:
            '''
            :param variables: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionenvironment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                function_environment_property = sam.CfnFunction.FunctionEnvironmentProperty(
                    variables={
                        "variables_key": "variables"
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cede0a875bba921466167c6599c161022b6030dbd7aafacc22aff1e6368d599c)
                check_type(argname="argument variables", value=variables, expected_type=type_hints["variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "variables": variables,
            }

        @builtins.property
        def variables(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionenvironment.html#cfn-serverless-function-functionenvironment-variables
            '''
            result = self._values.get("variables")
            assert result is not None, "Required property 'variables' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionEnvironmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.FunctionSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"function_name": "functionName"},
    )
    class FunctionSAMPTProperty:
        def __init__(self, *, function_name: builtins.str) -> None:
            '''
            :param function_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                function_sAMPTProperty = sam.CfnFunction.FunctionSAMPTProperty(
                    function_name="functionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__093f81bb3b5e1c086cd55a2d914acaab8a0a0ef0a4767ba196b131038b617b48)
                check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_name": function_name,
            }

        @builtins.property
        def function_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionsampt.html#cfn-serverless-function-functionsampt-functionname
            '''
            result = self._values.get("function_name")
            assert result is not None, "Required property 'function_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.FunctionUrlConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auth_type": "authType",
            "cors": "cors",
            "invoke_mode": "invokeMode",
        },
    )
    class FunctionUrlConfigProperty:
        def __init__(
            self,
            *,
            auth_type: builtins.str,
            cors: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnFunction.CorsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            invoke_mode: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param auth_type: 
            :param cors: 
            :param invoke_mode: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionurlconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                function_url_config_property = sam.CfnFunction.FunctionUrlConfigProperty(
                    auth_type="authType",
                
                    # the properties below are optional
                    cors="cors",
                    invoke_mode="invokeMode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4ecb4b4628aaffa7df25337985d75a10475a9a2acc64c33bc5ba8f22327c6647)
                check_type(argname="argument auth_type", value=auth_type, expected_type=type_hints["auth_type"])
                check_type(argname="argument cors", value=cors, expected_type=type_hints["cors"])
                check_type(argname="argument invoke_mode", value=invoke_mode, expected_type=type_hints["invoke_mode"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auth_type": auth_type,
            }
            if cors is not None:
                self._values["cors"] = cors
            if invoke_mode is not None:
                self._values["invoke_mode"] = invoke_mode

        @builtins.property
        def auth_type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionurlconfig.html#cfn-serverless-function-functionurlconfig-authtype
            '''
            result = self._values.get("auth_type")
            assert result is not None, "Required property 'auth_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def cors(
            self,
        ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.CorsConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionurlconfig.html#cfn-serverless-function-functionurlconfig-cors
            '''
            result = self._values.get("cors")
            return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnFunction.CorsConfigurationProperty"]], result)

        @builtins.property
        def invoke_mode(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-functionurlconfig.html#cfn-serverless-function-functionurlconfig-invokemode
            '''
            result = self._values.get("invoke_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionUrlConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.HooksProperty",
        jsii_struct_bases=[],
        name_mapping={"post_traffic": "postTraffic", "pre_traffic": "preTraffic"},
    )
    class HooksProperty:
        def __init__(
            self,
            *,
            post_traffic: typing.Optional[builtins.str] = None,
            pre_traffic: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param post_traffic: 
            :param pre_traffic: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-hooks.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                hooks_property = sam.CfnFunction.HooksProperty(
                    post_traffic="postTraffic",
                    pre_traffic="preTraffic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9007aebebebbce69c2d0c87f2e2742d1f8498d07cfe80ad0bb6c7443e5ac3797)
                check_type(argname="argument post_traffic", value=post_traffic, expected_type=type_hints["post_traffic"])
                check_type(argname="argument pre_traffic", value=pre_traffic, expected_type=type_hints["pre_traffic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if post_traffic is not None:
                self._values["post_traffic"] = post_traffic
            if pre_traffic is not None:
                self._values["pre_traffic"] = pre_traffic

        @builtins.property
        def post_traffic(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-hooks.html#cfn-serverless-function-hooks-posttraffic
            '''
            result = self._values.get("post_traffic")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def pre_traffic(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-hooks.html#cfn-serverless-function-hooks-pretraffic
            '''
            result = self._values.get("pre_traffic")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HooksProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.HttpApiEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "api_id": "apiId",
            "auth": "auth",
            "method": "method",
            "path": "path",
            "payload_format_version": "payloadFormatVersion",
            "route_settings": "routeSettings",
            "timeout_in_millis": "timeoutInMillis",
        },
    )
    class HttpApiEventProperty:
        def __init__(
            self,
            *,
            api_id: typing.Optional[builtins.str] = None,
            auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.HttpApiFunctionAuthProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            method: typing.Optional[builtins.str] = None,
            path: typing.Optional[builtins.str] = None,
            payload_format_version: typing.Optional[builtins.str] = None,
            route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.RouteSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            timeout_in_millis: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param api_id: 
            :param auth: 
            :param method: 
            :param path: 
            :param payload_format_version: 
            :param route_settings: 
            :param timeout_in_millis: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                http_api_event_property = sam.CfnFunction.HttpApiEventProperty(
                    api_id="apiId",
                    auth=sam.CfnFunction.HttpApiFunctionAuthProperty(
                        authorization_scopes=["authorizationScopes"],
                        authorizer="authorizer"
                    ),
                    method="method",
                    path="path",
                    payload_format_version="payloadFormatVersion",
                    route_settings=sam.CfnFunction.RouteSettingsProperty(
                        data_trace_enabled=False,
                        detailed_metrics_enabled=False,
                        logging_level="loggingLevel",
                        throttling_burst_limit=123,
                        throttling_rate_limit=123
                    ),
                    timeout_in_millis=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10711eaebc24b0b6d7c2096fa4e2efff09f1dc344dcd813dfbdbc65a0cd69d73)
                check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
                check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument payload_format_version", value=payload_format_version, expected_type=type_hints["payload_format_version"])
                check_type(argname="argument route_settings", value=route_settings, expected_type=type_hints["route_settings"])
                check_type(argname="argument timeout_in_millis", value=timeout_in_millis, expected_type=type_hints["timeout_in_millis"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if api_id is not None:
                self._values["api_id"] = api_id
            if auth is not None:
                self._values["auth"] = auth
            if method is not None:
                self._values["method"] = method
            if path is not None:
                self._values["path"] = path
            if payload_format_version is not None:
                self._values["payload_format_version"] = payload_format_version
            if route_settings is not None:
                self._values["route_settings"] = route_settings
            if timeout_in_millis is not None:
                self._values["timeout_in_millis"] = timeout_in_millis

        @builtins.property
        def api_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-apiid
            '''
            result = self._values.get("api_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def auth(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.HttpApiFunctionAuthProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-auth
            '''
            result = self._values.get("auth")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.HttpApiFunctionAuthProperty"]], result)

        @builtins.property
        def method(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-method
            '''
            result = self._values.get("method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-path
            '''
            result = self._values.get("path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload_format_version(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-payloadformatversion
            '''
            result = self._values.get("payload_format_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def route_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.RouteSettingsProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-routesettings
            '''
            result = self._values.get("route_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.RouteSettingsProperty"]], result)

        @builtins.property
        def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapievent.html#cfn-serverless-function-httpapievent-timeoutinmillis
            '''
            result = self._values.get("timeout_in_millis")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpApiEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.HttpApiFunctionAuthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_scopes": "authorizationScopes",
            "authorizer": "authorizer",
        },
    )
    class HttpApiFunctionAuthProperty:
        def __init__(
            self,
            *,
            authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            authorizer: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param authorization_scopes: 
            :param authorizer: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapifunctionauth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                http_api_function_auth_property = sam.CfnFunction.HttpApiFunctionAuthProperty(
                    authorization_scopes=["authorizationScopes"],
                    authorizer="authorizer"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7365210f2c0abe85eb4502abc70c0b91d091d90ad61f62b0e413a9f142531309)
                check_type(argname="argument authorization_scopes", value=authorization_scopes, expected_type=type_hints["authorization_scopes"])
                check_type(argname="argument authorizer", value=authorizer, expected_type=type_hints["authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorization_scopes is not None:
                self._values["authorization_scopes"] = authorization_scopes
            if authorizer is not None:
                self._values["authorizer"] = authorizer

        @builtins.property
        def authorization_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapifunctionauth.html#cfn-serverless-function-httpapifunctionauth-authorizationscopes
            '''
            result = self._values.get("authorization_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def authorizer(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-httpapifunctionauth.html#cfn-serverless-function-httpapifunctionauth-authorizer
            '''
            result = self._values.get("authorizer")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpApiFunctionAuthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.IAMPolicyDocumentProperty",
        jsii_struct_bases=[],
        name_mapping={"statement": "statement", "version": "version"},
    )
    class IAMPolicyDocumentProperty:
        def __init__(
            self,
            *,
            statement: typing.Any,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param statement: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-iampolicydocument.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # statement: Any
                
                i_aMPolicy_document_property = {
                    "statement": statement,
                
                    # the properties below are optional
                    "version": "version"
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10e67c50da978059d59c88ab8b8d1c7852ab81b9305b4eedbcdef681cc22ae0a)
                check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "statement": statement,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def statement(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-iampolicydocument.html#cfn-serverless-function-iampolicydocument-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-iampolicydocument.html#cfn-serverless-function-iampolicydocument-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IAMPolicyDocumentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.IdentitySAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"identity_name": "identityName"},
    )
    class IdentitySAMPTProperty:
        def __init__(self, *, identity_name: builtins.str) -> None:
            '''
            :param identity_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-identitysampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                identity_sAMPTProperty = sam.CfnFunction.IdentitySAMPTProperty(
                    identity_name="identityName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5e74d676d636da35f6fc94bb061eab42dfecba551f1f354cc4928c40528cdcc3)
                check_type(argname="argument identity_name", value=identity_name, expected_type=type_hints["identity_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "identity_name": identity_name,
            }

        @builtins.property
        def identity_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-identitysampt.html#cfn-serverless-function-identitysampt-identityname
            '''
            result = self._values.get("identity_name")
            assert result is not None, "Required property 'identity_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IdentitySAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.ImageConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "command": "command",
            "entry_point": "entryPoint",
            "working_directory": "workingDirectory",
        },
    )
    class ImageConfigProperty:
        def __init__(
            self,
            *,
            command: typing.Optional[typing.Sequence[builtins.str]] = None,
            entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
            working_directory: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param command: 
            :param entry_point: 
            :param working_directory: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-imageconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                image_config_property = sam.CfnFunction.ImageConfigProperty(
                    command=["command"],
                    entry_point=["entryPoint"],
                    working_directory="workingDirectory"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a4e61b4308921771ef55342ceffbb48da8059092023443e34810850ff6021235)
                check_type(argname="argument command", value=command, expected_type=type_hints["command"])
                check_type(argname="argument entry_point", value=entry_point, expected_type=type_hints["entry_point"])
                check_type(argname="argument working_directory", value=working_directory, expected_type=type_hints["working_directory"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if command is not None:
                self._values["command"] = command
            if entry_point is not None:
                self._values["entry_point"] = entry_point
            if working_directory is not None:
                self._values["working_directory"] = working_directory

        @builtins.property
        def command(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-imageconfig.html#cfn-serverless-function-imageconfig-command
            '''
            result = self._values.get("command")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def entry_point(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-imageconfig.html#cfn-serverless-function-imageconfig-entrypoint
            '''
            result = self._values.get("entry_point")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def working_directory(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-imageconfig.html#cfn-serverless-function-imageconfig-workingdirectory
            '''
            result = self._values.get("working_directory")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ImageConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.IoTRuleEventProperty",
        jsii_struct_bases=[],
        name_mapping={"sql": "sql", "aws_iot_sql_version": "awsIotSqlVersion"},
    )
    class IoTRuleEventProperty:
        def __init__(
            self,
            *,
            sql: builtins.str,
            aws_iot_sql_version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param sql: 
            :param aws_iot_sql_version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-iotruleevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                io_tRule_event_property = sam.CfnFunction.IoTRuleEventProperty(
                    sql="sql",
                
                    # the properties below are optional
                    aws_iot_sql_version="awsIotSqlVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e155526e0eb0c3fe9a5bad17ef4db715f4ba1cfd78bd6267ee8d5bc11fbc7b18)
                check_type(argname="argument sql", value=sql, expected_type=type_hints["sql"])
                check_type(argname="argument aws_iot_sql_version", value=aws_iot_sql_version, expected_type=type_hints["aws_iot_sql_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "sql": sql,
            }
            if aws_iot_sql_version is not None:
                self._values["aws_iot_sql_version"] = aws_iot_sql_version

        @builtins.property
        def sql(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-iotruleevent.html#cfn-serverless-function-iotruleevent-sql
            '''
            result = self._values.get("sql")
            assert result is not None, "Required property 'sql' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def aws_iot_sql_version(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-iotruleevent.html#cfn-serverless-function-iotruleevent-awsiotsqlversion
            '''
            result = self._values.get("aws_iot_sql_version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IoTRuleEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.KeySAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"key_id": "keyId"},
    )
    class KeySAMPTProperty:
        def __init__(self, *, key_id: builtins.str) -> None:
            '''
            :param key_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-keysampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                key_sAMPTProperty = sam.CfnFunction.KeySAMPTProperty(
                    key_id="keyId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__56d5c6f0f2fc01f9bdb0ea9e83b7b977b59c1cb7a304425fef68de2469c11aa9)
                check_type(argname="argument key_id", value=key_id, expected_type=type_hints["key_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key_id": key_id,
            }

        @builtins.property
        def key_id(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-keysampt.html#cfn-serverless-function-keysampt-keyid
            '''
            result = self._values.get("key_id")
            assert result is not None, "Required property 'key_id' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KeySAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.KinesisEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "starting_position": "startingPosition",
            "stream": "stream",
            "batch_size": "batchSize",
            "enabled": "enabled",
            "function_response_types": "functionResponseTypes",
        },
    )
    class KinesisEventProperty:
        def __init__(
            self,
            *,
            starting_position: builtins.str,
            stream: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            function_response_types: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''
            :param starting_position: 
            :param stream: 
            :param batch_size: 
            :param enabled: 
            :param function_response_types: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-kinesisevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                kinesis_event_property = sam.CfnFunction.KinesisEventProperty(
                    starting_position="startingPosition",
                    stream="stream",
                
                    # the properties below are optional
                    batch_size=123,
                    enabled=False,
                    function_response_types=["functionResponseTypes"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c64b1479b0a1842a1a96847b1a4615e328dddd86e05be0127714e361981e5dd6)
                check_type(argname="argument starting_position", value=starting_position, expected_type=type_hints["starting_position"])
                check_type(argname="argument stream", value=stream, expected_type=type_hints["stream"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument function_response_types", value=function_response_types, expected_type=type_hints["function_response_types"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "starting_position": starting_position,
                "stream": stream,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if enabled is not None:
                self._values["enabled"] = enabled
            if function_response_types is not None:
                self._values["function_response_types"] = function_response_types

        @builtins.property
        def starting_position(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-kinesisevent.html#cfn-serverless-function-kinesisevent-startingposition
            '''
            result = self._values.get("starting_position")
            assert result is not None, "Required property 'starting_position' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def stream(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-kinesisevent.html#cfn-serverless-function-kinesisevent-stream
            '''
            result = self._values.get("stream")
            assert result is not None, "Required property 'stream' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-kinesisevent.html#cfn-serverless-function-kinesisevent-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-kinesisevent.html#cfn-serverless-function-kinesisevent-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def function_response_types(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-kinesisevent.html#cfn-serverless-function-kinesisevent-functionresponsetypes
            '''
            result = self._values.get("function_response_types")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.LogGroupSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_name": "logGroupName"},
    )
    class LogGroupSAMPTProperty:
        def __init__(self, *, log_group_name: builtins.str) -> None:
            '''
            :param log_group_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-loggroupsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                log_group_sAMPTProperty = sam.CfnFunction.LogGroupSAMPTProperty(
                    log_group_name="logGroupName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e04b4c22d0166d6a3e5bd312c5c7d7ca6dc30a06d07b767141bb937c6cd7df74)
                check_type(argname="argument log_group_name", value=log_group_name, expected_type=type_hints["log_group_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_name": log_group_name,
            }

        @builtins.property
        def log_group_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-loggroupsampt.html#cfn-serverless-function-loggroupsampt-loggroupname
            '''
            result = self._values.get("log_group_name")
            assert result is not None, "Required property 'log_group_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogGroupSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.ParameterNameSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"parameter_name": "parameterName"},
    )
    class ParameterNameSAMPTProperty:
        def __init__(self, *, parameter_name: builtins.str) -> None:
            '''
            :param parameter_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-parameternamesampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                parameter_name_sAMPTProperty = sam.CfnFunction.ParameterNameSAMPTProperty(
                    parameter_name="parameterName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f5d361077204df508de1a22cf132522e123ef11c5d1b23a775902f5df87b052d)
                check_type(argname="argument parameter_name", value=parameter_name, expected_type=type_hints["parameter_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "parameter_name": parameter_name,
            }

        @builtins.property
        def parameter_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-parameternamesampt.html#cfn-serverless-function-parameternamesampt-parametername
            '''
            result = self._values.get("parameter_name")
            assert result is not None, "Required property 'parameter_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterNameSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.ProvisionedConcurrencyConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "provisioned_concurrent_executions": "provisionedConcurrentExecutions",
        },
    )
    class ProvisionedConcurrencyConfigProperty:
        def __init__(self, *, provisioned_concurrent_executions: builtins.str) -> None:
            '''
            :param provisioned_concurrent_executions: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-provisionedconcurrencyconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                provisioned_concurrency_config_property = sam.CfnFunction.ProvisionedConcurrencyConfigProperty(
                    provisioned_concurrent_executions="provisionedConcurrentExecutions"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11e41d9d2beb27f643bf25f769e8756e262c4750aeefbdc253950be55dda6ea3)
                check_type(argname="argument provisioned_concurrent_executions", value=provisioned_concurrent_executions, expected_type=type_hints["provisioned_concurrent_executions"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "provisioned_concurrent_executions": provisioned_concurrent_executions,
            }

        @builtins.property
        def provisioned_concurrent_executions(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-provisionedconcurrencyconfig.html#cfn-serverless-function-provisionedconcurrencyconfig-provisionedconcurrentexecutions
            '''
            result = self._values.get("provisioned_concurrent_executions")
            assert result is not None, "Required property 'provisioned_concurrent_executions' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedConcurrencyConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.QueueSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"queue_name": "queueName"},
    )
    class QueueSAMPTProperty:
        def __init__(self, *, queue_name: builtins.str) -> None:
            '''
            :param queue_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-queuesampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                queue_sAMPTProperty = sam.CfnFunction.QueueSAMPTProperty(
                    queue_name="queueName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2f0ef722a937a4210b60a915a707d83376fb56a04f5d7b493e528cba0661511d)
                check_type(argname="argument queue_name", value=queue_name, expected_type=type_hints["queue_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "queue_name": queue_name,
            }

        @builtins.property
        def queue_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-queuesampt.html#cfn-serverless-function-queuesampt-queuename
            '''
            result = self._values.get("queue_name")
            assert result is not None, "Required property 'queue_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueueSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.RequestModelProperty",
        jsii_struct_bases=[],
        name_mapping={
            "model": "model",
            "required": "required",
            "validate_body": "validateBody",
            "validate_parameters": "validateParameters",
        },
    )
    class RequestModelProperty:
        def __init__(
            self,
            *,
            model: builtins.str,
            required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            validate_body: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            validate_parameters: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param model: 
            :param required: 
            :param validate_body: 
            :param validate_parameters: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestmodel.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                request_model_property = sam.CfnFunction.RequestModelProperty(
                    model="model",
                
                    # the properties below are optional
                    required=False,
                    validate_body=False,
                    validate_parameters=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e309219acb0472ca0420cd85b485500ae16158e868f05c5257fcc93556c6d73)
                check_type(argname="argument model", value=model, expected_type=type_hints["model"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
                check_type(argname="argument validate_body", value=validate_body, expected_type=type_hints["validate_body"])
                check_type(argname="argument validate_parameters", value=validate_parameters, expected_type=type_hints["validate_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "model": model,
            }
            if required is not None:
                self._values["required"] = required
            if validate_body is not None:
                self._values["validate_body"] = validate_body
            if validate_parameters is not None:
                self._values["validate_parameters"] = validate_parameters

        @builtins.property
        def model(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestmodel.html#cfn-serverless-function-requestmodel-model
            '''
            result = self._values.get("model")
            assert result is not None, "Required property 'model' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestmodel.html#cfn-serverless-function-requestmodel-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def validate_body(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestmodel.html#cfn-serverless-function-requestmodel-validatebody
            '''
            result = self._values.get("validate_body")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def validate_parameters(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestmodel.html#cfn-serverless-function-requestmodel-validateparameters
            '''
            result = self._values.get("validate_parameters")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequestModelProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.RequestParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"caching": "caching", "required": "required"},
    )
    class RequestParameterProperty:
        def __init__(
            self,
            *,
            caching: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param caching: 
            :param required: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                request_parameter_property = sam.CfnFunction.RequestParameterProperty(
                    caching=False,
                    required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ac1e4a6cd652a6ad38da31062b24a82f26babdae66941dee658ef4cd3024ded0)
                check_type(argname="argument caching", value=caching, expected_type=type_hints["caching"])
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if caching is not None:
                self._values["caching"] = caching
            if required is not None:
                self._values["required"] = required

        @builtins.property
        def caching(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestparameter.html#cfn-serverless-function-requestparameter-caching
            '''
            result = self._values.get("caching")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def required(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-requestparameter.html#cfn-serverless-function-requestparameter-required
            '''
            result = self._values.get("required")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RequestParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.RouteSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_trace_enabled": "dataTraceEnabled",
            "detailed_metrics_enabled": "detailedMetricsEnabled",
            "logging_level": "loggingLevel",
            "throttling_burst_limit": "throttlingBurstLimit",
            "throttling_rate_limit": "throttlingRateLimit",
        },
    )
    class RouteSettingsProperty:
        def __init__(
            self,
            *,
            data_trace_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            detailed_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            logging_level: typing.Optional[builtins.str] = None,
            throttling_burst_limit: typing.Optional[jsii.Number] = None,
            throttling_rate_limit: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param data_trace_enabled: 
            :param detailed_metrics_enabled: 
            :param logging_level: 
            :param throttling_burst_limit: 
            :param throttling_rate_limit: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-routesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                route_settings_property = sam.CfnFunction.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a5029f2218b4af39c4bf3f003cf8016727b01889d5237da1b4bb1d35b53449a1)
                check_type(argname="argument data_trace_enabled", value=data_trace_enabled, expected_type=type_hints["data_trace_enabled"])
                check_type(argname="argument detailed_metrics_enabled", value=detailed_metrics_enabled, expected_type=type_hints["detailed_metrics_enabled"])
                check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
                check_type(argname="argument throttling_burst_limit", value=throttling_burst_limit, expected_type=type_hints["throttling_burst_limit"])
                check_type(argname="argument throttling_rate_limit", value=throttling_rate_limit, expected_type=type_hints["throttling_rate_limit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_trace_enabled is not None:
                self._values["data_trace_enabled"] = data_trace_enabled
            if detailed_metrics_enabled is not None:
                self._values["detailed_metrics_enabled"] = detailed_metrics_enabled
            if logging_level is not None:
                self._values["logging_level"] = logging_level
            if throttling_burst_limit is not None:
                self._values["throttling_burst_limit"] = throttling_burst_limit
            if throttling_rate_limit is not None:
                self._values["throttling_rate_limit"] = throttling_rate_limit

        @builtins.property
        def data_trace_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-routesettings.html#cfn-serverless-function-routesettings-datatraceenabled
            '''
            result = self._values.get("data_trace_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def detailed_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-routesettings.html#cfn-serverless-function-routesettings-detailedmetricsenabled
            '''
            result = self._values.get("detailed_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def logging_level(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-routesettings.html#cfn-serverless-function-routesettings-logginglevel
            '''
            result = self._values.get("logging_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-routesettings.html#cfn-serverless-function-routesettings-throttlingburstlimit
            '''
            result = self._values.get("throttling_burst_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-routesettings.html#cfn-serverless-function-routesettings-throttlingratelimit
            '''
            result = self._values.get("throttling_rate_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouteSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.S3EventProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "events": "events", "filter": "filter"},
    )
    class S3EventProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            events: builtins.str,
            filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.S3NotificationFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param bucket: 
            :param events: 
            :param filter: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3event.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_event_property = sam.CfnFunction.S3EventProperty(
                    bucket="bucket",
                    events="events",
                
                    # the properties below are optional
                    filter=sam.CfnFunction.S3NotificationFilterProperty(
                        s3_key=sam.CfnFunction.S3KeyFilterProperty(
                            rules=[sam.CfnFunction.S3KeyFilterRuleProperty(
                                name="name",
                                value="value"
                            )]
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9e49962e8f915b8ef11062814b9a35ca163775e823fb71789a682db9ceef34fb)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument events", value=events, expected_type=type_hints["events"])
                check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "events": events,
            }
            if filter is not None:
                self._values["filter"] = filter

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3event.html#cfn-serverless-function-s3event-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def events(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3event.html#cfn-serverless-function-s3event-events
            '''
            result = self._values.get("events")
            assert result is not None, "Required property 'events' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def filter(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.S3NotificationFilterProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3event.html#cfn-serverless-function-s3event-filter
            '''
            result = self._values.get("filter")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.S3NotificationFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3EventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.S3KeyFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"rules": "rules"},
    )
    class S3KeyFilterProperty:
        def __init__(
            self,
            *,
            rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.S3KeyFilterRuleProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''
            :param rules: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3keyfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_key_filter_property = sam.CfnFunction.S3KeyFilterProperty(
                    rules=[sam.CfnFunction.S3KeyFilterRuleProperty(
                        name="name",
                        value="value"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d5c06b2d04548048dde09ea0b1fe8ba1a7e4939a8123d9061cb00f7a61062a41)
                check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "rules": rules,
            }

        @builtins.property
        def rules(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunction.S3KeyFilterRuleProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3keyfilter.html#cfn-serverless-function-s3keyfilter-rules
            '''
            result = self._values.get("rules")
            assert result is not None, "Required property 'rules' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFunction.S3KeyFilterRuleProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3KeyFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.S3KeyFilterRuleProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "value": "value"},
    )
    class S3KeyFilterRuleProperty:
        def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
            '''
            :param name: 
            :param value: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3keyfilterrule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_key_filter_rule_property = sam.CfnFunction.S3KeyFilterRuleProperty(
                    name="name",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e611d540226e79d90ea54cd8dfc0d647853595c3f36c905003cee579212129e3)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "value": value,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3keyfilterrule.html#cfn-serverless-function-s3keyfilterrule-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3keyfilterrule.html#cfn-serverless-function-s3keyfilterrule-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3KeyFilterRuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key", "version": "version"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param bucket: 
            :param key: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_location_property = sam.CfnFunction.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                
                    # the properties below are optional
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__322de417e8a25e0402c762766d176033d9474d7a731b49c4ed8ebab366cf93f0)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3location.html#cfn-serverless-function-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3location.html#cfn-serverless-function-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3location.html#cfn-serverless-function-s3location-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.S3NotificationFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"s3_key": "s3Key"},
    )
    class S3NotificationFilterProperty:
        def __init__(
            self,
            *,
            s3_key: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.S3KeyFilterProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param s3_key: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3notificationfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_notification_filter_property = sam.CfnFunction.S3NotificationFilterProperty(
                    s3_key=sam.CfnFunction.S3KeyFilterProperty(
                        rules=[sam.CfnFunction.S3KeyFilterRuleProperty(
                            name="name",
                            value="value"
                        )]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__01d8e171e0b78d84acd020c613260bd3907f21f5febc160d00779177a8141c4d)
                check_type(argname="argument s3_key", value=s3_key, expected_type=type_hints["s3_key"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "s3_key": s3_key,
            }

        @builtins.property
        def s3_key(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnFunction.S3KeyFilterProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-s3notificationfilter.html#cfn-serverless-function-s3notificationfilter-s3key
            '''
            result = self._values.get("s3_key")
            assert result is not None, "Required property 's3_key' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFunction.S3KeyFilterProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3NotificationFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.SAMPolicyTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ami_describe_policy": "amiDescribePolicy",
            "aws_secrets_manager_get_secret_value_policy": "awsSecretsManagerGetSecretValuePolicy",
            "cloud_formation_describe_stacks_policy": "cloudFormationDescribeStacksPolicy",
            "cloud_watch_put_metric_policy": "cloudWatchPutMetricPolicy",
            "dynamo_db_crud_policy": "dynamoDbCrudPolicy",
            "dynamo_db_read_policy": "dynamoDbReadPolicy",
            "dynamo_db_stream_read_policy": "dynamoDbStreamReadPolicy",
            "dynamo_db_write_policy": "dynamoDbWritePolicy",
            "ec2_describe_policy": "ec2DescribePolicy",
            "elasticsearch_http_post_policy": "elasticsearchHttpPostPolicy",
            "filter_log_events_policy": "filterLogEventsPolicy",
            "kinesis_crud_policy": "kinesisCrudPolicy",
            "kinesis_stream_read_policy": "kinesisStreamReadPolicy",
            "kms_decrypt_policy": "kmsDecryptPolicy",
            "lambda_invoke_policy": "lambdaInvokePolicy",
            "rekognition_detect_only_policy": "rekognitionDetectOnlyPolicy",
            "rekognition_labels_policy": "rekognitionLabelsPolicy",
            "rekognition_no_data_access_policy": "rekognitionNoDataAccessPolicy",
            "rekognition_read_policy": "rekognitionReadPolicy",
            "rekognition_write_only_access_policy": "rekognitionWriteOnlyAccessPolicy",
            "s3_crud_policy": "s3CrudPolicy",
            "s3_read_policy": "s3ReadPolicy",
            "s3_write_policy": "s3WritePolicy",
            "ses_bulk_templated_crud_policy": "sesBulkTemplatedCrudPolicy",
            "ses_crud_policy": "sesCrudPolicy",
            "ses_email_template_crud_policy": "sesEmailTemplateCrudPolicy",
            "ses_send_bounce_policy": "sesSendBouncePolicy",
            "sns_crud_policy": "snsCrudPolicy",
            "sns_publish_message_policy": "snsPublishMessagePolicy",
            "sqs_poller_policy": "sqsPollerPolicy",
            "sqs_send_message_policy": "sqsSendMessagePolicy",
            "ssm_parameter_read_policy": "ssmParameterReadPolicy",
            "step_functions_execution_policy": "stepFunctionsExecutionPolicy",
            "vpc_access_policy": "vpcAccessPolicy",
        },
    )
    class SAMPolicyTemplateProperty:
        def __init__(
            self,
            *,
            ami_describe_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            aws_secrets_manager_get_secret_value_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.SecretArnSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_formation_describe_stacks_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cloud_watch_put_metric_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_db_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.TableSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_db_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.TableSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_db_stream_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.TableStreamSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            dynamo_db_write_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.TableSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ec2_describe_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            elasticsearch_http_post_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.DomainSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            filter_log_events_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.LogGroupSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.StreamSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kinesis_stream_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.StreamSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            kms_decrypt_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.KeySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_invoke_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.FunctionSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rekognition_detect_only_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rekognition_labels_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rekognition_no_data_access_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.CollectionSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rekognition_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.CollectionSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            rekognition_write_only_access_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.CollectionSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.BucketSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.BucketSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_write_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.BucketSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ses_bulk_templated_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.IdentitySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ses_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.IdentitySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ses_email_template_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ses_send_bounce_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.IdentitySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.TopicSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_publish_message_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.TopicSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs_poller_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.QueueSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sqs_send_message_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.QueueSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ssm_parameter_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.ParameterNameSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            step_functions_execution_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.StateMachineSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            vpc_access_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFunction.EmptySAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param ami_describe_policy: 
            :param aws_secrets_manager_get_secret_value_policy: 
            :param cloud_formation_describe_stacks_policy: 
            :param cloud_watch_put_metric_policy: 
            :param dynamo_db_crud_policy: 
            :param dynamo_db_read_policy: 
            :param dynamo_db_stream_read_policy: 
            :param dynamo_db_write_policy: 
            :param ec2_describe_policy: 
            :param elasticsearch_http_post_policy: 
            :param filter_log_events_policy: 
            :param kinesis_crud_policy: 
            :param kinesis_stream_read_policy: 
            :param kms_decrypt_policy: 
            :param lambda_invoke_policy: 
            :param rekognition_detect_only_policy: 
            :param rekognition_labels_policy: 
            :param rekognition_no_data_access_policy: 
            :param rekognition_read_policy: 
            :param rekognition_write_only_access_policy: 
            :param s3_crud_policy: 
            :param s3_read_policy: 
            :param s3_write_policy: 
            :param ses_bulk_templated_crud_policy: 
            :param ses_crud_policy: 
            :param ses_email_template_crud_policy: 
            :param ses_send_bounce_policy: 
            :param sns_crud_policy: 
            :param sns_publish_message_policy: 
            :param sqs_poller_policy: 
            :param sqs_send_message_policy: 
            :param ssm_parameter_read_policy: 
            :param step_functions_execution_policy: 
            :param vpc_access_policy: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s_aMPolicy_template_property = sam.CfnFunction.SAMPolicyTemplateProperty(
                    ami_describe_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    aws_secrets_manager_get_secret_value_policy=sam.CfnFunction.SecretArnSAMPTProperty(
                        secret_arn="secretArn"
                    ),
                    cloud_formation_describe_stacks_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    cloud_watch_put_metric_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    dynamo_db_crud_policy=sam.CfnFunction.TableSAMPTProperty(
                        table_name="tableName"
                    ),
                    dynamo_db_read_policy=sam.CfnFunction.TableSAMPTProperty(
                        table_name="tableName"
                    ),
                    dynamo_db_stream_read_policy=sam.CfnFunction.TableStreamSAMPTProperty(
                        stream_name="streamName",
                        table_name="tableName"
                    ),
                    dynamo_db_write_policy=sam.CfnFunction.TableSAMPTProperty(
                        table_name="tableName"
                    ),
                    ec2_describe_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    elasticsearch_http_post_policy=sam.CfnFunction.DomainSAMPTProperty(
                        domain_name="domainName"
                    ),
                    filter_log_events_policy=sam.CfnFunction.LogGroupSAMPTProperty(
                        log_group_name="logGroupName"
                    ),
                    kinesis_crud_policy=sam.CfnFunction.StreamSAMPTProperty(
                        stream_name="streamName"
                    ),
                    kinesis_stream_read_policy=sam.CfnFunction.StreamSAMPTProperty(
                        stream_name="streamName"
                    ),
                    kms_decrypt_policy=sam.CfnFunction.KeySAMPTProperty(
                        key_id="keyId"
                    ),
                    lambda_invoke_policy=sam.CfnFunction.FunctionSAMPTProperty(
                        function_name="functionName"
                    ),
                    rekognition_detect_only_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    rekognition_labels_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    rekognition_no_data_access_policy=sam.CfnFunction.CollectionSAMPTProperty(
                        collection_id="collectionId"
                    ),
                    rekognition_read_policy=sam.CfnFunction.CollectionSAMPTProperty(
                        collection_id="collectionId"
                    ),
                    rekognition_write_only_access_policy=sam.CfnFunction.CollectionSAMPTProperty(
                        collection_id="collectionId"
                    ),
                    s3_crud_policy=sam.CfnFunction.BucketSAMPTProperty(
                        bucket_name="bucketName"
                    ),
                    s3_read_policy=sam.CfnFunction.BucketSAMPTProperty(
                        bucket_name="bucketName"
                    ),
                    s3_write_policy=sam.CfnFunction.BucketSAMPTProperty(
                        bucket_name="bucketName"
                    ),
                    ses_bulk_templated_crud_policy=sam.CfnFunction.IdentitySAMPTProperty(
                        identity_name="identityName"
                    ),
                    ses_crud_policy=sam.CfnFunction.IdentitySAMPTProperty(
                        identity_name="identityName"
                    ),
                    ses_email_template_crud_policy=sam.CfnFunction.EmptySAMPTProperty(),
                    ses_send_bounce_policy=sam.CfnFunction.IdentitySAMPTProperty(
                        identity_name="identityName"
                    ),
                    sns_crud_policy=sam.CfnFunction.TopicSAMPTProperty(
                        topic_name="topicName"
                    ),
                    sns_publish_message_policy=sam.CfnFunction.TopicSAMPTProperty(
                        topic_name="topicName"
                    ),
                    sqs_poller_policy=sam.CfnFunction.QueueSAMPTProperty(
                        queue_name="queueName"
                    ),
                    sqs_send_message_policy=sam.CfnFunction.QueueSAMPTProperty(
                        queue_name="queueName"
                    ),
                    ssm_parameter_read_policy=sam.CfnFunction.ParameterNameSAMPTProperty(
                        parameter_name="parameterName"
                    ),
                    step_functions_execution_policy=sam.CfnFunction.StateMachineSAMPTProperty(
                        state_machine_name="stateMachineName"
                    ),
                    vpc_access_policy=sam.CfnFunction.EmptySAMPTProperty()
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ff6b7c5a716f70e2b1c660dcce5c7e1278abf95e639ec04dda55eeb73dab9900)
                check_type(argname="argument ami_describe_policy", value=ami_describe_policy, expected_type=type_hints["ami_describe_policy"])
                check_type(argname="argument aws_secrets_manager_get_secret_value_policy", value=aws_secrets_manager_get_secret_value_policy, expected_type=type_hints["aws_secrets_manager_get_secret_value_policy"])
                check_type(argname="argument cloud_formation_describe_stacks_policy", value=cloud_formation_describe_stacks_policy, expected_type=type_hints["cloud_formation_describe_stacks_policy"])
                check_type(argname="argument cloud_watch_put_metric_policy", value=cloud_watch_put_metric_policy, expected_type=type_hints["cloud_watch_put_metric_policy"])
                check_type(argname="argument dynamo_db_crud_policy", value=dynamo_db_crud_policy, expected_type=type_hints["dynamo_db_crud_policy"])
                check_type(argname="argument dynamo_db_read_policy", value=dynamo_db_read_policy, expected_type=type_hints["dynamo_db_read_policy"])
                check_type(argname="argument dynamo_db_stream_read_policy", value=dynamo_db_stream_read_policy, expected_type=type_hints["dynamo_db_stream_read_policy"])
                check_type(argname="argument dynamo_db_write_policy", value=dynamo_db_write_policy, expected_type=type_hints["dynamo_db_write_policy"])
                check_type(argname="argument ec2_describe_policy", value=ec2_describe_policy, expected_type=type_hints["ec2_describe_policy"])
                check_type(argname="argument elasticsearch_http_post_policy", value=elasticsearch_http_post_policy, expected_type=type_hints["elasticsearch_http_post_policy"])
                check_type(argname="argument filter_log_events_policy", value=filter_log_events_policy, expected_type=type_hints["filter_log_events_policy"])
                check_type(argname="argument kinesis_crud_policy", value=kinesis_crud_policy, expected_type=type_hints["kinesis_crud_policy"])
                check_type(argname="argument kinesis_stream_read_policy", value=kinesis_stream_read_policy, expected_type=type_hints["kinesis_stream_read_policy"])
                check_type(argname="argument kms_decrypt_policy", value=kms_decrypt_policy, expected_type=type_hints["kms_decrypt_policy"])
                check_type(argname="argument lambda_invoke_policy", value=lambda_invoke_policy, expected_type=type_hints["lambda_invoke_policy"])
                check_type(argname="argument rekognition_detect_only_policy", value=rekognition_detect_only_policy, expected_type=type_hints["rekognition_detect_only_policy"])
                check_type(argname="argument rekognition_labels_policy", value=rekognition_labels_policy, expected_type=type_hints["rekognition_labels_policy"])
                check_type(argname="argument rekognition_no_data_access_policy", value=rekognition_no_data_access_policy, expected_type=type_hints["rekognition_no_data_access_policy"])
                check_type(argname="argument rekognition_read_policy", value=rekognition_read_policy, expected_type=type_hints["rekognition_read_policy"])
                check_type(argname="argument rekognition_write_only_access_policy", value=rekognition_write_only_access_policy, expected_type=type_hints["rekognition_write_only_access_policy"])
                check_type(argname="argument s3_crud_policy", value=s3_crud_policy, expected_type=type_hints["s3_crud_policy"])
                check_type(argname="argument s3_read_policy", value=s3_read_policy, expected_type=type_hints["s3_read_policy"])
                check_type(argname="argument s3_write_policy", value=s3_write_policy, expected_type=type_hints["s3_write_policy"])
                check_type(argname="argument ses_bulk_templated_crud_policy", value=ses_bulk_templated_crud_policy, expected_type=type_hints["ses_bulk_templated_crud_policy"])
                check_type(argname="argument ses_crud_policy", value=ses_crud_policy, expected_type=type_hints["ses_crud_policy"])
                check_type(argname="argument ses_email_template_crud_policy", value=ses_email_template_crud_policy, expected_type=type_hints["ses_email_template_crud_policy"])
                check_type(argname="argument ses_send_bounce_policy", value=ses_send_bounce_policy, expected_type=type_hints["ses_send_bounce_policy"])
                check_type(argname="argument sns_crud_policy", value=sns_crud_policy, expected_type=type_hints["sns_crud_policy"])
                check_type(argname="argument sns_publish_message_policy", value=sns_publish_message_policy, expected_type=type_hints["sns_publish_message_policy"])
                check_type(argname="argument sqs_poller_policy", value=sqs_poller_policy, expected_type=type_hints["sqs_poller_policy"])
                check_type(argname="argument sqs_send_message_policy", value=sqs_send_message_policy, expected_type=type_hints["sqs_send_message_policy"])
                check_type(argname="argument ssm_parameter_read_policy", value=ssm_parameter_read_policy, expected_type=type_hints["ssm_parameter_read_policy"])
                check_type(argname="argument step_functions_execution_policy", value=step_functions_execution_policy, expected_type=type_hints["step_functions_execution_policy"])
                check_type(argname="argument vpc_access_policy", value=vpc_access_policy, expected_type=type_hints["vpc_access_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if ami_describe_policy is not None:
                self._values["ami_describe_policy"] = ami_describe_policy
            if aws_secrets_manager_get_secret_value_policy is not None:
                self._values["aws_secrets_manager_get_secret_value_policy"] = aws_secrets_manager_get_secret_value_policy
            if cloud_formation_describe_stacks_policy is not None:
                self._values["cloud_formation_describe_stacks_policy"] = cloud_formation_describe_stacks_policy
            if cloud_watch_put_metric_policy is not None:
                self._values["cloud_watch_put_metric_policy"] = cloud_watch_put_metric_policy
            if dynamo_db_crud_policy is not None:
                self._values["dynamo_db_crud_policy"] = dynamo_db_crud_policy
            if dynamo_db_read_policy is not None:
                self._values["dynamo_db_read_policy"] = dynamo_db_read_policy
            if dynamo_db_stream_read_policy is not None:
                self._values["dynamo_db_stream_read_policy"] = dynamo_db_stream_read_policy
            if dynamo_db_write_policy is not None:
                self._values["dynamo_db_write_policy"] = dynamo_db_write_policy
            if ec2_describe_policy is not None:
                self._values["ec2_describe_policy"] = ec2_describe_policy
            if elasticsearch_http_post_policy is not None:
                self._values["elasticsearch_http_post_policy"] = elasticsearch_http_post_policy
            if filter_log_events_policy is not None:
                self._values["filter_log_events_policy"] = filter_log_events_policy
            if kinesis_crud_policy is not None:
                self._values["kinesis_crud_policy"] = kinesis_crud_policy
            if kinesis_stream_read_policy is not None:
                self._values["kinesis_stream_read_policy"] = kinesis_stream_read_policy
            if kms_decrypt_policy is not None:
                self._values["kms_decrypt_policy"] = kms_decrypt_policy
            if lambda_invoke_policy is not None:
                self._values["lambda_invoke_policy"] = lambda_invoke_policy
            if rekognition_detect_only_policy is not None:
                self._values["rekognition_detect_only_policy"] = rekognition_detect_only_policy
            if rekognition_labels_policy is not None:
                self._values["rekognition_labels_policy"] = rekognition_labels_policy
            if rekognition_no_data_access_policy is not None:
                self._values["rekognition_no_data_access_policy"] = rekognition_no_data_access_policy
            if rekognition_read_policy is not None:
                self._values["rekognition_read_policy"] = rekognition_read_policy
            if rekognition_write_only_access_policy is not None:
                self._values["rekognition_write_only_access_policy"] = rekognition_write_only_access_policy
            if s3_crud_policy is not None:
                self._values["s3_crud_policy"] = s3_crud_policy
            if s3_read_policy is not None:
                self._values["s3_read_policy"] = s3_read_policy
            if s3_write_policy is not None:
                self._values["s3_write_policy"] = s3_write_policy
            if ses_bulk_templated_crud_policy is not None:
                self._values["ses_bulk_templated_crud_policy"] = ses_bulk_templated_crud_policy
            if ses_crud_policy is not None:
                self._values["ses_crud_policy"] = ses_crud_policy
            if ses_email_template_crud_policy is not None:
                self._values["ses_email_template_crud_policy"] = ses_email_template_crud_policy
            if ses_send_bounce_policy is not None:
                self._values["ses_send_bounce_policy"] = ses_send_bounce_policy
            if sns_crud_policy is not None:
                self._values["sns_crud_policy"] = sns_crud_policy
            if sns_publish_message_policy is not None:
                self._values["sns_publish_message_policy"] = sns_publish_message_policy
            if sqs_poller_policy is not None:
                self._values["sqs_poller_policy"] = sqs_poller_policy
            if sqs_send_message_policy is not None:
                self._values["sqs_send_message_policy"] = sqs_send_message_policy
            if ssm_parameter_read_policy is not None:
                self._values["ssm_parameter_read_policy"] = ssm_parameter_read_policy
            if step_functions_execution_policy is not None:
                self._values["step_functions_execution_policy"] = step_functions_execution_policy
            if vpc_access_policy is not None:
                self._values["vpc_access_policy"] = vpc_access_policy

        @builtins.property
        def ami_describe_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-amidescribepolicy
            '''
            result = self._values.get("ami_describe_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def aws_secrets_manager_get_secret_value_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.SecretArnSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-awssecretsmanagergetsecretvaluepolicy
            '''
            result = self._values.get("aws_secrets_manager_get_secret_value_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.SecretArnSAMPTProperty"]], result)

        @builtins.property
        def cloud_formation_describe_stacks_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-cloudformationdescribestackspolicy
            '''
            result = self._values.get("cloud_formation_describe_stacks_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def cloud_watch_put_metric_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-cloudwatchputmetricpolicy
            '''
            result = self._values.get("cloud_watch_put_metric_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def dynamo_db_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-dynamodbcrudpolicy
            '''
            result = self._values.get("dynamo_db_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableSAMPTProperty"]], result)

        @builtins.property
        def dynamo_db_read_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-dynamodbreadpolicy
            '''
            result = self._values.get("dynamo_db_read_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableSAMPTProperty"]], result)

        @builtins.property
        def dynamo_db_stream_read_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableStreamSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-dynamodbstreamreadpolicy
            '''
            result = self._values.get("dynamo_db_stream_read_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableStreamSAMPTProperty"]], result)

        @builtins.property
        def dynamo_db_write_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-dynamodbwritepolicy
            '''
            result = self._values.get("dynamo_db_write_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TableSAMPTProperty"]], result)

        @builtins.property
        def ec2_describe_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-ec2describepolicy
            '''
            result = self._values.get("ec2_describe_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def elasticsearch_http_post_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DomainSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-elasticsearchhttppostpolicy
            '''
            result = self._values.get("elasticsearch_http_post_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.DomainSAMPTProperty"]], result)

        @builtins.property
        def filter_log_events_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.LogGroupSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-filterlogeventspolicy
            '''
            result = self._values.get("filter_log_events_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.LogGroupSAMPTProperty"]], result)

        @builtins.property
        def kinesis_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.StreamSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-kinesiscrudpolicy
            '''
            result = self._values.get("kinesis_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.StreamSAMPTProperty"]], result)

        @builtins.property
        def kinesis_stream_read_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.StreamSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-kinesisstreamreadpolicy
            '''
            result = self._values.get("kinesis_stream_read_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.StreamSAMPTProperty"]], result)

        @builtins.property
        def kms_decrypt_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.KeySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-kmsdecryptpolicy
            '''
            result = self._values.get("kms_decrypt_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.KeySAMPTProperty"]], result)

        @builtins.property
        def lambda_invoke_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-lambdainvokepolicy
            '''
            result = self._values.get("lambda_invoke_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.FunctionSAMPTProperty"]], result)

        @builtins.property
        def rekognition_detect_only_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-rekognitiondetectonlypolicy
            '''
            result = self._values.get("rekognition_detect_only_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def rekognition_labels_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-rekognitionlabelspolicy
            '''
            result = self._values.get("rekognition_labels_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def rekognition_no_data_access_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.CollectionSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-rekognitionnodataaccesspolicy
            '''
            result = self._values.get("rekognition_no_data_access_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.CollectionSAMPTProperty"]], result)

        @builtins.property
        def rekognition_read_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.CollectionSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-rekognitionreadpolicy
            '''
            result = self._values.get("rekognition_read_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.CollectionSAMPTProperty"]], result)

        @builtins.property
        def rekognition_write_only_access_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.CollectionSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-rekognitionwriteonlyaccesspolicy
            '''
            result = self._values.get("rekognition_write_only_access_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.CollectionSAMPTProperty"]], result)

        @builtins.property
        def s3_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.BucketSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-s3crudpolicy
            '''
            result = self._values.get("s3_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.BucketSAMPTProperty"]], result)

        @builtins.property
        def s3_read_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.BucketSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-s3readpolicy
            '''
            result = self._values.get("s3_read_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.BucketSAMPTProperty"]], result)

        @builtins.property
        def s3_write_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.BucketSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-s3writepolicy
            '''
            result = self._values.get("s3_write_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.BucketSAMPTProperty"]], result)

        @builtins.property
        def ses_bulk_templated_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.IdentitySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-sesbulktemplatedcrudpolicy
            '''
            result = self._values.get("ses_bulk_templated_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.IdentitySAMPTProperty"]], result)

        @builtins.property
        def ses_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.IdentitySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-sescrudpolicy
            '''
            result = self._values.get("ses_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.IdentitySAMPTProperty"]], result)

        @builtins.property
        def ses_email_template_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-sesemailtemplatecrudpolicy
            '''
            result = self._values.get("ses_email_template_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        @builtins.property
        def ses_send_bounce_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.IdentitySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-sessendbouncepolicy
            '''
            result = self._values.get("ses_send_bounce_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.IdentitySAMPTProperty"]], result)

        @builtins.property
        def sns_crud_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TopicSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-snscrudpolicy
            '''
            result = self._values.get("sns_crud_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TopicSAMPTProperty"]], result)

        @builtins.property
        def sns_publish_message_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TopicSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-snspublishmessagepolicy
            '''
            result = self._values.get("sns_publish_message_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.TopicSAMPTProperty"]], result)

        @builtins.property
        def sqs_poller_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.QueueSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-sqspollerpolicy
            '''
            result = self._values.get("sqs_poller_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.QueueSAMPTProperty"]], result)

        @builtins.property
        def sqs_send_message_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.QueueSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-sqssendmessagepolicy
            '''
            result = self._values.get("sqs_send_message_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.QueueSAMPTProperty"]], result)

        @builtins.property
        def ssm_parameter_read_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ParameterNameSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-ssmparameterreadpolicy
            '''
            result = self._values.get("ssm_parameter_read_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.ParameterNameSAMPTProperty"]], result)

        @builtins.property
        def step_functions_execution_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.StateMachineSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-stepfunctionsexecutionpolicy
            '''
            result = self._values.get("step_functions_execution_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.StateMachineSAMPTProperty"]], result)

        @builtins.property
        def vpc_access_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sampolicytemplate.html#cfn-serverless-function-sampolicytemplate-vpcaccesspolicy
            '''
            result = self._values.get("vpc_access_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFunction.EmptySAMPTProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAMPolicyTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.SNSEventProperty",
        jsii_struct_bases=[],
        name_mapping={"topic": "topic"},
    )
    class SNSEventProperty:
        def __init__(self, *, topic: builtins.str) -> None:
            '''
            :param topic: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-snsevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s_nSEvent_property = sam.CfnFunction.SNSEventProperty(
                    topic="topic"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__355e23fa07290884140ffa4400be42ee2489af615d914e5dbc61418e2442fdb1)
                check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic": topic,
            }

        @builtins.property
        def topic(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-snsevent.html#cfn-serverless-function-snsevent-topic
            '''
            result = self._values.get("topic")
            assert result is not None, "Required property 'topic' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SNSEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.SQSEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "queue": "queue",
            "batch_size": "batchSize",
            "enabled": "enabled",
        },
    )
    class SQSEventProperty:
        def __init__(
            self,
            *,
            queue: builtins.str,
            batch_size: typing.Optional[jsii.Number] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param queue: 
            :param batch_size: 
            :param enabled: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sqsevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s_qSEvent_property = sam.CfnFunction.SQSEventProperty(
                    queue="queue",
                
                    # the properties below are optional
                    batch_size=123,
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be37486fa4f2ad612d19140f2fa9c114778a9568b98ab095bf59d0f490ebbf50)
                check_type(argname="argument queue", value=queue, expected_type=type_hints["queue"])
                check_type(argname="argument batch_size", value=batch_size, expected_type=type_hints["batch_size"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "queue": queue,
            }
            if batch_size is not None:
                self._values["batch_size"] = batch_size
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def queue(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sqsevent.html#cfn-serverless-function-sqsevent-queue
            '''
            result = self._values.get("queue")
            assert result is not None, "Required property 'queue' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def batch_size(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sqsevent.html#cfn-serverless-function-sqsevent-batchsize
            '''
            result = self._values.get("batch_size")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-sqsevent.html#cfn-serverless-function-sqsevent-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SQSEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.ScheduleEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "schedule": "schedule",
            "description": "description",
            "enabled": "enabled",
            "input": "input",
            "name": "name",
        },
    )
    class ScheduleEventProperty:
        def __init__(
            self,
            *,
            schedule: builtins.str,
            description: typing.Optional[builtins.str] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            input: typing.Optional[builtins.str] = None,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param schedule: 
            :param description: 
            :param enabled: 
            :param input: 
            :param name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-scheduleevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                schedule_event_property = sam.CfnFunction.ScheduleEventProperty(
                    schedule="schedule",
                
                    # the properties below are optional
                    description="description",
                    enabled=False,
                    input="input",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__63b58bf71ba62a34b17cdeb0700dc0b364f48f1ba42eb0303d2892d136a5646d)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule": schedule,
            }
            if description is not None:
                self._values["description"] = description
            if enabled is not None:
                self._values["enabled"] = enabled
            if input is not None:
                self._values["input"] = input
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def schedule(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-scheduleevent.html#cfn-serverless-function-scheduleevent-schedule
            '''
            result = self._values.get("schedule")
            assert result is not None, "Required property 'schedule' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-scheduleevent.html#cfn-serverless-function-scheduleevent-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-scheduleevent.html#cfn-serverless-function-scheduleevent-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-scheduleevent.html#cfn-serverless-function-scheduleevent-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-scheduleevent.html#cfn-serverless-function-scheduleevent-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.SecretArnSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"secret_arn": "secretArn"},
    )
    class SecretArnSAMPTProperty:
        def __init__(self, *, secret_arn: builtins.str) -> None:
            '''
            :param secret_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-secretarnsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                secret_arn_sAMPTProperty = sam.CfnFunction.SecretArnSAMPTProperty(
                    secret_arn="secretArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dc73d7367a2bd617be2d5ceeaf2320a43edae98c4dbb45f5f04715394f975ac9)
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "secret_arn": secret_arn,
            }

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-secretarnsampt.html#cfn-serverless-function-secretarnsampt-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SecretArnSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.StateMachineSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"state_machine_name": "stateMachineName"},
    )
    class StateMachineSAMPTProperty:
        def __init__(self, *, state_machine_name: builtins.str) -> None:
            '''
            :param state_machine_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-statemachinesampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                state_machine_sAMPTProperty = sam.CfnFunction.StateMachineSAMPTProperty(
                    state_machine_name="stateMachineName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__000e0ab9ec3a16a77064e3a41bdbbf9c89ce2137e298f69392fb7e13b45605d9)
                check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "state_machine_name": state_machine_name,
            }

        @builtins.property
        def state_machine_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-statemachinesampt.html#cfn-serverless-function-statemachinesampt-statemachinename
            '''
            result = self._values.get("state_machine_name")
            assert result is not None, "Required property 'state_machine_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateMachineSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.StreamSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_name": "streamName"},
    )
    class StreamSAMPTProperty:
        def __init__(self, *, stream_name: builtins.str) -> None:
            '''
            :param stream_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-streamsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                stream_sAMPTProperty = sam.CfnFunction.StreamSAMPTProperty(
                    stream_name="streamName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e84bbf253151430417441d85a9ba27164409cf10c9a4dc8bde343da7bad2804b)
                check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "stream_name": stream_name,
            }

        @builtins.property
        def stream_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-streamsampt.html#cfn-serverless-function-streamsampt-streamname
            '''
            result = self._values.get("stream_name")
            assert result is not None, "Required property 'stream_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StreamSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.TableSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"table_name": "tableName"},
    )
    class TableSAMPTProperty:
        def __init__(self, *, table_name: builtins.str) -> None:
            '''
            :param table_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-tablesampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                table_sAMPTProperty = sam.CfnFunction.TableSAMPTProperty(
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9b6f81630520c184d99ddebf05e101fb5f2f5d9dbf0765f6f86719cac31c0fa9)
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "table_name": table_name,
            }

        @builtins.property
        def table_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-tablesampt.html#cfn-serverless-function-tablesampt-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.TableStreamSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"stream_name": "streamName", "table_name": "tableName"},
    )
    class TableStreamSAMPTProperty:
        def __init__(
            self,
            *,
            stream_name: builtins.str,
            table_name: builtins.str,
        ) -> None:
            '''
            :param stream_name: 
            :param table_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-tablestreamsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                table_stream_sAMPTProperty = sam.CfnFunction.TableStreamSAMPTProperty(
                    stream_name="streamName",
                    table_name="tableName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33276c9d774d609586618c6f65f0d36451764e54646287ffc4e991358e24105e)
                check_type(argname="argument stream_name", value=stream_name, expected_type=type_hints["stream_name"])
                check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "stream_name": stream_name,
                "table_name": table_name,
            }

        @builtins.property
        def stream_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-tablestreamsampt.html#cfn-serverless-function-tablestreamsampt-streamname
            '''
            result = self._values.get("stream_name")
            assert result is not None, "Required property 'stream_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def table_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-tablestreamsampt.html#cfn-serverless-function-tablestreamsampt-tablename
            '''
            result = self._values.get("table_name")
            assert result is not None, "Required property 'table_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TableStreamSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.TopicSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_name": "topicName"},
    )
    class TopicSAMPTProperty:
        def __init__(self, *, topic_name: builtins.str) -> None:
            '''
            :param topic_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-topicsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                topic_sAMPTProperty = sam.CfnFunction.TopicSAMPTProperty(
                    topic_name="topicName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5ecb052268d71c7d0c161d9e3e08d937ebfc95358aef3ab88aaa379bea48a815)
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_name": topic_name,
            }

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-topicsampt.html#cfn-serverless-function-topicsampt-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TopicSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnFunction.VpcConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "security_group_ids": "securityGroupIds",
            "subnet_ids": "subnetIds",
        },
    )
    class VpcConfigProperty:
        def __init__(
            self,
            *,
            security_group_ids: typing.Sequence[builtins.str],
            subnet_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''
            :param security_group_ids: 
            :param subnet_ids: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-vpcconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                vpc_config_property = sam.CfnFunction.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4435eeff1c78c56e31a2a7233adfeb0466c2772d7ba3682a80039a306b4d45f1)
                check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
                check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "security_group_ids": security_group_ids,
                "subnet_ids": subnet_ids,
            }

        @builtins.property
        def security_group_ids(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-vpcconfig.html#cfn-serverless-function-vpcconfig-securitygroupids
            '''
            result = self._values.get("security_group_ids")
            assert result is not None, "Required property 'security_group_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def subnet_ids(self) -> typing.List[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-function-vpcconfig.html#cfn-serverless-function-vpcconfig-subnetids
            '''
            result = self._values.get("subnet_ids")
            assert result is not None, "Required property 'subnet_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnFunctionProps",
    jsii_struct_bases=[],
    name_mapping={
        "architectures": "architectures",
        "assume_role_policy_document": "assumeRolePolicyDocument",
        "auto_publish_alias": "autoPublishAlias",
        "auto_publish_code_sha256": "autoPublishCodeSha256",
        "code_signing_config_arn": "codeSigningConfigArn",
        "code_uri": "codeUri",
        "dead_letter_queue": "deadLetterQueue",
        "deployment_preference": "deploymentPreference",
        "description": "description",
        "environment": "environment",
        "ephemeral_storage": "ephemeralStorage",
        "event_invoke_config": "eventInvokeConfig",
        "events": "events",
        "file_system_configs": "fileSystemConfigs",
        "function_name": "functionName",
        "function_url_config": "functionUrlConfig",
        "handler": "handler",
        "image_config": "imageConfig",
        "image_uri": "imageUri",
        "inline_code": "inlineCode",
        "kms_key_arn": "kmsKeyArn",
        "layers": "layers",
        "memory_size": "memorySize",
        "package_type": "packageType",
        "permissions_boundary": "permissionsBoundary",
        "policies": "policies",
        "provisioned_concurrency_config": "provisionedConcurrencyConfig",
        "reserved_concurrent_executions": "reservedConcurrentExecutions",
        "role": "role",
        "runtime": "runtime",
        "tags": "tags",
        "timeout": "timeout",
        "tracing": "tracing",
        "version_description": "versionDescription",
        "vpc_config": "vpcConfig",
    },
)
class CfnFunctionProps:
    def __init__(
        self,
        *,
        architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
        assume_role_policy_document: typing.Any = None,
        auto_publish_alias: typing.Optional[builtins.str] = None,
        auto_publish_code_sha256: typing.Optional[builtins.str] = None,
        code_signing_config_arn: typing.Optional[builtins.str] = None,
        code_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dead_letter_queue: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DeadLetterQueueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DeploymentPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EphemeralStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        event_invoke_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventInvokeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        file_system_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FileSystemConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        function_name: typing.Optional[builtins.str] = None,
        function_url_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionUrlConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        handler: typing.Optional[builtins.str] = None,
        image_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ImageConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        image_uri: typing.Optional[builtins.str] = None,
        inline_code: typing.Optional[builtins.str] = None,
        kms_key_arn: typing.Optional[builtins.str] = None,
        layers: typing.Optional[typing.Sequence[builtins.str]] = None,
        memory_size: typing.Optional[jsii.Number] = None,
        package_type: typing.Optional[builtins.str] = None,
        permissions_boundary: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.SAMPolicyTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        provisioned_concurrency_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ProvisionedConcurrencyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
        role: typing.Optional[builtins.str] = None,
        runtime: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        timeout: typing.Optional[jsii.Number] = None,
        tracing: typing.Optional[builtins.str] = None,
        version_description: typing.Optional[builtins.str] = None,
        vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFunction``.

        :param architectures: 
        :param assume_role_policy_document: 
        :param auto_publish_alias: 
        :param auto_publish_code_sha256: 
        :param code_signing_config_arn: 
        :param code_uri: 
        :param dead_letter_queue: 
        :param deployment_preference: 
        :param description: 
        :param environment: 
        :param ephemeral_storage: 
        :param event_invoke_config: 
        :param events: 
        :param file_system_configs: 
        :param function_name: 
        :param function_url_config: 
        :param handler: 
        :param image_config: 
        :param image_uri: 
        :param inline_code: 
        :param kms_key_arn: 
        :param layers: 
        :param memory_size: 
        :param package_type: 
        :param permissions_boundary: 
        :param policies: 
        :param provisioned_concurrency_config: 
        :param reserved_concurrent_executions: 
        :param role: 
        :param runtime: 
        :param tags: 
        :param timeout: 
        :param tracing: 
        :param version_description: 
        :param vpc_config: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            # assume_role_policy_document: Any
            
            cfn_function_props = sam.CfnFunctionProps(
                architectures=["architectures"],
                assume_role_policy_document=assume_role_policy_document,
                auto_publish_alias="autoPublishAlias",
                auto_publish_code_sha256="autoPublishCodeSha256",
                code_signing_config_arn="codeSigningConfigArn",
                code_uri="codeUri",
                dead_letter_queue=sam.CfnFunction.DeadLetterQueueProperty(
                    target_arn="targetArn",
                    type="type"
                ),
                deployment_preference=sam.CfnFunction.DeploymentPreferenceProperty(
                    alarms=["alarms"],
                    enabled=False,
                    hooks=sam.CfnFunction.HooksProperty(
                        post_traffic="postTraffic",
                        pre_traffic="preTraffic"
                    ),
                    role="role",
                    type="type"
                ),
                description="description",
                environment=sam.CfnFunction.FunctionEnvironmentProperty(
                    variables={
                        "variables_key": "variables"
                    }
                ),
                ephemeral_storage=sam.CfnFunction.EphemeralStorageProperty(
                    size=123
                ),
                event_invoke_config=sam.CfnFunction.EventInvokeConfigProperty(
                    destination_config=sam.CfnFunction.EventInvokeDestinationConfigProperty(
                        on_failure=sam.CfnFunction.DestinationProperty(
                            destination="destination",
            
                            # the properties below are optional
                            type="type"
                        ),
                        on_success=sam.CfnFunction.DestinationProperty(
                            destination="destination",
            
                            # the properties below are optional
                            type="type"
                        )
                    ),
                    maximum_event_age_in_seconds=123,
                    maximum_retry_attempts=123
                ),
                events={
                    "events_key": sam.CfnFunction.EventSourceProperty(
                        properties=sam.CfnFunction.AlexaSkillEventProperty(
                            skill_id="skillId"
                        ),
                        type="type"
                    )
                },
                file_system_configs=[sam.CfnFunction.FileSystemConfigProperty(
                    arn="arn",
                    local_mount_path="localMountPath"
                )],
                function_name="functionName",
                function_url_config=sam.CfnFunction.FunctionUrlConfigProperty(
                    auth_type="authType",
            
                    # the properties below are optional
                    cors="cors",
                    invoke_mode="invokeMode"
                ),
                handler="handler",
                image_config=sam.CfnFunction.ImageConfigProperty(
                    command=["command"],
                    entry_point=["entryPoint"],
                    working_directory="workingDirectory"
                ),
                image_uri="imageUri",
                inline_code="inlineCode",
                kms_key_arn="kmsKeyArn",
                layers=["layers"],
                memory_size=123,
                package_type="packageType",
                permissions_boundary="permissionsBoundary",
                policies="policies",
                provisioned_concurrency_config=sam.CfnFunction.ProvisionedConcurrencyConfigProperty(
                    provisioned_concurrent_executions="provisionedConcurrentExecutions"
                ),
                reserved_concurrent_executions=123,
                role="role",
                runtime="runtime",
                tags={
                    "tags_key": "tags"
                },
                timeout=123,
                tracing="tracing",
                version_description="versionDescription",
                vpc_config=sam.CfnFunction.VpcConfigProperty(
                    security_group_ids=["securityGroupIds"],
                    subnet_ids=["subnetIds"]
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d36d7a3f5429a8550f324d9ddc7ca791a504b5e17ff50b124622826fe13b568b)
            check_type(argname="argument architectures", value=architectures, expected_type=type_hints["architectures"])
            check_type(argname="argument assume_role_policy_document", value=assume_role_policy_document, expected_type=type_hints["assume_role_policy_document"])
            check_type(argname="argument auto_publish_alias", value=auto_publish_alias, expected_type=type_hints["auto_publish_alias"])
            check_type(argname="argument auto_publish_code_sha256", value=auto_publish_code_sha256, expected_type=type_hints["auto_publish_code_sha256"])
            check_type(argname="argument code_signing_config_arn", value=code_signing_config_arn, expected_type=type_hints["code_signing_config_arn"])
            check_type(argname="argument code_uri", value=code_uri, expected_type=type_hints["code_uri"])
            check_type(argname="argument dead_letter_queue", value=dead_letter_queue, expected_type=type_hints["dead_letter_queue"])
            check_type(argname="argument deployment_preference", value=deployment_preference, expected_type=type_hints["deployment_preference"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument environment", value=environment, expected_type=type_hints["environment"])
            check_type(argname="argument ephemeral_storage", value=ephemeral_storage, expected_type=type_hints["ephemeral_storage"])
            check_type(argname="argument event_invoke_config", value=event_invoke_config, expected_type=type_hints["event_invoke_config"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument file_system_configs", value=file_system_configs, expected_type=type_hints["file_system_configs"])
            check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            check_type(argname="argument function_url_config", value=function_url_config, expected_type=type_hints["function_url_config"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
            check_type(argname="argument image_config", value=image_config, expected_type=type_hints["image_config"])
            check_type(argname="argument image_uri", value=image_uri, expected_type=type_hints["image_uri"])
            check_type(argname="argument inline_code", value=inline_code, expected_type=type_hints["inline_code"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument layers", value=layers, expected_type=type_hints["layers"])
            check_type(argname="argument memory_size", value=memory_size, expected_type=type_hints["memory_size"])
            check_type(argname="argument package_type", value=package_type, expected_type=type_hints["package_type"])
            check_type(argname="argument permissions_boundary", value=permissions_boundary, expected_type=type_hints["permissions_boundary"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument provisioned_concurrency_config", value=provisioned_concurrency_config, expected_type=type_hints["provisioned_concurrency_config"])
            check_type(argname="argument reserved_concurrent_executions", value=reserved_concurrent_executions, expected_type=type_hints["reserved_concurrent_executions"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument runtime", value=runtime, expected_type=type_hints["runtime"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument version_description", value=version_description, expected_type=type_hints["version_description"])
            check_type(argname="argument vpc_config", value=vpc_config, expected_type=type_hints["vpc_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if architectures is not None:
            self._values["architectures"] = architectures
        if assume_role_policy_document is not None:
            self._values["assume_role_policy_document"] = assume_role_policy_document
        if auto_publish_alias is not None:
            self._values["auto_publish_alias"] = auto_publish_alias
        if auto_publish_code_sha256 is not None:
            self._values["auto_publish_code_sha256"] = auto_publish_code_sha256
        if code_signing_config_arn is not None:
            self._values["code_signing_config_arn"] = code_signing_config_arn
        if code_uri is not None:
            self._values["code_uri"] = code_uri
        if dead_letter_queue is not None:
            self._values["dead_letter_queue"] = dead_letter_queue
        if deployment_preference is not None:
            self._values["deployment_preference"] = deployment_preference
        if description is not None:
            self._values["description"] = description
        if environment is not None:
            self._values["environment"] = environment
        if ephemeral_storage is not None:
            self._values["ephemeral_storage"] = ephemeral_storage
        if event_invoke_config is not None:
            self._values["event_invoke_config"] = event_invoke_config
        if events is not None:
            self._values["events"] = events
        if file_system_configs is not None:
            self._values["file_system_configs"] = file_system_configs
        if function_name is not None:
            self._values["function_name"] = function_name
        if function_url_config is not None:
            self._values["function_url_config"] = function_url_config
        if handler is not None:
            self._values["handler"] = handler
        if image_config is not None:
            self._values["image_config"] = image_config
        if image_uri is not None:
            self._values["image_uri"] = image_uri
        if inline_code is not None:
            self._values["inline_code"] = inline_code
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if layers is not None:
            self._values["layers"] = layers
        if memory_size is not None:
            self._values["memory_size"] = memory_size
        if package_type is not None:
            self._values["package_type"] = package_type
        if permissions_boundary is not None:
            self._values["permissions_boundary"] = permissions_boundary
        if policies is not None:
            self._values["policies"] = policies
        if provisioned_concurrency_config is not None:
            self._values["provisioned_concurrency_config"] = provisioned_concurrency_config
        if reserved_concurrent_executions is not None:
            self._values["reserved_concurrent_executions"] = reserved_concurrent_executions
        if role is not None:
            self._values["role"] = role
        if runtime is not None:
            self._values["runtime"] = runtime
        if tags is not None:
            self._values["tags"] = tags
        if timeout is not None:
            self._values["timeout"] = timeout
        if tracing is not None:
            self._values["tracing"] = tracing
        if version_description is not None:
            self._values["version_description"] = version_description
        if vpc_config is not None:
            self._values["vpc_config"] = vpc_config

    @builtins.property
    def architectures(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-architectures
        '''
        result = self._values.get("architectures")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def assume_role_policy_document(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-assumerolepolicydocument
        '''
        result = self._values.get("assume_role_policy_document")
        return typing.cast(typing.Any, result)

    @builtins.property
    def auto_publish_alias(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-autopublishalias
        '''
        result = self._values.get("auto_publish_alias")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_publish_code_sha256(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-autopublishcodesha256
        '''
        result = self._values.get("auto_publish_code_sha256")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_signing_config_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-codesigningconfigarn
        '''
        result = self._values.get("code_signing_config_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def code_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.S3LocationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-codeuri
        '''
        result = self._values.get("code_uri")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.S3LocationProperty]], result)

    @builtins.property
    def dead_letter_queue(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.DeadLetterQueueProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-deadletterqueue
        '''
        result = self._values.get("dead_letter_queue")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.DeadLetterQueueProperty]], result)

    @builtins.property
    def deployment_preference(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.DeploymentPreferenceProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-deploymentpreference
        '''
        result = self._values.get("deployment_preference")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.DeploymentPreferenceProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def environment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.FunctionEnvironmentProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-environment
        '''
        result = self._values.get("environment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.FunctionEnvironmentProperty]], result)

    @builtins.property
    def ephemeral_storage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.EphemeralStorageProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-ephemeralstorage
        '''
        result = self._values.get("ephemeral_storage")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.EphemeralStorageProperty]], result)

    @builtins.property
    def event_invoke_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.EventInvokeConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-eventinvokeconfig
        '''
        result = self._values.get("event_invoke_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.EventInvokeConfigProperty]], result)

    @builtins.property
    def events(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnFunction.EventSourceProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-events
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnFunction.EventSourceProperty]]]], result)

    @builtins.property
    def file_system_configs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFunction.FileSystemConfigProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-filesystemconfigs
        '''
        result = self._values.get("file_system_configs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFunction.FileSystemConfigProperty]]]], result)

    @builtins.property
    def function_name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-functionname
        '''
        result = self._values.get("function_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def function_url_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.FunctionUrlConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-functionurlconfig
        '''
        result = self._values.get("function_url_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.FunctionUrlConfigProperty]], result)

    @builtins.property
    def handler(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-handler
        '''
        result = self._values.get("handler")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def image_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.ImageConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-imageconfig
        '''
        result = self._values.get("image_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.ImageConfigProperty]], result)

    @builtins.property
    def image_uri(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-imageuri
        '''
        result = self._values.get("image_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def inline_code(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-inlinecode
        '''
        result = self._values.get("inline_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def layers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-layers
        '''
        result = self._values.get("layers")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def memory_size(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-memorysize
        '''
        result = self._values.get("memory_size")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def package_type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-packagetype
        '''
        result = self._values.get("package_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundary(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-permissionsboundary
        '''
        result = self._values.get("permissions_boundary")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.IAMPolicyDocumentProperty, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.IAMPolicyDocumentProperty, CfnFunction.SAMPolicyTemplateProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.IAMPolicyDocumentProperty, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.IAMPolicyDocumentProperty, CfnFunction.SAMPolicyTemplateProperty]]]], result)

    @builtins.property
    def provisioned_concurrency_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.ProvisionedConcurrencyConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-provisionedconcurrencyconfig
        '''
        result = self._values.get("provisioned_concurrency_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.ProvisionedConcurrencyConfigProperty]], result)

    @builtins.property
    def reserved_concurrent_executions(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-reservedconcurrentexecutions
        '''
        result = self._values.get("reserved_concurrent_executions")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-runtime
        '''
        result = self._values.get("runtime")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def timeout(self) -> typing.Optional[jsii.Number]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-timeout
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tracing(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-tracing
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version_description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-versiondescription
        '''
        result = self._values.get("version_description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.VpcConfigProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-function.html#cfn-serverless-function-vpcconfig
        '''
        result = self._values.get("vpc_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.VpcConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFunctionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnHttpApi(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi",
):
    '''https://github.com/aws/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesshttpapi.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html
    :cloudformationResource: AWS::Serverless::HttpApi
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        # authorizers: Any
        # definition_body: Any
        
        cfn_http_api = sam.CfnHttpApi(self, "MyCfnHttpApi",
            access_log_setting=sam.CfnHttpApi.AccessLogSettingProperty(
                destination_arn="destinationArn",
                format="format"
            ),
            auth=sam.CfnHttpApi.HttpApiAuthProperty(
                authorizers=authorizers,
                default_authorizer="defaultAuthorizer"
            ),
            cors_configuration=False,
            default_route_settings=sam.CfnHttpApi.RouteSettingsProperty(
                data_trace_enabled=False,
                detailed_metrics_enabled=False,
                logging_level="loggingLevel",
                throttling_burst_limit=123,
                throttling_rate_limit=123
            ),
            definition_body=definition_body,
            definition_uri="definitionUri",
            description="description",
            disable_execute_api_endpoint=False,
            domain=sam.CfnHttpApi.HttpApiDomainConfigurationProperty(
                certificate_arn="certificateArn",
                domain_name="domainName",
        
                # the properties below are optional
                base_path="basePath",
                endpoint_configuration="endpointConfiguration",
                mutual_tls_authentication=sam.CfnHttpApi.MutualTlsAuthenticationProperty(
                    truststore_uri="truststoreUri",
                    truststore_version=False
                ),
                route53=sam.CfnHttpApi.Route53ConfigurationProperty(
                    distributed_domain_name="distributedDomainName",
                    evaluate_target_health=False,
                    hosted_zone_id="hostedZoneId",
                    hosted_zone_name="hostedZoneName",
                    ip_v6=False
                ),
                security_policy="securityPolicy"
            ),
            fail_on_warnings=False,
            route_settings=sam.CfnHttpApi.RouteSettingsProperty(
                data_trace_enabled=False,
                detailed_metrics_enabled=False,
                logging_level="loggingLevel",
                throttling_burst_limit=123,
                throttling_rate_limit=123
            ),
            stage_name="stageName",
            stage_variables={
                "stage_variables_key": "stageVariables"
            },
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.AccessLogSettingProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.HttpApiAuthProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cors_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, typing.Union["CfnHttpApi.CorsConfigurationObjectProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.RouteSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_body: typing.Any = None,
        definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnHttpApi.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.HttpApiDomainConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.RouteSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        stage_name: typing.Optional[builtins.str] = None,
        stage_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param access_log_setting: 
        :param auth: 
        :param cors_configuration: 
        :param default_route_settings: 
        :param definition_body: 
        :param definition_uri: 
        :param description: 
        :param disable_execute_api_endpoint: 
        :param domain: 
        :param fail_on_warnings: 
        :param route_settings: 
        :param stage_name: 
        :param stage_variables: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2810a638ba3e7320fe893fabc5f6e87ff6c30d560aa983c6a0d6c0f8bf36db24)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHttpApiProps(
            access_log_setting=access_log_setting,
            auth=auth,
            cors_configuration=cors_configuration,
            default_route_settings=default_route_settings,
            definition_body=definition_body,
            definition_uri=definition_uri,
            description=description,
            disable_execute_api_endpoint=disable_execute_api_endpoint,
            domain=domain,
            fail_on_warnings=fail_on_warnings,
            route_settings=route_settings,
            stage_name=stage_name,
            stage_variables=stage_variables,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4f3553a6c850079b893b4af3eba9a2e875d8f7a2f7810fc1d60e2664a2a3bb7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__e64eb42bd5b3ff30eb1371e2bbc5bf92a3972db3b40c6c801031d7f11537292a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

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
    @jsii.member(jsii_name="accessLogSetting")
    def access_log_setting(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.AccessLogSettingProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.AccessLogSettingProperty"]], jsii.get(self, "accessLogSetting"))

    @access_log_setting.setter
    def access_log_setting(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.AccessLogSettingProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a42a2744dc641266e3d37b5f146f6af992595ec5ba766b45574ea243aa6fc44)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLogSetting", value)

    @builtins.property
    @jsii.member(jsii_name="auth")
    def auth(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.HttpApiAuthProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.HttpApiAuthProperty"]], jsii.get(self, "auth"))

    @auth.setter
    def auth(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.HttpApiAuthProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d554bf4285c5e79b485d5399187d984c4db50ac590f443a59fab5686f8a5f98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "auth", value)

    @builtins.property
    @jsii.member(jsii_name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, "CfnHttpApi.CorsConfigurationObjectProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, "CfnHttpApi.CorsConfigurationObjectProperty"]], jsii.get(self, "corsConfiguration"))

    @cors_configuration.setter
    def cors_configuration(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, "CfnHttpApi.CorsConfigurationObjectProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d80d30c6061e0bc43c731aed2d30d2e16c6817cc38f17f6e31e265dcb4ace5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "corsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRouteSettings")
    def default_route_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.RouteSettingsProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.RouteSettingsProperty"]], jsii.get(self, "defaultRouteSettings"))

    @default_route_settings.setter
    def default_route_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.RouteSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c79a8422ac135ae14261211b8dbc3a6cff2c1cd4dfd873119c1ea5a819c7f35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRouteSettings", value)

    @builtins.property
    @jsii.member(jsii_name="definitionBody")
    def definition_body(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "definitionBody"))

    @definition_body.setter
    def definition_body(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64a7cbe0232a4687fbe5d51da21fce7dd6fa5366be5dc78ecebd805606154fa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionBody", value)

    @builtins.property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnHttpApi.S3LocationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnHttpApi.S3LocationProperty"]], jsii.get(self, "definitionUri"))

    @definition_uri.setter
    def definition_uri(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnHttpApi.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad95de74fe527265b62ef85880e9cbbac95b824a1f02495ff12728a9388bcb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionUri", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2eaf9aeb8e4a3d3f2c267ba77886e61932ef901479c7475a9c8aea00f009a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableExecuteApiEndpoint"))

    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35d352404c375b1dfad345ab43624def545633ffca3918ffbb28046ee14d7978)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableExecuteApiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="domain")
    def domain(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.HttpApiDomainConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.HttpApiDomainConfigurationProperty"]], jsii.get(self, "domain"))

    @domain.setter
    def domain(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.HttpApiDomainConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e942057fdfda6966ac2fede8944ab9cb3e8bf62cbe0e8dd26293e1004dbebbc4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domain", value)

    @builtins.property
    @jsii.member(jsii_name="failOnWarnings")
    def fail_on_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "failOnWarnings"))

    @fail_on_warnings.setter
    def fail_on_warnings(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2409f872afa25b367ac77a9bf7ff8c646989e8ed593046716279b7f551051e90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="routeSettings")
    def route_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.RouteSettingsProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.RouteSettingsProperty"]], jsii.get(self, "routeSettings"))

    @route_settings.setter
    def route_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.RouteSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5197dd6c00fdbddd6b9b3cd699f235d4b1e49fe164b78213b9c4731c95d89470)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeSettings", value)

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageName"))

    @stage_name.setter
    def stage_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__690006efe3a8bbd86d333485a6f43ce5a5088b2ade6688f66fa4ed3f2910fd7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageName", value)

    @builtins.property
    @jsii.member(jsii_name="stageVariables")
    def stage_variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "stageVariables"))

    @stage_variables.setter
    def stage_variables(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__449af0a02d8005f7a293a627e1cb45ddbc2347c0cd6d00355c6149e405bd71de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageVariables", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e1532eb045406e1f0c887e9f0288aa942ba65703b7281fd270e9ce1d05639ac2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.AccessLogSettingProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn", "format": "format"},
    )
    class AccessLogSettingProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param destination_arn: 
            :param format: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-accesslogsetting.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                access_log_setting_property = sam.CfnHttpApi.AccessLogSettingProperty(
                    destination_arn="destinationArn",
                    format="format"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__396e25c7a235a0fd1fc98c660894c2403ae81136868a6928b6ac54684b38aba2)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn
            if format is not None:
                self._values["format"] = format

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-accesslogsetting.html#cfn-serverless-httpapi-accesslogsetting-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-accesslogsetting.html#cfn-serverless-httpapi-accesslogsetting-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessLogSettingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.CorsConfigurationObjectProperty",
        jsii_struct_bases=[],
        name_mapping={
            "allow_credentials": "allowCredentials",
            "allow_headers": "allowHeaders",
            "allow_methods": "allowMethods",
            "allow_origins": "allowOrigins",
            "expose_headers": "exposeHeaders",
            "max_age": "maxAge",
        },
    )
    class CorsConfigurationObjectProperty:
        def __init__(
            self,
            *,
            allow_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
            allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
            allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
            expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
            max_age: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param allow_credentials: 
            :param allow_headers: 
            :param allow_methods: 
            :param allow_origins: 
            :param expose_headers: 
            :param max_age: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                cors_configuration_object_property = sam.CfnHttpApi.CorsConfigurationObjectProperty(
                    allow_credentials=False,
                    allow_headers=["allowHeaders"],
                    allow_methods=["allowMethods"],
                    allow_origins=["allowOrigins"],
                    expose_headers=["exposeHeaders"],
                    max_age=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__92ebf64195227f64e22824cc3c2e16b820997afaf22279f214e4be9d2e5aeef7)
                check_type(argname="argument allow_credentials", value=allow_credentials, expected_type=type_hints["allow_credentials"])
                check_type(argname="argument allow_headers", value=allow_headers, expected_type=type_hints["allow_headers"])
                check_type(argname="argument allow_methods", value=allow_methods, expected_type=type_hints["allow_methods"])
                check_type(argname="argument allow_origins", value=allow_origins, expected_type=type_hints["allow_origins"])
                check_type(argname="argument expose_headers", value=expose_headers, expected_type=type_hints["expose_headers"])
                check_type(argname="argument max_age", value=max_age, expected_type=type_hints["max_age"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if allow_credentials is not None:
                self._values["allow_credentials"] = allow_credentials
            if allow_headers is not None:
                self._values["allow_headers"] = allow_headers
            if allow_methods is not None:
                self._values["allow_methods"] = allow_methods
            if allow_origins is not None:
                self._values["allow_origins"] = allow_origins
            if expose_headers is not None:
                self._values["expose_headers"] = expose_headers
            if max_age is not None:
                self._values["max_age"] = max_age

        @builtins.property
        def allow_credentials(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html#cfn-serverless-httpapi-corsconfigurationobject-allowcredentials
            '''
            result = self._values.get("allow_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html#cfn-serverless-httpapi-corsconfigurationobject-allowheaders
            '''
            result = self._values.get("allow_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html#cfn-serverless-httpapi-corsconfigurationobject-allowmethods
            '''
            result = self._values.get("allow_methods")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allow_origins(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html#cfn-serverless-httpapi-corsconfigurationobject-alloworigins
            '''
            result = self._values.get("allow_origins")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html#cfn-serverless-httpapi-corsconfigurationobject-exposeheaders
            '''
            result = self._values.get("expose_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def max_age(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-corsconfigurationobject.html#cfn-serverless-httpapi-corsconfigurationobject-maxage
            '''
            result = self._values.get("max_age")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CorsConfigurationObjectProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.HttpApiAuthProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorizers": "authorizers",
            "default_authorizer": "defaultAuthorizer",
        },
    )
    class HttpApiAuthProperty:
        def __init__(
            self,
            *,
            authorizers: typing.Any = None,
            default_authorizer: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param authorizers: 
            :param default_authorizer: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapiauth.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # authorizers: Any
                
                http_api_auth_property = sam.CfnHttpApi.HttpApiAuthProperty(
                    authorizers=authorizers,
                    default_authorizer="defaultAuthorizer"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1ac54b5b9b26f08c57fcf9efe33403e1ea8d4e4dbeb2436611dccb3a0e037587)
                check_type(argname="argument authorizers", value=authorizers, expected_type=type_hints["authorizers"])
                check_type(argname="argument default_authorizer", value=default_authorizer, expected_type=type_hints["default_authorizer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorizers is not None:
                self._values["authorizers"] = authorizers
            if default_authorizer is not None:
                self._values["default_authorizer"] = default_authorizer

        @builtins.property
        def authorizers(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapiauth.html#cfn-serverless-httpapi-httpapiauth-authorizers
            '''
            result = self._values.get("authorizers")
            return typing.cast(typing.Any, result)

        @builtins.property
        def default_authorizer(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapiauth.html#cfn-serverless-httpapi-httpapiauth-defaultauthorizer
            '''
            result = self._values.get("default_authorizer")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpApiAuthProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.HttpApiDomainConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "domain_name": "domainName",
            "base_path": "basePath",
            "endpoint_configuration": "endpointConfiguration",
            "mutual_tls_authentication": "mutualTlsAuthentication",
            "route53": "route53",
            "security_policy": "securityPolicy",
        },
    )
    class HttpApiDomainConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_arn: builtins.str,
            domain_name: builtins.str,
            base_path: typing.Optional[builtins.str] = None,
            endpoint_configuration: typing.Optional[builtins.str] = None,
            mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.MutualTlsAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            route53: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHttpApi.Route53ConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            security_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param certificate_arn: 
            :param domain_name: 
            :param base_path: 
            :param endpoint_configuration: 
            :param mutual_tls_authentication: 
            :param route53: 
            :param security_policy: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                http_api_domain_configuration_property = sam.CfnHttpApi.HttpApiDomainConfigurationProperty(
                    certificate_arn="certificateArn",
                    domain_name="domainName",
                
                    # the properties below are optional
                    base_path="basePath",
                    endpoint_configuration="endpointConfiguration",
                    mutual_tls_authentication=sam.CfnHttpApi.MutualTlsAuthenticationProperty(
                        truststore_uri="truststoreUri",
                        truststore_version=False
                    ),
                    route53=sam.CfnHttpApi.Route53ConfigurationProperty(
                        distributed_domain_name="distributedDomainName",
                        evaluate_target_health=False,
                        hosted_zone_id="hostedZoneId",
                        hosted_zone_name="hostedZoneName",
                        ip_v6=False
                    ),
                    security_policy="securityPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__668063eec4c8cd3e6e97d6a394cfeabd05caf1022045642b40cdb7058f97c736)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument base_path", value=base_path, expected_type=type_hints["base_path"])
                check_type(argname="argument endpoint_configuration", value=endpoint_configuration, expected_type=type_hints["endpoint_configuration"])
                check_type(argname="argument mutual_tls_authentication", value=mutual_tls_authentication, expected_type=type_hints["mutual_tls_authentication"])
                check_type(argname="argument route53", value=route53, expected_type=type_hints["route53"])
                check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "certificate_arn": certificate_arn,
                "domain_name": domain_name,
            }
            if base_path is not None:
                self._values["base_path"] = base_path
            if endpoint_configuration is not None:
                self._values["endpoint_configuration"] = endpoint_configuration
            if mutual_tls_authentication is not None:
                self._values["mutual_tls_authentication"] = mutual_tls_authentication
            if route53 is not None:
                self._values["route53"] = route53
            if security_policy is not None:
                self._values["security_policy"] = security_policy

        @builtins.property
        def certificate_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-certificatearn
            '''
            result = self._values.get("certificate_arn")
            assert result is not None, "Required property 'certificate_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def domain_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-domainname
            '''
            result = self._values.get("domain_name")
            assert result is not None, "Required property 'domain_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def base_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-basepath
            '''
            result = self._values.get("base_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint_configuration(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-endpointconfiguration
            '''
            result = self._values.get("endpoint_configuration")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mutual_tls_authentication(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.MutualTlsAuthenticationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-mutualtlsauthentication
            '''
            result = self._values.get("mutual_tls_authentication")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.MutualTlsAuthenticationProperty"]], result)

        @builtins.property
        def route53(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.Route53ConfigurationProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-route53
            '''
            result = self._values.get("route53")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHttpApi.Route53ConfigurationProperty"]], result)

        @builtins.property
        def security_policy(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-httpapidomainconfiguration.html#cfn-serverless-httpapi-httpapidomainconfiguration-securitypolicy
            '''
            result = self._values.get("security_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HttpApiDomainConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.MutualTlsAuthenticationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "truststore_uri": "truststoreUri",
            "truststore_version": "truststoreVersion",
        },
    )
    class MutualTlsAuthenticationProperty:
        def __init__(
            self,
            *,
            truststore_uri: typing.Optional[builtins.str] = None,
            truststore_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param truststore_uri: 
            :param truststore_version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-mutualtlsauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                mutual_tls_authentication_property = sam.CfnHttpApi.MutualTlsAuthenticationProperty(
                    truststore_uri="truststoreUri",
                    truststore_version=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd3ec0bc1b40dd4e0ee4569d04749d979c1acb5d1b78ef3f4d4293e1d362d289)
                check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
                check_type(argname="argument truststore_version", value=truststore_version, expected_type=type_hints["truststore_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if truststore_uri is not None:
                self._values["truststore_uri"] = truststore_uri
            if truststore_version is not None:
                self._values["truststore_version"] = truststore_version

        @builtins.property
        def truststore_uri(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-mutualtlsauthentication.html#cfn-serverless-httpapi-mutualtlsauthentication-truststoreuri
            '''
            result = self._values.get("truststore_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def truststore_version(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-mutualtlsauthentication.html#cfn-serverless-httpapi-mutualtlsauthentication-truststoreversion
            '''
            result = self._values.get("truststore_version")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MutualTlsAuthenticationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.Route53ConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "distributed_domain_name": "distributedDomainName",
            "evaluate_target_health": "evaluateTargetHealth",
            "hosted_zone_id": "hostedZoneId",
            "hosted_zone_name": "hostedZoneName",
            "ip_v6": "ipV6",
        },
    )
    class Route53ConfigurationProperty:
        def __init__(
            self,
            *,
            distributed_domain_name: typing.Optional[builtins.str] = None,
            evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            hosted_zone_id: typing.Optional[builtins.str] = None,
            hosted_zone_name: typing.Optional[builtins.str] = None,
            ip_v6: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param distributed_domain_name: 
            :param evaluate_target_health: 
            :param hosted_zone_id: 
            :param hosted_zone_name: 
            :param ip_v6: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-route53configuration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                route53_configuration_property = sam.CfnHttpApi.Route53ConfigurationProperty(
                    distributed_domain_name="distributedDomainName",
                    evaluate_target_health=False,
                    hosted_zone_id="hostedZoneId",
                    hosted_zone_name="hostedZoneName",
                    ip_v6=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2b137bd750a023ee9520050e4d7a987f36176f815267ef87f09c8c01fe6cbf4b)
                check_type(argname="argument distributed_domain_name", value=distributed_domain_name, expected_type=type_hints["distributed_domain_name"])
                check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
                check_type(argname="argument ip_v6", value=ip_v6, expected_type=type_hints["ip_v6"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if distributed_domain_name is not None:
                self._values["distributed_domain_name"] = distributed_domain_name
            if evaluate_target_health is not None:
                self._values["evaluate_target_health"] = evaluate_target_health
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id
            if hosted_zone_name is not None:
                self._values["hosted_zone_name"] = hosted_zone_name
            if ip_v6 is not None:
                self._values["ip_v6"] = ip_v6

        @builtins.property
        def distributed_domain_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-route53configuration.html#cfn-serverless-httpapi-route53configuration-distributeddomainname
            '''
            result = self._values.get("distributed_domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def evaluate_target_health(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-route53configuration.html#cfn-serverless-httpapi-route53configuration-evaluatetargethealth
            '''
            result = self._values.get("evaluate_target_health")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-route53configuration.html#cfn-serverless-httpapi-route53configuration-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-route53configuration.html#cfn-serverless-httpapi-route53configuration-hostedzonename
            '''
            result = self._values.get("hosted_zone_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ip_v6(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-route53configuration.html#cfn-serverless-httpapi-route53configuration-ipv6
            '''
            result = self._values.get("ip_v6")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "Route53ConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.RouteSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "data_trace_enabled": "dataTraceEnabled",
            "detailed_metrics_enabled": "detailedMetricsEnabled",
            "logging_level": "loggingLevel",
            "throttling_burst_limit": "throttlingBurstLimit",
            "throttling_rate_limit": "throttlingRateLimit",
        },
    )
    class RouteSettingsProperty:
        def __init__(
            self,
            *,
            data_trace_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            detailed_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            logging_level: typing.Optional[builtins.str] = None,
            throttling_burst_limit: typing.Optional[jsii.Number] = None,
            throttling_rate_limit: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param data_trace_enabled: 
            :param detailed_metrics_enabled: 
            :param logging_level: 
            :param throttling_burst_limit: 
            :param throttling_rate_limit: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-routesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                route_settings_property = sam.CfnHttpApi.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__38d112cd2b0f8f8b8b5bc3ed66336d958faca3358a97bd9430a8abe1f79d0b8b)
                check_type(argname="argument data_trace_enabled", value=data_trace_enabled, expected_type=type_hints["data_trace_enabled"])
                check_type(argname="argument detailed_metrics_enabled", value=detailed_metrics_enabled, expected_type=type_hints["detailed_metrics_enabled"])
                check_type(argname="argument logging_level", value=logging_level, expected_type=type_hints["logging_level"])
                check_type(argname="argument throttling_burst_limit", value=throttling_burst_limit, expected_type=type_hints["throttling_burst_limit"])
                check_type(argname="argument throttling_rate_limit", value=throttling_rate_limit, expected_type=type_hints["throttling_rate_limit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if data_trace_enabled is not None:
                self._values["data_trace_enabled"] = data_trace_enabled
            if detailed_metrics_enabled is not None:
                self._values["detailed_metrics_enabled"] = detailed_metrics_enabled
            if logging_level is not None:
                self._values["logging_level"] = logging_level
            if throttling_burst_limit is not None:
                self._values["throttling_burst_limit"] = throttling_burst_limit
            if throttling_rate_limit is not None:
                self._values["throttling_rate_limit"] = throttling_rate_limit

        @builtins.property
        def data_trace_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-routesettings.html#cfn-serverless-httpapi-routesettings-datatraceenabled
            '''
            result = self._values.get("data_trace_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def detailed_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-routesettings.html#cfn-serverless-httpapi-routesettings-detailedmetricsenabled
            '''
            result = self._values.get("detailed_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def logging_level(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-routesettings.html#cfn-serverless-httpapi-routesettings-logginglevel
            '''
            result = self._values.get("logging_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-routesettings.html#cfn-serverless-httpapi-routesettings-throttlingburstlimit
            '''
            result = self._values.get("throttling_burst_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-routesettings.html#cfn-serverless-httpapi-routesettings-throttlingratelimit
            '''
            result = self._values.get("throttling_rate_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouteSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnHttpApi.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key", "version": "version"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            version: jsii.Number,
        ) -> None:
            '''
            :param bucket: 
            :param key: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_location_property = sam.CfnHttpApi.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__74ce10b0d8c46201b88b9b0a1c3fb634f855f8d93c63ea0589504071aa7940d5)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
                "version": version,
            }

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-s3location.html#cfn-serverless-httpapi-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-s3location.html#cfn-serverless-httpapi-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-httpapi-s3location.html#cfn-serverless-httpapi-s3location-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnHttpApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "access_log_setting": "accessLogSetting",
        "auth": "auth",
        "cors_configuration": "corsConfiguration",
        "default_route_settings": "defaultRouteSettings",
        "definition_body": "definitionBody",
        "definition_uri": "definitionUri",
        "description": "description",
        "disable_execute_api_endpoint": "disableExecuteApiEndpoint",
        "domain": "domain",
        "fail_on_warnings": "failOnWarnings",
        "route_settings": "routeSettings",
        "stage_name": "stageName",
        "stage_variables": "stageVariables",
        "tags": "tags",
    },
)
class CfnHttpApiProps:
    def __init__(
        self,
        *,
        access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.AccessLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.HttpApiAuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cors_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, typing.Union[CfnHttpApi.CorsConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        definition_body: typing.Any = None,
        definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnHttpApi.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.HttpApiDomainConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        stage_name: typing.Optional[builtins.str] = None,
        stage_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHttpApi``.

        :param access_log_setting: 
        :param auth: 
        :param cors_configuration: 
        :param default_route_settings: 
        :param definition_body: 
        :param definition_uri: 
        :param description: 
        :param disable_execute_api_endpoint: 
        :param domain: 
        :param fail_on_warnings: 
        :param route_settings: 
        :param stage_name: 
        :param stage_variables: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            # authorizers: Any
            # definition_body: Any
            
            cfn_http_api_props = sam.CfnHttpApiProps(
                access_log_setting=sam.CfnHttpApi.AccessLogSettingProperty(
                    destination_arn="destinationArn",
                    format="format"
                ),
                auth=sam.CfnHttpApi.HttpApiAuthProperty(
                    authorizers=authorizers,
                    default_authorizer="defaultAuthorizer"
                ),
                cors_configuration=False,
                default_route_settings=sam.CfnHttpApi.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                ),
                definition_body=definition_body,
                definition_uri="definitionUri",
                description="description",
                disable_execute_api_endpoint=False,
                domain=sam.CfnHttpApi.HttpApiDomainConfigurationProperty(
                    certificate_arn="certificateArn",
                    domain_name="domainName",
            
                    # the properties below are optional
                    base_path="basePath",
                    endpoint_configuration="endpointConfiguration",
                    mutual_tls_authentication=sam.CfnHttpApi.MutualTlsAuthenticationProperty(
                        truststore_uri="truststoreUri",
                        truststore_version=False
                    ),
                    route53=sam.CfnHttpApi.Route53ConfigurationProperty(
                        distributed_domain_name="distributedDomainName",
                        evaluate_target_health=False,
                        hosted_zone_id="hostedZoneId",
                        hosted_zone_name="hostedZoneName",
                        ip_v6=False
                    ),
                    security_policy="securityPolicy"
                ),
                fail_on_warnings=False,
                route_settings=sam.CfnHttpApi.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                ),
                stage_name="stageName",
                stage_variables={
                    "stage_variables_key": "stageVariables"
                },
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fee3d57c5905e9ae9b8f419c1e059cc2543719f1378802233950cf6fd8455b0)
            check_type(argname="argument access_log_setting", value=access_log_setting, expected_type=type_hints["access_log_setting"])
            check_type(argname="argument auth", value=auth, expected_type=type_hints["auth"])
            check_type(argname="argument cors_configuration", value=cors_configuration, expected_type=type_hints["cors_configuration"])
            check_type(argname="argument default_route_settings", value=default_route_settings, expected_type=type_hints["default_route_settings"])
            check_type(argname="argument definition_body", value=definition_body, expected_type=type_hints["definition_body"])
            check_type(argname="argument definition_uri", value=definition_uri, expected_type=type_hints["definition_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_execute_api_endpoint", value=disable_execute_api_endpoint, expected_type=type_hints["disable_execute_api_endpoint"])
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
            check_type(argname="argument fail_on_warnings", value=fail_on_warnings, expected_type=type_hints["fail_on_warnings"])
            check_type(argname="argument route_settings", value=route_settings, expected_type=type_hints["route_settings"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
            check_type(argname="argument stage_variables", value=stage_variables, expected_type=type_hints["stage_variables"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if access_log_setting is not None:
            self._values["access_log_setting"] = access_log_setting
        if auth is not None:
            self._values["auth"] = auth
        if cors_configuration is not None:
            self._values["cors_configuration"] = cors_configuration
        if default_route_settings is not None:
            self._values["default_route_settings"] = default_route_settings
        if definition_body is not None:
            self._values["definition_body"] = definition_body
        if definition_uri is not None:
            self._values["definition_uri"] = definition_uri
        if description is not None:
            self._values["description"] = description
        if disable_execute_api_endpoint is not None:
            self._values["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if domain is not None:
            self._values["domain"] = domain
        if fail_on_warnings is not None:
            self._values["fail_on_warnings"] = fail_on_warnings
        if route_settings is not None:
            self._values["route_settings"] = route_settings
        if stage_name is not None:
            self._values["stage_name"] = stage_name
        if stage_variables is not None:
            self._values["stage_variables"] = stage_variables
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def access_log_setting(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.AccessLogSettingProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-accesslogsetting
        '''
        result = self._values.get("access_log_setting")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.AccessLogSettingProperty]], result)

    @builtins.property
    def auth(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.HttpApiAuthProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-auth
        '''
        result = self._values.get("auth")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.HttpApiAuthProperty]], result)

    @builtins.property
    def cors_configuration(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, CfnHttpApi.CorsConfigurationObjectProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-corsconfiguration
        '''
        result = self._values.get("cors_configuration")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, CfnHttpApi.CorsConfigurationObjectProperty]], result)

    @builtins.property
    def default_route_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.RouteSettingsProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-defaultroutesettings
        '''
        result = self._values.get("default_route_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.RouteSettingsProperty]], result)

    @builtins.property
    def definition_body(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-definitionbody
        '''
        result = self._values.get("definition_body")
        return typing.cast(typing.Any, result)

    @builtins.property
    def definition_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnHttpApi.S3LocationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-definitionuri
        '''
        result = self._values.get("definition_uri")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnHttpApi.S3LocationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_execute_api_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-disableexecuteapiendpoint
        '''
        result = self._values.get("disable_execute_api_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def domain(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.HttpApiDomainConfigurationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-domain
        '''
        result = self._values.get("domain")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.HttpApiDomainConfigurationProperty]], result)

    @builtins.property
    def fail_on_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-failonwarnings
        '''
        result = self._values.get("fail_on_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def route_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.RouteSettingsProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-routesettings
        '''
        result = self._values.get("route_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.RouteSettingsProperty]], result)

    @builtins.property
    def stage_name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-stagename
        '''
        result = self._values.get("stage_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stage_variables(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-stagevariables
        '''
        result = self._values.get("stage_variables")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-httpapi.html#cfn-serverless-httpapi-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHttpApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnLayerVersion(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnLayerVersion",
):
    '''https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesslayerversion.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html
    :cloudformationResource: AWS::Serverless::LayerVersion
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        cfn_layer_version = sam.CfnLayerVersion(self, "MyCfnLayerVersion",
            compatible_runtimes=["compatibleRuntimes"],
            content_uri="contentUri",
            description="description",
            layer_name="layerName",
            license_info="licenseInfo",
            retention_policy="retentionPolicy"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        compatible_runtimes: typing.Optional[typing.Sequence[builtins.str]] = None,
        content_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnLayerVersion.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        layer_name: typing.Optional[builtins.str] = None,
        license_info: typing.Optional[builtins.str] = None,
        retention_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param compatible_runtimes: 
        :param content_uri: 
        :param description: 
        :param layer_name: 
        :param license_info: 
        :param retention_policy: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d4f065acd39501197153b2ca3e032a641ca99d4d20a65016ce46a93cd18e68dc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnLayerVersionProps(
            compatible_runtimes=compatible_runtimes,
            content_uri=content_uri,
            description=description,
            layer_name=layer_name,
            license_info=license_info,
            retention_policy=retention_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d10b12c36b6dac762ac917c78dfa05198c3664b77c0fd3af72c71075106d3fb8)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ad5410fd56404e482d520099d0db7e08bd17f33b2168a1d37d2faaf71b8444f2)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="compatibleRuntimes")
    def compatible_runtimes(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "compatibleRuntimes"))

    @compatible_runtimes.setter
    def compatible_runtimes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__093cbf32daac268eebbcff5baa4f5e4ae65820ddbf5516ed189eebfc8c39f4f5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compatibleRuntimes", value)

    @builtins.property
    @jsii.member(jsii_name="contentUri")
    def content_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnLayerVersion.S3LocationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnLayerVersion.S3LocationProperty"]], jsii.get(self, "contentUri"))

    @content_uri.setter
    def content_uri(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnLayerVersion.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22130e3d78e15600d2b76b39b91e86e5c3ab5be2248240792ac38f9e1c8a087f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentUri", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__82bec5f248f119695b24893b3c462adcff54ddfb853afc3d225aad7725f573c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="layerName")
    def layer_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "layerName"))

    @layer_name.setter
    def layer_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4fae5281fd0168e1c7cdc7e763aafffbffdbd071fcc577f43706e60bf6604cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "layerName", value)

    @builtins.property
    @jsii.member(jsii_name="licenseInfo")
    def license_info(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "licenseInfo"))

    @license_info.setter
    def license_info(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2513868291110cf36dfdaefa90e775c1932a45c854cc31fc407238bd5ea1123)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "licenseInfo", value)

    @builtins.property
    @jsii.member(jsii_name="retentionPolicy")
    def retention_policy(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "retentionPolicy"))

    @retention_policy.setter
    def retention_policy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cffb01a050658eae0d54f4418d5c20e121fa2105419dbecb16143d35f51e731c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "retentionPolicy", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnLayerVersion.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key", "version": "version"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param bucket: 
            :param key: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-layerversion-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_location_property = sam.CfnLayerVersion.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                
                    # the properties below are optional
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10e0516e96e125765d789af3e0b7b3712f4bb6dcd1df25ef9f15e0aef059c171)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-layerversion-s3location.html#cfn-serverless-layerversion-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-layerversion-s3location.html#cfn-serverless-layerversion-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-layerversion-s3location.html#cfn-serverless-layerversion-s3location-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnLayerVersionProps",
    jsii_struct_bases=[],
    name_mapping={
        "compatible_runtimes": "compatibleRuntimes",
        "content_uri": "contentUri",
        "description": "description",
        "layer_name": "layerName",
        "license_info": "licenseInfo",
        "retention_policy": "retentionPolicy",
    },
)
class CfnLayerVersionProps:
    def __init__(
        self,
        *,
        compatible_runtimes: typing.Optional[typing.Sequence[builtins.str]] = None,
        content_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnLayerVersion.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        layer_name: typing.Optional[builtins.str] = None,
        license_info: typing.Optional[builtins.str] = None,
        retention_policy: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnLayerVersion``.

        :param compatible_runtimes: 
        :param content_uri: 
        :param description: 
        :param layer_name: 
        :param license_info: 
        :param retention_policy: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            cfn_layer_version_props = sam.CfnLayerVersionProps(
                compatible_runtimes=["compatibleRuntimes"],
                content_uri="contentUri",
                description="description",
                layer_name="layerName",
                license_info="licenseInfo",
                retention_policy="retentionPolicy"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71f32d1d804bafc80050e7d70d1d4cf4812a0a9fa8f770efb7646469f71b29c7)
            check_type(argname="argument compatible_runtimes", value=compatible_runtimes, expected_type=type_hints["compatible_runtimes"])
            check_type(argname="argument content_uri", value=content_uri, expected_type=type_hints["content_uri"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument layer_name", value=layer_name, expected_type=type_hints["layer_name"])
            check_type(argname="argument license_info", value=license_info, expected_type=type_hints["license_info"])
            check_type(argname="argument retention_policy", value=retention_policy, expected_type=type_hints["retention_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if compatible_runtimes is not None:
            self._values["compatible_runtimes"] = compatible_runtimes
        if content_uri is not None:
            self._values["content_uri"] = content_uri
        if description is not None:
            self._values["description"] = description
        if layer_name is not None:
            self._values["layer_name"] = layer_name
        if license_info is not None:
            self._values["license_info"] = license_info
        if retention_policy is not None:
            self._values["retention_policy"] = retention_policy

    @builtins.property
    def compatible_runtimes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html#cfn-serverless-layerversion-compatibleruntimes
        '''
        result = self._values.get("compatible_runtimes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def content_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnLayerVersion.S3LocationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html#cfn-serverless-layerversion-contenturi
        '''
        result = self._values.get("content_uri")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnLayerVersion.S3LocationProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html#cfn-serverless-layerversion-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def layer_name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html#cfn-serverless-layerversion-layername
        '''
        result = self._values.get("layer_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def license_info(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html#cfn-serverless-layerversion-licenseinfo
        '''
        result = self._values.get("license_info")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def retention_policy(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-layerversion.html#cfn-serverless-layerversion-retentionpolicy
        '''
        result = self._values.get("retention_policy")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnLayerVersionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnSimpleTable(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnSimpleTable",
):
    '''https://github.com/awslabs/serverless-application-model/blob/master/versions/2016-10-31.md#awsserverlesssimpletable.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html
    :cloudformationResource: AWS::Serverless::SimpleTable
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        cfn_simple_table = sam.CfnSimpleTable(self, "MyCfnSimpleTable",
            primary_key=sam.CfnSimpleTable.PrimaryKeyProperty(
                type="type",
        
                # the properties below are optional
                name="name"
            ),
            provisioned_throughput=sam.CfnSimpleTable.ProvisionedThroughputProperty(
                write_capacity_units=123,
        
                # the properties below are optional
                read_capacity_units=123
            ),
            sse_specification=sam.CfnSimpleTable.SSESpecificationProperty(
                sse_enabled=False
            ),
            table_name="tableName",
            tags={
                "tags_key": "tags"
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        primary_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimpleTable.PrimaryKeyProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimpleTable.ProvisionedThroughputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnSimpleTable.SSESpecificationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param primary_key: 
        :param provisioned_throughput: 
        :param sse_specification: 
        :param table_name: 
        :param tags: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49daa8880aa4482f844df7abde9b977c5fd9bef91c748954b20a349543a06826)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnSimpleTableProps(
            primary_key=primary_key,
            provisioned_throughput=provisioned_throughput,
            sse_specification=sse_specification,
            table_name=table_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84a15b03f8ad300dc65a45f999aa5db851797b235f56396c0c983ff265e5f1ef)
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
            type_hints = typing.get_type_hints(_typecheckingstub__40b2ece540d35a5352688cbd48945936ad81f4feec18d0f4135dcf496ddd58bb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

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
    @jsii.member(jsii_name="primaryKey")
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.PrimaryKeyProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.PrimaryKeyProperty"]], jsii.get(self, "primaryKey"))

    @primary_key.setter
    def primary_key(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.PrimaryKeyProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f863d7782f5fdb473e90c677b8c1346a76510547ebee96393b5c04f2b49e1bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryKey", value)

    @builtins.property
    @jsii.member(jsii_name="provisionedThroughput")
    def provisioned_throughput(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.ProvisionedThroughputProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.ProvisionedThroughputProperty"]], jsii.get(self, "provisionedThroughput"))

    @provisioned_throughput.setter
    def provisioned_throughput(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.ProvisionedThroughputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94e6b5aa5c341686833a2e2528d8fd9aab8a6e34492f10ec6af593470fd29e46)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "provisionedThroughput", value)

    @builtins.property
    @jsii.member(jsii_name="sseSpecification")
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.SSESpecificationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.SSESpecificationProperty"]], jsii.get(self, "sseSpecification"))

    @sse_specification.setter
    def sse_specification(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnSimpleTable.SSESpecificationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03fe1c6d28860594a6ed36eea11303eb5c04ccc3a46d405f6b9583834287d176)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sseSpecification", value)

    @builtins.property
    @jsii.member(jsii_name="tableName")
    def table_name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableName"))

    @table_name.setter
    def table_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8087284d8493b47700bc6e58124e49aceac5573dff0a7a9506a229b85c9ac57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d35381b92f1441a306a58be248d694e2e46740981b8c39578f6894a945658ed)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnSimpleTable.PrimaryKeyProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "name": "name"},
    )
    class PrimaryKeyProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param type: 
            :param name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-primarykey.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                primary_key_property = sam.CfnSimpleTable.PrimaryKeyProperty(
                    type="type",
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__be45ebf18bd2f3b3fe8e6d7df7f64c64d5e0c8b7bcb36b2e7e1c113748de9b74)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-primarykey.html#cfn-serverless-simpletable-primarykey-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-primarykey.html#cfn-serverless-simpletable-primarykey-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PrimaryKeyProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnSimpleTable.ProvisionedThroughputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "write_capacity_units": "writeCapacityUnits",
            "read_capacity_units": "readCapacityUnits",
        },
    )
    class ProvisionedThroughputProperty:
        def __init__(
            self,
            *,
            write_capacity_units: jsii.Number,
            read_capacity_units: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param write_capacity_units: 
            :param read_capacity_units: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-provisionedthroughput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                provisioned_throughput_property = sam.CfnSimpleTable.ProvisionedThroughputProperty(
                    write_capacity_units=123,
                
                    # the properties below are optional
                    read_capacity_units=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__487d0524c5037b22c73aabd8a4b7e2dabf1f5ac6c75c09973275c283ade8ceef)
                check_type(argname="argument write_capacity_units", value=write_capacity_units, expected_type=type_hints["write_capacity_units"])
                check_type(argname="argument read_capacity_units", value=read_capacity_units, expected_type=type_hints["read_capacity_units"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "write_capacity_units": write_capacity_units,
            }
            if read_capacity_units is not None:
                self._values["read_capacity_units"] = read_capacity_units

        @builtins.property
        def write_capacity_units(self) -> jsii.Number:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-provisionedthroughput.html#cfn-serverless-simpletable-provisionedthroughput-writecapacityunits
            '''
            result = self._values.get("write_capacity_units")
            assert result is not None, "Required property 'write_capacity_units' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def read_capacity_units(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-provisionedthroughput.html#cfn-serverless-simpletable-provisionedthroughput-readcapacityunits
            '''
            result = self._values.get("read_capacity_units")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ProvisionedThroughputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnSimpleTable.SSESpecificationProperty",
        jsii_struct_bases=[],
        name_mapping={"sse_enabled": "sseEnabled"},
    )
    class SSESpecificationProperty:
        def __init__(
            self,
            *,
            sse_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param sse_enabled: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-ssespecification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s_sESpecification_property = sam.CfnSimpleTable.SSESpecificationProperty(
                    sse_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7477a7138a2224049d36e777df52e78339ec289222e92cb6a4dcb006f978dbfe)
                check_type(argname="argument sse_enabled", value=sse_enabled, expected_type=type_hints["sse_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sse_enabled is not None:
                self._values["sse_enabled"] = sse_enabled

        @builtins.property
        def sse_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-simpletable-ssespecification.html#cfn-serverless-simpletable-ssespecification-sseenabled
            '''
            result = self._values.get("sse_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SSESpecificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnSimpleTableProps",
    jsii_struct_bases=[],
    name_mapping={
        "primary_key": "primaryKey",
        "provisioned_throughput": "provisionedThroughput",
        "sse_specification": "sseSpecification",
        "table_name": "tableName",
        "tags": "tags",
    },
)
class CfnSimpleTableProps:
    def __init__(
        self,
        *,
        primary_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.PrimaryKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.ProvisionedThroughputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.SSESpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        table_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnSimpleTable``.

        :param primary_key: 
        :param provisioned_throughput: 
        :param sse_specification: 
        :param table_name: 
        :param tags: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            cfn_simple_table_props = sam.CfnSimpleTableProps(
                primary_key=sam.CfnSimpleTable.PrimaryKeyProperty(
                    type="type",
            
                    # the properties below are optional
                    name="name"
                ),
                provisioned_throughput=sam.CfnSimpleTable.ProvisionedThroughputProperty(
                    write_capacity_units=123,
            
                    # the properties below are optional
                    read_capacity_units=123
                ),
                sse_specification=sam.CfnSimpleTable.SSESpecificationProperty(
                    sse_enabled=False
                ),
                table_name="tableName",
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__598a09546c8d488353c6a28e36199c3a64135f51ecbcebfaab1a6094ceadba3b)
            check_type(argname="argument primary_key", value=primary_key, expected_type=type_hints["primary_key"])
            check_type(argname="argument provisioned_throughput", value=provisioned_throughput, expected_type=type_hints["provisioned_throughput"])
            check_type(argname="argument sse_specification", value=sse_specification, expected_type=type_hints["sse_specification"])
            check_type(argname="argument table_name", value=table_name, expected_type=type_hints["table_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if primary_key is not None:
            self._values["primary_key"] = primary_key
        if provisioned_throughput is not None:
            self._values["provisioned_throughput"] = provisioned_throughput
        if sse_specification is not None:
            self._values["sse_specification"] = sse_specification
        if table_name is not None:
            self._values["table_name"] = table_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def primary_key(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.PrimaryKeyProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html#cfn-serverless-simpletable-primarykey
        '''
        result = self._values.get("primary_key")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.PrimaryKeyProperty]], result)

    @builtins.property
    def provisioned_throughput(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.ProvisionedThroughputProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html#cfn-serverless-simpletable-provisionedthroughput
        '''
        result = self._values.get("provisioned_throughput")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.ProvisionedThroughputProperty]], result)

    @builtins.property
    def sse_specification(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.SSESpecificationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html#cfn-serverless-simpletable-ssespecification
        '''
        result = self._values.get("sse_specification")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.SSESpecificationProperty]], result)

    @builtins.property
    def table_name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html#cfn-serverless-simpletable-tablename
        '''
        result = self._values.get("table_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-simpletable.html#cfn-serverless-simpletable-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnSimpleTableProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStateMachine(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine",
):
    '''https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-resource-statemachine.html.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html
    :cloudformationResource: AWS::Serverless::StateMachine
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_sam as sam
        
        # definition: Any
        
        cfn_state_machine = sam.CfnStateMachine(self, "MyCfnStateMachine",
            definition=definition,
            definition_substitutions={
                "definition_substitutions_key": "definitionSubstitutions"
            },
            definition_uri="definitionUri",
            events={
                "events_key": sam.CfnStateMachine.EventSourceProperty(
                    properties=sam.CfnStateMachine.ApiEventProperty(
                        method="method",
                        path="path",
        
                        # the properties below are optional
                        rest_api_id="restApiId"
                    ),
                    type="type"
                )
            },
            logging=sam.CfnStateMachine.LoggingConfigurationProperty(
                destinations=[sam.CfnStateMachine.LogDestinationProperty(
                    cloud_watch_logs_log_group=sam.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                        log_group_arn="logGroupArn"
                    )
                )],
                include_execution_data=False,
                level="level"
            ),
            name="name",
            permissions_boundaries="permissionsBoundaries",
            policies="policies",
            role="role",
            tags={
                "tags_key": "tags"
            },
            tracing=sam.CfnStateMachine.TracingConfigurationProperty(
                enabled=False
            ),
            type="type"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        definition: typing.Any = None,
        definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnStateMachine.S3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.EventSourceProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.LoggingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions_boundaries: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnStateMachine.IAMPolicyDocumentProperty", typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union["CfnStateMachine.IAMPolicyDocumentProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnStateMachine.SAMPolicyTemplateProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        role: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tracing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.TracingConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param definition: 
        :param definition_substitutions: 
        :param definition_uri: 
        :param events: 
        :param logging: 
        :param name: 
        :param permissions_boundaries: 
        :param policies: 
        :param role: 
        :param tags: 
        :param tracing: 
        :param type: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa34f84b79e27e3369f06403c6b18551d70f35e4a3b615bb7cd7c7098379784b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStateMachineProps(
            definition=definition,
            definition_substitutions=definition_substitutions,
            definition_uri=definition_uri,
            events=events,
            logging=logging,
            name=name,
            permissions_boundaries=permissions_boundaries,
            policies=policies,
            role=role,
            tags=tags,
            tracing=tracing,
            type=type,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0f447e7e1726ed05f7b3b1f0b0baee4f78b65aedfab90cf94f7a932b53ebd20)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8838b73bfb182cefd4b4952770146574fcbb71987f2ac5837f5c339109555e61)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="REQUIRED_TRANSFORM")
    def REQUIRED_TRANSFORM(cls) -> builtins.str:
        '''The ``Transform`` a template must use in order to use this resource.'''
        return typing.cast(builtins.str, jsii.sget(cls, "REQUIRED_TRANSFORM"))

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
    @jsii.member(jsii_name="definition")
    def definition(self) -> typing.Any:
        return typing.cast(typing.Any, jsii.get(self, "definition"))

    @definition.setter
    def definition(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d3d4f6819243ae5cfa1d9d6defa295a3b23790f17ebd02c4d51d355d543406b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="definitionSubstitutions")
    def definition_substitutions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], jsii.get(self, "definitionSubstitutions"))

    @definition_substitutions.setter
    def definition_substitutions(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5775a6876026b1a8c899a35d8111a4a33d5e70eba087059cf927fee69bfcad24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionSubstitutions", value)

    @builtins.property
    @jsii.member(jsii_name="definitionUri")
    def definition_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.S3LocationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.S3LocationProperty"]], jsii.get(self, "definitionUri"))

    @definition_uri.setter
    def definition_uri(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.S3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ac29b6e0fb8782fe04c91e9d376d5ece3d1cf8f5986daeec1b67d525f715aee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definitionUri", value)

    @builtins.property
    @jsii.member(jsii_name="events")
    def events(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnStateMachine.EventSourceProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnStateMachine.EventSourceProperty"]]]], jsii.get(self, "events"))

    @events.setter
    def events(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnStateMachine.EventSourceProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c69f012e3879a5483e31f6e7d98193cf937b522d1e5fc4155f1ace6557abe68a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "events", value)

    @builtins.property
    @jsii.member(jsii_name="logging")
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LoggingConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LoggingConfigurationProperty"]], jsii.get(self, "logging"))

    @logging.setter
    def logging(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LoggingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1bd2eec7384b45fa445ff5df87e1ec967ddba4c029ebdf2318c8153ffda4b5d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logging", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5550fb2235bd7489d45f17c70c50139dda815ee3a13d3c2d734e5b903ab4cf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="permissionsBoundaries")
    def permissions_boundaries(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "permissionsBoundaries"))

    @permissions_boundaries.setter
    def permissions_boundaries(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2aaa917b28fe4e0652ce7a6a1728ecade86d1885c3d308a39e942d6db4e60f14)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "permissionsBoundaries", value)

    @builtins.property
    @jsii.member(jsii_name="policies")
    def policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.IAMPolicyDocumentProperty", typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.IAMPolicyDocumentProperty", "CfnStateMachine.SAMPolicyTemplateProperty"]]]]:
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.IAMPolicyDocumentProperty", typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.IAMPolicyDocumentProperty", "CfnStateMachine.SAMPolicyTemplateProperty"]]]], jsii.get(self, "policies"))

    @policies.setter
    def policies(
        self,
        value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.IAMPolicyDocumentProperty", typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, "CfnStateMachine.IAMPolicyDocumentProperty", "CfnStateMachine.SAMPolicyTemplateProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75f2dd4ecaf463e4efaeb629364956c57cab27cb413f89bd7db13d284395bac4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "policies", value)

    @builtins.property
    @jsii.member(jsii_name="role")
    def role(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "role"))

    @role.setter
    def role(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f7e9ebff859a9ffc3340242f19d27c150cdf6585b4b792af885c5342f9331af2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "role", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__565feae73000a6262db11dd021fb78acbb7d88ef7985a3cb3c253bb8eed469aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tracing")
    def tracing(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.TracingConfigurationProperty"]]:
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.TracingConfigurationProperty"]], jsii.get(self, "tracing"))

    @tracing.setter
    def tracing(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.TracingConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8388e699502b5c0e2cfd9cce3567a56b150d0ef870feb0fa36e24467ee7fd59f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tracing", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "type"))

    @type.setter
    def type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d50f330540a6c9c0587734dc19098ad7a915876885f3320395fd2f25f92ce666)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.ApiEventProperty",
        jsii_struct_bases=[],
        name_mapping={"method": "method", "path": "path", "rest_api_id": "restApiId"},
    )
    class ApiEventProperty:
        def __init__(
            self,
            *,
            method: builtins.str,
            path: builtins.str,
            rest_api_id: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param method: 
            :param path: 
            :param rest_api_id: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-apievent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                api_event_property = sam.CfnStateMachine.ApiEventProperty(
                    method="method",
                    path="path",
                
                    # the properties below are optional
                    rest_api_id="restApiId"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__36a9790bf179dc695340e1ceefa5ddcd4bcf297927ed7bfe0ad828ef0b7e9165)
                check_type(argname="argument method", value=method, expected_type=type_hints["method"])
                check_type(argname="argument path", value=path, expected_type=type_hints["path"])
                check_type(argname="argument rest_api_id", value=rest_api_id, expected_type=type_hints["rest_api_id"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "method": method,
                "path": path,
            }
            if rest_api_id is not None:
                self._values["rest_api_id"] = rest_api_id

        @builtins.property
        def method(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-apievent.html#cfn-serverless-statemachine-apievent-method
            '''
            result = self._values.get("method")
            assert result is not None, "Required property 'method' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def path(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-apievent.html#cfn-serverless-statemachine-apievent-path
            '''
            result = self._values.get("path")
            assert result is not None, "Required property 'path' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def rest_api_id(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-apievent.html#cfn-serverless-statemachine-apievent-restapiid
            '''
            result = self._values.get("rest_api_id")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.CloudWatchEventEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pattern": "pattern",
            "event_bus_name": "eventBusName",
            "input": "input",
            "input_path": "inputPath",
        },
    )
    class CloudWatchEventEventProperty:
        def __init__(
            self,
            *,
            pattern: typing.Any,
            event_bus_name: typing.Optional[builtins.str] = None,
            input: typing.Optional[builtins.str] = None,
            input_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param pattern: 
            :param event_bus_name: 
            :param input: 
            :param input_path: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatcheventevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # pattern: Any
                
                cloud_watch_event_event_property = sam.CfnStateMachine.CloudWatchEventEventProperty(
                    pattern=pattern,
                
                    # the properties below are optional
                    event_bus_name="eventBusName",
                    input="input",
                    input_path="inputPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3043510f3e010c02b7e6d61039b56a09a5cc20da321879a3a1dd807d57236bf3)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pattern": pattern,
            }
            if event_bus_name is not None:
                self._values["event_bus_name"] = event_bus_name
            if input is not None:
                self._values["input"] = input
            if input_path is not None:
                self._values["input_path"] = input_path

        @builtins.property
        def pattern(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatcheventevent.html#cfn-serverless-statemachine-cloudwatcheventevent-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_bus_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatcheventevent.html#cfn-serverless-statemachine-cloudwatcheventevent-eventbusname
            '''
            result = self._values.get("event_bus_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatcheventevent.html#cfn-serverless-statemachine-cloudwatcheventevent-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatcheventevent.html#cfn-serverless-statemachine-cloudwatcheventevent-inputpath
            '''
            result = self._values.get("input_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchEventEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.CloudWatchLogsLogGroupProperty",
        jsii_struct_bases=[],
        name_mapping={"log_group_arn": "logGroupArn"},
    )
    class CloudWatchLogsLogGroupProperty:
        def __init__(self, *, log_group_arn: builtins.str) -> None:
            '''
            :param log_group_arn: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatchlogsloggroup.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                cloud_watch_logs_log_group_property = sam.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                    log_group_arn="logGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d1b7ec34ef3cd6ce67421530c570c208c6db5b7e85ef74cdc95aae9ebc0cf925)
                check_type(argname="argument log_group_arn", value=log_group_arn, expected_type=type_hints["log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "log_group_arn": log_group_arn,
            }

        @builtins.property
        def log_group_arn(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-cloudwatchlogsloggroup.html#cfn-serverless-statemachine-cloudwatchlogsloggroup-loggrouparn
            '''
            result = self._values.get("log_group_arn")
            assert result is not None, "Required property 'log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchLogsLogGroupProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.EventBridgeRuleEventProperty",
        jsii_struct_bases=[],
        name_mapping={
            "pattern": "pattern",
            "event_bus_name": "eventBusName",
            "input": "input",
            "input_path": "inputPath",
        },
    )
    class EventBridgeRuleEventProperty:
        def __init__(
            self,
            *,
            pattern: typing.Any,
            event_bus_name: typing.Optional[builtins.str] = None,
            input: typing.Optional[builtins.str] = None,
            input_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param pattern: 
            :param event_bus_name: 
            :param input: 
            :param input_path: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventbridgeruleevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # pattern: Any
                
                event_bridge_rule_event_property = sam.CfnStateMachine.EventBridgeRuleEventProperty(
                    pattern=pattern,
                
                    # the properties below are optional
                    event_bus_name="eventBusName",
                    input="input",
                    input_path="inputPath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c69530dd6f9c5f0c469af173c6c859df452b5c7d088a25087060787de43035bf)
                check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
                check_type(argname="argument event_bus_name", value=event_bus_name, expected_type=type_hints["event_bus_name"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
                check_type(argname="argument input_path", value=input_path, expected_type=type_hints["input_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pattern": pattern,
            }
            if event_bus_name is not None:
                self._values["event_bus_name"] = event_bus_name
            if input is not None:
                self._values["input"] = input
            if input_path is not None:
                self._values["input_path"] = input_path

        @builtins.property
        def pattern(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventbridgeruleevent.html#cfn-serverless-statemachine-eventbridgeruleevent-pattern
            '''
            result = self._values.get("pattern")
            assert result is not None, "Required property 'pattern' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def event_bus_name(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventbridgeruleevent.html#cfn-serverless-statemachine-eventbridgeruleevent-eventbusname
            '''
            result = self._values.get("event_bus_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventbridgeruleevent.html#cfn-serverless-statemachine-eventbridgeruleevent-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def input_path(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventbridgeruleevent.html#cfn-serverless-statemachine-eventbridgeruleevent-inputpath
            '''
            result = self._values.get("input_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventBridgeRuleEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.EventSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"properties": "properties", "type": "type"},
    )
    class EventSourceProperty:
        def __init__(
            self,
            *,
            properties: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.ApiEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnStateMachine.CloudWatchEventEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnStateMachine.EventBridgeRuleEventProperty", typing.Dict[builtins.str, typing.Any]], typing.Union["CfnStateMachine.ScheduleEventProperty", typing.Dict[builtins.str, typing.Any]]],
            type: builtins.str,
        ) -> None:
            '''
            :param properties: 
            :param type: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                event_source_property = sam.CfnStateMachine.EventSourceProperty(
                    properties=sam.CfnStateMachine.ApiEventProperty(
                        method="method",
                        path="path",
                
                        # the properties below are optional
                        rest_api_id="restApiId"
                    ),
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e48d983a36222c7edc08f990a77627e82bb5f349be43393cd36983084cc65baf)
                check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "properties": properties,
                "type": type,
            }

        @builtins.property
        def properties(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnStateMachine.ApiEventProperty", "CfnStateMachine.CloudWatchEventEventProperty", "CfnStateMachine.EventBridgeRuleEventProperty", "CfnStateMachine.ScheduleEventProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventsource.html#cfn-serverless-statemachine-eventsource-properties
            '''
            result = self._values.get("properties")
            assert result is not None, "Required property 'properties' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStateMachine.ApiEventProperty", "CfnStateMachine.CloudWatchEventEventProperty", "CfnStateMachine.EventBridgeRuleEventProperty", "CfnStateMachine.ScheduleEventProperty"], result)

        @builtins.property
        def type(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-eventsource.html#cfn-serverless-statemachine-eventsource-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.FunctionSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"function_name": "functionName"},
    )
    class FunctionSAMPTProperty:
        def __init__(self, *, function_name: builtins.str) -> None:
            '''
            :param function_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-functionsampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                function_sAMPTProperty = sam.CfnStateMachine.FunctionSAMPTProperty(
                    function_name="functionName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d2624ceb5c7626932a2d529134a4d68711bdd820bbbf14ef54bf9e0c4b85e69b)
                check_type(argname="argument function_name", value=function_name, expected_type=type_hints["function_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_name": function_name,
            }

        @builtins.property
        def function_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-functionsampt.html#cfn-serverless-statemachine-functionsampt-functionname
            '''
            result = self._values.get("function_name")
            assert result is not None, "Required property 'function_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FunctionSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.IAMPolicyDocumentProperty",
        jsii_struct_bases=[],
        name_mapping={"statement": "statement", "version": "version"},
    )
    class IAMPolicyDocumentProperty:
        def __init__(self, *, statement: typing.Any, version: builtins.str) -> None:
            '''
            :param statement: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-iampolicydocument.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                # statement: Any
                
                i_aMPolicy_document_property = {
                    "statement": statement,
                    "version": "version"
                }
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c6f663f1c2d20d6ad14f635cbaa2dae4bcb9499a11369ec11b26762e61633406)
                check_type(argname="argument statement", value=statement, expected_type=type_hints["statement"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "statement": statement,
                "version": version,
            }

        @builtins.property
        def statement(self) -> typing.Any:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-iampolicydocument.html#cfn-serverless-statemachine-iampolicydocument-statement
            '''
            result = self._values.get("statement")
            assert result is not None, "Required property 'statement' is missing"
            return typing.cast(typing.Any, result)

        @builtins.property
        def version(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-iampolicydocument.html#cfn-serverless-statemachine-iampolicydocument-version
            '''
            result = self._values.get("version")
            assert result is not None, "Required property 'version' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IAMPolicyDocumentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.LogDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs_log_group": "cloudWatchLogsLogGroup"},
    )
    class LogDestinationProperty:
        def __init__(
            self,
            *,
            cloud_watch_logs_log_group: typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.CloudWatchLogsLogGroupProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''
            :param cloud_watch_logs_log_group: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-logdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                log_destination_property = sam.CfnStateMachine.LogDestinationProperty(
                    cloud_watch_logs_log_group=sam.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                        log_group_arn="logGroupArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6ce735dd8db89ab446699c88f1f4e17c39b2b63345abe0a0ecb7fe6f180c708a)
                check_type(argname="argument cloud_watch_logs_log_group", value=cloud_watch_logs_log_group, expected_type=type_hints["cloud_watch_logs_log_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_logs_log_group": cloud_watch_logs_log_group,
            }

        @builtins.property
        def cloud_watch_logs_log_group(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnStateMachine.CloudWatchLogsLogGroupProperty"]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-logdestination.html#cfn-serverless-statemachine-logdestination-cloudwatchlogsloggroup
            '''
            result = self._values.get("cloud_watch_logs_log_group")
            assert result is not None, "Required property 'cloud_watch_logs_log_group' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnStateMachine.CloudWatchLogsLogGroupProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LogDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.LoggingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "destinations": "destinations",
            "include_execution_data": "includeExecutionData",
            "level": "level",
        },
    )
    class LoggingConfigurationProperty:
        def __init__(
            self,
            *,
            destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.LogDestinationProperty", typing.Dict[builtins.str, typing.Any]]]]],
            include_execution_data: typing.Union[builtins.bool, _IResolvable_da3f097b],
            level: builtins.str,
        ) -> None:
            '''
            :param destinations: 
            :param include_execution_data: 
            :param level: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-loggingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                logging_configuration_property = sam.CfnStateMachine.LoggingConfigurationProperty(
                    destinations=[sam.CfnStateMachine.LogDestinationProperty(
                        cloud_watch_logs_log_group=sam.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                            log_group_arn="logGroupArn"
                        )
                    )],
                    include_execution_data=False,
                    level="level"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bc54f834d8e55c057a6bcfa087f768484ceb97f5fde3f7f8c0296f718a629c2)
                check_type(argname="argument destinations", value=destinations, expected_type=type_hints["destinations"])
                check_type(argname="argument include_execution_data", value=include_execution_data, expected_type=type_hints["include_execution_data"])
                check_type(argname="argument level", value=level, expected_type=type_hints["level"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destinations": destinations,
                "include_execution_data": include_execution_data,
                "level": level,
            }

        @builtins.property
        def destinations(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LogDestinationProperty"]]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-loggingconfiguration.html#cfn-serverless-statemachine-loggingconfiguration-destinations
            '''
            result = self._values.get("destinations")
            assert result is not None, "Required property 'destinations' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.LogDestinationProperty"]]], result)

        @builtins.property
        def include_execution_data(
            self,
        ) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-loggingconfiguration.html#cfn-serverless-statemachine-loggingconfiguration-includeexecutiondata
            '''
            result = self._values.get("include_execution_data")
            assert result is not None, "Required property 'include_execution_data' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        @builtins.property
        def level(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-loggingconfiguration.html#cfn-serverless-statemachine-loggingconfiguration-level
            '''
            result = self._values.get("level")
            assert result is not None, "Required property 'level' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LoggingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.S3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"bucket": "bucket", "key": "key", "version": "version"},
    )
    class S3LocationProperty:
        def __init__(
            self,
            *,
            bucket: builtins.str,
            key: builtins.str,
            version: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''
            :param bucket: 
            :param key: 
            :param version: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-s3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s3_location_property = sam.CfnStateMachine.S3LocationProperty(
                    bucket="bucket",
                    key="key",
                
                    # the properties below are optional
                    version=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__934f7db3bc14294d26fb4899060ef54bc5d08fdd5ba17db2a66d7c6a280caf19)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket": bucket,
                "key": key,
            }
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def bucket(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-s3location.html#cfn-serverless-statemachine-s3location-bucket
            '''
            result = self._values.get("bucket")
            assert result is not None, "Required property 'bucket' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-s3location.html#cfn-serverless-statemachine-s3location-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def version(self) -> typing.Optional[jsii.Number]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-s3location.html#cfn-serverless-statemachine-s3location-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.SAMPolicyTemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lambda_invoke_policy": "lambdaInvokePolicy",
            "step_functions_execution_policy": "stepFunctionsExecutionPolicy",
        },
    )
    class SAMPolicyTemplateProperty:
        def __init__(
            self,
            *,
            lambda_invoke_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.FunctionSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            step_functions_execution_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStateMachine.StateMachineSAMPTProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''
            :param lambda_invoke_policy: 
            :param step_functions_execution_policy: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-sampolicytemplate.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                s_aMPolicy_template_property = sam.CfnStateMachine.SAMPolicyTemplateProperty(
                    lambda_invoke_policy=sam.CfnStateMachine.FunctionSAMPTProperty(
                        function_name="functionName"
                    ),
                    step_functions_execution_policy=sam.CfnStateMachine.StateMachineSAMPTProperty(
                        state_machine_name="stateMachineName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__635d502c9699a6c52eb9e5f1681c94fe4b561fc47930fb2c9289a37d74161c1f)
                check_type(argname="argument lambda_invoke_policy", value=lambda_invoke_policy, expected_type=type_hints["lambda_invoke_policy"])
                check_type(argname="argument step_functions_execution_policy", value=step_functions_execution_policy, expected_type=type_hints["step_functions_execution_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lambda_invoke_policy is not None:
                self._values["lambda_invoke_policy"] = lambda_invoke_policy
            if step_functions_execution_policy is not None:
                self._values["step_functions_execution_policy"] = step_functions_execution_policy

        @builtins.property
        def lambda_invoke_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.FunctionSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-sampolicytemplate.html#cfn-serverless-statemachine-sampolicytemplate-lambdainvokepolicy
            '''
            result = self._values.get("lambda_invoke_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.FunctionSAMPTProperty"]], result)

        @builtins.property
        def step_functions_execution_policy(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.StateMachineSAMPTProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-sampolicytemplate.html#cfn-serverless-statemachine-sampolicytemplate-stepfunctionsexecutionpolicy
            '''
            result = self._values.get("step_functions_execution_policy")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStateMachine.StateMachineSAMPTProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SAMPolicyTemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.ScheduleEventProperty",
        jsii_struct_bases=[],
        name_mapping={"schedule": "schedule", "input": "input"},
    )
    class ScheduleEventProperty:
        def __init__(
            self,
            *,
            schedule: builtins.str,
            input: typing.Optional[builtins.str] = None,
        ) -> None:
            '''
            :param schedule: 
            :param input: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-scheduleevent.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                schedule_event_property = sam.CfnStateMachine.ScheduleEventProperty(
                    schedule="schedule",
                
                    # the properties below are optional
                    input="input"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6b747b0481f1b704b7ab46bc6bcea38b37b4c026f34956aadf2b2701d277561a)
                check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
                check_type(argname="argument input", value=input, expected_type=type_hints["input"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "schedule": schedule,
            }
            if input is not None:
                self._values["input"] = input

        @builtins.property
        def schedule(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-scheduleevent.html#cfn-serverless-statemachine-scheduleevent-schedule
            '''
            result = self._values.get("schedule")
            assert result is not None, "Required property 'schedule' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def input(self) -> typing.Optional[builtins.str]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-scheduleevent.html#cfn-serverless-statemachine-scheduleevent-input
            '''
            result = self._values.get("input")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleEventProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.StateMachineSAMPTProperty",
        jsii_struct_bases=[],
        name_mapping={"state_machine_name": "stateMachineName"},
    )
    class StateMachineSAMPTProperty:
        def __init__(self, *, state_machine_name: builtins.str) -> None:
            '''
            :param state_machine_name: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-statemachinesampt.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                state_machine_sAMPTProperty = sam.CfnStateMachine.StateMachineSAMPTProperty(
                    state_machine_name="stateMachineName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__88ef1508a492222432242a9718c81cccbfe38b86b513c9f606ee3bbc38080c83)
                check_type(argname="argument state_machine_name", value=state_machine_name, expected_type=type_hints["state_machine_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "state_machine_name": state_machine_name,
            }

        @builtins.property
        def state_machine_name(self) -> builtins.str:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-statemachinesampt.html#cfn-serverless-statemachine-statemachinesampt-statemachinename
            '''
            result = self._values.get("state_machine_name")
            assert result is not None, "Required property 'state_machine_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StateMachineSAMPTProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_sam.CfnStateMachine.TracingConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"enabled": "enabled"},
    )
    class TracingConfigurationProperty:
        def __init__(
            self,
            *,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''
            :param enabled: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-tracingconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_sam as sam
                
                tracing_configuration_property = sam.CfnStateMachine.TracingConfigurationProperty(
                    enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8568d1e5362e81260a69221e107002da0809dc2714f5960aaa894d488ddaa3db)
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if enabled is not None:
                self._values["enabled"] = enabled

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-serverless-statemachine-tracingconfiguration.html#cfn-serverless-statemachine-tracingconfiguration-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TracingConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_sam.CfnStateMachineProps",
    jsii_struct_bases=[],
    name_mapping={
        "definition": "definition",
        "definition_substitutions": "definitionSubstitutions",
        "definition_uri": "definitionUri",
        "events": "events",
        "logging": "logging",
        "name": "name",
        "permissions_boundaries": "permissionsBoundaries",
        "policies": "policies",
        "role": "role",
        "tags": "tags",
        "tracing": "tracing",
        "type": "type",
    },
)
class CfnStateMachineProps:
    def __init__(
        self,
        *,
        definition: typing.Any = None,
        definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
        definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        permissions_boundaries: typing.Optional[builtins.str] = None,
        policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnStateMachine.SAMPolicyTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        role: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        tracing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.TracingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnStateMachine``.

        :param definition: 
        :param definition_substitutions: 
        :param definition_uri: 
        :param events: 
        :param logging: 
        :param name: 
        :param permissions_boundaries: 
        :param policies: 
        :param role: 
        :param tags: 
        :param tracing: 
        :param type: 

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_sam as sam
            
            # definition: Any
            
            cfn_state_machine_props = sam.CfnStateMachineProps(
                definition=definition,
                definition_substitutions={
                    "definition_substitutions_key": "definitionSubstitutions"
                },
                definition_uri="definitionUri",
                events={
                    "events_key": sam.CfnStateMachine.EventSourceProperty(
                        properties=sam.CfnStateMachine.ApiEventProperty(
                            method="method",
                            path="path",
            
                            # the properties below are optional
                            rest_api_id="restApiId"
                        ),
                        type="type"
                    )
                },
                logging=sam.CfnStateMachine.LoggingConfigurationProperty(
                    destinations=[sam.CfnStateMachine.LogDestinationProperty(
                        cloud_watch_logs_log_group=sam.CfnStateMachine.CloudWatchLogsLogGroupProperty(
                            log_group_arn="logGroupArn"
                        )
                    )],
                    include_execution_data=False,
                    level="level"
                ),
                name="name",
                permissions_boundaries="permissionsBoundaries",
                policies="policies",
                role="role",
                tags={
                    "tags_key": "tags"
                },
                tracing=sam.CfnStateMachine.TracingConfigurationProperty(
                    enabled=False
                ),
                type="type"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__505a369e8f3bf625077dedf7f13099c6e0c8e2c05182396505111670528d74d7)
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument definition_substitutions", value=definition_substitutions, expected_type=type_hints["definition_substitutions"])
            check_type(argname="argument definition_uri", value=definition_uri, expected_type=type_hints["definition_uri"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument logging", value=logging, expected_type=type_hints["logging"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument permissions_boundaries", value=permissions_boundaries, expected_type=type_hints["permissions_boundaries"])
            check_type(argname="argument policies", value=policies, expected_type=type_hints["policies"])
            check_type(argname="argument role", value=role, expected_type=type_hints["role"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tracing", value=tracing, expected_type=type_hints["tracing"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if definition is not None:
            self._values["definition"] = definition
        if definition_substitutions is not None:
            self._values["definition_substitutions"] = definition_substitutions
        if definition_uri is not None:
            self._values["definition_uri"] = definition_uri
        if events is not None:
            self._values["events"] = events
        if logging is not None:
            self._values["logging"] = logging
        if name is not None:
            self._values["name"] = name
        if permissions_boundaries is not None:
            self._values["permissions_boundaries"] = permissions_boundaries
        if policies is not None:
            self._values["policies"] = policies
        if role is not None:
            self._values["role"] = role
        if tags is not None:
            self._values["tags"] = tags
        if tracing is not None:
            self._values["tracing"] = tracing
        if type is not None:
            self._values["type"] = type

    @builtins.property
    def definition(self) -> typing.Any:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-definition
        '''
        result = self._values.get("definition")
        return typing.cast(typing.Any, result)

    @builtins.property
    def definition_substitutions(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-definitionsubstitutions
        '''
        result = self._values.get("definition_substitutions")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]], result)

    @builtins.property
    def definition_uri(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.S3LocationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-definitionuri
        '''
        result = self._values.get("definition_uri")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.S3LocationProperty]], result)

    @builtins.property
    def events(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnStateMachine.EventSourceProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-events
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnStateMachine.EventSourceProperty]]]], result)

    @builtins.property
    def logging(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.LoggingConfigurationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-logging
        '''
        result = self._values.get("logging")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.LoggingConfigurationProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def permissions_boundaries(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-permissionsboundaries
        '''
        result = self._values.get("permissions_boundaries")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policies(
        self,
    ) -> typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.IAMPolicyDocumentProperty, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.IAMPolicyDocumentProperty, CfnStateMachine.SAMPolicyTemplateProperty]]]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-policies
        '''
        result = self._values.get("policies")
        return typing.cast(typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.IAMPolicyDocumentProperty, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.IAMPolicyDocumentProperty, CfnStateMachine.SAMPolicyTemplateProperty]]]], result)

    @builtins.property
    def role(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-role
        '''
        result = self._values.get("role")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def tracing(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.TracingConfigurationProperty]]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-tracing
        '''
        result = self._values.get("tracing")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.TracingConfigurationProperty]], result)

    @builtins.property
    def type(self) -> typing.Optional[builtins.str]:
        '''
        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-serverless-statemachine.html#cfn-serverless-statemachine-type
        '''
        result = self._values.get("type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStateMachineProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApi",
    "CfnApiProps",
    "CfnApplication",
    "CfnApplicationProps",
    "CfnFunction",
    "CfnFunctionProps",
    "CfnHttpApi",
    "CfnHttpApiProps",
    "CfnLayerVersion",
    "CfnLayerVersionProps",
    "CfnSimpleTable",
    "CfnSimpleTableProps",
    "CfnStateMachine",
    "CfnStateMachineProps",
]

publication.publish()

def _typecheckingstub__3135996bb5e2b67d63a2144c699a4377166e2b1ebabc180e4c43b45b5c59afc6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    stage_name: builtins.str,
    access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.AccessLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    always_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.AuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    binary_media_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    cache_cluster_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cache_cluster_size: typing.Optional[builtins.str] = None,
    canary_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.CanarySettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cors: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.CorsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_body: typing.Any = None,
    definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.DomainConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint_configuration: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.EndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gateway_responses: typing.Any = None,
    method_settings: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    minimum_compression_size: typing.Optional[jsii.Number] = None,
    models: typing.Any = None,
    name: typing.Optional[builtins.str] = None,
    open_api_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tracing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__980c536039534f411567f6cf0cb008380fdcc0e98538bc3e291702cbf9a9759a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c6e7bfcfbe140d0e280964b4302aeb918e0c0bef723f5038b4e83865f2137a2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ed0b67619cb13cee60979ea07bab7433a9a3aac2c3381b9e76293bd8a4acbc0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3419ac45d5962e11eb2db0565d8366156554a528cc08dbac9e2dd50637f617de(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.AccessLogSettingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64308e272be1e8e8f200c8877ef85bc40f951d1580772db49e31028cd9e144f6(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b7899a6959fd44c06397e5419ff9b1ac5cc6f9086b4b8ebd3f8cdc094286e5b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.AuthProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8373fadf34e7203e351433b382ba203e1a684129fb26aa8b16985168b4775ba8(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6db99bca07f874422ccf27bae4b332d73412b5b284607e77cca4cf711315d689(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3feeb5c18554c7f510db8100d0cb77b1a824a847babeb1c247dc68e3e3eeb8bd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e835d60486fa1350fa728f5e35beef29325f8745ffd51ac4d8d10ded0065ea83(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.CanarySettingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21dbab6598d5847bc72ec62c28426fe0408db8682d5127fe28a05b213dc8b26a(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.CorsConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd38f5bcc3b8f3fac0bbdfb5d5e3af45744e24319a5d1d7e28038ee4bdfb281(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f2e92449b9c950f501c430abd84aa43a5df516a6602172d17f1558ebe2fea14(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__353032891306086a17e2ae218e03d18455f1ba6f7127e6fefb12def15f0da51c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da75fbe1266a65afaa78ba97bcf585c32f11bacc0c752250a64bb1bdec2930f(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6672be629c8cc80fa0f0b711bf815d7d7e9a5fee9699f73a5b9e844ba8b3b1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.DomainConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966627515263d6c2176ac06d97124210d55dfafc260439f62393f93e44921771(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnApi.EndpointConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8484ea00d921c99afaacbd03cc62295f32910b5df7d96ca8db6a13dc54d28f6a(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89314956b349bc8e1c3bc352780728615074b16dbe9e899a681b4d3fe381dec7(
    value: typing.Optional[typing.Union[typing.List[typing.Any], _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1347fd00b71a6087fdb38700bc130ac87aa76321596ad0a55c2ce78a266a0942(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c11bc94dea5aec21ef52c13c5f4551cc63138a4c4b4f582d2fb6ace3a82483(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbbe4108d9afb71eb640322c267e8e750561d165eff7247edc582f829e3cf088(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2751c6279da41aa599812d74ed6dc4408a3f0805176952a12d00f84ae79a1385(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50f4bb3d61c77c677d99cdcdff136faa1b17e44d9a17165841d93e999613f334(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__381be80448e4bb2d0dfa01f12de99215cac54995a787d289c523b6d8bae92a6c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e18d5b2f60202118ae9b46b2c208eab95ae644832c6148e75937bc7ad0ae9622(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de360432e84693b1344e24631c0725f17fe9270f6be8fe45212ab38ec786134f(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3fa398b1d1629ec063ca30c8b836b8fd210cb478aeb0e7e717a65aa88f949c58(
    *,
    add_default_authorizer_to_cors_preflight: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    authorizers: typing.Any = None,
    default_authorizer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a04c0e58764c2325f15e42a28ebefd2c7e52c177703a95e3b0742576c53e8499(
    *,
    deployment_id: typing.Optional[builtins.str] = None,
    percent_traffic: typing.Optional[jsii.Number] = None,
    stage_variable_overrides: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    use_stage_cache: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__414d627674291aa30dac0b91f4404e6642cfb76656455ab0d5ac92d71982b33a(
    *,
    allow_origin: builtins.str,
    allow_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    allow_headers: typing.Optional[builtins.str] = None,
    allow_methods: typing.Optional[builtins.str] = None,
    max_age: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0f6b4af2fa09b8ccef31dbe8c276532aaa162a75dff7ddbd02a008f9fc5bfdd(
    *,
    certificate_arn: builtins.str,
    domain_name: builtins.str,
    base_path: typing.Optional[typing.Sequence[builtins.str]] = None,
    endpoint_configuration: typing.Optional[builtins.str] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.MutualTlsAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
    route53: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.Route53ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5c7e18fd130e51b8b9ea76b2bcd48c7975a71dbfb0d2ad44746bc76e20bd62(
    *,
    type: typing.Optional[builtins.str] = None,
    vpc_endpoint_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1c2641cdeae9cf6962a20881f31e2146da63ab3ee69f6cf60f458d943b69df(
    *,
    truststore_uri: typing.Optional[builtins.str] = None,
    truststore_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f36a5c3a1241146402681a4c7202b049f3e90d3934d1bc88f8dbe5add7348851(
    *,
    distributed_domain_name: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    ip_v6: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64d64a8ff239842e276cc5e9a2d2aa0f5e33af73e03496183475271e84846c22(
    *,
    bucket: builtins.str,
    key: builtins.str,
    version: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3541ced1e3b9f417bf5019481767d1f0ed3628dc1464b54b8ea1849ea8aa47(
    *,
    stage_name: builtins.str,
    access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.AccessLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    always_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.AuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    binary_media_types: typing.Optional[typing.Sequence[builtins.str]] = None,
    cache_cluster_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    cache_cluster_size: typing.Optional[builtins.str] = None,
    canary_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.CanarySettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cors: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.CorsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_body: typing.Any = None,
    definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.DomainConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    endpoint_configuration: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApi.EndpointConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    gateway_responses: typing.Any = None,
    method_settings: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    minimum_compression_size: typing.Optional[jsii.Number] = None,
    models: typing.Any = None,
    name: typing.Optional[builtins.str] = None,
    open_api_version: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tracing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64c7803062c8244dab10c00b85c3ab7470f7dfeddb1993dc04852359393beb15(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    location: typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationLocationProperty, typing.Dict[builtins.str, typing.Any]]],
    notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3cfb8ff6c6b925c585f554d1d6674947d33c737cdcd2d16d29336a09fb2af11(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4faa051f2c7e79e7f0b8a01c67414bff6de09f387a519833619276f21769af3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bea2e888b58c031cfd3e0c09e3a28062b4857ad0468afb21392d872ac2d42fb(
    value: typing.Union[builtins.str, _IResolvable_da3f097b, CfnApplication.ApplicationLocationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fdba732f0fdb414d7b870bb171355caae720f58a2e5c1495b6c5a846dfb2a30d(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05c9df790cddd4512e3cf1277ea55b48b4d5ddfef54d5b82a13d917e4712e8d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0fe9f2d4319340e068aa84c98f1764850903463360c677f6dc11f74a9577151f(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afbf7f8fe9ecd7f281a8700abae88f7369951bf8e9137d2c282937a3bd700912(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__397227b947496de6fb046a0031f35d134a16d78a2e12e88cce0ddcbadcb03021(
    *,
    application_id: builtins.str,
    semantic_version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5cdd3da86c77e72e8f53daca88bd679d2d41f1881eeba6c4c20c6c5e7f670253(
    *,
    location: typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnApplication.ApplicationLocationProperty, typing.Dict[builtins.str, typing.Any]]],
    notification_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout_in_minutes: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da820696f032573ba53a3fb82221aa76870f3c6257f7de23fa48e9c11fdc3f08(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
    assume_role_policy_document: typing.Any = None,
    auto_publish_alias: typing.Optional[builtins.str] = None,
    auto_publish_code_sha256: typing.Optional[builtins.str] = None,
    code_signing_config_arn: typing.Optional[builtins.str] = None,
    code_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dead_letter_queue: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DeadLetterQueueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DeploymentPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EphemeralStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_invoke_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventInvokeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    file_system_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FileSystemConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    function_name: typing.Optional[builtins.str] = None,
    function_url_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionUrlConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    handler: typing.Optional[builtins.str] = None,
    image_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ImageConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_uri: typing.Optional[builtins.str] = None,
    inline_code: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    layers: typing.Optional[typing.Sequence[builtins.str]] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    package_type: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.SAMPolicyTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    provisioned_concurrency_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ProvisionedConcurrencyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout: typing.Optional[jsii.Number] = None,
    tracing: typing.Optional[builtins.str] = None,
    version_description: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e45cd8ce55983e9ade3f7d3db7401329aa94c3de47100e451bd25c652fc8de8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d8539381db7c34f023921a302ec379417ffbf36402294f5eb3096b31814951f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__961f66d7c1974b43320280bf59275bb9f65d08936dd9d10f4bb6bd856765683b(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d24caacf917d9eb83fd84a13970be6e1524465e06595fa482fd7e7a9ec270bbf(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__928c74644f46c5a0366f7094096db9442d7f036bff4056876fdf442aae89329f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a62a2ab953ee75469cf466d51df213fadfd7c1799b0c5c15f75c8fa97f63ef(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__462f250f21efb27dfe8ec5ab212e7a371eb77ae2d2cff5e42b415fe85501e28c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cd8c7343e03b00e454847a98b74d6c18757a798061a0ddaf9a40e957581ac4a(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1602c0ac23686b7e1ab4aa81450903e569d8e163f1f83becee2385582866bbe1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.DeadLetterQueueProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__434662ed37f7d673963a8e62cf6926339c0b7fcb88c58f9dd34b3bd32ef97ba4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.DeploymentPreferenceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b6f7788ac06b74276f6901acf24ecaf6ddabedbb85d96bb18cf3dc5cb0d8297(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428eed8cc97b122d6d3fcf1bf8472333306140ea5618f5d11b4469437f630916(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.FunctionEnvironmentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9011531a438d2eaca67b7717924c213173db335f957acba46c544dd74b4ebb72(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.EphemeralStorageProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9204c789f9d6e39e76d74025d5c69e0df77fbfa07d0e171d4cecae9f820841dd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.EventInvokeConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2245995f969ab359206105cc502e300f6696f9fd12878fe4d42221d1797d638e(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnFunction.EventSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85d9a64fa00484d8a57b4834aad1164c5c67d396a62327b84d9334439033a987(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnFunction.FileSystemConfigProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cab4b037257cf0675e6835048a9e6cfb3e5cd6acdb3b55b490c89baed365f5d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ab14c2ec03c7a9a455a90ea2ef0ddc230f820b134925767451df0b7a7c86933b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.FunctionUrlConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__377c21e52d013c50d30d5fea093cdec36f68ad854d28d8167a3783f4a9325031(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54089d0977582d5c52fe11343780afa92a8e83a310df8e70688fea8475dbd769(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.ImageConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25165da87e6cfd066042bc2056dd24babd47eea0ae440928a841b2bf58331a15(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2929da0c5428b1fb11c1c65e03c66d9973c6e3dd0d780359dacfe5a2540e4abe(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9997d0fe87f5763b8f89c3f2e9a29cdb0fc9b631403c7494015279c18e6296e9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e4befefb0525c722a39ef1e0102f0459a29f5e5356c132aee49997615b8748d1(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6af5e2bf43488197cc6f5b04bb14d08efd37e9d60d192cb173bc23214be102f7(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cd8147db2aefc22ae6b434ed65a87a0ff8e7c7136999239199804af637649806(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a8715a4cc2adf7439e44f16517420c3a8100bcd7e4f87112ec67554facec1af(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__723515eaec195d558c2b0a94039b44d2f6f71b663c26fc9b10e22ed013d700f7(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.IAMPolicyDocumentProperty, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, CfnFunction.IAMPolicyDocumentProperty, CfnFunction.SAMPolicyTemplateProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ae3ba871bdb92769cd518d31fe5feb386d450634d533562571e0615487f99895(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.ProvisionedConcurrencyConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2b977ba94a4c4945498cbd322fabf09517286f8ac213e5c731e705341c92e89(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0043d107bb7948c568b884ae4373072e04967fa286a3683b7ff122face99e23d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc251e6ad3743a7b8ec0db51b707d68db1077bce8c40f0750bbefa772191aa8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a812fb883340d42ee86b3177bf56d4cbad4fe39e7ebdee880b6444f84b71912a(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72a6bef8ed2bad0c1bae6b02c41c93b4e95c2bfc799e03db9e219bda13907d10(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba0c5501cb85e810b59d3660e5b8e6c48fb00cc9ff1d8d6e3a86dd424d0bf9ae(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2050e867f2d1878cd72f006d40acf5a093399cd84485570dc3134fad0c9b3a5c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f964396263820171d9c1edb021bcf4380c3bed41a2e424da67596989c6e18b94(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFunction.VpcConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3124f40a27e9cf66ff11c883916bf49e663187b79e9133aa89ceb6611bca8300(
    *,
    skill_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f431b22ab6809e259ce2cfa0a8d8ae7ab76c9c0e9197b6defd75f8427566d0d(
    *,
    method: builtins.str,
    path: builtins.str,
    auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.AuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_model: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.RequestModelProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    request_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.RequestParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    rest_api_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__996c871f7db703ff8a44473691cb09158b2791e2346716a2043c81e40cb18878(
    *,
    api_key_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    authorizer: typing.Optional[builtins.str] = None,
    resource_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.AuthResourcePolicyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f4e76793befb0779e1b3791b310b700b6dd4dc94bfc2025141c8541ac674d43(
    *,
    aws_account_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
    aws_account_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    custom_statements: typing.Optional[typing.Union[typing.Sequence[typing.Any], _IResolvable_da3f097b]] = None,
    intrinsic_vpc_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
    intrinsic_vpce_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
    intrinsic_vpce_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    intrinsic_vpc_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ip_range_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
    ip_range_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_vpc_blacklist: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_vpc_whitelist: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e32c5d57ac6183e9b983ffee717a883834c6cd8abc9cff6eafc5dd3db50076f(
    *,
    bucket_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be8ac98ed839a6bf585f926df5cfdc585e188fadadb59d1f1ab3b400f4f5b8dc(
    *,
    pattern: typing.Any,
    input: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d94fbed6c1c504c6a4078c8680333fcee8b6484a9ee431feaed212bfc5d4b139(
    *,
    filter_pattern: builtins.str,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32d7960cc4b1211bf60468d1f1ecd9519efe3f5ed0542d2fd8e57411f28e2c6e(
    *,
    trigger: builtins.str,
    user_pool: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91c13b6a4fa04c2fd214ebd4f9d5faa0504e553c9c177f43a0a91c75576b6355(
    *,
    collection_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fac2265244f6246045fce25da128ba28a1ecb08ded9209e8645ac8803baf502(
    *,
    allow_origin: builtins.str,
    allow_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    allow_headers: typing.Optional[builtins.str] = None,
    allow_methods: typing.Optional[builtins.str] = None,
    max_age: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__143f4d03feab04a8091259025b7001d0b3a0ff69ed51079f2b5c3fb6ea308d0e(
    *,
    target_arn: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80ec550d24f9c572e123af872fcbd1cc14c85c62218fcfd842baa9ea0c19457a(
    *,
    alarms: typing.Optional[typing.Sequence[builtins.str]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    hooks: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.HooksProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    role: typing.Optional[builtins.str] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4e6834826ec418bf7cb40a517aefae406afe2f01b87c594e8231af7ef2d44d(
    *,
    on_failure: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19a984fddac7f5aa6614ba358e496e5c6a3d64eafb7a8830156d75413789877b(
    *,
    destination: builtins.str,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3416f800b26e4a4b713814421c02a5eb690455ce925e56586a4b9cc295c379de(
    *,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7994f805931bd9f33200b9289406ebe947e1aced753b2b63caa991acbaf8375c(
    *,
    starting_position: builtins.str,
    stream: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    bisect_batch_on_function_error: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    destination_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    maximum_batching_window_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_record_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
    parallelization_factor: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45ce4e684ab9f5b3cf6bc040b2591caf92efd3e71ca512561d8aadf333956351(
    *,
    size: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d21280faa223e5cbaf484b31b1a54c1e27952496279e4371dd37068f58de2e84(
    *,
    pattern: typing.Any,
    event_bus_name: typing.Optional[builtins.str] = None,
    input: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ffdd8314f781fb14b52a4e1dcbd551aaa143d3be4ebfc91835e84610c1a8221(
    *,
    destination_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventInvokeDestinationConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    maximum_event_age_in_seconds: typing.Optional[jsii.Number] = None,
    maximum_retry_attempts: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__824278198c661e967b66f4eb4f6fbf05437a14c87c92ad92b09b58ec2b9430b4(
    *,
    on_failure: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    on_success: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46dbad2fdf51b82abf61512b482e040cb7a9cad1c34fcb57e442b94e170227ba(
    *,
    properties: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.AlexaSkillEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.ApiEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.CloudWatchEventEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.CloudWatchLogsEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.CognitoEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.DynamoDBEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.EventBridgeRuleEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.HttpApiEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.IoTRuleEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.KinesisEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.S3EventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.ScheduleEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.SNSEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.SQSEventProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__042927e3bdc41bb37d7a425bbdfe932f3c1c939361ff5d3c2e6aecdc7fa434c9(
    *,
    arn: typing.Optional[builtins.str] = None,
    local_mount_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cede0a875bba921466167c6599c161022b6030dbd7aafacc22aff1e6368d599c(
    *,
    variables: typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093f81bb3b5e1c086cd55a2d914acaab8a0a0ef0a4767ba196b131038b617b48(
    *,
    function_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4ecb4b4628aaffa7df25337985d75a10475a9a2acc64c33bc5ba8f22327c6647(
    *,
    auth_type: builtins.str,
    cors: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.CorsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    invoke_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9007aebebebbce69c2d0c87f2e2742d1f8498d07cfe80ad0bb6c7443e5ac3797(
    *,
    post_traffic: typing.Optional[builtins.str] = None,
    pre_traffic: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10711eaebc24b0b6d7c2096fa4e2efff09f1dc344dcd813dfbdbc65a0cd69d73(
    *,
    api_id: typing.Optional[builtins.str] = None,
    auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.HttpApiFunctionAuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    method: typing.Optional[builtins.str] = None,
    path: typing.Optional[builtins.str] = None,
    payload_format_version: typing.Optional[builtins.str] = None,
    route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    timeout_in_millis: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7365210f2c0abe85eb4502abc70c0b91d091d90ad61f62b0e413a9f142531309(
    *,
    authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    authorizer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e67c50da978059d59c88ab8b8d1c7852ab81b9305b4eedbcdef681cc22ae0a(
    *,
    statement: typing.Any,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e74d676d636da35f6fc94bb061eab42dfecba551f1f354cc4928c40528cdcc3(
    *,
    identity_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4e61b4308921771ef55342ceffbb48da8059092023443e34810850ff6021235(
    *,
    command: typing.Optional[typing.Sequence[builtins.str]] = None,
    entry_point: typing.Optional[typing.Sequence[builtins.str]] = None,
    working_directory: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e155526e0eb0c3fe9a5bad17ef4db715f4ba1cfd78bd6267ee8d5bc11fbc7b18(
    *,
    sql: builtins.str,
    aws_iot_sql_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d5c6f0f2fc01f9bdb0ea9e83b7b977b59c1cb7a304425fef68de2469c11aa9(
    *,
    key_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c64b1479b0a1842a1a96847b1a4615e328dddd86e05be0127714e361981e5dd6(
    *,
    starting_position: builtins.str,
    stream: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    function_response_types: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e04b4c22d0166d6a3e5bd312c5c7d7ca6dc30a06d07b767141bb937c6cd7df74(
    *,
    log_group_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f5d361077204df508de1a22cf132522e123ef11c5d1b23a775902f5df87b052d(
    *,
    parameter_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11e41d9d2beb27f643bf25f769e8756e262c4750aeefbdc253950be55dda6ea3(
    *,
    provisioned_concurrent_executions: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f0ef722a937a4210b60a915a707d83376fb56a04f5d7b493e528cba0661511d(
    *,
    queue_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e309219acb0472ca0420cd85b485500ae16158e868f05c5257fcc93556c6d73(
    *,
    model: builtins.str,
    required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    validate_body: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    validate_parameters: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac1e4a6cd652a6ad38da31062b24a82f26babdae66941dee658ef4cd3024ded0(
    *,
    caching: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a5029f2218b4af39c4bf3f003cf8016727b01889d5237da1b4bb1d35b53449a1(
    *,
    data_trace_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    detailed_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    throttling_burst_limit: typing.Optional[jsii.Number] = None,
    throttling_rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e49962e8f915b8ef11062814b9a35ca163775e823fb71789a682db9ceef34fb(
    *,
    bucket: builtins.str,
    events: builtins.str,
    filter: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.S3NotificationFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5c06b2d04548048dde09ea0b1fe8ba1a7e4939a8123d9061cb00f7a61062a41(
    *,
    rules: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.S3KeyFilterRuleProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e611d540226e79d90ea54cd8dfc0d647853595c3f36c905003cee579212129e3(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__322de417e8a25e0402c762766d176033d9474d7a731b49c4ed8ebab366cf93f0(
    *,
    bucket: builtins.str,
    key: builtins.str,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01d8e171e0b78d84acd020c613260bd3907f21f5febc160d00779177a8141c4d(
    *,
    s3_key: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.S3KeyFilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff6b7c5a716f70e2b1c660dcce5c7e1278abf95e639ec04dda55eeb73dab9900(
    *,
    ami_describe_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    aws_secrets_manager_get_secret_value_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.SecretArnSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_formation_describe_stacks_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cloud_watch_put_metric_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.TableSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.TableSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_stream_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.TableStreamSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dynamo_db_write_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.TableSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ec2_describe_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    elasticsearch_http_post_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DomainSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    filter_log_events_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.LogGroupSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.StreamSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kinesis_stream_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.StreamSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    kms_decrypt_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.KeySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_invoke_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rekognition_detect_only_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rekognition_labels_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rekognition_no_data_access_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.CollectionSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rekognition_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.CollectionSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    rekognition_write_only_access_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.CollectionSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.BucketSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.BucketSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_write_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.BucketSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ses_bulk_templated_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.IdentitySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ses_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.IdentitySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ses_email_template_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ses_send_bounce_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.IdentitySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_crud_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.TopicSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_publish_message_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.TopicSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs_poller_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.QueueSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sqs_send_message_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.QueueSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ssm_parameter_read_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ParameterNameSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    step_functions_execution_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.StateMachineSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_access_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EmptySAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355e23fa07290884140ffa4400be42ee2489af615d914e5dbc61418e2442fdb1(
    *,
    topic: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be37486fa4f2ad612d19140f2fa9c114778a9568b98ab095bf59d0f490ebbf50(
    *,
    queue: builtins.str,
    batch_size: typing.Optional[jsii.Number] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b58bf71ba62a34b17cdeb0700dc0b364f48f1ba42eb0303d2892d136a5646d(
    *,
    schedule: builtins.str,
    description: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    input: typing.Optional[builtins.str] = None,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc73d7367a2bd617be2d5ceeaf2320a43edae98c4dbb45f5f04715394f975ac9(
    *,
    secret_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__000e0ab9ec3a16a77064e3a41bdbbf9c89ce2137e298f69392fb7e13b45605d9(
    *,
    state_machine_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e84bbf253151430417441d85a9ba27164409cf10c9a4dc8bde343da7bad2804b(
    *,
    stream_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b6f81630520c184d99ddebf05e101fb5f2f5d9dbf0765f6f86719cac31c0fa9(
    *,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33276c9d774d609586618c6f65f0d36451764e54646287ffc4e991358e24105e(
    *,
    stream_name: builtins.str,
    table_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ecb052268d71c7d0c161d9e3e08d937ebfc95358aef3ab88aaa379bea48a815(
    *,
    topic_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4435eeff1c78c56e31a2a7233adfeb0466c2772d7ba3682a80039a306b4d45f1(
    *,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d36d7a3f5429a8550f324d9ddc7ca791a504b5e17ff50b124622826fe13b568b(
    *,
    architectures: typing.Optional[typing.Sequence[builtins.str]] = None,
    assume_role_policy_document: typing.Any = None,
    auto_publish_alias: typing.Optional[builtins.str] = None,
    auto_publish_code_sha256: typing.Optional[builtins.str] = None,
    code_signing_config_arn: typing.Optional[builtins.str] = None,
    code_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dead_letter_queue: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DeadLetterQueueProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_preference: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.DeploymentPreferenceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    environment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionEnvironmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ephemeral_storage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EphemeralStorageProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    event_invoke_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventInvokeConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    file_system_configs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FileSystemConfigProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    function_name: typing.Optional[builtins.str] = None,
    function_url_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.FunctionUrlConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    handler: typing.Optional[builtins.str] = None,
    image_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ImageConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    image_uri: typing.Optional[builtins.str] = None,
    inline_code: typing.Optional[builtins.str] = None,
    kms_key_arn: typing.Optional[builtins.str] = None,
    layers: typing.Optional[typing.Sequence[builtins.str]] = None,
    memory_size: typing.Optional[jsii.Number] = None,
    package_type: typing.Optional[builtins.str] = None,
    permissions_boundary: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnFunction.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnFunction.SAMPolicyTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    provisioned_concurrency_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.ProvisionedConcurrencyConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    reserved_concurrent_executions: typing.Optional[jsii.Number] = None,
    role: typing.Optional[builtins.str] = None,
    runtime: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    timeout: typing.Optional[jsii.Number] = None,
    tracing: typing.Optional[builtins.str] = None,
    version_description: typing.Optional[builtins.str] = None,
    vpc_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFunction.VpcConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2810a638ba3e7320fe893fabc5f6e87ff6c30d560aa983c6a0d6c0f8bf36db24(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.AccessLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.HttpApiAuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cors_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, typing.Union[CfnHttpApi.CorsConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_body: typing.Any = None,
    definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnHttpApi.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.HttpApiDomainConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stage_name: typing.Optional[builtins.str] = None,
    stage_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4f3553a6c850079b893b4af3eba9a2e875d8f7a2f7810fc1d60e2664a2a3bb7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e64eb42bd5b3ff30eb1371e2bbc5bf92a3972db3b40c6c801031d7f11537292a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a42a2744dc641266e3d37b5f146f6af992595ec5ba766b45574ea243aa6fc44(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.AccessLogSettingProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d554bf4285c5e79b485d5399187d984c4db50ac590f443a59fab5686f8a5f98(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.HttpApiAuthProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d80d30c6061e0bc43c731aed2d30d2e16c6817cc38f17f6e31e265dcb4ace5d(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, CfnHttpApi.CorsConfigurationObjectProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c79a8422ac135ae14261211b8dbc3a6cff2c1cd4dfd873119c1ea5a819c7f35(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.RouteSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64a7cbe0232a4687fbe5d51da21fce7dd6fa5366be5dc78ecebd805606154fa9(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad95de74fe527265b62ef85880e9cbbac95b824a1f02495ff12728a9388bcb2(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnHttpApi.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2eaf9aeb8e4a3d3f2c267ba77886e61932ef901479c7475a9c8aea00f009a8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35d352404c375b1dfad345ab43624def545633ffca3918ffbb28046ee14d7978(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e942057fdfda6966ac2fede8944ab9cb3e8bf62cbe0e8dd26293e1004dbebbc4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.HttpApiDomainConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2409f872afa25b367ac77a9bf7ff8c646989e8ed593046716279b7f551051e90(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5197dd6c00fdbddd6b9b3cd699f235d4b1e49fe164b78213b9c4731c95d89470(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHttpApi.RouteSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__690006efe3a8bbd86d333485a6f43ce5a5088b2ade6688f66fa4ed3f2910fd7b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__449af0a02d8005f7a293a627e1cb45ddbc2347c0cd6d00355c6149e405bd71de(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e1532eb045406e1f0c887e9f0288aa942ba65703b7281fd270e9ce1d05639ac2(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396e25c7a235a0fd1fc98c660894c2403ae81136868a6928b6ac54684b38aba2(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92ebf64195227f64e22824cc3c2e16b820997afaf22279f214e4be9d2e5aeef7(
    *,
    allow_credentials: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    allow_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    allow_methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    allow_origins: typing.Optional[typing.Sequence[builtins.str]] = None,
    expose_headers: typing.Optional[typing.Sequence[builtins.str]] = None,
    max_age: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ac54b5b9b26f08c57fcf9efe33403e1ea8d4e4dbeb2436611dccb3a0e037587(
    *,
    authorizers: typing.Any = None,
    default_authorizer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__668063eec4c8cd3e6e97d6a394cfeabd05caf1022045642b40cdb7058f97c736(
    *,
    certificate_arn: builtins.str,
    domain_name: builtins.str,
    base_path: typing.Optional[builtins.str] = None,
    endpoint_configuration: typing.Optional[builtins.str] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.MutualTlsAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    route53: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.Route53ConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3ec0bc1b40dd4e0ee4569d04749d979c1acb5d1b78ef3f4d4293e1d362d289(
    *,
    truststore_uri: typing.Optional[builtins.str] = None,
    truststore_version: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2b137bd750a023ee9520050e4d7a987f36176f815267ef87f09c8c01fe6cbf4b(
    *,
    distributed_domain_name: typing.Optional[builtins.str] = None,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    ip_v6: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__38d112cd2b0f8f8b8b5bc3ed66336d958faca3358a97bd9430a8abe1f79d0b8b(
    *,
    data_trace_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    detailed_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    throttling_burst_limit: typing.Optional[jsii.Number] = None,
    throttling_rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74ce10b0d8c46201b88b9b0a1c3fb634f855f8d93c63ea0589504071aa7940d5(
    *,
    bucket: builtins.str,
    key: builtins.str,
    version: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fee3d57c5905e9ae9b8f419c1e059cc2543719f1378802233950cf6fd8455b0(
    *,
    access_log_setting: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.AccessLogSettingProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auth: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.HttpApiAuthProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cors_configuration: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b, typing.Union[CfnHttpApi.CorsConfigurationObjectProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    definition_body: typing.Any = None,
    definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnHttpApi.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    domain: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.HttpApiDomainConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHttpApi.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stage_name: typing.Optional[builtins.str] = None,
    stage_variables: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d4f065acd39501197153b2ca3e032a641ca99d4d20a65016ce46a93cd18e68dc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    compatible_runtimes: typing.Optional[typing.Sequence[builtins.str]] = None,
    content_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnLayerVersion.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    layer_name: typing.Optional[builtins.str] = None,
    license_info: typing.Optional[builtins.str] = None,
    retention_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d10b12c36b6dac762ac917c78dfa05198c3664b77c0fd3af72c71075106d3fb8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad5410fd56404e482d520099d0db7e08bd17f33b2168a1d37d2faaf71b8444f2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__093cbf32daac268eebbcff5baa4f5e4ae65820ddbf5516ed189eebfc8c39f4f5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22130e3d78e15600d2b76b39b91e86e5c3ab5be2248240792ac38f9e1c8a087f(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnLayerVersion.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__82bec5f248f119695b24893b3c462adcff54ddfb853afc3d225aad7725f573c2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4fae5281fd0168e1c7cdc7e763aafffbffdbd071fcc577f43706e60bf6604cd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2513868291110cf36dfdaefa90e775c1932a45c854cc31fc407238bd5ea1123(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cffb01a050658eae0d54f4418d5c20e121fa2105419dbecb16143d35f51e731c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10e0516e96e125765d789af3e0b7b3712f4bb6dcd1df25ef9f15e0aef059c171(
    *,
    bucket: builtins.str,
    key: builtins.str,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71f32d1d804bafc80050e7d70d1d4cf4812a0a9fa8f770efb7646469f71b29c7(
    *,
    compatible_runtimes: typing.Optional[typing.Sequence[builtins.str]] = None,
    content_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnLayerVersion.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    layer_name: typing.Optional[builtins.str] = None,
    license_info: typing.Optional[builtins.str] = None,
    retention_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49daa8880aa4482f844df7abde9b977c5fd9bef91c748954b20a349543a06826(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    primary_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.PrimaryKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.ProvisionedThroughputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.SSESpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84a15b03f8ad300dc65a45f999aa5db851797b235f56396c0c983ff265e5f1ef(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b2ece540d35a5352688cbd48945936ad81f4feec18d0f4135dcf496ddd58bb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f863d7782f5fdb473e90c677b8c1346a76510547ebee96393b5c04f2b49e1bf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.PrimaryKeyProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94e6b5aa5c341686833a2e2528d8fd9aab8a6e34492f10ec6af593470fd29e46(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.ProvisionedThroughputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03fe1c6d28860594a6ed36eea11303eb5c04ccc3a46d405f6b9583834287d176(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnSimpleTable.SSESpecificationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8087284d8493b47700bc6e58124e49aceac5573dff0a7a9506a229b85c9ac57(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d35381b92f1441a306a58be248d694e2e46740981b8c39578f6894a945658ed(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be45ebf18bd2f3b3fe8e6d7df7f64c64d5e0c8b7bcb36b2e7e1c113748de9b74(
    *,
    type: builtins.str,
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__487d0524c5037b22c73aabd8a4b7e2dabf1f5ac6c75c09973275c283ade8ceef(
    *,
    write_capacity_units: jsii.Number,
    read_capacity_units: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7477a7138a2224049d36e777df52e78339ec289222e92cb6a4dcb006f978dbfe(
    *,
    sse_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__598a09546c8d488353c6a28e36199c3a64135f51ecbcebfaab1a6094ceadba3b(
    *,
    primary_key: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.PrimaryKeyProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    provisioned_throughput: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.ProvisionedThroughputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sse_specification: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnSimpleTable.SSESpecificationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    table_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa34f84b79e27e3369f06403c6b18551d70f35e4a3b615bb7cd7c7098379784b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    definition: typing.Any = None,
    definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    permissions_boundaries: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnStateMachine.SAMPolicyTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    role: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tracing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.TracingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0f447e7e1726ed05f7b3b1f0b0baee4f78b65aedfab90cf94f7a932b53ebd20(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8838b73bfb182cefd4b4952770146574fcbb71987f2ac5837f5c339109555e61(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d3d4f6819243ae5cfa1d9d6defa295a3b23790f17ebd02c4d51d355d543406b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5775a6876026b1a8c899a35d8111a4a33d5e70eba087059cf927fee69bfcad24(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ac29b6e0fb8782fe04c91e9d376d5ece3d1cf8f5986daeec1b67d525f715aee(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.S3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c69f012e3879a5483e31f6e7d98193cf937b522d1e5fc4155f1ace6557abe68a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnStateMachine.EventSourceProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bd2eec7384b45fa445ff5df87e1ec967ddba4c029ebdf2318c8153ffda4b5d9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.LoggingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5550fb2235bd7489d45f17c70c50139dda815ee3a13d3c2d734e5b903ab4cf8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2aaa917b28fe4e0652ce7a6a1728ecade86d1885c3d308a39e942d6db4e60f14(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75f2dd4ecaf463e4efaeb629364956c57cab27cb413f89bd7db13d284395bac4(
    value: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.IAMPolicyDocumentProperty, typing.List[typing.Union[builtins.str, _IResolvable_da3f097b, CfnStateMachine.IAMPolicyDocumentProperty, CfnStateMachine.SAMPolicyTemplateProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f7e9ebff859a9ffc3340242f19d27c150cdf6585b4b792af885c5342f9331af2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__565feae73000a6262db11dd021fb78acbb7d88ef7985a3cb3c253bb8eed469aa(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8388e699502b5c0e2cfd9cce3567a56b150d0ef870feb0fa36e24467ee7fd59f(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStateMachine.TracingConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d50f330540a6c9c0587734dc19098ad7a915876885f3320395fd2f25f92ce666(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36a9790bf179dc695340e1ceefa5ddcd4bcf297927ed7bfe0ad828ef0b7e9165(
    *,
    method: builtins.str,
    path: builtins.str,
    rest_api_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3043510f3e010c02b7e6d61039b56a09a5cc20da321879a3a1dd807d57236bf3(
    *,
    pattern: typing.Any,
    event_bus_name: typing.Optional[builtins.str] = None,
    input: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1b7ec34ef3cd6ce67421530c570c208c6db5b7e85ef74cdc95aae9ebc0cf925(
    *,
    log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c69530dd6f9c5f0c469af173c6c859df452b5c7d088a25087060787de43035bf(
    *,
    pattern: typing.Any,
    event_bus_name: typing.Optional[builtins.str] = None,
    input: typing.Optional[builtins.str] = None,
    input_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e48d983a36222c7edc08f990a77627e82bb5f349be43393cd36983084cc65baf(
    *,
    properties: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.ApiEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnStateMachine.CloudWatchEventEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnStateMachine.EventBridgeRuleEventProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnStateMachine.ScheduleEventProperty, typing.Dict[builtins.str, typing.Any]]],
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d2624ceb5c7626932a2d529134a4d68711bdd820bbbf14ef54bf9e0c4b85e69b(
    *,
    function_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6f663f1c2d20d6ad14f635cbaa2dae4bcb9499a11369ec11b26762e61633406(
    *,
    statement: typing.Any,
    version: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce735dd8db89ab446699c88f1f4e17c39b2b63345abe0a0ecb7fe6f180c708a(
    *,
    cloud_watch_logs_log_group: typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.CloudWatchLogsLogGroupProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bc54f834d8e55c057a6bcfa087f768484ceb97f5fde3f7f8c0296f718a629c2(
    *,
    destinations: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LogDestinationProperty, typing.Dict[builtins.str, typing.Any]]]]],
    include_execution_data: typing.Union[builtins.bool, _IResolvable_da3f097b],
    level: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__934f7db3bc14294d26fb4899060ef54bc5d08fdd5ba17db2a66d7c6a280caf19(
    *,
    bucket: builtins.str,
    key: builtins.str,
    version: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__635d502c9699a6c52eb9e5f1681c94fe4b561fc47930fb2c9289a37d74161c1f(
    *,
    lambda_invoke_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.FunctionSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    step_functions_execution_policy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.StateMachineSAMPTProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6b747b0481f1b704b7ab46bc6bcea38b37b4c026f34956aadf2b2701d277561a(
    *,
    schedule: builtins.str,
    input: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ef1508a492222432242a9718c81cccbfe38b86b513c9f606ee3bbc38080c83(
    *,
    state_machine_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8568d1e5362e81260a69221e107002da0809dc2714f5960aaa894d488ddaa3db(
    *,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__505a369e8f3bf625077dedf7f13099c6e0c8e2c05182396505111670528d74d7(
    *,
    definition: typing.Any = None,
    definition_substitutions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, builtins.str]]] = None,
    definition_uri: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.S3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    events: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.EventSourceProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    logging: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.LoggingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    permissions_boundaries: typing.Optional[builtins.str] = None,
    policies: typing.Optional[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Sequence[typing.Union[builtins.str, _IResolvable_da3f097b, typing.Union[CfnStateMachine.IAMPolicyDocumentProperty, typing.Dict[builtins.str, typing.Any]], typing.Union[CfnStateMachine.SAMPolicyTemplateProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    role: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    tracing: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStateMachine.TracingConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
