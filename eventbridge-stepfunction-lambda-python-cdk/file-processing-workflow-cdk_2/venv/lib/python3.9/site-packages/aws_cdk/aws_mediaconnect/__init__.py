'''
# AWS::MediaConnect Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_mediaconnect as mediaconnect
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for MediaConnect construct libraries](https://constructs.dev/search?q=mediaconnect)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::MediaConnect resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConnect.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::MediaConnect](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_MediaConnect.html).

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
class CfnBridge(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge",
):
    '''The AWS::MediaConnect::Bridge resource defines a connection between your data center’s gateway instances and the cloud.

    For each bridge, you specify the type of bridge, transport protocol to use, and details for any outputs and failover.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_bridge = mediaconnect.CfnBridge(self, "MyCfnBridge",
            name="name",
            placement_arn="placementArn",
            sources=[mediaconnect.CfnBridge.BridgeSourceProperty(
                flow_source=mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
                    name="name",
        
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                network_source=mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol"
                )
            )],
        
            # the properties below are optional
            egress_gateway_bridge=mediaconnect.CfnBridge.EgressGatewayBridgeProperty(
                max_bitrate=123
            ),
            ingress_gateway_bridge=mediaconnect.CfnBridge.IngressGatewayBridgeProperty(
                max_bitrate=123,
                max_outputs=123
            ),
            outputs=[mediaconnect.CfnBridge.BridgeOutputProperty(
                network_output=mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            )],
            source_failover_config=mediaconnect.CfnBridge.FailoverConfigProperty(
                failover_mode="failoverMode",
        
                # the properties below are optional
                source_priority=mediaconnect.CfnBridge.SourcePriorityProperty(
                    primary_source="primarySource"
                ),
                state="state"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        placement_arn: builtins.str,
        sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.BridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]]],
        egress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.EgressGatewayBridgeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.IngressGatewayBridgeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.BridgeOutputProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.FailoverConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
        :param placement_arn: The bridge placement Amazon Resource Number (ARN).
        :param sources: The sources that you want to add to this bridge.
        :param egress_gateway_bridge: Create a bridge with the egress bridge type. An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.
        :param ingress_gateway_bridge: Create a bridge with the ingress bridge type. An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.
        :param outputs: The outputs that you want to add to this bridge.
        :param source_failover_config: The settings for source failover.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21d1f093ae6c3ef104fbfbb93b13b3338230662ddb218fed6d74e5040acf931c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBridgeProps(
            name=name,
            placement_arn=placement_arn,
            sources=sources,
            egress_gateway_bridge=egress_gateway_bridge,
            ingress_gateway_bridge=ingress_gateway_bridge,
            outputs=outputs,
            source_failover_config=source_failover_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e83409273af3b66857452f9f32805fa3650ea56dd8bccf1a4cae459f1669317)
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
            type_hints = typing.get_type_hints(_typecheckingstub__34788268cca3ef6b9f17b00e64981600b0697ff2af1a873da5b2521e55e8f627)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrBridgeArn")
    def attr_bridge_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the bridge.

        :cloudformationAttribute: BridgeArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBridgeArn"))

    @builtins.property
    @jsii.member(jsii_name="attrBridgeState")
    def attr_bridge_state(self) -> builtins.str:
        '''The current status of the bridge.

        Possible values are: ACTIVE or STANDBY.

        :cloudformationAttribute: BridgeState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrBridgeState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The network output name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__897e5b31abf5fb8064d23feda8e8dab6abc8fc04b479fede8ec2f5a8f11283ae)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="placementArn")
    def placement_arn(self) -> builtins.str:
        '''The bridge placement Amazon Resource Number (ARN).'''
        return typing.cast(builtins.str, jsii.get(self, "placementArn"))

    @placement_arn.setter
    def placement_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b6c0d91a8143e25d3431f038cc493b72ff78caeb2aae6a8de25ef906162ed203)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "placementArn", value)

    @builtins.property
    @jsii.member(jsii_name="sources")
    def sources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeSourceProperty"]]]:
        '''The sources that you want to add to this bridge.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeSourceProperty"]]], jsii.get(self, "sources"))

    @sources.setter
    def sources(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeSourceProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c151228d22c29de1b22fb11c72513278ae8b19faf50c26128a49b5bb5cd8231e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sources", value)

    @builtins.property
    @jsii.member(jsii_name="egressGatewayBridge")
    def egress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.EgressGatewayBridgeProperty"]]:
        '''Create a bridge with the egress bridge type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.EgressGatewayBridgeProperty"]], jsii.get(self, "egressGatewayBridge"))

    @egress_gateway_bridge.setter
    def egress_gateway_bridge(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.EgressGatewayBridgeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8744f4915b3da8a1fb0b28e71cdd2260912dbea385353bb4a2378a0dcf2e1a19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressGatewayBridge", value)

    @builtins.property
    @jsii.member(jsii_name="ingressGatewayBridge")
    def ingress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.IngressGatewayBridgeProperty"]]:
        '''Create a bridge with the ingress bridge type.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.IngressGatewayBridgeProperty"]], jsii.get(self, "ingressGatewayBridge"))

    @ingress_gateway_bridge.setter
    def ingress_gateway_bridge(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.IngressGatewayBridgeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2370206c3aaeddbbe4f170d30b717ce583cd273a4a651e68abaf2042096869bf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingressGatewayBridge", value)

    @builtins.property
    @jsii.member(jsii_name="outputs")
    def outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeOutputProperty"]]]]:
        '''The outputs that you want to add to this bridge.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeOutputProperty"]]]], jsii.get(self, "outputs"))

    @outputs.setter
    def outputs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeOutputProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f0f04e00fdc529449b6434bd02be499c861ae34a03215caf6afedaf59974ca0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputs", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFailoverConfig")
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.FailoverConfigProperty"]]:
        '''The settings for source failover.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.FailoverConfigProperty"]], jsii.get(self, "sourceFailoverConfig"))

    @source_failover_config.setter
    def source_failover_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.FailoverConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a1d3ccb8b1bf31380b43926b18329ad07b95b13cfd50c81dfdcb52ed4700194)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFailoverConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeFlowSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_arn": "flowArn",
            "name": "name",
            "flow_vpc_interface_attachment": "flowVpcInterfaceAttachment",
        },
    )
    class BridgeFlowSourceProperty:
        def __init__(
            self,
            *,
            flow_arn: builtins.str,
            name: builtins.str,
            flow_vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of the bridge.

            A flow source originates in MediaConnect as an existing cloud flow.

            :param flow_arn: The ARN of the cloud flow used as a source of this bridge.
            :param name: The name of the flow source.
            :param flow_vpc_interface_attachment: The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_flow_source_property = mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
                    name="name",
                
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c9a85716cc44ad0d338a783771f76c5420792553cd40338bc48069294fac934)
                check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument flow_vpc_interface_attachment", value=flow_vpc_interface_attachment, expected_type=type_hints["flow_vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_arn": flow_arn,
                "name": name,
            }
            if flow_vpc_interface_attachment is not None:
                self._values["flow_vpc_interface_attachment"] = flow_vpc_interface_attachment

        @builtins.property
        def flow_arn(self) -> builtins.str:
            '''The ARN of the cloud flow used as a source of this bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-flowarn
            '''
            result = self._values.get("flow_arn")
            assert result is not None, "Required property 'flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the flow source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flow_vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.VpcInterfaceAttachmentProperty"]]:
            '''The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeflowsource.html#cfn-mediaconnect-bridge-bridgeflowsource-flowvpcinterfaceattachment
            '''
            result = self._values.get("flow_vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeFlowSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeNetworkOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ip_address": "ipAddress",
            "name": "name",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
            "ttl": "ttl",
        },
    )
    class BridgeNetworkOutputProperty:
        def __init__(
            self,
            *,
            ip_address: builtins.str,
            name: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
            ttl: jsii.Number,
        ) -> None:
            '''The output of the bridge.

            A network output is delivered to your premises.

            :param ip_address: The network output IP Address.
            :param name: The network output name.
            :param network_name: The network output's gateway network name.
            :param port: The network output port.
            :param protocol: The network output protocol.
            :param ttl: The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_output_property = mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__621a738d7654729dd7b3374ce4f5872ae1b369d023ed93a125315923bc53acb5)
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip_address": ip_address,
                "name": name,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
                "ttl": ttl,
            }

        @builtins.property
        def ip_address(self) -> builtins.str:
            '''The network output IP Address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-ipaddress
            '''
            result = self._values.get("ip_address")
            assert result is not None, "Required property 'ip_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The network output name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network output's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network output port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network output protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworkoutput.html#cfn-mediaconnect-bridge-bridgenetworkoutput-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeNetworkSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "multicast_ip": "multicastIp",
            "name": "name",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
        },
    )
    class BridgeNetworkSourceProperty:
        def __init__(
            self,
            *,
            multicast_ip: builtins.str,
            name: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
        ) -> None:
            '''The source of the bridge.

            A network source originates at your premises.

            :param multicast_ip: The network source multicast IP.
            :param name: The name of the network source. This name is used to reference the source and must be unique among sources in this bridge.
            :param network_name: The network source's gateway network name.
            :param port: The network source port.
            :param protocol: The network source protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_source_property = mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    name="name",
                    network_name="networkName",
                    port=123,
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1642b43f3173ebc33fe250c935a5af5006fe555caff2d5246139c99d6cfb0d9b)
                check_type(argname="argument multicast_ip", value=multicast_ip, expected_type=type_hints["multicast_ip"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "multicast_ip": multicast_ip,
                "name": name,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
            }

        @builtins.property
        def multicast_ip(self) -> builtins.str:
            '''The network source multicast IP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-multicastip
            '''
            result = self._values.get("multicast_ip")
            assert result is not None, "Required property 'multicast_ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the network source.

            This name is used to reference the source and must be unique among sources in this bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network source's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network source port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network source protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgenetworksource.html#cfn-mediaconnect-bridge-bridgenetworksource-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeOutputProperty",
        jsii_struct_bases=[],
        name_mapping={"network_output": "networkOutput"},
    )
    class BridgeOutputProperty:
        def __init__(
            self,
            *,
            network_output: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.BridgeNetworkOutputProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The output of the bridge.

            :param network_output: The output of the bridge. A network output is delivered to your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_output_property = mediaconnect.CfnBridge.BridgeOutputProperty(
                    network_output=mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                        ip_address="ipAddress",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol",
                        ttl=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__dff659c89b605c1b1a727af90c48784adba90b01104dfd2da4ea33b042b8e12f)
                check_type(argname="argument network_output", value=network_output, expected_type=type_hints["network_output"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if network_output is not None:
                self._values["network_output"] = network_output

        @builtins.property
        def network_output(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeNetworkOutputProperty"]]:
            '''The output of the bridge.

            A network output is delivered to your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgeoutput.html#cfn-mediaconnect-bridge-bridgeoutput-networkoutput
            '''
            result = self._values.get("network_output")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeNetworkOutputProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.BridgeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={"flow_source": "flowSource", "network_source": "networkSource"},
    )
    class BridgeSourceProperty:
        def __init__(
            self,
            *,
            flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.BridgeFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.BridgeNetworkSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The bridge's source.

            :param flow_source: The source of the bridge. A flow source originates in MediaConnect as an existing cloud flow.
            :param network_source: The source of the bridge. A network source originates at your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_source_property = mediaconnect.CfnBridge.BridgeSourceProperty(
                    flow_source=mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                        flow_arn="flowArn",
                        name="name",
                
                        # the properties below are optional
                        flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    network_source=mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                        multicast_ip="multicastIp",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__048c12dd6c2d1c5e61292ef13f12e16c2c87cce382b5d57ada270cfd08a1b24d)
                check_type(argname="argument flow_source", value=flow_source, expected_type=type_hints["flow_source"])
                check_type(argname="argument network_source", value=network_source, expected_type=type_hints["network_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if flow_source is not None:
                self._values["flow_source"] = flow_source
            if network_source is not None:
                self._values["network_source"] = network_source

        @builtins.property
        def flow_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeFlowSourceProperty"]]:
            '''The source of the bridge.

            A flow source originates in MediaConnect as an existing cloud flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html#cfn-mediaconnect-bridge-bridgesource-flowsource
            '''
            result = self._values.get("flow_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeFlowSourceProperty"]], result)

        @builtins.property
        def network_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeNetworkSourceProperty"]]:
            '''The source of the bridge.

            A network source originates at your premises.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-bridgesource.html#cfn-mediaconnect-bridge-bridgesource-networksource
            '''
            result = self._values.get("network_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.BridgeNetworkSourceProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.EgressGatewayBridgeProperty",
        jsii_struct_bases=[],
        name_mapping={"max_bitrate": "maxBitrate"},
    )
    class EgressGatewayBridgeProperty:
        def __init__(self, *, max_bitrate: jsii.Number) -> None:
            '''Create a bridge with the egress bridge type.

            An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.

            :param max_bitrate: The maximum expected bitrate (in bps) of the egress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-egressgatewaybridge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                egress_gateway_bridge_property = mediaconnect.CfnBridge.EgressGatewayBridgeProperty(
                    max_bitrate=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b88384d6e7eaf984035fe7a0fba90d12833212086c785ad13a9117af87f05ec0)
                check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_bitrate": max_bitrate,
            }

        @builtins.property
        def max_bitrate(self) -> jsii.Number:
            '''The maximum expected bitrate (in bps) of the egress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-egressgatewaybridge.html#cfn-mediaconnect-bridge-egressgatewaybridge-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            assert result is not None, "Required property 'max_bitrate' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EgressGatewayBridgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.FailoverConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failover_mode": "failoverMode",
            "source_priority": "sourcePriority",
            "state": "state",
        },
    )
    class FailoverConfigProperty:
        def __init__(
            self,
            *,
            failover_mode: builtins.str,
            source_priority: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridge.SourcePriorityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for source failover.

            :param failover_mode: The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.
            :param source_priority: The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams. This setting only applies when Failover Mode is set to FAILOVER.
            :param state: The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                failover_config_property = mediaconnect.CfnBridge.FailoverConfigProperty(
                    failover_mode="failoverMode",
                
                    # the properties below are optional
                    source_priority=mediaconnect.CfnBridge.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2344e6b90e667c45e503f080b931cc817ed70f01054abb50495f2670d204d2b3)
                check_type(argname="argument failover_mode", value=failover_mode, expected_type=type_hints["failover_mode"])
                check_type(argname="argument source_priority", value=source_priority, expected_type=type_hints["source_priority"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "failover_mode": failover_mode,
            }
            if source_priority is not None:
                self._values["source_priority"] = source_priority
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def failover_mode(self) -> builtins.str:
            '''The type of failover you choose for this flow.

            MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-failovermode
            '''
            result = self._values.get("failover_mode")
            assert result is not None, "Required property 'failover_mode' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def source_priority(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.SourcePriorityProperty"]]:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams. This setting only applies when Failover Mode is set to FAILOVER.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-sourcepriority
            '''
            result = self._values.get("source_priority")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridge.SourcePriorityProperty"]], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''The state of source failover on the flow.

            If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-failoverconfig.html#cfn-mediaconnect-bridge-failoverconfig-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.IngressGatewayBridgeProperty",
        jsii_struct_bases=[],
        name_mapping={"max_bitrate": "maxBitrate", "max_outputs": "maxOutputs"},
    )
    class IngressGatewayBridgeProperty:
        def __init__(
            self,
            *,
            max_bitrate: jsii.Number,
            max_outputs: jsii.Number,
        ) -> None:
            '''Create a bridge with the ingress bridge type.

            An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

            :param max_bitrate: The maximum expected bitrate (in bps) of the ingress bridge.
            :param max_outputs: The maximum number of outputs on the ingress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                ingress_gateway_bridge_property = mediaconnect.CfnBridge.IngressGatewayBridgeProperty(
                    max_bitrate=123,
                    max_outputs=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__167e9f3b8055cd05eb90612891a377cb4cde612ba7f0ec6b9e69f7d2df6ce8e6)
                check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
                check_type(argname="argument max_outputs", value=max_outputs, expected_type=type_hints["max_outputs"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "max_bitrate": max_bitrate,
                "max_outputs": max_outputs,
            }

        @builtins.property
        def max_bitrate(self) -> jsii.Number:
            '''The maximum expected bitrate (in bps) of the ingress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            assert result is not None, "Required property 'max_bitrate' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def max_outputs(self) -> jsii.Number:
            '''The maximum number of outputs on the ingress bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-ingressgatewaybridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge-maxoutputs
            '''
            result = self._values.get("max_outputs")
            assert result is not None, "Required property 'max_outputs' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IngressGatewayBridgeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.SourcePriorityProperty",
        jsii_struct_bases=[],
        name_mapping={"primary_source": "primarySource"},
    )
    class SourcePriorityProperty:
        def __init__(
            self,
            *,
            primary_source: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams. This setting only applies when Failover Mode is set to FAILOVER.

            :param primary_source: The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-sourcepriority.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                source_priority_property = mediaconnect.CfnBridge.SourcePriorityProperty(
                    primary_source="primarySource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__58ccd453e30991d345c7d1533308b0d3e5827af4b03a42b43534f313026666a0)
                check_type(argname="argument primary_source", value=primary_source, expected_type=type_hints["primary_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if primary_source is not None:
                self._values["primary_source"] = primary_source

        @builtins.property
        def primary_source(self) -> typing.Optional[builtins.str]:
            '''The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-sourcepriority.html#cfn-mediaconnect-bridge-sourcepriority-primarysource
            '''
            result = self._values.get("primary_source")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourcePriorityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The VPC interface that you want to send your output to.

            :param vpc_interface_name: The name of the VPC interface that you want to send your output to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d7119bd5cac44e94824a018e0819faa64fdc04125060ad413d57b0a00d0a8066)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface that you want to send your output to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridge-vpcinterfaceattachment.html#cfn-mediaconnect-bridge-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnBridgeOutput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeOutput",
):
    '''Adds outputs to an existing bridge.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_bridge_output = mediaconnect.CfnBridgeOutput(self, "MyCfnBridgeOutput",
            bridge_arn="bridgeArn",
            name="name",
            network_output=mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty(
                ip_address="ipAddress",
                network_name="networkName",
                port=123,
                protocol="protocol",
                ttl=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        network_output: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridgeOutput.BridgeNetworkOutputProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bridge_arn: The ARN of the bridge that you want to describe.
        :param name: The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
        :param network_output: Add a network output to an existing bridge.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37400ec0d6ede2ac41f09e81db31275470bfb18f7999012a07d588a5abfc45e7)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBridgeOutputProps(
            bridge_arn=bridge_arn, name=name, network_output=network_output
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb205f08441d39d8e1889501076cfae52006c266e0dcc55675d37bdd36eecce7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8dfc4c93ee2ec8174192f41cba8f3d6deeacc3ee4b3eeb41940e9f61c1b8c0a5)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="bridgeArn")
    def bridge_arn(self) -> builtins.str:
        '''The ARN of the bridge that you want to describe.'''
        return typing.cast(builtins.str, jsii.get(self, "bridgeArn"))

    @bridge_arn.setter
    def bridge_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__238bd53ec2ae6381eaaf2c652a080561d1722805471e9d898d9d8e2b66530295)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bridgeArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The network output name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4567364d21ca9ebe1a2f33abcf1e7bc00c0f6b671c2062fd3c6766537faf1fa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networkOutput")
    def network_output(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBridgeOutput.BridgeNetworkOutputProperty"]:
        '''Add a network output to an existing bridge.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBridgeOutput.BridgeNetworkOutputProperty"], jsii.get(self, "networkOutput"))

    @network_output.setter
    def network_output(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBridgeOutput.BridgeNetworkOutputProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78fe544a540a0346bab7b296adf77b0088521ed5104d3678ee517ee4d8b43eb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkOutput", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty",
        jsii_struct_bases=[],
        name_mapping={
            "ip_address": "ipAddress",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
            "ttl": "ttl",
        },
    )
    class BridgeNetworkOutputProperty:
        def __init__(
            self,
            *,
            ip_address: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
            ttl: jsii.Number,
        ) -> None:
            '''The output of the bridge.

            A network output is delivered to your premises.

            :param ip_address: The network output IP Address.
            :param network_name: The network output's gateway network name.
            :param port: The network output port.
            :param protocol: The network output protocol.
            :param ttl: The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_output_property = mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2c8d614c4eaf3e7a9715a54c7d8f6d68001dfdd34bed46af49b236cf97208c5b)
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip_address": ip_address,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
                "ttl": ttl,
            }

        @builtins.property
        def ip_address(self) -> builtins.str:
            '''The network output IP Address.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ipaddress
            '''
            result = self._values.get("ip_address")
            assert result is not None, "Required property 'ip_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network output's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network output port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network output protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def ttl(self) -> jsii.Number:
            '''The network output TTL.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgeoutput-bridgenetworkoutput.html#cfn-mediaconnect-bridgeoutput-bridgenetworkoutput-ttl
            '''
            result = self._values.get("ttl")
            assert result is not None, "Required property 'ttl' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkOutputProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "bridge_arn": "bridgeArn",
        "name": "name",
        "network_output": "networkOutput",
    },
)
class CfnBridgeOutputProps:
    def __init__(
        self,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        network_output: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeOutput.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnBridgeOutput``.

        :param bridge_arn: The ARN of the bridge that you want to describe.
        :param name: The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
        :param network_output: Add a network output to an existing bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_bridge_output_props = mediaconnect.CfnBridgeOutputProps(
                bridge_arn="bridgeArn",
                name="name",
                network_output=mediaconnect.CfnBridgeOutput.BridgeNetworkOutputProperty(
                    ip_address="ipAddress",
                    network_name="networkName",
                    port=123,
                    protocol="protocol",
                    ttl=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__96c246f60ce4e5ad45fa8b46aaba3a5dc86b8fbceb04cd700ed6ecc964f18f2a)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument network_output", value=network_output, expected_type=type_hints["network_output"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
            "name": name,
            "network_output": network_output,
        }

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The ARN of the bridge that you want to describe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-bridgearn
        '''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The network output name.

        This name is used to reference the output and must be unique among outputs in this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def network_output(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBridgeOutput.BridgeNetworkOutputProperty]:
        '''Add a network output to an existing bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgeoutput.html#cfn-mediaconnect-bridgeoutput-networkoutput
        '''
        result = self._values.get("network_output")
        assert result is not None, "Required property 'network_output' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBridgeOutput.BridgeNetworkOutputProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBridgeOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "placement_arn": "placementArn",
        "sources": "sources",
        "egress_gateway_bridge": "egressGatewayBridge",
        "ingress_gateway_bridge": "ingressGatewayBridge",
        "outputs": "outputs",
        "source_failover_config": "sourceFailoverConfig",
    },
)
class CfnBridgeProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        placement_arn: builtins.str,
        sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
        egress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.EgressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ingress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.IngressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeOutputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBridge``.

        :param name: The network output name. This name is used to reference the output and must be unique among outputs in this bridge.
        :param placement_arn: The bridge placement Amazon Resource Number (ARN).
        :param sources: The sources that you want to add to this bridge.
        :param egress_gateway_bridge: Create a bridge with the egress bridge type. An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.
        :param ingress_gateway_bridge: Create a bridge with the ingress bridge type. An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.
        :param outputs: The outputs that you want to add to this bridge.
        :param source_failover_config: The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_bridge_props = mediaconnect.CfnBridgeProps(
                name="name",
                placement_arn="placementArn",
                sources=[mediaconnect.CfnBridge.BridgeSourceProperty(
                    flow_source=mediaconnect.CfnBridge.BridgeFlowSourceProperty(
                        flow_arn="flowArn",
                        name="name",
            
                        # the properties below are optional
                        flow_vpc_interface_attachment=mediaconnect.CfnBridge.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    network_source=mediaconnect.CfnBridge.BridgeNetworkSourceProperty(
                        multicast_ip="multicastIp",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol"
                    )
                )],
            
                # the properties below are optional
                egress_gateway_bridge=mediaconnect.CfnBridge.EgressGatewayBridgeProperty(
                    max_bitrate=123
                ),
                ingress_gateway_bridge=mediaconnect.CfnBridge.IngressGatewayBridgeProperty(
                    max_bitrate=123,
                    max_outputs=123
                ),
                outputs=[mediaconnect.CfnBridge.BridgeOutputProperty(
                    network_output=mediaconnect.CfnBridge.BridgeNetworkOutputProperty(
                        ip_address="ipAddress",
                        name="name",
                        network_name="networkName",
                        port=123,
                        protocol="protocol",
                        ttl=123
                    )
                )],
                source_failover_config=mediaconnect.CfnBridge.FailoverConfigProperty(
                    failover_mode="failoverMode",
            
                    # the properties below are optional
                    source_priority=mediaconnect.CfnBridge.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__73e5019972892e93be93b465cdd4743483355d6d745af2863fcbd2ab360c88ef)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument placement_arn", value=placement_arn, expected_type=type_hints["placement_arn"])
            check_type(argname="argument sources", value=sources, expected_type=type_hints["sources"])
            check_type(argname="argument egress_gateway_bridge", value=egress_gateway_bridge, expected_type=type_hints["egress_gateway_bridge"])
            check_type(argname="argument ingress_gateway_bridge", value=ingress_gateway_bridge, expected_type=type_hints["ingress_gateway_bridge"])
            check_type(argname="argument outputs", value=outputs, expected_type=type_hints["outputs"])
            check_type(argname="argument source_failover_config", value=source_failover_config, expected_type=type_hints["source_failover_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "placement_arn": placement_arn,
            "sources": sources,
        }
        if egress_gateway_bridge is not None:
            self._values["egress_gateway_bridge"] = egress_gateway_bridge
        if ingress_gateway_bridge is not None:
            self._values["ingress_gateway_bridge"] = ingress_gateway_bridge
        if outputs is not None:
            self._values["outputs"] = outputs
        if source_failover_config is not None:
            self._values["source_failover_config"] = source_failover_config

    @builtins.property
    def name(self) -> builtins.str:
        '''The network output name.

        This name is used to reference the output and must be unique among outputs in this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def placement_arn(self) -> builtins.str:
        '''The bridge placement Amazon Resource Number (ARN).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-placementarn
        '''
        result = self._values.get("placement_arn")
        assert result is not None, "Required property 'placement_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sources(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeSourceProperty]]]:
        '''The sources that you want to add to this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-sources
        '''
        result = self._values.get("sources")
        assert result is not None, "Required property 'sources' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeSourceProperty]]], result)

    @builtins.property
    def egress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.EgressGatewayBridgeProperty]]:
        '''Create a bridge with the egress bridge type.

        An egress bridge is a cloud-to-ground bridge. The content comes from an existing MediaConnect flow and is delivered to your premises.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-egressgatewaybridge
        '''
        result = self._values.get("egress_gateway_bridge")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.EgressGatewayBridgeProperty]], result)

    @builtins.property
    def ingress_gateway_bridge(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.IngressGatewayBridgeProperty]]:
        '''Create a bridge with the ingress bridge type.

        An ingress bridge is a ground-to-cloud bridge. The content originates at your premises and is delivered to the cloud.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-ingressgatewaybridge
        '''
        result = self._values.get("ingress_gateway_bridge")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.IngressGatewayBridgeProperty]], result)

    @builtins.property
    def outputs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeOutputProperty]]]]:
        '''The outputs that you want to add to this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-outputs
        '''
        result = self._values.get("outputs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeOutputProperty]]]], result)

    @builtins.property
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.FailoverConfigProperty]]:
        '''The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridge.html#cfn-mediaconnect-bridge-sourcefailoverconfig
        '''
        result = self._values.get("source_failover_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.FailoverConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBridgeProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnBridgeSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource",
):
    '''Adds sources to an existing bridge.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_bridge_source = mediaconnect.CfnBridgeSource(self, "MyCfnBridgeSource",
            bridge_arn="bridgeArn",
            name="name",
        
            # the properties below are optional
            flow_source=mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty(
                flow_arn="flowArn",
        
                # the properties below are optional
                flow_vpc_interface_attachment=mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            ),
            network_source=mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty(
                multicast_ip="multicastIp",
                network_name="networkName",
                port=123,
                protocol="protocol"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridgeSource.BridgeFlowSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridgeSource.BridgeNetworkSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param bridge_arn: The ARN of the bridge that you want to describe.
        :param name: The name of the network source. This name is used to reference the source and must be unique among sources in this bridge.
        :param flow_source: Add a flow source to an existing bridge.
        :param network_source: Add a network source to an existing bridge.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e36e10c04a0f01de7ebc0521a5800daea1daa62e3bd343704ff6e84525f6f408)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBridgeSourceProps(
            bridge_arn=bridge_arn,
            name=name,
            flow_source=flow_source,
            network_source=network_source,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8ee6617fa681b5aaf625fc2493bb4ea5b5e578a01029bdd7ba2b8647be429130)
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
            type_hints = typing.get_type_hints(_typecheckingstub__64ce37bd7d5055cf2fb388e369c965f5e01fd162753e68839b53dd0443911c4b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="bridgeArn")
    def bridge_arn(self) -> builtins.str:
        '''The ARN of the bridge that you want to describe.'''
        return typing.cast(builtins.str, jsii.get(self, "bridgeArn"))

    @bridge_arn.setter
    def bridge_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__28bb545b11a59b0c10f19770b49da21586071508bfbed47b6b137ab43e2aaa5d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "bridgeArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the network source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__26ff480997cae96d755e2b7e83019229c27702f843cafce3fc5647020ec7d7a7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="flowSource")
    def flow_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.BridgeFlowSourceProperty"]]:
        '''Add a flow source to an existing bridge.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.BridgeFlowSourceProperty"]], jsii.get(self, "flowSource"))

    @flow_source.setter
    def flow_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.BridgeFlowSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa9a2d6952ebe510d69e3877d36b01cb4f6aa83e11dfcf61576bdfaffa0dea74)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowSource", value)

    @builtins.property
    @jsii.member(jsii_name="networkSource")
    def network_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.BridgeNetworkSourceProperty"]]:
        '''Add a network source to an existing bridge.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.BridgeNetworkSourceProperty"]], jsii.get(self, "networkSource"))

    @network_source.setter
    def network_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.BridgeNetworkSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__afb1ff783738c431282bcaa0dec602d425b3f5a39195a1f65e4e683ba344caea)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networkSource", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "flow_arn": "flowArn",
            "flow_vpc_interface_attachment": "flowVpcInterfaceAttachment",
        },
    )
    class BridgeFlowSourceProperty:
        def __init__(
            self,
            *,
            flow_arn: builtins.str,
            flow_vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBridgeSource.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source of the bridge.

            A flow source originates in MediaConnect as an existing cloud flow.

            :param flow_arn: The ARN of the cloud flow used as a source of this bridge.
            :param flow_vpc_interface_attachment: The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_flow_source_property = mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
                
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8bb9109e42561a117540865cd31be3adb19651461f90f2af2ac7c6ce75a0c13e)
                check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
                check_type(argname="argument flow_vpc_interface_attachment", value=flow_vpc_interface_attachment, expected_type=type_hints["flow_vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "flow_arn": flow_arn,
            }
            if flow_vpc_interface_attachment is not None:
                self._values["flow_vpc_interface_attachment"] = flow_vpc_interface_attachment

        @builtins.property
        def flow_arn(self) -> builtins.str:
            '''The ARN of the cloud flow used as a source of this bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html#cfn-mediaconnect-bridgesource-bridgeflowsource-flowarn
            '''
            result = self._values.get("flow_arn")
            assert result is not None, "Required property 'flow_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flow_vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.VpcInterfaceAttachmentProperty"]]:
            '''The name of the VPC interface attachment to use for this source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgeflowsource.html#cfn-mediaconnect-bridgesource-bridgeflowsource-flowvpcinterfaceattachment
            '''
            result = self._values.get("flow_vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBridgeSource.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeFlowSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "multicast_ip": "multicastIp",
            "network_name": "networkName",
            "port": "port",
            "protocol": "protocol",
        },
    )
    class BridgeNetworkSourceProperty:
        def __init__(
            self,
            *,
            multicast_ip: builtins.str,
            network_name: builtins.str,
            port: jsii.Number,
            protocol: builtins.str,
        ) -> None:
            '''The source of the bridge.

            A network source originates at your premises.

            :param multicast_ip: The network source multicast IP.
            :param network_name: The network source's gateway network name.
            :param port: The network source port.
            :param protocol: The network source protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                bridge_network_source_property = mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    network_name="networkName",
                    port=123,
                    protocol="protocol"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__93b2199f774afbb32a622ba44ca26954c8e46e149f1bc0836b1dda198de28020)
                check_type(argname="argument multicast_ip", value=multicast_ip, expected_type=type_hints["multicast_ip"])
                check_type(argname="argument network_name", value=network_name, expected_type=type_hints["network_name"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "multicast_ip": multicast_ip,
                "network_name": network_name,
                "port": port,
                "protocol": protocol,
            }

        @builtins.property
        def multicast_ip(self) -> builtins.str:
            '''The network source multicast IP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-multicastip
            '''
            result = self._values.get("multicast_ip")
            assert result is not None, "Required property 'multicast_ip' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def network_name(self) -> builtins.str:
            '''The network source's gateway network name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-networkname
            '''
            result = self._values.get("network_name")
            assert result is not None, "Required property 'network_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def port(self) -> jsii.Number:
            '''The network source port.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-port
            '''
            result = self._values.get("port")
            assert result is not None, "Required property 'port' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def protocol(self) -> builtins.str:
            '''The network source protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-bridgenetworksource.html#cfn-mediaconnect-bridgesource-bridgenetworksource-protocol
            '''
            result = self._values.get("protocol")
            assert result is not None, "Required property 'protocol' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BridgeNetworkSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The VPC interface that you want to send your output to.

            :param vpc_interface_name: The name of the VPC interface that you want to send your output to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e6d9b48314e46735258c941180d8e92fa25af944c2b991fb6827ccc97fa800b4)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface that you want to send your output to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-bridgesource-vpcinterfaceattachment.html#cfn-mediaconnect-bridgesource-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnBridgeSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "bridge_arn": "bridgeArn",
        "name": "name",
        "flow_source": "flowSource",
        "network_source": "networkSource",
    },
)
class CfnBridgeSourceProps:
    def __init__(
        self,
        *,
        bridge_arn: builtins.str,
        name: builtins.str,
        flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBridgeSource``.

        :param bridge_arn: The ARN of the bridge that you want to describe.
        :param name: The name of the network source. This name is used to reference the source and must be unique among sources in this bridge.
        :param flow_source: Add a flow source to an existing bridge.
        :param network_source: Add a network source to an existing bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_bridge_source_props = mediaconnect.CfnBridgeSourceProps(
                bridge_arn="bridgeArn",
                name="name",
            
                # the properties below are optional
                flow_source=mediaconnect.CfnBridgeSource.BridgeFlowSourceProperty(
                    flow_arn="flowArn",
            
                    # the properties below are optional
                    flow_vpc_interface_attachment=mediaconnect.CfnBridgeSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                network_source=mediaconnect.CfnBridgeSource.BridgeNetworkSourceProperty(
                    multicast_ip="multicastIp",
                    network_name="networkName",
                    port=123,
                    protocol="protocol"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5f2a15e5c2c97898000fd91706ed5ee02d0a7d5d31640d04f545d4db3c27ec23)
            check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument flow_source", value=flow_source, expected_type=type_hints["flow_source"])
            check_type(argname="argument network_source", value=network_source, expected_type=type_hints["network_source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bridge_arn": bridge_arn,
            "name": name,
        }
        if flow_source is not None:
            self._values["flow_source"] = flow_source
        if network_source is not None:
            self._values["network_source"] = network_source

    @builtins.property
    def bridge_arn(self) -> builtins.str:
        '''The ARN of the bridge that you want to describe.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-bridgearn
        '''
        result = self._values.get("bridge_arn")
        assert result is not None, "Required property 'bridge_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the network source.

        This name is used to reference the source and must be unique among sources in this bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeFlowSourceProperty]]:
        '''Add a flow source to an existing bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-flowsource
        '''
        result = self._values.get("flow_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeFlowSourceProperty]], result)

    @builtins.property
    def network_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeNetworkSourceProperty]]:
        '''Add a network source to an existing bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-bridgesource.html#cfn-mediaconnect-bridgesource-networksource
        '''
        result = self._values.get("network_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeNetworkSourceProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBridgeSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFlow(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow",
):
    '''The AWS::MediaConnect::Flow resource defines a connection between one or more video sources and one or more outputs.

    For each flow, you specify the transport protocol to use, encryption information, and details for any outputs or entitlements that you want. AWS Elemental MediaConnect returns an ingest endpoint where you can send your live video as a single unicast stream. The service replicates and distributes the video to every output that you specify, whether inside or outside the AWS Cloud. You can also set up entitlements on a flow to allow other AWS accounts to access your content.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow = mediaconnect.CfnFlow(self, "MyCfnFlow",
            name="name",
            source=mediaconnect.CfnFlow.SourceProperty(
                decryption=mediaconnect.CfnFlow.EncryptionProperty(
                    role_arn="roleArn",
        
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                ),
                description="description",
                entitlement_arn="entitlementArn",
                gateway_bridge_source=mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
        
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                ingest_ip="ingestIp",
                ingest_port=123,
                max_bitrate=123,
                max_latency=123,
                min_latency=123,
                name="name",
                protocol="protocol",
                sender_control_port=123,
                sender_ip_address="senderIpAddress",
                source_arn="sourceArn",
                source_ingest_port="sourceIngestPort",
                source_listener_address="sourceListenerAddress",
                source_listener_port=123,
                stream_id="streamId",
                vpc_interface_name="vpcInterfaceName",
                whitelist_cidr="whitelistCidr"
            ),
        
            # the properties below are optional
            availability_zone="availabilityZone",
            source_failover_config=mediaconnect.CfnFlow.FailoverConfigProperty(
                failover_mode="failoverMode",
                recovery_window=123,
                source_priority=mediaconnect.CfnFlow.SourcePriorityProperty(
                    primary_source="primarySource"
                ),
                state="state"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        source: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SourceProperty", typing.Dict[builtins.str, typing.Any]]],
        availability_zone: typing.Optional[builtins.str] = None,
        source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.FailoverConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the flow.
        :param source: The settings for the source that you want to use for the new flow.
        :param availability_zone: The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
        :param source_failover_config: The settings for source failover.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3568a95be2a886825b3db731f10e2fdea8be142c554d1e2055d7e22f5e6a3991)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowProps(
            name=name,
            source=source,
            availability_zone=availability_zone,
            source_failover_config=source_failover_config,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3bf65a3dfd8c719cb8ba7cde45e0dc8693f2306db4dba4cd6da5e4727579cc7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8244ccdcee08a7984c185f2ee476300520ed80658ec1efcbcb9634a230a0687a)
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
        '''The Amazon Resource Name (ARN) of the flow.

        :cloudformationAttribute: FlowArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowArn"))

    @builtins.property
    @jsii.member(jsii_name="attrFlowAvailabilityZone")
    def attr_flow_availability_zone(self) -> builtins.str:
        '''The Availability Zone that the flow was created in.

        These options are limited to the Availability Zones within the current AWS Region.

        :cloudformationAttribute: FlowAvailabilityZone
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrFlowAvailabilityZone"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceIngestIp")
    def attr_source_ingest_ip(self) -> builtins.str:
        '''The IP address that the flow listens on for incoming content.

        :cloudformationAttribute: Source.IngestIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceIngestIp"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceSourceArn")
    def attr_source_source_arn(self) -> builtins.str:
        '''The ARN of the source.

        :cloudformationAttribute: Source.SourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceSourceIngestPort")
    def attr_source_source_ingest_port(self) -> builtins.str:
        '''The port that the flow listens on for incoming content.

        If the protocol of the source is Zixi, the port must be set to 2088.

        :cloudformationAttribute: Source.SourceIngestPort
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceSourceIngestPort"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7b9dd07005f4a1ea040eea97dccca156a16f5e9f3f6686139fbd52108ac4c3b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="source")
    def source(self) -> typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceProperty"]:
        '''The settings for the source that you want to use for the new flow.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceProperty"], jsii.get(self, "source"))

    @source.setter
    def source(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFlow.SourceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__869299c75adeb5a7d478686f55b98acba18c279372a76486ab2c6231b1e54e54)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "source", value)

    @builtins.property
    @jsii.member(jsii_name="availabilityZone")
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that you want to create the flow in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "availabilityZone"))

    @availability_zone.setter
    def availability_zone(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843065332a6d7586586605a6ec8a2bd932a36dd6774052d60e5f9fd8e52c280c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "availabilityZone", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFailoverConfig")
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.FailoverConfigProperty"]]:
        '''The settings for source failover.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.FailoverConfigProperty"]], jsii.get(self, "sourceFailoverConfig"))

    @source_failover_config.setter
    def source_failover_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.FailoverConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9d7deae7edf526ef9a6af2e16b592ef198ecb0cc777d1c7d97f392933ad97ef6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFailoverConfig", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "algorithm": "algorithm",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            algorithm: typing.Optional[builtins.str] = None,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the encryption of the flow.

            :param role_arn: The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
            :param device_id: The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"
            :param region: The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param resource_id: An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.
            :param url: The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlow.EncryptionProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__023b62e8b380bcfa878c2a07568bc0d0f9912919827c329972ee2130250892b3)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content.

            This parameter is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''The value of one of the devices that you configured with your digital rights management (DRM) platform key provider.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the API Gateway proxy endpoint was created in.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''An identifier for the content.

            The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL from the API Gateway proxy that you set up to talk to your key server.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-encryption.html#cfn-mediaconnect-flow-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.FailoverConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "failover_mode": "failoverMode",
            "recovery_window": "recoveryWindow",
            "source_priority": "sourcePriority",
            "state": "state",
        },
    )
    class FailoverConfigProperty:
        def __init__(
            self,
            *,
            failover_mode: typing.Optional[builtins.str] = None,
            recovery_window: typing.Optional[jsii.Number] = None,
            source_priority: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.SourcePriorityProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            state: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for source failover.

            :param failover_mode: The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams. The string for this property must be entered as MERGE or FAILOVER. No other string entry is valid.
            :param recovery_window: The size of the buffer (delay) that the service maintains. A larger buffer means a longer delay in transmitting the stream, but more room for error correction. A smaller buffer means a shorter delay, but less room for error correction. You can choose a value from 100-500 ms. If you keep this field blank, the service uses the default value of 200 ms. This setting only applies when Failover Mode is set to MERGE.
            :param source_priority: The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams. This setting only applies when Failover Mode is set to FAILOVER.
            :param state: The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                failover_config_property = mediaconnect.CfnFlow.FailoverConfigProperty(
                    failover_mode="failoverMode",
                    recovery_window=123,
                    source_priority=mediaconnect.CfnFlow.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__60d936fe41cb44293e591fd7a9b89da19bc9fc2509d0dacf4ad7a22a54e1bae9)
                check_type(argname="argument failover_mode", value=failover_mode, expected_type=type_hints["failover_mode"])
                check_type(argname="argument recovery_window", value=recovery_window, expected_type=type_hints["recovery_window"])
                check_type(argname="argument source_priority", value=source_priority, expected_type=type_hints["source_priority"])
                check_type(argname="argument state", value=state, expected_type=type_hints["state"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if failover_mode is not None:
                self._values["failover_mode"] = failover_mode
            if recovery_window is not None:
                self._values["recovery_window"] = recovery_window
            if source_priority is not None:
                self._values["source_priority"] = source_priority
            if state is not None:
                self._values["state"] = state

        @builtins.property
        def failover_mode(self) -> typing.Optional[builtins.str]:
            '''The type of failover you choose for this flow.

            MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams. The string for this property must be entered as MERGE or FAILOVER. No other string entry is valid.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-failovermode
            '''
            result = self._values.get("failover_mode")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recovery_window(self) -> typing.Optional[jsii.Number]:
            '''The size of the buffer (delay) that the service maintains.

            A larger buffer means a longer delay in transmitting the stream, but more room for error correction. A smaller buffer means a shorter delay, but less room for error correction. You can choose a value from 100-500 ms. If you keep this field blank, the service uses the default value of 200 ms. This setting only applies when Failover Mode is set to MERGE.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-recoverywindow
            '''
            result = self._values.get("recovery_window")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def source_priority(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SourcePriorityProperty"]]:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams. This setting only applies when Failover Mode is set to FAILOVER.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-sourcepriority
            '''
            result = self._values.get("source_priority")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.SourcePriorityProperty"]], result)

        @builtins.property
        def state(self) -> typing.Optional[builtins.str]:
            '''The state of source failover on the flow.

            If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-failoverconfig.html#cfn-mediaconnect-flow-failoverconfig-state
            '''
            result = self._values.get("state")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FailoverConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.GatewayBridgeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bridge_arn": "bridgeArn",
            "vpc_interface_attachment": "vpcInterfaceAttachment",
        },
    )
    class GatewayBridgeSourceProperty:
        def __init__(
            self,
            *,
            bridge_arn: builtins.str,
            vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source configuration for cloud flows receiving a stream from a bridge.

            :param bridge_arn: The ARN of the bridge feeding this flow.
            :param vpc_interface_attachment: The settings for attaching a VPC interface to an resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                gateway_bridge_source_property = mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
                
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__00bf15dc37f493c33d6b2109cfa6283d2bb14bdc23b0ae4fd75a67ca60084ea8)
                check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
                check_type(argname="argument vpc_interface_attachment", value=vpc_interface_attachment, expected_type=type_hints["vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bridge_arn": bridge_arn,
            }
            if vpc_interface_attachment is not None:
                self._values["vpc_interface_attachment"] = vpc_interface_attachment

        @builtins.property
        def bridge_arn(self) -> builtins.str:
            '''The ARN of the bridge feeding this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html#cfn-mediaconnect-flow-gatewaybridgesource-bridgearn
            '''
            result = self._values.get("bridge_arn")
            assert result is not None, "Required property 'bridge_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.VpcInterfaceAttachmentProperty"]]:
            '''The settings for attaching a VPC interface to an resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-gatewaybridgesource.html#cfn-mediaconnect-flow-gatewaybridgesource-vpcinterfaceattachment
            '''
            result = self._values.get("vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayBridgeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SourcePriorityProperty",
        jsii_struct_bases=[],
        name_mapping={"primary_source": "primarySource"},
    )
    class SourcePriorityProperty:
        def __init__(self, *, primary_source: builtins.str) -> None:
            '''The priority you want to assign to a source.

            You can have a primary stream and a backup stream or two equally prioritized streams. This setting only applies when Failover Mode is set to FAILOVER.

            :param primary_source: The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcepriority.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                source_priority_property = mediaconnect.CfnFlow.SourcePriorityProperty(
                    primary_source="primarySource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a502d8c706596e3abd881dc963357d969893e22e8d25e78085445e09c58ac78b)
                check_type(argname="argument primary_source", value=primary_source, expected_type=type_hints["primary_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "primary_source": primary_source,
            }

        @builtins.property
        def primary_source(self) -> builtins.str:
            '''The name of the source you choose as the primary source for this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-sourcepriority.html#cfn-mediaconnect-flow-sourcepriority-primarysource
            '''
            result = self._values.get("primary_source")
            assert result is not None, "Required property 'primary_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SourcePriorityProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.SourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "decryption": "decryption",
            "description": "description",
            "entitlement_arn": "entitlementArn",
            "gateway_bridge_source": "gatewayBridgeSource",
            "ingest_ip": "ingestIp",
            "ingest_port": "ingestPort",
            "max_bitrate": "maxBitrate",
            "max_latency": "maxLatency",
            "min_latency": "minLatency",
            "name": "name",
            "protocol": "protocol",
            "sender_control_port": "senderControlPort",
            "sender_ip_address": "senderIpAddress",
            "source_arn": "sourceArn",
            "source_ingest_port": "sourceIngestPort",
            "source_listener_address": "sourceListenerAddress",
            "source_listener_port": "sourceListenerPort",
            "stream_id": "streamId",
            "vpc_interface_name": "vpcInterfaceName",
            "whitelist_cidr": "whitelistCidr",
        },
    )
    class SourceProperty:
        def __init__(
            self,
            *,
            decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            description: typing.Optional[builtins.str] = None,
            entitlement_arn: typing.Optional[builtins.str] = None,
            gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlow.GatewayBridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ingest_ip: typing.Optional[builtins.str] = None,
            ingest_port: typing.Optional[jsii.Number] = None,
            max_bitrate: typing.Optional[jsii.Number] = None,
            max_latency: typing.Optional[jsii.Number] = None,
            min_latency: typing.Optional[jsii.Number] = None,
            name: typing.Optional[builtins.str] = None,
            protocol: typing.Optional[builtins.str] = None,
            sender_control_port: typing.Optional[jsii.Number] = None,
            sender_ip_address: typing.Optional[builtins.str] = None,
            source_arn: typing.Optional[builtins.str] = None,
            source_ingest_port: typing.Optional[builtins.str] = None,
            source_listener_address: typing.Optional[builtins.str] = None,
            source_listener_port: typing.Optional[jsii.Number] = None,
            stream_id: typing.Optional[builtins.str] = None,
            vpc_interface_name: typing.Optional[builtins.str] = None,
            whitelist_cidr: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The details of the sources of the flow.

            If you are creating a flow with a VPC source, you must first create the flow with a temporary standard source by doing the following:

            - Use CloudFormation to create a flow with a standard source that uses the flow’s public IP address.
            - Use CloudFormation to create the VPC interface to add to this flow. This can also be done as part of the previous step.
            - After CloudFormation has created the flow and the VPC interface, update the source to point to the VPC interface that you created.

            :param decryption: The type of encryption that is used on the content ingested from the source.
            :param description: A description of the source. This description is not visible outside of the current AWS account.
            :param entitlement_arn: The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account. The entitlement is set by the content originator and the ARN is generated as part of the originator’s flow.
            :param gateway_bridge_source: The source configuration for cloud flows receiving a stream from a bridge.
            :param ingest_ip: The IP address that the flow listens on for incoming content.
            :param ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
            :param max_bitrate: The maximum bitrate for RIST, RTP, and RTP-FEC streams.
            :param max_latency: The maximum latency in milliseconds for a RIST or Zixi-based source. Default: - 2000
            :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. Default: - 2000
            :param name: The name of the source.
            :param protocol: The protocol that is used by the source. AWS CloudFormation does not currently support CDI or ST 2110 JPEG XS source protocols.
            :param sender_control_port: The port that the flow uses to send outbound requests to initiate connection with the sender.
            :param sender_ip_address: The IP address that the flow communicates with to initiate connection with the sender.
            :param source_arn: The ARN of the source.
            :param source_ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
            :param source_listener_address: Source IP or domain name for SRT-caller protocol.
            :param source_listener_port: Source port for SRT-caller protocol.
            :param stream_id: The stream ID that you want to use for the transport. This parameter applies only to Zixi-based streams.
            :param vpc_interface_name: The name of the VPC interface that the source content comes from.
            :param whitelist_cidr: The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                source_property = mediaconnect.CfnFlow.SourceProperty(
                    decryption=mediaconnect.CfnFlow.EncryptionProperty(
                        role_arn="roleArn",
                
                        # the properties below are optional
                        algorithm="algorithm",
                        constant_initialization_vector="constantInitializationVector",
                        device_id="deviceId",
                        key_type="keyType",
                        region="region",
                        resource_id="resourceId",
                        secret_arn="secretArn",
                        url="url"
                    ),
                    description="description",
                    entitlement_arn="entitlementArn",
                    gateway_bridge_source=mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                        bridge_arn="bridgeArn",
                
                        # the properties below are optional
                        vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    ingest_ip="ingestIp",
                    ingest_port=123,
                    max_bitrate=123,
                    max_latency=123,
                    min_latency=123,
                    name="name",
                    protocol="protocol",
                    sender_control_port=123,
                    sender_ip_address="senderIpAddress",
                    source_arn="sourceArn",
                    source_ingest_port="sourceIngestPort",
                    source_listener_address="sourceListenerAddress",
                    source_listener_port=123,
                    stream_id="streamId",
                    vpc_interface_name="vpcInterfaceName",
                    whitelist_cidr="whitelistCidr"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0c35ebd36bb52715c021bc299f222a377254ec8a3bd90d9c933fbefcac2bdf0c)
                check_type(argname="argument decryption", value=decryption, expected_type=type_hints["decryption"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
                check_type(argname="argument entitlement_arn", value=entitlement_arn, expected_type=type_hints["entitlement_arn"])
                check_type(argname="argument gateway_bridge_source", value=gateway_bridge_source, expected_type=type_hints["gateway_bridge_source"])
                check_type(argname="argument ingest_ip", value=ingest_ip, expected_type=type_hints["ingest_ip"])
                check_type(argname="argument ingest_port", value=ingest_port, expected_type=type_hints["ingest_port"])
                check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
                check_type(argname="argument max_latency", value=max_latency, expected_type=type_hints["max_latency"])
                check_type(argname="argument min_latency", value=min_latency, expected_type=type_hints["min_latency"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
                check_type(argname="argument sender_control_port", value=sender_control_port, expected_type=type_hints["sender_control_port"])
                check_type(argname="argument sender_ip_address", value=sender_ip_address, expected_type=type_hints["sender_ip_address"])
                check_type(argname="argument source_arn", value=source_arn, expected_type=type_hints["source_arn"])
                check_type(argname="argument source_ingest_port", value=source_ingest_port, expected_type=type_hints["source_ingest_port"])
                check_type(argname="argument source_listener_address", value=source_listener_address, expected_type=type_hints["source_listener_address"])
                check_type(argname="argument source_listener_port", value=source_listener_port, expected_type=type_hints["source_listener_port"])
                check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
                check_type(argname="argument whitelist_cidr", value=whitelist_cidr, expected_type=type_hints["whitelist_cidr"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if decryption is not None:
                self._values["decryption"] = decryption
            if description is not None:
                self._values["description"] = description
            if entitlement_arn is not None:
                self._values["entitlement_arn"] = entitlement_arn
            if gateway_bridge_source is not None:
                self._values["gateway_bridge_source"] = gateway_bridge_source
            if ingest_ip is not None:
                self._values["ingest_ip"] = ingest_ip
            if ingest_port is not None:
                self._values["ingest_port"] = ingest_port
            if max_bitrate is not None:
                self._values["max_bitrate"] = max_bitrate
            if max_latency is not None:
                self._values["max_latency"] = max_latency
            if min_latency is not None:
                self._values["min_latency"] = min_latency
            if name is not None:
                self._values["name"] = name
            if protocol is not None:
                self._values["protocol"] = protocol
            if sender_control_port is not None:
                self._values["sender_control_port"] = sender_control_port
            if sender_ip_address is not None:
                self._values["sender_ip_address"] = sender_ip_address
            if source_arn is not None:
                self._values["source_arn"] = source_arn
            if source_ingest_port is not None:
                self._values["source_ingest_port"] = source_ingest_port
            if source_listener_address is not None:
                self._values["source_listener_address"] = source_listener_address
            if source_listener_port is not None:
                self._values["source_listener_port"] = source_listener_port
            if stream_id is not None:
                self._values["stream_id"] = stream_id
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name
            if whitelist_cidr is not None:
                self._values["whitelist_cidr"] = whitelist_cidr

        @builtins.property
        def decryption(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.EncryptionProperty"]]:
            '''The type of encryption that is used on the content ingested from the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-decryption
            '''
            result = self._values.get("decryption")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.EncryptionProperty"]], result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of the source.

            This description is not visible outside of the current AWS account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def entitlement_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the entitlement that allows you to subscribe to content that comes from another AWS account.

            The entitlement is set by the content originator and the ARN is generated as part of the originator’s flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-entitlementarn
            '''
            result = self._values.get("entitlement_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def gateway_bridge_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.GatewayBridgeSourceProperty"]]:
            '''The source configuration for cloud flows receiving a stream from a bridge.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-gatewaybridgesource
            '''
            result = self._values.get("gateway_bridge_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlow.GatewayBridgeSourceProperty"]], result)

        @builtins.property
        def ingest_ip(self) -> typing.Optional[builtins.str]:
            '''The IP address that the flow listens on for incoming content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestip
            '''
            result = self._values.get("ingest_ip")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ingest_port(self) -> typing.Optional[jsii.Number]:
            '''The port that the flow listens on for incoming content.

            If the protocol of the source is Zixi, the port must be set to 2088.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-ingestport
            '''
            result = self._values.get("ingest_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_bitrate(self) -> typing.Optional[jsii.Number]:
            '''The maximum bitrate for RIST, RTP, and RTP-FEC streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxbitrate
            '''
            result = self._values.get("max_bitrate")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def max_latency(self) -> typing.Optional[jsii.Number]:
            '''The maximum latency in milliseconds for a RIST or Zixi-based source.

            :default: - 2000

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-maxlatency
            '''
            result = self._values.get("max_latency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def min_latency(self) -> typing.Optional[jsii.Number]:
            '''The minimum latency in milliseconds for SRT-based streams.

            In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.

            :default: - 2000

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-minlatency
            '''
            result = self._values.get("min_latency")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def protocol(self) -> typing.Optional[builtins.str]:
            '''The protocol that is used by the source.

            AWS CloudFormation does not currently support CDI or ST 2110 JPEG XS source protocols.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-protocol
            '''
            result = self._values.get("protocol")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sender_control_port(self) -> typing.Optional[jsii.Number]:
            '''The port that the flow uses to send outbound requests to initiate connection with the sender.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sendercontrolport
            '''
            result = self._values.get("sender_control_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def sender_ip_address(self) -> typing.Optional[builtins.str]:
            '''The IP address that the flow communicates with to initiate connection with the sender.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-senderipaddress
            '''
            result = self._values.get("sender_ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the source.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcearn
            '''
            result = self._values.get("source_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_ingest_port(self) -> typing.Optional[builtins.str]:
            '''The port that the flow listens on for incoming content.

            If the protocol of the source is Zixi, the port must be set to 2088.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourceingestport
            '''
            result = self._values.get("source_ingest_port")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_listener_address(self) -> typing.Optional[builtins.str]:
            '''Source IP or domain name for SRT-caller protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcelisteneraddress
            '''
            result = self._values.get("source_listener_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def source_listener_port(self) -> typing.Optional[jsii.Number]:
            '''Source port for SRT-caller protocol.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-sourcelistenerport
            '''
            result = self._values.get("source_listener_port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def stream_id(self) -> typing.Optional[builtins.str]:
            '''The stream ID that you want to use for the transport.

            This parameter applies only to Zixi-based streams.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-streamid
            '''
            result = self._values.get("stream_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface that the source content comes from.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def whitelist_cidr(self) -> typing.Optional[builtins.str]:
            '''The range of IP addresses that are allowed to contribute content to your source.

            Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-source.html#cfn-mediaconnect-flow-source-whitelistcidr
            '''
            result = self._values.get("whitelist_cidr")
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
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__866ca963188936c1dd8965fb722dc7f781261eab36e78ecdb20a9d41b146ef40)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flow-vpcinterfaceattachment.html#cfn-mediaconnect-flow-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnFlowEntitlement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowEntitlement",
):
    '''The AWS::MediaConnect::FlowEntitlement resource defines the permission that an AWS account grants to another AWS account to allow access to the content in a specific AWS Elemental MediaConnect flow.

    The content originator grants an entitlement to a specific AWS account (the subscriber). When an entitlement is granted, the subscriber can create a flow using the originator's flow as the source. Each flow can have up to 50 entitlements.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_entitlement = mediaconnect.CfnFlowEntitlement(self, "MyCfnFlowEntitlement",
            description="description",
            flow_arn="flowArn",
            name="name",
            subscribers=["subscribers"],
        
            # the properties below are optional
            data_transfer_subscriber_fee_percent=123,
            encryption=mediaconnect.CfnFlowEntitlement.EncryptionProperty(
                algorithm="algorithm",
                role_arn="roleArn",
        
                # the properties below are optional
                constant_initialization_vector="constantInitializationVector",
                device_id="deviceId",
                key_type="keyType",
                region="region",
                resource_id="resourceId",
                secret_arn="secretArn",
                url="url"
            ),
            entitlement_status="entitlementStatus"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        flow_arn: builtins.str,
        name: builtins.str,
        subscribers: typing.Sequence[builtins.str],
        data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlowEntitlement.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the entitlement. This description appears only on the MediaConnect console and is not visible outside of the current AWS account.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name of the entitlement. This value must be unique within the current flow.
        :param subscribers: The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
        :param data_transfer_subscriber_fee_percent: The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for. Default: - 0
        :param encryption: The type of encryption that MediaConnect will use on the output that is associated with the entitlement.
        :param entitlement_status: An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17ecd85086df3a96cb74577c3e3a831ea91a89b617bcd18f7684fd357569ebd4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowEntitlementProps(
            description=description,
            flow_arn=flow_arn,
            name=name,
            subscribers=subscribers,
            data_transfer_subscriber_fee_percent=data_transfer_subscriber_fee_percent,
            encryption=encryption,
            entitlement_status=entitlement_status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc2981b84449358974725cfa5726c974127f55b1d0ed785957f4a1db25fbaf37)
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
            type_hints = typing.get_type_hints(_typecheckingstub__2fa54f5d69b72c125e54c71a8aa7a22fc52b087370efdb65ece275ef52b680b8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrEntitlementArn")
    def attr_entitlement_arn(self) -> builtins.str:
        '''The entitlement ARN.

        :cloudformationAttribute: EntitlementArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrEntitlementArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the entitlement.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba5eab3ebe302e351ac5ac0d66029f44599f4749a72395abe65585f0a24955a1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e11924d752092913d6e2606c9cde4c9d3a676e93d2cdf59e192e9e6c293bfe35)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the entitlement.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__916ef20a18bd718e63e193a4bfe9a47ef0a3fa7c7d6eb6a74a9f583ad5834eb2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="subscribers")
    def subscribers(self) -> typing.List[builtins.str]:
        '''The AWS account IDs that you want to share your content with.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "subscribers"))

    @subscribers.setter
    def subscribers(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ffb421693bf57958756eb013d4d8a721597fcd6b5c4d155ff98a2fc1ee7f4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscribers", value)

    @builtins.property
    @jsii.member(jsii_name="dataTransferSubscriberFeePercent")
    def data_transfer_subscriber_fee_percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "dataTransferSubscriberFeePercent"))

    @data_transfer_subscriber_fee_percent.setter
    def data_transfer_subscriber_fee_percent(
        self,
        value: typing.Optional[jsii.Number],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__440918e3c472d10f8c3846eeee04790645912cc1f354752fcf74610c24a956dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dataTransferSubscriberFeePercent", value)

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowEntitlement.EncryptionProperty"]]:
        '''The type of encryption that MediaConnect will use on the output that is associated with the entitlement.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowEntitlement.EncryptionProperty"]], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowEntitlement.EncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e186a635819e5284e2d58b4d8e7f8c317f8ef3dcaf08d3a66dfe0e4f1b061e89)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="entitlementStatus")
    def entitlement_status(self) -> typing.Optional[builtins.str]:
        '''An indication of whether the new entitlement should be enabled or disabled as soon as it is created.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entitlementStatus"))

    @entitlement_status.setter
    def entitlement_status(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdf1b9a179db4ad86ff23860586d83012068ae1abfca84e5defe29f68556a89a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlementStatus", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowEntitlement.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "algorithm": "algorithm",
            "role_arn": "roleArn",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            algorithm: builtins.str,
            role_arn: builtins.str,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the encryption of the flow.

            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param role_arn: The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
            :param device_id: The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"
            :param region: The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param resource_id: An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.
            :param url: The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlowEntitlement.EncryptionProperty(
                    algorithm="algorithm",
                    role_arn="roleArn",
                
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a86c4f896040118c2a4fab234e2a7101cc609c650cf5a8c91892db664909f050)
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "algorithm": algorithm,
                "role_arn": role_arn,
            }
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def algorithm(self) -> builtins.str:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            assert result is not None, "Required property 'algorithm' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content.

            This parameter is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''The value of one of the devices that you configured with your digital rights management (DRM) platform key provider.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the API Gateway proxy endpoint was created in.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''An identifier for the content.

            The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL from the API Gateway proxy that you set up to talk to your key server.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowentitlement-encryption.html#cfn-mediaconnect-flowentitlement-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowEntitlementProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "flow_arn": "flowArn",
        "name": "name",
        "subscribers": "subscribers",
        "data_transfer_subscriber_fee_percent": "dataTransferSubscriberFeePercent",
        "encryption": "encryption",
        "entitlement_status": "entitlementStatus",
    },
)
class CfnFlowEntitlementProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        flow_arn: builtins.str,
        name: builtins.str,
        subscribers: typing.Sequence[builtins.str],
        data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
        encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowEntitlement.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_status: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowEntitlement``.

        :param description: A description of the entitlement. This description appears only on the MediaConnect console and is not visible outside of the current AWS account.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name of the entitlement. This value must be unique within the current flow.
        :param subscribers: The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.
        :param data_transfer_subscriber_fee_percent: The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for. Default: - 0
        :param encryption: The type of encryption that MediaConnect will use on the output that is associated with the entitlement.
        :param entitlement_status: An indication of whether the new entitlement should be enabled or disabled as soon as it is created. If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_entitlement_props = mediaconnect.CfnFlowEntitlementProps(
                description="description",
                flow_arn="flowArn",
                name="name",
                subscribers=["subscribers"],
            
                # the properties below are optional
                data_transfer_subscriber_fee_percent=123,
                encryption=mediaconnect.CfnFlowEntitlement.EncryptionProperty(
                    algorithm="algorithm",
                    role_arn="roleArn",
            
                    # the properties below are optional
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                ),
                entitlement_status="entitlementStatus"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7f5911f6dc55c43d6c5bdd5da77a5eb8fb59e8f8418ae5a951a5e0f015b5055)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument subscribers", value=subscribers, expected_type=type_hints["subscribers"])
            check_type(argname="argument data_transfer_subscriber_fee_percent", value=data_transfer_subscriber_fee_percent, expected_type=type_hints["data_transfer_subscriber_fee_percent"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument entitlement_status", value=entitlement_status, expected_type=type_hints["entitlement_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "flow_arn": flow_arn,
            "name": name,
            "subscribers": subscribers,
        }
        if data_transfer_subscriber_fee_percent is not None:
            self._values["data_transfer_subscriber_fee_percent"] = data_transfer_subscriber_fee_percent
        if encryption is not None:
            self._values["encryption"] = encryption
        if entitlement_status is not None:
            self._values["entitlement_status"] = entitlement_status

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the entitlement.

        This description appears only on the MediaConnect console and is not visible outside of the current AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the entitlement.

        This value must be unique within the current flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscribers(self) -> typing.List[builtins.str]:
        '''The AWS account IDs that you want to share your content with.

        The receiving accounts (subscribers) will be allowed to create their own flows using your content as the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-subscribers
        '''
        result = self._values.get("subscribers")
        assert result is not None, "Required property 'subscribers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def data_transfer_subscriber_fee_percent(self) -> typing.Optional[jsii.Number]:
        '''The percentage of the entitlement data transfer fee that you want the subscriber to be responsible for.

        :default: - 0

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-datatransfersubscriberfeepercent
        '''
        result = self._values.get("data_transfer_subscriber_fee_percent")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowEntitlement.EncryptionProperty]]:
        '''The type of encryption that MediaConnect will use on the output that is associated with the entitlement.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowEntitlement.EncryptionProperty]], result)

    @builtins.property
    def entitlement_status(self) -> typing.Optional[builtins.str]:
        '''An indication of whether the new entitlement should be enabled or disabled as soon as it is created.

        If you don’t specify the entitlementStatus field in your request, MediaConnect sets it to ENABLED.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowentitlement.html#cfn-mediaconnect-flowentitlement-entitlementstatus
        '''
        result = self._values.get("entitlement_status")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowEntitlementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFlowOutput(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput",
):
    '''The AWS::MediaConnect::FlowOutput resource defines the destination address, protocol, and port that AWS Elemental MediaConnect sends the ingested video to.

    Each flow can have up to 50 outputs. An output can have the same protocol or a different protocol from the source. The following protocols are supported: RIST, RTP, RTP-FEC, SRT-listener, SRT-caller, Zixi pull, Zixi push, and Fujitsu-QoS. CDI and ST 2110 JPEG XS protocols are not currently supported by AWS CloudFormation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_output = mediaconnect.CfnFlowOutput(self, "MyCfnFlowOutput",
            flow_arn="flowArn",
            protocol="protocol",
        
            # the properties below are optional
            cidr_allow_list=["cidrAllowList"],
            description="description",
            destination="destination",
            encryption=mediaconnect.CfnFlowOutput.EncryptionProperty(
                role_arn="roleArn",
                secret_arn="secretArn",
        
                # the properties below are optional
                algorithm="algorithm",
                key_type="keyType"
            ),
            max_latency=123,
            min_latency=123,
            name="name",
            port=123,
            remote_id="remoteId",
            smoothing_latency=123,
            stream_id="streamId",
            vpc_interface_attachment=mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty(
                vpc_interface_name="vpcInterfaceName"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        flow_arn: builtins.str,
        protocol: builtins.str,
        cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        destination: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlowOutput.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        remote_id: typing.Optional[builtins.str] = None,
        smoothing_latency: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlowOutput.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param flow_arn: The Amazon Resource Name (ARN) of the flow this output is attached to.
        :param protocol: The protocol to use for the output.
        :param cidr_allow_list: The range of IP addresses that are allowed to initiate output requests to this flow. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param description: A description of the output. This description is not visible outside of the current AWS account even if the account grants entitlements to other accounts.
        :param destination: The IP address where you want to send the output.
        :param encryption: The encryption credentials that you want to use for the output.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams.
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
        :param name: The name of the VPC interface.
        :param port: The port to use when MediaConnect distributes content to the output.
        :param remote_id: The identifier that is assigned to the Zixi receiver. This parameter applies only to outputs that use Zixi pull.
        :param smoothing_latency: The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_attachment: The VPC interface that you want to send your output to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__50a855342b002f2aaf180af2a85e45ce23346b4a5b582c00ee1a8474e9dd9bf1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowOutputProps(
            flow_arn=flow_arn,
            protocol=protocol,
            cidr_allow_list=cidr_allow_list,
            description=description,
            destination=destination,
            encryption=encryption,
            max_latency=max_latency,
            min_latency=min_latency,
            name=name,
            port=port,
            remote_id=remote_id,
            smoothing_latency=smoothing_latency,
            stream_id=stream_id,
            vpc_interface_attachment=vpc_interface_attachment,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99f7a6ea2f782501225c570fc34c141a4efdd391bd9340c51c8bd1b59b8a807b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8fe52bb8ba629a55d8f6926893cc92e58afb2df918e7d368aeddb04aa5bb1855)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrOutputArn")
    def attr_output_arn(self) -> builtins.str:
        '''The ARN of the output.

        :cloudformationAttribute: OutputArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrOutputArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow this output is attached to.'''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b58a8b918485e48f2bd2cbf5a806a141e4d5ae34f2cf830391b88420333717)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> builtins.str:
        '''The protocol to use for the output.'''
        return typing.cast(builtins.str, jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9a09f7a6d8ae99d18b6e3bb11284fa5b865ca2146c5efb07536e593ee9a05bc7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="cidrAllowList")
    def cidr_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The range of IP addresses that are allowed to initiate output requests to this flow.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "cidrAllowList"))

    @cidr_allow_list.setter
    def cidr_allow_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07f3031245a81d1c4e02553eaeb7fc62e38e625e4d2cfe7b7ff3ecce31ce6ef5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrAllowList", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04edd4c6554768eef7ffa49af9bf9fdec351390bdef1d2d14056f7b2afa9b477)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="destination")
    def destination(self) -> typing.Optional[builtins.str]:
        '''The IP address where you want to send the output.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destination"))

    @destination.setter
    def destination(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b3f2991cc0ce7b9368aefbf86c1373167ce7a90e3225db313dd6d35540907285)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destination", value)

    @builtins.property
    @jsii.member(jsii_name="encryption")
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowOutput.EncryptionProperty"]]:
        '''The encryption credentials that you want to use for the output.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowOutput.EncryptionProperty"]], jsii.get(self, "encryption"))

    @encryption.setter
    def encryption(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowOutput.EncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__78a7a7ea75faea54e857e52b24703069f4dd92643ca1173b27422c3504eee69b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encryption", value)

    @builtins.property
    @jsii.member(jsii_name="maxLatency")
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLatency"))

    @max_latency.setter
    def max_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9801fdc6b598fc4f2e913edc8984f374a7594553b0a1ef32ea0fa7be05bb61db)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLatency", value)

    @builtins.property
    @jsii.member(jsii_name="minLatency")
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLatency"))

    @min_latency.setter
    def min_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddb7401a37f3ff6ff7dc25a56db1a28806074c96fc3f42a6bd90cc4feab9b693)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLatency", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the VPC interface.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07b750df47b88518fdf7bc5d1baec396797cb9cc3a0c8bdc7742108d9c93c231)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="port")
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to use when MediaConnect distributes content to the output.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "port"))

    @port.setter
    def port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082204a6d2f259b91fea6a581b0aa8a534b0e447853734806818dfa91f967458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "port", value)

    @builtins.property
    @jsii.member(jsii_name="remoteId")
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that is assigned to the Zixi receiver.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "remoteId"))

    @remote_id.setter
    def remote_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0f19d4552e8cf70ccb26264cc49b216d391ddef580a3635679d644bda9f8dabf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "remoteId", value)

    @builtins.property
    @jsii.member(jsii_name="smoothingLatency")
    def smoothing_latency(self) -> typing.Optional[jsii.Number]:
        '''The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "smoothingLatency"))

    @smoothing_latency.setter
    def smoothing_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2a7c12acde851480773f720ab16362e6f6dd272465bbe84d6b60322c1bfd207d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "smoothingLatency", value)

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dadac9d58702681fe997f284efaad53e6d5af9dac998dd803277c6ed1ee2a381)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcInterfaceAttachment")
    def vpc_interface_attachment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]]:
        '''The VPC interface that you want to send your output to.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]], jsii.get(self, "vpcInterfaceAttachment"))

    @vpc_interface_attachment.setter
    def vpc_interface_attachment(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowOutput.VpcInterfaceAttachmentProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__65a3e058407bcf8bd6fa065c9fd3cd66a1c54e7edb3b48af25c7893fd72db21d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcInterfaceAttachment", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "secret_arn": "secretArn",
            "algorithm": "algorithm",
            "key_type": "keyType",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            secret_arn: builtins.str,
            algorithm: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the encryption of the flow.

            :param role_arn: The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.
            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlowOutput.EncryptionProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn",
                
                    # the properties below are optional
                    algorithm="algorithm",
                    key_type="keyType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__12ea6e5693abf5b0e777cf50bd86212ef7db4809c0713169b65c0d055bed2f19)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
                "secret_arn": secret_arn,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if key_type is not None:
                self._values["key_type"] = key_type

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def secret_arn(self) -> builtins.str:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            assert result is not None, "Required property 'secret_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-encryption.html#cfn-mediaconnect-flowoutput-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The VPC interface that you want to send your output to.

            :param vpc_interface_name: The name of the VPC interface that you want to send your output to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7072f99adeda4341a6581cacf2975b777cc5b063364d5416156250ca7f1e5619)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface that you want to send your output to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowoutput-vpcinterfaceattachment.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowOutputProps",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "protocol": "protocol",
        "cidr_allow_list": "cidrAllowList",
        "description": "description",
        "destination": "destination",
        "encryption": "encryption",
        "max_latency": "maxLatency",
        "min_latency": "minLatency",
        "name": "name",
        "port": "port",
        "remote_id": "remoteId",
        "smoothing_latency": "smoothingLatency",
        "stream_id": "streamId",
        "vpc_interface_attachment": "vpcInterfaceAttachment",
    },
)
class CfnFlowOutputProps:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        protocol: builtins.str,
        cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        description: typing.Optional[builtins.str] = None,
        destination: typing.Optional[builtins.str] = None,
        encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        name: typing.Optional[builtins.str] = None,
        port: typing.Optional[jsii.Number] = None,
        remote_id: typing.Optional[builtins.str] = None,
        smoothing_latency: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowOutput``.

        :param flow_arn: The Amazon Resource Name (ARN) of the flow this output is attached to.
        :param protocol: The protocol to use for the output.
        :param cidr_allow_list: The range of IP addresses that are allowed to initiate output requests to this flow. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param description: A description of the output. This description is not visible outside of the current AWS account even if the account grants entitlements to other accounts.
        :param destination: The IP address where you want to send the output.
        :param encryption: The encryption credentials that you want to use for the output.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams.
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.
        :param name: The name of the VPC interface.
        :param port: The port to use when MediaConnect distributes content to the output.
        :param remote_id: The identifier that is assigned to the Zixi receiver. This parameter applies only to outputs that use Zixi pull.
        :param smoothing_latency: The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_attachment: The VPC interface that you want to send your output to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_output_props = mediaconnect.CfnFlowOutputProps(
                flow_arn="flowArn",
                protocol="protocol",
            
                # the properties below are optional
                cidr_allow_list=["cidrAllowList"],
                description="description",
                destination="destination",
                encryption=mediaconnect.CfnFlowOutput.EncryptionProperty(
                    role_arn="roleArn",
                    secret_arn="secretArn",
            
                    # the properties below are optional
                    algorithm="algorithm",
                    key_type="keyType"
                ),
                max_latency=123,
                min_latency=123,
                name="name",
                port=123,
                remote_id="remoteId",
                smoothing_latency=123,
                stream_id="streamId",
                vpc_interface_attachment=mediaconnect.CfnFlowOutput.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__90cee4cbdefa91956af92950bb2bfd2da4fa4f982f439596444cda5251a2c34d)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument cidr_allow_list", value=cidr_allow_list, expected_type=type_hints["cidr_allow_list"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument encryption", value=encryption, expected_type=type_hints["encryption"])
            check_type(argname="argument max_latency", value=max_latency, expected_type=type_hints["max_latency"])
            check_type(argname="argument min_latency", value=min_latency, expected_type=type_hints["min_latency"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument remote_id", value=remote_id, expected_type=type_hints["remote_id"])
            check_type(argname="argument smoothing_latency", value=smoothing_latency, expected_type=type_hints["smoothing_latency"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument vpc_interface_attachment", value=vpc_interface_attachment, expected_type=type_hints["vpc_interface_attachment"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
            "protocol": protocol,
        }
        if cidr_allow_list is not None:
            self._values["cidr_allow_list"] = cidr_allow_list
        if description is not None:
            self._values["description"] = description
        if destination is not None:
            self._values["destination"] = destination
        if encryption is not None:
            self._values["encryption"] = encryption
        if max_latency is not None:
            self._values["max_latency"] = max_latency
        if min_latency is not None:
            self._values["min_latency"] = min_latency
        if name is not None:
            self._values["name"] = name
        if port is not None:
            self._values["port"] = port
        if remote_id is not None:
            self._values["remote_id"] = remote_id
        if smoothing_latency is not None:
            self._values["smoothing_latency"] = smoothing_latency
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if vpc_interface_attachment is not None:
            self._values["vpc_interface_attachment"] = vpc_interface_attachment

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow this output is attached to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protocol(self) -> builtins.str:
        '''The protocol to use for the output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-protocol
        '''
        result = self._values.get("protocol")
        assert result is not None, "Required property 'protocol' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def cidr_allow_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The range of IP addresses that are allowed to initiate output requests to this flow.

        Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-cidrallowlist
        '''
        result = self._values.get("cidr_allow_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the output.

        This description is not visible outside of the current AWS account even if the account grants entitlements to other accounts.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination(self) -> typing.Optional[builtins.str]:
        '''The IP address where you want to send the output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-destination
        '''
        result = self._values.get("destination")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.EncryptionProperty]]:
        '''The encryption credentials that you want to use for the output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-encryption
        '''
        result = self._values.get("encryption")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.EncryptionProperty]], result)

    @builtins.property
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.

        This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-maxlatency
        '''
        result = self._values.get("max_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.

        In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-minlatency
        '''
        result = self._values.get("min_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the VPC interface.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''The port to use when MediaConnect distributes content to the output.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-port
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def remote_id(self) -> typing.Optional[builtins.str]:
        '''The identifier that is assigned to the Zixi receiver.

        This parameter applies only to outputs that use Zixi pull.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-remoteid
        '''
        result = self._values.get("remote_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def smoothing_latency(self) -> typing.Optional[jsii.Number]:
        '''The smoothing latency in milliseconds for RIST, RTP, and RTP-FEC streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-smoothinglatency
        '''
        result = self._values.get("smoothing_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.

        This parameter applies only to Zixi and SRT caller-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_interface_attachment(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.VpcInterfaceAttachmentProperty]]:
        '''The VPC interface that you want to send your output to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowoutput.html#cfn-mediaconnect-flowoutput-vpcinterfaceattachment
        '''
        result = self._values.get("vpc_interface_attachment")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.VpcInterfaceAttachmentProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowOutputProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "source": "source",
        "availability_zone": "availabilityZone",
        "source_failover_config": "sourceFailoverConfig",
    },
)
class CfnFlowProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
        availability_zone: typing.Optional[builtins.str] = None,
        source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlow``.

        :param name: The name of the flow.
        :param source: The settings for the source that you want to use for the new flow.
        :param availability_zone: The Availability Zone that you want to create the flow in. These options are limited to the Availability Zones within the current AWS Region.
        :param source_failover_config: The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_props = mediaconnect.CfnFlowProps(
                name="name",
                source=mediaconnect.CfnFlow.SourceProperty(
                    decryption=mediaconnect.CfnFlow.EncryptionProperty(
                        role_arn="roleArn",
            
                        # the properties below are optional
                        algorithm="algorithm",
                        constant_initialization_vector="constantInitializationVector",
                        device_id="deviceId",
                        key_type="keyType",
                        region="region",
                        resource_id="resourceId",
                        secret_arn="secretArn",
                        url="url"
                    ),
                    description="description",
                    entitlement_arn="entitlementArn",
                    gateway_bridge_source=mediaconnect.CfnFlow.GatewayBridgeSourceProperty(
                        bridge_arn="bridgeArn",
            
                        # the properties below are optional
                        vpc_interface_attachment=mediaconnect.CfnFlow.VpcInterfaceAttachmentProperty(
                            vpc_interface_name="vpcInterfaceName"
                        )
                    ),
                    ingest_ip="ingestIp",
                    ingest_port=123,
                    max_bitrate=123,
                    max_latency=123,
                    min_latency=123,
                    name="name",
                    protocol="protocol",
                    sender_control_port=123,
                    sender_ip_address="senderIpAddress",
                    source_arn="sourceArn",
                    source_ingest_port="sourceIngestPort",
                    source_listener_address="sourceListenerAddress",
                    source_listener_port=123,
                    stream_id="streamId",
                    vpc_interface_name="vpcInterfaceName",
                    whitelist_cidr="whitelistCidr"
                ),
            
                # the properties below are optional
                availability_zone="availabilityZone",
                source_failover_config=mediaconnect.CfnFlow.FailoverConfigProperty(
                    failover_mode="failoverMode",
                    recovery_window=123,
                    source_priority=mediaconnect.CfnFlow.SourcePriorityProperty(
                        primary_source="primarySource"
                    ),
                    state="state"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__32a16a7697723a7ef816aaa9d297ca08cd44085f922995184f8bfdfde65f0c24)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
            check_type(argname="argument source_failover_config", value=source_failover_config, expected_type=type_hints["source_failover_config"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "source": source,
        }
        if availability_zone is not None:
            self._values["availability_zone"] = availability_zone
        if source_failover_config is not None:
            self._values["source_failover_config"] = source_failover_config

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> typing.Union[_IResolvable_da3f097b, CfnFlow.SourceProperty]:
        '''The settings for the source that you want to use for the new flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-source
        '''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFlow.SourceProperty], result)

    @builtins.property
    def availability_zone(self) -> typing.Optional[builtins.str]:
        '''The Availability Zone that you want to create the flow in.

        These options are limited to the Availability Zones within the current AWS Region.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-availabilityzone
        '''
        result = self._values.get("availability_zone")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_failover_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.FailoverConfigProperty]]:
        '''The settings for source failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flow.html#cfn-mediaconnect-flow-sourcefailoverconfig
        '''
        result = self._values.get("source_failover_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.FailoverConfigProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFlowSource(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource",
):
    '''The AWS::MediaConnect::FlowSource resource is used to add additional sources to an existing flow.

    Adding an additional source requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. A source is the external video content that includes configuration information (encryption and source type) and a network address. Each flow has at least one source. A standard source comes from a source other than another AWS Elemental MediaConnect flow, such as an on-premises encoder.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_source = mediaconnect.CfnFlowSource(self, "MyCfnFlowSource",
            description="description",
            name="name",
        
            # the properties below are optional
            decryption=mediaconnect.CfnFlowSource.EncryptionProperty(
                role_arn="roleArn",
        
                # the properties below are optional
                algorithm="algorithm",
                constant_initialization_vector="constantInitializationVector",
                device_id="deviceId",
                key_type="keyType",
                region="region",
                resource_id="resourceId",
                secret_arn="secretArn",
                url="url"
            ),
            entitlement_arn="entitlementArn",
            flow_arn="flowArn",
            gateway_bridge_source=mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty(
                bridge_arn="bridgeArn",
        
                # the properties below are optional
                vpc_interface_attachment=mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            ),
            ingest_port=123,
            max_bitrate=123,
            max_latency=123,
            min_latency=123,
            protocol="protocol",
            sender_control_port=123,
            sender_ip_address="senderIpAddress",
            source_listener_address="sourceListenerAddress",
            source_listener_port=123,
            stream_id="streamId",
            vpc_interface_name="vpcInterfaceName",
            whitelist_cidr="whitelistCidr"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        description: builtins.str,
        name: builtins.str,
        decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlowSource.EncryptionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_arn: typing.Optional[builtins.str] = None,
        flow_arn: typing.Optional[builtins.str] = None,
        gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlowSource.GatewayBridgeSourceProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ingest_port: typing.Optional[jsii.Number] = None,
        max_bitrate: typing.Optional[jsii.Number] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        sender_control_port: typing.Optional[jsii.Number] = None,
        sender_ip_address: typing.Optional[builtins.str] = None,
        source_listener_address: typing.Optional[builtins.str] = None,
        source_listener_port: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_name: typing.Optional[builtins.str] = None,
        whitelist_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param description: A description of the source. This description is not visible outside of the current AWS account.
        :param name: The name of the source.
        :param decryption: The type of encryption that is used on the content ingested from the source.
        :param entitlement_arn: The ARN of the entitlement that allows you to subscribe to the flow. The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow this source is connected to. The flow must have Failover enabled to add an additional source.
        :param gateway_bridge_source: The source configuration for cloud flows receiving a stream from a bridge.
        :param ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
        :param max_bitrate: The maximum bitrate for RIST, RTP, and RTP-FEC streams.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams. Default: - 2000
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. Default: - 2000
        :param protocol: The protocol that the source uses to deliver the content to MediaConnect. Adding additional sources to an existing flow requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. Only the following protocols support failover: Zixi-push, RTP-FEC, RTP, RIST and SRT protocols. If you use failover with SRT caller or listener, the ``FailoverMode`` property must be set to ``FAILOVER`` . The ``FailoverMode`` property is found in the ``FailoverConfig`` resource of the same flow ARN you used for the source's ``FlowArn`` property. SRT caller/listener does not support merge mode failover.
        :param sender_control_port: The port that the flow uses to send outbound requests to initiate connection with the sender.
        :param sender_ip_address: The IP address that the flow communicates with to initiate connection with the sender.
        :param source_listener_address: Source IP or domain name for SRT-caller protocol.
        :param source_listener_port: Source port for SRT-caller protocol.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_name: The name of the VPC interface that you want to send your output to.
        :param whitelist_cidr: The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f14359cee01f3506467d65b7510ab8dfc45bad9d560a39ede9f196eb193c6d3f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowSourceProps(
            description=description,
            name=name,
            decryption=decryption,
            entitlement_arn=entitlement_arn,
            flow_arn=flow_arn,
            gateway_bridge_source=gateway_bridge_source,
            ingest_port=ingest_port,
            max_bitrate=max_bitrate,
            max_latency=max_latency,
            min_latency=min_latency,
            protocol=protocol,
            sender_control_port=sender_control_port,
            sender_ip_address=sender_ip_address,
            source_listener_address=source_listener_address,
            source_listener_port=source_listener_port,
            stream_id=stream_id,
            vpc_interface_name=vpc_interface_name,
            whitelist_cidr=whitelist_cidr,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db3fd76f8220dae1a8772091086f599345d67d89097d2f85b9307e60f66eebda)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8852c4ff5ee8f7563716bed6f284156dda285971d2136f38033b85a389bd073b)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrIngestIp")
    def attr_ingest_ip(self) -> builtins.str:
        '''The IP address that the flow listens on for incoming content.

        :cloudformationAttribute: IngestIp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrIngestIp"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceArn")
    def attr_source_arn(self) -> builtins.str:
        '''The ARN of the source.

        :cloudformationAttribute: SourceArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceArn"))

    @builtins.property
    @jsii.member(jsii_name="attrSourceIngestPort")
    def attr_source_ingest_port(self) -> builtins.str:
        '''The port that the flow listens on for incoming content.

        If the protocol of the source is Zixi, the port must be set to 2088.

        :cloudformationAttribute: SourceIngestPort
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrSourceIngestPort"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        '''A description of the source.'''
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__169574c8d258397d0753838843606fa3a6f2792dbfbe9f805a3263cc2ce8bf99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the source.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56248647932d6154f5cc0ea3f1df2a2bb25f298ef25872b32e9b4dd6f8e0ff07)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="decryption")
    def decryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.EncryptionProperty"]]:
        '''The type of encryption that is used on the content ingested from the source.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.EncryptionProperty"]], jsii.get(self, "decryption"))

    @decryption.setter
    def decryption(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.EncryptionProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__713d2beba8d5285adfd07ee3f7ca737392fb89294806031a6cc288bb72c8f180)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "decryption", value)

    @builtins.property
    @jsii.member(jsii_name="entitlementArn")
    def entitlement_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the entitlement that allows you to subscribe to the flow.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "entitlementArn"))

    @entitlement_arn.setter
    def entitlement_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ba0fab964dfcf99d0e38ef04172e971ea1753fa1d98e88458675e4386302dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "entitlementArn", value)

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the flow this source is connected to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a393333c9ad7ce002f047c125d9ee3348efa283a66d9def5950529184e3be294)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value)

    @builtins.property
    @jsii.member(jsii_name="gatewayBridgeSource")
    def gateway_bridge_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.GatewayBridgeSourceProperty"]]:
        '''The source configuration for cloud flows receiving a stream from a bridge.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.GatewayBridgeSourceProperty"]], jsii.get(self, "gatewayBridgeSource"))

    @gateway_bridge_source.setter
    def gateway_bridge_source(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.GatewayBridgeSourceProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5cf895711559ebd9f3d9816442bc2258d4ed6f493bb32badf0ea76f038dd16a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "gatewayBridgeSource", value)

    @builtins.property
    @jsii.member(jsii_name="ingestPort")
    def ingest_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow listens on for incoming content.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "ingestPort"))

    @ingest_port.setter
    def ingest_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8065f994df3b6b1f35a330146835da3506ebb87915688c1139a725cf72b5f618)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ingestPort", value)

    @builtins.property
    @jsii.member(jsii_name="maxBitrate")
    def max_bitrate(self) -> typing.Optional[jsii.Number]:
        '''The maximum bitrate for RIST, RTP, and RTP-FEC streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBitrate"))

    @max_bitrate.setter
    def max_bitrate(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e362dd143dad56909dafd2e42bfcb4f36d21b914a7b90872305a01bec7758a1f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBitrate", value)

    @builtins.property
    @jsii.member(jsii_name="maxLatency")
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxLatency"))

    @max_latency.setter
    def max_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__59ebbbae1ffe64a0b2ace0c589cfc271c5cf5155fb97c05e5866f905264c33c3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxLatency", value)

    @builtins.property
    @jsii.member(jsii_name="minLatency")
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "minLatency"))

    @min_latency.setter
    def min_latency(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__99ef8a4669e860fa72d8e2f4dc3ad3fe414a8d53d7156d84af37cde5562fb88d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "minLatency", value)

    @builtins.property
    @jsii.member(jsii_name="protocol")
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol that the source uses to deliver the content to MediaConnect.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "protocol"))

    @protocol.setter
    def protocol(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb57175f10a9dd5a4e263ec48354d53559458e760a13228af2bc8b2d5a738add)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protocol", value)

    @builtins.property
    @jsii.member(jsii_name="senderControlPort")
    def sender_control_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow uses to send outbound requests to initiate connection with the sender.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "senderControlPort"))

    @sender_control_port.setter
    def sender_control_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2cb25d08779ab67d6811a557f48cd15bde00000d84c5ba57f8165f13a3f72f99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "senderControlPort", value)

    @builtins.property
    @jsii.member(jsii_name="senderIpAddress")
    def sender_ip_address(self) -> typing.Optional[builtins.str]:
        '''The IP address that the flow communicates with to initiate connection with the sender.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "senderIpAddress"))

    @sender_ip_address.setter
    def sender_ip_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce59a08878045e4b8bc6ff139a2307a1a5d3d8b55ad67c907a140517d9fdee00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "senderIpAddress", value)

    @builtins.property
    @jsii.member(jsii_name="sourceListenerAddress")
    def source_listener_address(self) -> typing.Optional[builtins.str]:
        '''Source IP or domain name for SRT-caller protocol.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceListenerAddress"))

    @source_listener_address.setter
    def source_listener_address(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f71f744022b312b3b4bc69179b8e4ce2cdb7fdeb46c179d7c72e3db30ac42e6c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceListenerAddress", value)

    @builtins.property
    @jsii.member(jsii_name="sourceListenerPort")
    def source_listener_port(self) -> typing.Optional[jsii.Number]:
        '''Source port for SRT-caller protocol.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "sourceListenerPort"))

    @source_listener_port.setter
    def source_listener_port(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fc08edbf9070870e3f4ff641570a5fbe7bd92875ead1c75b9697e32c94084f4f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceListenerPort", value)

    @builtins.property
    @jsii.member(jsii_name="streamId")
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "streamId"))

    @stream_id.setter
    def stream_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f3b58b86420e937edcb73256eccae2a94f77b56863e967c6b79430f30f5ae00)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "streamId", value)

    @builtins.property
    @jsii.member(jsii_name="vpcInterfaceName")
    def vpc_interface_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VPC interface that you want to send your output to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "vpcInterfaceName"))

    @vpc_interface_name.setter
    def vpc_interface_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aaca9be06dd26e302844cbceb849d87c083af662bbe659afe5a1819fd6ac9f7b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcInterfaceName", value)

    @builtins.property
    @jsii.member(jsii_name="whitelistCidr")
    def whitelist_cidr(self) -> typing.Optional[builtins.str]:
        '''The range of IP addresses that are allowed to contribute content to your source.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "whitelistCidr"))

    @whitelist_cidr.setter
    def whitelist_cidr(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45499d5b323bea3d710e7e2165d62c80e1951ab949967a5138abfc7e37f673dc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "whitelistCidr", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource.EncryptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "role_arn": "roleArn",
            "algorithm": "algorithm",
            "constant_initialization_vector": "constantInitializationVector",
            "device_id": "deviceId",
            "key_type": "keyType",
            "region": "region",
            "resource_id": "resourceId",
            "secret_arn": "secretArn",
            "url": "url",
        },
    )
    class EncryptionProperty:
        def __init__(
            self,
            *,
            role_arn: builtins.str,
            algorithm: typing.Optional[builtins.str] = None,
            constant_initialization_vector: typing.Optional[builtins.str] = None,
            device_id: typing.Optional[builtins.str] = None,
            key_type: typing.Optional[builtins.str] = None,
            region: typing.Optional[builtins.str] = None,
            resource_id: typing.Optional[builtins.str] = None,
            secret_arn: typing.Optional[builtins.str] = None,
            url: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Information about the encryption of the flow.

            :param role_arn: The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).
            :param algorithm: The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256). If you are using SPEKE or SRT-password encryption, this property must be left blank.
            :param constant_initialization_vector: A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content. This parameter is not valid for static key encryption.
            :param device_id: The value of one of the devices that you configured with your digital rights management (DRM) platform key provider. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param key_type: The type of key that is used for the encryption. If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` . Default: - "static-key"
            :param region: The AWS Region that the API Gateway proxy endpoint was created in. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param resource_id: An identifier for the content. The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.
            :param secret_arn: The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.
            :param url: The URL from the API Gateway proxy that you set up to talk to your key server. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                encryption_property = mediaconnect.CfnFlowSource.EncryptionProperty(
                    role_arn="roleArn",
                
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bc2e1b7c07a7a0aadaba7f4f2e0a0214eedc45460e5f4d6b8a4e1af4b33ff561)
                check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
                check_type(argname="argument algorithm", value=algorithm, expected_type=type_hints["algorithm"])
                check_type(argname="argument constant_initialization_vector", value=constant_initialization_vector, expected_type=type_hints["constant_initialization_vector"])
                check_type(argname="argument device_id", value=device_id, expected_type=type_hints["device_id"])
                check_type(argname="argument key_type", value=key_type, expected_type=type_hints["key_type"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument secret_arn", value=secret_arn, expected_type=type_hints["secret_arn"])
                check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "role_arn": role_arn,
            }
            if algorithm is not None:
                self._values["algorithm"] = algorithm
            if constant_initialization_vector is not None:
                self._values["constant_initialization_vector"] = constant_initialization_vector
            if device_id is not None:
                self._values["device_id"] = device_id
            if key_type is not None:
                self._values["key_type"] = key_type
            if region is not None:
                self._values["region"] = region
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if secret_arn is not None:
                self._values["secret_arn"] = secret_arn
            if url is not None:
                self._values["url"] = url

        @builtins.property
        def role_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the role that you created during setup (when you set up MediaConnect as a trusted entity).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-rolearn
            '''
            result = self._values.get("role_arn")
            assert result is not None, "Required property 'role_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def algorithm(self) -> typing.Optional[builtins.str]:
            '''The type of algorithm that is used for static key encryption (such as aes128, aes192, or aes256).

            If you are using SPEKE or SRT-password encryption, this property must be left blank.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-algorithm
            '''
            result = self._values.get("algorithm")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def constant_initialization_vector(self) -> typing.Optional[builtins.str]:
            '''A 128-bit, 16-byte hex value represented by a 32-character string, to be used with the key for encrypting content.

            This parameter is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-constantinitializationvector
            '''
            result = self._values.get("constant_initialization_vector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def device_id(self) -> typing.Optional[builtins.str]:
            '''The value of one of the devices that you configured with your digital rights management (DRM) platform key provider.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-deviceid
            '''
            result = self._values.get("device_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def key_type(self) -> typing.Optional[builtins.str]:
            '''The type of key that is used for the encryption.

            If you don't specify a ``keyType`` value, the service uses the default setting ( ``static-key`` ). Valid key types are: ``static-key`` , ``speke`` , and ``srt-password`` .

            :default: - "static-key"

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-keytype
            '''
            result = self._values.get("key_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region that the API Gateway proxy endpoint was created in.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_id(self) -> typing.Optional[builtins.str]:
            '''An identifier for the content.

            The service sends this value to the key server to identify the current endpoint. The resource ID is also known as the content ID. This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def secret_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the secret that you created in AWS Secrets Manager to store the encryption key.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-secretarn
            '''
            result = self._values.get("secret_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def url(self) -> typing.Optional[builtins.str]:
            '''The URL from the API Gateway proxy that you set up to talk to your key server.

            This parameter is required for SPEKE encryption and is not valid for static key encryption.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-encryption.html#cfn-mediaconnect-flowsource-encryption-url
            '''
            result = self._values.get("url")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EncryptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bridge_arn": "bridgeArn",
            "vpc_interface_attachment": "vpcInterfaceAttachment",
        },
    )
    class GatewayBridgeSourceProperty:
        def __init__(
            self,
            *,
            bridge_arn: builtins.str,
            vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFlowSource.VpcInterfaceAttachmentProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The source configuration for cloud flows receiving a stream from a bridge.

            :param bridge_arn: The ARN of the bridge feeding this flow.
            :param vpc_interface_attachment: The settings for attaching a VPC interface to an resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                gateway_bridge_source_property = mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
                
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__30ed56e867002e6d71070cfe3db49514b39a97f4380a7b126282076647a88405)
                check_type(argname="argument bridge_arn", value=bridge_arn, expected_type=type_hints["bridge_arn"])
                check_type(argname="argument vpc_interface_attachment", value=vpc_interface_attachment, expected_type=type_hints["vpc_interface_attachment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bridge_arn": bridge_arn,
            }
            if vpc_interface_attachment is not None:
                self._values["vpc_interface_attachment"] = vpc_interface_attachment

        @builtins.property
        def bridge_arn(self) -> builtins.str:
            '''The ARN of the bridge feeding this flow.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html#cfn-mediaconnect-flowsource-gatewaybridgesource-bridgearn
            '''
            result = self._values.get("bridge_arn")
            assert result is not None, "Required property 'bridge_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_interface_attachment(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.VpcInterfaceAttachmentProperty"]]:
            '''The settings for attaching a VPC interface to an resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-gatewaybridgesource.html#cfn-mediaconnect-flowsource-gatewaybridgesource-vpcinterfaceattachment
            '''
            result = self._values.get("vpc_interface_attachment")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFlowSource.VpcInterfaceAttachmentProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayBridgeSourceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_interface_name": "vpcInterfaceName"},
    )
    class VpcInterfaceAttachmentProperty:
        def __init__(
            self,
            *,
            vpc_interface_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The settings for attaching a VPC interface to an resource.

            :param vpc_interface_name: The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                vpc_interface_attachment_property = mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                    vpc_interface_name="vpcInterfaceName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__91f29aa73d1270b98bef9297507fc5368a6213455c4fab06ce82317542ccbecb)
                check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if vpc_interface_name is not None:
                self._values["vpc_interface_name"] = vpc_interface_name

        @builtins.property
        def vpc_interface_name(self) -> typing.Optional[builtins.str]:
            '''The name of the VPC interface to use for this resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-flowsource-vpcinterfaceattachment.html#cfn-mediaconnect-flowsource-vpcinterfaceattachment-vpcinterfacename
            '''
            result = self._values.get("vpc_interface_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VpcInterfaceAttachmentProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowSourceProps",
    jsii_struct_bases=[],
    name_mapping={
        "description": "description",
        "name": "name",
        "decryption": "decryption",
        "entitlement_arn": "entitlementArn",
        "flow_arn": "flowArn",
        "gateway_bridge_source": "gatewayBridgeSource",
        "ingest_port": "ingestPort",
        "max_bitrate": "maxBitrate",
        "max_latency": "maxLatency",
        "min_latency": "minLatency",
        "protocol": "protocol",
        "sender_control_port": "senderControlPort",
        "sender_ip_address": "senderIpAddress",
        "source_listener_address": "sourceListenerAddress",
        "source_listener_port": "sourceListenerPort",
        "stream_id": "streamId",
        "vpc_interface_name": "vpcInterfaceName",
        "whitelist_cidr": "whitelistCidr",
    },
)
class CfnFlowSourceProps:
    def __init__(
        self,
        *,
        description: builtins.str,
        name: builtins.str,
        decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        entitlement_arn: typing.Optional[builtins.str] = None,
        flow_arn: typing.Optional[builtins.str] = None,
        gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        ingest_port: typing.Optional[jsii.Number] = None,
        max_bitrate: typing.Optional[jsii.Number] = None,
        max_latency: typing.Optional[jsii.Number] = None,
        min_latency: typing.Optional[jsii.Number] = None,
        protocol: typing.Optional[builtins.str] = None,
        sender_control_port: typing.Optional[jsii.Number] = None,
        sender_ip_address: typing.Optional[builtins.str] = None,
        source_listener_address: typing.Optional[builtins.str] = None,
        source_listener_port: typing.Optional[jsii.Number] = None,
        stream_id: typing.Optional[builtins.str] = None,
        vpc_interface_name: typing.Optional[builtins.str] = None,
        whitelist_cidr: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFlowSource``.

        :param description: A description of the source. This description is not visible outside of the current AWS account.
        :param name: The name of the source.
        :param decryption: The type of encryption that is used on the content ingested from the source.
        :param entitlement_arn: The ARN of the entitlement that allows you to subscribe to the flow. The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow.
        :param flow_arn: The Amazon Resource Name (ARN) of the flow this source is connected to. The flow must have Failover enabled to add an additional source.
        :param gateway_bridge_source: The source configuration for cloud flows receiving a stream from a bridge.
        :param ingest_port: The port that the flow listens on for incoming content. If the protocol of the source is Zixi, the port must be set to 2088.
        :param max_bitrate: The maximum bitrate for RIST, RTP, and RTP-FEC streams.
        :param max_latency: The maximum latency in milliseconds. This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams. Default: - 2000
        :param min_latency: The minimum latency in milliseconds for SRT-based streams. In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency. Default: - 2000
        :param protocol: The protocol that the source uses to deliver the content to MediaConnect. Adding additional sources to an existing flow requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. Only the following protocols support failover: Zixi-push, RTP-FEC, RTP, RIST and SRT protocols. If you use failover with SRT caller or listener, the ``FailoverMode`` property must be set to ``FAILOVER`` . The ``FailoverMode`` property is found in the ``FailoverConfig`` resource of the same flow ARN you used for the source's ``FlowArn`` property. SRT caller/listener does not support merge mode failover.
        :param sender_control_port: The port that the flow uses to send outbound requests to initiate connection with the sender.
        :param sender_ip_address: The IP address that the flow communicates with to initiate connection with the sender.
        :param source_listener_address: Source IP or domain name for SRT-caller protocol.
        :param source_listener_port: Source port for SRT-caller protocol.
        :param stream_id: The stream ID that you want to use for this transport. This parameter applies only to Zixi and SRT caller-based streams.
        :param vpc_interface_name: The name of the VPC interface that you want to send your output to.
        :param whitelist_cidr: The range of IP addresses that are allowed to contribute content to your source. Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_source_props = mediaconnect.CfnFlowSourceProps(
                description="description",
                name="name",
            
                # the properties below are optional
                decryption=mediaconnect.CfnFlowSource.EncryptionProperty(
                    role_arn="roleArn",
            
                    # the properties below are optional
                    algorithm="algorithm",
                    constant_initialization_vector="constantInitializationVector",
                    device_id="deviceId",
                    key_type="keyType",
                    region="region",
                    resource_id="resourceId",
                    secret_arn="secretArn",
                    url="url"
                ),
                entitlement_arn="entitlementArn",
                flow_arn="flowArn",
                gateway_bridge_source=mediaconnect.CfnFlowSource.GatewayBridgeSourceProperty(
                    bridge_arn="bridgeArn",
            
                    # the properties below are optional
                    vpc_interface_attachment=mediaconnect.CfnFlowSource.VpcInterfaceAttachmentProperty(
                        vpc_interface_name="vpcInterfaceName"
                    )
                ),
                ingest_port=123,
                max_bitrate=123,
                max_latency=123,
                min_latency=123,
                protocol="protocol",
                sender_control_port=123,
                sender_ip_address="senderIpAddress",
                source_listener_address="sourceListenerAddress",
                source_listener_port=123,
                stream_id="streamId",
                vpc_interface_name="vpcInterfaceName",
                whitelist_cidr="whitelistCidr"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dd2a850713cccb402475afd88e4c523840081ad6429c6abf35e564ea3f27ca1)
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument decryption", value=decryption, expected_type=type_hints["decryption"])
            check_type(argname="argument entitlement_arn", value=entitlement_arn, expected_type=type_hints["entitlement_arn"])
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument gateway_bridge_source", value=gateway_bridge_source, expected_type=type_hints["gateway_bridge_source"])
            check_type(argname="argument ingest_port", value=ingest_port, expected_type=type_hints["ingest_port"])
            check_type(argname="argument max_bitrate", value=max_bitrate, expected_type=type_hints["max_bitrate"])
            check_type(argname="argument max_latency", value=max_latency, expected_type=type_hints["max_latency"])
            check_type(argname="argument min_latency", value=min_latency, expected_type=type_hints["min_latency"])
            check_type(argname="argument protocol", value=protocol, expected_type=type_hints["protocol"])
            check_type(argname="argument sender_control_port", value=sender_control_port, expected_type=type_hints["sender_control_port"])
            check_type(argname="argument sender_ip_address", value=sender_ip_address, expected_type=type_hints["sender_ip_address"])
            check_type(argname="argument source_listener_address", value=source_listener_address, expected_type=type_hints["source_listener_address"])
            check_type(argname="argument source_listener_port", value=source_listener_port, expected_type=type_hints["source_listener_port"])
            check_type(argname="argument stream_id", value=stream_id, expected_type=type_hints["stream_id"])
            check_type(argname="argument vpc_interface_name", value=vpc_interface_name, expected_type=type_hints["vpc_interface_name"])
            check_type(argname="argument whitelist_cidr", value=whitelist_cidr, expected_type=type_hints["whitelist_cidr"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "description": description,
            "name": name,
        }
        if decryption is not None:
            self._values["decryption"] = decryption
        if entitlement_arn is not None:
            self._values["entitlement_arn"] = entitlement_arn
        if flow_arn is not None:
            self._values["flow_arn"] = flow_arn
        if gateway_bridge_source is not None:
            self._values["gateway_bridge_source"] = gateway_bridge_source
        if ingest_port is not None:
            self._values["ingest_port"] = ingest_port
        if max_bitrate is not None:
            self._values["max_bitrate"] = max_bitrate
        if max_latency is not None:
            self._values["max_latency"] = max_latency
        if min_latency is not None:
            self._values["min_latency"] = min_latency
        if protocol is not None:
            self._values["protocol"] = protocol
        if sender_control_port is not None:
            self._values["sender_control_port"] = sender_control_port
        if sender_ip_address is not None:
            self._values["sender_ip_address"] = sender_ip_address
        if source_listener_address is not None:
            self._values["source_listener_address"] = source_listener_address
        if source_listener_port is not None:
            self._values["source_listener_port"] = source_listener_port
        if stream_id is not None:
            self._values["stream_id"] = stream_id
        if vpc_interface_name is not None:
            self._values["vpc_interface_name"] = vpc_interface_name
        if whitelist_cidr is not None:
            self._values["whitelist_cidr"] = whitelist_cidr

    @builtins.property
    def description(self) -> builtins.str:
        '''A description of the source.

        This description is not visible outside of the current AWS account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-description
        '''
        result = self._values.get("description")
        assert result is not None, "Required property 'description' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def decryption(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.EncryptionProperty]]:
        '''The type of encryption that is used on the content ingested from the source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-decryption
        '''
        result = self._values.get("decryption")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.EncryptionProperty]], result)

    @builtins.property
    def entitlement_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the entitlement that allows you to subscribe to the flow.

        The entitlement is set by the content originator, and the ARN is generated as part of the originator's flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-entitlementarn
        '''
        result = self._values.get("entitlement_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def flow_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the flow this source is connected to.

        The flow must have Failover enabled to add an additional source.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-flowarn
        '''
        result = self._values.get("flow_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def gateway_bridge_source(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.GatewayBridgeSourceProperty]]:
        '''The source configuration for cloud flows receiving a stream from a bridge.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-gatewaybridgesource
        '''
        result = self._values.get("gateway_bridge_source")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.GatewayBridgeSourceProperty]], result)

    @builtins.property
    def ingest_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow listens on for incoming content.

        If the protocol of the source is Zixi, the port must be set to 2088.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-ingestport
        '''
        result = self._values.get("ingest_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_bitrate(self) -> typing.Optional[jsii.Number]:
        '''The maximum bitrate for RIST, RTP, and RTP-FEC streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxbitrate
        '''
        result = self._values.get("max_bitrate")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def max_latency(self) -> typing.Optional[jsii.Number]:
        '''The maximum latency in milliseconds.

        This parameter applies only to RIST-based, Zixi-based, and Fujitsu-based streams.

        :default: - 2000

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-maxlatency
        '''
        result = self._values.get("max_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def min_latency(self) -> typing.Optional[jsii.Number]:
        '''The minimum latency in milliseconds for SRT-based streams.

        In streams that use the SRT protocol, this value that you set on your MediaConnect source or output represents the minimal potential latency of that connection. The latency of the stream is set to the highest number between the sender’s minimum latency and the receiver’s minimum latency.

        :default: - 2000

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-minlatency
        '''
        result = self._values.get("min_latency")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def protocol(self) -> typing.Optional[builtins.str]:
        '''The protocol that the source uses to deliver the content to MediaConnect.

        Adding additional sources to an existing flow requires Failover to be enabled. When you enable Failover, the additional source must use the same protocol as the existing source. Only the following protocols support failover: Zixi-push, RTP-FEC, RTP, RIST and SRT protocols.

        If you use failover with SRT caller or listener, the ``FailoverMode`` property must be set to ``FAILOVER`` . The ``FailoverMode`` property is found in the ``FailoverConfig`` resource of the same flow ARN you used for the source's ``FlowArn`` property. SRT caller/listener does not support merge mode failover.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-protocol
        '''
        result = self._values.get("protocol")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def sender_control_port(self) -> typing.Optional[jsii.Number]:
        '''The port that the flow uses to send outbound requests to initiate connection with the sender.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sendercontrolport
        '''
        result = self._values.get("sender_control_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def sender_ip_address(self) -> typing.Optional[builtins.str]:
        '''The IP address that the flow communicates with to initiate connection with the sender.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-senderipaddress
        '''
        result = self._values.get("sender_ip_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_listener_address(self) -> typing.Optional[builtins.str]:
        '''Source IP or domain name for SRT-caller protocol.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sourcelisteneraddress
        '''
        result = self._values.get("source_listener_address")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def source_listener_port(self) -> typing.Optional[jsii.Number]:
        '''Source port for SRT-caller protocol.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-sourcelistenerport
        '''
        result = self._values.get("source_listener_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def stream_id(self) -> typing.Optional[builtins.str]:
        '''The stream ID that you want to use for this transport.

        This parameter applies only to Zixi and SRT caller-based streams.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-streamid
        '''
        result = self._values.get("stream_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc_interface_name(self) -> typing.Optional[builtins.str]:
        '''The name of the VPC interface that you want to send your output to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-vpcinterfacename
        '''
        result = self._values.get("vpc_interface_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def whitelist_cidr(self) -> typing.Optional[builtins.str]:
        '''The range of IP addresses that are allowed to contribute content to your source.

        Format the IP addresses as a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowsource.html#cfn-mediaconnect-flowsource-whitelistcidr
        '''
        result = self._values.get("whitelist_cidr")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowSourceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFlowVpcInterface(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowVpcInterface",
):
    '''The AWS::MediaConnect::FlowVpcInterface resource is a connection between your AWS Elemental MediaConnect flow and a virtual private cloud (VPC) that you created using the Amazon Virtual Private Cloud service.

    To avoid streaming your content over the public internet, you can add up to two VPC interfaces to your flow and use those connections to transfer content between your VPC and MediaConnect.

    You can update an existing flow to add a VPC interface. If you haven’t created the flow yet, you must create the flow with a temporary standard source by doing the following:

    - Use CloudFormation to create a flow with a standard source that uses to the flow’s public IP address.
    - Use CloudFormation to create a VPC interface to add to this flow. This can also be done as part of the previous step.
    - After CloudFormation has created the flow and the VPC interface, update the source to point to the VPC interface that you created.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_flow_vpc_interface = mediaconnect.CfnFlowVpcInterface(self, "MyCfnFlowVpcInterface",
            flow_arn="flowArn",
            name="name",
            role_arn="roleArn",
            security_group_ids=["securityGroupIds"],
            subnet_id="subnetId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        flow_arn: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name of the VPC Interface. This value must be unique within the current flow.
        :param role_arn: The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.
        :param security_group_ids: The VPC security groups that you want MediaConnect to use for your VPC configuration. You must include at least one security group in the request.
        :param subnet_id: The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dbdfc221c828cffa79a57d6d84dccb050776de58319678209806d7b3bc310582)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFlowVpcInterfaceProps(
            flow_arn=flow_arn,
            name=name,
            role_arn=role_arn,
            security_group_ids=security_group_ids,
            subnet_id=subnet_id,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2669da051110c0f17f8e796d79785f21a3eedb15f26aad564f80d786fc0b5008)
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
            type_hints = typing.get_type_hints(_typecheckingstub__bb4bbb0359f95aef0014b12311830a206a9476a44d94de97d750a09771a603ae)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrNetworkInterfaceIds")
    def attr_network_interface_ids(self) -> typing.List[builtins.str]:
        '''The IDs of the network interfaces that MediaConnect created in your account.

        :cloudformationAttribute: NetworkInterfaceIds
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNetworkInterfaceIds"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="flowArn")
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.'''
        return typing.cast(builtins.str, jsii.get(self, "flowArn"))

    @flow_arn.setter
    def flow_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__01b2ebce5fcf204059015d9ab2acd7dd1255fb422e85ba46d8372e7ed14634e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flowArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the VPC Interface.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__315756aca1be9462393133e8a1bd030c6830be9cd62201141209ba92bca00733)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d1a6f274a5840002030ca9431469bb3346277b4320449fb605700060689db4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="securityGroupIds")
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The VPC security groups that you want MediaConnect to use for your VPC configuration.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "securityGroupIds"))

    @security_group_ids.setter
    def security_group_ids(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22fe25e82013a9b0baddbe815abf51918a6107457c49b594041bb09b37e6db29)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityGroupIds", value)

    @builtins.property
    @jsii.member(jsii_name="subnetId")
    def subnet_id(self) -> builtins.str:
        '''The subnet IDs that you want to use for your VPC interface.'''
        return typing.cast(builtins.str, jsii.get(self, "subnetId"))

    @subnet_id.setter
    def subnet_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__21ff66cbd4857ab742f4461a355254e9a8da4cf04f8543fbb07ab7e6bde77b87)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subnetId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnFlowVpcInterfaceProps",
    jsii_struct_bases=[],
    name_mapping={
        "flow_arn": "flowArn",
        "name": "name",
        "role_arn": "roleArn",
        "security_group_ids": "securityGroupIds",
        "subnet_id": "subnetId",
    },
)
class CfnFlowVpcInterfaceProps:
    def __init__(
        self,
        *,
        flow_arn: builtins.str,
        name: builtins.str,
        role_arn: builtins.str,
        security_group_ids: typing.Sequence[builtins.str],
        subnet_id: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnFlowVpcInterface``.

        :param flow_arn: The Amazon Resource Name (ARN) of the flow.
        :param name: The name of the VPC Interface. This value must be unique within the current flow.
        :param role_arn: The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.
        :param security_group_ids: The VPC security groups that you want MediaConnect to use for your VPC configuration. You must include at least one security group in the request.
        :param subnet_id: The subnet IDs that you want to use for your VPC interface. A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block. The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_flow_vpc_interface_props = mediaconnect.CfnFlowVpcInterfaceProps(
                flow_arn="flowArn",
                name="name",
                role_arn="roleArn",
                security_group_ids=["securityGroupIds"],
                subnet_id="subnetId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4407e3345806447ad15e49eb19ee87fc76290919c1ac77d7b46df8daf4909410)
            check_type(argname="argument flow_arn", value=flow_arn, expected_type=type_hints["flow_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument security_group_ids", value=security_group_ids, expected_type=type_hints["security_group_ids"])
            check_type(argname="argument subnet_id", value=subnet_id, expected_type=type_hints["subnet_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flow_arn": flow_arn,
            "name": name,
            "role_arn": role_arn,
            "security_group_ids": security_group_ids,
            "subnet_id": subnet_id,
        }

    @builtins.property
    def flow_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-flowarn
        '''
        result = self._values.get("flow_arn")
        assert result is not None, "Required property 'flow_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the VPC Interface.

        This value must be unique within the current flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the role that you created when you set up MediaConnect as a trusted service.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def security_group_ids(self) -> typing.List[builtins.str]:
        '''The VPC security groups that you want MediaConnect to use for your VPC configuration.

        You must include at least one security group in the request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-securitygroupids
        '''
        result = self._values.get("security_group_ids")
        assert result is not None, "Required property 'security_group_ids' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def subnet_id(self) -> builtins.str:
        '''The subnet IDs that you want to use for your VPC interface.

        A range of IP addresses in your VPC. When you create your VPC, you specify a range of IPv4 addresses for the VPC in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16. This is the primary CIDR block for your VPC. When you create a subnet for your VPC, you specify the CIDR block for the subnet, which is a subset of the VPC CIDR block.

        The subnets that you use across all VPC interfaces on the flow must be in the same Availability Zone as the flow.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-flowvpcinterface.html#cfn-mediaconnect-flowvpcinterface-subnetid
        '''
        result = self._values.get("subnet_id")
        assert result is not None, "Required property 'subnet_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFlowVpcInterfaceProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnGateway(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnGateway",
):
    '''The AWS::MediaConnect::Gateway resource is used to create a new gateway.

    AWS Elemental MediaConnect Gateway is a feature of MediaConnect that allows the deployment of on-premises resources for transporting live video to and from the AWS Cloud. MediaConnect Gateway allows you to contribute live video to the AWS Cloud from on-premises hardware, as well as distribute live video from the AWS Cloud to your local data center.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_mediaconnect as mediaconnect
        
        cfn_gateway = mediaconnect.CfnGateway(self, "MyCfnGateway",
            egress_cidr_blocks=["egressCidrBlocks"],
            name="name",
            networks=[mediaconnect.CfnGateway.GatewayNetworkProperty(
                cidr_block="cidrBlock",
                name="name"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        egress_cidr_blocks: typing.Sequence[builtins.str],
        name: builtins.str,
        networks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnGateway.GatewayNetworkProperty", typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param egress_cidr_blocks: The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param name: The name of the gateway. This name can not be modified after the gateway is created.
        :param networks: The list of networks that you want to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a889ede67aac65e3ba7da8735ec09aa46c53edb047800db832cc8f049ee063d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnGatewayProps(
            egress_cidr_blocks=egress_cidr_blocks, name=name, networks=networks
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15b19201085d642ad5919470c92f83f2874346dacf31c924443c14fa4ce8557e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__309d2649c79792783a657ac296a1e3f1559ca3d115f8d29a00fcf51ab5b9eea1)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayArn")
    def attr_gateway_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the gateway.

        :cloudformationAttribute: GatewayArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayArn"))

    @builtins.property
    @jsii.member(jsii_name="attrGatewayState")
    def attr_gateway_state(self) -> builtins.str:
        '''The current state of the gateway.

        Possible values are: CREATING, ACTIVE, UPDATING, ERROR, DELETING, DELETED.

        :cloudformationAttribute: GatewayState
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrGatewayState"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="egressCidrBlocks")
    def egress_cidr_blocks(self) -> typing.List[builtins.str]:
        '''The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway.'''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "egressCidrBlocks"))

    @egress_cidr_blocks.setter
    def egress_cidr_blocks(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c756c6472ede1cbb1eb656c10e07629e0cf818e434b2e8f9c94de41e295b332e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "egressCidrBlocks", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the gateway.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f455f9a25731428a340c77bb14b2965a474f55740a64090450ee7dee16709ce)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="networks")
    def networks(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayNetworkProperty"]]]:
        '''The list of networks that you want to add.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayNetworkProperty"]]], jsii.get(self, "networks"))

    @networks.setter
    def networks(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnGateway.GatewayNetworkProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87886ff9eadfa80377e79911ce74141941af595ecff54249e0b94a2aa4f4fdb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "networks", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_mediaconnect.CfnGateway.GatewayNetworkProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr_block": "cidrBlock", "name": "name"},
    )
    class GatewayNetworkProperty:
        def __init__(self, *, cidr_block: builtins.str, name: builtins.str) -> None:
            '''The network settings for a gateway.

            :param cidr_block: A unique IP address range to use for this network. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
            :param name: The name of the network. This name is used to reference the network and must be unique among networks in this gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_mediaconnect as mediaconnect
                
                gateway_network_property = mediaconnect.CfnGateway.GatewayNetworkProperty(
                    cidr_block="cidrBlock",
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f67f020f764410bf45106fcabf15d8329d4bbbd3768cac4cd170ba1032378127)
                check_type(argname="argument cidr_block", value=cidr_block, expected_type=type_hints["cidr_block"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr_block": cidr_block,
                "name": name,
            }

        @builtins.property
        def cidr_block(self) -> builtins.str:
            '''A unique IP address range to use for this network.

            These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html#cfn-mediaconnect-gateway-gatewaynetwork-cidrblock
            '''
            result = self._values.get("cidr_block")
            assert result is not None, "Required property 'cidr_block' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the network.

            This name is used to reference the network and must be unique among networks in this gateway.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-mediaconnect-gateway-gatewaynetwork.html#cfn-mediaconnect-gateway-gatewaynetwork-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GatewayNetworkProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_mediaconnect.CfnGatewayProps",
    jsii_struct_bases=[],
    name_mapping={
        "egress_cidr_blocks": "egressCidrBlocks",
        "name": "name",
        "networks": "networks",
    },
)
class CfnGatewayProps:
    def __init__(
        self,
        *,
        egress_cidr_blocks: typing.Sequence[builtins.str],
        name: builtins.str,
        networks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayNetworkProperty, typing.Dict[builtins.str, typing.Any]]]]],
    ) -> None:
        '''Properties for defining a ``CfnGateway``.

        :param egress_cidr_blocks: The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway. These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.
        :param name: The name of the gateway. This name can not be modified after the gateway is created.
        :param networks: The list of networks that you want to add.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_mediaconnect as mediaconnect
            
            cfn_gateway_props = mediaconnect.CfnGatewayProps(
                egress_cidr_blocks=["egressCidrBlocks"],
                name="name",
                networks=[mediaconnect.CfnGateway.GatewayNetworkProperty(
                    cidr_block="cidrBlock",
                    name="name"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__87c57a9fbadb9701c4e8bd3f97f24fe63b6ebd3d8f830d826fedc59b0e40f450)
            check_type(argname="argument egress_cidr_blocks", value=egress_cidr_blocks, expected_type=type_hints["egress_cidr_blocks"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument networks", value=networks, expected_type=type_hints["networks"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "egress_cidr_blocks": egress_cidr_blocks,
            "name": name,
            "networks": networks,
        }

    @builtins.property
    def egress_cidr_blocks(self) -> typing.List[builtins.str]:
        '''The range of IP addresses that are allowed to contribute content or initiate output requests for flows communicating with this gateway.

        These IP addresses should be in the form of a Classless Inter-Domain Routing (CIDR) block; for example, 10.0.0.0/16.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-egresscidrblocks
        '''
        result = self._values.get("egress_cidr_blocks")
        assert result is not None, "Required property 'egress_cidr_blocks' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the gateway.

        This name can not be modified after the gateway is created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def networks(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayNetworkProperty]]]:
        '''The list of networks that you want to add.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-mediaconnect-gateway.html#cfn-mediaconnect-gateway-networks
        '''
        result = self._values.get("networks")
        assert result is not None, "Required property 'networks' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayNetworkProperty]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnGatewayProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBridge",
    "CfnBridgeOutput",
    "CfnBridgeOutputProps",
    "CfnBridgeProps",
    "CfnBridgeSource",
    "CfnBridgeSourceProps",
    "CfnFlow",
    "CfnFlowEntitlement",
    "CfnFlowEntitlementProps",
    "CfnFlowOutput",
    "CfnFlowOutputProps",
    "CfnFlowProps",
    "CfnFlowSource",
    "CfnFlowSourceProps",
    "CfnFlowVpcInterface",
    "CfnFlowVpcInterfaceProps",
    "CfnGateway",
    "CfnGatewayProps",
]

publication.publish()

def _typecheckingstub__21d1f093ae6c3ef104fbfbb93b13b3338230662ddb218fed6d74e5040acf931c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    placement_arn: builtins.str,
    sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    egress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.EgressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.IngressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeOutputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e83409273af3b66857452f9f32805fa3650ea56dd8bccf1a4cae459f1669317(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34788268cca3ef6b9f17b00e64981600b0697ff2af1a873da5b2521e55e8f627(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__897e5b31abf5fb8064d23feda8e8dab6abc8fc04b479fede8ec2f5a8f11283ae(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6c0d91a8143e25d3431f038cc493b72ff78caeb2aae6a8de25ef906162ed203(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c151228d22c29de1b22fb11c72513278ae8b19faf50c26128a49b5bb5cd8231e(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeSourceProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8744f4915b3da8a1fb0b28e71cdd2260912dbea385353bb4a2378a0dcf2e1a19(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.EgressGatewayBridgeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2370206c3aaeddbbe4f170d30b717ce583cd273a4a651e68abaf2042096869bf(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.IngressGatewayBridgeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f0f04e00fdc529449b6434bd02be499c861ae34a03215caf6afedaf59974ca0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBridge.BridgeOutputProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a1d3ccb8b1bf31380b43926b18329ad07b95b13cfd50c81dfdcb52ed4700194(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridge.FailoverConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c9a85716cc44ad0d338a783771f76c5420792553cd40338bc48069294fac934(
    *,
    flow_arn: builtins.str,
    name: builtins.str,
    flow_vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__621a738d7654729dd7b3374ce4f5872ae1b369d023ed93a125315923bc53acb5(
    *,
    ip_address: builtins.str,
    name: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    ttl: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1642b43f3173ebc33fe250c935a5af5006fe555caff2d5246139c99d6cfb0d9b(
    *,
    multicast_ip: builtins.str,
    name: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dff659c89b605c1b1a727af90c48784adba90b01104dfd2da4ea33b042b8e12f(
    *,
    network_output: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__048c12dd6c2d1c5e61292ef13f12e16c2c87cce382b5d57ada270cfd08a1b24d(
    *,
    flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b88384d6e7eaf984035fe7a0fba90d12833212086c785ad13a9117af87f05ec0(
    *,
    max_bitrate: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2344e6b90e667c45e503f080b931cc817ed70f01054abb50495f2670d204d2b3(
    *,
    failover_mode: builtins.str,
    source_priority: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.SourcePriorityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__167e9f3b8055cd05eb90612891a377cb4cde612ba7f0ec6b9e69f7d2df6ce8e6(
    *,
    max_bitrate: jsii.Number,
    max_outputs: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58ccd453e30991d345c7d1533308b0d3e5827af4b03a42b43534f313026666a0(
    *,
    primary_source: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7119bd5cac44e94824a018e0819faa64fdc04125060ad413d57b0a00d0a8066(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37400ec0d6ede2ac41f09e81db31275470bfb18f7999012a07d588a5abfc45e7(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    network_output: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeOutput.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb205f08441d39d8e1889501076cfae52006c266e0dcc55675d37bdd36eecce7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8dfc4c93ee2ec8174192f41cba8f3d6deeacc3ee4b3eeb41940e9f61c1b8c0a5(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__238bd53ec2ae6381eaaf2c652a080561d1722805471e9d898d9d8e2b66530295(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4567364d21ca9ebe1a2f33abcf1e7bc00c0f6b671c2062fd3c6766537faf1fa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78fe544a540a0346bab7b296adf77b0088521ed5104d3678ee517ee4d8b43eb1(
    value: typing.Union[_IResolvable_da3f097b, CfnBridgeOutput.BridgeNetworkOutputProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c8d614c4eaf3e7a9715a54c7d8f6d68001dfdd34bed46af49b236cf97208c5b(
    *,
    ip_address: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
    ttl: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96c246f60ce4e5ad45fa8b46aaba3a5dc86b8fbceb04cd700ed6ecc964f18f2a(
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    network_output: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeOutput.BridgeNetworkOutputProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__73e5019972892e93be93b465cdd4743483355d6d745af2863fcbd2ab360c88ef(
    *,
    name: builtins.str,
    placement_arn: builtins.str,
    sources: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]]],
    egress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.EgressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingress_gateway_bridge: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.IngressGatewayBridgeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    outputs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.BridgeOutputProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridge.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e36e10c04a0f01de7ebc0521a5800daea1daa62e3bd343704ff6e84525f6f408(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8ee6617fa681b5aaf625fc2493bb4ea5b5e578a01029bdd7ba2b8647be429130(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64ce37bd7d5055cf2fb388e369c965f5e01fd162753e68839b53dd0443911c4b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__28bb545b11a59b0c10f19770b49da21586071508bfbed47b6b137ab43e2aaa5d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__26ff480997cae96d755e2b7e83019229c27702f843cafce3fc5647020ec7d7a7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa9a2d6952ebe510d69e3877d36b01cb4f6aa83e11dfcf61576bdfaffa0dea74(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeFlowSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__afb1ff783738c431282bcaa0dec602d425b3f5a39195a1f65e4e683ba344caea(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnBridgeSource.BridgeNetworkSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bb9109e42561a117540865cd31be3adb19651461f90f2af2ac7c6ce75a0c13e(
    *,
    flow_arn: builtins.str,
    flow_vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93b2199f774afbb32a622ba44ca26954c8e46e149f1bc0836b1dda198de28020(
    *,
    multicast_ip: builtins.str,
    network_name: builtins.str,
    port: jsii.Number,
    protocol: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e6d9b48314e46735258c941180d8e92fa25af944c2b991fb6827ccc97fa800b4(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f2a15e5c2c97898000fd91706ed5ee02d0a7d5d31640d04f545d4db3c27ec23(
    *,
    bridge_arn: builtins.str,
    name: builtins.str,
    flow_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeFlowSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    network_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBridgeSource.BridgeNetworkSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3568a95be2a886825b3db731f10e2fdea8be142c554d1e2055d7e22f5e6a3991(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    availability_zone: typing.Optional[builtins.str] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3bf65a3dfd8c719cb8ba7cde45e0dc8693f2306db4dba4cd6da5e4727579cc7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8244ccdcee08a7984c185f2ee476300520ed80658ec1efcbcb9634a230a0687a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7b9dd07005f4a1ea040eea97dccca156a16f5e9f3f6686139fbd52108ac4c3b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__869299c75adeb5a7d478686f55b98acba18c279372a76486ab2c6231b1e54e54(
    value: typing.Union[_IResolvable_da3f097b, CfnFlow.SourceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843065332a6d7586586605a6ec8a2bd932a36dd6774052d60e5f9fd8e52c280c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9d7deae7edf526ef9a6af2e16b592ef198ecb0cc777d1c7d97f392933ad97ef6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlow.FailoverConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__023b62e8b380bcfa878c2a07568bc0d0f9912919827c329972ee2130250892b3(
    *,
    role_arn: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    device_id: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__60d936fe41cb44293e591fd7a9b89da19bc9fc2509d0dacf4ad7a22a54e1bae9(
    *,
    failover_mode: typing.Optional[builtins.str] = None,
    recovery_window: typing.Optional[jsii.Number] = None,
    source_priority: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourcePriorityProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    state: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__00bf15dc37f493c33d6b2109cfa6283d2bb14bdc23b0ae4fd75a67ca60084ea8(
    *,
    bridge_arn: builtins.str,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a502d8c706596e3abd881dc963357d969893e22e8d25e78085445e09c58ac78b(
    *,
    primary_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c35ebd36bb52715c021bc299f222a377254ec8a3bd90d9c933fbefcac2bdf0c(
    *,
    decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    entitlement_arn: typing.Optional[builtins.str] = None,
    gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingest_ip: typing.Optional[builtins.str] = None,
    ingest_port: typing.Optional[jsii.Number] = None,
    max_bitrate: typing.Optional[jsii.Number] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    protocol: typing.Optional[builtins.str] = None,
    sender_control_port: typing.Optional[jsii.Number] = None,
    sender_ip_address: typing.Optional[builtins.str] = None,
    source_arn: typing.Optional[builtins.str] = None,
    source_ingest_port: typing.Optional[builtins.str] = None,
    source_listener_address: typing.Optional[builtins.str] = None,
    source_listener_port: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_name: typing.Optional[builtins.str] = None,
    whitelist_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__866ca963188936c1dd8965fb722dc7f781261eab36e78ecdb20a9d41b146ef40(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17ecd85086df3a96cb74577c3e3a831ea91a89b617bcd18f7684fd357569ebd4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    flow_arn: builtins.str,
    name: builtins.str,
    subscribers: typing.Sequence[builtins.str],
    data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowEntitlement.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc2981b84449358974725cfa5726c974127f55b1d0ed785957f4a1db25fbaf37(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fa54f5d69b72c125e54c71a8aa7a22fc52b087370efdb65ece275ef52b680b8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba5eab3ebe302e351ac5ac0d66029f44599f4749a72395abe65585f0a24955a1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e11924d752092913d6e2606c9cde4c9d3a676e93d2cdf59e192e9e6c293bfe35(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__916ef20a18bd718e63e193a4bfe9a47ef0a3fa7c7d6eb6a74a9f583ad5834eb2(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ffb421693bf57958756eb013d4d8a721597fcd6b5c4d155ff98a2fc1ee7f4e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__440918e3c472d10f8c3846eeee04790645912cc1f354752fcf74610c24a956dc(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e186a635819e5284e2d58b4d8e7f8c317f8ef3dcaf08d3a66dfe0e4f1b061e89(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowEntitlement.EncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdf1b9a179db4ad86ff23860586d83012068ae1abfca84e5defe29f68556a89a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a86c4f896040118c2a4fab234e2a7101cc609c650cf5a8c91892db664909f050(
    *,
    algorithm: builtins.str,
    role_arn: builtins.str,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    device_id: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7f5911f6dc55c43d6c5bdd5da77a5eb8fb59e8f8418ae5a951a5e0f015b5055(
    *,
    description: builtins.str,
    flow_arn: builtins.str,
    name: builtins.str,
    subscribers: typing.Sequence[builtins.str],
    data_transfer_subscriber_fee_percent: typing.Optional[jsii.Number] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowEntitlement.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_status: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__50a855342b002f2aaf180af2a85e45ce23346b4a5b582c00ee1a8474e9dd9bf1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    flow_arn: builtins.str,
    protocol: builtins.str,
    cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    destination: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    remote_id: typing.Optional[builtins.str] = None,
    smoothing_latency: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99f7a6ea2f782501225c570fc34c141a4efdd391bd9340c51c8bd1b59b8a807b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe52bb8ba629a55d8f6926893cc92e58afb2df918e7d368aeddb04aa5bb1855(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b58a8b918485e48f2bd2cbf5a806a141e4d5ae34f2cf830391b88420333717(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9a09f7a6d8ae99d18b6e3bb11284fa5b865ca2146c5efb07536e593ee9a05bc7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07f3031245a81d1c4e02553eaeb7fc62e38e625e4d2cfe7b7ff3ecce31ce6ef5(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04edd4c6554768eef7ffa49af9bf9fdec351390bdef1d2d14056f7b2afa9b477(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b3f2991cc0ce7b9368aefbf86c1373167ce7a90e3225db313dd6d35540907285(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__78a7a7ea75faea54e857e52b24703069f4dd92643ca1173b27422c3504eee69b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.EncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9801fdc6b598fc4f2e913edc8984f374a7594553b0a1ef32ea0fa7be05bb61db(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddb7401a37f3ff6ff7dc25a56db1a28806074c96fc3f42a6bd90cc4feab9b693(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07b750df47b88518fdf7bc5d1baec396797cb9cc3a0c8bdc7742108d9c93c231(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082204a6d2f259b91fea6a581b0aa8a534b0e447853734806818dfa91f967458(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f19d4552e8cf70ccb26264cc49b216d391ddef580a3635679d644bda9f8dabf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2a7c12acde851480773f720ab16362e6f6dd272465bbe84d6b60322c1bfd207d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dadac9d58702681fe997f284efaad53e6d5af9dac998dd803277c6ed1ee2a381(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__65a3e058407bcf8bd6fa065c9fd3cd66a1c54e7edb3b48af25c7893fd72db21d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowOutput.VpcInterfaceAttachmentProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__12ea6e5693abf5b0e777cf50bd86212ef7db4809c0713169b65c0d055bed2f19(
    *,
    role_arn: builtins.str,
    secret_arn: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7072f99adeda4341a6581cacf2975b777cc5b063364d5416156250ca7f1e5619(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__90cee4cbdefa91956af92950bb2bfd2da4fa4f982f439596444cda5251a2c34d(
    *,
    flow_arn: builtins.str,
    protocol: builtins.str,
    cidr_allow_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    description: typing.Optional[builtins.str] = None,
    destination: typing.Optional[builtins.str] = None,
    encryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    name: typing.Optional[builtins.str] = None,
    port: typing.Optional[jsii.Number] = None,
    remote_id: typing.Optional[builtins.str] = None,
    smoothing_latency: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowOutput.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__32a16a7697723a7ef816aaa9d297ca08cd44085f922995184f8bfdfde65f0c24(
    *,
    name: builtins.str,
    source: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.SourceProperty, typing.Dict[builtins.str, typing.Any]]],
    availability_zone: typing.Optional[builtins.str] = None,
    source_failover_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlow.FailoverConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f14359cee01f3506467d65b7510ab8dfc45bad9d560a39ede9f196eb193c6d3f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    description: builtins.str,
    name: builtins.str,
    decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_arn: typing.Optional[builtins.str] = None,
    flow_arn: typing.Optional[builtins.str] = None,
    gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingest_port: typing.Optional[jsii.Number] = None,
    max_bitrate: typing.Optional[jsii.Number] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    sender_control_port: typing.Optional[jsii.Number] = None,
    sender_ip_address: typing.Optional[builtins.str] = None,
    source_listener_address: typing.Optional[builtins.str] = None,
    source_listener_port: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_name: typing.Optional[builtins.str] = None,
    whitelist_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db3fd76f8220dae1a8772091086f599345d67d89097d2f85b9307e60f66eebda(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8852c4ff5ee8f7563716bed6f284156dda285971d2136f38033b85a389bd073b(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__169574c8d258397d0753838843606fa3a6f2792dbfbe9f805a3263cc2ce8bf99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56248647932d6154f5cc0ea3f1df2a2bb25f298ef25872b32e9b4dd6f8e0ff07(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__713d2beba8d5285adfd07ee3f7ca737392fb89294806031a6cc288bb72c8f180(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.EncryptionProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ba0fab964dfcf99d0e38ef04172e971ea1753fa1d98e88458675e4386302dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a393333c9ad7ce002f047c125d9ee3348efa283a66d9def5950529184e3be294(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5cf895711559ebd9f3d9816442bc2258d4ed6f493bb32badf0ea76f038dd16a(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnFlowSource.GatewayBridgeSourceProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8065f994df3b6b1f35a330146835da3506ebb87915688c1139a725cf72b5f618(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e362dd143dad56909dafd2e42bfcb4f36d21b914a7b90872305a01bec7758a1f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__59ebbbae1ffe64a0b2ace0c589cfc271c5cf5155fb97c05e5866f905264c33c3(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99ef8a4669e860fa72d8e2f4dc3ad3fe414a8d53d7156d84af37cde5562fb88d(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb57175f10a9dd5a4e263ec48354d53559458e760a13228af2bc8b2d5a738add(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2cb25d08779ab67d6811a557f48cd15bde00000d84c5ba57f8165f13a3f72f99(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce59a08878045e4b8bc6ff139a2307a1a5d3d8b55ad67c907a140517d9fdee00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f71f744022b312b3b4bc69179b8e4ce2cdb7fdeb46c179d7c72e3db30ac42e6c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc08edbf9070870e3f4ff641570a5fbe7bd92875ead1c75b9697e32c94084f4f(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f3b58b86420e937edcb73256eccae2a94f77b56863e967c6b79430f30f5ae00(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aaca9be06dd26e302844cbceb849d87c083af662bbe659afe5a1819fd6ac9f7b(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45499d5b323bea3d710e7e2165d62c80e1951ab949967a5138abfc7e37f673dc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bc2e1b7c07a7a0aadaba7f4f2e0a0214eedc45460e5f4d6b8a4e1af4b33ff561(
    *,
    role_arn: builtins.str,
    algorithm: typing.Optional[builtins.str] = None,
    constant_initialization_vector: typing.Optional[builtins.str] = None,
    device_id: typing.Optional[builtins.str] = None,
    key_type: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    resource_id: typing.Optional[builtins.str] = None,
    secret_arn: typing.Optional[builtins.str] = None,
    url: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__30ed56e867002e6d71070cfe3db49514b39a97f4380a7b126282076647a88405(
    *,
    bridge_arn: builtins.str,
    vpc_interface_attachment: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.VpcInterfaceAttachmentProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f29aa73d1270b98bef9297507fc5368a6213455c4fab06ce82317542ccbecb(
    *,
    vpc_interface_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dd2a850713cccb402475afd88e4c523840081ad6429c6abf35e564ea3f27ca1(
    *,
    description: builtins.str,
    name: builtins.str,
    decryption: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.EncryptionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    entitlement_arn: typing.Optional[builtins.str] = None,
    flow_arn: typing.Optional[builtins.str] = None,
    gateway_bridge_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFlowSource.GatewayBridgeSourceProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ingest_port: typing.Optional[jsii.Number] = None,
    max_bitrate: typing.Optional[jsii.Number] = None,
    max_latency: typing.Optional[jsii.Number] = None,
    min_latency: typing.Optional[jsii.Number] = None,
    protocol: typing.Optional[builtins.str] = None,
    sender_control_port: typing.Optional[jsii.Number] = None,
    sender_ip_address: typing.Optional[builtins.str] = None,
    source_listener_address: typing.Optional[builtins.str] = None,
    source_listener_port: typing.Optional[jsii.Number] = None,
    stream_id: typing.Optional[builtins.str] = None,
    vpc_interface_name: typing.Optional[builtins.str] = None,
    whitelist_cidr: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dbdfc221c828cffa79a57d6d84dccb050776de58319678209806d7b3bc310582(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    flow_arn: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2669da051110c0f17f8e796d79785f21a3eedb15f26aad564f80d786fc0b5008(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb4bbb0359f95aef0014b12311830a206a9476a44d94de97d750a09771a603ae(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__01b2ebce5fcf204059015d9ab2acd7dd1255fb422e85ba46d8372e7ed14634e7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__315756aca1be9462393133e8a1bd030c6830be9cd62201141209ba92bca00733(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__25d1a6f274a5840002030ca9431469bb3346277b4320449fb605700060689db4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22fe25e82013a9b0baddbe815abf51918a6107457c49b594041bb09b37e6db29(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__21ff66cbd4857ab742f4461a355254e9a8da4cf04f8543fbb07ab7e6bde77b87(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4407e3345806447ad15e49eb19ee87fc76290919c1ac77d7b46df8daf4909410(
    *,
    flow_arn: builtins.str,
    name: builtins.str,
    role_arn: builtins.str,
    security_group_ids: typing.Sequence[builtins.str],
    subnet_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4a889ede67aac65e3ba7da8735ec09aa46c53edb047800db832cc8f049ee063d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    egress_cidr_blocks: typing.Sequence[builtins.str],
    name: builtins.str,
    networks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayNetworkProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15b19201085d642ad5919470c92f83f2874346dacf31c924443c14fa4ce8557e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__309d2649c79792783a657ac296a1e3f1559ca3d115f8d29a00fcf51ab5b9eea1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c756c6472ede1cbb1eb656c10e07629e0cf818e434b2e8f9c94de41e295b332e(
    value: typing.List[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f455f9a25731428a340c77bb14b2965a474f55740a64090450ee7dee16709ce(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87886ff9eadfa80377e79911ce74141941af595ecff54249e0b94a2aa4f4fdb6(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnGateway.GatewayNetworkProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f67f020f764410bf45106fcabf15d8329d4bbbd3768cac4cd170ba1032378127(
    *,
    cidr_block: builtins.str,
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__87c57a9fbadb9701c4e8bd3f97f24fe63b6ebd3d8f830d826fedc59b0e40f450(
    *,
    egress_cidr_blocks: typing.Sequence[builtins.str],
    name: builtins.str,
    networks: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnGateway.GatewayNetworkProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass
