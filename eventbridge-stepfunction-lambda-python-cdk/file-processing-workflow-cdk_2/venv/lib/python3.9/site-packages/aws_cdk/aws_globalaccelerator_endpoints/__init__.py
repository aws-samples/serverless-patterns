'''
# Endpoints for AWS Global Accelerator

This library contains integration classes to reference endpoints in AWS
Global Accelerator. Instances of these classes should be passed to the
`endpointGroup.addEndpoint()` method.

See the README of the `aws-cdk-lib/aws-globalaccelerator` library for more information on
AWS Global Accelerator, and examples of all the integration classes available in
this module.
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

from ..aws_ec2 import CfnEIP as _CfnEIP_f7fb6536, IInstance as _IInstance_ab239e7c
from ..aws_elasticloadbalancingv2 import (
    IApplicationLoadBalancer as _IApplicationLoadBalancer_4cbd50ab,
    INetworkLoadBalancer as _INetworkLoadBalancer_96e17101,
)
from ..aws_globalaccelerator import IEndpoint as _IEndpoint_9ce24655


@jsii.implements(_IEndpoint_9ce24655)
class ApplicationLoadBalancerEndpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.ApplicationLoadBalancerEndpoint",
):
    '''Use an Application Load Balancer as a Global Accelerator Endpoint.

    :exampleMetadata: infused

    Example::

        # alb: elbv2.ApplicationLoadBalancer
        # listener: globalaccelerator.Listener
        
        
        listener.add_endpoint_group("Group",
            endpoints=[
                ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
                    weight=128,
                    preserve_client_ip=True
                )
            ]
        )
    '''

    def __init__(
        self,
        load_balancer: _IApplicationLoadBalancer_4cbd50ab,
        *,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param load_balancer: -
        :param preserve_client_ip: Forward the client IP address in an ``X-Forwarded-For`` header. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if available
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba4640acce1129555dd019374571778734d893a209c2784f062edff4221df6f1)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        options = ApplicationLoadBalancerEndpointOptions(
            preserve_client_ip=preserve_client_ip, weight=weight
        )

        jsii.create(self.__class__, self, [load_balancer, options])

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.ApplicationLoadBalancerEndpointOptions",
    jsii_struct_bases=[],
    name_mapping={"preserve_client_ip": "preserveClientIp", "weight": "weight"},
)
class ApplicationLoadBalancerEndpointOptions:
    def __init__(
        self,
        *,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for a ApplicationLoadBalancerEndpoint.

        :param preserve_client_ip: Forward the client IP address in an ``X-Forwarded-For`` header. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if available
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :exampleMetadata: infused

        Example::

            # alb: elbv2.ApplicationLoadBalancer
            # listener: globalaccelerator.Listener
            
            
            listener.add_endpoint_group("Group",
                endpoints=[
                    ga_endpoints.ApplicationLoadBalancerEndpoint(alb,
                        weight=128,
                        preserve_client_ip=True
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c0ac3083381dd6ab3fdb91d6359ab553b1b88dc7e082a30b6e898d5733adbc0)
            check_type(argname="argument preserve_client_ip", value=preserve_client_ip, expected_type=type_hints["preserve_client_ip"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preserve_client_ip is not None:
            self._values["preserve_client_ip"] = preserve_client_ip
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def preserve_client_ip(self) -> typing.Optional[builtins.bool]:
        '''Forward the client IP address in an ``X-Forwarded-For`` header.

        GlobalAccelerator will create Network Interfaces in your VPC in order
        to preserve the client IP address.

        Client IP address preservation is supported only in specific AWS Regions.
        See the GlobalAccelerator Developer Guide for a list.

        :default: true if available
        '''
        result = self._values.get("preserve_client_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Endpoint weight across all endpoints in the group.

        Must be a value between 0 and 255.

        :default: 128
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ApplicationLoadBalancerEndpointOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IEndpoint_9ce24655)
class CfnEipEndpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.CfnEipEndpoint",
):
    '''Use an EC2 Instance as a Global Accelerator Endpoint.

    :exampleMetadata: infused

    Example::

        # listener: globalaccelerator.Listener
        # eip: ec2.CfnEIP
        
        
        listener.add_endpoint_group("Group",
            endpoints=[
                ga_endpoints.CfnEipEndpoint(eip,
                    weight=128
                )
            ]
        )
    '''

    def __init__(
        self,
        eip: _CfnEIP_f7fb6536,
        *,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param eip: -
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea5231b8f6dbbebc7fcece999f2933e63d13dacdbd7d2bdc4b9c382b4aac06c7)
            check_type(argname="argument eip", value=eip, expected_type=type_hints["eip"])
        options = CfnEipEndpointProps(weight=weight)

        jsii.create(self.__class__, self, [eip, options])

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.CfnEipEndpointProps",
    jsii_struct_bases=[],
    name_mapping={"weight": "weight"},
)
class CfnEipEndpointProps:
    def __init__(self, *, weight: typing.Optional[jsii.Number] = None) -> None:
        '''Properties for a NetworkLoadBalancerEndpoint.

        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :exampleMetadata: infused

        Example::

            # listener: globalaccelerator.Listener
            # eip: ec2.CfnEIP
            
            
            listener.add_endpoint_group("Group",
                endpoints=[
                    ga_endpoints.CfnEipEndpoint(eip,
                        weight=128
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__325966af990f79d498fd30f2d9440803965b307292d612b47a1b6dbd862fb2ef)
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Endpoint weight across all endpoints in the group.

        Must be a value between 0 and 255.

        :default: 128
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEipEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IEndpoint_9ce24655)
class InstanceEndpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.InstanceEndpoint",
):
    '''Use an EC2 Instance as a Global Accelerator Endpoint.

    :exampleMetadata: infused

    Example::

        # listener: globalaccelerator.Listener
        # instance: ec2.Instance
        
        
        listener.add_endpoint_group("Group",
            endpoints=[
                ga_endpoints.InstanceEndpoint(instance,
                    weight=128,
                    preserve_client_ip=True
                )
            ]
        )
    '''

    def __init__(
        self,
        instance: _IInstance_ab239e7c,
        *,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param instance: -
        :param preserve_client_ip: Forward the client IP address. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if available
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c2cf290b2c92721fe0ccf29dedc01f3c274ef2f3250c08926449f729dd41260)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
        options = InstanceEndpointProps(
            preserve_client_ip=preserve_client_ip, weight=weight
        )

        jsii.create(self.__class__, self, [instance, options])

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.InstanceEndpointProps",
    jsii_struct_bases=[],
    name_mapping={"preserve_client_ip": "preserveClientIp", "weight": "weight"},
)
class InstanceEndpointProps:
    def __init__(
        self,
        *,
        preserve_client_ip: typing.Optional[builtins.bool] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for a NetworkLoadBalancerEndpoint.

        :param preserve_client_ip: Forward the client IP address. GlobalAccelerator will create Network Interfaces in your VPC in order to preserve the client IP address. Client IP address preservation is supported only in specific AWS Regions. See the GlobalAccelerator Developer Guide for a list. Default: true if available
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :exampleMetadata: infused

        Example::

            # listener: globalaccelerator.Listener
            # instance: ec2.Instance
            
            
            listener.add_endpoint_group("Group",
                endpoints=[
                    ga_endpoints.InstanceEndpoint(instance,
                        weight=128,
                        preserve_client_ip=True
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234a90a888e0bfaab2b608e4e2c1e1a69a9e87121c40a35a442f702755d1d047)
            check_type(argname="argument preserve_client_ip", value=preserve_client_ip, expected_type=type_hints["preserve_client_ip"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if preserve_client_ip is not None:
            self._values["preserve_client_ip"] = preserve_client_ip
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def preserve_client_ip(self) -> typing.Optional[builtins.bool]:
        '''Forward the client IP address.

        GlobalAccelerator will create Network Interfaces in your VPC in order
        to preserve the client IP address.

        Client IP address preservation is supported only in specific AWS Regions.
        See the GlobalAccelerator Developer Guide for a list.

        :default: true if available
        '''
        result = self._values.get("preserve_client_ip")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Endpoint weight across all endpoints in the group.

        Must be a value between 0 and 255.

        :default: 128
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "InstanceEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IEndpoint_9ce24655)
class NetworkLoadBalancerEndpoint(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.NetworkLoadBalancerEndpoint",
):
    '''Use a Network Load Balancer as a Global Accelerator Endpoint.

    :exampleMetadata: infused

    Example::

        # Create an Accelerator
        accelerator = globalaccelerator.Accelerator(self, "Accelerator")
        
        # Create a Listener
        listener = accelerator.add_listener("Listener",
            port_ranges=[globalaccelerator.PortRange(from_port=80), globalaccelerator.PortRange(from_port=443)
            ]
        )
        
        # Import the Load Balancers
        nlb1 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB1",
            load_balancer_arn="arn:aws:elasticloadbalancing:us-west-2:111111111111:loadbalancer/app/my-load-balancer1/e16bef66805b"
        )
        nlb2 = elbv2.NetworkLoadBalancer.from_network_load_balancer_attributes(self, "NLB2",
            load_balancer_arn="arn:aws:elasticloadbalancing:ap-south-1:111111111111:loadbalancer/app/my-load-balancer2/5513dc2ea8a1"
        )
        
        # Add one EndpointGroup for each Region we are targeting
        listener.add_endpoint_group("Group1",
            endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb1)]
        )
        listener.add_endpoint_group("Group2",
            # Imported load balancers automatically calculate their Region from the ARN.
            # If you are load balancing to other resources, you must also pass a `region`
            # parameter here.
            endpoints=[ga_endpoints.NetworkLoadBalancerEndpoint(nlb2)]
        )
    '''

    def __init__(
        self,
        load_balancer: _INetworkLoadBalancer_96e17101,
        *,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param load_balancer: -
        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__edacbc82e43081f03b16a95735ec03233b002430b75f4210e6958b2ecdfcde4d)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        options = NetworkLoadBalancerEndpointProps(weight=weight)

        jsii.create(self.__class__, self, [load_balancer, options])

    @jsii.member(jsii_name="renderEndpointConfiguration")
    def render_endpoint_configuration(self) -> typing.Any:
        '''Render the endpoint to an endpoint configuration.'''
        return typing.cast(typing.Any, jsii.invoke(self, "renderEndpointConfiguration", []))

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''The region where the endpoint is located.

        If the region cannot be determined, ``undefined`` is returned
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_globalaccelerator_endpoints.NetworkLoadBalancerEndpointProps",
    jsii_struct_bases=[],
    name_mapping={"weight": "weight"},
)
class NetworkLoadBalancerEndpointProps:
    def __init__(self, *, weight: typing.Optional[jsii.Number] = None) -> None:
        '''Properties for a NetworkLoadBalancerEndpoint.

        :param weight: Endpoint weight across all endpoints in the group. Must be a value between 0 and 255. Default: 128

        :exampleMetadata: infused

        Example::

            # nlb: elbv2.NetworkLoadBalancer
            # listener: globalaccelerator.Listener
            
            
            listener.add_endpoint_group("Group",
                endpoints=[
                    ga_endpoints.NetworkLoadBalancerEndpoint(nlb,
                        weight=128
                    )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a3059a828313b5b869d2a1ae70c7acf7cf9e4d48942d0394e47efafc648b331f)
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Endpoint weight across all endpoints in the group.

        Must be a value between 0 and 255.

        :default: 128
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NetworkLoadBalancerEndpointProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "ApplicationLoadBalancerEndpoint",
    "ApplicationLoadBalancerEndpointOptions",
    "CfnEipEndpoint",
    "CfnEipEndpointProps",
    "InstanceEndpoint",
    "InstanceEndpointProps",
    "NetworkLoadBalancerEndpoint",
    "NetworkLoadBalancerEndpointProps",
]

publication.publish()

def _typecheckingstub__ba4640acce1129555dd019374571778734d893a209c2784f062edff4221df6f1(
    load_balancer: _IApplicationLoadBalancer_4cbd50ab,
    *,
    preserve_client_ip: typing.Optional[builtins.bool] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c0ac3083381dd6ab3fdb91d6359ab553b1b88dc7e082a30b6e898d5733adbc0(
    *,
    preserve_client_ip: typing.Optional[builtins.bool] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea5231b8f6dbbebc7fcece999f2933e63d13dacdbd7d2bdc4b9c382b4aac06c7(
    eip: _CfnEIP_f7fb6536,
    *,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__325966af990f79d498fd30f2d9440803965b307292d612b47a1b6dbd862fb2ef(
    *,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c2cf290b2c92721fe0ccf29dedc01f3c274ef2f3250c08926449f729dd41260(
    instance: _IInstance_ab239e7c,
    *,
    preserve_client_ip: typing.Optional[builtins.bool] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234a90a888e0bfaab2b608e4e2c1e1a69a9e87121c40a35a442f702755d1d047(
    *,
    preserve_client_ip: typing.Optional[builtins.bool] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__edacbc82e43081f03b16a95735ec03233b002430b75f4210e6958b2ecdfcde4d(
    load_balancer: _INetworkLoadBalancer_96e17101,
    *,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a3059a828313b5b869d2a1ae70c7acf7cf9e4d48942d0394e47efafc648b331f(
    *,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
