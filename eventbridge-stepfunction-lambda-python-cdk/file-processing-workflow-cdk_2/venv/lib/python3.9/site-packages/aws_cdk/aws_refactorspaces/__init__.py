'''
# AWS::RefactorSpaces Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_refactorspaces as refactorspaces
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for RefactorSpaces construct libraries](https://constructs.dev/search?q=refactorspaces)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::RefactorSpaces resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RefactorSpaces.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::RefactorSpaces](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_RefactorSpaces.html).

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
class CfnApplication(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnApplication",
):
    '''Creates an AWS Migration Hub Refactor Spaces application.

    The account that owns the environment also owns the applications created inside the environment, regardless of the account that creates the application. Refactor Spaces provisions an Amazon API Gateway , API Gateway VPC link, and Network Load Balancer for the application proxy inside your account.

    In environments created with a `CreateEnvironment:NetworkFabricType <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType>`_ of ``NONE`` you need to configure `VPC to VPC connectivity <https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html>`_ between your service VPC and the application proxy VPC to route traffic through the application proxy to a service with a private URL endpoint. For more information, see `Create an application <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-application.html>`_ in the *Refactor Spaces User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_application = refactorspaces.CfnApplication(self, "MyCfnApplication",
            environment_identifier="environmentIdentifier",
            name="name",
            proxy_type="proxyType",
            vpc_id="vpcId",
        
            # the properties below are optional
            api_gateway_proxy=refactorspaces.CfnApplication.ApiGatewayProxyInputProperty(
                endpoint_type="endpointType",
                stage_name="stageName"
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
        environment_identifier: builtins.str,
        name: builtins.str,
        proxy_type: builtins.str,
        vpc_id: builtins.str,
        api_gateway_proxy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnApplication.ApiGatewayProxyInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param environment_identifier: The unique identifier of the environment.
        :param name: The name of the application.
        :param proxy_type: The proxy type of the proxy created within the application.
        :param vpc_id: The ID of the virtual private cloud (VPC).
        :param api_gateway_proxy: The endpoint URL of the Amazon API Gateway proxy.
        :param tags: The tags assigned to the application.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__efe09dd43c3fb974d0c5c81b4c42f5319245347d1ba0af51a0027fe77e6aad92)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnApplicationProps(
            environment_identifier=environment_identifier,
            name=name,
            proxy_type=proxy_type,
            vpc_id=vpc_id,
            api_gateway_proxy=api_gateway_proxy,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7011b5f5302cb44f6e8327da1d8ab609b5b090012feee8d5dabc192d2d37d59)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c7b07ea069ba96164c117171200d67b8576bba98226e2c28037fb29d5532de04)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrApiGatewayId")
    def attr_api_gateway_id(self) -> builtins.str:
        '''The resource ID of the API Gateway for the proxy.

        :cloudformationAttribute: ApiGatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApiGatewayId"))

    @builtins.property
    @jsii.member(jsii_name="attrApplicationIdentifier")
    def attr_application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :cloudformationAttribute: ApplicationIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrApplicationIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the application.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNlbArn")
    def attr_nlb_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Network Load Balancer .

        :cloudformationAttribute: NlbArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNlbArn"))

    @builtins.property
    @jsii.member(jsii_name="attrNlbName")
    def attr_nlb_name(self) -> builtins.str:
        '''The name of the Network Load Balancer configured by the API Gateway proxy.

        :cloudformationAttribute: NlbName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrNlbName"))

    @builtins.property
    @jsii.member(jsii_name="attrProxyUrl")
    def attr_proxy_url(self) -> builtins.str:
        '''The endpoint URL of the Amazon API Gateway proxy.

        :cloudformationAttribute: ProxyUrl
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProxyUrl"))

    @builtins.property
    @jsii.member(jsii_name="attrStageName")
    def attr_stage_name(self) -> builtins.str:
        '''The name of the API Gateway stage.

        The name defaults to ``prod`` .

        :cloudformationAttribute: StageName
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStageName"))

    @builtins.property
    @jsii.member(jsii_name="attrVpcLinkId")
    def attr_vpc_link_id(self) -> builtins.str:
        '''The ``VpcLink`` ID of the API Gateway proxy.

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
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__551b88889ac6d0f58295880113eee3f55c2efd4355df92b3f9fccd2c956c9fca)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea6a7a37a56ee75ee952f2138af2c8ba8401cf74adeebf8a6922eee0cb947a31)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="proxyType")
    def proxy_type(self) -> builtins.str:
        '''The proxy type of the proxy created within the application.'''
        return typing.cast(builtins.str, jsii.get(self, "proxyType"))

    @proxy_type.setter
    def proxy_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad9a18d39ac5a21164a646b9a15b300ea6334fa64dfb5bfd0570b989b3ef8e85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proxyType", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> builtins.str:
        '''The ID of the virtual private cloud (VPC).'''
        return typing.cast(builtins.str, jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ef1d0faba679fd338f3cd08e2e7cdf05975edb143dd0e601f14bd72625ad717)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @builtins.property
    @jsii.member(jsii_name="apiGatewayProxy")
    def api_gateway_proxy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApiGatewayProxyInputProperty"]]:
        '''The endpoint URL of the Amazon API Gateway proxy.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApiGatewayProxyInputProperty"]], jsii.get(self, "apiGatewayProxy"))

    @api_gateway_proxy.setter
    def api_gateway_proxy(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnApplication.ApiGatewayProxyInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__390d5bc749674d9a5d49b0922c18346f5f99422a80c7f57838dc984bbd83d042)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "apiGatewayProxy", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the application.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__18ae2f9cbdac00e453fc30ac71e6f9520bc5a36f13a98e2f67326fd8969c8d23)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnApplication.ApiGatewayProxyInputProperty",
        jsii_struct_bases=[],
        name_mapping={"endpoint_type": "endpointType", "stage_name": "stageName"},
    )
    class ApiGatewayProxyInputProperty:
        def __init__(
            self,
            *,
            endpoint_type: typing.Optional[builtins.str] = None,
            stage_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A wrapper object holding the Amazon API Gateway endpoint input.

            :param endpoint_type: The type of endpoint to use for the API Gateway proxy. If no value is specified in the request, the value is set to ``REGIONAL`` by default. If the value is set to ``PRIVATE`` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud ( Amazon VPC ) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint ( AWS PrivateLink ) availability, see `Access Refactor Spaces using an interface endpoint ( AWS PrivateLink ) <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html>`_ .
            :param stage_name: The name of the API Gateway stage. The name defaults to ``prod`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                api_gateway_proxy_input_property = refactorspaces.CfnApplication.ApiGatewayProxyInputProperty(
                    endpoint_type="endpointType",
                    stage_name="stageName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bf716c9691040b260b80d99cde314be1acfd63ad22719816a1f0749c8b5fa383)
                check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
                check_type(argname="argument stage_name", value=stage_name, expected_type=type_hints["stage_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if endpoint_type is not None:
                self._values["endpoint_type"] = endpoint_type
            if stage_name is not None:
                self._values["stage_name"] = stage_name

        @builtins.property
        def endpoint_type(self) -> typing.Optional[builtins.str]:
            '''The type of endpoint to use for the API Gateway proxy.

            If no value is specified in the request, the value is set to ``REGIONAL`` by default.

            If the value is set to ``PRIVATE`` in the request, this creates a private API endpoint that is isolated from the public internet. The private endpoint can only be accessed by using Amazon Virtual Private Cloud ( Amazon VPC ) interface endpoints for the Amazon API Gateway that has been granted access. For more information about creating a private connection with Refactor Spaces and interface endpoint ( AWS PrivateLink ) availability, see `Access Refactor Spaces using an interface endpoint ( AWS PrivateLink ) <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/vpc-interface-endpoints.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html#cfn-refactorspaces-application-apigatewayproxyinput-endpointtype
            '''
            result = self._values.get("endpoint_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def stage_name(self) -> typing.Optional[builtins.str]:
            '''The name of the API Gateway stage.

            The name defaults to ``prod`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-application-apigatewayproxyinput.html#cfn-refactorspaces-application-apigatewayproxyinput-stagename
            '''
            result = self._values.get("stage_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApiGatewayProxyInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnApplicationProps",
    jsii_struct_bases=[],
    name_mapping={
        "environment_identifier": "environmentIdentifier",
        "name": "name",
        "proxy_type": "proxyType",
        "vpc_id": "vpcId",
        "api_gateway_proxy": "apiGatewayProxy",
        "tags": "tags",
    },
)
class CfnApplicationProps:
    def __init__(
        self,
        *,
        environment_identifier: builtins.str,
        name: builtins.str,
        proxy_type: builtins.str,
        vpc_id: builtins.str,
        api_gateway_proxy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApiGatewayProxyInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnApplication``.

        :param environment_identifier: The unique identifier of the environment.
        :param name: The name of the application.
        :param proxy_type: The proxy type of the proxy created within the application.
        :param vpc_id: The ID of the virtual private cloud (VPC).
        :param api_gateway_proxy: The endpoint URL of the Amazon API Gateway proxy.
        :param tags: The tags assigned to the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_application_props = refactorspaces.CfnApplicationProps(
                environment_identifier="environmentIdentifier",
                name="name",
                proxy_type="proxyType",
                vpc_id="vpcId",
            
                # the properties below are optional
                api_gateway_proxy=refactorspaces.CfnApplication.ApiGatewayProxyInputProperty(
                    endpoint_type="endpointType",
                    stage_name="stageName"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5974ddb2dc67ffb28c95d9f66ee42fa70224d0f4aa23981df037681d6c4fdf1)
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument proxy_type", value=proxy_type, expected_type=type_hints["proxy_type"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
            check_type(argname="argument api_gateway_proxy", value=api_gateway_proxy, expected_type=type_hints["api_gateway_proxy"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "environment_identifier": environment_identifier,
            "name": name,
            "proxy_type": proxy_type,
            "vpc_id": vpc_id,
        }
        if api_gateway_proxy is not None:
            self._values["api_gateway_proxy"] = api_gateway_proxy
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def proxy_type(self) -> builtins.str:
        '''The proxy type of the proxy created within the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-proxytype
        '''
        result = self._values.get("proxy_type")
        assert result is not None, "Required property 'proxy_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def vpc_id(self) -> builtins.str:
        '''The ID of the virtual private cloud (VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-vpcid
        '''
        result = self._values.get("vpc_id")
        assert result is not None, "Required property 'vpc_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def api_gateway_proxy(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApiGatewayProxyInputProperty]]:
        '''The endpoint URL of the Amazon API Gateway proxy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-apigatewayproxy
        '''
        result = self._values.get("api_gateway_proxy")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApiGatewayProxyInputProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-application.html#cfn-refactorspaces-application-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnApplicationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnEnvironment(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnEnvironment",
):
    '''Creates an AWS Migration Hub Refactor Spaces environment.

    The caller owns the environment resource, and all Refactor Spaces applications, services, and routes created within the environment. They are referred to as the *environment owner* . The environment owner has cross-account visibility and control of Refactor Spaces resources that are added to the environment by other accounts that the environment is shared with.

    When creating an environment with a `CreateEnvironment:NetworkFabricType <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType>`_ of ``TRANSIT_GATEWAY`` , Refactor Spaces provisions a transit gateway to enable services in VPCs to communicate directly across accounts. If `CreateEnvironment:NetworkFabricType <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType>`_ is ``NONE`` , Refactor Spaces does not create a transit gateway and you must use your network infrastructure to route traffic to services with private URL endpoints.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_environment = refactorspaces.CfnEnvironment(self, "MyCfnEnvironment",
            name="name",
            network_fabric_type="networkFabricType",
        
            # the properties below are optional
            description="description",
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
        network_fabric_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the environment.
        :param network_fabric_type: The network fabric type of the environment.
        :param description: A description of the environment.
        :param tags: The tags assigned to the environment.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a536c3debb5766a7d9c84ccebc269b62327808a31254e1265a594b329b64555)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEnvironmentProps(
            name=name,
            network_fabric_type=network_fabric_type,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee147fff7adf7bdc8ae158201b2d10a5109e1a28aa52431dbc158d7e263fcbde)
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
            type_hints = typing.get_type_hints(_typecheckingstub__138e64a98402d3a98928b3e46ccae4a4d0dea8d23b6abe8a4b1ebce5abad37ef)
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
        '''The Amazon Resource Name (ARN) of the environment.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrEnvironmentIdentifier")
    def attr_environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :cloudformationAttribute: EnvironmentIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEnvironmentIdentifier"))

    @builtins.property
    @jsii.member(jsii_name="attrTransitGatewayId")
    def attr_transit_gateway_id(self) -> builtins.str:
        '''The ID of the AWS Transit Gateway set up by the environment.

        :cloudformationAttribute: TransitGatewayId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrTransitGatewayId"))

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
        '''The name of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a1dd279f966e1ba560574858b8d147fa089efd23806e011056a3ab45fef84b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkFabricType")
    def network_fabric_type(self) -> builtins.str:
        '''The network fabric type of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "networkFabricType"))

    @network_fabric_type.setter
    def network_fabric_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7218caf601ef511e6c489e41a01233a12b0895a28a26b826e4c2c36d324becd3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkFabricType", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__271815f6b6299ae2b9ca94d64e6b3e5f6de740f2212fc74c92c95cfbbb1f7c99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the environment.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49a8b10d6ea6b81c02ef39ee701909acec2186e1d9db3d4d4ad46420728b6698)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnEnvironmentProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "network_fabric_type": "networkFabricType",
        "description": "description",
        "tags": "tags",
    },
)
class CfnEnvironmentProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        network_fabric_type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEnvironment``.

        :param name: The name of the environment.
        :param network_fabric_type: The network fabric type of the environment.
        :param description: A description of the environment.
        :param tags: The tags assigned to the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_environment_props = refactorspaces.CfnEnvironmentProps(
                name="name",
                network_fabric_type="networkFabricType",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc993226fa6d6cb56a25f6ae5fb96e6ea288e1bcd336e16e685ce08129bd9ae6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_fabric_type", value=network_fabric_type, expected_type=type_hints["network_fabric_type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "network_fabric_type": network_fabric_type,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_fabric_type(self) -> builtins.str:
        '''The network fabric type of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-networkfabrictype
        '''
        result = self._values.get("network_fabric_type")
        assert result is not None, "Required property 'network_fabric_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-environment.html#cfn-refactorspaces-environment-tags
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


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnRoute(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRoute",
):
    '''Creates an AWS Migration Hub Refactor Spaces route.

    The account owner of the service resource is always the environment owner, regardless of which account creates the route. Routes target a service in the application. If an application does not have any routes, then the first route must be created as a ``DEFAULT`` ``RouteType`` .

    When created, the default route defaults to an active state so state is not a required input. However, like all other state values the state of the default route can be updated after creation, but only when all other routes are also inactive. Conversely, no route can be active without the default route also being active.
    .. epigraph::

       In the ``AWS::RefactorSpaces::Route`` resource, you can only update the ``ActivationState`` property, which resides under the ``UriPathRoute`` and ``DefaultRoute`` properties. All other properties associated with the ``AWS::RefactorSpaces::Route`` cannot be updated, even though the property description might indicate otherwise. Updating all other properties will result in the replacement of Route.

    When you create a route, Refactor Spaces configures the Amazon API Gateway to send traffic to the target service as follows:

    - *URL Endpoints*

    If the service has a URL endpoint, and the endpoint resolves to a private IP address, Refactor Spaces routes traffic using the API Gateway VPC link. If a service endpoint resolves to a public IP address, Refactor Spaces routes traffic over the public internet. Services can have HTTP or HTTPS URL endpoints. For HTTPS URLs, publicly-signed certificates are supported. Private Certificate Authorities (CAs) are permitted only if the CA's domain is also publicly resolvable.

    Refactor Spaces automatically resolves the public Domain Name System (DNS) names that are set in ``CreateService:UrlEndpoint`` when you create a service. The DNS names resolve when the DNS time-to-live (TTL) expires, or every 60 seconds for TTLs less than 60 seconds. This periodic DNS resolution ensures that the route configuration remains up-to-date.

    *One-time health check*

    A one-time health check is performed on the service when either the route is updated from inactive to active, or when it is created with an active state. If the health check fails, the route transitions the route state to ``FAILED`` , an error code of ``SERVICE_ENDPOINT_HEALTH_CHECK_FAILURE`` is provided, and no traffic is sent to the service.

    For private URLs, a target group is created on the Network Load Balancer and the load balancer target group runs default target health checks. By default, the health check is run against the service endpoint URL. Optionally, the health check can be performed against a different protocol, port, and/or path using the `CreateService:UrlEndpoint <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateService.html#migrationhubrefactorspaces-CreateService-request-UrlEndpoint>`_ parameter. All other health check settings for the load balancer use the default values described in the `Health checks for your target groups <https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html>`_ in the *Elastic Load Balancing guide* . The health check is considered successful if at least one target within the target group transitions to a healthy state.

    - *AWS Lambda function endpoints*

    If the service has an AWS Lambda function endpoint, then Refactor Spaces configures the Lambda function's resource policy to allow the application's API Gateway to invoke the function.

    The Lambda function state is checked. If the function is not active, the function configuration is updated so that Lambda resources are provisioned. If the Lambda state is ``Failed`` , then the route creation fails. For more information, see the `GetFunctionConfiguration's State response parameter <https://docs.aws.amazon.com/lambda/latest/dg/API_GetFunctionConfiguration.html#SSS-GetFunctionConfiguration-response-State>`_ in the *AWS Lambda Developer Guide* .

    A check is performed to determine that a Lambda function with the specified ARN exists. If it does not exist, the health check fails. For public URLs, a connection is opened to the public endpoint. If the URL is not reachable, the health check fails.

    *Environments without a network bridge*

    When you create environments without a network bridge ( `CreateEnvironment:NetworkFabricType <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/APIReference/API_CreateEnvironment.html#migrationhubrefactorspaces-CreateEnvironment-request-NetworkFabricType>`_ is ``NONE)`` and you use your own networking infrastructure, you need to configure `VPC to VPC connectivity <https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/amazon-vpc-to-amazon-vpc-connectivity-options.html>`_ between your network and the application proxy VPC. Route creation from the application proxy to service endpoints will fail if your network is not configured to connect to the application proxy VPC. For more information, see `Create a route <https://docs.aws.amazon.com/migrationhub-refactor-spaces/latest/userguide/getting-started-create-role.html>`_ in the *Refactor Spaces User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_route = refactorspaces.CfnRoute(self, "MyCfnRoute",
            application_identifier="applicationIdentifier",
            environment_identifier="environmentIdentifier",
            route_type="routeType",
            service_identifier="serviceIdentifier",
        
            # the properties below are optional
            default_route=refactorspaces.CfnRoute.DefaultRouteInputProperty(
                activation_state="activationState"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            uri_path_route=refactorspaces.CfnRoute.UriPathRouteInputProperty(
                activation_state="activationState",
        
                # the properties below are optional
                append_source_path=False,
                include_child_paths=False,
                methods=["methods"],
                source_path="sourcePath"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        route_type: builtins.str,
        service_identifier: builtins.str,
        default_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoute.DefaultRouteInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uri_path_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRoute.UriPathRouteInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_identifier: The unique identifier of the application.
        :param environment_identifier: The unique identifier of the environment.
        :param route_type: The route type of the route.
        :param service_identifier: The unique identifier of the service.
        :param default_route: Configuration for the default route type.
        :param tags: The tags assigned to the route.
        :param uri_path_route: The configuration for the URI path route type.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5ef0962b163b395fd9c904416cc27c1511b7a89295feb97b9cedbae2ffcc49a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRouteProps(
            application_identifier=application_identifier,
            environment_identifier=environment_identifier,
            route_type=route_type,
            service_identifier=service_identifier,
            default_route=default_route,
            tags=tags,
            uri_path_route=uri_path_route,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__60184063db47ddac5005c921e627702643821a736e07d8b748466fcebc033f42)
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
            type_hints = typing.get_type_hints(_typecheckingstub__6284677163b0dcbf6c699e94d88765e9b298f9ed01772681e946311408ae6213)
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
        '''The Amazon Resource Name (ARN) of the route.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrPathResourceToId")
    def attr_path_resource_to_id(self) -> builtins.str:
        '''A mapping of Amazon API Gateway path resources to resource IDs.

        :cloudformationAttribute: PathResourceToId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrPathResourceToId"))

    @builtins.property
    @jsii.member(jsii_name="attrRouteIdentifier")
    def attr_route_identifier(self) -> builtins.str:
        '''The unique identifier of the route.

        :cloudformationAttribute: RouteIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRouteIdentifier"))

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
    @jsii.member(jsii_name="applicationIdentifier")
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationIdentifier"))

    @application_identifier.setter
    def application_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2d376946bad32a682cda77d07b2b073fc17cadaed1fc43223dffcfa5c37412f7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1dfd28d40096cf9941517ac9d2d037635b77d983d8f46a22cfed6d4627d4cd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="routeType")
    def route_type(self) -> builtins.str:
        '''The route type of the route.'''
        return typing.cast(builtins.str, jsii.get(self, "routeType"))

    @route_type.setter
    def route_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__946936a18776032253422bf6f3cdec83d06e049a9564dd0c7786c8c37a23e190)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "routeType", value)

    @builtins.property
    @jsii.member(jsii_name="serviceIdentifier")
    def service_identifier(self) -> builtins.str:
        '''The unique identifier of the service.'''
        return typing.cast(builtins.str, jsii.get(self, "serviceIdentifier"))

    @service_identifier.setter
    def service_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7759c2cbb7a97913b9c2fa8aa25c156f897dad50e14e10650aa2acd1c08b3e8d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "serviceIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="defaultRoute")
    def default_route(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoute.DefaultRouteInputProperty"]]:
        '''Configuration for the default route type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoute.DefaultRouteInputProperty"]], jsii.get(self, "defaultRoute"))

    @default_route.setter
    def default_route(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoute.DefaultRouteInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7daaefa65bcec7258677987651fbf35fbcc04f2bae9397a83e03cd4f41cb202a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "defaultRoute", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the route.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__883c592efbf4191da735efaffbd65e0924e0209da44250420beef388acb08935)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="uriPathRoute")
    def uri_path_route(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoute.UriPathRouteInputProperty"]]:
        '''The configuration for the URI path route type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoute.UriPathRouteInputProperty"]], jsii.get(self, "uriPathRoute"))

    @uri_path_route.setter
    def uri_path_route(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRoute.UriPathRouteInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75056f6caa086eeec89a3d9d03525f3ab78e1c72b12ce9818295f9f36a109ee1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "uriPathRoute", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRoute.DefaultRouteInputProperty",
        jsii_struct_bases=[],
        name_mapping={"activation_state": "activationState"},
    )
    class DefaultRouteInputProperty:
        def __init__(self, *, activation_state: builtins.str) -> None:
            '''The configuration for the default route type.

            :param activation_state: If set to ``ACTIVE`` , traffic is forwarded to this route’s service after the route is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                default_route_input_property = refactorspaces.CfnRoute.DefaultRouteInputProperty(
                    activation_state="activationState"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7ea6aa520044cedf5d9d051fb9eb89987341d453afc149037ea9c10707849676)
                check_type(argname="argument activation_state", value=activation_state, expected_type=type_hints["activation_state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "activation_state": activation_state,
            }

        @builtins.property
        def activation_state(self) -> builtins.str:
            '''If set to ``ACTIVE`` , traffic is forwarded to this route’s service after the route is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-defaultrouteinput.html#cfn-refactorspaces-route-defaultrouteinput-activationstate
            '''
            result = self._values.get("activation_state")
            assert result is not None, "Required property 'activation_state' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefaultRouteInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRoute.UriPathRouteInputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "activation_state": "activationState",
            "append_source_path": "appendSourcePath",
            "include_child_paths": "includeChildPaths",
            "methods": "methods",
            "source_path": "sourcePath",
        },
    )
    class UriPathRouteInputProperty:
        def __init__(
            self,
            *,
            activation_state: builtins.str,
            append_source_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_child_paths: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            methods: typing.Optional[typing.Sequence[builtins.str]] = None,
            source_path: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the URI path route type.

            :param activation_state: If set to ``ACTIVE`` , traffic is forwarded to this route’s service after the route is created.
            :param append_source_path: If set to ``true`` , this option appends the source path to the service URL endpoint.
            :param include_child_paths: Indicates whether to match all subpaths of the given source path. If this value is ``false`` , requests must match the source path exactly before they are forwarded to this route's service.
            :param methods: A list of HTTP methods to match. An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.
            :param source_path: This is the path that Refactor Spaces uses to match traffic. Paths must start with ``/`` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                uri_path_route_input_property = refactorspaces.CfnRoute.UriPathRouteInputProperty(
                    activation_state="activationState",
                
                    # the properties below are optional
                    append_source_path=False,
                    include_child_paths=False,
                    methods=["methods"],
                    source_path="sourcePath"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__37bbcddaf33ba9305fa2a3feb1d85f7802a55919b9491e2ea4b5663e05573965)
                check_type(argname="argument activation_state", value=activation_state, expected_type=type_hints["activation_state"])
                check_type(argname="argument append_source_path", value=append_source_path, expected_type=type_hints["append_source_path"])
                check_type(argname="argument include_child_paths", value=include_child_paths, expected_type=type_hints["include_child_paths"])
                check_type(argname="argument methods", value=methods, expected_type=type_hints["methods"])
                check_type(argname="argument source_path", value=source_path, expected_type=type_hints["source_path"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "activation_state": activation_state,
            }
            if append_source_path is not None:
                self._values["append_source_path"] = append_source_path
            if include_child_paths is not None:
                self._values["include_child_paths"] = include_child_paths
            if methods is not None:
                self._values["methods"] = methods
            if source_path is not None:
                self._values["source_path"] = source_path

        @builtins.property
        def activation_state(self) -> builtins.str:
            '''If set to ``ACTIVE`` , traffic is forwarded to this route’s service after the route is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-activationstate
            '''
            result = self._values.get("activation_state")
            assert result is not None, "Required property 'activation_state' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def append_source_path(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If set to ``true`` , this option appends the source path to the service URL endpoint.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-appendsourcepath
            '''
            result = self._values.get("append_source_path")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_child_paths(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Indicates whether to match all subpaths of the given source path.

            If this value is ``false`` , requests must match the source path exactly before they are forwarded to this route's service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-includechildpaths
            '''
            result = self._values.get("include_child_paths")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def methods(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of HTTP methods to match.

            An empty list matches all values. If a method is present, only HTTP requests using that method are forwarded to this route’s service.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-methods
            '''
            result = self._values.get("methods")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def source_path(self) -> typing.Optional[builtins.str]:
            '''This is the path that Refactor Spaces uses to match traffic.

            Paths must start with ``/`` and are relative to the base of the application. To use path parameters in the source path, add a variable in curly braces. For example, the resource path {user} represents a path parameter called 'user'.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-route-uripathrouteinput.html#cfn-refactorspaces-route-uripathrouteinput-sourcepath
            '''
            result = self._values.get("source_path")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UriPathRouteInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnRouteProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "environment_identifier": "environmentIdentifier",
        "route_type": "routeType",
        "service_identifier": "serviceIdentifier",
        "default_route": "defaultRoute",
        "tags": "tags",
        "uri_path_route": "uriPathRoute",
    },
)
class CfnRouteProps:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        environment_identifier: builtins.str,
        route_type: builtins.str,
        service_identifier: builtins.str,
        default_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoute.DefaultRouteInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        uri_path_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoute.UriPathRouteInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRoute``.

        :param application_identifier: The unique identifier of the application.
        :param environment_identifier: The unique identifier of the environment.
        :param route_type: The route type of the route.
        :param service_identifier: The unique identifier of the service.
        :param default_route: Configuration for the default route type.
        :param tags: The tags assigned to the route.
        :param uri_path_route: The configuration for the URI path route type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_route_props = refactorspaces.CfnRouteProps(
                application_identifier="applicationIdentifier",
                environment_identifier="environmentIdentifier",
                route_type="routeType",
                service_identifier="serviceIdentifier",
            
                # the properties below are optional
                default_route=refactorspaces.CfnRoute.DefaultRouteInputProperty(
                    activation_state="activationState"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                uri_path_route=refactorspaces.CfnRoute.UriPathRouteInputProperty(
                    activation_state="activationState",
            
                    # the properties below are optional
                    append_source_path=False,
                    include_child_paths=False,
                    methods=["methods"],
                    source_path="sourcePath"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58f3ed916c6586128a311abab14b0fec6e77c0d76bd30bce92f9ecaf0e766f82)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument route_type", value=route_type, expected_type=type_hints["route_type"])
            check_type(argname="argument service_identifier", value=service_identifier, expected_type=type_hints["service_identifier"])
            check_type(argname="argument default_route", value=default_route, expected_type=type_hints["default_route"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument uri_path_route", value=uri_path_route, expected_type=type_hints["uri_path_route"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_identifier": application_identifier,
            "environment_identifier": environment_identifier,
            "route_type": route_type,
            "service_identifier": service_identifier,
        }
        if default_route is not None:
            self._values["default_route"] = default_route
        if tags is not None:
            self._values["tags"] = tags
        if uri_path_route is not None:
            self._values["uri_path_route"] = uri_path_route

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-applicationidentifier
        '''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def route_type(self) -> builtins.str:
        '''The route type of the route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-routetype
        '''
        result = self._values.get("route_type")
        assert result is not None, "Required property 'route_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def service_identifier(self) -> builtins.str:
        '''The unique identifier of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-serviceidentifier
        '''
        result = self._values.get("service_identifier")
        assert result is not None, "Required property 'service_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def default_route(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoute.DefaultRouteInputProperty]]:
        '''Configuration for the default route type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-defaultroute
        '''
        result = self._values.get("default_route")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoute.DefaultRouteInputProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the route.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def uri_path_route(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoute.UriPathRouteInputProperty]]:
        '''The configuration for the URI path route type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-route.html#cfn-refactorspaces-route-uripathroute
        '''
        result = self._values.get("uri_path_route")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoute.UriPathRouteInputProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRouteProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnService(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnService",
):
    '''Creates an AWS Migration Hub Refactor Spaces service.

    The account owner of the service is always the environment owner, regardless of which account in the environment creates the service. Services have either a URL endpoint in a virtual private cloud (VPC), or a Lambda function endpoint.
    .. epigraph::

       If an AWS resource is launched in a service VPC, and you want it to be accessible to all of an environment’s services with VPCs and routes, apply the ``RefactorSpacesSecurityGroup`` to the resource. Alternatively, to add more cross-account constraints, apply your own security group.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_refactorspaces as refactorspaces
        
        cfn_service = refactorspaces.CfnService(self, "MyCfnService",
            application_identifier="applicationIdentifier",
            endpoint_type="endpointType",
            environment_identifier="environmentIdentifier",
            name="name",
        
            # the properties below are optional
            description="description",
            lambda_endpoint=refactorspaces.CfnService.LambdaEndpointInputProperty(
                arn="arn"
            ),
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            url_endpoint=refactorspaces.CfnService.UrlEndpointInputProperty(
                url="url",
        
                # the properties below are optional
                health_url="healthUrl"
            ),
            vpc_id="vpcId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        application_identifier: builtins.str,
        endpoint_type: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        lambda_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.LambdaEndpointInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        url_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnService.UrlEndpointInputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param application_identifier: The unique identifier of the application.
        :param endpoint_type: The endpoint type of the service.
        :param environment_identifier: The unique identifier of the environment.
        :param name: The name of the service.
        :param description: A description of the service.
        :param lambda_endpoint: A summary of the configuration for the AWS Lambda endpoint type.
        :param tags: The tags assigned to the service.
        :param url_endpoint: The summary of the configuration for the URL endpoint type.
        :param vpc_id: The ID of the virtual private cloud (VPC).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__907108c117201c32b64506342f78814db9193df99c310b83aeb209b6a8528fca)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnServiceProps(
            application_identifier=application_identifier,
            endpoint_type=endpoint_type,
            environment_identifier=environment_identifier,
            name=name,
            description=description,
            lambda_endpoint=lambda_endpoint,
            tags=tags,
            url_endpoint=url_endpoint,
            vpc_id=vpc_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad0a0706d3cf628dd2f4bba24ce52af6b8979f729ac8aaeb29e6b4361a578f9c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c2be472b9f8e246428a9701ace98667526f183bbfec96c95a0180ac2e13c4f6c)
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
        '''The Amazon Resource Name (ARN) of the service.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrServiceIdentifier")
    def attr_service_identifier(self) -> builtins.str:
        '''The unique identifier of the service.

        :cloudformationAttribute: ServiceIdentifier
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrServiceIdentifier"))

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
    @jsii.member(jsii_name="applicationIdentifier")
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.'''
        return typing.cast(builtins.str, jsii.get(self, "applicationIdentifier"))

    @application_identifier.setter
    def application_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bc95c36e696bf37c3a13a332dd78e99ff05fc55f61bedb0bf3039b4b44ad086e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="endpointType")
    def endpoint_type(self) -> builtins.str:
        '''The endpoint type of the service.'''
        return typing.cast(builtins.str, jsii.get(self, "endpointType"))

    @endpoint_type.setter
    def endpoint_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab98e4a7a0d2b4244aeb0f56d8799acba24397c5a6cd75177f9e053b1dee7ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "endpointType", value)

    @builtins.property
    @jsii.member(jsii_name="environmentIdentifier")
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.'''
        return typing.cast(builtins.str, jsii.get(self, "environmentIdentifier"))

    @environment_identifier.setter
    def environment_identifier(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee4ee299ba0a135de1f7cd2547d097ea2e42a4dfdc805e8903fa2bf85bd7e2ad)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "environmentIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the service.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5b6424269db3750c7b2d731b92e0a2069274bacaf384c3008704b8e25ad468c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__acc7be1c8c1640bd1e15d025ea9355524675edeb39983f97d86a7e6ced15b3b8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="lambdaEndpoint")
    def lambda_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.LambdaEndpointInputProperty"]]:
        '''A summary of the configuration for the AWS Lambda endpoint type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.LambdaEndpointInputProperty"]], jsii.get(self, "lambdaEndpoint"))

    @lambda_endpoint.setter
    def lambda_endpoint(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.LambdaEndpointInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6ce79e2a942fa4033925666009e186a65598cb3fb97ca81fa09a9b48ea3a2edb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "lambdaEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the service.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad2b386f0bd1b47d4230e316b8b3242b690f8af43ec7e3f72704df78d7fe2f28)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="urlEndpoint")
    def url_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.UrlEndpointInputProperty"]]:
        '''The summary of the configuration for the URL endpoint type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.UrlEndpointInputProperty"]], jsii.get(self, "urlEndpoint"))

    @url_endpoint.setter
    def url_endpoint(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnService.UrlEndpointInputProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f0628736507918deb2b4a7cc291d152a96d1e6411ee5763d8d3b3773677094e4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "urlEndpoint", value)

    @builtins.property
    @jsii.member(jsii_name="vpcId")
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC).'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcId"))

    @vpc_id.setter
    def vpc_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be028763858573aceaa89ada74c7837c9fb7f514d8e7110b5d1d143f99aceb19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcId", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnService.LambdaEndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={"arn": "arn"},
    )
    class LambdaEndpointInputProperty:
        def __init__(self, *, arn: builtins.str) -> None:
            '''The input for the AWS Lambda endpoint type.

            :param arn: The Amazon Resource Name (ARN) of the Lambda function or alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                lambda_endpoint_input_property = refactorspaces.CfnService.LambdaEndpointInputProperty(
                    arn="arn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a27c719738d8d78360e3d609d139b4f7429ffca1893e97611f5810b0c4259189)
                check_type(argname="argument arn", value=arn, expected_type=type_hints["arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "arn": arn,
            }

        @builtins.property
        def arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Lambda function or alias.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-lambdaendpointinput.html#cfn-refactorspaces-service-lambdaendpointinput-arn
            '''
            result = self._values.get("arn")
            assert result is not None, "Required property 'arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaEndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_refactorspaces.CfnService.UrlEndpointInputProperty",
        jsii_struct_bases=[],
        name_mapping={"url": "url", "health_url": "healthUrl"},
    )
    class UrlEndpointInputProperty:
        def __init__(
            self,
            *,
            url: builtins.str,
            health_url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The configuration for the URL endpoint type.

            :param url: The URL to route traffic to. The URL must be an `rfc3986-formatted URL <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc3986>`_ . If the host is a domain name, the name must be resolvable over the public internet. If the scheme is ``https`` , the top level domain of the host must be listed in the `IANA root zone database <https://docs.aws.amazon.com/https://www.iana.org/domains/root/db>`_ .
            :param health_url: The health check URL of the URL endpoint type. If the URL is a public endpoint, the ``HealthUrl`` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_refactorspaces as refactorspaces
                
                url_endpoint_input_property = refactorspaces.CfnService.UrlEndpointInputProperty(
                    url="url",
                
                    # the properties below are optional
                    health_url="healthUrl"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7d86383e689f1caa847c77d7b82f3353251e619448c701919f0bc57ed8bd5287)
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
                check_type(argname="argument health_url", value=health_url, expected_type=type_hints["health_url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "url": url,
            }
            if health_url is not None:
                self._values["health_url"] = health_url

        @builtins.property
        def url(self) -> builtins.str:
            '''The URL to route traffic to.

            The URL must be an `rfc3986-formatted URL <https://docs.aws.amazon.com/https://datatracker.ietf.org/doc/html/rfc3986>`_ . If the host is a domain name, the name must be resolvable over the public internet. If the scheme is ``https`` , the top level domain of the host must be listed in the `IANA root zone database <https://docs.aws.amazon.com/https://www.iana.org/domains/root/db>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html#cfn-refactorspaces-service-urlendpointinput-url
            '''
            result = self._values.get("url")
            assert result is not None, "Required property 'url' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def health_url(self) -> typing.Optional[builtins.str]:
            '''The health check URL of the URL endpoint type.

            If the URL is a public endpoint, the ``HealthUrl`` must also be a public endpoint. If the URL is a private endpoint inside a virtual private cloud (VPC), the health URL must also be a private endpoint, and the host must be the same as the URL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-refactorspaces-service-urlendpointinput.html#cfn-refactorspaces-service-urlendpointinput-healthurl
            '''
            result = self._values.get("health_url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "UrlEndpointInputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_refactorspaces.CfnServiceProps",
    jsii_struct_bases=[],
    name_mapping={
        "application_identifier": "applicationIdentifier",
        "endpoint_type": "endpointType",
        "environment_identifier": "environmentIdentifier",
        "name": "name",
        "description": "description",
        "lambda_endpoint": "lambdaEndpoint",
        "tags": "tags",
        "url_endpoint": "urlEndpoint",
        "vpc_id": "vpcId",
    },
)
class CfnServiceProps:
    def __init__(
        self,
        *,
        application_identifier: builtins.str,
        endpoint_type: builtins.str,
        environment_identifier: builtins.str,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        lambda_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.LambdaEndpointInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        url_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.UrlEndpointInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnService``.

        :param application_identifier: The unique identifier of the application.
        :param endpoint_type: The endpoint type of the service.
        :param environment_identifier: The unique identifier of the environment.
        :param name: The name of the service.
        :param description: A description of the service.
        :param lambda_endpoint: A summary of the configuration for the AWS Lambda endpoint type.
        :param tags: The tags assigned to the service.
        :param url_endpoint: The summary of the configuration for the URL endpoint type.
        :param vpc_id: The ID of the virtual private cloud (VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_refactorspaces as refactorspaces
            
            cfn_service_props = refactorspaces.CfnServiceProps(
                application_identifier="applicationIdentifier",
                endpoint_type="endpointType",
                environment_identifier="environmentIdentifier",
                name="name",
            
                # the properties below are optional
                description="description",
                lambda_endpoint=refactorspaces.CfnService.LambdaEndpointInputProperty(
                    arn="arn"
                ),
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                url_endpoint=refactorspaces.CfnService.UrlEndpointInputProperty(
                    url="url",
            
                    # the properties below are optional
                    health_url="healthUrl"
                ),
                vpc_id="vpcId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf70d7a4201e85912150041ac9f121f471751b70ebb43643750e3cc404c36803)
            check_type(argname="argument application_identifier", value=application_identifier, expected_type=type_hints["application_identifier"])
            check_type(argname="argument endpoint_type", value=endpoint_type, expected_type=type_hints["endpoint_type"])
            check_type(argname="argument environment_identifier", value=environment_identifier, expected_type=type_hints["environment_identifier"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument lambda_endpoint", value=lambda_endpoint, expected_type=type_hints["lambda_endpoint"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument url_endpoint", value=url_endpoint, expected_type=type_hints["url_endpoint"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "application_identifier": application_identifier,
            "endpoint_type": endpoint_type,
            "environment_identifier": environment_identifier,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if lambda_endpoint is not None:
            self._values["lambda_endpoint"] = lambda_endpoint
        if tags is not None:
            self._values["tags"] = tags
        if url_endpoint is not None:
            self._values["url_endpoint"] = url_endpoint
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def application_identifier(self) -> builtins.str:
        '''The unique identifier of the application.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-applicationidentifier
        '''
        result = self._values.get("application_identifier")
        assert result is not None, "Required property 'application_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_type(self) -> builtins.str:
        '''The endpoint type of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-endpointtype
        '''
        result = self._values.get("endpoint_type")
        assert result is not None, "Required property 'endpoint_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def environment_identifier(self) -> builtins.str:
        '''The unique identifier of the environment.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-environmentidentifier
        '''
        result = self._values.get("environment_identifier")
        assert result is not None, "Required property 'environment_identifier' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def lambda_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.LambdaEndpointInputProperty]]:
        '''A summary of the configuration for the AWS Lambda endpoint type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-lambdaendpoint
        '''
        result = self._values.get("lambda_endpoint")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.LambdaEndpointInputProperty]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags assigned to the service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def url_endpoint(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.UrlEndpointInputProperty]]:
        '''The summary of the configuration for the URL endpoint type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-urlendpoint
        '''
        result = self._values.get("url_endpoint")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.UrlEndpointInputProperty]], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the virtual private cloud (VPC).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-refactorspaces-service.html#cfn-refactorspaces-service-vpcid
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnServiceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnApplication",
    "CfnApplicationProps",
    "CfnEnvironment",
    "CfnEnvironmentProps",
    "CfnRoute",
    "CfnRouteProps",
    "CfnService",
    "CfnServiceProps",
]

publication.publish()

def _typecheckingstub__efe09dd43c3fb974d0c5c81b4c42f5319245347d1ba0af51a0027fe77e6aad92(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    environment_identifier: builtins.str,
    name: builtins.str,
    proxy_type: builtins.str,
    vpc_id: builtins.str,
    api_gateway_proxy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApiGatewayProxyInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7011b5f5302cb44f6e8327da1d8ab609b5b090012feee8d5dabc192d2d37d59(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b07ea069ba96164c117171200d67b8576bba98226e2c28037fb29d5532de04(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__551b88889ac6d0f58295880113eee3f55c2efd4355df92b3f9fccd2c956c9fca(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea6a7a37a56ee75ee952f2138af2c8ba8401cf74adeebf8a6922eee0cb947a31(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad9a18d39ac5a21164a646b9a15b300ea6334fa64dfb5bfd0570b989b3ef8e85(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ef1d0faba679fd338f3cd08e2e7cdf05975edb143dd0e601f14bd72625ad717(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__390d5bc749674d9a5d49b0922c18346f5f99422a80c7f57838dc984bbd83d042(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnApplication.ApiGatewayProxyInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__18ae2f9cbdac00e453fc30ac71e6f9520bc5a36f13a98e2f67326fd8969c8d23(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bf716c9691040b260b80d99cde314be1acfd63ad22719816a1f0749c8b5fa383(
    *,
    endpoint_type: typing.Optional[builtins.str] = None,
    stage_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5974ddb2dc67ffb28c95d9f66ee42fa70224d0f4aa23981df037681d6c4fdf1(
    *,
    environment_identifier: builtins.str,
    name: builtins.str,
    proxy_type: builtins.str,
    vpc_id: builtins.str,
    api_gateway_proxy: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnApplication.ApiGatewayProxyInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a536c3debb5766a7d9c84ccebc269b62327808a31254e1265a594b329b64555(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    network_fabric_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee147fff7adf7bdc8ae158201b2d10a5109e1a28aa52431dbc158d7e263fcbde(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__138e64a98402d3a98928b3e46ccae4a4d0dea8d23b6abe8a4b1ebce5abad37ef(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a1dd279f966e1ba560574858b8d147fa089efd23806e011056a3ab45fef84b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7218caf601ef511e6c489e41a01233a12b0895a28a26b826e4c2c36d324becd3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__271815f6b6299ae2b9ca94d64e6b3e5f6de740f2212fc74c92c95cfbbb1f7c99(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49a8b10d6ea6b81c02ef39ee701909acec2186e1d9db3d4d4ad46420728b6698(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc993226fa6d6cb56a25f6ae5fb96e6ea288e1bcd336e16e685ce08129bd9ae6(
    *,
    name: builtins.str,
    network_fabric_type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5ef0962b163b395fd9c904416cc27c1511b7a89295feb97b9cedbae2ffcc49a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_identifier: builtins.str,
    environment_identifier: builtins.str,
    route_type: builtins.str,
    service_identifier: builtins.str,
    default_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoute.DefaultRouteInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri_path_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoute.UriPathRouteInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60184063db47ddac5005c921e627702643821a736e07d8b748466fcebc033f42(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6284677163b0dcbf6c699e94d88765e9b298f9ed01772681e946311408ae6213(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2d376946bad32a682cda77d07b2b073fc17cadaed1fc43223dffcfa5c37412f7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1dfd28d40096cf9941517ac9d2d037635b77d983d8f46a22cfed6d4627d4cd1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__946936a18776032253422bf6f3cdec83d06e049a9564dd0c7786c8c37a23e190(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7759c2cbb7a97913b9c2fa8aa25c156f897dad50e14e10650aa2acd1c08b3e8d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7daaefa65bcec7258677987651fbf35fbcc04f2bae9397a83e03cd4f41cb202a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoute.DefaultRouteInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__883c592efbf4191da735efaffbd65e0924e0209da44250420beef388acb08935(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75056f6caa086eeec89a3d9d03525f3ab78e1c72b12ce9818295f9f36a109ee1(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRoute.UriPathRouteInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ea6aa520044cedf5d9d051fb9eb89987341d453afc149037ea9c10707849676(
    *,
    activation_state: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37bbcddaf33ba9305fa2a3feb1d85f7802a55919b9491e2ea4b5663e05573965(
    *,
    activation_state: builtins.str,
    append_source_path: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_child_paths: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    methods: typing.Optional[typing.Sequence[builtins.str]] = None,
    source_path: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58f3ed916c6586128a311abab14b0fec6e77c0d76bd30bce92f9ecaf0e766f82(
    *,
    application_identifier: builtins.str,
    environment_identifier: builtins.str,
    route_type: builtins.str,
    service_identifier: builtins.str,
    default_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoute.DefaultRouteInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    uri_path_route: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRoute.UriPathRouteInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__907108c117201c32b64506342f78814db9193df99c310b83aeb209b6a8528fca(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    application_identifier: builtins.str,
    endpoint_type: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    lambda_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.LambdaEndpointInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    url_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.UrlEndpointInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad0a0706d3cf628dd2f4bba24ce52af6b8979f729ac8aaeb29e6b4361a578f9c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c2be472b9f8e246428a9701ace98667526f183bbfec96c95a0180ac2e13c4f6c(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc95c36e696bf37c3a13a332dd78e99ff05fc55f61bedb0bf3039b4b44ad086e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab98e4a7a0d2b4244aeb0f56d8799acba24397c5a6cd75177f9e053b1dee7ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee4ee299ba0a135de1f7cd2547d097ea2e42a4dfdc805e8903fa2bf85bd7e2ad(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5b6424269db3750c7b2d731b92e0a2069274bacaf384c3008704b8e25ad468c(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__acc7be1c8c1640bd1e15d025ea9355524675edeb39983f97d86a7e6ced15b3b8(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6ce79e2a942fa4033925666009e186a65598cb3fb97ca81fa09a9b48ea3a2edb(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.LambdaEndpointInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad2b386f0bd1b47d4230e316b8b3242b690f8af43ec7e3f72704df78d7fe2f28(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f0628736507918deb2b4a7cc291d152a96d1e6411ee5763d8d3b3773677094e4(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnService.UrlEndpointInputProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be028763858573aceaa89ada74c7837c9fb7f514d8e7110b5d1d143f99aceb19(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a27c719738d8d78360e3d609d139b4f7429ffca1893e97611f5810b0c4259189(
    *,
    arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d86383e689f1caa847c77d7b82f3353251e619448c701919f0bc57ed8bd5287(
    *,
    url: builtins.str,
    health_url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf70d7a4201e85912150041ac9f121f471751b70ebb43643750e3cc404c36803(
    *,
    application_identifier: builtins.str,
    endpoint_type: builtins.str,
    environment_identifier: builtins.str,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    lambda_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.LambdaEndpointInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    url_endpoint: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnService.UrlEndpointInputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
