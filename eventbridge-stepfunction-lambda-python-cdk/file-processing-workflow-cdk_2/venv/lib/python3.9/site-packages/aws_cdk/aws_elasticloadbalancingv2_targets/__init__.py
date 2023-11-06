'''
# Targets for AWS Elastic Load Balancing V2

This package contains targets for ELBv2. See the README of the `aws-cdk-lib/aws-elasticloadbalancingv2` library.
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

from ..aws_ec2 import Instance as _Instance_873cd165
from ..aws_elasticloadbalancingv2 import (
    ApplicationLoadBalancer as _ApplicationLoadBalancer_341e4ec1,
    IApplicationLoadBalancerTarget as _IApplicationLoadBalancerTarget_fabf9003,
    IApplicationTargetGroup as _IApplicationTargetGroup_57799827,
    INetworkLoadBalancerTarget as _INetworkLoadBalancerTarget_688b169f,
    INetworkTargetGroup as _INetworkTargetGroup_abca2df7,
    LoadBalancerTargetProps as _LoadBalancerTargetProps_4c30a73c,
)
from ..aws_lambda import IFunction as _IFunction_6adb0ab8


@jsii.implements(_INetworkLoadBalancerTarget_688b169f)
class AlbArnTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.AlbArnTarget",
):
    '''A single Application Load Balancer as the target for load balancing.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        alb_arn_target = elasticloadbalancingv2_targets.AlbArnTarget("albArn", 123)
    '''

    def __init__(self, alb_arn: builtins.str, port: jsii.Number) -> None:
        '''Create a new alb target.

        :param alb_arn: The ARN of the application load balancer to load balance to.
        :param port: The port on which the target is listening.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__25d70f2793026e068f7401c24a9086fabd06f88513447495a5230201e1c35f0b)
            check_type(argname="argument alb_arn", value=alb_arn, expected_type=type_hints["alb_arn"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [alb_arn, port])

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: _INetworkTargetGroup_abca2df7,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this alb target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ea49d3d21e7fdd26737ad142510132a0b92aad60fc05d121077fff9d7ef5770)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


class AlbTarget(
    AlbArnTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.AlbTarget",
):
    '''A single Application Load Balancer as the target for load balancing.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancingv2_targets as targets
        import aws_cdk.aws_ecs as ecs
        import aws_cdk.aws_ecs_patterns as patterns
        
        # vpc: ec2.Vpc
        
        
        task = ecs.FargateTaskDefinition(self, "Task", cpu=256, memory_limit_mi_b=512)
        task.add_container("nginx",
            image=ecs.ContainerImage.from_registry("public.ecr.aws/nginx/nginx:latest"),
            port_mappings=[ecs.PortMapping(container_port=80)]
        )
        
        svc = patterns.ApplicationLoadBalancedFargateService(self, "Service",
            vpc=vpc,
            task_definition=task,
            public_load_balancer=False
        )
        
        nlb = elbv2.NetworkLoadBalancer(self, "Nlb",
            vpc=vpc,
            cross_zone_enabled=True,
            internet_facing=True
        )
        
        listener = nlb.add_listener("listener", port=80)
        
        listener.add_targets("Targets",
            targets=[targets.AlbTarget(svc.load_balancer, 80)],
            port=80
        )
        
        CfnOutput(self, "NlbEndpoint", value=f"http://{nlb.loadBalancerDnsName}")
    '''

    def __init__(
        self,
        alb: _ApplicationLoadBalancer_341e4ec1,
        port: jsii.Number,
    ) -> None:
        '''
        :param alb: The application load balancer to load balance to.
        :param port: The port on which the target is listening.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bd3c46777bea3cc0051ec19e4d49e906dc65667b0e86f1104c7ed8f70dc67e80)
            check_type(argname="argument alb", value=alb, expected_type=type_hints["alb"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [alb, port])


@jsii.implements(_IApplicationLoadBalancerTarget_fabf9003, _INetworkLoadBalancerTarget_688b169f)
class InstanceIdTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.InstanceIdTarget",
):
    '''An EC2 instance that is the target for load balancing.

    If you register a target of this type, you are responsible for making
    sure the load balancer's security group can connect to the instance.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        instance_id_target = elasticloadbalancingv2_targets.InstanceIdTarget("instanceId", 123)
    '''

    def __init__(
        self,
        instance_id: builtins.str,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new Instance target.

        :param instance_id: Instance ID of the instance to register to.
        :param port: Override the default port for the target group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b3820af24c8d0caf9d54065ac5cda2ca9979ee90fbb15f9f692a3542160b38b)
            check_type(argname="argument instance_id", value=instance_id, expected_type=type_hints["instance_id"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [instance_id, port])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(
        self,
        target_group: _IApplicationTargetGroup_57799827,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e70e7ee18a71770eaa08504d84271779a0a58094edefcc8ce3216dc7e9b68be)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToApplicationTargetGroup", [target_group]))

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: _INetworkTargetGroup_abca2df7,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c0af4f33601944860c7afb8bd7b24a7ae7f810bbfad86781e7210eacdf47b0a)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


class InstanceTarget(
    InstanceIdTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.InstanceTarget",
):
    '''
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ec2 as ec2
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        # instance: ec2.Instance
        
        instance_target = elasticloadbalancingv2_targets.InstanceTarget(instance, 123)
    '''

    def __init__(
        self,
        instance: _Instance_873cd165,
        port: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Create a new Instance target.

        :param instance: Instance to register to.
        :param port: Override the default port for the target group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d0b0a387fdd5384869920ca6a60983b93293d68a187d248cc55a87ec55602502)
            check_type(argname="argument instance", value=instance, expected_type=type_hints["instance"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
        jsii.create(self.__class__, self, [instance, port])


@jsii.implements(_IApplicationLoadBalancerTarget_fabf9003, _INetworkLoadBalancerTarget_688b169f)
class IpTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.IpTarget",
):
    '''An IP address that is a target for load balancing.

    Specify IP addresses from the subnets of the virtual private cloud (VPC) for
    the target group, the RFC 1918 range (10.0.0.0/8, 172.16.0.0/12, and
    192.168.0.0/16), and the RFC 6598 range (100.64.0.0/10). You can't specify
    publicly routable IP addresses.

    If you register a target of this type, you are responsible for making
    sure the load balancer's security group can send packets to the IP address.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_elasticloadbalancingv2_targets as elasticloadbalancingv2_targets
        
        ip_target = elasticloadbalancingv2_targets.IpTarget("ipAddress", 123, "availabilityZone")
    '''

    def __init__(
        self,
        ip_address: builtins.str,
        port: typing.Optional[jsii.Number] = None,
        availability_zone: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Create a new IPAddress target.

        The availabilityZone parameter determines whether the target receives
        traffic from the load balancer nodes in the specified Availability Zone
        or from all enabled Availability Zones for the load balancer.

        This parameter is not supported if the target type of the target group
        is instance. If the IP address is in a subnet of the VPC for the target
        group, the Availability Zone is automatically detected and this
        parameter is optional. If the IP address is outside the VPC, this
        parameter is required.

        With an Application Load Balancer, if the IP address is outside the VPC
        for the target group, the only supported value is all.

        Default is automatic.

        :param ip_address: The IP Address to load balance to.
        :param port: Override the group's default port.
        :param availability_zone: Availability zone to send traffic from.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce293fbbbc943f4efe7d581fe7eec34ab650ed64fb91ba63a9a9f352c105579e)
            check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument availability_zone", value=availability_zone, expected_type=type_hints["availability_zone"])
        jsii.create(self.__class__, self, [ip_address, port, availability_zone])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(
        self,
        target_group: _IApplicationTargetGroup_57799827,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a9a376c8ed3a883a27f4ae60ca1aec9ad984e59f8e7fa8a170556c3f7fe55e5)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToApplicationTargetGroup", [target_group]))

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: _INetworkTargetGroup_abca2df7,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__069f34c3f18be180bdb72c9a996b9bd91047c65c9c1cf353e7587ca71c38032a)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


@jsii.implements(_IApplicationLoadBalancerTarget_fabf9003)
class LambdaTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_elasticloadbalancingv2_targets.LambdaTarget",
):
    '''
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_lambda as lambda_
        import aws_cdk.aws_elasticloadbalancingv2_targets as targets
        
        # lambda_function: lambda.Function
        # lb: elbv2.ApplicationLoadBalancer
        
        
        listener = lb.add_listener("Listener", port=80)
        listener.add_targets("Targets",
            targets=[targets.LambdaTarget(lambda_function)],
        
            # For Lambda Targets, you need to explicitly enable health checks if you
            # want them.
            health_check=elbv2.HealthCheck(
                enabled=True
            )
        )
    '''

    def __init__(self, fn: _IFunction_6adb0ab8) -> None:
        '''Create a new Lambda target.

        :param fn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5275fd84f4406ac6b5a4f40a26b3d677ee61e71807bc8aeac8ac506eccc3bc3b)
            check_type(argname="argument fn", value=fn, expected_type=type_hints["fn"])
        jsii.create(self.__class__, self, [fn])

    @jsii.member(jsii_name="attachToApplicationTargetGroup")
    def attach_to_application_target_group(
        self,
        target_group: _IApplicationTargetGroup_57799827,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b190f4c5fe7b990d3e274ecebf1188f5d7b6279fa49c8d06b07414c2348d886)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToApplicationTargetGroup", [target_group]))

    @jsii.member(jsii_name="attachToNetworkTargetGroup")
    def attach_to_network_target_group(
        self,
        target_group: _INetworkTargetGroup_abca2df7,
    ) -> _LoadBalancerTargetProps_4c30a73c:
        '''Register this instance target with a load balancer.

        Don't call this, it is called automatically when you add the target to a
        load balancer.

        :param target_group: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2f6c60936adbb8b62de293ba6e14e2a54ee5b179f71c61e5f73cca4e987d14a)
            check_type(argname="argument target_group", value=target_group, expected_type=type_hints["target_group"])
        return typing.cast(_LoadBalancerTargetProps_4c30a73c, jsii.invoke(self, "attachToNetworkTargetGroup", [target_group]))


__all__ = [
    "AlbArnTarget",
    "AlbTarget",
    "InstanceIdTarget",
    "InstanceTarget",
    "IpTarget",
    "LambdaTarget",
]

publication.publish()

def _typecheckingstub__25d70f2793026e068f7401c24a9086fabd06f88513447495a5230201e1c35f0b(
    alb_arn: builtins.str,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ea49d3d21e7fdd26737ad142510132a0b92aad60fc05d121077fff9d7ef5770(
    target_group: _INetworkTargetGroup_abca2df7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3c46777bea3cc0051ec19e4d49e906dc65667b0e86f1104c7ed8f70dc67e80(
    alb: _ApplicationLoadBalancer_341e4ec1,
    port: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b3820af24c8d0caf9d54065ac5cda2ca9979ee90fbb15f9f692a3542160b38b(
    instance_id: builtins.str,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e70e7ee18a71770eaa08504d84271779a0a58094edefcc8ce3216dc7e9b68be(
    target_group: _IApplicationTargetGroup_57799827,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c0af4f33601944860c7afb8bd7b24a7ae7f810bbfad86781e7210eacdf47b0a(
    target_group: _INetworkTargetGroup_abca2df7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0b0a387fdd5384869920ca6a60983b93293d68a187d248cc55a87ec55602502(
    instance: _Instance_873cd165,
    port: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce293fbbbc943f4efe7d581fe7eec34ab650ed64fb91ba63a9a9f352c105579e(
    ip_address: builtins.str,
    port: typing.Optional[jsii.Number] = None,
    availability_zone: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a9a376c8ed3a883a27f4ae60ca1aec9ad984e59f8e7fa8a170556c3f7fe55e5(
    target_group: _IApplicationTargetGroup_57799827,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__069f34c3f18be180bdb72c9a996b9bd91047c65c9c1cf353e7587ca71c38032a(
    target_group: _INetworkTargetGroup_abca2df7,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5275fd84f4406ac6b5a4f40a26b3d677ee61e71807bc8aeac8ac506eccc3bc3b(
    fn: _IFunction_6adb0ab8,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b190f4c5fe7b990d3e274ecebf1188f5d7b6279fa49c8d06b07414c2348d886(
    target_group: _IApplicationTargetGroup_57799827,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2f6c60936adbb8b62de293ba6e14e2a54ee5b179f71c61e5f73cca4e987d14a(
    target_group: _INetworkTargetGroup_abca2df7,
) -> None:
    """Type checking stubs"""
    pass
