'''
# Route53 Alias Record Targets for the CDK Route53 Library

This library contains Route53 Alias Record targets for:

* API Gateway custom domains

  ```python
  import aws_cdk.aws_apigateway as apigw

  # zone: route53.HostedZone
  # rest_api: apigw.LambdaRestApi


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.ApiGateway(rest_api))
  )
  ```
* API Gateway V2 custom domains

  ```python
  import aws_cdk.aws_apigatewayv2_alpha as apigwv2

  # zone: route53.HostedZone
  # domain_name: apigwv2.DomainName


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.ApiGatewayv2DomainProperties(domain_name.regional_domain_name, domain_name.regional_hosted_zone_id))
  )
  ```
* CloudFront distributions

  ```python
  import aws_cdk.aws_cloudfront as cloudfront

  # zone: route53.HostedZone
  # distribution: cloudfront.CloudFrontWebDistribution


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(distribution))
  )
  ```
* ELBv2 load balancers

  ```python
  import aws_cdk.aws_elasticloadbalancingv2 as elbv2

  # zone: route53.HostedZone
  # lb: elbv2.ApplicationLoadBalancer


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(lb))
  )
  ```
* Classic load balancers

  ```python
  import aws_cdk.aws_elasticloadbalancing as elb

  # zone: route53.HostedZone
  # lb: elb.LoadBalancer


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.ClassicLoadBalancerTarget(lb))
  )
  ```

**Important:** Based on [AWS documentation](https://aws.amazon.com/de/premiumsupport/knowledge-center/alias-resource-record-set-route53-cli/), all alias record in Route 53 that points to a Elastic Load Balancer will always include *dualstack* for the DNSName to resolve IPv4/IPv6 addresses (without *dualstack* IPv6 will not resolve).

For example, if the Amazon-provided DNS for the load balancer is `ALB-xxxxxxx.us-west-2.elb.amazonaws.com`, CDK will create alias target in Route 53 will be `dualstack.ALB-xxxxxxx.us-west-2.elb.amazonaws.com`.

* GlobalAccelerator

  ```python
  import aws_cdk.aws_globalaccelerator as globalaccelerator

  # zone: route53.HostedZone
  # accelerator: globalaccelerator.Accelerator


  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.GlobalAcceleratorTarget(accelerator))
  )
  ```

**Important:** If you use GlobalAcceleratorDomainTarget, passing a string rather than an instance of IAccelerator, ensure that the string is a valid domain name of an existing Global Accelerator instance.
See [the documentation on DNS addressing](https://docs.aws.amazon.com/global-accelerator/latest/dg/dns-addressing-custom-domains.dns-addressing.html) with Global Accelerator for more info.

* InterfaceVpcEndpoints

**Important:** Based on the CFN docs for VPCEndpoints - [see here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-vpcendpoint.html#aws-resource-ec2-vpcendpoint-return-values) - the attributes returned for DnsEntries in CloudFormation is a combination of the hosted zone ID and the DNS name. The entries are ordered as follows: regional public DNS, zonal public DNS, private DNS, and wildcard DNS. This order is not enforced for AWS Marketplace services, and therefore this CDK construct is ONLY guaranteed to work with non-marketplace services.

```python
import aws_cdk.aws_ec2 as ec2

# zone: route53.HostedZone
# interface_vpc_endpoint: ec2.InterfaceVpcEndpoint


route53.ARecord(self, "AliasRecord",
    zone=zone,
    target=route53.RecordTarget.from_alias(targets.InterfaceVpcEndpointTarget(interface_vpc_endpoint))
)
```

* S3 Bucket Website:

**Important:** The Bucket name must strictly match the full DNS name.
See [the Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html) for more info.

```python
import aws_cdk.aws_s3 as s3


record_name = "www"
domain_name = "example.com"

bucket_website = s3.Bucket(self, "BucketWebsite",
    bucket_name=[record_name, domain_name].join("."),  # www.example.com
    public_read_access=True,
    website_index_document="index.html"
)

zone = route53.HostedZone.from_lookup(self, "Zone", domain_name=domain_name) # example.com

route53.ARecord(self, "AliasRecord",
    zone=zone,
    record_name=record_name,  # www
    target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket_website))
)
```

* User pool domain

  ```python
  import aws_cdk.aws_cognito as cognito

  # zone: route53.HostedZone
  # domain: cognito.UserPoolDomain

  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.UserPoolDomainTarget(domain))
  )
  ```
* Route 53 record

  ```python
  # zone: route53.HostedZone
  # record: route53.ARecord

  route53.ARecord(self, "AliasRecord",
      zone=zone,
      target=route53.RecordTarget.from_alias(targets.Route53RecordTarget(record))
  )
  ```
* Elastic Beanstalk environment:

**Important:** Only supports Elastic Beanstalk environments created after 2016 that have a regional endpoint.

```python
# zone: route53.HostedZone
# ebs_environment_url: str


route53.ARecord(self, "AliasRecord",
    zone=zone,
    target=route53.RecordTarget.from_alias(targets.ElasticBeanstalkEnvironmentEndpointTarget(ebs_environment_url))
)
```

See the documentation of `aws-cdk-lib/aws-route53` for more information.
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
from ..aws_apigateway import (
    IDomainName as _IDomainName_6c4e4c80, RestApiBase as _RestApiBase_0431da32
)
from ..aws_cloudfront import IDistribution as _IDistribution_7ac752a4
from ..aws_cognito import UserPoolDomain as _UserPoolDomain_f402e168
from ..aws_ec2 import InterfaceVpcEndpoint as _InterfaceVpcEndpoint_9b08bb25
from ..aws_elasticloadbalancing import LoadBalancer as _LoadBalancer_a894d40e
from ..aws_elasticloadbalancingv2 import ILoadBalancerV2 as _ILoadBalancerV2_4c5c0fbb
from ..aws_globalaccelerator import IAccelerator as _IAccelerator_88df59f2
from ..aws_route53 import (
    AliasRecordTargetConfig as _AliasRecordTargetConfig_588f62e9,
    IAliasRecordTarget as _IAliasRecordTarget_aae9327f,
    IHostedZone as _IHostedZone_9a6907ad,
    IRecordSet as _IRecordSet_7d446a82,
)
from ..aws_s3 import IBucket as _IBucket_42e086fd


@jsii.implements(_IAliasRecordTarget_aae9327f)
class ApiGatewayDomain(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.ApiGatewayDomain",
):
    '''Defines an API Gateway domain name as the alias target.

    Use the ``ApiGateway`` class if you wish to map the alias to an REST API with a
    domain name defined through the ``RestApiProps.domainName`` prop.

    :exampleMetadata: infused

    Example::

        # hosted_zone_for_example_com: Any
        # domain_name: apigateway.DomainName
        
        import aws_cdk.aws_route53 as route53
        import aws_cdk.aws_route53_targets as targets
        
        
        route53.ARecord(self, "CustomDomainAliasRecord",
            zone=hosted_zone_for_example_com,
            target=route53.RecordTarget.from_alias(targets.ApiGatewayDomain(domain_name))
        )
    '''

    def __init__(self, domain_name: _IDomainName_6c4e4c80) -> None:
        '''
        :param domain_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d0921c623b2237609e875d52509b1328a8d0819876cad269003b2c5fd4b5b41)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        jsii.create(self.__class__, self, [domain_name])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fba9f83d64f14df4ac3b2eb072aa1a489a55ffa3d1f675d5f2b4cc091ed1545e)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class ApiGatewayv2DomainProperties(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.ApiGatewayv2DomainProperties",
):
    '''Defines an API Gateway V2 domain name as the alias target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_apigatewayv2_alpha as apigwv2
        
        # zone: route53.HostedZone
        # domain_name: apigwv2.DomainName
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ApiGatewayv2DomainProperties(domain_name.regional_domain_name, domain_name.regional_hosted_zone_id))
        )
    '''

    def __init__(
        self,
        regional_domain_name: builtins.str,
        regional_hosted_zone_id: builtins.str,
    ) -> None:
        '''
        :param regional_domain_name: the domain name associated with the regional endpoint for this custom domain name.
        :param regional_hosted_zone_id: the region-specific Amazon Route 53 Hosted Zone ID of the regional endpoint.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__483c7c259350e0aa6e9eeb29414ed4c8d358b92ef14b0a7044fe79d005aa1d57)
            check_type(argname="argument regional_domain_name", value=regional_domain_name, expected_type=type_hints["regional_domain_name"])
            check_type(argname="argument regional_hosted_zone_id", value=regional_hosted_zone_id, expected_type=type_hints["regional_hosted_zone_id"])
        jsii.create(self.__class__, self, [regional_domain_name, regional_hosted_zone_id])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__06815ea952926fe8cadd75b92163d9cdaa6382360911ec0411cabfe9a3c03a6c)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class BucketWebsiteTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.BucketWebsiteTarget",
):
    '''Use a S3 as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_s3 as s3
        
        
        record_name = "www"
        domain_name = "example.com"
        
        bucket_website = s3.Bucket(self, "BucketWebsite",
            bucket_name=[record_name, domain_name].join("."),  # www.example.com
            public_read_access=True,
            website_index_document="index.html"
        )
        
        zone = route53.HostedZone.from_lookup(self, "Zone", domain_name=domain_name) # example.com
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            record_name=record_name,  # www
            target=route53.RecordTarget.from_alias(targets.BucketWebsiteTarget(bucket_website))
        )
    '''

    def __init__(self, bucket: _IBucket_42e086fd) -> None:
        '''
        :param bucket: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ddbd19de44d0f648d972f99cbd261ae3e9159511037db7c12ae0ebcb70553020)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        jsii.create(self.__class__, self, [bucket])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd2ecb9daaec6458d815966f81355d94c2b67af66e5e1242ed3eb80048b7a1d4)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class ClassicLoadBalancerTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.ClassicLoadBalancerTarget",
):
    '''Use a classic ELB as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancing as elb
        
        # zone: route53.HostedZone
        # lb: elb.LoadBalancer
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ClassicLoadBalancerTarget(lb))
        )
    '''

    def __init__(self, load_balancer: _LoadBalancer_a894d40e) -> None:
        '''
        :param load_balancer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df60d89e015cd817a27383507bd36a21baad91e6194326c62959170a57cfec93)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        jsii.create(self.__class__, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6edcf9d41588b12bcddbe0a1a663413d6102c86e1b5f3d2d52c448ffa8ba0048)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class CloudFrontTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.CloudFrontTarget",
):
    '''Use a CloudFront Distribution as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cloudfront as cloudfront
        
        # my_zone: route53.HostedZone
        # distribution: cloudfront.CloudFrontWebDistribution
        
        route53.AaaaRecord(self, "Alias",
            zone=my_zone,
            target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(distribution))
        )
    '''

    def __init__(self, distribution: _IDistribution_7ac752a4) -> None:
        '''
        :param distribution: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0387f27ff80dda6a9654a3e1c030c822248f13c035f56a26ddb4824ba54fa0d1)
            check_type(argname="argument distribution", value=distribution, expected_type=type_hints["distribution"])
        jsii.create(self.__class__, self, [distribution])

    @jsii.member(jsii_name="getHostedZoneId")
    @builtins.classmethod
    def get_hosted_zone_id(cls, scope: _constructs_77d1e7e8.IConstruct) -> builtins.str:
        '''Get the hosted zone id for the current scope.

        :param scope: - scope in which this resource is defined.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e952cb31d689e0424d3f21de36bba9e037a41b28afb935bda9111a47be9b9afb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        return typing.cast(builtins.str, jsii.sinvoke(cls, "getHostedZoneId", [scope]))

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff9f8a6340ffc435ad18afba28ab7e6b035f0745841d574ed011feee8830d2db)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CLOUDFRONT_ZONE_ID")
    def CLOUDFRONT_ZONE_ID(cls) -> builtins.str:
        '''The hosted zone Id if using an alias record in Route53.

        This value never changes.
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "CLOUDFRONT_ZONE_ID"))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class ElasticBeanstalkEnvironmentEndpointTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.ElasticBeanstalkEnvironmentEndpointTarget",
):
    '''Use an Elastic Beanstalk environment URL as an alias record target. E.g. mysampleenvironment.xyz.us-east-1.elasticbeanstalk.com or mycustomcnameprefix.us-east-1.elasticbeanstalk.com.

    Only supports Elastic Beanstalk environments created after 2016 that have a regional endpoint.

    :exampleMetadata: infused

    Example::

        # zone: route53.HostedZone
        # ebs_environment_url: str
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ElasticBeanstalkEnvironmentEndpointTarget(ebs_environment_url))
        )
    '''

    def __init__(self, environment_endpoint: builtins.str) -> None:
        '''
        :param environment_endpoint: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d25d707c026f750072f9d979b0260dab154996d630c701cc92fda7ebe39de84)
            check_type(argname="argument environment_endpoint", value=environment_endpoint, expected_type=type_hints["environment_endpoint"])
        jsii.create(self.__class__, self, [environment_endpoint])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__84020a15dd8ef0dcc21b591bd97f450f84cc046c2f1899e6aab8e6cbfd2ed378)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class GlobalAcceleratorDomainTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.GlobalAcceleratorDomainTarget",
):
    '''Use a Global Accelerator domain name as an alias record target.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53_targets as route53_targets
        
        global_accelerator_domain_target = route53_targets.GlobalAcceleratorDomainTarget("acceleratorDomainName")
    '''

    def __init__(self, accelerator_domain_name: builtins.str) -> None:
        '''Create an Alias Target for a Global Accelerator domain name.

        :param accelerator_domain_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c1f5b78bdd86e72483e6033d5bd58f9ee505b8c5c7e7f7a4716fcd03bd2f17e)
            check_type(argname="argument accelerator_domain_name", value=accelerator_domain_name, expected_type=type_hints["accelerator_domain_name"])
        jsii.create(self.__class__, self, [accelerator_domain_name])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__558f27329c2636934fcd56512940ef2784d615ef258b5e13b88e1bdfd7dc8d79)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="GLOBAL_ACCELERATOR_ZONE_ID")
    def GLOBAL_ACCELERATOR_ZONE_ID(cls) -> builtins.str:
        '''The hosted zone Id if using an alias record in Route53.

        This value never changes.
        Ref: https://docs.aws.amazon.com/general/latest/gr/global_accelerator.html
        '''
        return typing.cast(builtins.str, jsii.sget(cls, "GLOBAL_ACCELERATOR_ZONE_ID"))


class GlobalAcceleratorTarget(
    GlobalAcceleratorDomainTarget,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.GlobalAcceleratorTarget",
):
    '''Use a Global Accelerator instance domain name as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_globalaccelerator as globalaccelerator
        
        # zone: route53.HostedZone
        # accelerator: globalaccelerator.Accelerator
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.GlobalAcceleratorTarget(accelerator))
        )
    '''

    def __init__(self, accelerator: _IAccelerator_88df59f2) -> None:
        '''Create an Alias Target for a Global Accelerator instance.

        :param accelerator: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e91db2b16be80023a03d4863b5100b3072db6e16f816be05e613cdcc1e6baec)
            check_type(argname="argument accelerator", value=accelerator, expected_type=type_hints["accelerator"])
        jsii.create(self.__class__, self, [accelerator])


@jsii.implements(_IAliasRecordTarget_aae9327f)
class InterfaceVpcEndpointTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.InterfaceVpcEndpointTarget",
):
    '''Set an InterfaceVpcEndpoint as a target for an ARecord.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ec2 as ec2
        
        # zone: route53.HostedZone
        # interface_vpc_endpoint: ec2.InterfaceVpcEndpoint
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.InterfaceVpcEndpointTarget(interface_vpc_endpoint))
        )
    '''

    def __init__(self, vpc_endpoint: _InterfaceVpcEndpoint_9b08bb25) -> None:
        '''
        :param vpc_endpoint: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec571e3ea34290d4de9c515d3722116d3a7ea94b76024cfe173ea6c897eecb0d)
            check_type(argname="argument vpc_endpoint", value=vpc_endpoint, expected_type=type_hints["vpc_endpoint"])
        jsii.create(self.__class__, self, [vpc_endpoint])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6092dd3b5ac5bc3015dda9338cbe628b55da24a7ed91f812d3cfd949f452a7d)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class LoadBalancerTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.LoadBalancerTarget",
):
    '''Use an ELBv2 as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_elasticloadbalancingv2 as elbv2
        
        # zone: route53.HostedZone
        # lb: elbv2.ApplicationLoadBalancer
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.LoadBalancerTarget(lb))
        )
    '''

    def __init__(self, load_balancer: _ILoadBalancerV2_4c5c0fbb) -> None:
        '''
        :param load_balancer: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d1a985c9395ef813e5bd41f719bb6218efa5bb0e851f54f91b3d61c932cb1c59)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        jsii.create(self.__class__, self, [load_balancer])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__beeacae3772d5371ddf28b7c33e79baecf305ce65d9e646f0f3f8eb9da81ad8b)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class Route53RecordTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.Route53RecordTarget",
):
    '''Use another Route 53 record as an alias record target.

    :exampleMetadata: infused

    Example::

        # zone: route53.HostedZone
        # record: route53.ARecord
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.Route53RecordTarget(record))
        )
    '''

    def __init__(self, record: _IRecordSet_7d446a82) -> None:
        '''
        :param record: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2066ecabfb9b9141cbb485e7f03d0f098e5abdd8192896fc3d377b5727352fd7)
            check_type(argname="argument record", value=record, expected_type=type_hints["record"])
        jsii.create(self.__class__, self, [record])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20a2915996329a774faa7e609ae99a71303eecebe91edad6fdb7552e5beea323)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, zone]))


@jsii.implements(_IAliasRecordTarget_aae9327f)
class UserPoolDomainTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.UserPoolDomainTarget",
):
    '''Use a user pool domain as an alias record target.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_cognito as cognito
        
        # zone: route53.HostedZone
        # domain: cognito.UserPoolDomain
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.UserPoolDomainTarget(domain))
        )
    '''

    def __init__(self, domain: _UserPoolDomain_f402e168) -> None:
        '''
        :param domain: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b00bf5eba0024f5bf7c1acfbffab5d3fa54e65eb29951b3b0fe2f665920291d0)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        jsii.create(self.__class__, self, [domain])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        _record: _IRecordSet_7d446a82,
        _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> _AliasRecordTargetConfig_588f62e9:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param _record: -
        :param _zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ce4923401899f48bd0c1ae21051fc7f7dfe9597cb06da980cb1dc4cf441fbf3c)
            check_type(argname="argument _record", value=_record, expected_type=type_hints["_record"])
            check_type(argname="argument _zone", value=_zone, expected_type=type_hints["_zone"])
        return typing.cast(_AliasRecordTargetConfig_588f62e9, jsii.invoke(self, "bind", [_record, _zone]))


class ApiGateway(
    ApiGatewayDomain,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_targets.ApiGateway",
):
    '''Defines an API Gateway REST API as the alias target. Requires that the domain name will be defined through ``RestApiProps.domainName``.

    You can direct the alias to any ``apigateway.DomainName`` resource through the
    ``ApiGatewayDomain`` class.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_route53 as route53
        import aws_cdk.aws_route53_targets as targets
        
        # api: apigateway.RestApi
        # hosted_zone_for_example_com: Any
        
        
        route53.ARecord(self, "CustomDomainAliasRecord",
            zone=hosted_zone_for_example_com,
            target=route53.RecordTarget.from_alias(targets.ApiGateway(api))
        )
    '''

    def __init__(self, api: _RestApiBase_0431da32) -> None:
        '''
        :param api: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__570d79c602907c31355fd27286b9195e6a4ac50d33a57b857248da0d9c6d3dad)
            check_type(argname="argument api", value=api, expected_type=type_hints["api"])
        jsii.create(self.__class__, self, [api])


__all__ = [
    "ApiGateway",
    "ApiGatewayDomain",
    "ApiGatewayv2DomainProperties",
    "BucketWebsiteTarget",
    "ClassicLoadBalancerTarget",
    "CloudFrontTarget",
    "ElasticBeanstalkEnvironmentEndpointTarget",
    "GlobalAcceleratorDomainTarget",
    "GlobalAcceleratorTarget",
    "InterfaceVpcEndpointTarget",
    "LoadBalancerTarget",
    "Route53RecordTarget",
    "UserPoolDomainTarget",
]

publication.publish()

def _typecheckingstub__0d0921c623b2237609e875d52509b1328a8d0819876cad269003b2c5fd4b5b41(
    domain_name: _IDomainName_6c4e4c80,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fba9f83d64f14df4ac3b2eb072aa1a489a55ffa3d1f675d5f2b4cc091ed1545e(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__483c7c259350e0aa6e9eeb29414ed4c8d358b92ef14b0a7044fe79d005aa1d57(
    regional_domain_name: builtins.str,
    regional_hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__06815ea952926fe8cadd75b92163d9cdaa6382360911ec0411cabfe9a3c03a6c(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ddbd19de44d0f648d972f99cbd261ae3e9159511037db7c12ae0ebcb70553020(
    bucket: _IBucket_42e086fd,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd2ecb9daaec6458d815966f81355d94c2b67af66e5e1242ed3eb80048b7a1d4(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df60d89e015cd817a27383507bd36a21baad91e6194326c62959170a57cfec93(
    load_balancer: _LoadBalancer_a894d40e,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6edcf9d41588b12bcddbe0a1a663413d6102c86e1b5f3d2d52c448ffa8ba0048(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0387f27ff80dda6a9654a3e1c030c822248f13c035f56a26ddb4824ba54fa0d1(
    distribution: _IDistribution_7ac752a4,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e952cb31d689e0424d3f21de36bba9e037a41b28afb935bda9111a47be9b9afb(
    scope: _constructs_77d1e7e8.IConstruct,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ff9f8a6340ffc435ad18afba28ab7e6b035f0745841d574ed011feee8830d2db(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d25d707c026f750072f9d979b0260dab154996d630c701cc92fda7ebe39de84(
    environment_endpoint: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__84020a15dd8ef0dcc21b591bd97f450f84cc046c2f1899e6aab8e6cbfd2ed378(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c1f5b78bdd86e72483e6033d5bd58f9ee505b8c5c7e7f7a4716fcd03bd2f17e(
    accelerator_domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__558f27329c2636934fcd56512940ef2784d615ef258b5e13b88e1bdfd7dc8d79(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e91db2b16be80023a03d4863b5100b3072db6e16f816be05e613cdcc1e6baec(
    accelerator: _IAccelerator_88df59f2,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec571e3ea34290d4de9c515d3722116d3a7ea94b76024cfe173ea6c897eecb0d(
    vpc_endpoint: _InterfaceVpcEndpoint_9b08bb25,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6092dd3b5ac5bc3015dda9338cbe628b55da24a7ed91f812d3cfd949f452a7d(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d1a985c9395ef813e5bd41f719bb6218efa5bb0e851f54f91b3d61c932cb1c59(
    load_balancer: _ILoadBalancerV2_4c5c0fbb,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__beeacae3772d5371ddf28b7c33e79baecf305ce65d9e646f0f3f8eb9da81ad8b(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2066ecabfb9b9141cbb485e7f03d0f098e5abdd8192896fc3d377b5727352fd7(
    record: _IRecordSet_7d446a82,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20a2915996329a774faa7e609ae99a71303eecebe91edad6fdb7552e5beea323(
    _record: _IRecordSet_7d446a82,
    zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b00bf5eba0024f5bf7c1acfbffab5d3fa54e65eb29951b3b0fe2f665920291d0(
    domain: _UserPoolDomain_f402e168,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ce4923401899f48bd0c1ae21051fc7f7dfe9597cb06da980cb1dc4cf441fbf3c(
    _record: _IRecordSet_7d446a82,
    _zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__570d79c602907c31355fd27286b9195e6a4ac50d33a57b857248da0d9c6d3dad(
    api: _RestApiBase_0431da32,
) -> None:
    """Type checking stubs"""
    pass
