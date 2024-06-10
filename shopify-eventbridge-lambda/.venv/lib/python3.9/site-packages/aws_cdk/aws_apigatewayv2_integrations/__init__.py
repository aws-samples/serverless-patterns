'''
# AWS APIGatewayv2 Integrations

## Table of Contents

* [HTTP APIs](#http-apis)

  * [Lambda Integration](#lambda)
  * [HTTP Proxy Integration](#http-proxy)
  * [StepFunctions Integration](#stepfunctions-integration)
  * [Private Integration](#private-integration)
  * [Request Parameters](#request-parameters)
* [WebSocket APIs](#websocket-apis)

  * [Lambda WebSocket Integration](#lambda-websocket-integration)
  * [AWS WebSocket Integration](#aws-websocket-integration)

## HTTP APIs

Integrations connect a route to backend resources. HTTP APIs support Lambda proxy, AWS service, and HTTP proxy integrations. HTTP proxy integrations are also known as private integrations.

### Lambda

Lambda integrations enable integrating an HTTP API route with a Lambda function. When a client invokes the route, the
API Gateway service forwards the request to the Lambda function and returns the function's response to the client.

The API Gateway service will invoke the Lambda function with an event payload of a specific format. The service expects
the function to respond in a specific format. The details on this format are available at [Working with AWS Lambda
proxy integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html).

The following code configures a route `GET /books` with a Lambda proxy integration.

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration

# books_default_fn: lambda.Function

books_integration = HttpLambdaIntegration("BooksIntegration", books_default_fn)

http_api = apigwv2.HttpApi(self, "HttpApi")

http_api.add_routes(
    path="/books",
    methods=[apigwv2.HttpMethod.GET],
    integration=books_integration
)
```

### HTTP Proxy

HTTP Proxy integrations enables connecting an HTTP API route to a publicly routable HTTP endpoint. When a client
invokes the route, the API Gateway service forwards the entire request and response between the API Gateway endpoint
and the integrating HTTP endpoint. More information can be found at [Working with HTTP proxy
integrations](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-http.html).

The following code configures a route `GET /books` with an HTTP proxy integration to an HTTP endpoint
`get-books-proxy.example.com`.

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpUrlIntegration


books_integration = HttpUrlIntegration("BooksIntegration", "https://get-books-proxy.example.com")

http_api = apigwv2.HttpApi(self, "HttpApi")

http_api.add_routes(
    path="/books",
    methods=[apigwv2.HttpMethod.GET],
    integration=books_integration
)
```

### StepFunctions Integration

Step Functions integrations enable integrating an HTTP API route with AWS Step Functions.
This allows the HTTP API to start state machine executions synchronously or asynchronously, or to stop executions.

When a client invokes the route configured with a Step Functions integration, the API Gateway service interacts with the specified state machine according to the integration subtype (e.g., starts a new execution, synchronously starts an execution, or stops an execution) and returns the response to the client.

The following code configures a Step Functions integrations:

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpStepFunctionsIntegration
import aws_cdk.aws_stepfunctions as sfn

# state_machine: sfn.StateMachine
# http_api: apigwv2.HttpApi


http_api.add_routes(
    path="/start",
    methods=[apigwv2.HttpMethod.POST],
    integration=HttpStepFunctionsIntegration("StartExecutionIntegration",
        state_machine=state_machine,
        subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_START_EXECUTION
    )
)

http_api.add_routes(
    path="/start-sync",
    methods=[apigwv2.HttpMethod.POST],
    integration=HttpStepFunctionsIntegration("StartSyncExecutionIntegration",
        state_machine=state_machine,
        subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_START_SYNC_EXECUTION
    )
)

http_api.add_routes(
    path="/stop",
    methods=[apigwv2.HttpMethod.POST],
    integration=HttpStepFunctionsIntegration("StopExecutionIntegration",
        state_machine=state_machine,
        subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_STOP_EXECUTION,
        # For the `STOP_EXECUTION` subtype, it is necessary to specify the `executionArn`.
        parameter_mapping=apigwv2.ParameterMapping().custom("ExecutionArn", "$request.querystring.executionArn")
    )
)
```

**Note**:

* The `executionArn` parameter is required for the `STOP_EXECUTION` subtype. It is necessary to specify the `executionArn` in the `parameterMapping` property of the `HttpStepFunctionsIntegration` object.
* `START_SYNC_EXECUTION` subtype is only supported for EXPRESS type state machine.

### Private Integration

Private integrations enable integrating an HTTP API route with private resources in a VPC, such as Application Load Balancers or
Amazon ECS container-based applications.  Using private integrations, resources in a VPC can be exposed for access by
clients outside of the VPC.

The following integrations are supported for private resources in a VPC.

#### Application Load Balancer

The following code is a basic application load balancer private integration of HTTP API:

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpAlbIntegration


vpc = ec2.Vpc(self, "VPC")
lb = elbv2.ApplicationLoadBalancer(self, "lb", vpc=vpc)
listener = lb.add_listener("listener", port=80)
listener.add_targets("target",
    port=80
)

http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
    default_integration=HttpAlbIntegration("DefaultIntegration", listener)
)
```

When an imported load balancer is used, the `vpc` option must be specified for `HttpAlbIntegration`.

#### Network Load Balancer

The following code is a basic network load balancer private integration of HTTP API:

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpNlbIntegration


vpc = ec2.Vpc(self, "VPC")
lb = elbv2.NetworkLoadBalancer(self, "lb", vpc=vpc)
listener = lb.add_listener("listener", port=80)
listener.add_targets("target",
    port=80
)

http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
    default_integration=HttpNlbIntegration("DefaultIntegration", listener)
)
```

When an imported load balancer is used, the `vpc` option must be specified for `HttpNlbIntegration`.

#### Cloud Map Service Discovery

The following code is a basic discovery service private integration of HTTP API:

```python
import aws_cdk.aws_servicediscovery as servicediscovery
from aws_cdk.aws_apigatewayv2_integrations import HttpServiceDiscoveryIntegration


vpc = ec2.Vpc(self, "VPC")
vpc_link = apigwv2.VpcLink(self, "VpcLink", vpc=vpc)
namespace = servicediscovery.PrivateDnsNamespace(self, "Namespace",
    name="boobar.com",
    vpc=vpc
)
service = namespace.create_service("Service")

http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
    default_integration=HttpServiceDiscoveryIntegration("DefaultIntegration", service,
        vpc_link=vpc_link
    )
)
```

### Request Parameters

Request parameter mapping allows API requests from clients to be modified before they reach backend integrations.
Parameter mapping can be used to specify modifications to request parameters. See [Transforming API requests and
responses](https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html).

The following example creates a new header - `header2` - as a copy of `header1` and removes `header1`.

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpAlbIntegration

# lb: elbv2.ApplicationLoadBalancer

listener = lb.add_listener("listener", port=80)
listener.add_targets("target",
    port=80
)

http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
    default_integration=HttpAlbIntegration("DefaultIntegration", listener,
        parameter_mapping=apigwv2.ParameterMapping().append_header("header2", apigwv2.MappingValue.request_header("header1")).remove_header("header1")
    )
)
```

To add mapping keys and values not yet supported by the CDK, use the `custom()` method:

```python
from aws_cdk.aws_apigatewayv2_integrations import HttpAlbIntegration

# lb: elbv2.ApplicationLoadBalancer

listener = lb.add_listener("listener", port=80)
listener.add_targets("target",
    port=80
)

http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
    default_integration=HttpAlbIntegration("DefaultIntegration", listener,
        parameter_mapping=apigwv2.ParameterMapping().custom("myKey", "myValue")
    )
)
```

## WebSocket APIs

WebSocket integrations connect a route to backend resources. The following integrations are supported in the CDK.

### Lambda WebSocket Integration

Lambda integrations enable integrating a WebSocket API route with a Lambda function. When a client connects/disconnects
or sends a message specific to a route, the API Gateway service forwards the request to the Lambda function

The API Gateway service will invoke the Lambda function with an event payload of a specific format.

The following code configures a `sendMessage` route with a Lambda integration

```python
from aws_cdk.aws_apigatewayv2_integrations import WebSocketLambdaIntegration

# message_handler: lambda.Function


web_socket_api = apigwv2.WebSocketApi(self, "mywsapi")
apigwv2.WebSocketStage(self, "mystage",
    web_socket_api=web_socket_api,
    stage_name="dev",
    auto_deploy=True
)
web_socket_api.add_route("sendMessage",
    integration=WebSocketLambdaIntegration("SendMessageIntegration", message_handler)
)
```

### AWS WebSocket Integration

AWS type integrations enable integrating with any supported AWS service. This is only supported for WebSocket APIs. When a client
connects/disconnects or sends a message specific to a route, the API Gateway service forwards the request to the specified AWS service.

The following code configures a `$connect` route with a AWS integration that integrates with a dynamodb table. On websocket api connect,
it will write new entry to the dynamodb table.

```python
from aws_cdk.aws_apigatewayv2_integrations import WebSocketAwsIntegration
import aws_cdk.aws_dynamodb as dynamodb
import aws_cdk.aws_iam as iam

# api_role: iam.Role
# table: dynamodb.Table


web_socket_api = apigwv2.WebSocketApi(self, "mywsapi")
apigwv2.WebSocketStage(self, "mystage",
    web_socket_api=web_socket_api,
    stage_name="dev",
    auto_deploy=True
)
web_socket_api.add_route("$connect",
    integration=WebSocketAwsIntegration("DynamodbPutItem",
        integration_uri=f"arn:aws:apigateway:{this.region}:dynamodb:action/PutItem",
        integration_method=apigwv2.HttpMethod.POST,
        credentials_role=api_role,
        request_templates={
            "application/json": JSON.stringify({
                "TableName": table.table_name,
                "Item": {
                    "id": {
                        "S": "$context.requestId"
                    }
                }
            })
        }
    )
)
```

You can also set additional properties to change the behavior of your integration, such as `contentHandling`.
See [Working with binary media types for WebSocket APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/websocket-api-develop-binary-media-types.html).
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
from .. import Duration as _Duration_4839e8c3
from ..aws_apigatewayv2 import (
    ContentHandling as _ContentHandling_1512a7da,
    HttpConnectionType as _HttpConnectionType_02a8b6fb,
    HttpIntegrationSubtype as _HttpIntegrationSubtype_beb63b59,
    HttpIntegrationType as _HttpIntegrationType_aee0d440,
    HttpMethod as _HttpMethod_4c4f3090,
    HttpRouteIntegration as _HttpRouteIntegration_d3ee7c34,
    HttpRouteIntegrationBindOptions as _HttpRouteIntegrationBindOptions_f870a39e,
    HttpRouteIntegrationConfig as _HttpRouteIntegrationConfig_aafc4b76,
    IHttpRoute as _IHttpRoute_2fbc6171,
    IVpcLink as _IVpcLink_adecf0e2,
    IWebSocketRoute as _IWebSocketRoute_006c2390,
    ParameterMapping as _ParameterMapping_c11a48e0,
    PassthroughBehavior as _PassthroughBehavior_379b8a9e,
    PayloadFormatVersion as _PayloadFormatVersion_a469cb03,
    WebSocketRouteIntegration as _WebSocketRouteIntegration_bb950e43,
    WebSocketRouteIntegrationBindOptions as _WebSocketRouteIntegrationBindOptions_4f27dddb,
    WebSocketRouteIntegrationConfig as _WebSocketRouteIntegrationConfig_7402c18a,
)
from ..aws_elasticloadbalancingv2 import (
    IApplicationListener as _IApplicationListener_60f2beb6,
    INetworkListener as _INetworkListener_fccca3bd,
)
from ..aws_iam import IRole as _IRole_235f5d8e
from ..aws_lambda import IFunction as _IFunction_6adb0ab8
from ..aws_servicediscovery import IService as _IService_46860ae1
from ..aws_stepfunctions import StateMachine as _StateMachine_a256d24f


class HttpAlbIntegration(
    _HttpRouteIntegration_d3ee7c34,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpAlbIntegration",
):
    '''The Application Load Balancer integration resource for HTTP API.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_integrations import HttpAlbIntegration
        
        
        vpc = ec2.Vpc(self, "VPC")
        lb = elbv2.ApplicationLoadBalancer(self, "lb", vpc=vpc)
        listener = lb.add_listener("listener", port=80)
        listener.add_targets("target",
            port=80
        )
        
        http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
            default_integration=HttpAlbIntegration("DefaultIntegration", listener)
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        listener: _IApplicationListener_60f2beb6,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param listener: the ELB application listener.
        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__928f282b08310c18e1704595722c48f29856eea7d0afc8e0dd89d67e61a77820)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
        props = HttpAlbIntegrationProps(
            method=method,
            parameter_mapping=parameter_mapping,
            secure_server_name=secure_server_name,
            vpc_link=vpc_link,
        )

        jsii.create(self.__class__, self, [id, listener, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _HttpRouteIntegrationConfig_aafc4b76:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(_HttpRouteIntegrationConfig_aafc4b76, jsii.invoke(self, "bind", [options]))

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def _connection_type(self) -> _HttpConnectionType_02a8b6fb:
        return typing.cast(_HttpConnectionType_02a8b6fb, jsii.get(self, "connectionType"))

    @_connection_type.setter
    def _connection_type(self, value: _HttpConnectionType_02a8b6fb) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddd81275967dd8f82fea61a7accd8241f873539fe596998c66af3c580e913284)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def _http_method(self) -> _HttpMethod_4c4f3090:
        return typing.cast(_HttpMethod_4c4f3090, jsii.get(self, "httpMethod"))

    @_http_method.setter
    def _http_method(self, value: _HttpMethod_4c4f3090) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49d2707c331ffacddcce15a9f8462f5b4bd86acafca4f99ffac86d61fdd968c5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def _integration_type(self) -> _HttpIntegrationType_aee0d440:
        return typing.cast(_HttpIntegrationType_aee0d440, jsii.get(self, "integrationType"))

    @_integration_type.setter
    def _integration_type(self, value: _HttpIntegrationType_aee0d440) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68d6f772e2a89442556f1760d95c537293e8868e69f39350b976830ea7c5d7c8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersion")
    def _payload_format_version(self) -> _PayloadFormatVersion_a469cb03:
        return typing.cast(_PayloadFormatVersion_a469cb03, jsii.get(self, "payloadFormatVersion"))

    @_payload_format_version.setter
    def _payload_format_version(self, value: _PayloadFormatVersion_a469cb03) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6120aff86732fb3507f4b0835b6bc561a686dcb25788f79481dc42c78203b26)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadFormatVersion", value)


class HttpLambdaIntegration(
    _HttpRouteIntegration_d3ee7c34,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpLambdaIntegration",
):
    '''The Lambda Proxy integration resource for HTTP API.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_integrations import HttpLambdaIntegration
        
        # books_default_fn: lambda.Function
        
        books_integration = HttpLambdaIntegration("BooksIntegration", books_default_fn)
        
        http_api = apigwv2.HttpApi(self, "HttpApi")
        
        http_api.add_routes(
            path="/books",
            methods=[apigwv2.HttpMethod.GET],
            integration=books_integration
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        handler: _IFunction_6adb0ab8,
        *,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        payload_format_version: typing.Optional[_PayloadFormatVersion_a469cb03] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param handler: the Lambda handler to integrate with.
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param payload_format_version: Version of the payload sent to the lambda handler. Default: PayloadFormatVersion.VERSION_2_0
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__186fcdf4e12ad29dbad06f4ae566e815dd0e4855b4b9ffd6626f945f2a4aee19)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = HttpLambdaIntegrationProps(
            parameter_mapping=parameter_mapping,
            payload_format_version=payload_format_version,
        )

        jsii.create(self.__class__, self, [id, handler, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _HttpRouteIntegrationConfig_aafc4b76:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        _options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(_HttpRouteIntegrationConfig_aafc4b76, jsii.invoke(self, "bind", [_options]))

    @jsii.member(jsii_name="completeBind")
    def _complete_bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> None:
        '''Complete the binding of the integration to the route.

        In some cases, there is
        some additional work to do, such as adding permissions for the API to access
        the target. This work is necessary whether the integration has just been
        created for this route or it is an existing one, previously created for other
        routes. In most cases, however, concrete implementations do not need to
        override this method.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(None, jsii.invoke(self, "completeBind", [options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpLambdaIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "parameter_mapping": "parameterMapping",
        "payload_format_version": "payloadFormatVersion",
    },
)
class HttpLambdaIntegrationProps:
    def __init__(
        self,
        *,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        payload_format_version: typing.Optional[_PayloadFormatVersion_a469cb03] = None,
    ) -> None:
        '''Lambda Proxy integration properties.

        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param payload_format_version: Version of the payload sent to the lambda handler. Default: PayloadFormatVersion.VERSION_2_0

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
            
            # parameter_mapping: apigatewayv2.ParameterMapping
            # payload_format_version: apigatewayv2.PayloadFormatVersion
            
            http_lambda_integration_props = apigatewayv2_integrations.HttpLambdaIntegrationProps(
                parameter_mapping=parameter_mapping,
                payload_format_version=payload_format_version
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7494501e4bf220385c831472b8042a561df79a565c497e77d41cfc10427bce41)
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
            check_type(argname="argument payload_format_version", value=payload_format_version, expected_type=type_hints["payload_format_version"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping
        if payload_format_version is not None:
            self._values["payload_format_version"] = payload_format_version

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        :default: undefined requests are sent to the backend unmodified

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    @builtins.property
    def payload_format_version(self) -> typing.Optional[_PayloadFormatVersion_a469cb03]:
        '''Version of the payload sent to the lambda handler.

        :default: PayloadFormatVersion.VERSION_2_0

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-develop-integrations-lambda.html
        '''
        result = self._values.get("payload_format_version")
        return typing.cast(typing.Optional[_PayloadFormatVersion_a469cb03], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpLambdaIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpNlbIntegration(
    _HttpRouteIntegration_d3ee7c34,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpNlbIntegration",
):
    '''The Network Load Balancer integration resource for HTTP API.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_integrations import HttpNlbIntegration
        
        
        vpc = ec2.Vpc(self, "VPC")
        lb = elbv2.NetworkLoadBalancer(self, "lb", vpc=vpc)
        listener = lb.add_listener("listener", port=80)
        listener.add_targets("target",
            port=80
        )
        
        http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
            default_integration=HttpNlbIntegration("DefaultIntegration", listener)
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        listener: _INetworkListener_fccca3bd,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param listener: the ELB network listener.
        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__543e48e97b53816262605885854d56b7f2c624e9fe59f7e60eadcde801acaebd)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument listener", value=listener, expected_type=type_hints["listener"])
        props = HttpNlbIntegrationProps(
            method=method,
            parameter_mapping=parameter_mapping,
            secure_server_name=secure_server_name,
            vpc_link=vpc_link,
        )

        jsii.create(self.__class__, self, [id, listener, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _HttpRouteIntegrationConfig_aafc4b76:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(_HttpRouteIntegrationConfig_aafc4b76, jsii.invoke(self, "bind", [options]))

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def _connection_type(self) -> _HttpConnectionType_02a8b6fb:
        return typing.cast(_HttpConnectionType_02a8b6fb, jsii.get(self, "connectionType"))

    @_connection_type.setter
    def _connection_type(self, value: _HttpConnectionType_02a8b6fb) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d360e4b817e6fc6c8ae4e1350d9dd6b3d69b40c54401465c6ef888953f765e38)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def _http_method(self) -> _HttpMethod_4c4f3090:
        return typing.cast(_HttpMethod_4c4f3090, jsii.get(self, "httpMethod"))

    @_http_method.setter
    def _http_method(self, value: _HttpMethod_4c4f3090) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c789ab75d5a6290c76fe8fce0b824cd0926bb50f6f9fb91ff77ef01e82a1ea0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def _integration_type(self) -> _HttpIntegrationType_aee0d440:
        return typing.cast(_HttpIntegrationType_aee0d440, jsii.get(self, "integrationType"))

    @_integration_type.setter
    def _integration_type(self, value: _HttpIntegrationType_aee0d440) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__585857799e486703df2825ecce003717b9e731a7928c8409a6da811435c79165)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersion")
    def _payload_format_version(self) -> _PayloadFormatVersion_a469cb03:
        return typing.cast(_PayloadFormatVersion_a469cb03, jsii.get(self, "payloadFormatVersion"))

    @_payload_format_version.setter
    def _payload_format_version(self, value: _PayloadFormatVersion_a469cb03) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__36f10890866a2476ef7a837c18a7bab079976e4adf47e736ccebe3fc7ec980ca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadFormatVersion", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpPrivateIntegrationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "method": "method",
        "parameter_mapping": "parameterMapping",
        "secure_server_name": "secureServerName",
        "vpc_link": "vpcLink",
    },
)
class HttpPrivateIntegrationOptions:
    def __init__(
        self,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''Base options for private integration.

        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
            
            # parameter_mapping: apigatewayv2.ParameterMapping
            # vpc_link: apigatewayv2.VpcLink
            
            http_private_integration_options = apigatewayv2_integrations.HttpPrivateIntegrationOptions(
                method=apigatewayv2.HttpMethod.ANY,
                parameter_mapping=parameter_mapping,
                secure_server_name="secureServerName",
                vpc_link=vpc_link
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d60e74e57400fa0f9757a69ecb53197543ad6fd054f8168eaa56d7cd010107b5)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
            check_type(argname="argument secure_server_name", value=secure_server_name, expected_type=type_hints["secure_server_name"])
            check_type(argname="argument vpc_link", value=vpc_link, expected_type=type_hints["vpc_link"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping
        if secure_server_name is not None:
            self._values["secure_server_name"] = secure_server_name
        if vpc_link is not None:
            self._values["vpc_link"] = vpc_link

    @builtins.property
    def method(self) -> typing.Optional[_HttpMethod_4c4f3090]:
        '''The HTTP method that must be used to invoke the underlying HTTP proxy.

        :default: HttpMethod.ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[_HttpMethod_4c4f3090], result)

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        :default: undefined requests are sent to the backend unmodified

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    @builtins.property
    def secure_server_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the server name to verified by HTTPS when calling the backend integration.

        :default: undefined private integration traffic will use HTTP protocol

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html
        '''
        result = self._values.get("secure_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_link(self) -> typing.Optional[_IVpcLink_adecf0e2]:
        '''The vpc link to be used for the private integration.

        :default: - a new VpcLink is created
        '''
        result = self._values.get("vpc_link")
        return typing.cast(typing.Optional[_IVpcLink_adecf0e2], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpPrivateIntegrationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpServiceDiscoveryIntegration(
    _HttpRouteIntegration_d3ee7c34,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpServiceDiscoveryIntegration",
):
    '''The Service Discovery integration resource for HTTP API.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_servicediscovery as servicediscovery
        from aws_cdk.aws_apigatewayv2_integrations import HttpServiceDiscoveryIntegration
        
        
        vpc = ec2.Vpc(self, "VPC")
        vpc_link = apigwv2.VpcLink(self, "VpcLink", vpc=vpc)
        namespace = servicediscovery.PrivateDnsNamespace(self, "Namespace",
            name="boobar.com",
            vpc=vpc
        )
        service = namespace.create_service("Service")
        
        http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
            default_integration=HttpServiceDiscoveryIntegration("DefaultIntegration", service,
                vpc_link=vpc_link
            )
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        service: _IService_46860ae1,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param service: the service discovery resource to integrate with.
        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc876ae5ee3ca1141486563e7214d682fb6d2e3b3b1ab6b4f91e525d7a19b53e)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
        props = HttpServiceDiscoveryIntegrationProps(
            method=method,
            parameter_mapping=parameter_mapping,
            secure_server_name=secure_server_name,
            vpc_link=vpc_link,
        )

        jsii.create(self.__class__, self, [id, service, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _HttpRouteIntegrationConfig_aafc4b76:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        _options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(_HttpRouteIntegrationConfig_aafc4b76, jsii.invoke(self, "bind", [_options]))

    @builtins.property
    @jsii.member(jsii_name="connectionType")
    def _connection_type(self) -> _HttpConnectionType_02a8b6fb:
        return typing.cast(_HttpConnectionType_02a8b6fb, jsii.get(self, "connectionType"))

    @_connection_type.setter
    def _connection_type(self, value: _HttpConnectionType_02a8b6fb) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88fa11bc73bf44288cb7467c39d6aa21cc34611adb58ae52dbcb42fe2150a266)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionType", value)

    @builtins.property
    @jsii.member(jsii_name="httpMethod")
    def _http_method(self) -> _HttpMethod_4c4f3090:
        return typing.cast(_HttpMethod_4c4f3090, jsii.get(self, "httpMethod"))

    @_http_method.setter
    def _http_method(self, value: _HttpMethod_4c4f3090) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3cc3ee501484e0e7058df9083bcfc3e410c2de2357a283e797038514e45bae8e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "httpMethod", value)

    @builtins.property
    @jsii.member(jsii_name="integrationType")
    def _integration_type(self) -> _HttpIntegrationType_aee0d440:
        return typing.cast(_HttpIntegrationType_aee0d440, jsii.get(self, "integrationType"))

    @_integration_type.setter
    def _integration_type(self, value: _HttpIntegrationType_aee0d440) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5909d37808307699be7a07730689164f1e138383252eae1d7c68420302f2e9c4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "integrationType", value)

    @builtins.property
    @jsii.member(jsii_name="payloadFormatVersion")
    def _payload_format_version(self) -> _PayloadFormatVersion_a469cb03:
        return typing.cast(_PayloadFormatVersion_a469cb03, jsii.get(self, "payloadFormatVersion"))

    @_payload_format_version.setter
    def _payload_format_version(self, value: _PayloadFormatVersion_a469cb03) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2db70ce1255fd6ff4a3b0a88a1c0a0096c5eb165bf1ce3544bee82d10bcc54d7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "payloadFormatVersion", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpServiceDiscoveryIntegrationProps",
    jsii_struct_bases=[HttpPrivateIntegrationOptions],
    name_mapping={
        "method": "method",
        "parameter_mapping": "parameterMapping",
        "secure_server_name": "secureServerName",
        "vpc_link": "vpcLink",
    },
)
class HttpServiceDiscoveryIntegrationProps(HttpPrivateIntegrationOptions):
    def __init__(
        self,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''Properties to initialize ``HttpServiceDiscoveryIntegration``.

        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_servicediscovery as servicediscovery
            from aws_cdk.aws_apigatewayv2_integrations import HttpServiceDiscoveryIntegration
            
            
            vpc = ec2.Vpc(self, "VPC")
            vpc_link = apigwv2.VpcLink(self, "VpcLink", vpc=vpc)
            namespace = servicediscovery.PrivateDnsNamespace(self, "Namespace",
                name="boobar.com",
                vpc=vpc
            )
            service = namespace.create_service("Service")
            
            http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
                default_integration=HttpServiceDiscoveryIntegration("DefaultIntegration", service,
                    vpc_link=vpc_link
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8bbb857ee24522818d504a3830c65b95bbc66b9ef70c67fa5b85fbdca1aaf1c1)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
            check_type(argname="argument secure_server_name", value=secure_server_name, expected_type=type_hints["secure_server_name"])
            check_type(argname="argument vpc_link", value=vpc_link, expected_type=type_hints["vpc_link"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping
        if secure_server_name is not None:
            self._values["secure_server_name"] = secure_server_name
        if vpc_link is not None:
            self._values["vpc_link"] = vpc_link

    @builtins.property
    def method(self) -> typing.Optional[_HttpMethod_4c4f3090]:
        '''The HTTP method that must be used to invoke the underlying HTTP proxy.

        :default: HttpMethod.ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[_HttpMethod_4c4f3090], result)

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        :default: undefined requests are sent to the backend unmodified

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    @builtins.property
    def secure_server_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the server name to verified by HTTPS when calling the backend integration.

        :default: undefined private integration traffic will use HTTP protocol

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html
        '''
        result = self._values.get("secure_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_link(self) -> typing.Optional[_IVpcLink_adecf0e2]:
        '''The vpc link to be used for the private integration.

        :default: - a new VpcLink is created
        '''
        result = self._values.get("vpc_link")
        return typing.cast(typing.Optional[_IVpcLink_adecf0e2], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpServiceDiscoveryIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpStepFunctionsIntegration(
    _HttpRouteIntegration_d3ee7c34,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpStepFunctionsIntegration",
):
    '''The StepFunctions integration resource for HTTP API.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_integrations import HttpStepFunctionsIntegration
        import aws_cdk.aws_stepfunctions as sfn
        
        # state_machine: sfn.StateMachine
        # http_api: apigwv2.HttpApi
        
        
        http_api.add_routes(
            path="/start",
            methods=[apigwv2.HttpMethod.POST],
            integration=HttpStepFunctionsIntegration("StartExecutionIntegration",
                state_machine=state_machine,
                subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_START_EXECUTION
            )
        )
        
        http_api.add_routes(
            path="/start-sync",
            methods=[apigwv2.HttpMethod.POST],
            integration=HttpStepFunctionsIntegration("StartSyncExecutionIntegration",
                state_machine=state_machine,
                subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_START_SYNC_EXECUTION
            )
        )
        
        http_api.add_routes(
            path="/stop",
            methods=[apigwv2.HttpMethod.POST],
            integration=HttpStepFunctionsIntegration("StopExecutionIntegration",
                state_machine=state_machine,
                subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_STOP_EXECUTION,
                # For the `STOP_EXECUTION` subtype, it is necessary to specify the `executionArn`.
                parameter_mapping=apigwv2.ParameterMapping().custom("ExecutionArn", "$request.querystring.executionArn")
            )
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        state_machine: _StateMachine_a256d24f,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        subtype: typing.Optional[_HttpIntegrationSubtype_beb63b59] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param state_machine: Statemachine that Integrates with API Gateway.
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. When the subtype is either ``START_EXECUTION`` or ``START_SYNC_EXECUTION``, it is necessary to specify the ``StateMachineArn``. Conversely, when the subtype is ``STOP_EXECUTION``, the ``ExecutionArn`` must be specified. Default: - specify only ``StateMachineArn``
        :param subtype: The subtype of the HTTP integration. Only subtypes starting with STEPFUNCTIONS_ can be specified. Default: HttpIntegrationSubtype.STEPFUNCTIONS_START_EXECUTION
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76518171338936bd0fbff4054b2b72b876355e21b6eef931d4dd4f111fc7889f)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HttpStepFunctionsIntegrationProps(
            state_machine=state_machine,
            parameter_mapping=parameter_mapping,
            subtype=subtype,
        )

        jsii.create(self.__class__, self, [id, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _HttpRouteIntegrationConfig_aafc4b76:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(_HttpRouteIntegrationConfig_aafc4b76, jsii.invoke(self, "bind", [options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpStepFunctionsIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "state_machine": "stateMachine",
        "parameter_mapping": "parameterMapping",
        "subtype": "subtype",
    },
)
class HttpStepFunctionsIntegrationProps:
    def __init__(
        self,
        *,
        state_machine: _StateMachine_a256d24f,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        subtype: typing.Optional[_HttpIntegrationSubtype_beb63b59] = None,
    ) -> None:
        '''Properties to initialize ``HttpStepFunctionsIntegration``.

        :param state_machine: Statemachine that Integrates with API Gateway.
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. When the subtype is either ``START_EXECUTION`` or ``START_SYNC_EXECUTION``, it is necessary to specify the ``StateMachineArn``. Conversely, when the subtype is ``STOP_EXECUTION``, the ``ExecutionArn`` must be specified. Default: - specify only ``StateMachineArn``
        :param subtype: The subtype of the HTTP integration. Only subtypes starting with STEPFUNCTIONS_ can be specified. Default: HttpIntegrationSubtype.STEPFUNCTIONS_START_EXECUTION

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_apigatewayv2_integrations import HttpStepFunctionsIntegration
            import aws_cdk.aws_stepfunctions as sfn
            
            # state_machine: sfn.StateMachine
            # http_api: apigwv2.HttpApi
            
            
            http_api.add_routes(
                path="/start",
                methods=[apigwv2.HttpMethod.POST],
                integration=HttpStepFunctionsIntegration("StartExecutionIntegration",
                    state_machine=state_machine,
                    subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_START_EXECUTION
                )
            )
            
            http_api.add_routes(
                path="/start-sync",
                methods=[apigwv2.HttpMethod.POST],
                integration=HttpStepFunctionsIntegration("StartSyncExecutionIntegration",
                    state_machine=state_machine,
                    subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_START_SYNC_EXECUTION
                )
            )
            
            http_api.add_routes(
                path="/stop",
                methods=[apigwv2.HttpMethod.POST],
                integration=HttpStepFunctionsIntegration("StopExecutionIntegration",
                    state_machine=state_machine,
                    subtype=apigwv2.HttpIntegrationSubtype.STEPFUNCTIONS_STOP_EXECUTION,
                    # For the `STOP_EXECUTION` subtype, it is necessary to specify the `executionArn`.
                    parameter_mapping=apigwv2.ParameterMapping().custom("ExecutionArn", "$request.querystring.executionArn")
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7072515a6bcc56ecf05d39b9b84f7dde9de04e9c2caf9ada206b863db8625ed)
            check_type(argname="argument state_machine", value=state_machine, expected_type=type_hints["state_machine"])
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
            check_type(argname="argument subtype", value=subtype, expected_type=type_hints["subtype"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "state_machine": state_machine,
        }
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping
        if subtype is not None:
            self._values["subtype"] = subtype

    @builtins.property
    def state_machine(self) -> _StateMachine_a256d24f:
        '''Statemachine that Integrates with API Gateway.'''
        result = self._values.get("state_machine")
        assert result is not None, "Required property 'state_machine' is missing"
        return typing.cast(_StateMachine_a256d24f, result)

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        When the subtype is either ``START_EXECUTION`` or ``START_SYNC_EXECUTION``,
        it is necessary to specify the ``StateMachineArn``.
        Conversely, when the subtype is ``STOP_EXECUTION``, the ``ExecutionArn`` must be specified.

        :default: - specify only ``StateMachineArn``

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    @builtins.property
    def subtype(self) -> typing.Optional[_HttpIntegrationSubtype_beb63b59]:
        '''The subtype of the HTTP integration.

        Only subtypes starting with STEPFUNCTIONS_ can be specified.

        :default: HttpIntegrationSubtype.STEPFUNCTIONS_START_EXECUTION
        '''
        result = self._values.get("subtype")
        return typing.cast(typing.Optional[_HttpIntegrationSubtype_beb63b59], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpStepFunctionsIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class HttpUrlIntegration(
    _HttpRouteIntegration_d3ee7c34,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpUrlIntegration",
):
    '''The HTTP Proxy integration resource for HTTP API.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_authorizers import HttpLambdaAuthorizer, HttpLambdaResponseType
        from aws_cdk.aws_apigatewayv2_integrations import HttpUrlIntegration
        
        # This function handles your auth logic
        # auth_handler: lambda.Function
        
        
        authorizer = HttpLambdaAuthorizer("BooksAuthorizer", auth_handler,
            response_types=[HttpLambdaResponseType.SIMPLE]
        )
        
        api = apigwv2.HttpApi(self, "HttpApi")
        
        api.add_routes(
            integration=HttpUrlIntegration("BooksIntegration", "https://get-books-proxy.example.com"),
            path="/books",
            authorizer=authorizer
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        url: builtins.str,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param url: the URL to proxy to.
        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__39ce64d79e6c4249c8c60321022b7721149966e379b0f947f602cb248aee9bce)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
        props = HttpUrlIntegrationProps(
            method=method, parameter_mapping=parameter_mapping
        )

        jsii.create(self.__class__, self, [id, url, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IHttpRoute_2fbc6171,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _HttpRouteIntegrationConfig_aafc4b76:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``HttpRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        _options = _HttpRouteIntegrationBindOptions_f870a39e(route=route, scope=scope)

        return typing.cast(_HttpRouteIntegrationConfig_aafc4b76, jsii.invoke(self, "bind", [_options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpUrlIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={"method": "method", "parameter_mapping": "parameterMapping"},
)
class HttpUrlIntegrationProps:
    def __init__(
        self,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    ) -> None:
        '''Properties to initialize a new ``HttpProxyIntegration``.

        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
            
            # parameter_mapping: apigatewayv2.ParameterMapping
            
            http_url_integration_props = apigatewayv2_integrations.HttpUrlIntegrationProps(
                method=apigatewayv2.HttpMethod.ANY,
                parameter_mapping=parameter_mapping
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__abe29aa89dc1da944745a812d1d5e87dd81ab57867504a928a129c8b904c99da)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping

    @builtins.property
    def method(self) -> typing.Optional[_HttpMethod_4c4f3090]:
        '''The HTTP method that must be used to invoke the underlying HTTP proxy.

        :default: HttpMethod.ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[_HttpMethod_4c4f3090], result)

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        :default: undefined requests are sent to the backend unmodified

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpUrlIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebSocketAwsIntegration(
    _WebSocketRouteIntegration_bb950e43,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.WebSocketAwsIntegration",
):
    '''AWS WebSocket AWS Type Integration.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_integrations import WebSocketAwsIntegration
        import aws_cdk.aws_dynamodb as dynamodb
        import aws_cdk.aws_iam as iam
        
        # api_role: iam.Role
        # table: dynamodb.Table
        
        
        web_socket_api = apigwv2.WebSocketApi(self, "mywsapi")
        apigwv2.WebSocketStage(self, "mystage",
            web_socket_api=web_socket_api,
            stage_name="dev",
            auto_deploy=True
        )
        web_socket_api.add_route("$connect",
            integration=WebSocketAwsIntegration("DynamodbPutItem",
                integration_uri=f"arn:aws:apigateway:{this.region}:dynamodb:action/PutItem",
                integration_method=apigwv2.HttpMethod.POST,
                credentials_role=api_role,
                request_templates={
                    "application/json": JSON.stringify({
                        "TableName": table.table_name,
                        "Item": {
                            "id": {
                                "S": "$context.requestId"
                            }
                        }
                    })
                }
            )
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        *,
        integration_method: builtins.str,
        integration_uri: builtins.str,
        content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
        credentials_role: typing.Optional[_IRole_235f5d8e] = None,
        passthrough_behavior: typing.Optional[_PassthroughBehavior_379b8a9e] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param integration_method: Specifies the integration's HTTP method type.
        :param integration_uri: Integration URI.
        :param content_handling: Specifies how to handle response payload content type conversions. Default: - The response payload will be passed through from the integration response to the route response or method response without modification.
        :param credentials_role: Specifies the credentials role required for the integration. Default: - No credential role provided.
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Default: - No passthrough behavior required.
        :param request_parameters: The request parameters that API Gateway sends with the backend request. Specify request parameters as key-value pairs (string-to-string mappings), with a destination as the key and a source as the value. Default: - No request parameter provided to the integration.
        :param request_templates: A map of Apache Velocity templates that are applied on the request payload. Example:: { "application/json": "{ \\"statusCode\\": 200 }" } Default: - No request template provided to the integration.
        :param template_selection_expression: The template selection expression for the integration. Default: - No template selection expression provided.
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9bba00d2a284a155db9e940bdf51118b0715f0312e8109e916f7848b20023815)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = WebSocketAwsIntegrationProps(
            integration_method=integration_method,
            integration_uri=integration_uri,
            content_handling=content_handling,
            credentials_role=credentials_role,
            passthrough_behavior=passthrough_behavior,
            request_parameters=request_parameters,
            request_templates=request_templates,
            template_selection_expression=template_selection_expression,
            timeout=timeout,
        )

        jsii.create(self.__class__, self, [id, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IWebSocketRoute_006c2390,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _WebSocketRouteIntegrationConfig_7402c18a:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``WebSocketRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        _options = _WebSocketRouteIntegrationBindOptions_4f27dddb(
            route=route, scope=scope
        )

        return typing.cast(_WebSocketRouteIntegrationConfig_7402c18a, jsii.invoke(self, "bind", [_options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.WebSocketAwsIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={
        "integration_method": "integrationMethod",
        "integration_uri": "integrationUri",
        "content_handling": "contentHandling",
        "credentials_role": "credentialsRole",
        "passthrough_behavior": "passthroughBehavior",
        "request_parameters": "requestParameters",
        "request_templates": "requestTemplates",
        "template_selection_expression": "templateSelectionExpression",
        "timeout": "timeout",
    },
)
class WebSocketAwsIntegrationProps:
    def __init__(
        self,
        *,
        integration_method: builtins.str,
        integration_uri: builtins.str,
        content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
        credentials_role: typing.Optional[_IRole_235f5d8e] = None,
        passthrough_behavior: typing.Optional[_PassthroughBehavior_379b8a9e] = None,
        request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        template_selection_expression: typing.Optional[builtins.str] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Props for AWS type integration for a WebSocket Api.

        :param integration_method: Specifies the integration's HTTP method type.
        :param integration_uri: Integration URI.
        :param content_handling: Specifies how to handle response payload content type conversions. Default: - The response payload will be passed through from the integration response to the route response or method response without modification.
        :param credentials_role: Specifies the credentials role required for the integration. Default: - No credential role provided.
        :param passthrough_behavior: Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource. There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and NEVER. Default: - No passthrough behavior required.
        :param request_parameters: The request parameters that API Gateway sends with the backend request. Specify request parameters as key-value pairs (string-to-string mappings), with a destination as the key and a source as the value. Default: - No request parameter provided to the integration.
        :param request_templates: A map of Apache Velocity templates that are applied on the request payload. Example:: { "application/json": "{ \\"statusCode\\": 200 }" } Default: - No request template provided to the integration.
        :param template_selection_expression: The template selection expression for the integration. Default: - No template selection expression provided.
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_apigatewayv2_integrations import WebSocketAwsIntegration
            import aws_cdk.aws_dynamodb as dynamodb
            import aws_cdk.aws_iam as iam
            
            # api_role: iam.Role
            # table: dynamodb.Table
            
            
            web_socket_api = apigwv2.WebSocketApi(self, "mywsapi")
            apigwv2.WebSocketStage(self, "mystage",
                web_socket_api=web_socket_api,
                stage_name="dev",
                auto_deploy=True
            )
            web_socket_api.add_route("$connect",
                integration=WebSocketAwsIntegration("DynamodbPutItem",
                    integration_uri=f"arn:aws:apigateway:{this.region}:dynamodb:action/PutItem",
                    integration_method=apigwv2.HttpMethod.POST,
                    credentials_role=api_role,
                    request_templates={
                        "application/json": JSON.stringify({
                            "TableName": table.table_name,
                            "Item": {
                                "id": {
                                    "S": "$context.requestId"
                                }
                            }
                        })
                    }
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aa585be6945644a75e60414b518cacf76637190e70170ea912e9826651e3e5ea)
            check_type(argname="argument integration_method", value=integration_method, expected_type=type_hints["integration_method"])
            check_type(argname="argument integration_uri", value=integration_uri, expected_type=type_hints["integration_uri"])
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument credentials_role", value=credentials_role, expected_type=type_hints["credentials_role"])
            check_type(argname="argument passthrough_behavior", value=passthrough_behavior, expected_type=type_hints["passthrough_behavior"])
            check_type(argname="argument request_parameters", value=request_parameters, expected_type=type_hints["request_parameters"])
            check_type(argname="argument request_templates", value=request_templates, expected_type=type_hints["request_templates"])
            check_type(argname="argument template_selection_expression", value=template_selection_expression, expected_type=type_hints["template_selection_expression"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "integration_method": integration_method,
            "integration_uri": integration_uri,
        }
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if credentials_role is not None:
            self._values["credentials_role"] = credentials_role
        if passthrough_behavior is not None:
            self._values["passthrough_behavior"] = passthrough_behavior
        if request_parameters is not None:
            self._values["request_parameters"] = request_parameters
        if request_templates is not None:
            self._values["request_templates"] = request_templates
        if template_selection_expression is not None:
            self._values["template_selection_expression"] = template_selection_expression
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def integration_method(self) -> builtins.str:
        '''Specifies the integration's HTTP method type.'''
        result = self._values.get("integration_method")
        assert result is not None, "Required property 'integration_method' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def integration_uri(self) -> builtins.str:
        '''Integration URI.'''
        result = self._values.get("integration_uri")
        assert result is not None, "Required property 'integration_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def content_handling(self) -> typing.Optional[_ContentHandling_1512a7da]:
        '''Specifies how to handle response payload content type conversions.

        :default:

        - The response payload will be passed through from the integration response to
        the route response or method response without modification.
        '''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[_ContentHandling_1512a7da], result)

    @builtins.property
    def credentials_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Specifies the credentials role required for the integration.

        :default: - No credential role provided.
        '''
        result = self._values.get("credentials_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def passthrough_behavior(self) -> typing.Optional[_PassthroughBehavior_379b8a9e]:
        '''Specifies the pass-through behavior for incoming requests based on the Content-Type header in the request, and the available mapping templates specified as the requestTemplates property on the Integration resource.

        There are three valid values: WHEN_NO_MATCH, WHEN_NO_TEMPLATES, and
        NEVER.

        :default: - No passthrough behavior required.
        '''
        result = self._values.get("passthrough_behavior")
        return typing.cast(typing.Optional[_PassthroughBehavior_379b8a9e], result)

    @builtins.property
    def request_parameters(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The request parameters that API Gateway sends with the backend request.

        Specify request parameters as key-value pairs (string-to-string
        mappings), with a destination as the key and a source as the value.

        :default: - No request parameter provided to the integration.
        '''
        result = self._values.get("request_parameters")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def request_templates(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A map of Apache Velocity templates that are applied on the request payload.

        Example::

             { "application/json": "{ \\"statusCode\\": 200 }" }

        :default: - No request template provided to the integration.
        '''
        result = self._values.get("request_templates")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def template_selection_expression(self) -> typing.Optional[builtins.str]:
        '''The template selection expression for the integration.

        :default: - No template selection expression provided.
        '''
        result = self._values.get("template_selection_expression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum amount of time an integration will run before it returns without a response.

        Must be between 50 milliseconds and 29 seconds.

        :default: Duration.seconds(29)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebSocketAwsIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebSocketLambdaIntegration(
    _WebSocketRouteIntegration_bb950e43,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.WebSocketLambdaIntegration",
):
    '''Lambda WebSocket Integration.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_apigatewayv2_integrations import WebSocketLambdaIntegration
        
        # message_handler: lambda.Function
        
        
        web_socket_api = apigwv2.WebSocketApi(self, "mywsapi")
        apigwv2.WebSocketStage(self, "mystage",
            web_socket_api=web_socket_api,
            stage_name="dev",
            auto_deploy=True
        )
        web_socket_api.add_route("sendMessage",
            integration=WebSocketLambdaIntegration("SendMessageIntegration", message_handler)
        )
    '''

    def __init__(
        self,
        id: builtins.str,
        handler: _IFunction_6adb0ab8,
        *,
        content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param id: id of the underlying integration construct.
        :param handler: the Lambda function handler.
        :param content_handling: Specifies how to handle response payload content type conversions. Default: - The response payload will be passed through from the integration response to the route response or method response without modification.
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__990acb5e6eea396fa4e1595408a45c01b4b03ad6d7085d83c680a56888ae6a6a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument handler", value=handler, expected_type=type_hints["handler"])
        props = WebSocketLambdaIntegrationProps(
            content_handling=content_handling, timeout=timeout
        )

        jsii.create(self.__class__, self, [id, handler, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IWebSocketRoute_006c2390,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _WebSocketRouteIntegrationConfig_7402c18a:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``WebSocketRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        options = _WebSocketRouteIntegrationBindOptions_4f27dddb(
            route=route, scope=scope
        )

        return typing.cast(_WebSocketRouteIntegrationConfig_7402c18a, jsii.invoke(self, "bind", [options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.WebSocketLambdaIntegrationProps",
    jsii_struct_bases=[],
    name_mapping={"content_handling": "contentHandling", "timeout": "timeout"},
)
class WebSocketLambdaIntegrationProps:
    def __init__(
        self,
        *,
        content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
        timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Props for Lambda type integration for a WebSocket Api.

        :param content_handling: Specifies how to handle response payload content type conversions. Default: - The response payload will be passed through from the integration response to the route response or method response without modification.
        :param timeout: The maximum amount of time an integration will run before it returns without a response. Must be between 50 milliseconds and 29 seconds. Default: Duration.seconds(29)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
            
            web_socket_lambda_integration_props = apigatewayv2_integrations.WebSocketLambdaIntegrationProps(
                content_handling=apigatewayv2.ContentHandling.CONVERT_TO_BINARY,
                timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3043b7d6bcd4be959d4924c0dbbe6ad490dc788f95ab7a014933e7e1b2fefff)
            check_type(argname="argument content_handling", value=content_handling, expected_type=type_hints["content_handling"])
            check_type(argname="argument timeout", value=timeout, expected_type=type_hints["timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if content_handling is not None:
            self._values["content_handling"] = content_handling
        if timeout is not None:
            self._values["timeout"] = timeout

    @builtins.property
    def content_handling(self) -> typing.Optional[_ContentHandling_1512a7da]:
        '''Specifies how to handle response payload content type conversions.

        :default:

        - The response payload will be passed through from the integration response to
        the route response or method response without modification.
        '''
        result = self._values.get("content_handling")
        return typing.cast(typing.Optional[_ContentHandling_1512a7da], result)

    @builtins.property
    def timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The maximum amount of time an integration will run before it returns without a response.

        Must be between 50 milliseconds and 29 seconds.

        :default: Duration.seconds(29)
        '''
        result = self._values.get("timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WebSocketLambdaIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class WebSocketMockIntegration(
    _WebSocketRouteIntegration_bb950e43,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.WebSocketMockIntegration",
):
    '''Mock WebSocket Integration.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
        
        web_socket_mock_integration = apigatewayv2_integrations.WebSocketMockIntegration("id")
    '''

    def __init__(self, id: builtins.str) -> None:
        '''
        :param id: id of the underlying integration construct.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0919a4fac21867e16e13ed094546c03cf261043724396e00ccd357f077081bad)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        jsii.create(self.__class__, self, [id])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        *,
        route: _IWebSocketRoute_006c2390,
        scope: _constructs_77d1e7e8.Construct,
    ) -> _WebSocketRouteIntegrationConfig_7402c18a:
        '''Bind this integration to the route.

        :param route: The route to which this is being bound.
        :param scope: The current scope in which the bind is occurring. If the ``WebSocketRouteIntegration`` being bound creates additional constructs, this will be used as their parent scope.
        '''
        options = _WebSocketRouteIntegrationBindOptions_4f27dddb(
            route=route, scope=scope
        )

        return typing.cast(_WebSocketRouteIntegrationConfig_7402c18a, jsii.invoke(self, "bind", [options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpAlbIntegrationProps",
    jsii_struct_bases=[HttpPrivateIntegrationOptions],
    name_mapping={
        "method": "method",
        "parameter_mapping": "parameterMapping",
        "secure_server_name": "secureServerName",
        "vpc_link": "vpcLink",
    },
)
class HttpAlbIntegrationProps(HttpPrivateIntegrationOptions):
    def __init__(
        self,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''Properties to initialize ``HttpAlbIntegration``.

        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_apigatewayv2_integrations import HttpAlbIntegration
            
            # lb: elbv2.ApplicationLoadBalancer
            
            listener = lb.add_listener("listener", port=80)
            listener.add_targets("target",
                port=80
            )
            
            http_endpoint = apigwv2.HttpApi(self, "HttpProxyPrivateApi",
                default_integration=HttpAlbIntegration("DefaultIntegration", listener,
                    parameter_mapping=apigwv2.ParameterMapping().custom("myKey", "myValue")
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__888094a9f19868567acc15fa299310b8ddeaefe11dd88694812981a0e5f266e7)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
            check_type(argname="argument secure_server_name", value=secure_server_name, expected_type=type_hints["secure_server_name"])
            check_type(argname="argument vpc_link", value=vpc_link, expected_type=type_hints["vpc_link"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping
        if secure_server_name is not None:
            self._values["secure_server_name"] = secure_server_name
        if vpc_link is not None:
            self._values["vpc_link"] = vpc_link

    @builtins.property
    def method(self) -> typing.Optional[_HttpMethod_4c4f3090]:
        '''The HTTP method that must be used to invoke the underlying HTTP proxy.

        :default: HttpMethod.ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[_HttpMethod_4c4f3090], result)

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        :default: undefined requests are sent to the backend unmodified

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    @builtins.property
    def secure_server_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the server name to verified by HTTPS when calling the backend integration.

        :default: undefined private integration traffic will use HTTP protocol

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html
        '''
        result = self._values.get("secure_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_link(self) -> typing.Optional[_IVpcLink_adecf0e2]:
        '''The vpc link to be used for the private integration.

        :default: - a new VpcLink is created
        '''
        result = self._values.get("vpc_link")
        return typing.cast(typing.Optional[_IVpcLink_adecf0e2], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpAlbIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_apigatewayv2_integrations.HttpNlbIntegrationProps",
    jsii_struct_bases=[HttpPrivateIntegrationOptions],
    name_mapping={
        "method": "method",
        "parameter_mapping": "parameterMapping",
        "secure_server_name": "secureServerName",
        "vpc_link": "vpcLink",
    },
)
class HttpNlbIntegrationProps(HttpPrivateIntegrationOptions):
    def __init__(
        self,
        *,
        method: typing.Optional[_HttpMethod_4c4f3090] = None,
        parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
        secure_server_name: typing.Optional[builtins.str] = None,
        vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
    ) -> None:
        '''Properties to initialize ``HttpNlbIntegration``.

        :param method: The HTTP method that must be used to invoke the underlying HTTP proxy. Default: HttpMethod.ANY
        :param parameter_mapping: Specifies how to transform HTTP requests before sending them to the backend. Default: undefined requests are sent to the backend unmodified
        :param secure_server_name: Specifies the server name to verified by HTTPS when calling the backend integration. Default: undefined private integration traffic will use HTTP protocol
        :param vpc_link: The vpc link to be used for the private integration. Default: - a new VpcLink is created

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_apigatewayv2 as apigatewayv2
            from aws_cdk import aws_apigatewayv2_integrations as apigatewayv2_integrations
            
            # parameter_mapping: apigatewayv2.ParameterMapping
            # vpc_link: apigatewayv2.VpcLink
            
            http_nlb_integration_props = apigatewayv2_integrations.HttpNlbIntegrationProps(
                method=apigatewayv2.HttpMethod.ANY,
                parameter_mapping=parameter_mapping,
                secure_server_name="secureServerName",
                vpc_link=vpc_link
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26b3884985e428aa291cb06dd5d372bf9b2520356516ccc3fd63c2d6fc1fe361)
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument parameter_mapping", value=parameter_mapping, expected_type=type_hints["parameter_mapping"])
            check_type(argname="argument secure_server_name", value=secure_server_name, expected_type=type_hints["secure_server_name"])
            check_type(argname="argument vpc_link", value=vpc_link, expected_type=type_hints["vpc_link"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if method is not None:
            self._values["method"] = method
        if parameter_mapping is not None:
            self._values["parameter_mapping"] = parameter_mapping
        if secure_server_name is not None:
            self._values["secure_server_name"] = secure_server_name
        if vpc_link is not None:
            self._values["vpc_link"] = vpc_link

    @builtins.property
    def method(self) -> typing.Optional[_HttpMethod_4c4f3090]:
        '''The HTTP method that must be used to invoke the underlying HTTP proxy.

        :default: HttpMethod.ANY
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional[_HttpMethod_4c4f3090], result)

    @builtins.property
    def parameter_mapping(self) -> typing.Optional[_ParameterMapping_c11a48e0]:
        '''Specifies how to transform HTTP requests before sending them to the backend.

        :default: undefined requests are sent to the backend unmodified

        :see: https://docs.aws.amazon.com/apigateway/latest/developerguide/http-api-parameter-mapping.html
        '''
        result = self._values.get("parameter_mapping")
        return typing.cast(typing.Optional[_ParameterMapping_c11a48e0], result)

    @builtins.property
    def secure_server_name(self) -> typing.Optional[builtins.str]:
        '''Specifies the server name to verified by HTTPS when calling the backend integration.

        :default: undefined private integration traffic will use HTTP protocol

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-apigatewayv2-integration-tlsconfig.html
        '''
        result = self._values.get("secure_server_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_link(self) -> typing.Optional[_IVpcLink_adecf0e2]:
        '''The vpc link to be used for the private integration.

        :default: - a new VpcLink is created
        '''
        result = self._values.get("vpc_link")
        return typing.cast(typing.Optional[_IVpcLink_adecf0e2], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpNlbIntegrationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HttpAlbIntegration",
    "HttpAlbIntegrationProps",
    "HttpLambdaIntegration",
    "HttpLambdaIntegrationProps",
    "HttpNlbIntegration",
    "HttpNlbIntegrationProps",
    "HttpPrivateIntegrationOptions",
    "HttpServiceDiscoveryIntegration",
    "HttpServiceDiscoveryIntegrationProps",
    "HttpStepFunctionsIntegration",
    "HttpStepFunctionsIntegrationProps",
    "HttpUrlIntegration",
    "HttpUrlIntegrationProps",
    "WebSocketAwsIntegration",
    "WebSocketAwsIntegrationProps",
    "WebSocketLambdaIntegration",
    "WebSocketLambdaIntegrationProps",
    "WebSocketMockIntegration",
]

publication.publish()

def _typecheckingstub__928f282b08310c18e1704595722c48f29856eea7d0afc8e0dd89d67e61a77820(
    id: builtins.str,
    listener: _IApplicationListener_60f2beb6,
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddd81275967dd8f82fea61a7accd8241f873539fe596998c66af3c580e913284(
    value: _HttpConnectionType_02a8b6fb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49d2707c331ffacddcce15a9f8462f5b4bd86acafca4f99ffac86d61fdd968c5(
    value: _HttpMethod_4c4f3090,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68d6f772e2a89442556f1760d95c537293e8868e69f39350b976830ea7c5d7c8(
    value: _HttpIntegrationType_aee0d440,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6120aff86732fb3507f4b0835b6bc561a686dcb25788f79481dc42c78203b26(
    value: _PayloadFormatVersion_a469cb03,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__186fcdf4e12ad29dbad06f4ae566e815dd0e4855b4b9ffd6626f945f2a4aee19(
    id: builtins.str,
    handler: _IFunction_6adb0ab8,
    *,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    payload_format_version: typing.Optional[_PayloadFormatVersion_a469cb03] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7494501e4bf220385c831472b8042a561df79a565c497e77d41cfc10427bce41(
    *,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    payload_format_version: typing.Optional[_PayloadFormatVersion_a469cb03] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__543e48e97b53816262605885854d56b7f2c624e9fe59f7e60eadcde801acaebd(
    id: builtins.str,
    listener: _INetworkListener_fccca3bd,
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d360e4b817e6fc6c8ae4e1350d9dd6b3d69b40c54401465c6ef888953f765e38(
    value: _HttpConnectionType_02a8b6fb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c789ab75d5a6290c76fe8fce0b824cd0926bb50f6f9fb91ff77ef01e82a1ea0(
    value: _HttpMethod_4c4f3090,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__585857799e486703df2825ecce003717b9e731a7928c8409a6da811435c79165(
    value: _HttpIntegrationType_aee0d440,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__36f10890866a2476ef7a837c18a7bab079976e4adf47e736ccebe3fc7ec980ca(
    value: _PayloadFormatVersion_a469cb03,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d60e74e57400fa0f9757a69ecb53197543ad6fd054f8168eaa56d7cd010107b5(
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc876ae5ee3ca1141486563e7214d682fb6d2e3b3b1ab6b4f91e525d7a19b53e(
    id: builtins.str,
    service: _IService_46860ae1,
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88fa11bc73bf44288cb7467c39d6aa21cc34611adb58ae52dbcb42fe2150a266(
    value: _HttpConnectionType_02a8b6fb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3cc3ee501484e0e7058df9083bcfc3e410c2de2357a283e797038514e45bae8e(
    value: _HttpMethod_4c4f3090,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5909d37808307699be7a07730689164f1e138383252eae1d7c68420302f2e9c4(
    value: _HttpIntegrationType_aee0d440,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2db70ce1255fd6ff4a3b0a88a1c0a0096c5eb165bf1ce3544bee82d10bcc54d7(
    value: _PayloadFormatVersion_a469cb03,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bbb857ee24522818d504a3830c65b95bbc66b9ef70c67fa5b85fbdca1aaf1c1(
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76518171338936bd0fbff4054b2b72b876355e21b6eef931d4dd4f111fc7889f(
    id: builtins.str,
    *,
    state_machine: _StateMachine_a256d24f,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    subtype: typing.Optional[_HttpIntegrationSubtype_beb63b59] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7072515a6bcc56ecf05d39b9b84f7dde9de04e9c2caf9ada206b863db8625ed(
    *,
    state_machine: _StateMachine_a256d24f,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    subtype: typing.Optional[_HttpIntegrationSubtype_beb63b59] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39ce64d79e6c4249c8c60321022b7721149966e379b0f947f602cb248aee9bce(
    id: builtins.str,
    url: builtins.str,
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__abe29aa89dc1da944745a812d1d5e87dd81ab57867504a928a129c8b904c99da(
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bba00d2a284a155db9e940bdf51118b0715f0312e8109e916f7848b20023815(
    id: builtins.str,
    *,
    integration_method: builtins.str,
    integration_uri: builtins.str,
    content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
    credentials_role: typing.Optional[_IRole_235f5d8e] = None,
    passthrough_behavior: typing.Optional[_PassthroughBehavior_379b8a9e] = None,
    request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aa585be6945644a75e60414b518cacf76637190e70170ea912e9826651e3e5ea(
    *,
    integration_method: builtins.str,
    integration_uri: builtins.str,
    content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
    credentials_role: typing.Optional[_IRole_235f5d8e] = None,
    passthrough_behavior: typing.Optional[_PassthroughBehavior_379b8a9e] = None,
    request_parameters: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    request_templates: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    template_selection_expression: typing.Optional[builtins.str] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__990acb5e6eea396fa4e1595408a45c01b4b03ad6d7085d83c680a56888ae6a6a(
    id: builtins.str,
    handler: _IFunction_6adb0ab8,
    *,
    content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3043b7d6bcd4be959d4924c0dbbe6ad490dc788f95ab7a014933e7e1b2fefff(
    *,
    content_handling: typing.Optional[_ContentHandling_1512a7da] = None,
    timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0919a4fac21867e16e13ed094546c03cf261043724396e00ccd357f077081bad(
    id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__888094a9f19868567acc15fa299310b8ddeaefe11dd88694812981a0e5f266e7(
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26b3884985e428aa291cb06dd5d372bf9b2520356516ccc3fd63c2d6fc1fe361(
    *,
    method: typing.Optional[_HttpMethod_4c4f3090] = None,
    parameter_mapping: typing.Optional[_ParameterMapping_c11a48e0] = None,
    secure_server_name: typing.Optional[builtins.str] = None,
    vpc_link: typing.Optional[_IVpcLink_adecf0e2] = None,
) -> None:
    """Type checking stubs"""
    pass
