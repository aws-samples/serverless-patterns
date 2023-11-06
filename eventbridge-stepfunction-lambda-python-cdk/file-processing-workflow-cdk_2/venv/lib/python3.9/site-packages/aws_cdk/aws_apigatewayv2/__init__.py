'''
# AWS::ApiGatewayV2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_apigatewayv2 as apigateway
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for ApiGatewayV2 construct libraries](https://constructs.dev/search?q=apigatewayv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::ApiGatewayV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.html) directly.

> An experimental construct library for this service is available in preview. Since it is not stable yet, it is distributed
> as a separate package so that you can pin its version independently of the rest of the CDK. See the package:
>
> <span class="package-reference">@aws-cdk/aws-apigatewayv2-alpha</span>

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::ApiGatewayV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_ApiGatewayV2.html).

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
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnApi(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApi",
):
    '''The ``AWS::ApiGatewayV2::Api`` resource creates an API.

    WebSocket APIs and HTTP APIs are supported. For more information about WebSocket APIs, see `About WebSocket APIs in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-overview.html>`_ in the *API Gateway Developer Guide* . For more information about HTTP APIs, see `HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api.html>`_ in the *API Gateway Developer Guide.*

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # body: Any
        
        cfn_api = apigatewayv2.CfnApi(self, "MyCfnApi",
            api_key_selection_expression="apiKeySelectionExpression",
            base_path="basePath",
            body=body,
            body_s3_location=apigatewayv2.CfnApi.BodyS3LocationProperty(
                bucket="bucket",
                etag="etag",
                key="key",
                version="version"
            ),
            cors_configuration=apigatewayv2.CfnApi.CorsProperty(
                allow_credentials=False,
                allow_headers=["allowHeaders"],
                allow_methods=["allowMethods"],
                allow_origins=["allowOrigins"],
                expose_headers=["exposeHeaders"],
                max_age=123
            ),
            credentials_arn="credentialsArn",
            description="description",
            disable_execute_api_endpoint=False,
            disable_schema_validation=False,
            fail_on_warnings=False,
            name="name",
            protocol_type="protocolType",
            route_key="routeKey",
            route_selection_expression="routeSelectionExpression",
            tags={
                "tags_key": "tags"
            },
            target="target",
            version="version"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_key_selection_expression: typing.Optional[builtins.str] = None,
        base_path: typing.Optional[builtins.str] = None,
        body: typing.Any = None,
        body_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.BodyS3LocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cors_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApi.CorsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        credentials_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        disable_schema_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        protocol_type: typing.Optional[builtins.str] = None,
        route_key: typing.Optional[builtins.str] = None,
        route_selection_expression: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_key_selection_expression: An API key selection expression. Supported only for WebSocket APIs. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`_ .
        :param base_path: Specifies how to interpret the base path of the API during import. Valid values are ``ignore`` , ``prepend`` , and ``split`` . The default value is ``ignore`` . To learn more, see `Set the OpenAPI basePath Property <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html>`_ . Supported only for HTTP APIs.
        :param body: The OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location`` . If you specify a ``Body`` or ``BodyS3Location`` , don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route`` . API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.
        :param body_s3_location: The S3 location of an OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location`` . If you specify a ``Body`` or ``BodyS3Location`` , don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route`` . API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.
        :param cors_configuration: A CORS configuration. Supported only for HTTP APIs. See `Configuring CORS <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html>`_ for more information.
        :param credentials_arn: This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify ``arn:aws:iam::*:user/*`` . To use resource-based permissions on supported AWS services, specify ``null`` . Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.
        :param description: The description of the API.
        :param disable_execute_api_endpoint: Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.
        :param disable_schema_validation: Avoid validating models when creating a deployment. Supported only for WebSocket APIs.
        :param fail_on_warnings: Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.
        :param name: The name of the API. Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation`` .
        :param protocol_type: The API protocol. Valid values are ``WEBSOCKET`` or ``HTTP`` . Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation`` .
        :param route_key: This property is part of quick create. If you don't specify a ``routeKey`` , a default route of ``$default`` is created. The ``$default`` route acts as a catch-all for any request made to your API, for a particular stage. The ``$default`` route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.
        :param route_selection_expression: The route selection expression for the API. For HTTP APIs, the ``routeSelectionExpression`` must be ``${request.method} ${request.path}`` . If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.
        :param tags: The collection of tags. Each tag element is associated with a given resource.
        :param target: This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.
        :param version: A version identifier for the API.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1db7633eb849c7234f54cf8f50ef6e4c6273ca1ab60db537f47e511e2240c5b6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiProps(
            api_key_selection_expression=api_key_selection_expression,
            base_path=base_path,
            body=body,
            body_s3_location=body_s3_location,
            cors_configuration=cors_configuration,
            credentials_arn=credentials_arn,
            description=description,
            disable_execute_api_endpoint=disable_execute_api_endpoint,
            disable_schema_validation=disable_schema_validation,
            fail_on_warnings=fail_on_warnings,
            name=name,
            protocol_type=protocol_type,
            route_key=route_key,
            route_selection_expression=route_selection_expression,
            tags=tags,
            target=target,
            version=version,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea567b8b40be10165a36dab66b11588d141fcb6bb04249eea1d0752e699710d4)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d18d8bbf1817171b680c668ba45b7bf21f8602f6a88656a3fcba170987a99efd)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiEndpoint")
    def attr_api_endpoint(self) -> builtins.str:
        '''The default endpoint for an API.

        For example: ``https://abcdef.execute-api.us-west-2.amazonaws.com`` .

        :cloudformationAttribute: ApiEndpoint
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiEndpoint"))

    @builtins.property
    @jsii.member(jsii_name="attrApiId")
    def attr_api_id(self) -> builtins.str:
        '''The API identifier.

        :cloudformationAttribute: ApiId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiId"))

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
    @jsii.member(jsii_name="apiKeySelectionExpression")
    def api_key_selection_expression(self) -> typing.Optional[builtins.str]:
        '''An API key selection expression.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiKeySelectionExpression"))

    @api_key_selection_expression.setter
    def api_key_selection_expression(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f558d38700b12a8436eb254b53f9b036b9dcc79e6b13662d5cc5f734a50cc0e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeySelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="basePath")
    def base_path(self) -> typing.Optional[builtins.str]:
        '''Specifies how to interpret the base path of the API during import.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "basePath"))

    @base_path.setter
    def base_path(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c9c0986fef807a65a36cb9c2c2088cce866089cadbd06372d8e636cee797253)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "basePath", value)

    @builtins.property
    @jsii.member(jsii_name="body")
    def body(self) -> typing.Any:
        '''The OpenAPI definition.'''
        return typing.cast(typing.Any, jsii.get(self, "body"))

    @body.setter
    def body(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b640ee61c5afa6ad142df6ac4f94d2662b22d8db131f7f0bbb9357d1e77d98)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "body", value)

    @builtins.property
    @jsii.member(jsii_name="bodyS3Location")
    def body_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.BodyS3LocationProperty"]]:
        '''The S3 location of an OpenAPI definition.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.BodyS3LocationProperty"]], jsii.get(self, "bodyS3Location"))

    @body_s3_location.setter
    def body_s3_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.BodyS3LocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__461aef5629963bb7b74c508fa030064900f1e11ec3308ed14d0e0125845f569b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bodyS3Location", value)

    @builtins.property
    @jsii.member(jsii_name="corsConfiguration")
    def cors_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.CorsProperty"]]:
        '''A CORS configuration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.CorsProperty"]], jsii.get(self, "corsConfiguration"))

    @cors_configuration.setter
    def cors_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApi.CorsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea01a446f6b48d1d09e26c2d973a367686fc04ba3d8d5922215249b2d34b67eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "corsConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> typing.Optional[builtins.str]:
        '''This property is part of quick create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsArn"))

    @credentials_arn.setter
    def credentials_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd12bd9456ce5e4af4343ebe09227e1fa34692caf0b82db4abd6147ac9f132f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9bc7f78ea01f8843ca5b04055b6b342ad243dd45e7ab88143c592adf5b5a283)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="disableExecuteApiEndpoint")
    def disable_execute_api_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableExecuteApiEndpoint"))

    @disable_execute_api_endpoint.setter
    def disable_execute_api_endpoint(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77d94dbd246367bad1d084b1e206403a882329be7b7bb9331e4bd1fa90ae597a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableExecuteApiEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="disableSchemaValidation")
    def disable_schema_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Avoid validating models when creating a deployment.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "disableSchemaValidation"))

    @disable_schema_validation.setter
    def disable_schema_validation(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c4fafef5608e6998354242dff5cfd6b04966c90f66f2d2737cfed24eb25398a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "disableSchemaValidation", value)

    @builtins.property
    @jsii.member(jsii_name="failOnWarnings")
    def fail_on_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to rollback the API creation when a warning is encountered.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "failOnWarnings"))

    @fail_on_warnings.setter
    def fail_on_warnings(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ce8eb7264be44ff3a6ae79c6be6a193c31eb617518209aeb51c346aac7c5536)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failOnWarnings", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6de2f3d46e4a0275374cdfba39222daec1a50d7516f00756e898551462523fb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="protocolType")
    def protocol_type(self) -> typing.Optional[builtins.str]:
        '''The API protocol.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocolType"))

    @protocol_type.setter
    def protocol_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e57f77aa16016f544c5223d6856ffa749c3e01cee63831813142637d65047878)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocolType", value)

    @builtins.property
    @jsii.member(jsii_name="routeKey")
    def route_key(self) -> typing.Optional[builtins.str]:
        '''This property is part of quick create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeKey"))

    @route_key.setter
    def route_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f1526e8beb3aabccc2d1a4a66b85888cbae9836882586cbc1831cb780485872)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeKey", value)

    @builtins.property
    @jsii.member(jsii_name="routeSelectionExpression")
    def route_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The route selection expression for the API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeSelectionExpression"))

    @route_selection_expression.setter
    def route_selection_expression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ae3d20180c61889cbbc3db2ac94b1665ceb0357e28b396e9eb10b36443cc6d3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The collection of tags.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ade78b4fb0e303cc30b6b8a9298c4758fd1370f3627ea5e37db0fe2e2ce623af)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.Optional[builtins.str]:
        '''This property is part of quick create.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "target"))

    @target.setter
    def target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96f6611a87a6cb532fe3a0a6fda47d8cb668095b5984db628a9a79828ae2b327)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @builtins.property
    @jsii.member(jsii_name="version")
    def version(self) -> typing.Optional[builtins.str]:
        '''A version identifier for the API.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "version"))

    @version.setter
    def version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__122ec616b9f721d7146444333bfc18f20226b393d496105443355c5add69abf9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "version", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApi.BodyS3LocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket": "bucket",
            "etag": "etag",
            "key": "key",
            "version": "version",
        },
    )
    class BodyS3LocationProperty:
        def __init__(
            self,
            *,
            bucket: typing.Optional[builtins.str] = None,
            etag: typing.Optional[builtins.str] = None,
            key: typing.Optional[builtins.str] = None,
            version: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``BodyS3Location`` property specifies an S3 location from which to import an OpenAPI definition.

            Supported only for HTTP APIs.

            :param bucket: The S3 bucket that contains the OpenAPI definition to import. Required if you specify a ``BodyS3Location`` for an API.
            :param etag: The Etag of the S3 object.
            :param key: The key of the S3 object. Required if you specify a ``BodyS3Location`` for an API.
            :param version: The version of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                body_s3_location_property = apigatewayv2.CfnApi.BodyS3LocationProperty(
                    bucket="bucket",
                    etag="etag",
                    key="key",
                    version="version"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__086d4bdce422b6d8380b205644d06b82c6e6ca7cc5c6a6813f2498660cf2e643)
                check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
                check_type(argname="argument etag", value=etag, expected_type=type_hints["etag"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if bucket is not None:
                self._values["bucket"] = bucket
            if etag is not None:
                self._values["etag"] = etag
            if key is not None:
                self._values["key"] = key
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def bucket(self) -> typing.Optional[builtins.str]:
            '''The S3 bucket that contains the OpenAPI definition to import.

            Required if you specify a ``BodyS3Location`` for an API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-bucket
            '''
            result = self._values.get("bucket")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def etag(self) -> typing.Optional[builtins.str]:
            '''The Etag of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-etag
            '''
            result = self._values.get("etag")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The key of the S3 object.

            Required if you specify a ``BodyS3Location`` for an API.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def version(self) -> typing.Optional[builtins.str]:
            '''The version of the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-bodys3location.html#cfn-apigatewayv2-api-bodys3location-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BodyS3LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApi.CorsProperty",
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
    class CorsProperty:
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
            '''The ``Cors`` property specifies a CORS configuration for an API.

            Supported only for HTTP APIs. See `Configuring CORS <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html>`_ for more information.

            :param allow_credentials: Specifies whether credentials are included in the CORS request. Supported only for HTTP APIs.
            :param allow_headers: Represents a collection of allowed headers. Supported only for HTTP APIs.
            :param allow_methods: Represents a collection of allowed HTTP methods. Supported only for HTTP APIs.
            :param allow_origins: Represents a collection of allowed origins. Supported only for HTTP APIs.
            :param expose_headers: Represents a collection of exposed headers. Supported only for HTTP APIs.
            :param max_age: The number of seconds that the browser should cache preflight request results. Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                cors_property = apigatewayv2.CfnApi.CorsProperty(
                    allow_credentials=False,
                    allow_headers=["allowHeaders"],
                    allow_methods=["allowMethods"],
                    allow_origins=["allowOrigins"],
                    expose_headers=["exposeHeaders"],
                    max_age=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6a3791259651e5580c105c2edbd7e61bfe4d9352ce320e2b6cee928ff45f804)
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
            '''Specifies whether credentials are included in the CORS request.

            Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowcredentials
            '''
            result = self._values.get("allow_credentials")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def allow_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents a collection of allowed headers.

            Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowheaders
            '''
            result = self._values.get("allow_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allow_methods(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents a collection of allowed HTTP methods.

            Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-allowmethods
            '''
            result = self._values.get("allow_methods")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def allow_origins(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents a collection of allowed origins.

            Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-alloworigins
            '''
            result = self._values.get("allow_origins")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def expose_headers(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Represents a collection of exposed headers.

            Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-exposeheaders
            '''
            result = self._values.get("expose_headers")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def max_age(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds that the browser should cache preflight request results.

            Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-api-cors.html#cfn-apigatewayv2-api-cors-maxage
            '''
            result = self._values.get("max_age")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CorsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnApiGatewayManagedOverrides(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverrides",
):
    '''The ``AWS::ApiGatewayV2::ApiGatewayManagedOverrides`` resource overrides the default properties of API Gateway-managed resources that are implicitly configured for you when you use quick create.

    When you create an API by using quick create, an ``AWS::ApiGatewayV2::Route`` , ``AWS::ApiGatewayV2::Integration`` , and ``AWS::ApiGatewayV2::Stage`` are created for you and associated with your ``AWS::ApiGatewayV2::Api`` . The ``AWS::ApiGatewayV2::ApiGatewayManagedOverrides`` resource enables you to set, or override the properties of these implicit resources. Supported only for HTTP APIs.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # route_settings: Any
        # stage_variables: Any
        
        cfn_api_gateway_managed_overrides = apigatewayv2.CfnApiGatewayManagedOverrides(self, "MyCfnApiGatewayManagedOverrides",
            api_id="apiId",
        
            # the properties below are optional
            integration=apigatewayv2.CfnApiGatewayManagedOverrides.IntegrationOverridesProperty(
                description="description",
                integration_method="integrationMethod",
                payload_format_version="payloadFormatVersion",
                timeout_in_millis=123
            ),
            route=apigatewayv2.CfnApiGatewayManagedOverrides.RouteOverridesProperty(
                authorization_scopes=["authorizationScopes"],
                authorization_type="authorizationType",
                authorizer_id="authorizerId",
                operation_name="operationName",
                target="target"
            ),
            stage=apigatewayv2.CfnApiGatewayManagedOverrides.StageOverridesProperty(
                access_log_settings=apigatewayv2.CfnApiGatewayManagedOverrides.AccessLogSettingsProperty(
                    destination_arn="destinationArn",
                    format="format"
                ),
                auto_deploy=False,
                default_route_settings=apigatewayv2.CfnApiGatewayManagedOverrides.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                ),
                description="description",
                route_settings=route_settings,
                stage_variables=stage_variables
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        integration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApiGatewayManagedOverrides.IntegrationOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApiGatewayManagedOverrides.RouteOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        stage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApiGatewayManagedOverrides.StageOverridesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The ID of the API for which to override the configuration of API Gateway-managed resources.
        :param integration: Overrides the integration configuration for an API Gateway-managed integration.
        :param route: Overrides the route configuration for an API Gateway-managed route.
        :param stage: Overrides the stage configuration for an API Gateway-managed stage.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3082a35122d304d1e6cb138bd4f4ff647c08d9345fc0680734a094f650214a9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiGatewayManagedOverridesProps(
            api_id=api_id, integration=integration, route=route, stage=stage
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f546675cd72b747ba4414186c0b784c272bc9b2cc62f6d8527feb95ad0069a7d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__074d92384425f99a1b1f84fd40ccd33b5d3ff6d021bbdf363f73d6c45065193c)
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
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The ID of the API for which to override the configuration of API Gateway-managed resources.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a21a84b347534934baae96f0d955d7cb2a425b3a984d9cccb6b9853851a463)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="integration")
    def integration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.IntegrationOverridesProperty"]]:
        '''Overrides the integration configuration for an API Gateway-managed integration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.IntegrationOverridesProperty"]], jsii.get(self, "integration"))

    @integration.setter
    def integration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.IntegrationOverridesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6e8f6e317166c4e7072ff432e3e7eccfb8b95c41ae3624cbc1df56dfb741e92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integration", value)

    @builtins.property
    @jsii.member(jsii_name="route")
    def route(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.RouteOverridesProperty"]]:
        '''Overrides the route configuration for an API Gateway-managed route.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.RouteOverridesProperty"]], jsii.get(self, "route"))

    @route.setter
    def route(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.RouteOverridesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80d7eeb3e44a467671100a29546de04d5d43029de65fbf94591ab14fffad1c5c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "route", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.StageOverridesProperty"]]:
        '''Overrides the stage configuration for an API Gateway-managed stage.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.StageOverridesProperty"]], jsii.get(self, "stage"))

    @stage.setter
    def stage(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.StageOverridesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b463a4abcee245efa2b5f8331eb964b48378707ae4929bfd7871d5ecef589ae8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverrides.AccessLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn", "format": "format"},
    )
    class AccessLogSettingsProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``AccessLogSettings`` property overrides the access log settings for an API Gateway-managed stage.

            :param destination_arn: The ARN of the CloudWatch Logs log group to receive access logs.
            :param format: A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                access_log_settings_property = apigatewayv2.CfnApiGatewayManagedOverrides.AccessLogSettingsProperty(
                    destination_arn="destinationArn",
                    format="format"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f3107ba375d42b235637a85ea013e8de6b4867611024bc71e2c59db92941dcc1)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn
            if format is not None:
                self._values["format"] = format

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch Logs log group to receive access logs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''A single line format of the access logs of data, as specified by selected $context variables.

            The format must include at least $context.requestId.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-accesslogsettings-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverrides.IntegrationOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "description": "description",
            "integration_method": "integrationMethod",
            "payload_format_version": "payloadFormatVersion",
            "timeout_in_millis": "timeoutInMillis",
        },
    )
    class IntegrationOverridesProperty:
        def __init__(
            self,
            *,
            description: typing.Optional[builtins.str] = None,
            integration_method: typing.Optional[builtins.str] = None,
            payload_format_version: typing.Optional[builtins.str] = None,
            timeout_in_millis: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''The ``IntegrationOverrides`` property overrides the integration settings for an API Gateway-managed integration.

            If you remove this property, API Gateway restores the default values.

            :param description: The description of the integration.
            :param integration_method: Specifies the integration's HTTP method type.
            :param payload_format_version: Specifies the format of the payload sent to an integration. Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are ``1.0`` and ``2.0`` . For all other integrations, ``1.0`` is the only supported value. To learn more, see `Working with AWS Lambda proxy integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html>`_ .
            :param timeout_in_millis: Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                integration_overrides_property = apigatewayv2.CfnApiGatewayManagedOverrides.IntegrationOverridesProperty(
                    description="description",
                    integration_method="integrationMethod",
                    payload_format_version="payloadFormatVersion",
                    timeout_in_millis=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__52af4fb74c40ef1f2f6be4941e114a9dee678620d84a75a3d412e8f19efd0a5e)
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument integration_method", value=integration_method, expected_type=type_hints["integration_method"])
                check_type(argname="argument payload_format_version", value=payload_format_version, expected_type=type_hints["payload_format_version"])
                check_type(argname="argument timeout_in_millis", value=timeout_in_millis, expected_type=type_hints["timeout_in_millis"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if description is not None:
                self._values["description"] = description
            if integration_method is not None:
                self._values["integration_method"] = integration_method
            if payload_format_version is not None:
                self._values["payload_format_version"] = payload_format_version
            if timeout_in_millis is not None:
                self._values["timeout_in_millis"] = timeout_in_millis

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description of the integration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def integration_method(self) -> typing.Optional[builtins.str]:
            '''Specifies the integration's HTTP method type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-integrationmethod
            '''
            result = self._values.get("integration_method")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def payload_format_version(self) -> typing.Optional[builtins.str]:
            '''Specifies the format of the payload sent to an integration.

            Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are ``1.0`` and ``2.0`` . For all other integrations, ``1.0`` is the only supported value. To learn more, see `Working with AWS Lambda proxy integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-payloadformatversion
            '''
            result = self._values.get("payload_format_version")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
            '''Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs.

            The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integrationoverrides-timeoutinmillis
            '''
            result = self._values.get("timeout_in_millis")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IntegrationOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverrides.RouteOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "authorization_scopes": "authorizationScopes",
            "authorization_type": "authorizationType",
            "authorizer_id": "authorizerId",
            "operation_name": "operationName",
            "target": "target",
        },
    )
    class RouteOverridesProperty:
        def __init__(
            self,
            *,
            authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
            authorization_type: typing.Optional[builtins.str] = None,
            authorizer_id: typing.Optional[builtins.str] = None,
            operation_name: typing.Optional[builtins.str] = None,
            target: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``RouteOverrides`` property overrides the route configuration for an API Gateway-managed route.

            If you remove this property, API Gateway restores the default values.

            :param authorization_scopes: The authorization scopes supported by this route.
            :param authorization_type: The authorization type for the route. To learn more, see `AuthorizationType <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype>`_ .
            :param authorizer_id: The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
            :param operation_name: The operation name for the route.
            :param target: For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                route_overrides_property = apigatewayv2.CfnApiGatewayManagedOverrides.RouteOverridesProperty(
                    authorization_scopes=["authorizationScopes"],
                    authorization_type="authorizationType",
                    authorizer_id="authorizerId",
                    operation_name="operationName",
                    target="target"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b352b9e190a07978f5f79a0a25e0674fec09f30874ec1c2794f521e6c482f06)
                check_type(argname="argument authorization_scopes", value=authorization_scopes, expected_type=type_hints["authorization_scopes"])
                check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
                check_type(argname="argument authorizer_id", value=authorizer_id, expected_type=type_hints["authorizer_id"])
                check_type(argname="argument operation_name", value=operation_name, expected_type=type_hints["operation_name"])
                check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if authorization_scopes is not None:
                self._values["authorization_scopes"] = authorization_scopes
            if authorization_type is not None:
                self._values["authorization_type"] = authorization_type
            if authorizer_id is not None:
                self._values["authorizer_id"] = authorizer_id
            if operation_name is not None:
                self._values["operation_name"] = operation_name
            if target is not None:
                self._values["target"] = target

        @builtins.property
        def authorization_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The authorization scopes supported by this route.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationscopes
            '''
            result = self._values.get("authorization_scopes")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def authorization_type(self) -> typing.Optional[builtins.str]:
            '''The authorization type for the route.

            To learn more, see `AuthorizationType <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizationtype
            '''
            result = self._values.get("authorization_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def authorizer_id(self) -> typing.Optional[builtins.str]:
            '''The identifier of the ``Authorizer`` resource to be associated with this route.

            The authorizer identifier is generated by API Gateway when you created the authorizer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-authorizerid
            '''
            result = self._values.get("authorizer_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def operation_name(self) -> typing.Optional[builtins.str]:
            '''The operation name for the route.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-operationname
            '''
            result = self._values.get("operation_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def target(self) -> typing.Optional[builtins.str]:
            '''For HTTP integrations, specify a fully qualified URL.

            For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routeoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routeoverrides-target
            '''
            result = self._values.get("target")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RouteOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverrides.RouteSettingsProperty",
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
            '''The ``RouteSettings`` property overrides the route settings for an API Gateway-managed route.

            :param data_trace_enabled: Specifies whether ( ``true`` ) or not ( ``false`` ) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.
            :param detailed_metrics_enabled: Specifies whether detailed metrics are enabled.
            :param logging_level: Specifies the logging level for this route: ``INFO`` , ``ERROR`` , or ``OFF`` . This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.
            :param throttling_burst_limit: Specifies the throttling burst limit.
            :param throttling_rate_limit: Specifies the throttling rate limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                route_settings_property = apigatewayv2.CfnApiGatewayManagedOverrides.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a3c274518dfd0a38d624673e2404ec404bd69957d2d008f63dd8c49507e3bdd3)
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
            '''Specifies whether ( ``true`` ) or not ( ``false`` ) data trace logging is enabled for this route.

            This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-datatraceenabled
            '''
            result = self._values.get("data_trace_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def detailed_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether detailed metrics are enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-detailedmetricsenabled
            '''
            result = self._values.get("detailed_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def logging_level(self) -> typing.Optional[builtins.str]:
            '''Specifies the logging level for this route: ``INFO`` , ``ERROR`` , or ``OFF`` .

            This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-logginglevel
            '''
            result = self._values.get("logging_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
            '''Specifies the throttling burst limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingburstlimit
            '''
            result = self._values.get("throttling_burst_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
            '''Specifies the throttling rate limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-routesettings.html#cfn-apigatewayv2-apigatewaymanagedoverrides-routesettings-throttlingratelimit
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
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverrides.StageOverridesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "access_log_settings": "accessLogSettings",
            "auto_deploy": "autoDeploy",
            "default_route_settings": "defaultRouteSettings",
            "description": "description",
            "route_settings": "routeSettings",
            "stage_variables": "stageVariables",
        },
    )
    class StageOverridesProperty:
        def __init__(
            self,
            *,
            access_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApiGatewayManagedOverrides.AccessLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            auto_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApiGatewayManagedOverrides.RouteSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            description: typing.Optional[builtins.str] = None,
            route_settings: typing.Any = None,
            stage_variables: typing.Any = None,
        ) -> None:
            '''The ``StageOverrides`` property overrides the stage configuration for an API Gateway-managed stage.

            If you remove this property, API Gateway restores the default values.

            :param access_log_settings: Settings for logging access in a stage.
            :param auto_deploy: Specifies whether updates to an API automatically trigger a new deployment. The default value is ``true`` .
            :param default_route_settings: The default route settings for the stage.
            :param description: The description for the API stage.
            :param route_settings: Route settings for the stage.
            :param stage_variables: A map that defines the stage variables for a ``Stage`` . Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                # route_settings: Any
                # stage_variables: Any
                
                stage_overrides_property = apigatewayv2.CfnApiGatewayManagedOverrides.StageOverridesProperty(
                    access_log_settings=apigatewayv2.CfnApiGatewayManagedOverrides.AccessLogSettingsProperty(
                        destination_arn="destinationArn",
                        format="format"
                    ),
                    auto_deploy=False,
                    default_route_settings=apigatewayv2.CfnApiGatewayManagedOverrides.RouteSettingsProperty(
                        data_trace_enabled=False,
                        detailed_metrics_enabled=False,
                        logging_level="loggingLevel",
                        throttling_burst_limit=123,
                        throttling_rate_limit=123
                    ),
                    description="description",
                    route_settings=route_settings,
                    stage_variables=stage_variables
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea132c6be8d923c2d66569aa4c4173cf533b8a8f3c8959eb63a39674fed009f3)
                check_type(argname="argument access_log_settings", value=access_log_settings, expected_type=type_hints["access_log_settings"])
                check_type(argname="argument auto_deploy", value=auto_deploy, expected_type=type_hints["auto_deploy"])
                check_type(argname="argument default_route_settings", value=default_route_settings, expected_type=type_hints["default_route_settings"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument route_settings", value=route_settings, expected_type=type_hints["route_settings"])
                check_type(argname="argument stage_variables", value=stage_variables, expected_type=type_hints["stage_variables"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if access_log_settings is not None:
                self._values["access_log_settings"] = access_log_settings
            if auto_deploy is not None:
                self._values["auto_deploy"] = auto_deploy
            if default_route_settings is not None:
                self._values["default_route_settings"] = default_route_settings
            if description is not None:
                self._values["description"] = description
            if route_settings is not None:
                self._values["route_settings"] = route_settings
            if stage_variables is not None:
                self._values["stage_variables"] = stage_variables

        @builtins.property
        def access_log_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.AccessLogSettingsProperty"]]:
            '''Settings for logging access in a stage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-accesslogsettings
            '''
            result = self._values.get("access_log_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.AccessLogSettingsProperty"]], result)

        @builtins.property
        def auto_deploy(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether updates to an API automatically trigger a new deployment.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-autodeploy
            '''
            result = self._values.get("auto_deploy")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def default_route_settings(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.RouteSettingsProperty"]]:
            '''The default route settings for the stage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-defaultroutesettings
            '''
            result = self._values.get("default_route_settings")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApiGatewayManagedOverrides.RouteSettingsProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''The description for the API stage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def route_settings(self) -> typing.Any:
            '''Route settings for the stage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-routesettings
            '''
            result = self._values.get("route_settings")
            return typing.cast(typing.Any, result)

        @builtins.property
        def stage_variables(self) -> typing.Any:
            '''A map that defines the stage variables for a ``Stage`` .

            Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-apigatewaymanagedoverrides-stageoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stageoverrides-stagevariables
            '''
            result = self._values.get("stage_variables")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StageOverridesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiGatewayManagedOverridesProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "integration": "integration",
        "route": "route",
        "stage": "stage",
    },
)
class CfnApiGatewayManagedOverridesProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        integration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.IntegrationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.RouteOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        stage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.StageOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApiGatewayManagedOverrides``.

        :param api_id: The ID of the API for which to override the configuration of API Gateway-managed resources.
        :param integration: Overrides the integration configuration for an API Gateway-managed integration.
        :param route: Overrides the route configuration for an API Gateway-managed route.
        :param stage: Overrides the stage configuration for an API Gateway-managed stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # route_settings: Any
            # stage_variables: Any
            
            cfn_api_gateway_managed_overrides_props = apigatewayv2.CfnApiGatewayManagedOverridesProps(
                api_id="apiId",
            
                # the properties below are optional
                integration=apigatewayv2.CfnApiGatewayManagedOverrides.IntegrationOverridesProperty(
                    description="description",
                    integration_method="integrationMethod",
                    payload_format_version="payloadFormatVersion",
                    timeout_in_millis=123
                ),
                route=apigatewayv2.CfnApiGatewayManagedOverrides.RouteOverridesProperty(
                    authorization_scopes=["authorizationScopes"],
                    authorization_type="authorizationType",
                    authorizer_id="authorizerId",
                    operation_name="operationName",
                    target="target"
                ),
                stage=apigatewayv2.CfnApiGatewayManagedOverrides.StageOverridesProperty(
                    access_log_settings=apigatewayv2.CfnApiGatewayManagedOverrides.AccessLogSettingsProperty(
                        destination_arn="destinationArn",
                        format="format"
                    ),
                    auto_deploy=False,
                    default_route_settings=apigatewayv2.CfnApiGatewayManagedOverrides.RouteSettingsProperty(
                        data_trace_enabled=False,
                        detailed_metrics_enabled=False,
                        logging_level="loggingLevel",
                        throttling_burst_limit=123,
                        throttling_rate_limit=123
                    ),
                    description="description",
                    route_settings=route_settings,
                    stage_variables=stage_variables
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__40b87ae4ac983962d1367d2c0b468ff7d196133f8fa354542fbc9cb69df972c1)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument integration", value=integration, expected_type=type_hints["integration"])
            check_type(argname="argument route", value=route, expected_type=type_hints["route"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }
        if integration is not None:
            self._values["integration"] = integration
        if route is not None:
            self._values["route"] = route
        if stage is not None:
            self._values["stage"] = stage

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The ID of the API for which to override the configuration of API Gateway-managed resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.IntegrationOverridesProperty]]:
        '''Overrides the integration configuration for an API Gateway-managed integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-integration
        '''
        result = self._values.get("integration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.IntegrationOverridesProperty]], result)

    @builtins.property
    def route(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.RouteOverridesProperty]]:
        '''Overrides the route configuration for an API Gateway-managed route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-route
        '''
        result = self._values.get("route")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.RouteOverridesProperty]], result)

    @builtins.property
    def stage(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.StageOverridesProperty]]:
        '''Overrides the stage configuration for an API Gateway-managed stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apigatewaymanagedoverrides.html#cfn-apigatewayv2-apigatewaymanagedoverrides-stage
        '''
        result = self._values.get("stage")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.StageOverridesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiGatewayManagedOverridesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnApiMapping(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiMapping",
):
    '''The ``AWS::ApiGatewayV2::ApiMapping`` resource contains an API mapping.

    An API mapping relates a path of your custom domain name to a stage of your API. A custom domain name can have multiple API mappings, but the paths can't overlap. A custom domain can map only to APIs of the same protocol type. For more information, see `CreateApiMapping <https://docs.aws.amazon.com/apigatewayv2/latest/api-reference/domainnames-domainname-apimappings.html#CreateApiMapping>`_ in the *Amazon API Gateway V2 API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        cfn_api_mapping = apigatewayv2.CfnApiMapping(self, "MyCfnApiMapping",
            api_id="apiId",
            domain_name="domainName",
            stage="stage",
        
            # the properties below are optional
            api_mapping_key="apiMappingKey"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        domain_name: builtins.str,
        stage: builtins.str,
        api_mapping_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The identifier of the API.
        :param domain_name: The domain name.
        :param stage: The API stage.
        :param api_mapping_key: The API mapping key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c7941c91626bf9a2ba9b280f45933deda0d260740aa53002a46b6ab82a16ee7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApiMappingProps(
            api_id=api_id,
            domain_name=domain_name,
            stage=stage,
            api_mapping_key=api_mapping_key,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c82011934bb943ac56e9ca15a3fe2a18c216660e1756e95e52e27f231dec231)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1ae4463f7feed53f0bfce2bb7e7a44ca8cb4a75981a848eb321c6769c45e5ce5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiMappingId")
    def attr_api_mapping_id(self) -> builtins.str:
        '''The API mapping resource ID.

        :cloudformationAttribute: ApiMappingId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiMappingId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The identifier of the API.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16b4567f90930e8b6066ebfc2754fe20fbf1ac5584fafac3590ca91aa888c9f8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29763e906ad99eaf78d0a9dee6a0499887496126efb3aa75ef00df49524186fb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="stage")
    def stage(self) -> builtins.str:
        '''The API stage.'''
        return typing.cast(builtins.str, jsii.get(self, "stage"))

    @stage.setter
    def stage(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__795325b53a59ad485c851fa2a6b00f03e881044ac7a59f18df5adbe25da80c91)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stage", value)

    @builtins.property
    @jsii.member(jsii_name="apiMappingKey")
    def api_mapping_key(self) -> typing.Optional[builtins.str]:
        '''The API mapping key.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "apiMappingKey"))

    @api_mapping_key.setter
    def api_mapping_key(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cff63da4774ec3927c6108752f4d513d841d877a4cb52ccfe4e4a61e344e1424)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiMappingKey", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiMappingProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "domain_name": "domainName",
        "stage": "stage",
        "api_mapping_key": "apiMappingKey",
    },
)
class CfnApiMappingProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        domain_name: builtins.str,
        stage: builtins.str,
        api_mapping_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApiMapping``.

        :param api_id: The identifier of the API.
        :param domain_name: The domain name.
        :param stage: The API stage.
        :param api_mapping_key: The API mapping key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            cfn_api_mapping_props = apigatewayv2.CfnApiMappingProps(
                api_id="apiId",
                domain_name="domainName",
                stage="stage",
            
                # the properties below are optional
                api_mapping_key="apiMappingKey"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__35fae8a54109857e64a283a909a1a23ceda5ded3bf38ca4bce78df48ed736863)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument stage", value=stage, expected_type=type_hints["stage"])
            check_type(argname="argument api_mapping_key", value=api_mapping_key, expected_type=type_hints["api_mapping_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "domain_name": domain_name,
            "stage": stage,
        }
        if api_mapping_key is not None:
            self._values["api_mapping_key"] = api_mapping_key

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The identifier of the API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stage(self) -> builtins.str:
        '''The API stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-stage
        '''
        result = self._values.get("stage")
        assert result is not None, "Required property 'stage' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_mapping_key(self) -> typing.Optional[builtins.str]:
        '''The API mapping key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-apimapping.html#cfn-apigatewayv2-apimapping-apimappingkey
        '''
        result = self._values.get("api_mapping_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiMappingProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnApiProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_key_selection_expression": "apiKeySelectionExpression",
        "base_path": "basePath",
        "body": "body",
        "body_s3_location": "bodyS3Location",
        "cors_configuration": "corsConfiguration",
        "credentials_arn": "credentialsArn",
        "description": "description",
        "disable_execute_api_endpoint": "disableExecuteApiEndpoint",
        "disable_schema_validation": "disableSchemaValidation",
        "fail_on_warnings": "failOnWarnings",
        "name": "name",
        "protocol_type": "protocolType",
        "route_key": "routeKey",
        "route_selection_expression": "routeSelectionExpression",
        "tags": "tags",
        "target": "target",
        "version": "version",
    },
)
class CfnApiProps:
    def __init__(
        self,
        *,
        api_key_selection_expression: typing.Optional[builtins.str] = None,
        base_path: typing.Optional[builtins.str] = None,
        body: typing.Any = None,
        body_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.BodyS3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cors_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.CorsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        credentials_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        disable_schema_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        name: typing.Optional[builtins.str] = None,
        protocol_type: typing.Optional[builtins.str] = None,
        route_key: typing.Optional[builtins.str] = None,
        route_selection_expression: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        target: typing.Optional[builtins.str] = None,
        version: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnApi``.

        :param api_key_selection_expression: An API key selection expression. Supported only for WebSocket APIs. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`_ .
        :param base_path: Specifies how to interpret the base path of the API during import. Valid values are ``ignore`` , ``prepend`` , and ``split`` . The default value is ``ignore`` . To learn more, see `Set the OpenAPI basePath Property <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html>`_ . Supported only for HTTP APIs.
        :param body: The OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location`` . If you specify a ``Body`` or ``BodyS3Location`` , don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route`` . API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.
        :param body_s3_location: The S3 location of an OpenAPI definition. Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location`` . If you specify a ``Body`` or ``BodyS3Location`` , don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route`` . API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.
        :param cors_configuration: A CORS configuration. Supported only for HTTP APIs. See `Configuring CORS <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html>`_ for more information.
        :param credentials_arn: This property is part of quick create. It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify ``arn:aws:iam::*:user/*`` . To use resource-based permissions on supported AWS services, specify ``null`` . Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.
        :param description: The description of the API.
        :param disable_execute_api_endpoint: Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint. By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.
        :param disable_schema_validation: Avoid validating models when creating a deployment. Supported only for WebSocket APIs.
        :param fail_on_warnings: Specifies whether to rollback the API creation when a warning is encountered. By default, API creation continues if a warning is encountered.
        :param name: The name of the API. Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation`` .
        :param protocol_type: The API protocol. Valid values are ``WEBSOCKET`` or ``HTTP`` . Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation`` .
        :param route_key: This property is part of quick create. If you don't specify a ``routeKey`` , a default route of ``$default`` is created. The ``$default`` route acts as a catch-all for any request made to your API, for a particular stage. The ``$default`` route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.
        :param route_selection_expression: The route selection expression for the API. For HTTP APIs, the ``routeSelectionExpression`` must be ``${request.method} ${request.path}`` . If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.
        :param tags: The collection of tags. Each tag element is associated with a given resource.
        :param target: This property is part of quick create. Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.
        :param version: A version identifier for the API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # body: Any
            
            cfn_api_props = apigatewayv2.CfnApiProps(
                api_key_selection_expression="apiKeySelectionExpression",
                base_path="basePath",
                body=body,
                body_s3_location=apigatewayv2.CfnApi.BodyS3LocationProperty(
                    bucket="bucket",
                    etag="etag",
                    key="key",
                    version="version"
                ),
                cors_configuration=apigatewayv2.CfnApi.CorsProperty(
                    allow_credentials=False,
                    allow_headers=["allowHeaders"],
                    allow_methods=["allowMethods"],
                    allow_origins=["allowOrigins"],
                    expose_headers=["exposeHeaders"],
                    max_age=123
                ),
                credentials_arn="credentialsArn",
                description="description",
                disable_execute_api_endpoint=False,
                disable_schema_validation=False,
                fail_on_warnings=False,
                name="name",
                protocol_type="protocolType",
                route_key="routeKey",
                route_selection_expression="routeSelectionExpression",
                tags={
                    "tags_key": "tags"
                },
                target="target",
                version="version"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__de72efdeda792916a7e0a8d8953153208abe93b442ac8056802f749d4b8c27c4)
            check_type(argname="argument api_key_selection_expression", value=api_key_selection_expression, expected_type=type_hints["api_key_selection_expression"])
            check_type(argname="argument base_path", value=base_path, expected_type=type_hints["base_path"])
            check_type(argname="argument body", value=body, expected_type=type_hints["body"])
            check_type(argname="argument body_s3_location", value=body_s3_location, expected_type=type_hints["body_s3_location"])
            check_type(argname="argument cors_configuration", value=cors_configuration, expected_type=type_hints["cors_configuration"])
            check_type(argname="argument credentials_arn", value=credentials_arn, expected_type=type_hints["credentials_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument disable_execute_api_endpoint", value=disable_execute_api_endpoint, expected_type=type_hints["disable_execute_api_endpoint"])
            check_type(argname="argument disable_schema_validation", value=disable_schema_validation, expected_type=type_hints["disable_schema_validation"])
            check_type(argname="argument fail_on_warnings", value=fail_on_warnings, expected_type=type_hints["fail_on_warnings"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument protocol_type", value=protocol_type, expected_type=type_hints["protocol_type"])
            check_type(argname="argument route_key", value=route_key, expected_type=type_hints["route_key"])
            check_type(argname="argument route_selection_expression", value=route_selection_expression, expected_type=type_hints["route_selection_expression"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
            check_type(argname="argument version", value=version, expected_type=type_hints["version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if api_key_selection_expression is not None:
            self._values["api_key_selection_expression"] = api_key_selection_expression
        if base_path is not None:
            self._values["base_path"] = base_path
        if body is not None:
            self._values["body"] = body
        if body_s3_location is not None:
            self._values["body_s3_location"] = body_s3_location
        if cors_configuration is not None:
            self._values["cors_configuration"] = cors_configuration
        if credentials_arn is not None:
            self._values["credentials_arn"] = credentials_arn
        if description is not None:
            self._values["description"] = description
        if disable_execute_api_endpoint is not None:
            self._values["disable_execute_api_endpoint"] = disable_execute_api_endpoint
        if disable_schema_validation is not None:
            self._values["disable_schema_validation"] = disable_schema_validation
        if fail_on_warnings is not None:
            self._values["fail_on_warnings"] = fail_on_warnings
        if name is not None:
            self._values["name"] = name
        if protocol_type is not None:
            self._values["protocol_type"] = protocol_type
        if route_key is not None:
            self._values["route_key"] = route_key
        if route_selection_expression is not None:
            self._values["route_selection_expression"] = route_selection_expression
        if tags is not None:
            self._values["tags"] = tags
        if target is not None:
            self._values["target"] = target
        if version is not None:
            self._values["version"] = version

    @builtins.property
    def api_key_selection_expression(self) -> typing.Optional[builtins.str]:
        '''An API key selection expression.

        Supported only for WebSocket APIs. See `API Key Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-apikey-selection-expressions>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-apikeyselectionexpression
        '''
        result = self._values.get("api_key_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def base_path(self) -> typing.Optional[builtins.str]:
        '''Specifies how to interpret the base path of the API during import.

        Valid values are ``ignore`` , ``prepend`` , and ``split`` . The default value is ``ignore`` . To learn more, see `Set the OpenAPI basePath Property <https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-import-api-basePath.html>`_ . Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-basepath
        '''
        result = self._values.get("base_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def body(self) -> typing.Any:
        '''The OpenAPI definition.

        Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location`` . If you specify a ``Body`` or ``BodyS3Location`` , don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route`` . API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-body
        '''
        result = self._values.get("body")
        return typing.cast(typing.Any, result)

    @builtins.property
    def body_s3_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.BodyS3LocationProperty]]:
        '''The S3 location of an OpenAPI definition.

        Supported only for HTTP APIs. To import an HTTP API, you must specify a ``Body`` or ``BodyS3Location`` . If you specify a ``Body`` or ``BodyS3Location`` , don't specify CloudFormation resources such as ``AWS::ApiGatewayV2::Authorizer`` or ``AWS::ApiGatewayV2::Route`` . API Gateway doesn't support the combination of OpenAPI and CloudFormation resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-bodys3location
        '''
        result = self._values.get("body_s3_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.BodyS3LocationProperty]], result)

    @builtins.property
    def cors_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.CorsProperty]]:
        '''A CORS configuration.

        Supported only for HTTP APIs. See `Configuring CORS <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-cors.html>`_ for more information.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-corsconfiguration
        '''
        result = self._values.get("cors_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.CorsProperty]], result)

    @builtins.property
    def credentials_arn(self) -> typing.Optional[builtins.str]:
        '''This property is part of quick create.

        It specifies the credentials required for the integration, if any. For a Lambda integration, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify ``arn:aws:iam::*:user/*`` . To use resource-based permissions on supported AWS services, specify ``null`` . Currently, this property is not used for HTTP integrations. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-credentialsarn
        '''
        result = self._values.get("credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def disable_execute_api_endpoint(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether clients can invoke your API by using the default ``execute-api`` endpoint.

        By default, clients can invoke your API with the default https://{api_id}.execute-api.{region}.amazonaws.com endpoint. To require that clients use a custom domain name to invoke your API, disable the default endpoint.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableexecuteapiendpoint
        '''
        result = self._values.get("disable_execute_api_endpoint")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def disable_schema_validation(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Avoid validating models when creating a deployment.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-disableschemavalidation
        '''
        result = self._values.get("disable_schema_validation")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def fail_on_warnings(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether to rollback the API creation when a warning is encountered.

        By default, API creation continues if a warning is encountered.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-failonwarnings
        '''
        result = self._values.get("fail_on_warnings")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the API.

        Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def protocol_type(self) -> typing.Optional[builtins.str]:
        '''The API protocol.

        Valid values are ``WEBSOCKET`` or ``HTTP`` . Required unless you specify an OpenAPI definition for ``Body`` or ``S3BodyLocation`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-protocoltype
        '''
        result = self._values.get("protocol_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_key(self) -> typing.Optional[builtins.str]:
        '''This property is part of quick create.

        If you don't specify a ``routeKey`` , a default route of ``$default`` is created. The ``$default`` route acts as a catch-all for any request made to your API, for a particular stage. The ``$default`` route key can't be modified. You can add routes after creating the API, and you can update the route keys of additional routes. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routekey
        '''
        result = self._values.get("route_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The route selection expression for the API.

        For HTTP APIs, the ``routeSelectionExpression`` must be ``${request.method} ${request.path}`` . If not provided, this will be the default for HTTP APIs. This property is required for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-routeselectionexpression
        '''
        result = self._values.get("route_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The collection of tags.

        Each tag element is associated with a given resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''This property is part of quick create.

        Quick create produces an API with an integration, a default catch-all route, and a default stage which is configured to automatically deploy changes. For HTTP integrations, specify a fully qualified URL. For Lambda integrations, specify a function ARN. The type of the integration will be HTTP_PROXY or AWS_PROXY, respectively. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def version(self) -> typing.Optional[builtins.str]:
        '''A version identifier for the API.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-api.html#cfn-apigatewayv2-api-version
        '''
        result = self._values.get("version")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApiProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAuthorizer(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnAuthorizer",
):
    '''The ``AWS::ApiGatewayV2::Authorizer`` resource creates an authorizer for a WebSocket API or an HTTP API.

    To learn more, see `Controlling and managing access to a WebSocket API in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-control-access.html>`_ and `Controlling and managing access to an HTTP API in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-access-control.html>`_ in the *API Gateway Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        cfn_authorizer = apigatewayv2.CfnAuthorizer(self, "MyCfnAuthorizer",
            api_id="apiId",
            authorizer_type="authorizerType",
            name="name",
        
            # the properties below are optional
            authorizer_credentials_arn="authorizerCredentialsArn",
            authorizer_payload_format_version="authorizerPayloadFormatVersion",
            authorizer_result_ttl_in_seconds=123,
            authorizer_uri="authorizerUri",
            enable_simple_responses=False,
            identity_source=["identitySource"],
            identity_validation_expression="identityValidationExpression",
            jwt_configuration=apigatewayv2.CfnAuthorizer.JWTConfigurationProperty(
                audience=["audience"],
                issuer="issuer"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        authorizer_type: builtins.str,
        name: builtins.str,
        authorizer_credentials_arn: typing.Optional[builtins.str] = None,
        authorizer_payload_format_version: typing.Optional[builtins.str] = None,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        authorizer_uri: typing.Optional[builtins.str] = None,
        enable_simple_responses: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        identity_source: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
        jwt_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnAuthorizer.JWTConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param authorizer_type: The authorizer type. Specify ``REQUEST`` for a Lambda function using incoming request parameters. Specify ``JWT`` to use JSON Web Tokens (supported only for HTTP APIs).
        :param name: The name of the authorizer.
        :param authorizer_credentials_arn: Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for ``REQUEST`` authorizers.
        :param authorizer_payload_format_version: Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are ``1.0`` and ``2.0`` . To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .
        :param authorizer_result_ttl_in_seconds: The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.
        :param authorizer_uri: The authorizer's Uniform Resource Identifier (URI). For ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2: *{account_id}* :function: *{lambda_function_name}* /invocations`` . In general, the URI has this form: ``arn:aws:apigateway: *{region}* :lambda:path/ *{service_api}*`` , where *{region}* is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .
        :param enable_simple_responses: Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .
        :param identity_source: The identity source for which authorization is requested. For a ``REQUEST`` authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with ``$`` , for example, ``$request.header.Auth`` , ``$request.querystring.Name`` . These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ . For ``JWT`` , a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example ``$request.header.Authorization`` .
        :param identity_validation_expression: This parameter is not used.
        :param jwt_configuration: The ``JWTConfiguration`` property specifies the configuration of a JWT authorizer. Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a867239336510db3ecc55c81cb94d0d83923605d20916fa98ef4877f9a6bb310)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAuthorizerProps(
            api_id=api_id,
            authorizer_type=authorizer_type,
            name=name,
            authorizer_credentials_arn=authorizer_credentials_arn,
            authorizer_payload_format_version=authorizer_payload_format_version,
            authorizer_result_ttl_in_seconds=authorizer_result_ttl_in_seconds,
            authorizer_uri=authorizer_uri,
            enable_simple_responses=enable_simple_responses,
            identity_source=identity_source,
            identity_validation_expression=identity_validation_expression,
            jwt_configuration=jwt_configuration,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d959aa36bcde5579969213ffe818029e4f8c72a281aa48051e9a737c828e1ddd)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cf024f12578bd433a40860ee462136ed673aae2a31c77ef7c5d0718c4d76c50f)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAuthorizerId")
    def attr_authorizer_id(self) -> builtins.str:
        '''The authorizer ID.

        :cloudformationAttribute: AuthorizerId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAuthorizerId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c94b906e2fe834cc4b37a4eb041b8e7ab23901d40aeb5912de689fad4139fc9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerType")
    def authorizer_type(self) -> builtins.str:
        '''The authorizer type.'''
        return typing.cast(builtins.str, jsii.get(self, "authorizerType"))

    @authorizer_type.setter
    def authorizer_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdc8e9a7d4d7429420766da5e132ae16ec76fc2f3e679d82cdf69137c200fbc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerType", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the authorizer.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78b3b857580e5719b96ef1257bd96e1a2a67be3225151b97e8008a99ed6a360)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerCredentialsArn")
    def authorizer_credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerCredentialsArn"))

    @authorizer_credentials_arn.setter
    def authorizer_credentials_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29e0e6baddf2813e344a9f995c17c9369390dcc36a6c186182885b5956b6be2a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerCredentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerPayloadFormatVersion")
    def authorizer_payload_format_version(self) -> typing.Optional[builtins.str]:
        '''Specifies the format of the payload sent to an HTTP API Lambda authorizer.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerPayloadFormatVersion"))

    @authorizer_payload_format_version.setter
    def authorizer_payload_format_version(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__704a1ebfe51335da671a36d566a2f9ebce2a91877958850fce305542c6f8147f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerPayloadFormatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerResultTtlInSeconds")
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time to live (TTL) for cached authorizer results, in seconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "authorizerResultTtlInSeconds"))

    @authorizer_result_ttl_in_seconds.setter
    def authorizer_result_ttl_in_seconds(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__10386c9852429b19804f6174b4c7ef97c7b3cbf3a8183c5db8d1df686554caee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerResultTtlInSeconds", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerUri")
    def authorizer_uri(self) -> typing.Optional[builtins.str]:
        '''The authorizer's Uniform Resource Identifier (URI).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerUri"))

    @authorizer_uri.setter
    def authorizer_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f0becd827426ad17e13b4edec41e2383d35feec43ac97627da48c167c25f0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerUri", value)

    @builtins.property
    @jsii.member(jsii_name="enableSimpleResponses")
    def enable_simple_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a Lambda authorizer returns a response in a simple format.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "enableSimpleResponses"))

    @enable_simple_responses.setter
    def enable_simple_responses(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca220b368392b92ad3186f8b7a90bf77a210aaafee93b2a0e9444103bac3301c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableSimpleResponses", value)

    @builtins.property
    @jsii.member(jsii_name="identitySource")
    def identity_source(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identity source for which authorization is requested.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "identitySource"))

    @identity_source.setter
    def identity_source(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ace1f00404a76cab1dbe9bd4e4f41644b1de7a3dd37df8e37625966ae52594c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identitySource", value)

    @builtins.property
    @jsii.member(jsii_name="identityValidationExpression")
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''This parameter is not used.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "identityValidationExpression"))

    @identity_validation_expression.setter
    def identity_validation_expression(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d335b88eea9c6ce2df51c3c8e9af597d3a4f3fb42410c60a1fbc7de5813a7800)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "identityValidationExpression", value)

    @builtins.property
    @jsii.member(jsii_name="jwtConfiguration")
    def jwt_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAuthorizer.JWTConfigurationProperty"]]:
        '''The ``JWTConfiguration`` property specifies the configuration of a JWT authorizer.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAuthorizer.JWTConfigurationProperty"]], jsii.get(self, "jwtConfiguration"))

    @jwt_configuration.setter
    def jwt_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnAuthorizer.JWTConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9a032d11594e2f9a62ed9a4289c33939ffb5bebe7caa00404debfb40cd260e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jwtConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnAuthorizer.JWTConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"audience": "audience", "issuer": "issuer"},
    )
    class JWTConfigurationProperty:
        def __init__(
            self,
            *,
            audience: typing.Optional[typing.Sequence[builtins.str]] = None,
            issuer: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``JWTConfiguration`` property specifies the configuration of a JWT authorizer.

            Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.

            :param audience: A list of the intended recipients of the JWT. A valid JWT must provide an ``aud`` that matches at least one entry in this list. See `RFC 7519 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc7519#section-4.1.3>`_ . Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.
            :param issuer: The base domain of the identity provider that issues JSON Web Tokens. For example, an Amazon Cognito user pool has the following format: ``https://cognito-idp. {region} .amazonaws.com/ {userPoolId}`` . Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                j_wTConfiguration_property = apigatewayv2.CfnAuthorizer.JWTConfigurationProperty(
                    audience=["audience"],
                    issuer="issuer"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8e3111dc0620a413031b38e657a146c66f5c593098e2264e4a367a7d9cae646b)
                check_type(argname="argument audience", value=audience, expected_type=type_hints["audience"])
                check_type(argname="argument issuer", value=issuer, expected_type=type_hints["issuer"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if audience is not None:
                self._values["audience"] = audience
            if issuer is not None:
                self._values["issuer"] = issuer

        @builtins.property
        def audience(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of the intended recipients of the JWT.

            A valid JWT must provide an ``aud`` that matches at least one entry in this list. See `RFC 7519 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc7519#section-4.1.3>`_ . Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-audience
            '''
            result = self._values.get("audience")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def issuer(self) -> typing.Optional[builtins.str]:
            '''The base domain of the identity provider that issues JSON Web Tokens.

            For example, an Amazon Cognito user pool has the following format: ``https://cognito-idp. {region} .amazonaws.com/ {userPoolId}`` . Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-authorizer-jwtconfiguration.html#cfn-apigatewayv2-authorizer-jwtconfiguration-issuer
            '''
            result = self._values.get("issuer")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "JWTConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnAuthorizerProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "authorizer_type": "authorizerType",
        "name": "name",
        "authorizer_credentials_arn": "authorizerCredentialsArn",
        "authorizer_payload_format_version": "authorizerPayloadFormatVersion",
        "authorizer_result_ttl_in_seconds": "authorizerResultTtlInSeconds",
        "authorizer_uri": "authorizerUri",
        "enable_simple_responses": "enableSimpleResponses",
        "identity_source": "identitySource",
        "identity_validation_expression": "identityValidationExpression",
        "jwt_configuration": "jwtConfiguration",
    },
)
class CfnAuthorizerProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        authorizer_type: builtins.str,
        name: builtins.str,
        authorizer_credentials_arn: typing.Optional[builtins.str] = None,
        authorizer_payload_format_version: typing.Optional[builtins.str] = None,
        authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
        authorizer_uri: typing.Optional[builtins.str] = None,
        enable_simple_responses: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        identity_source: typing.Optional[typing.Sequence[builtins.str]] = None,
        identity_validation_expression: typing.Optional[builtins.str] = None,
        jwt_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAuthorizer.JWTConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAuthorizer``.

        :param api_id: The API identifier.
        :param authorizer_type: The authorizer type. Specify ``REQUEST`` for a Lambda function using incoming request parameters. Specify ``JWT`` to use JSON Web Tokens (supported only for HTTP APIs).
        :param name: The name of the authorizer.
        :param authorizer_credentials_arn: Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer. To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for ``REQUEST`` authorizers.
        :param authorizer_payload_format_version: Specifies the format of the payload sent to an HTTP API Lambda authorizer. Required for HTTP API Lambda authorizers. Supported values are ``1.0`` and ``2.0`` . To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .
        :param authorizer_result_ttl_in_seconds: The time to live (TTL) for cached authorizer results, in seconds. If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.
        :param authorizer_uri: The authorizer's Uniform Resource Identifier (URI). For ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2: *{account_id}* :function: *{lambda_function_name}* /invocations`` . In general, the URI has this form: ``arn:aws:apigateway: *{region}* :lambda:path/ *{service_api}*`` , where *{region}* is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .
        :param enable_simple_responses: Specifies whether a Lambda authorizer returns a response in a simple format. By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .
        :param identity_source: The identity source for which authorization is requested. For a ``REQUEST`` authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with ``$`` , for example, ``$request.header.Auth`` , ``$request.querystring.Name`` . These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ . For ``JWT`` , a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example ``$request.header.Authorization`` .
        :param identity_validation_expression: This parameter is not used.
        :param jwt_configuration: The ``JWTConfiguration`` property specifies the configuration of a JWT authorizer. Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            cfn_authorizer_props = apigatewayv2.CfnAuthorizerProps(
                api_id="apiId",
                authorizer_type="authorizerType",
                name="name",
            
                # the properties below are optional
                authorizer_credentials_arn="authorizerCredentialsArn",
                authorizer_payload_format_version="authorizerPayloadFormatVersion",
                authorizer_result_ttl_in_seconds=123,
                authorizer_uri="authorizerUri",
                enable_simple_responses=False,
                identity_source=["identitySource"],
                identity_validation_expression="identityValidationExpression",
                jwt_configuration=apigatewayv2.CfnAuthorizer.JWTConfigurationProperty(
                    audience=["audience"],
                    issuer="issuer"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7793252368a914b674f8f80b8ab85fd50270086231afdc5a63d6706fc8985226)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument authorizer_type", value=authorizer_type, expected_type=type_hints["authorizer_type"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument authorizer_credentials_arn", value=authorizer_credentials_arn, expected_type=type_hints["authorizer_credentials_arn"])
            check_type(argname="argument authorizer_payload_format_version", value=authorizer_payload_format_version, expected_type=type_hints["authorizer_payload_format_version"])
            check_type(argname="argument authorizer_result_ttl_in_seconds", value=authorizer_result_ttl_in_seconds, expected_type=type_hints["authorizer_result_ttl_in_seconds"])
            check_type(argname="argument authorizer_uri", value=authorizer_uri, expected_type=type_hints["authorizer_uri"])
            check_type(argname="argument enable_simple_responses", value=enable_simple_responses, expected_type=type_hints["enable_simple_responses"])
            check_type(argname="argument identity_source", value=identity_source, expected_type=type_hints["identity_source"])
            check_type(argname="argument identity_validation_expression", value=identity_validation_expression, expected_type=type_hints["identity_validation_expression"])
            check_type(argname="argument jwt_configuration", value=jwt_configuration, expected_type=type_hints["jwt_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "authorizer_type": authorizer_type,
            "name": name,
        }
        if authorizer_credentials_arn is not None:
            self._values["authorizer_credentials_arn"] = authorizer_credentials_arn
        if authorizer_payload_format_version is not None:
            self._values["authorizer_payload_format_version"] = authorizer_payload_format_version
        if authorizer_result_ttl_in_seconds is not None:
            self._values["authorizer_result_ttl_in_seconds"] = authorizer_result_ttl_in_seconds
        if authorizer_uri is not None:
            self._values["authorizer_uri"] = authorizer_uri
        if enable_simple_responses is not None:
            self._values["enable_simple_responses"] = enable_simple_responses
        if identity_source is not None:
            self._values["identity_source"] = identity_source
        if identity_validation_expression is not None:
            self._values["identity_validation_expression"] = identity_validation_expression
        if jwt_configuration is not None:
            self._values["jwt_configuration"] = jwt_configuration

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_type(self) -> builtins.str:
        '''The authorizer type.

        Specify ``REQUEST`` for a Lambda function using incoming request parameters. Specify ``JWT`` to use JSON Web Tokens (supported only for HTTP APIs).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizertype
        '''
        result = self._values.get("authorizer_type")
        assert result is not None, "Required property 'authorizer_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the authorizer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def authorizer_credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the required credentials as an IAM role for API Gateway to invoke the authorizer.

        To specify an IAM role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To use resource-based permissions on the Lambda function, specify null. Supported only for ``REQUEST`` authorizers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizercredentialsarn
        '''
        result = self._values.get("authorizer_credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_payload_format_version(self) -> typing.Optional[builtins.str]:
        '''Specifies the format of the payload sent to an HTTP API Lambda authorizer.

        Required for HTTP API Lambda authorizers. Supported values are ``1.0`` and ``2.0`` . To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerpayloadformatversion
        '''
        result = self._values.get("authorizer_payload_format_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_result_ttl_in_seconds(self) -> typing.Optional[jsii.Number]:
        '''The time to live (TTL) for cached authorizer results, in seconds.

        If it equals 0, authorization caching is disabled. If it is greater than 0, API Gateway caches authorizer responses. The maximum value is 3600, or 1 hour. Supported only for HTTP API Lambda authorizers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizerresultttlinseconds
        '''
        result = self._values.get("authorizer_result_ttl_in_seconds")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def authorizer_uri(self) -> typing.Optional[builtins.str]:
        '''The authorizer's Uniform Resource Identifier (URI).

        For ``REQUEST`` authorizers, this must be a well-formed Lambda function URI, for example, ``arn:aws:apigateway:us-west-2:lambda:path/2015-03-31/functions/arn:aws:lambda:us-west-2: *{account_id}* :function: *{lambda_function_name}* /invocations`` . In general, the URI has this form: ``arn:aws:apigateway: *{region}* :lambda:path/ *{service_api}*`` , where *{region}* is the same as the region hosting the Lambda function, path indicates that the remaining substring in the URI should be treated as the path to the resource, including the initial ``/`` . For Lambda functions, this is usually of the form ``/2015-03-31/functions/[FunctionARN]/invocations`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-authorizeruri
        '''
        result = self._values.get("authorizer_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enable_simple_responses(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether a Lambda authorizer returns a response in a simple format.

        By default, a Lambda authorizer must return an IAM policy. If enabled, the Lambda authorizer can return a boolean value instead of an IAM policy. Supported only for HTTP APIs. To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-enablesimpleresponses
        '''
        result = self._values.get("enable_simple_responses")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def identity_source(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The identity source for which authorization is requested.

        For a ``REQUEST`` authorizer, this is optional. The value is a set of one or more mapping expressions of the specified request parameters. The identity source can be headers, query string parameters, stage variables, and context parameters. For example, if an Auth header and a Name query string parameter are defined as identity sources, this value is route.request.header.Auth, route.request.querystring.Name for WebSocket APIs. For HTTP APIs, use selection expressions prefixed with ``$`` , for example, ``$request.header.Auth`` , ``$request.querystring.Name`` . These parameters are used to perform runtime validation for Lambda-based authorizers by verifying all of the identity-related request parameters are present in the request, not null, and non-empty. Only when this is true does the authorizer invoke the authorizer Lambda function. Otherwise, it returns a 401 Unauthorized response without calling the Lambda function. For HTTP APIs, identity sources are also used as the cache key when caching is enabled. To learn more, see `Working with AWS Lambda authorizers for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-lambda-authorizer.html>`_ .

        For ``JWT`` , a single entry that specifies where to extract the JSON Web Token (JWT) from inbound requests. Currently only header-based and query parameter-based selections are supported, for example ``$request.header.Authorization`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identitysource
        '''
        result = self._values.get("identity_source")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def identity_validation_expression(self) -> typing.Optional[builtins.str]:
        '''This parameter is not used.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-identityvalidationexpression
        '''
        result = self._values.get("identity_validation_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def jwt_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAuthorizer.JWTConfigurationProperty]]:
        '''The ``JWTConfiguration`` property specifies the configuration of a JWT authorizer.

        Required for the ``JWT`` authorizer type. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-authorizer.html#cfn-apigatewayv2-authorizer-jwtconfiguration
        '''
        result = self._values.get("jwt_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAuthorizer.JWTConfigurationProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAuthorizerProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDeployment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnDeployment",
):
    '''The ``AWS::ApiGatewayV2::Deployment`` resource creates a deployment for an API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        cfn_deployment = apigatewayv2.CfnDeployment(self, "MyCfnDeployment",
            api_id="apiId",
        
            # the properties below are optional
            description="description",
            stage_name="stageName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        stage_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param description: The description for the deployment resource.
        :param stage_name: The name of an existing stage to associate with the deployment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd659e77f6f73d039f09dfba950ad0f0c80871608d2a7828058dceb3e7fe181)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDeploymentProps(
            api_id=api_id, description=description, stage_name=stage_name
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f8481ebeeb348b5cd00950f41454661b821577bbfc21c63c7524dd95654fc17)
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
            type_hints = typing.get_type_hints(_typecheckingstub__cb7dbc3d4832449936a54c0e42e5bc985b663309bbdb2aeba47447838030f7d3)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDeploymentId")
    def attr_deployment_id(self) -> builtins.str:
        '''The deployment ID.

        :cloudformationAttribute: DeploymentId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDeploymentId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8380391f5e9a81027656c48bdab6533551d7416be7d4c0a61dcb8c7870a6695d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the deployment resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a096735639df363beb6e57d5ef578f6cf95a74095409ee9c322663acd1f5ba03)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> typing.Optional[builtins.str]:
        '''The name of an existing stage to associate with the deployment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "stageName"))

    @stage_name.setter
    def stage_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33040a213f03d33962ff4df0681abb8f23303cac13cf97cc0ac997dc873eb59c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnDeploymentProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "description": "description",
        "stage_name": "stageName",
    },
)
class CfnDeploymentProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        stage_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDeployment``.

        :param api_id: The API identifier.
        :param description: The description for the deployment resource.
        :param stage_name: The name of an existing stage to associate with the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            cfn_deployment_props = apigatewayv2.CfnDeploymentProps(
                api_id="apiId",
            
                # the properties below are optional
                description="description",
                stage_name="stageName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__497cc0e552f167da7730bb49dda8116b36b3c3e31b6bebeabe6ecf25f997b531)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
        }
        if description is not None:
            self._values["description"] = description
        if stage_name is not None:
            self._values["stage_name"] = stage_name

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the deployment resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def stage_name(self) -> typing.Optional[builtins.str]:
        '''The name of an existing stage to associate with the deployment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-deployment.html#cfn-apigatewayv2-deployment-stagename
        '''
        result = self._values.get("stage_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDeploymentProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnDomainName(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnDomainName",
):
    '''The ``AWS::ApiGatewayV2::DomainName`` resource specifies a custom domain name for your API in Amazon API Gateway (API Gateway).

    You can use a custom domain name to provide a URL that's more intuitive and easier to recall. For more information about using custom domain names, see `Set up Custom Domain Name for an API in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html>`_ in the *API Gateway Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # tags: Any
        
        cfn_domain_name = apigatewayv2.CfnDomainName(self, "MyCfnDomainName",
            domain_name="domainName",
        
            # the properties below are optional
            domain_name_configurations=[apigatewayv2.CfnDomainName.DomainNameConfigurationProperty(
                certificate_arn="certificateArn",
                certificate_name="certificateName",
                endpoint_type="endpointType",
                ownership_verification_certificate_arn="ownershipVerificationCertificateArn",
                security_policy="securityPolicy"
            )],
            mutual_tls_authentication=apigatewayv2.CfnDomainName.MutualTlsAuthenticationProperty(
                truststore_uri="truststoreUri",
                truststore_version="truststoreVersion"
            ),
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        domain_name_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomainName.DomainNameConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnDomainName.MutualTlsAuthenticationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        :param domain_name_configurations: The domain name configurations.
        :param mutual_tls_authentication: The mutual TLS authentication configuration for a custom domain name.
        :param tags: The collection of tags associated with a domain name.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1dd1a2be8baf8f5fddc282520a295c206cc1466b04d57a3227f938bdec4a2f5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDomainNameProps(
            domain_name=domain_name,
            domain_name_configurations=domain_name_configurations,
            mutual_tls_authentication=mutual_tls_authentication,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca0b93c0a8031fc21c98a7b59eb1a20d1be884a8f1e1d5510fcbeea6febc52bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__56ce76adb9b6f17382e4b34b13786dcec99768d000140b8e1aa78820d94d0a4b)
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
    @jsii.member(jsii_name="attrRegionalDomainName")
    def attr_regional_domain_name(self) -> builtins.str:
        '''The domain name associated with the regional endpoint for this custom domain name.

        You set up this association by adding a DNS record that points the custom domain name to this regional domain name.

        :cloudformationAttribute: RegionalDomainName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegionalDomainName"))

    @builtins.property
    @jsii.member(jsii_name="attrRegionalHostedZoneId")
    def attr_regional_hosted_zone_id(self) -> builtins.str:
        '''The region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint.

        :cloudformationAttribute: RegionalHostedZoneId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRegionalHostedZoneId"))

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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The custom domain name for your API in Amazon API Gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8174f7ac22c1397914e489109ad7e6891d4964a0f3d3972fd7f5fa8ce72c3bce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="domainNameConfigurations")
    def domain_name_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomainName.DomainNameConfigurationProperty"]]]]:
        '''The domain name configurations.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomainName.DomainNameConfigurationProperty"]]]], jsii.get(self, "domainNameConfigurations"))

    @domain_name_configurations.setter
    def domain_name_configurations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnDomainName.DomainNameConfigurationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b9b6be5b4180a1026f7ee79c898cdcb31077d95e3aa103f952db8e5fc4901eb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainNameConfigurations", value)

    @builtins.property
    @jsii.member(jsii_name="mutualTlsAuthentication")
    def mutual_tls_authentication(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomainName.MutualTlsAuthenticationProperty"]]:
        '''The mutual TLS authentication configuration for a custom domain name.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomainName.MutualTlsAuthenticationProperty"]], jsii.get(self, "mutualTlsAuthentication"))

    @mutual_tls_authentication.setter
    def mutual_tls_authentication(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnDomainName.MutualTlsAuthenticationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7db79836bb2717dd9f77cf2a7e1dbf16c2828d8d2066adf6a1fd6f14bd19d816)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mutualTlsAuthentication", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The collection of tags associated with a domain name.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91e15ff48f085b835a961d76641a12ee2d099786f346c15be08cd6e10f58f927)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnDomainName.DomainNameConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "certificate_arn": "certificateArn",
            "certificate_name": "certificateName",
            "endpoint_type": "endpointType",
            "ownership_verification_certificate_arn": "ownershipVerificationCertificateArn",
            "security_policy": "securityPolicy",
        },
    )
    class DomainNameConfigurationProperty:
        def __init__(
            self,
            *,
            certificate_arn: typing.Optional[builtins.str] = None,
            certificate_name: typing.Optional[builtins.str] = None,
            endpoint_type: typing.Optional[builtins.str] = None,
            ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
            security_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``DomainNameConfiguration`` property type specifies the configuration for a an API's domain name.

            ``DomainNameConfiguration`` is a property of the `AWS::ApiGatewayV2::DomainName <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html>`_ resource.

            :param certificate_arn: An AWS -managed certificate that will be used by the edge-optimized endpoint for this domain name. AWS Certificate Manager is the only supported source.
            :param certificate_name: The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.
            :param endpoint_type: The endpoint type.
            :param ownership_verification_certificate_arn: The Amazon resource name (ARN) for the public certificate issued by AWS Certificate Manager . This ARN is used to validate custom domain ownership. It's required only if you configure mutual TLS and use either an ACM-imported or a private CA certificate ARN as the regionalCertificateArn.
            :param security_policy: The Transport Layer Security (TLS) version of the security policy for this domain name. The valid values are ``TLS_1_0`` and ``TLS_1_2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                domain_name_configuration_property = apigatewayv2.CfnDomainName.DomainNameConfigurationProperty(
                    certificate_arn="certificateArn",
                    certificate_name="certificateName",
                    endpoint_type="endpointType",
                    ownership_verification_certificate_arn="ownershipVerificationCertificateArn",
                    security_policy="securityPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__faaf4905cea99e081f1f881fa68755b4ec1bc0ed8f4e145c30baf36d95e5cc83)
                check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
                check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
                check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
                check_type(argname="argument ownership_verification_certificate_arn", value=ownership_verification_certificate_arn, expected_type=type_hints["ownership_verification_certificate_arn"])
                check_type(argname="argument security_policy", value=security_policy, expected_type=type_hints["security_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if certificate_arn is not None:
                self._values["certificate_arn"] = certificate_arn
            if certificate_name is not None:
                self._values["certificate_name"] = certificate_name
            if endpoint_type is not None:
                self._values["endpoint_type"] = endpoint_type
            if ownership_verification_certificate_arn is not None:
                self._values["ownership_verification_certificate_arn"] = ownership_verification_certificate_arn
            if security_policy is not None:
                self._values["security_policy"] = security_policy

        @builtins.property
        def certificate_arn(self) -> typing.Optional[builtins.str]:
            '''An AWS -managed certificate that will be used by the edge-optimized endpoint for this domain name.

            AWS Certificate Manager is the only supported source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatearn
            '''
            result = self._values.get("certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def certificate_name(self) -> typing.Optional[builtins.str]:
            '''The user-friendly name of the certificate that will be used by the edge-optimized endpoint for this domain name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-certificatename
            '''
            result = self._values.get("certificate_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def endpoint_type(self) -> typing.Optional[builtins.str]:
            '''The endpoint type.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-endpointtype
            '''
            result = self._values.get("endpoint_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ownership_verification_certificate_arn(
            self,
        ) -> typing.Optional[builtins.str]:
            '''The Amazon resource name (ARN) for the public certificate issued by AWS Certificate Manager .

            This ARN is used to validate custom domain ownership. It's required only if you configure mutual TLS and use either an ACM-imported or a private CA certificate ARN as the regionalCertificateArn.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-ownershipverificationcertificatearn
            '''
            result = self._values.get("ownership_verification_certificate_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def security_policy(self) -> typing.Optional[builtins.str]:
            '''The Transport Layer Security (TLS) version of the security policy for this domain name.

            The valid values are ``TLS_1_0`` and ``TLS_1_2`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-domainnameconfiguration.html#cfn-apigatewayv2-domainname-domainnameconfiguration-securitypolicy
            '''
            result = self._values.get("security_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainNameConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnDomainName.MutualTlsAuthenticationProperty",
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
            '''If specified, API Gateway performs two-way authentication between the client and the server.

            Clients must present a trusted certificate to access your API.

            :param truststore_uri: An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, ``s3:// bucket-name / key-name`` . The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.
            :param truststore_version: The version of the S3 object that contains your truststore. To specify a version, you must have versioning enabled for the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                mutual_tls_authentication_property = apigatewayv2.CfnDomainName.MutualTlsAuthenticationProperty(
                    truststore_uri="truststoreUri",
                    truststore_version="truststoreVersion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6f25cc46ec061420fb13cc99bbb2ac01e6cf22e79cf84955006c7e3a92b30e40)
                check_type(argname="argument truststore_uri", value=truststore_uri, expected_type=type_hints["truststore_uri"])
                check_type(argname="argument truststore_version", value=truststore_version, expected_type=type_hints["truststore_version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if truststore_uri is not None:
                self._values["truststore_uri"] = truststore_uri
            if truststore_version is not None:
                self._values["truststore_version"] = truststore_version

        @builtins.property
        def truststore_uri(self) -> typing.Optional[builtins.str]:
            '''An Amazon S3 URL that specifies the truststore for mutual TLS authentication, for example, ``s3:// bucket-name / key-name`` .

            The truststore can contain certificates from public or private certificate authorities. To update the truststore, upload a new version to S3, and then update your custom domain name to use the new version. To update the truststore, you must have permissions to access the S3 object.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreuri
            '''
            result = self._values.get("truststore_uri")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def truststore_version(self) -> typing.Optional[builtins.str]:
            '''The version of the S3 object that contains your truststore.

            To specify a version, you must have versioning enabled for the S3 bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-domainname-mutualtlsauthentication.html#cfn-apigatewayv2-domainname-mutualtlsauthentication-truststoreversion
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
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnDomainNameProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "domain_name_configurations": "domainNameConfigurations",
        "mutual_tls_authentication": "mutualTlsAuthentication",
        "tags": "tags",
    },
)
class CfnDomainNameProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        domain_name_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomainName.DomainNameConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomainName.MutualTlsAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnDomainName``.

        :param domain_name: The custom domain name for your API in Amazon API Gateway. Uppercase letters are not supported.
        :param domain_name_configurations: The domain name configurations.
        :param mutual_tls_authentication: The mutual TLS authentication configuration for a custom domain name.
        :param tags: The collection of tags associated with a domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # tags: Any
            
            cfn_domain_name_props = apigatewayv2.CfnDomainNameProps(
                domain_name="domainName",
            
                # the properties below are optional
                domain_name_configurations=[apigatewayv2.CfnDomainName.DomainNameConfigurationProperty(
                    certificate_arn="certificateArn",
                    certificate_name="certificateName",
                    endpoint_type="endpointType",
                    ownership_verification_certificate_arn="ownershipVerificationCertificateArn",
                    security_policy="securityPolicy"
                )],
                mutual_tls_authentication=apigatewayv2.CfnDomainName.MutualTlsAuthenticationProperty(
                    truststore_uri="truststoreUri",
                    truststore_version="truststoreVersion"
                ),
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1629526da8e64502c98094213f6afc52d78388551bbefd7f02cebe4452a94a5c)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument domain_name_configurations", value=domain_name_configurations, expected_type=type_hints["domain_name_configurations"])
            check_type(argname="argument mutual_tls_authentication", value=mutual_tls_authentication, expected_type=type_hints["mutual_tls_authentication"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if domain_name_configurations is not None:
            self._values["domain_name_configurations"] = domain_name_configurations
        if mutual_tls_authentication is not None:
            self._values["mutual_tls_authentication"] = mutual_tls_authentication
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The custom domain name for your API in Amazon API Gateway.

        Uppercase letters are not supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def domain_name_configurations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDomainName.DomainNameConfigurationProperty]]]]:
        '''The domain name configurations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-domainnameconfigurations
        '''
        result = self._values.get("domain_name_configurations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDomainName.DomainNameConfigurationProperty]]]], result)

    @builtins.property
    def mutual_tls_authentication(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomainName.MutualTlsAuthenticationProperty]]:
        '''The mutual TLS authentication configuration for a custom domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-mutualtlsauthentication
        '''
        result = self._values.get("mutual_tls_authentication")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomainName.MutualTlsAuthenticationProperty]], result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The collection of tags associated with a domain name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-domainname.html#cfn-apigatewayv2-domainname-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDomainNameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIntegration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegration",
):
    '''The ``AWS::ApiGatewayV2::Integration`` resource creates an integration for an API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # request_parameters: Any
        # request_templates: Any
        # response_parameters: Any
        
        cfn_integration = apigatewayv2.CfnIntegration(self, "MyCfnIntegration",
            api_id="apiId",
            integration_type="integrationType",
        
            # the properties below are optional
            connection_id="connectionId",
            connection_type="connectionType",
            content_handling_strategy="contentHandlingStrategy",
            credentials_arn="credentialsArn",
            description="description",
            integration_method="integrationMethod",
            integration_subtype="integrationSubtype",
            integration_uri="integrationUri",
            passthrough_behavior="passthroughBehavior",
            payload_format_version="payloadFormatVersion",
            request_parameters=request_parameters,
            request_templates=request_templates,
            response_parameters=response_parameters,
            template_selection_expression="templateSelectionExpression",
            timeout_in_millis=123,
            tls_config=apigatewayv2.CfnIntegration.TlsConfigProperty(
                server_name_to_verify="serverNameToVerify"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        integration_type: builtins.str,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[builtins.str] = None,
        content_handling_strategy: typing.Optional[builtins.str] = None,
        credentials_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        integration_method: typing.Optional[builtins.str] = None,
        integration_subtype: typing.Optional[builtins.str] = None,
        integration_uri: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[builtins.str] = None,
        payload_format_version: typing.Optional[builtins.str] = None,
        request_parameters: typing.Any = None,
        request_templates: typing.Any = None,
        response_parameters: typing.Any = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
        timeout_in_millis: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.TlsConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param integration_type: The integration type of an integration. One of the following:. ``AWS`` : for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs. ``AWS_PROXY`` : for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration. ``HTTP`` : for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs. ``HTTP_PROXY`` : for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an ``HTTP_PROXY`` integration. ``MOCK`` : for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.
        :param connection_id: The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        :param connection_type: The type of the network connection to the integration endpoint. Specify ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and resources in a VPC. The default value is ``INTERNET`` .
        :param content_handling_strategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors: ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob. ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string. If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :param credentials_arn: Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::*:user/*`` . To use resource-based permissions on supported AWS services, don't specify this parameter.
        :param description: The description of the integration.
        :param integration_method: Specifies the integration's HTTP method type.
        :param integration_subtype: Supported only for HTTP API ``AWS_PROXY`` integrations. Specifies the AWS service action to invoke. To learn more, see `Integration subtype reference <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html>`_ .
        :param integration_uri: For a Lambda integration, specify the URI of a Lambda function. For an HTTP integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses ``DiscoverInstances`` to identify resources. You can use query parameters to target specific resources. To learn more, see `DiscoverInstances <https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html>`_ . For private integrations, all resources must be owned by the same AWS account .
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the ``Content-Type`` header in the request, and the available mapping templates specified as the ``requestTemplates`` property on the ``Integration`` resource. There are three valid values: ``WHEN_NO_MATCH`` , ``WHEN_NO_TEMPLATES`` , and ``NEVER`` . Supported only for WebSocket APIs. ``WHEN_NO_MATCH`` passes the request body for unmapped content types through to the integration backend without transformation. ``NEVER`` rejects unmapped content types with an ``HTTP 415 Unsupported Media Type`` response. ``WHEN_NO_TEMPLATES`` allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same ``HTTP 415 Unsupported Media Type`` response.
        :param payload_format_version: Specifies the format of the payload sent to an integration. Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are ``1.0`` and ``2.0`` . For all other integrations, ``1.0`` is the only supported value. To learn more, see `Working with AWS Lambda proxy integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html>`_ .
        :param request_parameters: For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of ``method.request. {location} . {name}`` , where ``{location}`` is ``querystring`` , ``path`` , or ``header`` ; and ``{name}`` must be a valid and unique method request parameter name. For HTTP API integrations with a specified ``integrationSubtype`` , request parameters are a key-value map specifying parameters that are passed to ``AWS_PROXY`` integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Working with AWS service integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html>`_ . For HTTP API integrations without a specified ``integrationSubtype`` request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern :<header|querystring|path>. where action can be ``append`` , ``overwrite`` or ``remove`` . For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .
        :param request_templates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.
        :param response_parameters: Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. The value is of type ```ResponseParameterList`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html>`_ . To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .
        :param template_selection_expression: The template selection expression for the integration. Supported only for WebSocket APIs.
        :param timeout_in_millis: Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.
        :param tls_config: The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__89ee25d7b8304fd6f8c1196e47b946d8bf8256f5a9f37b58c7c5f5cb8f73bd7f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationProps(
            api_id=api_id,
            integration_type=integration_type,
            connection_id=connection_id,
            connection_type=connection_type,
            content_handling_strategy=content_handling_strategy,
            credentials_arn=credentials_arn,
            description=description,
            integration_method=integration_method,
            integration_subtype=integration_subtype,
            integration_uri=integration_uri,
            passthrough_behavior=passthrough_behavior,
            payload_format_version=payload_format_version,
            request_parameters=request_parameters,
            request_templates=request_templates,
            response_parameters=response_parameters,
            template_selection_expression=template_selection_expression,
            timeout_in_millis=timeout_in_millis,
            tls_config=tls_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee31d41d0171be6e19e690774d5d6627ad812e56a2cab81fa66b2f61aa6f3951)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6126d2c248e8bb9199dba590d9b83e8f9719b81bd829888c5414ef87a3d59219)
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
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa39d0c12f6743ba2631e050aa28a363ddcc81dfd7ae60bc844dc7f45a3a0c7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def integration_type(self) -> builtins.str:
        '''The integration type of an integration.

        One of the following:.
        '''
        return typing.cast(builtins.str, jsii.get(self, "integrationType"))

    @integration_type.setter
    def integration_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b18c92c57e09be6a12ef9c2311c8921cafb5f4dff56e0f8e98710440065d0f75)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value)

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC link for a private integration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__46edc03483245f7ebd5b029a181a06f1ae098e07971bccad9b4ecd1986adc162)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''The type of the network connection to the integration endpoint.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionType"))

    @connection_type.setter
    def connection_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48543c37e107a7129a6cbc73639e8383fb2c4225d304382db660f52645290ecd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="contentHandlingStrategy")
    def content_handling_strategy(self) -> typing.Optional[builtins.str]:
        '''Supported only for WebSocket APIs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentHandlingStrategy"))

    @content_handling_strategy.setter
    def content_handling_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8b1973f1c5573b93173e49c64f6e70a715914d1fba975e1eb8070226202221f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentHandlingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="credentialsArn")
    def credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the credentials required for the integration, if any.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "credentialsArn"))

    @credentials_arn.setter
    def credentials_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6d8c439acc57ba5be7137b02b1514b0e9a84285d9b207cf8edbb188cd3c9cdf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "credentialsArn", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the integration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc069b9321eb211ab95f9c0904ca5919c9d265fef15a59838ae9f884273b0669)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="integrationMethod")
    def integration_method(self) -> typing.Optional[builtins.str]:
        '''Specifies the integration's HTTP method type.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationMethod"))

    @integration_method.setter
    def integration_method(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0362127f0c545ac01dd3b59243c935c5756b6e9251c2a8e04597ec0281a833a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationMethod", value)

    @builtins.property
    @jsii.member(jsii_name="integrationSubtype")
    def integration_subtype(self) -> typing.Optional[builtins.str]:
        '''Supported only for HTTP API ``AWS_PROXY`` integrations.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationSubtype"))

    @integration_subtype.setter
    def integration_subtype(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3bad3279c4a378ed62fbce1637f2a011d7a2661bced09041c61a0e4f83f4c3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationSubtype", value)

    @builtins.property
    @jsii.member(jsii_name="integrationUri")
    def integration_uri(self) -> typing.Optional[builtins.str]:
        '''For a Lambda integration, specify the URI of a Lambda function.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "integrationUri"))

    @integration_uri.setter
    def integration_uri(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cd111331771976544458360d1a6a3bad5e722f1484325d01c7bce109006e405)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationUri", value)

    @builtins.property
    @jsii.member(jsii_name="passthroughBehavior")
    def passthrough_behavior(self) -> typing.Optional[builtins.str]:
        '''Specifies the pass-through behavior for incoming requests based on the ``Content-Type`` header in the request, and the available mapping templates specified as the ``requestTemplates`` property on the ``Integration`` resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "passthroughBehavior"))

    @passthrough_behavior.setter
    def passthrough_behavior(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a727a930643734ff056002d99f5485b84de3c8a9714ff88c9ec6e4b4ed6b2609)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "passthroughBehavior", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersion")
    def payload_format_version(self) -> typing.Optional[builtins.str]:
        '''Specifies the format of the payload sent to an integration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "payloadFormatVersion"))

    @payload_format_version.setter
    def payload_format_version(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__16e1cdf41a9fbafec3a3f020dce252f9e906c5147a18a5fdd738f8075d840baa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadFormatVersion", value)

    @builtins.property
    @jsii.member(jsii_name="requestParameters")
    def request_parameters(self) -> typing.Any:
        '''For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend.'''
        return typing.cast(typing.Any, jsii.get(self, "requestParameters"))

    @request_parameters.setter
    def request_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a2e295280878c041c9a343d25c3d468f9c0db07048c247f5796a3bbcf24039)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestParameters", value)

    @builtins.property
    @jsii.member(jsii_name="requestTemplates")
    def request_templates(self) -> typing.Any:
        '''Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.'''
        return typing.cast(typing.Any, jsii.get(self, "requestTemplates"))

    @request_templates.setter
    def request_templates(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__101df28f0b4f486748827f04e36cb60e9930a7fcbc372f1a22e694f243437ba1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestTemplates", value)

    @builtins.property
    @jsii.member(jsii_name="responseParameters")
    def response_parameters(self) -> typing.Any:
        '''Supported only for HTTP APIs.'''
        return typing.cast(typing.Any, jsii.get(self, "responseParameters"))

    @response_parameters.setter
    def response_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f2c90c96ec7876c8a6c376c4c46707e575640a158942a5c3ead1572769175c15)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseParameters", value)

    @builtins.property
    @jsii.member(jsii_name="templateSelectionExpression")
    def template_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The template selection expression for the integration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateSelectionExpression"))

    @template_selection_expression.setter
    def template_selection_expression(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__09b070ac49ad358b1b6713b8e487d653fdf93ef9e4ad8b29c6d2348ec5347cb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="timeoutInMillis")
    def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
        '''Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "timeoutInMillis"))

    @timeout_in_millis.setter
    def timeout_in_millis(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2265ff6343fb7bb0629e72dfee180369b7d8341ec892b8f4c3180f1f615f5128)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "timeoutInMillis", value)

    @builtins.property
    @jsii.member(jsii_name="tlsConfig")
    def tls_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TlsConfigProperty"]]:
        '''The TLS configuration for a private integration.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TlsConfigProperty"]], jsii.get(self, "tlsConfig"))

    @tls_config.setter
    def tls_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnIntegration.TlsConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56ceb8ff581bdc4197d98dbf69a924ea37de46cfdd6f6f8c1a6c46a94c82e8b2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tlsConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegration.ResponseParameterListProperty",
        jsii_struct_bases=[],
        name_mapping={"response_parameters": "responseParameters"},
    )
    class ResponseParameterListProperty:
        def __init__(
            self,
            *,
            response_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnIntegration.ResponseParameterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Specifies a list of response parameters for an HTTP API.

            :param response_parameters: Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match the pattern ``<action>:<header>.<location>`` or ``overwrite.statuscode`` . The action can be ``append`` , ``overwrite`` or ``remove`` . The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                response_parameter_list_property = apigatewayv2.CfnIntegration.ResponseParameterListProperty(
                    response_parameters=[apigatewayv2.CfnIntegration.ResponseParameterProperty(
                        destination="destination",
                        source="source"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3dbe4af6ef419f3fca35eeefa87a09cafa7177216b644e69571fe9d05b2b0ed7)
                check_type(argname="argument response_parameters", value=response_parameters, expected_type=type_hints["response_parameters"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if response_parameters is not None:
                self._values["response_parameters"] = response_parameters

        @builtins.property
        def response_parameters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ResponseParameterProperty"]]]]:
            '''Supported only for HTTP APIs.

            You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match the pattern ``<action>:<header>.<location>`` or ``overwrite.statuscode`` . The action can be ``append`` , ``overwrite`` or ``remove`` . The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html#cfn-apigatewayv2-integration-responseparameterlist-responseparameters
            '''
            result = self._values.get("response_parameters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnIntegration.ResponseParameterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResponseParameterListProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegration.ResponseParameterProperty",
        jsii_struct_bases=[],
        name_mapping={"destination": "destination", "source": "source"},
    )
    class ResponseParameterProperty:
        def __init__(self, *, destination: builtins.str, source: builtins.str) -> None:
            '''Supported only for HTTP APIs.

            You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. Response parameters are a key-value map. The key must match the pattern ``<action>:<header>.<location>`` or ``overwrite.statuscode`` . The action can be ``append`` , ``overwrite`` or ``remove`` . The value can be a static value, or map to response data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

            :param destination: Specifies the location of the response to modify, and how to modify it. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .
            :param source: Specifies the data to update the parameter with. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                response_parameter_property = apigatewayv2.CfnIntegration.ResponseParameterProperty(
                    destination="destination",
                    source="source"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fe5d304364e2ba9a1fee328297e69bcc2440350e01f210541d4decfd2aff9755)
                check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
                check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "destination": destination,
                "source": source,
            }

        @builtins.property
        def destination(self) -> builtins.str:
            '''Specifies the location of the response to modify, and how to modify it.

            To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-destination
            '''
            result = self._values.get("destination")
            assert result is not None, "Required property 'destination' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source(self) -> builtins.str:
            '''Specifies the data to update the parameter with.

            To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameter.html#cfn-apigatewayv2-integration-responseparameter-source
            '''
            result = self._values.get("source")
            assert result is not None, "Required property 'source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ResponseParameterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegration.TlsConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"server_name_to_verify": "serverNameToVerify"},
    )
    class TlsConfigProperty:
        def __init__(
            self,
            *,
            server_name_to_verify: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The ``TlsConfig`` property specifies the TLS configuration for a private integration.

            If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

            :param server_name_to_verify: If you specify a server name, API Gateway uses it to verify the hostname on the integration's certificate. The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                tls_config_property = apigatewayv2.CfnIntegration.TlsConfigProperty(
                    server_name_to_verify="serverNameToVerify"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__33df515d85a59f496faf5c4df3725daf4904bdfdc12bedcbb859eda8bf55bb43)
                check_type(argname="argument server_name_to_verify", value=server_name_to_verify, expected_type=type_hints["server_name_to_verify"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if server_name_to_verify is not None:
                self._values["server_name_to_verify"] = server_name_to_verify

        @builtins.property
        def server_name_to_verify(self) -> typing.Optional[builtins.str]:
            '''If you specify a server name, API Gateway uses it to verify the hostname on the integration's certificate.

            The server name is also included in the TLS handshake to support Server Name Indication (SNI) or virtual hosting.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html#cfn-apigatewayv2-integration-tlsconfig-servernametoverify
            '''
            result = self._values.get("server_name_to_verify")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TlsConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "integration_type": "integrationType",
        "connection_id": "connectionId",
        "connection_type": "connectionType",
        "content_handling_strategy": "contentHandlingStrategy",
        "credentials_arn": "credentialsArn",
        "description": "description",
        "integration_method": "integrationMethod",
        "integration_subtype": "integrationSubtype",
        "integration_uri": "integrationUri",
        "passthrough_behavior": "passthroughBehavior",
        "payload_format_version": "payloadFormatVersion",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "response_parameters": "responseParameters",
        "template_selection_expression": "templateSelectionExpression",
        "timeout_in_millis": "timeoutInMillis",
        "tls_config": "tlsConfig",
    },
)
class CfnIntegrationProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        integration_type: builtins.str,
        connection_id: typing.Optional[builtins.str] = None,
        connection_type: typing.Optional[builtins.str] = None,
        content_handling_strategy: typing.Optional[builtins.str] = None,
        credentials_arn: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        integration_method: typing.Optional[builtins.str] = None,
        integration_subtype: typing.Optional[builtins.str] = None,
        integration_uri: typing.Optional[builtins.str] = None,
        passthrough_behavior: typing.Optional[builtins.str] = None,
        payload_format_version: typing.Optional[builtins.str] = None,
        request_parameters: typing.Any = None,
        request_templates: typing.Any = None,
        response_parameters: typing.Any = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
        timeout_in_millis: typing.Optional[jsii.Number] = None,
        tls_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TlsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnIntegration``.

        :param api_id: The API identifier.
        :param integration_type: The integration type of an integration. One of the following:. ``AWS`` : for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs. ``AWS_PROXY`` : for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration. ``HTTP`` : for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs. ``HTTP_PROXY`` : for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an ``HTTP_PROXY`` integration. ``MOCK`` : for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.
        :param connection_id: The ID of the VPC link for a private integration. Supported only for HTTP APIs.
        :param connection_type: The type of the network connection to the integration endpoint. Specify ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and resources in a VPC. The default value is ``INTERNET`` .
        :param content_handling_strategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors: ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob. ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string. If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :param credentials_arn: Specifies the credentials required for the integration, if any. For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::*:user/*`` . To use resource-based permissions on supported AWS services, don't specify this parameter.
        :param description: The description of the integration.
        :param integration_method: Specifies the integration's HTTP method type.
        :param integration_subtype: Supported only for HTTP API ``AWS_PROXY`` integrations. Specifies the AWS service action to invoke. To learn more, see `Integration subtype reference <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html>`_ .
        :param integration_uri: For a Lambda integration, specify the URI of a Lambda function. For an HTTP integration, specify a fully-qualified URL. For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses ``DiscoverInstances`` to identify resources. You can use query parameters to target specific resources. To learn more, see `DiscoverInstances <https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html>`_ . For private integrations, all resources must be owned by the same AWS account .
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the ``Content-Type`` header in the request, and the available mapping templates specified as the ``requestTemplates`` property on the ``Integration`` resource. There are three valid values: ``WHEN_NO_MATCH`` , ``WHEN_NO_TEMPLATES`` , and ``NEVER`` . Supported only for WebSocket APIs. ``WHEN_NO_MATCH`` passes the request body for unmapped content types through to the integration backend without transformation. ``NEVER`` rejects unmapped content types with an ``HTTP 415 Unsupported Media Type`` response. ``WHEN_NO_TEMPLATES`` allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same ``HTTP 415 Unsupported Media Type`` response.
        :param payload_format_version: Specifies the format of the payload sent to an integration. Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are ``1.0`` and ``2.0`` . For all other integrations, ``1.0`` is the only supported value. To learn more, see `Working with AWS Lambda proxy integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html>`_ .
        :param request_parameters: For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend. The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of ``method.request. {location} . {name}`` , where ``{location}`` is ``querystring`` , ``path`` , or ``header`` ; and ``{name}`` must be a valid and unique method request parameter name. For HTTP API integrations with a specified ``integrationSubtype`` , request parameters are a key-value map specifying parameters that are passed to ``AWS_PROXY`` integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Working with AWS service integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html>`_ . For HTTP API integrations without a specified ``integrationSubtype`` request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern :<header|querystring|path>. where action can be ``append`` , ``overwrite`` or ``remove`` . For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .
        :param request_templates: Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client. The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.
        :param response_parameters: Supported only for HTTP APIs. You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. The value is of type ```ResponseParameterList`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html>`_ . To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .
        :param template_selection_expression: The template selection expression for the integration. Supported only for WebSocket APIs.
        :param timeout_in_millis: Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs. The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.
        :param tls_config: The TLS configuration for a private integration. If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # request_parameters: Any
            # request_templates: Any
            # response_parameters: Any
            
            cfn_integration_props = apigatewayv2.CfnIntegrationProps(
                api_id="apiId",
                integration_type="integrationType",
            
                # the properties below are optional
                connection_id="connectionId",
                connection_type="connectionType",
                content_handling_strategy="contentHandlingStrategy",
                credentials_arn="credentialsArn",
                description="description",
                integration_method="integrationMethod",
                integration_subtype="integrationSubtype",
                integration_uri="integrationUri",
                passthrough_behavior="passthroughBehavior",
                payload_format_version="payloadFormatVersion",
                request_parameters=request_parameters,
                request_templates=request_templates,
                response_parameters=response_parameters,
                template_selection_expression="templateSelectionExpression",
                timeout_in_millis=123,
                tls_config=apigatewayv2.CfnIntegration.TlsConfigProperty(
                    server_name_to_verify="serverNameToVerify"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__959841762bab1a313d723cf36b281fcb4d5c0bb2f15ded3e0c7f38aaa97997c1)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument integration_type", value=integration_type, expected_type=type_hints["integration_type"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument connection_type", value=connection_type, expected_type=type_hints["connection_type"])
            check_type(argname="argument content_handling_strategy", value=content_handling_strategy, expected_type=type_hints["content_handling_strategy"])
            check_type(argname="argument credentials_arn", value=credentials_arn, expected_type=type_hints["credentials_arn"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument integration_method", value=integration_method, expected_type=type_hints["integration_method"])
            check_type(argname="argument integration_subtype", value=integration_subtype, expected_type=type_hints["integration_subtype"])
            check_type(argname="argument integration_uri", value=integration_uri, expected_type=type_hints["integration_uri"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument payload_format_version", value=payload_format_version, expected_type=type_hints["payload_format_version"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument response_parameters", value=response_parameters, expected_type=type_hints["response_parameters"])
            check_type(argname="argument template_selection_expression", value=template_selection_expression, expected_type=type_hints["template_selection_expression"])
            check_type(argname="argument timeout_in_millis", value=timeout_in_millis, expected_type=type_hints["timeout_in_millis"])
            check_type(argname="argument tls_config", value=tls_config, expected_type=type_hints["tls_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "integration_type": integration_type,
        }
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if connection_type is not None:
            self._values["connection_type"] = connection_type
        if content_handling_strategy is not None:
            self._values["content_handling_strategy"] = content_handling_strategy
        if credentials_arn is not None:
            self._values["credentials_arn"] = credentials_arn
        if description is not None:
            self._values["description"] = description
        if integration_method is not None:
            self._values["integration_method"] = integration_method
        if integration_subtype is not None:
            self._values["integration_subtype"] = integration_subtype
        if integration_uri is not None:
            self._values["integration_uri"] = integration_uri
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if payload_format_version is not None:
            self._values["payload_format_version"] = payload_format_version
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if response_parameters is not None:
            self._values["response_parameters"] = response_parameters
        if template_selection_expression is not None:
            self._values["template_selection_expression"] = template_selection_expression
        if timeout_in_millis is not None:
            self._values["timeout_in_millis"] = timeout_in_millis
        if tls_config is not None:
            self._values["tls_config"] = tls_config

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_type(self) -> builtins.str:
        '''The integration type of an integration. One of the following:.

        ``AWS`` : for integrating the route or method request with an AWS service action, including the Lambda function-invoking action. With the Lambda function-invoking action, this is referred to as the Lambda custom integration. With any other AWS service action, this is known as AWS integration. Supported only for WebSocket APIs.

        ``AWS_PROXY`` : for integrating the route or method request with a Lambda function or other AWS service action. This integration is also referred to as a Lambda proxy integration.

        ``HTTP`` : for integrating the route or method request with an HTTP endpoint. This integration is also referred to as the HTTP custom integration. Supported only for WebSocket APIs.

        ``HTTP_PROXY`` : for integrating the route or method request with an HTTP endpoint, with the client request passed through as-is. This is also referred to as HTTP proxy integration. For HTTP API private integrations, use an ``HTTP_PROXY`` integration.

        ``MOCK`` : for integrating the route or method request with API Gateway as a "loopback" endpoint without invoking any backend. Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationtype
        '''
        result = self._values.get("integration_type")
        assert result is not None, "Required property 'integration_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the VPC link for a private integration.

        Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectionid
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_type(self) -> typing.Optional[builtins.str]:
        '''The type of the network connection to the integration endpoint.

        Specify ``INTERNET`` for connections through the public routable internet or ``VPC_LINK`` for private connections between API Gateway and resources in a VPC. The default value is ``INTERNET`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-connectiontype
        '''
        result = self._values.get("connection_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def content_handling_strategy(self) -> typing.Optional[builtins.str]:
        '''Supported only for WebSocket APIs.

        Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

        ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.

        ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.

        If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-contenthandlingstrategy
        '''
        result = self._values.get("content_handling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def credentials_arn(self) -> typing.Optional[builtins.str]:
        '''Specifies the credentials required for the integration, if any.

        For AWS integrations, three options are available. To specify an IAM Role for API Gateway to assume, use the role's Amazon Resource Name (ARN). To require that the caller's identity be passed through from the request, specify the string ``arn:aws:iam::*:user/*`` . To use resource-based permissions on supported AWS services, don't specify this parameter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-credentialsarn
        '''
        result = self._values.get("credentials_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the integration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_method(self) -> typing.Optional[builtins.str]:
        '''Specifies the integration's HTTP method type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationmethod
        '''
        result = self._values.get("integration_method")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_subtype(self) -> typing.Optional[builtins.str]:
        '''Supported only for HTTP API ``AWS_PROXY`` integrations.

        Specifies the AWS service action to invoke. To learn more, see `Integration subtype reference <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services-reference.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationsubtype
        '''
        result = self._values.get("integration_subtype")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def integration_uri(self) -> typing.Optional[builtins.str]:
        '''For a Lambda integration, specify the URI of a Lambda function.

        For an HTTP integration, specify a fully-qualified URL.

        For an HTTP API private integration, specify the ARN of an Application Load Balancer listener, Network Load Balancer listener, or AWS Cloud Map service. If you specify the ARN of an AWS Cloud Map service, API Gateway uses ``DiscoverInstances`` to identify resources. You can use query parameters to target specific resources. To learn more, see `DiscoverInstances <https://docs.aws.amazon.com/cloud-map/latest/api/API_DiscoverInstances.html>`_ . For private integrations, all resources must be owned by the same AWS account .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-integrationuri
        '''
        result = self._values.get("integration_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def passthrough_behavior(self) -> typing.Optional[builtins.str]:
        '''Specifies the pass-through behavior for incoming requests based on the ``Content-Type`` header in the request, and the available mapping templates specified as the ``requestTemplates`` property on the ``Integration`` resource.

        There are three valid values: ``WHEN_NO_MATCH`` , ``WHEN_NO_TEMPLATES`` , and ``NEVER`` . Supported only for WebSocket APIs.

        ``WHEN_NO_MATCH`` passes the request body for unmapped content types through to the integration backend without transformation.

        ``NEVER`` rejects unmapped content types with an ``HTTP 415 Unsupported Media Type`` response.

        ``WHEN_NO_TEMPLATES`` allows pass-through when the integration has no content types mapped to templates. However, if there is at least one content type defined, unmapped content types will be rejected with the same ``HTTP 415 Unsupported Media Type`` response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-passthroughbehavior
        '''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def payload_format_version(self) -> typing.Optional[builtins.str]:
        '''Specifies the format of the payload sent to an integration.

        Required for HTTP APIs. For HTTP APIs, supported values for Lambda proxy integrations are ``1.0`` and ``2.0`` . For all other integrations, ``1.0`` is the only supported value. To learn more, see `Working with AWS Lambda proxy integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-payloadformatversion
        '''
        result = self._values.get("payload_format_version")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_parameters(self) -> typing.Any:
        '''For WebSocket APIs, a key-value map specifying request parameters that are passed from the method request to the backend.

        The key is an integration request parameter name and the associated value is a method request parameter value or static value that must be enclosed within single quotes and pre-encoded as required by the backend. The method request parameter value must match the pattern of ``method.request. {location} . {name}`` , where ``{location}`` is ``querystring`` , ``path`` , or ``header`` ; and ``{name}`` must be a valid and unique method request parameter name.

        For HTTP API integrations with a specified ``integrationSubtype`` , request parameters are a key-value map specifying parameters that are passed to ``AWS_PROXY`` integrations. You can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Working with AWS service integrations for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-aws-services.html>`_ .

        For HTTP API integrations without a specified ``integrationSubtype`` request parameters are a key-value map specifying how to transform HTTP requests before sending them to the backend. The key should follow the pattern :<header|querystring|path>. where action can be ``append`` , ``overwrite`` or ``remove`` . For values, you can provide static values, or map request data, stage variables, or context variables that are evaluated at runtime. To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requestparameters
        '''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def request_templates(self) -> typing.Any:
        '''Represents a map of Velocity templates that are applied on the request payload based on the value of the Content-Type header sent by the client.

        The content type value is the key in this map, and the template (as a String) is the value. Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-requesttemplates
        '''
        result = self._values.get("request_templates")
        return typing.cast(typing.Any, result)

    @builtins.property
    def response_parameters(self) -> typing.Any:
        '''Supported only for HTTP APIs.

        You use response parameters to transform the HTTP response from a backend integration before returning the response to clients. Specify a key-value map from a selection key to response parameters. The selection key must be a valid HTTP status code within the range of 200-599. The value is of type ```ResponseParameterList`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-responseparameterlist.html>`_ . To learn more, see `Transforming API requests and responses <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-responseparameters
        '''
        result = self._values.get("response_parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The template selection expression for the integration.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-templateselectionexpression
        '''
        result = self._values.get("template_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout_in_millis(self) -> typing.Optional[jsii.Number]:
        '''Custom timeout between 50 and 29,000 milliseconds for WebSocket APIs and between 50 and 30,000 milliseconds for HTTP APIs.

        The default timeout is 29 seconds for WebSocket APIs and 30 seconds for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-timeoutinmillis
        '''
        result = self._values.get("timeout_in_millis")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def tls_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.TlsConfigProperty]]:
        '''The TLS configuration for a private integration.

        If you specify a TLS configuration, private integration traffic uses the HTTPS protocol. Supported only for HTTP APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integration.html#cfn-apigatewayv2-integration-tlsconfig
        '''
        result = self._values.get("tls_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.TlsConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnIntegrationResponse(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegrationResponse",
):
    '''The ``AWS::ApiGatewayV2::IntegrationResponse`` resource updates an integration response for an WebSocket API.

    For more information, see `Set up WebSocket API Integration Responses in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-integration-responses.html>`_ in the *API Gateway Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # response_parameters: Any
        # response_templates: Any
        
        cfn_integration_response = apigatewayv2.CfnIntegrationResponse(self, "MyCfnIntegrationResponse",
            api_id="apiId",
            integration_id="integrationId",
            integration_response_key="integrationResponseKey",
        
            # the properties below are optional
            content_handling_strategy="contentHandlingStrategy",
            response_parameters=response_parameters,
            response_templates=response_templates,
            template_selection_expression="templateSelectionExpression"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        integration_id: builtins.str,
        integration_response_key: builtins.str,
        content_handling_strategy: typing.Optional[builtins.str] = None,
        response_parameters: typing.Any = None,
        response_templates: typing.Any = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param integration_id: The integration ID.
        :param integration_response_key: The integration response key.
        :param content_handling_strategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors: ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob. ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string. If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :param response_parameters: A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header. *{name}*`` , where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header. *{name}*`` or ``integration.response.body. *{JSON-expression}*`` , where ``*{name}*`` is a valid and unique response header name and ``*{JSON-expression}*`` is a valid JSON expression without the ``$`` prefix.
        :param response_templates: The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
        :param template_selection_expression: The template selection expression for the integration response. Supported only for WebSocket APIs.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3073dfa88ecd48398fee93e5529ed75a9739534bd3b09ae3db2434d1d7330349)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnIntegrationResponseProps(
            api_id=api_id,
            integration_id=integration_id,
            integration_response_key=integration_response_key,
            content_handling_strategy=content_handling_strategy,
            response_parameters=response_parameters,
            response_templates=response_templates,
            template_selection_expression=template_selection_expression,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9eb8a7a88b16046fe04b3947f00ae23d6f9d961c6d7e9537f31bb0a6a85ea14)
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
            type_hints = typing.get_type_hints(_typecheckingstub__7c355c31fef694ade9a614c0a6d364f0f220effb67f50cfb01812e98200801ef)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIntegrationResponseId")
    def attr_integration_response_id(self) -> builtins.str:
        '''The integration response ID.

        :cloudformationAttribute: IntegrationResponseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIntegrationResponseId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99fea032bb48ce29028df074824542352a22c09d235ca01d0b3c55e23f7c3b92)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationId")
    def integration_id(self) -> builtins.str:
        '''The integration ID.'''
        return typing.cast(builtins.str, jsii.get(self, "integrationId"))

    @integration_id.setter
    def integration_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cdf5a2e36e17c7956158792201f399023d1254bba7b297a2ba1de3687f4b7b99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationId", value)

    @builtins.property
    @jsii.member(jsii_name="integrationResponseKey")
    def integration_response_key(self) -> builtins.str:
        '''The integration response key.'''
        return typing.cast(builtins.str, jsii.get(self, "integrationResponseKey"))

    @integration_response_key.setter
    def integration_response_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8059eca870e9610a9500cc304aaeb602575652ebbc3fe0ab8399e773b218fef)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationResponseKey", value)

    @builtins.property
    @jsii.member(jsii_name="contentHandlingStrategy")
    def content_handling_strategy(self) -> typing.Optional[builtins.str]:
        '''Supported only for WebSocket APIs.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentHandlingStrategy"))

    @content_handling_strategy.setter
    def content_handling_strategy(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1fa5320f9dd58af11d49e6707ba435d74bd31b41b5f0cc79f4306bfd30a79a28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentHandlingStrategy", value)

    @builtins.property
    @jsii.member(jsii_name="responseParameters")
    def response_parameters(self) -> typing.Any:
        '''A key-value map specifying response parameters that are passed to the method response from the backend.'''
        return typing.cast(typing.Any, jsii.get(self, "responseParameters"))

    @response_parameters.setter
    def response_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2575e266b0e74bc1ed655a2ba782d189b25474ca18b53d97c2003730abca92ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseParameters", value)

    @builtins.property
    @jsii.member(jsii_name="responseTemplates")
    def response_templates(self) -> typing.Any:
        '''The collection of response templates for the integration response as a string-to-string map of key-value pairs.'''
        return typing.cast(typing.Any, jsii.get(self, "responseTemplates"))

    @response_templates.setter
    def response_templates(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a3ba7c35e06acda935a23473c90cfa001239c682c8737d897cf6ec207fd49cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseTemplates", value)

    @builtins.property
    @jsii.member(jsii_name="templateSelectionExpression")
    def template_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The template selection expression for the integration response.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "templateSelectionExpression"))

    @template_selection_expression.setter
    def template_selection_expression(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cf04d9ff614e1130ca1b37b22fad9aecf0edfc31b0571b48e6cd2eb3a838e25)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "templateSelectionExpression", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnIntegrationResponseProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "integration_id": "integrationId",
        "integration_response_key": "integrationResponseKey",
        "content_handling_strategy": "contentHandlingStrategy",
        "response_parameters": "responseParameters",
        "response_templates": "responseTemplates",
        "template_selection_expression": "templateSelectionExpression",
    },
)
class CfnIntegrationResponseProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        integration_id: builtins.str,
        integration_response_key: builtins.str,
        content_handling_strategy: typing.Optional[builtins.str] = None,
        response_parameters: typing.Any = None,
        response_templates: typing.Any = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnIntegrationResponse``.

        :param api_id: The API identifier.
        :param integration_id: The integration ID.
        :param integration_response_key: The integration response key.
        :param content_handling_strategy: Supported only for WebSocket APIs. Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors: ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob. ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string. If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.
        :param response_parameters: A key-value map specifying response parameters that are passed to the method response from the backend. The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header. *{name}*`` , where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header. *{name}*`` or ``integration.response.body. *{JSON-expression}*`` , where ``*{name}*`` is a valid and unique response header name and ``*{JSON-expression}*`` is a valid JSON expression without the ``$`` prefix.
        :param response_templates: The collection of response templates for the integration response as a string-to-string map of key-value pairs. Response templates are represented as a key/value map, with a content-type as the key and a template as the value.
        :param template_selection_expression: The template selection expression for the integration response. Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # response_parameters: Any
            # response_templates: Any
            
            cfn_integration_response_props = apigatewayv2.CfnIntegrationResponseProps(
                api_id="apiId",
                integration_id="integrationId",
                integration_response_key="integrationResponseKey",
            
                # the properties below are optional
                content_handling_strategy="contentHandlingStrategy",
                response_parameters=response_parameters,
                response_templates=response_templates,
                template_selection_expression="templateSelectionExpression"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ac9393ea8482959d9abf755d543e025afdf5cabf2379a474cfb607ced90a7d)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument integration_id", value=integration_id, expected_type=type_hints["integration_id"])
            check_type(argname="argument integration_response_key", value=integration_response_key, expected_type=type_hints["integration_response_key"])
            check_type(argname="argument content_handling_strategy", value=content_handling_strategy, expected_type=type_hints["content_handling_strategy"])
            check_type(argname="argument response_parameters", value=response_parameters, expected_type=type_hints["response_parameters"])
            check_type(argname="argument response_templates", value=response_templates, expected_type=type_hints["response_templates"])
            check_type(argname="argument template_selection_expression", value=template_selection_expression, expected_type=type_hints["template_selection_expression"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "integration_id": integration_id,
            "integration_response_key": integration_response_key,
        }
        if content_handling_strategy is not None:
            self._values["content_handling_strategy"] = content_handling_strategy
        if response_parameters is not None:
            self._values["response_parameters"] = response_parameters
        if response_templates is not None:
            self._values["response_templates"] = response_templates
        if template_selection_expression is not None:
            self._values["template_selection_expression"] = template_selection_expression

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_id(self) -> builtins.str:
        '''The integration ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationid
        '''
        result = self._values.get("integration_id")
        assert result is not None, "Required property 'integration_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_response_key(self) -> builtins.str:
        '''The integration response key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-integrationresponsekey
        '''
        result = self._values.get("integration_response_key")
        assert result is not None, "Required property 'integration_response_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_handling_strategy(self) -> typing.Optional[builtins.str]:
        '''Supported only for WebSocket APIs.

        Specifies how to handle response payload content type conversions. Supported values are ``CONVERT_TO_BINARY`` and ``CONVERT_TO_TEXT`` , with the following behaviors:

        ``CONVERT_TO_BINARY`` : Converts a response payload from a Base64-encoded string to the corresponding binary blob.

        ``CONVERT_TO_TEXT`` : Converts a response payload from a binary blob to a Base64-encoded string.

        If this property is not defined, the response payload will be passed through from the integration response to the route response or method response without modification.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-contenthandlingstrategy
        '''
        result = self._values.get("content_handling_strategy")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_parameters(self) -> typing.Any:
        '''A key-value map specifying response parameters that are passed to the method response from the backend.

        The key is a method response header parameter name and the mapped value is an integration response header value, a static value enclosed within a pair of single quotes, or a JSON expression from the integration response body. The mapping key must match the pattern of ``method.response.header. *{name}*`` , where name is a valid and unique header name. The mapped non-static value must match the pattern of ``integration.response.header. *{name}*`` or ``integration.response.body. *{JSON-expression}*`` , where ``*{name}*`` is a valid and unique response header name and ``*{JSON-expression}*`` is a valid JSON expression without the ``$`` prefix.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responseparameters
        '''
        result = self._values.get("response_parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def response_templates(self) -> typing.Any:
        '''The collection of response templates for the integration response as a string-to-string map of key-value pairs.

        Response templates are represented as a key/value map, with a content-type as the key and a template as the value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-responsetemplates
        '''
        result = self._values.get("response_templates")
        return typing.cast(typing.Any, result)

    @builtins.property
    def template_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The template selection expression for the integration response.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-integrationresponse.html#cfn-apigatewayv2-integrationresponse-templateselectionexpression
        '''
        result = self._values.get("template_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnIntegrationResponseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnModel(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnModel",
):
    '''The ``AWS::ApiGatewayV2::Model`` resource updates data model for a WebSocket API.

    For more information, see `Model Selection Expressions <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-selection-expressions.html#apigateway-websocket-api-model-selection-expressions>`_ in the *API Gateway Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # schema: Any
        
        cfn_model = apigatewayv2.CfnModel(self, "MyCfnModel",
            api_id="apiId",
            name="name",
            schema=schema,
        
            # the properties below are optional
            content_type="contentType",
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        name: builtins.str,
        schema: typing.Any,
        content_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param name: The name of the model.
        :param schema: The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :param content_type: The content-type for the model, for example, "application/json".
        :param description: The description of the model.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6ccae01e5e00deb4abf47fade1fc44a9e24a6b132f346a2168e61859b0fd0f9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnModelProps(
            api_id=api_id,
            name=name,
            schema=schema,
            content_type=content_type,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__614a93ac0501ec7b30c025d62a3fb8396af011528fee2dfdf92a02c0f03cb4f6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__094e778f5596bd0c50f977ede46b679b30895ef9e7437e30638ba85c8324aa5a)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrModelId")
    def attr_model_id(self) -> builtins.str:
        '''The model ID.

        :cloudformationAttribute: ModelId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrModelId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd7208082e475506377665abd7f89515f9cd05cb4a805ac3d22330cf7717506a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the model.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fc2be804afd386603717c4be503b6428d5db3793acae35866859f65b5633bd9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> typing.Any:
        '''The schema for the model.'''
        return typing.cast(typing.Any, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a9ac80c16be2c7876398f311a65e5d43fc4f955ae556019897effbfac12b594)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="contentType")
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The content-type for the model, for example, "application/json".'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contentType"))

    @content_type.setter
    def content_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0927afd42ecf7d6a1d74ddcea4ee74039cff8c61540dd3db8f4d477df2b2dbf8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contentType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the model.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c31bf4c0f98d1cb3fa2591344d5a2ba5243703029f6fd8f52ee51debcac4b197)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnModelProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "name": "name",
        "schema": "schema",
        "content_type": "contentType",
        "description": "description",
    },
)
class CfnModelProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        name: builtins.str,
        schema: typing.Any,
        content_type: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnModel``.

        :param api_id: The API identifier.
        :param name: The name of the model.
        :param schema: The schema for the model. For application/json models, this should be JSON schema draft 4 model.
        :param content_type: The content-type for the model, for example, "application/json".
        :param description: The description of the model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # schema: Any
            
            cfn_model_props = apigatewayv2.CfnModelProps(
                api_id="apiId",
                name="name",
                schema=schema,
            
                # the properties below are optional
                content_type="contentType",
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__94458d573335422ed4ef0420d5707527a083fd922a556e7e5cf9d2df4b6b770b)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument content_type", value=content_type, expected_type=type_hints["content_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "name": name,
            "schema": schema,
        }
        if content_type is not None:
            self._values["content_type"] = content_type
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def schema(self) -> typing.Any:
        '''The schema for the model.

        For application/json models, this should be JSON schema draft 4 model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-schema
        '''
        result = self._values.get("schema")
        assert result is not None, "Required property 'schema' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def content_type(self) -> typing.Optional[builtins.str]:
        '''The content-type for the model, for example, "application/json".

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-contenttype
        '''
        result = self._values.get("content_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the model.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-model.html#cfn-apigatewayv2-model-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnModelProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRoute(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnRoute",
):
    '''The ``AWS::ApiGatewayV2::Route`` resource creates a route for an API.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # request_models: Any
        # request_parameters: Any
        
        cfn_route = apigatewayv2.CfnRoute(self, "MyCfnRoute",
            api_id="apiId",
            route_key="routeKey",
        
            # the properties below are optional
            api_key_required=False,
            authorization_scopes=["authorizationScopes"],
            authorization_type="authorizationType",
            authorizer_id="authorizerId",
            model_selection_expression="modelSelectionExpression",
            operation_name="operationName",
            request_models=request_models,
            request_parameters=request_parameters,
            route_response_selection_expression="routeResponseSelectionExpression",
            target="target"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        route_key: builtins.str,
        api_key_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        authorization_type: typing.Optional[builtins.str] = None,
        authorizer_id: typing.Optional[builtins.str] = None,
        model_selection_expression: typing.Optional[builtins.str] = None,
        operation_name: typing.Optional[builtins.str] = None,
        request_models: typing.Any = None,
        request_parameters: typing.Any = None,
        route_response_selection_expression: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param route_key: The route key for the route. For HTTP APIs, the route key can be either ``$default`` , or a combination of an HTTP method and resource path, for example, ``GET /pets`` .
        :param api_key_required: Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        :param authorization_scopes: The authorization scopes supported by this route.
        :param authorization_type: The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        :param authorizer_id: The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        :param model_selection_expression: The model selection expression for the route. Supported only for WebSocket APIs.
        :param operation_name: The operation name for the route.
        :param request_models: The request models for the route. Supported only for WebSocket APIs.
        :param request_parameters: The request parameters for the route. Supported only for WebSocket APIs.
        :param route_response_selection_expression: The route response selection expression for the route. Supported only for WebSocket APIs.
        :param target: The target for the route.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__684f667963694c8b4dd362278e6d43f4e671fbdd6c30e9164a05a537ed94abfc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouteProps(
            api_id=api_id,
            route_key=route_key,
            api_key_required=api_key_required,
            authorization_scopes=authorization_scopes,
            authorization_type=authorization_type,
            authorizer_id=authorizer_id,
            model_selection_expression=model_selection_expression,
            operation_name=operation_name,
            request_models=request_models,
            request_parameters=request_parameters,
            route_response_selection_expression=route_response_selection_expression,
            target=target,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__320c6e2f5cab38967ffd9b0ed4b2ddc789a3410d286b29ec51e096ae927441dc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__32a26d4ab03701420baf53d66a1006c11e7600abd1e7af917d90a4992ed19eeb)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRouteId")
    def attr_route_id(self) -> builtins.str:
        '''The route ID.

        :cloudformationAttribute: RouteId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRouteId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__817ae6943537234b9b4f8b1026eb08df9aa3dcc5a4a3d2e1bcdaccb4c8859013)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="routeKey")
    def route_key(self) -> builtins.str:
        '''The route key for the route.'''
        return typing.cast(builtins.str, jsii.get(self, "routeKey"))

    @route_key.setter
    def route_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b1b526cae660647aa14081711ec4c4c83f9f47ffa9d750a776fd3cca7a492415)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeKey", value)

    @builtins.property
    @jsii.member(jsii_name="apiKeyRequired")
    def api_key_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether an API key is required for the route.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "apiKeyRequired"))

    @api_key_required.setter
    def api_key_required(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__358b8c173a385a0f2f4df063725f0a0c0994b4367e7ee327094d60be73d0159b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiKeyRequired", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationScopes")
    def authorization_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The authorization scopes supported by this route.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "authorizationScopes"))

    @authorization_scopes.setter
    def authorization_scopes(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd8ccd7b07196f3b620d34a517b46ebd7d064a73896e86a7708c2f852454a3c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationScopes", value)

    @builtins.property
    @jsii.member(jsii_name="authorizationType")
    def authorization_type(self) -> typing.Optional[builtins.str]:
        '''The authorization type for the route.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizationType"))

    @authorization_type.setter
    def authorization_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__710b2a2b6379ef5ced6134bab0acb3a139eae146d1637c631fa1ac82e1293aa5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizationType", value)

    @builtins.property
    @jsii.member(jsii_name="authorizerId")
    def authorizer_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the ``Authorizer`` resource to be associated with this route.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "authorizerId"))

    @authorizer_id.setter
    def authorizer_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__207cf5963882c49224627f6fb3fd59f643cdf1d90254c55bb502b2ed93138b09)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "authorizerId", value)

    @builtins.property
    @jsii.member(jsii_name="modelSelectionExpression")
    def model_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The model selection expression for the route.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelSelectionExpression"))

    @model_selection_expression.setter
    def model_selection_expression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b8705da16da23f26d861473096719d972912648ca74dd5bb739b97403054a0f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="operationName")
    def operation_name(self) -> typing.Optional[builtins.str]:
        '''The operation name for the route.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operationName"))

    @operation_name.setter
    def operation_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8135ad6e2375b25f70679c06db1891227be6c2f927872bf884a88cc18e03968e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operationName", value)

    @builtins.property
    @jsii.member(jsii_name="requestModels")
    def request_models(self) -> typing.Any:
        '''The request models for the route.'''
        return typing.cast(typing.Any, jsii.get(self, "requestModels"))

    @request_models.setter
    def request_models(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__966777ea62e0e3d128249c9c19b073476ddd0fe229b79943181b9727a164557d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestModels", value)

    @builtins.property
    @jsii.member(jsii_name="requestParameters")
    def request_parameters(self) -> typing.Any:
        '''The request parameters for the route.'''
        return typing.cast(typing.Any, jsii.get(self, "requestParameters"))

    @request_parameters.setter
    def request_parameters(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__435eeaef03289d500227b42f18979b36e67086e9d93768b135e26be8fd96d93c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requestParameters", value)

    @builtins.property
    @jsii.member(jsii_name="routeResponseSelectionExpression")
    def route_response_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The route response selection expression for the route.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "routeResponseSelectionExpression"))

    @route_response_selection_expression.setter
    def route_response_selection_expression(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bf161d094c7f77313e160a547c5e5314f99a3b8acd6fe48762a098ff337f142d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeResponseSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="target")
    def target(self) -> typing.Optional[builtins.str]:
        '''The target for the route.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "target"))

    @target.setter
    def target(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__11684b3d73b34e31f947a907e002a5a3f8deadc5f5d21850e1751afa90ceb81e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "target", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnRoute.ParameterConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={"required": "required"},
    )
    class ParameterConstraintsProperty:
        def __init__(
            self,
            *,
            required: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''
            :param required: 

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                parameter_constraints_property = apigatewayv2.CfnRoute.ParameterConstraintsProperty(
                    required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a20f7e0c1183a32a2b6d2b5daf9aa8b640963d055ad89eddfe0a955d42b69cd8)
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "required": required,
            }

        @builtins.property
        def required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-route-parameterconstraints.html#cfn-apigatewayv2-route-parameterconstraints-required
            '''
            result = self._values.get("required")
            assert result is not None, "Required property 'required' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnRouteProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "route_key": "routeKey",
        "api_key_required": "apiKeyRequired",
        "authorization_scopes": "authorizationScopes",
        "authorization_type": "authorizationType",
        "authorizer_id": "authorizerId",
        "model_selection_expression": "modelSelectionExpression",
        "operation_name": "operationName",
        "request_models": "requestModels",
        "request_parameters": "requestParameters",
        "route_response_selection_expression": "routeResponseSelectionExpression",
        "target": "target",
    },
)
class CfnRouteProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        route_key: builtins.str,
        api_key_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
        authorization_type: typing.Optional[builtins.str] = None,
        authorizer_id: typing.Optional[builtins.str] = None,
        model_selection_expression: typing.Optional[builtins.str] = None,
        operation_name: typing.Optional[builtins.str] = None,
        request_models: typing.Any = None,
        request_parameters: typing.Any = None,
        route_response_selection_expression: typing.Optional[builtins.str] = None,
        target: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoute``.

        :param api_id: The API identifier.
        :param route_key: The route key for the route. For HTTP APIs, the route key can be either ``$default`` , or a combination of an HTTP method and resource path, for example, ``GET /pets`` .
        :param api_key_required: Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
        :param authorization_scopes: The authorization scopes supported by this route.
        :param authorization_type: The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
        :param authorizer_id: The identifier of the ``Authorizer`` resource to be associated with this route. The authorizer identifier is generated by API Gateway when you created the authorizer.
        :param model_selection_expression: The model selection expression for the route. Supported only for WebSocket APIs.
        :param operation_name: The operation name for the route.
        :param request_models: The request models for the route. Supported only for WebSocket APIs.
        :param request_parameters: The request parameters for the route. Supported only for WebSocket APIs.
        :param route_response_selection_expression: The route response selection expression for the route. Supported only for WebSocket APIs.
        :param target: The target for the route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # request_models: Any
            # request_parameters: Any
            
            cfn_route_props = apigatewayv2.CfnRouteProps(
                api_id="apiId",
                route_key="routeKey",
            
                # the properties below are optional
                api_key_required=False,
                authorization_scopes=["authorizationScopes"],
                authorization_type="authorizationType",
                authorizer_id="authorizerId",
                model_selection_expression="modelSelectionExpression",
                operation_name="operationName",
                request_models=request_models,
                request_parameters=request_parameters,
                route_response_selection_expression="routeResponseSelectionExpression",
                target="target"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2628a47509f0aa7b326e157f1d321ae5bb9aee16e4672e277cea07a7f37adcba)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument route_key", value=route_key, expected_type=type_hints["route_key"])
            check_type(argname="argument api_key_required", value=api_key_required, expected_type=type_hints["api_key_required"])
            check_type(argname="argument authorization_scopes", value=authorization_scopes, expected_type=type_hints["authorization_scopes"])
            check_type(argname="argument authorization_type", value=authorization_type, expected_type=type_hints["authorization_type"])
            check_type(argname="argument authorizer_id", value=authorizer_id, expected_type=type_hints["authorizer_id"])
            check_type(argname="argument model_selection_expression", value=model_selection_expression, expected_type=type_hints["model_selection_expression"])
            check_type(argname="argument operation_name", value=operation_name, expected_type=type_hints["operation_name"])
            check_type(argname="argument request_models", value=request_models, expected_type=type_hints["request_models"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument route_response_selection_expression", value=route_response_selection_expression, expected_type=type_hints["route_response_selection_expression"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "route_key": route_key,
        }
        if api_key_required is not None:
            self._values["api_key_required"] = api_key_required
        if authorization_scopes is not None:
            self._values["authorization_scopes"] = authorization_scopes
        if authorization_type is not None:
            self._values["authorization_type"] = authorization_type
        if authorizer_id is not None:
            self._values["authorizer_id"] = authorizer_id
        if model_selection_expression is not None:
            self._values["model_selection_expression"] = model_selection_expression
        if operation_name is not None:
            self._values["operation_name"] = operation_name
        if request_models is not None:
            self._values["request_models"] = request_models
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if route_response_selection_expression is not None:
            self._values["route_response_selection_expression"] = route_response_selection_expression
        if target is not None:
            self._values["target"] = target

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_key(self) -> builtins.str:
        '''The route key for the route.

        For HTTP APIs, the route key can be either ``$default`` , or a combination of an HTTP method and resource path, for example, ``GET /pets`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routekey
        '''
        result = self._values.get("route_key")
        assert result is not None, "Required property 'route_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_key_required(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether an API key is required for the route.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-apikeyrequired
        '''
        result = self._values.get("api_key_required")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def authorization_scopes(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The authorization scopes supported by this route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationscopes
        '''
        result = self._values.get("authorization_scopes")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def authorization_type(self) -> typing.Optional[builtins.str]:
        '''The authorization type for the route.

        For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizationtype
        '''
        result = self._values.get("authorization_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def authorizer_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of the ``Authorizer`` resource to be associated with this route.

        The authorizer identifier is generated by API Gateway when you created the authorizer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-authorizerid
        '''
        result = self._values.get("authorizer_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def model_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The model selection expression for the route.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-modelselectionexpression
        '''
        result = self._values.get("model_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def operation_name(self) -> typing.Optional[builtins.str]:
        '''The operation name for the route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-operationname
        '''
        result = self._values.get("operation_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def request_models(self) -> typing.Any:
        '''The request models for the route.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestmodels
        '''
        result = self._values.get("request_models")
        return typing.cast(typing.Any, result)

    @builtins.property
    def request_parameters(self) -> typing.Any:
        '''The request parameters for the route.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-requestparameters
        '''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Any, result)

    @builtins.property
    def route_response_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The route response selection expression for the route.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-routeresponseselectionexpression
        '''
        result = self._values.get("route_response_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def target(self) -> typing.Optional[builtins.str]:
        '''The target for the route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-route.html#cfn-apigatewayv2-route-target
        '''
        result = self._values.get("target")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRouteResponse(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnRouteResponse",
):
    '''The ``AWS::ApiGatewayV2::RouteResponse`` resource creates a route response for a WebSocket API.

    For more information, see `Set up Route Responses for a WebSocket API in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-websocket-api-route-response.html>`_ in the *API Gateway Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # response_models: Any
        
        cfn_route_response = apigatewayv2.CfnRouteResponse(self, "MyCfnRouteResponse",
            api_id="apiId",
            route_id="routeId",
            route_response_key="routeResponseKey",
        
            # the properties below are optional
            model_selection_expression="modelSelectionExpression",
            response_models=response_models,
            response_parameters={
                "response_parameters_key": apigatewayv2.CfnRouteResponse.ParameterConstraintsProperty(
                    required=False
                )
            }
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        route_id: builtins.str,
        route_response_key: builtins.str,
        model_selection_expression: typing.Optional[builtins.str] = None,
        response_models: typing.Any = None,
        response_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union["CfnRouteResponse.ParameterConstraintsProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param route_id: The route ID.
        :param route_response_key: The route response key.
        :param model_selection_expression: The model selection expression for the route response. Supported only for WebSocket APIs.
        :param response_models: The response models for the route response.
        :param response_parameters: The route response parameters.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfaf600ddc8caeb97e41fee38b4de9c8fb9d185fa3ec18942f79f3893b8bef51)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouteResponseProps(
            api_id=api_id,
            route_id=route_id,
            route_response_key=route_response_key,
            model_selection_expression=model_selection_expression,
            response_models=response_models,
            response_parameters=response_parameters,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__396915a95af209f92313053f98eabbb48e49ef4061931d44d85f72ccb908b7e2)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8b989b0d6859022f53c1b5edba59217d08a86f1ab1fb99ae706e99fd946229fc)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrRouteResponseId")
    def attr_route_response_id(self) -> builtins.str:
        '''The route response ID.

        :cloudformationAttribute: RouteResponseId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRouteResponseId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80374cb7a6bb214c9c92bb6ddb083cdbcef83f46270a64db85109a45c17759c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="routeId")
    def route_id(self) -> builtins.str:
        '''The route ID.'''
        return typing.cast(builtins.str, jsii.get(self, "routeId"))

    @route_id.setter
    def route_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__592e3a33ad0f2f9f26c7e2f768d47cf4ce3fc02a4163624603480e3ae1b33c63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeId", value)

    @builtins.property
    @jsii.member(jsii_name="routeResponseKey")
    def route_response_key(self) -> builtins.str:
        '''The route response key.'''
        return typing.cast(builtins.str, jsii.get(self, "routeResponseKey"))

    @route_response_key.setter
    def route_response_key(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__210ce20ec5517850582ca60d34b2b638e220326969bfa6897b7d1a0636a92361)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeResponseKey", value)

    @builtins.property
    @jsii.member(jsii_name="modelSelectionExpression")
    def model_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The model selection expression for the route response.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelSelectionExpression"))

    @model_selection_expression.setter
    def model_selection_expression(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__903fde614a75269b08834aec81261c81e5c574a3af3db707d8cd7b207129a670)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelSelectionExpression", value)

    @builtins.property
    @jsii.member(jsii_name="responseModels")
    def response_models(self) -> typing.Any:
        '''The response models for the route response.'''
        return typing.cast(typing.Any, jsii.get(self, "responseModels"))

    @response_models.setter
    def response_models(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__03faecb8792316337b34af5c47692d7e5866e563a65e7afcbfc9043d35b8f42c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseModels", value)

    @builtins.property
    @jsii.member(jsii_name="responseParameters")
    def response_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRouteResponse.ParameterConstraintsProperty"]]]]:
        '''The route response parameters.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRouteResponse.ParameterConstraintsProperty"]]]], jsii.get(self, "responseParameters"))

    @response_parameters.setter
    def response_parameters(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, "CfnRouteResponse.ParameterConstraintsProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fadfcdb67c25b7fc23ab64866f4161b7cde8c566e504b8aa2a58d0798ecfab7a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "responseParameters", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnRouteResponse.ParameterConstraintsProperty",
        jsii_struct_bases=[],
        name_mapping={"required": "required"},
    )
    class ParameterConstraintsProperty:
        def __init__(
            self,
            *,
            required: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''Specifies whether the parameter is required.

            :param required: Specifies whether the parameter is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                parameter_constraints_property = apigatewayv2.CfnRouteResponse.ParameterConstraintsProperty(
                    required=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0b539ced1929d65d764bbe6c2bdf11baa4f870e1b409230563c2613a25e709e7)
                check_type(argname="argument required", value=required, expected_type=type_hints["required"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "required": required,
            }

        @builtins.property
        def required(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Specifies whether the parameter is required.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-routeresponse-parameterconstraints.html#cfn-apigatewayv2-routeresponse-parameterconstraints-required
            '''
            result = self._values.get("required")
            assert result is not None, "Required property 'required' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ParameterConstraintsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnRouteResponseProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "route_id": "routeId",
        "route_response_key": "routeResponseKey",
        "model_selection_expression": "modelSelectionExpression",
        "response_models": "responseModels",
        "response_parameters": "responseParameters",
    },
)
class CfnRouteResponseProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        route_id: builtins.str,
        route_response_key: builtins.str,
        model_selection_expression: typing.Optional[builtins.str] = None,
        response_models: typing.Any = None,
        response_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouteResponse.ParameterConstraintsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRouteResponse``.

        :param api_id: The API identifier.
        :param route_id: The route ID.
        :param route_response_key: The route response key.
        :param model_selection_expression: The model selection expression for the route response. Supported only for WebSocket APIs.
        :param response_models: The response models for the route response.
        :param response_parameters: The route response parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # response_models: Any
            
            cfn_route_response_props = apigatewayv2.CfnRouteResponseProps(
                api_id="apiId",
                route_id="routeId",
                route_response_key="routeResponseKey",
            
                # the properties below are optional
                model_selection_expression="modelSelectionExpression",
                response_models=response_models,
                response_parameters={
                    "response_parameters_key": apigatewayv2.CfnRouteResponse.ParameterConstraintsProperty(
                        required=False
                    )
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3357f1247faebabfedb5db2b33a7b9038414306326813b06294bdc9f355e50bb)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument route_id", value=route_id, expected_type=type_hints["route_id"])
            check_type(argname="argument route_response_key", value=route_response_key, expected_type=type_hints["route_response_key"])
            check_type(argname="argument model_selection_expression", value=model_selection_expression, expected_type=type_hints["model_selection_expression"])
            check_type(argname="argument response_models", value=response_models, expected_type=type_hints["response_models"])
            check_type(argname="argument response_parameters", value=response_parameters, expected_type=type_hints["response_parameters"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "route_id": route_id,
            "route_response_key": route_response_key,
        }
        if model_selection_expression is not None:
            self._values["model_selection_expression"] = model_selection_expression
        if response_models is not None:
            self._values["response_models"] = response_models
        if response_parameters is not None:
            self._values["response_parameters"] = response_parameters

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_id(self) -> builtins.str:
        '''The route ID.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeid
        '''
        result = self._values.get("route_id")
        assert result is not None, "Required property 'route_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_response_key(self) -> builtins.str:
        '''The route response key.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-routeresponsekey
        '''
        result = self._values.get("route_response_key")
        assert result is not None, "Required property 'route_response_key' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The model selection expression for the route response.

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-modelselectionexpression
        '''
        result = self._values.get("model_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def response_models(self) -> typing.Any:
        '''The response models for the route response.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responsemodels
        '''
        result = self._values.get("response_models")
        return typing.cast(typing.Any, result)

    @builtins.property
    def response_parameters(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnRouteResponse.ParameterConstraintsProperty]]]]:
        '''The route response parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-routeresponse.html#cfn-apigatewayv2-routeresponse-responseparameters
        '''
        result = self._values.get("response_parameters")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnRouteResponse.ParameterConstraintsProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteResponseProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnStage(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnStage",
):
    '''The ``AWS::ApiGatewayV2::Stage`` resource specifies a stage for an API.

    Each stage is a named reference to a deployment of the API and is made available for client applications to call. To learn more, see `Working with stages for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-stages.html>`_ and `Deploy a WebSocket API in API Gateway <https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-set-up-websocket-deployment.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        # route_settings: Any
        # stage_variables: Any
        # tags: Any
        
        cfn_stage = apigatewayv2.CfnStage(self, "MyCfnStage",
            api_id="apiId",
            stage_name="stageName",
        
            # the properties below are optional
            access_log_settings=apigatewayv2.CfnStage.AccessLogSettingsProperty(
                destination_arn="destinationArn",
                format="format"
            ),
            access_policy_id="accessPolicyId",
            auto_deploy=False,
            client_certificate_id="clientCertificateId",
            default_route_settings=apigatewayv2.CfnStage.RouteSettingsProperty(
                data_trace_enabled=False,
                detailed_metrics_enabled=False,
                logging_level="loggingLevel",
                throttling_burst_limit=123,
                throttling_rate_limit=123
            ),
            deployment_id="deploymentId",
            description="description",
            route_settings=route_settings,
            stage_variables=stage_variables,
            tags=tags
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        api_id: builtins.str,
        stage_name: builtins.str,
        access_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStage.AccessLogSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        access_policy_id: typing.Optional[builtins.str] = None,
        auto_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        client_certificate_id: typing.Optional[builtins.str] = None,
        default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnStage.RouteSettingsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        route_settings: typing.Any = None,
        stage_variables: typing.Any = None,
        tags: typing.Any = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param api_id: The API identifier.
        :param stage_name: The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be ``$default`` . Maximum length is 128 characters.
        :param access_log_settings: Settings for logging access in this stage.
        :param access_policy_id: This parameter is not currently supported.
        :param auto_deploy: Specifies whether updates to an API automatically trigger a new deployment. The default value is ``false`` .
        :param client_certificate_id: The identifier of a client certificate for a ``Stage`` . Supported only for WebSocket APIs.
        :param default_route_settings: The default route settings for the stage.
        :param deployment_id: The deployment identifier for the API stage. Can't be updated if ``autoDeploy`` is enabled.
        :param description: The description for the API stage.
        :param route_settings: Route settings for the stage.
        :param stage_variables: A map that defines the stage variables for a ``Stage`` . Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
        :param tags: The collection of tags. Each tag element is associated with a given resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b591f85024a936a75a298c8df17bc186d28dc5bff565564266bc639d476a92b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnStageProps(
            api_id=api_id,
            stage_name=stage_name,
            access_log_settings=access_log_settings,
            access_policy_id=access_policy_id,
            auto_deploy=auto_deploy,
            client_certificate_id=client_certificate_id,
            default_route_settings=default_route_settings,
            deployment_id=deployment_id,
            description=description,
            route_settings=route_settings,
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
            type_hints = typing.get_type_hints(_typecheckingstub__bbdad4215e0fef19862d943551630b59b5ecc3d826cf440041eb0b87b3341739)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8ecdf23a27ee39b01f2d4524d30008046b8ab8fed11606883ee0e66076c8085a)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="apiId")
    def api_id(self) -> builtins.str:
        '''The API identifier.'''
        return typing.cast(builtins.str, jsii.get(self, "apiId"))

    @api_id.setter
    def api_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe20c363af8f167b271354971cde5b1226e9aee5dcb45701f177abd3a7153dc1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiId", value)

    @builtins.property
    @jsii.member(jsii_name="stageName")
    def stage_name(self) -> builtins.str:
        '''The stage name.'''
        return typing.cast(builtins.str, jsii.get(self, "stageName"))

    @stage_name.setter
    def stage_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d04550bd54e71dee0877ee7904a8dfda4940b7a589681bcffed0326b8a91e95)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageName", value)

    @builtins.property
    @jsii.member(jsii_name="accessLogSettings")
    def access_log_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.AccessLogSettingsProperty"]]:
        '''Settings for logging access in this stage.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.AccessLogSettingsProperty"]], jsii.get(self, "accessLogSettings"))

    @access_log_settings.setter
    def access_log_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.AccessLogSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41aa5e58f595164332cc49c2cd34671974f6ff1b7934764d4695984cf7c9b069)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessLogSettings", value)

    @builtins.property
    @jsii.member(jsii_name="accessPolicyId")
    def access_policy_id(self) -> typing.Optional[builtins.str]:
        '''This parameter is not currently supported.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accessPolicyId"))

    @access_policy_id.setter
    def access_policy_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c956981c48b5497e6f4b22a1086c4e15f4617defe34d9dbe01a4524d5ed2a63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accessPolicyId", value)

    @builtins.property
    @jsii.member(jsii_name="autoDeploy")
    def auto_deploy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether updates to an API automatically trigger a new deployment.'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "autoDeploy"))

    @auto_deploy.setter
    def auto_deploy(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a8c4584c0c93ee7f63b53757d31787de58c4bb8f7a9eb24e9460876be43a6bd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autoDeploy", value)

    @builtins.property
    @jsii.member(jsii_name="clientCertificateId")
    def client_certificate_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of a client certificate for a ``Stage`` .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clientCertificateId"))

    @client_certificate_id.setter
    def client_certificate_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac6a4617e9ec38fabe78997fd8650207fa434265fecffc49e232b0e22a2ad136)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientCertificateId", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRouteSettings")
    def default_route_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.RouteSettingsProperty"]]:
        '''The default route settings for the stage.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.RouteSettingsProperty"]], jsii.get(self, "defaultRouteSettings"))

    @default_route_settings.setter
    def default_route_settings(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnStage.RouteSettingsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54a6835d490d578a89779a53d6e38b8118c89a32a5950b8c56b84d2dd8cb500b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRouteSettings", value)

    @builtins.property
    @jsii.member(jsii_name="deploymentId")
    def deployment_id(self) -> typing.Optional[builtins.str]:
        '''The deployment identifier for the API stage.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deploymentId"))

    @deployment_id.setter
    def deployment_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e741d0a38ed5e7ac2772707efd1dad1df2fbffad430ef4a3e2d9f44551e363b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deploymentId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the API stage.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a7c76644da05ec60a751783a988b29417ab8c3537430ab30a6e18db6805f1a4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="routeSettings")
    def route_settings(self) -> typing.Any:
        '''Route settings for the stage.'''
        return typing.cast(typing.Any, jsii.get(self, "routeSettings"))

    @route_settings.setter
    def route_settings(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea66ca7778a34e67ecb19c32f7dc4ee70a2e25558201756e1a92f80f726fd31b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeSettings", value)

    @builtins.property
    @jsii.member(jsii_name="stageVariables")
    def stage_variables(self) -> typing.Any:
        '''A map that defines the stage variables for a ``Stage`` .'''
        return typing.cast(typing.Any, jsii.get(self, "stageVariables"))

    @stage_variables.setter
    def stage_variables(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f03c043379dbbf4d7224f010dc09fd8445ce8565949828b067e3a58db7e3974c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "stageVariables", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Any:
        '''The collection of tags.'''
        return typing.cast(typing.Any, jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__751499e9aa415500e38391dc29ec87e1832fdefc98cd9719cb645294c398456e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnStage.AccessLogSettingsProperty",
        jsii_struct_bases=[],
        name_mapping={"destination_arn": "destinationArn", "format": "format"},
    )
    class AccessLogSettingsProperty:
        def __init__(
            self,
            *,
            destination_arn: typing.Optional[builtins.str] = None,
            format: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings for logging access in a stage.

            :param destination_arn: The ARN of the CloudWatch Logs log group to receive access logs. This parameter is required to enable access logging.
            :param format: A single line format of the access logs of data, as specified by selected $context variables. The format must include at least $context.requestId. This parameter is required to enable access logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                access_log_settings_property = apigatewayv2.CfnStage.AccessLogSettingsProperty(
                    destination_arn="destinationArn",
                    format="format"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2df15414b1dce14b24093aa467b87e46f6d07de6294f3274c908b91ef8a72935)
                check_type(argname="argument destination_arn", value=destination_arn, expected_type=type_hints["destination_arn"])
                check_type(argname="argument format", value=format, expected_type=type_hints["format"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if destination_arn is not None:
                self._values["destination_arn"] = destination_arn
            if format is not None:
                self._values["format"] = format

        @builtins.property
        def destination_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the CloudWatch Logs log group to receive access logs.

            This parameter is required to enable access logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-destinationarn
            '''
            result = self._values.get("destination_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def format(self) -> typing.Optional[builtins.str]:
            '''A single line format of the access logs of data, as specified by selected $context variables.

            The format must include at least $context.requestId. This parameter is required to enable access logging.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-accesslogsettings.html#cfn-apigatewayv2-stage-accesslogsettings-format
            '''
            result = self._values.get("format")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccessLogSettingsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnStage.RouteSettingsProperty",
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
            '''Represents a collection of route settings.

            :param data_trace_enabled: Specifies whether ( ``true`` ) or not ( ``false`` ) data trace logging is enabled for this route. This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.
            :param detailed_metrics_enabled: Specifies whether detailed metrics are enabled.
            :param logging_level: Specifies the logging level for this route: ``INFO`` , ``ERROR`` , or ``OFF`` . This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.
            :param throttling_burst_limit: Specifies the throttling burst limit.
            :param throttling_rate_limit: Specifies the throttling rate limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_apigatewayv2 as apigatewayv2
                
                route_settings_property = apigatewayv2.CfnStage.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b4f54bf7ffb1a1931a8cd8327c492e6086c85e4a4bdff47ada5c3125081df6c5)
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
            '''Specifies whether ( ``true`` ) or not ( ``false`` ) data trace logging is enabled for this route.

            This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-datatraceenabled
            '''
            result = self._values.get("data_trace_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def detailed_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether detailed metrics are enabled.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-detailedmetricsenabled
            '''
            result = self._values.get("detailed_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def logging_level(self) -> typing.Optional[builtins.str]:
            '''Specifies the logging level for this route: ``INFO`` , ``ERROR`` , or ``OFF`` .

            This property affects the log entries pushed to Amazon CloudWatch Logs. Supported only for WebSocket APIs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-logginglevel
            '''
            result = self._values.get("logging_level")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def throttling_burst_limit(self) -> typing.Optional[jsii.Number]:
            '''Specifies the throttling burst limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingburstlimit
            '''
            result = self._values.get("throttling_burst_limit")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def throttling_rate_limit(self) -> typing.Optional[jsii.Number]:
            '''Specifies the throttling rate limit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-stage-routesettings.html#cfn-apigatewayv2-stage-routesettings-throttlingratelimit
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
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnStageProps",
    jsii_struct_bases=[],
    name_mapping={
        "api_id": "apiId",
        "stage_name": "stageName",
        "access_log_settings": "accessLogSettings",
        "access_policy_id": "accessPolicyId",
        "auto_deploy": "autoDeploy",
        "client_certificate_id": "clientCertificateId",
        "default_route_settings": "defaultRouteSettings",
        "deployment_id": "deploymentId",
        "description": "description",
        "route_settings": "routeSettings",
        "stage_variables": "stageVariables",
        "tags": "tags",
    },
)
class CfnStageProps:
    def __init__(
        self,
        *,
        api_id: builtins.str,
        stage_name: builtins.str,
        access_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.AccessLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        access_policy_id: typing.Optional[builtins.str] = None,
        auto_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        client_certificate_id: typing.Optional[builtins.str] = None,
        default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        deployment_id: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        route_settings: typing.Any = None,
        stage_variables: typing.Any = None,
        tags: typing.Any = None,
    ) -> None:
        '''Properties for defining a ``CfnStage``.

        :param api_id: The API identifier.
        :param stage_name: The stage name. Stage names can contain only alphanumeric characters, hyphens, and underscores, or be ``$default`` . Maximum length is 128 characters.
        :param access_log_settings: Settings for logging access in this stage.
        :param access_policy_id: This parameter is not currently supported.
        :param auto_deploy: Specifies whether updates to an API automatically trigger a new deployment. The default value is ``false`` .
        :param client_certificate_id: The identifier of a client certificate for a ``Stage`` . Supported only for WebSocket APIs.
        :param default_route_settings: The default route settings for the stage.
        :param deployment_id: The deployment identifier for the API stage. Can't be updated if ``autoDeploy`` is enabled.
        :param description: The description for the API stage.
        :param route_settings: Route settings for the stage.
        :param stage_variables: A map that defines the stage variables for a ``Stage`` . Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.
        :param tags: The collection of tags. Each tag element is associated with a given resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            # route_settings: Any
            # stage_variables: Any
            # tags: Any
            
            cfn_stage_props = apigatewayv2.CfnStageProps(
                api_id="apiId",
                stage_name="stageName",
            
                # the properties below are optional
                access_log_settings=apigatewayv2.CfnStage.AccessLogSettingsProperty(
                    destination_arn="destinationArn",
                    format="format"
                ),
                access_policy_id="accessPolicyId",
                auto_deploy=False,
                client_certificate_id="clientCertificateId",
                default_route_settings=apigatewayv2.CfnStage.RouteSettingsProperty(
                    data_trace_enabled=False,
                    detailed_metrics_enabled=False,
                    logging_level="loggingLevel",
                    throttling_burst_limit=123,
                    throttling_rate_limit=123
                ),
                deployment_id="deploymentId",
                description="description",
                route_settings=route_settings,
                stage_variables=stage_variables,
                tags=tags
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__657f0385aed25a61e439d353b337b2757a7bca2c9aea6481d87aedf65da61dd3)
            check_type(argname="argument api_id", value=api_id, expected_type=type_hints["api_id"])
            check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
            check_type(argname="argument access_log_settings", value=access_log_settings, expected_type=type_hints["access_log_settings"])
            check_type(argname="argument access_policy_id", value=access_policy_id, expected_type=type_hints["access_policy_id"])
            check_type(argname="argument auto_deploy", value=auto_deploy, expected_type=type_hints["auto_deploy"])
            check_type(argname="argument client_certificate_id", value=client_certificate_id, expected_type=type_hints["client_certificate_id"])
            check_type(argname="argument default_route_settings", value=default_route_settings, expected_type=type_hints["default_route_settings"])
            check_type(argname="argument deployment_id", value=deployment_id, expected_type=type_hints["deployment_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument route_settings", value=route_settings, expected_type=type_hints["route_settings"])
            check_type(argname="argument stage_variables", value=stage_variables, expected_type=type_hints["stage_variables"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "api_id": api_id,
            "stage_name": stage_name,
        }
        if access_log_settings is not None:
            self._values["access_log_settings"] = access_log_settings
        if access_policy_id is not None:
            self._values["access_policy_id"] = access_policy_id
        if auto_deploy is not None:
            self._values["auto_deploy"] = auto_deploy
        if client_certificate_id is not None:
            self._values["client_certificate_id"] = client_certificate_id
        if default_route_settings is not None:
            self._values["default_route_settings"] = default_route_settings
        if deployment_id is not None:
            self._values["deployment_id"] = deployment_id
        if description is not None:
            self._values["description"] = description
        if route_settings is not None:
            self._values["route_settings"] = route_settings
        if stage_variables is not None:
            self._values["stage_variables"] = stage_variables
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def api_id(self) -> builtins.str:
        '''The API identifier.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-apiid
        '''
        result = self._values.get("api_id")
        assert result is not None, "Required property 'api_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def stage_name(self) -> builtins.str:
        '''The stage name.

        Stage names can contain only alphanumeric characters, hyphens, and underscores, or be ``$default`` . Maximum length is 128 characters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagename
        '''
        result = self._values.get("stage_name")
        assert result is not None, "Required property 'stage_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def access_log_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.AccessLogSettingsProperty]]:
        '''Settings for logging access in this stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesslogsettings
        '''
        result = self._values.get("access_log_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.AccessLogSettingsProperty]], result)

    @builtins.property
    def access_policy_id(self) -> typing.Optional[builtins.str]:
        '''This parameter is not currently supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-accesspolicyid
        '''
        result = self._values.get("access_policy_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def auto_deploy(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''Specifies whether updates to an API automatically trigger a new deployment.

        The default value is ``false`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-autodeploy
        '''
        result = self._values.get("auto_deploy")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def client_certificate_id(self) -> typing.Optional[builtins.str]:
        '''The identifier of a client certificate for a ``Stage`` .

        Supported only for WebSocket APIs.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-clientcertificateid
        '''
        result = self._values.get("client_certificate_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_route_settings(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.RouteSettingsProperty]]:
        '''The default route settings for the stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-defaultroutesettings
        '''
        result = self._values.get("default_route_settings")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.RouteSettingsProperty]], result)

    @builtins.property
    def deployment_id(self) -> typing.Optional[builtins.str]:
        '''The deployment identifier for the API stage.

        Can't be updated if ``autoDeploy`` is enabled.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-deploymentid
        '''
        result = self._values.get("deployment_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description for the API stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route_settings(self) -> typing.Any:
        '''Route settings for the stage.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-routesettings
        '''
        result = self._values.get("route_settings")
        return typing.cast(typing.Any, result)

    @builtins.property
    def stage_variables(self) -> typing.Any:
        '''A map that defines the stage variables for a ``Stage`` .

        Variable names can have alphanumeric and underscore characters, and the values must match [A-Za-z0-9-._~:/?#&=,]+.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-stagevariables
        '''
        result = self._values.get("stage_variables")
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Any:
        '''The collection of tags.

        Each tag element is associated with a given resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-stage.html#cfn-apigatewayv2-stage-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Any, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnStageProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnVpcLink(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnVpcLink",
):
    '''The ``AWS::ApiGatewayV2::VpcLink`` resource creates a VPC link.

    Supported only for HTTP APIs. The VPC link status must transition from ``PENDING`` to ``AVAILABLE`` to successfully create a VPC link, which can take up to 10 minutes. To learn more, see `Working with VPC Links for HTTP APIs <https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-vpc-links.html>`_ in the *API Gateway Developer Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2 as apigatewayv2
        
        cfn_vpc_link = apigatewayv2.CfnVpcLink(self, "MyCfnVpcLink",
            name="name",
            subnet_ids=["subnetIds"],
        
            # the properties below are optional
            security_group_ids=["securityGroupIds"],
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
        name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the VPC link.
        :param subnet_ids: A list of subnet IDs to include in the VPC link.
        :param security_group_ids: A list of security group IDs for the VPC link.
        :param tags: The collection of tags. Each tag element is associated with a given resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c311f0c712d17a23f40a3997d551ec4685650a39ccca44f14c887295da27c0d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVpcLinkProps(
            name=name,
            subnet_ids=subnet_ids,
            security_group_ids=security_group_ids,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__31e7d691834230970f8fa995f5cb9af99751ab5011d6ef4c4f4a656dc8e4f035)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f4ada05715ecfeb20e014eb30b95742288093511f7d2de71cd823a4f6a3c6359)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcLinkId")
    def attr_vpc_link_id(self) -> builtins.str:
        '''The VPC link ID.

        :cloudformationAttribute: VpcLinkId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVpcLinkId"))

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
        '''The name of the VPC link.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a68acbefe43d1496e326d236ecda5853ae402a2016531047f7ecf885dec6c002)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subnetIds")
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of subnet IDs to include in the VPC link.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subnetIds"))

    @subnet_ids.setter
    def subnet_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__71b2854d014a1a439edb860779512c90020df989899cf1adced4e3b5f2d70af4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetIds", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs for the VPC link.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7d7b3db2c880db4099782067eed38dceedec114dfa1a78bd9caf33d8a491a8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The collection of tags.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ed14236b4263520664773636899de1162d8f6cc986b4772464579ab1525d16d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2.CfnVpcLinkProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "subnet_ids": "subnetIds",
        "security_group_ids": "securityGroupIds",
        "tags": "tags",
    },
)
class CfnVpcLinkProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        subnet_ids: typing.Sequence[builtins.str],
        security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVpcLink``.

        :param name: The name of the VPC link.
        :param subnet_ids: A list of subnet IDs to include in the VPC link.
        :param security_group_ids: A list of security group IDs for the VPC link.
        :param tags: The collection of tags. Each tag element is associated with a given resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            
            cfn_vpc_link_props = apigatewayv2.CfnVpcLinkProps(
                name="name",
                subnet_ids=["subnetIds"],
            
                # the properties below are optional
                security_group_ids=["securityGroupIds"],
                tags={
                    "tags_key": "tags"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88ff01f13c7c99226d1a763eb58d4cbc600fe6193b5dd3e6398606d88dd4ea1b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subnet_ids", value=subnet_ids, expected_type=type_hints["subnet_ids"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "subnet_ids": subnet_ids,
        }
        if security_group_ids is not None:
            self._values["security_group_ids"] = security_group_ids
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the VPC link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subnet_ids(self) -> typing.List[builtins.str]:
        '''A list of subnet IDs to include in the VPC link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-subnetids
        '''
        result = self._values.get("subnet_ids")
        assert result is not None, "Required property 'subnet_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def security_group_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''A list of security group IDs for the VPC link.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The collection of tags.

        Each tag element is associated with a given resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigatewayv2-vpclink.html#cfn-apigatewayv2-vpclink-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVpcLinkProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApi",
    "CfnApiGatewayManagedOverrides",
    "CfnApiGatewayManagedOverridesProps",
    "CfnApiMapping",
    "CfnApiMappingProps",
    "CfnApiProps",
    "CfnAuthorizer",
    "CfnAuthorizerProps",
    "CfnDeployment",
    "CfnDeploymentProps",
    "CfnDomainName",
    "CfnDomainNameProps",
    "CfnIntegration",
    "CfnIntegrationProps",
    "CfnIntegrationResponse",
    "CfnIntegrationResponseProps",
    "CfnModel",
    "CfnModelProps",
    "CfnRoute",
    "CfnRouteProps",
    "CfnRouteResponse",
    "CfnRouteResponseProps",
    "CfnStage",
    "CfnStageProps",
    "CfnVpcLink",
    "CfnVpcLinkProps",
]

publication.publish()

def _typecheckingstub__1db7633eb849c7234f54cf8f50ef6e4c6273ca1ab60db537f47e511e2240c5b6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_key_selection_expression: typing.Optional[builtins.str] = None,
    base_path: typing.Optional[builtins.str] = None,
    body: typing.Any = None,
    body_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.BodyS3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cors_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.CorsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    credentials_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    disable_schema_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    protocol_type: typing.Optional[builtins.str] = None,
    route_key: typing.Optional[builtins.str] = None,
    route_selection_expression: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea567b8b40be10165a36dab66b11588d141fcb6bb04249eea1d0752e699710d4(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d18d8bbf1817171b680c668ba45b7bf21f8602f6a88656a3fcba170987a99efd(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f558d38700b12a8436eb254b53f9b036b9dcc79e6b13662d5cc5f734a50cc0e1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c9c0986fef807a65a36cb9c2c2088cce866089cadbd06372d8e636cee797253(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b640ee61c5afa6ad142df6ac4f94d2662b22d8db131f7f0bbb9357d1e77d98(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__461aef5629963bb7b74c508fa030064900f1e11ec3308ed14d0e0125845f569b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.BodyS3LocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea01a446f6b48d1d09e26c2d973a367686fc04ba3d8d5922215249b2d34b67eb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApi.CorsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd12bd9456ce5e4af4343ebe09227e1fa34692caf0b82db4abd6147ac9f132f7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9bc7f78ea01f8843ca5b04055b6b342ad243dd45e7ab88143c592adf5b5a283(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77d94dbd246367bad1d084b1e206403a882329be7b7bb9331e4bd1fa90ae597a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c4fafef5608e6998354242dff5cfd6b04966c90f66f2d2737cfed24eb25398a(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ce8eb7264be44ff3a6ae79c6be6a193c31eb617518209aeb51c346aac7c5536(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6de2f3d46e4a0275374cdfba39222daec1a50d7516f00756e898551462523fb6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e57f77aa16016f544c5223d6856ffa749c3e01cee63831813142637d65047878(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f1526e8beb3aabccc2d1a4a66b85888cbae9836882586cbc1831cb780485872(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ae3d20180c61889cbbc3db2ac94b1665ceb0357e28b396e9eb10b36443cc6d3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ade78b4fb0e303cc30b6b8a9298c4758fd1370f3627ea5e37db0fe2e2ce623af(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96f6611a87a6cb532fe3a0a6fda47d8cb668095b5984db628a9a79828ae2b327(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__122ec616b9f721d7146444333bfc18f20226b393d496105443355c5add69abf9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__086d4bdce422b6d8380b205644d06b82c6e6ca7cc5c6a6813f2498660cf2e643(
    *,
    bucket: typing.Optional[builtins.str] = None,
    etag: typing.Optional[builtins.str] = None,
    key: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6a3791259651e5580c105c2edbd7e61bfe4d9352ce320e2b6cee928ff45f804(
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

def _typecheckingstub__3082a35122d304d1e6cb138bd4f4ff647c08d9345fc0680734a094f650214a9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    integration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.IntegrationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.RouteOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.StageOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f546675cd72b747ba4414186c0b784c272bc9b2cc62f6d8527feb95ad0069a7d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__074d92384425f99a1b1f84fd40ccd33b5d3ff6d021bbdf363f73d6c45065193c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a21a84b347534934baae96f0d955d7cb2a425b3a984d9cccb6b9853851a463(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6e8f6e317166c4e7072ff432e3e7eccfb8b95c41ae3624cbc1df56dfb741e92(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.IntegrationOverridesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80d7eeb3e44a467671100a29546de04d5d43029de65fbf94591ab14fffad1c5c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.RouteOverridesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b463a4abcee245efa2b5f8331eb964b48378707ae4929bfd7871d5ecef589ae8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApiGatewayManagedOverrides.StageOverridesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3107ba375d42b235637a85ea013e8de6b4867611024bc71e2c59db92941dcc1(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52af4fb74c40ef1f2f6be4941e114a9dee678620d84a75a3d412e8f19efd0a5e(
    *,
    description: typing.Optional[builtins.str] = None,
    integration_method: typing.Optional[builtins.str] = None,
    payload_format_version: typing.Optional[builtins.str] = None,
    timeout_in_millis: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b352b9e190a07978f5f79a0a25e0674fec09f30874ec1c2794f521e6c482f06(
    *,
    authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    authorization_type: typing.Optional[builtins.str] = None,
    authorizer_id: typing.Optional[builtins.str] = None,
    operation_name: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3c274518dfd0a38d624673e2404ec404bd69957d2d008f63dd8c49507e3bdd3(
    *,
    data_trace_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    detailed_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    throttling_burst_limit: typing.Optional[jsii.Number] = None,
    throttling_rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea132c6be8d923c2d66569aa4c4173cf533b8a8f3c8959eb63a39674fed009f3(
    *,
    access_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.AccessLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    auto_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    route_settings: typing.Any = None,
    stage_variables: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__40b87ae4ac983962d1367d2c0b468ff7d196133f8fa354542fbc9cb69df972c1(
    *,
    api_id: builtins.str,
    integration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.IntegrationOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.RouteOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApiGatewayManagedOverrides.StageOverridesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c7941c91626bf9a2ba9b280f45933deda0d260740aa53002a46b6ab82a16ee7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    domain_name: builtins.str,
    stage: builtins.str,
    api_mapping_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c82011934bb943ac56e9ca15a3fe2a18c216660e1756e95e52e27f231dec231(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ae4463f7feed53f0bfce2bb7e7a44ca8cb4a75981a848eb321c6769c45e5ce5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16b4567f90930e8b6066ebfc2754fe20fbf1ac5584fafac3590ca91aa888c9f8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29763e906ad99eaf78d0a9dee6a0499887496126efb3aa75ef00df49524186fb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__795325b53a59ad485c851fa2a6b00f03e881044ac7a59f18df5adbe25da80c91(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cff63da4774ec3927c6108752f4d513d841d877a4cb52ccfe4e4a61e344e1424(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__35fae8a54109857e64a283a909a1a23ceda5ded3bf38ca4bce78df48ed736863(
    *,
    api_id: builtins.str,
    domain_name: builtins.str,
    stage: builtins.str,
    api_mapping_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__de72efdeda792916a7e0a8d8953153208abe93b442ac8056802f749d4b8c27c4(
    *,
    api_key_selection_expression: typing.Optional[builtins.str] = None,
    base_path: typing.Optional[builtins.str] = None,
    body: typing.Any = None,
    body_s3_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.BodyS3LocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cors_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApi.CorsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    credentials_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    disable_execute_api_endpoint: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    disable_schema_validation: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    fail_on_warnings: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    protocol_type: typing.Optional[builtins.str] = None,
    route_key: typing.Optional[builtins.str] = None,
    route_selection_expression: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    target: typing.Optional[builtins.str] = None,
    version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a867239336510db3ecc55c81cb94d0d83923605d20916fa98ef4877f9a6bb310(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    authorizer_type: builtins.str,
    name: builtins.str,
    authorizer_credentials_arn: typing.Optional[builtins.str] = None,
    authorizer_payload_format_version: typing.Optional[builtins.str] = None,
    authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    authorizer_uri: typing.Optional[builtins.str] = None,
    enable_simple_responses: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    identity_source: typing.Optional[typing.Sequence[builtins.str]] = None,
    identity_validation_expression: typing.Optional[builtins.str] = None,
    jwt_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAuthorizer.JWTConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d959aa36bcde5579969213ffe818029e4f8c72a281aa48051e9a737c828e1ddd(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf024f12578bd433a40860ee462136ed673aae2a31c77ef7c5d0718c4d76c50f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c94b906e2fe834cc4b37a4eb041b8e7ab23901d40aeb5912de689fad4139fc9d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdc8e9a7d4d7429420766da5e132ae16ec76fc2f3e679d82cdf69137c200fbc3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78b3b857580e5719b96ef1257bd96e1a2a67be3225151b97e8008a99ed6a360(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29e0e6baddf2813e344a9f995c17c9369390dcc36a6c186182885b5956b6be2a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__704a1ebfe51335da671a36d566a2f9ebce2a91877958850fce305542c6f8147f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10386c9852429b19804f6174b4c7ef97c7b3cbf3a8183c5db8d1df686554caee(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f0becd827426ad17e13b4edec41e2383d35feec43ac97627da48c167c25f0d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca220b368392b92ad3186f8b7a90bf77a210aaafee93b2a0e9444103bac3301c(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ace1f00404a76cab1dbe9bd4e4f41644b1de7a3dd37df8e37625966ae52594c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d335b88eea9c6ce2df51c3c8e9af597d3a4f3fb42410c60a1fbc7de5813a7800(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9a032d11594e2f9a62ed9a4289c33939ffb5bebe7caa00404debfb40cd260e0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnAuthorizer.JWTConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e3111dc0620a413031b38e657a146c66f5c593098e2264e4a367a7d9cae646b(
    *,
    audience: typing.Optional[typing.Sequence[builtins.str]] = None,
    issuer: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7793252368a914b674f8f80b8ab85fd50270086231afdc5a63d6706fc8985226(
    *,
    api_id: builtins.str,
    authorizer_type: builtins.str,
    name: builtins.str,
    authorizer_credentials_arn: typing.Optional[builtins.str] = None,
    authorizer_payload_format_version: typing.Optional[builtins.str] = None,
    authorizer_result_ttl_in_seconds: typing.Optional[jsii.Number] = None,
    authorizer_uri: typing.Optional[builtins.str] = None,
    enable_simple_responses: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    identity_source: typing.Optional[typing.Sequence[builtins.str]] = None,
    identity_validation_expression: typing.Optional[builtins.str] = None,
    jwt_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnAuthorizer.JWTConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd659e77f6f73d039f09dfba950ad0f0c80871608d2a7828058dceb3e7fe181(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    stage_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f8481ebeeb348b5cd00950f41454661b821577bbfc21c63c7524dd95654fc17(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb7dbc3d4832449936a54c0e42e5bc985b663309bbdb2aeba47447838030f7d3(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8380391f5e9a81027656c48bdab6533551d7416be7d4c0a61dcb8c7870a6695d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a096735639df363beb6e57d5ef578f6cf95a74095409ee9c322663acd1f5ba03(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33040a213f03d33962ff4df0681abb8f23303cac13cf97cc0ac997dc873eb59c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__497cc0e552f167da7730bb49dda8116b36b3c3e31b6bebeabe6ecf25f997b531(
    *,
    api_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    stage_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1dd1a2be8baf8f5fddc282520a295c206cc1466b04d57a3227f938bdec4a2f5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    domain_name_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomainName.DomainNameConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomainName.MutualTlsAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca0b93c0a8031fc21c98a7b59eb1a20d1be884a8f1e1d5510fcbeea6febc52bc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ce76adb9b6f17382e4b34b13786dcec99768d000140b8e1aa78820d94d0a4b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8174f7ac22c1397914e489109ad7e6891d4964a0f3d3972fd7f5fa8ce72c3bce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b6be5b4180a1026f7ee79c898cdcb31077d95e3aa103f952db8e5fc4901eb6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnDomainName.DomainNameConfigurationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7db79836bb2717dd9f77cf2a7e1dbf16c2828d8d2066adf6a1fd6f14bd19d816(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnDomainName.MutualTlsAuthenticationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91e15ff48f085b835a961d76641a12ee2d099786f346c15be08cd6e10f58f927(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faaf4905cea99e081f1f881fa68755b4ec1bc0ed8f4e145c30baf36d95e5cc83(
    *,
    certificate_arn: typing.Optional[builtins.str] = None,
    certificate_name: typing.Optional[builtins.str] = None,
    endpoint_type: typing.Optional[builtins.str] = None,
    ownership_verification_certificate_arn: typing.Optional[builtins.str] = None,
    security_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f25cc46ec061420fb13cc99bbb2ac01e6cf22e79cf84955006c7e3a92b30e40(
    *,
    truststore_uri: typing.Optional[builtins.str] = None,
    truststore_version: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1629526da8e64502c98094213f6afc52d78388551bbefd7f02cebe4452a94a5c(
    *,
    domain_name: builtins.str,
    domain_name_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomainName.DomainNameConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    mutual_tls_authentication: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnDomainName.MutualTlsAuthenticationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ee25d7b8304fd6f8c1196e47b946d8bf8256f5a9f37b58c7c5f5cb8f73bd7f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    integration_type: builtins.str,
    connection_id: typing.Optional[builtins.str] = None,
    connection_type: typing.Optional[builtins.str] = None,
    content_handling_strategy: typing.Optional[builtins.str] = None,
    credentials_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    integration_method: typing.Optional[builtins.str] = None,
    integration_subtype: typing.Optional[builtins.str] = None,
    integration_uri: typing.Optional[builtins.str] = None,
    passthrough_behavior: typing.Optional[builtins.str] = None,
    payload_format_version: typing.Optional[builtins.str] = None,
    request_parameters: typing.Any = None,
    request_templates: typing.Any = None,
    response_parameters: typing.Any = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
    timeout_in_millis: typing.Optional[jsii.Number] = None,
    tls_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TlsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee31d41d0171be6e19e690774d5d6627ad812e56a2cab81fa66b2f61aa6f3951(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6126d2c248e8bb9199dba590d9b83e8f9719b81bd829888c5414ef87a3d59219(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa39d0c12f6743ba2631e050aa28a363ddcc81dfd7ae60bc844dc7f45a3a0c7a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18c92c57e09be6a12ef9c2311c8921cafb5f4dff56e0f8e98710440065d0f75(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__46edc03483245f7ebd5b029a181a06f1ae098e07971bccad9b4ecd1986adc162(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48543c37e107a7129a6cbc73639e8383fb2c4225d304382db660f52645290ecd(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8b1973f1c5573b93173e49c64f6e70a715914d1fba975e1eb8070226202221f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6d8c439acc57ba5be7137b02b1514b0e9a84285d9b207cf8edbb188cd3c9cdf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc069b9321eb211ab95f9c0904ca5919c9d265fef15a59838ae9f884273b0669(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0362127f0c545ac01dd3b59243c935c5756b6e9251c2a8e04597ec0281a833a1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3bad3279c4a378ed62fbce1637f2a011d7a2661bced09041c61a0e4f83f4c3a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cd111331771976544458360d1a6a3bad5e722f1484325d01c7bce109006e405(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a727a930643734ff056002d99f5485b84de3c8a9714ff88c9ec6e4b4ed6b2609(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__16e1cdf41a9fbafec3a3f020dce252f9e906c5147a18a5fdd738f8075d840baa(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a2e295280878c041c9a343d25c3d468f9c0db07048c247f5796a3bbcf24039(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__101df28f0b4f486748827f04e36cb60e9930a7fcbc372f1a22e694f243437ba1(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2c90c96ec7876c8a6c376c4c46707e575640a158942a5c3ead1572769175c15(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__09b070ac49ad358b1b6713b8e487d653fdf93ef9e4ad8b29c6d2348ec5347cb2(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2265ff6343fb7bb0629e72dfee180369b7d8341ec892b8f4c3180f1f615f5128(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56ceb8ff581bdc4197d98dbf69a924ea37de46cfdd6f6f8c1a6c46a94c82e8b2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnIntegration.TlsConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dbe4af6ef419f3fca35eeefa87a09cafa7177216b644e69571fe9d05b2b0ed7(
    *,
    response_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.ResponseParameterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe5d304364e2ba9a1fee328297e69bcc2440350e01f210541d4decfd2aff9755(
    *,
    destination: builtins.str,
    source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33df515d85a59f496faf5c4df3725daf4904bdfdc12bedcbb859eda8bf55bb43(
    *,
    server_name_to_verify: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__959841762bab1a313d723cf36b281fcb4d5c0bb2f15ded3e0c7f38aaa97997c1(
    *,
    api_id: builtins.str,
    integration_type: builtins.str,
    connection_id: typing.Optional[builtins.str] = None,
    connection_type: typing.Optional[builtins.str] = None,
    content_handling_strategy: typing.Optional[builtins.str] = None,
    credentials_arn: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    integration_method: typing.Optional[builtins.str] = None,
    integration_subtype: typing.Optional[builtins.str] = None,
    integration_uri: typing.Optional[builtins.str] = None,
    passthrough_behavior: typing.Optional[builtins.str] = None,
    payload_format_version: typing.Optional[builtins.str] = None,
    request_parameters: typing.Any = None,
    request_templates: typing.Any = None,
    response_parameters: typing.Any = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
    timeout_in_millis: typing.Optional[jsii.Number] = None,
    tls_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnIntegration.TlsConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3073dfa88ecd48398fee93e5529ed75a9739534bd3b09ae3db2434d1d7330349(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    integration_id: builtins.str,
    integration_response_key: builtins.str,
    content_handling_strategy: typing.Optional[builtins.str] = None,
    response_parameters: typing.Any = None,
    response_templates: typing.Any = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9eb8a7a88b16046fe04b3947f00ae23d6f9d961c6d7e9537f31bb0a6a85ea14(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c355c31fef694ade9a614c0a6d364f0f220effb67f50cfb01812e98200801ef(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99fea032bb48ce29028df074824542352a22c09d235ca01d0b3c55e23f7c3b92(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cdf5a2e36e17c7956158792201f399023d1254bba7b297a2ba1de3687f4b7b99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8059eca870e9610a9500cc304aaeb602575652ebbc3fe0ab8399e773b218fef(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1fa5320f9dd58af11d49e6707ba435d74bd31b41b5f0cc79f4306bfd30a79a28(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2575e266b0e74bc1ed655a2ba782d189b25474ca18b53d97c2003730abca92ff(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a3ba7c35e06acda935a23473c90cfa001239c682c8737d897cf6ec207fd49cf(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cf04d9ff614e1130ca1b37b22fad9aecf0edfc31b0571b48e6cd2eb3a838e25(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ac9393ea8482959d9abf755d543e025afdf5cabf2379a474cfb607ced90a7d(
    *,
    api_id: builtins.str,
    integration_id: builtins.str,
    integration_response_key: builtins.str,
    content_handling_strategy: typing.Optional[builtins.str] = None,
    response_parameters: typing.Any = None,
    response_templates: typing.Any = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6ccae01e5e00deb4abf47fade1fc44a9e24a6b132f346a2168e61859b0fd0f9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    name: builtins.str,
    schema: typing.Any,
    content_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__614a93ac0501ec7b30c025d62a3fb8396af011528fee2dfdf92a02c0f03cb4f6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__094e778f5596bd0c50f977ede46b679b30895ef9e7437e30638ba85c8324aa5a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd7208082e475506377665abd7f89515f9cd05cb4a805ac3d22330cf7717506a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fc2be804afd386603717c4be503b6428d5db3793acae35866859f65b5633bd9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a9ac80c16be2c7876398f311a65e5d43fc4f955ae556019897effbfac12b594(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0927afd42ecf7d6a1d74ddcea4ee74039cff8c61540dd3db8f4d477df2b2dbf8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c31bf4c0f98d1cb3fa2591344d5a2ba5243703029f6fd8f52ee51debcac4b197(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94458d573335422ed4ef0420d5707527a083fd922a556e7e5cf9d2df4b6b770b(
    *,
    api_id: builtins.str,
    name: builtins.str,
    schema: typing.Any,
    content_type: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__684f667963694c8b4dd362278e6d43f4e671fbdd6c30e9164a05a537ed94abfc(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    route_key: builtins.str,
    api_key_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    authorization_type: typing.Optional[builtins.str] = None,
    authorizer_id: typing.Optional[builtins.str] = None,
    model_selection_expression: typing.Optional[builtins.str] = None,
    operation_name: typing.Optional[builtins.str] = None,
    request_models: typing.Any = None,
    request_parameters: typing.Any = None,
    route_response_selection_expression: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__320c6e2f5cab38967ffd9b0ed4b2ddc789a3410d286b29ec51e096ae927441dc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a26d4ab03701420baf53d66a1006c11e7600abd1e7af917d90a4992ed19eeb(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__817ae6943537234b9b4f8b1026eb08df9aa3dcc5a4a3d2e1bcdaccb4c8859013(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b1b526cae660647aa14081711ec4c4c83f9f47ffa9d750a776fd3cca7a492415(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__358b8c173a385a0f2f4df063725f0a0c0994b4367e7ee327094d60be73d0159b(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd8ccd7b07196f3b620d34a517b46ebd7d064a73896e86a7708c2f852454a3c(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__710b2a2b6379ef5ced6134bab0acb3a139eae146d1637c631fa1ac82e1293aa5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__207cf5963882c49224627f6fb3fd59f643cdf1d90254c55bb502b2ed93138b09(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b8705da16da23f26d861473096719d972912648ca74dd5bb739b97403054a0f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8135ad6e2375b25f70679c06db1891227be6c2f927872bf884a88cc18e03968e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__966777ea62e0e3d128249c9c19b073476ddd0fe229b79943181b9727a164557d(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435eeaef03289d500227b42f18979b36e67086e9d93768b135e26be8fd96d93c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf161d094c7f77313e160a547c5e5314f99a3b8acd6fe48762a098ff337f142d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11684b3d73b34e31f947a907e002a5a3f8deadc5f5d21850e1751afa90ceb81e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a20f7e0c1183a32a2b6d2b5daf9aa8b640963d055ad89eddfe0a955d42b69cd8(
    *,
    required: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2628a47509f0aa7b326e157f1d321ae5bb9aee16e4672e277cea07a7f37adcba(
    *,
    api_id: builtins.str,
    route_key: builtins.str,
    api_key_required: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    authorization_scopes: typing.Optional[typing.Sequence[builtins.str]] = None,
    authorization_type: typing.Optional[builtins.str] = None,
    authorizer_id: typing.Optional[builtins.str] = None,
    model_selection_expression: typing.Optional[builtins.str] = None,
    operation_name: typing.Optional[builtins.str] = None,
    request_models: typing.Any = None,
    request_parameters: typing.Any = None,
    route_response_selection_expression: typing.Optional[builtins.str] = None,
    target: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfaf600ddc8caeb97e41fee38b4de9c8fb9d185fa3ec18942f79f3893b8bef51(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    route_id: builtins.str,
    route_response_key: builtins.str,
    model_selection_expression: typing.Optional[builtins.str] = None,
    response_models: typing.Any = None,
    response_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouteResponse.ParameterConstraintsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__396915a95af209f92313053f98eabbb48e49ef4061931d44d85f72ccb908b7e2(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b989b0d6859022f53c1b5edba59217d08a86f1ab1fb99ae706e99fd946229fc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80374cb7a6bb214c9c92bb6ddb083cdbcef83f46270a64db85109a45c17759c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__592e3a33ad0f2f9f26c7e2f768d47cf4ce3fc02a4163624603480e3ae1b33c63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__210ce20ec5517850582ca60d34b2b638e220326969bfa6897b7d1a0636a92361(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__903fde614a75269b08834aec81261c81e5c574a3af3db707d8cd7b207129a670(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03faecb8792316337b34af5c47692d7e5866e563a65e7afcbfc9043d35b8f42c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fadfcdb67c25b7fc23ab64866f4161b7cde8c566e504b8aa2a58d0798ecfab7a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, CfnRouteResponse.ParameterConstraintsProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0b539ced1929d65d764bbe6c2bdf11baa4f870e1b409230563c2613a25e709e7(
    *,
    required: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3357f1247faebabfedb5db2b33a7b9038414306326813b06294bdc9f355e50bb(
    *,
    api_id: builtins.str,
    route_id: builtins.str,
    route_response_key: builtins.str,
    model_selection_expression: typing.Optional[builtins.str] = None,
    response_models: typing.Any = None,
    response_parameters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Union[_IResolvable_da3f097b, typing.Union[CfnRouteResponse.ParameterConstraintsProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b591f85024a936a75a298c8df17bc186d28dc5bff565564266bc639d476a92b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    api_id: builtins.str,
    stage_name: builtins.str,
    access_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.AccessLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    access_policy_id: typing.Optional[builtins.str] = None,
    auto_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    client_certificate_id: typing.Optional[builtins.str] = None,
    default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    route_settings: typing.Any = None,
    stage_variables: typing.Any = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbdad4215e0fef19862d943551630b59b5ecc3d826cf440041eb0b87b3341739(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ecdf23a27ee39b01f2d4524d30008046b8ab8fed11606883ee0e66076c8085a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe20c363af8f167b271354971cde5b1226e9aee5dcb45701f177abd3a7153dc1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d04550bd54e71dee0877ee7904a8dfda4940b7a589681bcffed0326b8a91e95(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41aa5e58f595164332cc49c2cd34671974f6ff1b7934764d4695984cf7c9b069(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.AccessLogSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c956981c48b5497e6f4b22a1086c4e15f4617defe34d9dbe01a4524d5ed2a63(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a8c4584c0c93ee7f63b53757d31787de58c4bb8f7a9eb24e9460876be43a6bd(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac6a4617e9ec38fabe78997fd8650207fa434265fecffc49e232b0e22a2ad136(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54a6835d490d578a89779a53d6e38b8118c89a32a5950b8c56b84d2dd8cb500b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnStage.RouteSettingsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e741d0a38ed5e7ac2772707efd1dad1df2fbffad430ef4a3e2d9f44551e363b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a7c76644da05ec60a751783a988b29417ab8c3537430ab30a6e18db6805f1a4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea66ca7778a34e67ecb19c32f7dc4ee70a2e25558201756e1a92f80f726fd31b(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f03c043379dbbf4d7224f010dc09fd8445ce8565949828b067e3a58db7e3974c(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__751499e9aa415500e38391dc29ec87e1832fdefc98cd9719cb645294c398456e(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2df15414b1dce14b24093aa467b87e46f6d07de6294f3274c908b91ef8a72935(
    *,
    destination_arn: typing.Optional[builtins.str] = None,
    format: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4f54bf7ffb1a1931a8cd8327c492e6086c85e4a4bdff47ada5c3125081df6c5(
    *,
    data_trace_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    detailed_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    logging_level: typing.Optional[builtins.str] = None,
    throttling_burst_limit: typing.Optional[jsii.Number] = None,
    throttling_rate_limit: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__657f0385aed25a61e439d353b337b2757a7bca2c9aea6481d87aedf65da61dd3(
    *,
    api_id: builtins.str,
    stage_name: builtins.str,
    access_log_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.AccessLogSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    access_policy_id: typing.Optional[builtins.str] = None,
    auto_deploy: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    client_certificate_id: typing.Optional[builtins.str] = None,
    default_route_settings: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnStage.RouteSettingsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    deployment_id: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    route_settings: typing.Any = None,
    stage_variables: typing.Any = None,
    tags: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c311f0c712d17a23f40a3997d551ec4685650a39ccca44f14c887295da27c0d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31e7d691834230970f8fa995f5cb9af99751ab5011d6ef4c4f4a656dc8e4f035(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4ada05715ecfeb20e014eb30b95742288093511f7d2de71cd823a4f6a3c6359(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a68acbefe43d1496e326d236ecda5853ae402a2016531047f7ecf885dec6c002(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__71b2854d014a1a439edb860779512c90020df989899cf1adced4e3b5f2d70af4(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7d7b3db2c880db4099782067eed38dceedec114dfa1a78bd9caf33d8a491a8e(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed14236b4263520664773636899de1162d8f6cc986b4772464579ab1525d16d9(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88ff01f13c7c99226d1a763eb58d4cbc600fe6193b5dd3e6398606d88dd4ea1b(
    *,
    name: builtins.str,
    subnet_ids: typing.Sequence[builtins.str],
    security_group_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
