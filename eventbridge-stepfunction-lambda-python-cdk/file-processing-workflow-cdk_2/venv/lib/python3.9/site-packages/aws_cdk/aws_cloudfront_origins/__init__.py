'''
# CloudFront Origins for the CDK CloudFront Library

This library contains convenience methods for defining origins for a CloudFront distribution. You can use this library to create origins from
S3 buckets, Elastic Load Balancing v2 load balancers, or any other domain name.

## S3 Bucket

An S3 bucket can be added as an origin. If the bucket is configured as a website endpoint, the distribution can use S3 redirects and S3 custom error
documents.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket))
)
```

The above will treat the bucket differently based on if `IBucket.isWebsite` is set or not. If the bucket is configured as a website, the bucket is
treated as an HTTP origin, and the built-in S3 redirects and error pages can be used. Otherwise, the bucket is handled as a bucket origin and
CloudFront's redirect and error handling will be used. In the latter case, the Origin will create an origin access identity and grant it access to the
underlying bucket. This can be used in conjunction with a bucket that is not public to require that your users access your content using CloudFront
URLs and not S3 URLs directly. Alternatively, a custom origin access identity can be passed to the S3 origin in the properties.

### Adding Custom Headers

You can configure CloudFront to add custom headers to the requests that it sends to your origin. These custom headers enable you to send and gather information from your origin that you don’t get with typical viewer requests. These headers can even be customized for each origin. CloudFront supports custom headers for both for custom and Amazon S3 origins.

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket,
        custom_headers={
            "Foo": "bar"
        }
    ))
)
```

## ELBv2 Load Balancer

An Elastic Load Balancing (ELB) v2 load balancer may be used as an origin. In order for a load balancer to serve as an origin, it must be publicly
accessible (`internetFacing` is true). Both Application and Network load balancers are supported.

```python
import aws_cdk.aws_ec2 as ec2
import aws_cdk.aws_elasticloadbalancingv2 as elbv2

# vpc: ec2.Vpc

# Create an application load balancer in a VPC. 'internetFacing' must be 'true'
# for CloudFront to access the load balancer and use it as an origin.
lb = elbv2.ApplicationLoadBalancer(self, "LB",
    vpc=vpc,
    internet_facing=True
)
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.LoadBalancerV2Origin(lb))
)
```

The origin can also be customized to respond on different ports, have different connection properties, etc.

```python
import aws_cdk.aws_elasticloadbalancingv2 as elbv2

# load_balancer: elbv2.ApplicationLoadBalancer

origin = origins.LoadBalancerV2Origin(load_balancer,
    connection_attempts=3,
    connection_timeout=Duration.seconds(5),
    read_timeout=Duration.seconds(45),
    keepalive_timeout=Duration.seconds(45),
    protocol_policy=cloudfront.OriginProtocolPolicy.MATCH_VIEWER
)
```

Note that the `readTimeout` and `keepaliveTimeout` properties can extend their values over 60 seconds only if a limit increase request for CloudFront origin response timeout
quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Consider that this value is
still limited to a maximum value of 180 seconds, which is a hard limit for that quota.

## From an HTTP endpoint

Origins can also be created from any other HTTP endpoint, given the domain name, and optionally, other origin properties.

```python
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.HttpOrigin("www.example.com"))
)
```

See the documentation of `aws-cdk-lib/aws-cloudfront` for more information.

## Failover Origins (Origin Groups)

You can set up CloudFront with origin failover for scenarios that require high availability.
To get started, you create an origin group with two origins: a primary and a secondary.
If the primary origin is unavailable, or returns specific HTTP response status codes that indicate a failure,
CloudFront automatically switches to the secondary origin.
You achieve that behavior in the CDK using the `OriginGroup` class:

```python
my_bucket = s3.Bucket(self, "myBucket")
cloudfront.Distribution(self, "myDist",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.OriginGroup(
            primary_origin=origins.S3Origin(my_bucket),
            fallback_origin=origins.HttpOrigin("www.example.com"),
            # optional, defaults to: 500, 502, 503 and 504
            fallback_status_codes=[404]
        )
    )
)
```

## From an API Gateway REST API

Origins can be created from an API Gateway REST API. It is recommended to use a
[regional API](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-api-endpoint-types.html) in this case. The origin path will automatically be set as the stage name.

```python
# api: apigateway.RestApi

cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api))
)
```

If you want to use a different origin path, you can specify it in the `originPath` property.

```python
# api: apigateway.RestApi

cloudfront.Distribution(self, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api, origin_path="/custom-origin-path"))
)
```
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
from .. import Duration as _Duration_4839e8c3
from ..aws_apigateway import RestApi as _RestApi_777c8238
from ..aws_cloudfront import (
    CfnDistribution as _CfnDistribution_d9ad3595,
    IOrigin as _IOrigin_83d4c1fa,
    IOriginAccessIdentity as _IOriginAccessIdentity_a922494c,
    OriginBase as _OriginBase_b8fe5bcc,
    OriginBindConfig as _OriginBindConfig_25a57096,
    OriginBindOptions as _OriginBindOptions_088c2b51,
    OriginProps as _OriginProps_0675928d,
    OriginProtocolPolicy as _OriginProtocolPolicy_967ed73c,
    OriginSslPolicy as _OriginSslPolicy_d65cede2,
)
from ..aws_elasticloadbalancingv2 import ILoadBalancerV2 as _ILoadBalancerV2_4c5c0fbb
from ..aws_s3 import IBucket as _IBucket_42e086fd


class HttpOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.HttpOrigin",
):
    '''An Origin for an HTTP server or S3 bucket configured for website hosting.

    :exampleMetadata: infused

    Example::

        # Validating signed URLs or signed cookies with Trusted Key Groups
        
        # public key in PEM format
        # public_key: str
        
        pub_key = cloudfront.PublicKey(self, "MyPubKey",
            encoded_key=public_key
        )
        
        key_group = cloudfront.KeyGroup(self, "MyKeyGroup",
            items=[pub_key
            ]
        )
        
        cloudfront.Distribution(self, "Dist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.HttpOrigin("www.example.com"),
                trusted_key_groups=[key_group
                ]
            )
        )
    '''

    def __init__(
        self,
        domain_name: builtins.str,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param domain_name: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__57d13f69f251622e0723aa73c3eb93e482e0deb7a7b1e8439c7d7ad35cfc0cc5)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        props = HttpOriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [domain_name, props])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.HttpOriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class HttpOriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for an Origin backed by an S3 website-configured bucket, load balancer, or custom HTTP server.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_cloudfront as cloudfront
            from aws_cdk import aws_cloudfront_origins as cloudfront_origins
            
            http_origin_props = cloudfront_origins.HttpOriginProps(
                connection_attempts=123,
                connection_timeout=cdk.Duration.minutes(30),
                custom_headers={
                    "custom_headers_key": "customHeaders"
                },
                http_port=123,
                https_port=123,
                keepalive_timeout=cdk.Duration.minutes(30),
                origin_id="originId",
                origin_path="originPath",
                origin_shield_enabled=False,
                origin_shield_region="originShieldRegion",
                origin_ssl_protocols=[cloudfront.OriginSslPolicy.SSL_V3],
                protocol_policy=cloudfront.OriginProtocolPolicy.HTTP_ONLY,
                read_timeout=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13f43bf70f0a97ee8ca0e4f7aca38d43089ed2bc254d5c2b57c73b51c1c2b9df)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_OriginSslPolicy_d65cede2]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_OriginSslPolicy_d65cede2]], result)

    @builtins.property
    def protocol_policy(self) -> typing.Optional[_OriginProtocolPolicy_967ed73c]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_OriginProtocolPolicy_967ed73c], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class LoadBalancerV2Origin(
    HttpOrigin,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.LoadBalancerV2Origin",
):
    '''An Origin for a v2 load balancer.

    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_ec2 as ec2
        import aws_cdk.aws_elasticloadbalancingv2 as elbv2
        
        # vpc: ec2.Vpc
        
        # Create an application load balancer in a VPC. 'internetFacing' must be 'true'
        # for CloudFront to access the load balancer and use it as an origin.
        lb = elbv2.ApplicationLoadBalancer(self, "LB",
            vpc=vpc,
            internet_facing=True
        )
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.LoadBalancerV2Origin(lb))
        )
    '''

    def __init__(
        self,
        load_balancer: _ILoadBalancerV2_4c5c0fbb,
        *,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param load_balancer: -
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2e5124d4f469d6539077a529c09cfba685fe4a7037b9417216b18f6ccdba96c0)
            check_type(argname="argument load_balancer", value=load_balancer, expected_type=type_hints["load_balancer"])
        props = LoadBalancerV2OriginProps(
            http_port=http_port,
            https_port=https_port,
            keepalive_timeout=keepalive_timeout,
            origin_ssl_protocols=origin_ssl_protocols,
            protocol_policy=protocol_policy,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [load_balancer, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.LoadBalancerV2OriginProps",
    jsii_struct_bases=[HttpOriginProps],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "http_port": "httpPort",
        "https_port": "httpsPort",
        "keepalive_timeout": "keepaliveTimeout",
        "origin_ssl_protocols": "originSslProtocols",
        "protocol_policy": "protocolPolicy",
        "read_timeout": "readTimeout",
    },
)
class LoadBalancerV2OriginProps(HttpOriginProps):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        http_port: typing.Optional[jsii.Number] = None,
        https_port: typing.Optional[jsii.Number] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
        protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for an Origin backed by a v2 load balancer.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param http_port: The HTTP port that CloudFront uses to connect to the origin. Default: 80
        :param https_port: The HTTPS port that CloudFront uses to connect to the origin. Default: 443
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param origin_ssl_protocols: The SSL versions to use when interacting with the origin. Default: OriginSslPolicy.TLS_V1_2
        :param protocol_policy: Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin. Default: OriginProtocolPolicy.HTTPS_ONLY
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_elasticloadbalancingv2 as elbv2
            
            # load_balancer: elbv2.ApplicationLoadBalancer
            
            origin = origins.LoadBalancerV2Origin(load_balancer,
                connection_attempts=3,
                connection_timeout=Duration.seconds(5),
                read_timeout=Duration.seconds(45),
                keepalive_timeout=Duration.seconds(45),
                protocol_policy=cloudfront.OriginProtocolPolicy.MATCH_VIEWER
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c72b63200b184ae3f51c9b6a19be2eef9bddae313ee00c7378396c0dcf586887)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument http_port", value=http_port, expected_type=type_hints["http_port"])
            check_type(argname="argument https_port", value=https_port, expected_type=type_hints["https_port"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument origin_ssl_protocols", value=origin_ssl_protocols, expected_type=type_hints["origin_ssl_protocols"])
            check_type(argname="argument protocol_policy", value=protocol_policy, expected_type=type_hints["protocol_policy"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if http_port is not None:
            self._values["http_port"] = http_port
        if https_port is not None:
            self._values["https_port"] = https_port
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if origin_ssl_protocols is not None:
            self._values["origin_ssl_protocols"] = origin_ssl_protocols
        if protocol_policy is not None:
            self._values["protocol_policy"] = protocol_policy
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def http_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTP port that CloudFront uses to connect to the origin.

        :default: 80
        '''
        result = self._values.get("http_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def https_port(self) -> typing.Optional[jsii.Number]:
        '''The HTTPS port that CloudFront uses to connect to the origin.

        :default: 443
        '''
        result = self._values.get("https_port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def origin_ssl_protocols(
        self,
    ) -> typing.Optional[typing.List[_OriginSslPolicy_d65cede2]]:
        '''The SSL versions to use when interacting with the origin.

        :default: OriginSslPolicy.TLS_V1_2
        '''
        result = self._values.get("origin_ssl_protocols")
        return typing.cast(typing.Optional[typing.List[_OriginSslPolicy_d65cede2]], result)

    @builtins.property
    def protocol_policy(self) -> typing.Optional[_OriginProtocolPolicy_967ed73c]:
        '''Specifies the protocol (HTTP or HTTPS) that CloudFront uses to connect to the origin.

        :default: OriginProtocolPolicy.HTTPS_ONLY
        '''
        result = self._values.get("protocol_policy")
        return typing.cast(typing.Optional[_OriginProtocolPolicy_967ed73c], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LoadBalancerV2OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IOrigin_83d4c1fa)
class OriginGroup(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.OriginGroup",
):
    '''An Origin that represents a group.

    Consists of a primary Origin,
    and a fallback Origin called when the primary returns one of the provided HTTP status codes.

    :exampleMetadata: infused

    Example::

        my_bucket = s3.Bucket(self, "myBucket")
        cloudfront.Distribution(self, "myDist",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.OriginGroup(
                    primary_origin=origins.S3Origin(my_bucket),
                    fallback_origin=origins.HttpOrigin("www.example.com"),
                    # optional, defaults to: 500, 502, 503 and 504
                    fallback_status_codes=[404]
                )
            )
        )
    '''

    def __init__(
        self,
        *,
        fallback_origin: _IOrigin_83d4c1fa,
        primary_origin: _IOrigin_83d4c1fa,
        fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''
        :param fallback_origin: The fallback origin that should serve requests when the primary fails.
        :param primary_origin: The primary origin that should serve requests for this group.
        :param fallback_status_codes: The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin. Default: - 500, 502, 503 and 504
        '''
        props = OriginGroupProps(
            fallback_origin=fallback_origin,
            primary_origin=primary_origin,
            fallback_status_codes=fallback_status_codes,
        )

        jsii.create(self.__class__, self, [props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        origin_id: builtins.str,
    ) -> _OriginBindConfig_25a57096:
        '''The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__428f309ea8c48c002d77db24802c77164c9607d40492e08c4b243080f941ff61)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = _OriginBindOptions_088c2b51(origin_id=origin_id)

        return typing.cast(_OriginBindConfig_25a57096, jsii.invoke(self, "bind", [scope, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.OriginGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "fallback_origin": "fallbackOrigin",
        "primary_origin": "primaryOrigin",
        "fallback_status_codes": "fallbackStatusCodes",
    },
)
class OriginGroupProps:
    def __init__(
        self,
        *,
        fallback_origin: _IOrigin_83d4c1fa,
        primary_origin: _IOrigin_83d4c1fa,
        fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
    ) -> None:
        '''Construction properties for ``OriginGroup``.

        :param fallback_origin: The fallback origin that should serve requests when the primary fails.
        :param primary_origin: The primary origin that should serve requests for this group.
        :param fallback_status_codes: The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin. Default: - 500, 502, 503 and 504

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(
                    origin=origins.OriginGroup(
                        primary_origin=origins.S3Origin(my_bucket),
                        fallback_origin=origins.HttpOrigin("www.example.com"),
                        # optional, defaults to: 500, 502, 503 and 504
                        fallback_status_codes=[404]
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3d6baf80fcac5a22fc2c985c83f9022e23b11075b338c076ac86172fff7d7e8b)
            check_type(argname="argument fallback_origin", value=fallback_origin, expected_type=type_hints["fallback_origin"])
            check_type(argname="argument primary_origin", value=primary_origin, expected_type=type_hints["primary_origin"])
            check_type(argname="argument fallback_status_codes", value=fallback_status_codes, expected_type=type_hints["fallback_status_codes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "fallback_origin": fallback_origin,
            "primary_origin": primary_origin,
        }
        if fallback_status_codes is not None:
            self._values["fallback_status_codes"] = fallback_status_codes

    @builtins.property
    def fallback_origin(self) -> _IOrigin_83d4c1fa:
        '''The fallback origin that should serve requests when the primary fails.'''
        result = self._values.get("fallback_origin")
        assert result is not None, "Required property 'fallback_origin' is missing"
        return typing.cast(_IOrigin_83d4c1fa, result)

    @builtins.property
    def primary_origin(self) -> _IOrigin_83d4c1fa:
        '''The primary origin that should serve requests for this group.'''
        result = self._values.get("primary_origin")
        assert result is not None, "Required property 'primary_origin' is missing"
        return typing.cast(_IOrigin_83d4c1fa, result)

    @builtins.property
    def fallback_status_codes(self) -> typing.Optional[typing.List[jsii.Number]]:
        '''The list of HTTP status codes that, when returned from the primary origin, would cause querying the fallback origin.

        :default: - 500, 502, 503 and 504
        '''
        result = self._values.get("fallback_status_codes")
        return typing.cast(typing.Optional[typing.List[jsii.Number]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "OriginGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RestApiOrigin(
    _OriginBase_b8fe5bcc,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.RestApiOrigin",
):
    '''An Origin for an API Gateway REST API.

    :exampleMetadata: infused

    Example::

        # api: apigateway.RestApi
        
        cloudfront.Distribution(self, "Distribution",
            default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api))
        )
    '''

    def __init__(
        self,
        rest_api: _RestApi_777c8238,
        *,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param rest_api: -
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56b6a9ee9b4e8ac821a25cc86fc2ff9f7490081ff9a35a5c551216af6a6ab722)
            check_type(argname="argument rest_api", value=rest_api, expected_type=type_hints["rest_api"])
        props = RestApiOriginProps(
            keepalive_timeout=keepalive_timeout,
            read_timeout=read_timeout,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [rest_api, props])

    @jsii.member(jsii_name="renderCustomOriginConfig")
    def _render_custom_origin_config(
        self,
    ) -> typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty]:
        return typing.cast(typing.Optional[_CfnDistribution_d9ad3595.CustomOriginConfigProperty], jsii.invoke(self, "renderCustomOriginConfig", []))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.RestApiOriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "keepalive_timeout": "keepaliveTimeout",
        "read_timeout": "readTimeout",
    },
)
class RestApiOriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
        read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Properties for an Origin for an API Gateway REST API.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param keepalive_timeout: Specifies how long, in seconds, CloudFront persists its connection to the origin. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(5)
        :param read_timeout: Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout. The valid range is from 1 to 180 seconds, inclusive. Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time. Default: Duration.seconds(30)

        :exampleMetadata: infused

        Example::

            # api: apigateway.RestApi
            
            cloudfront.Distribution(self, "Distribution",
                default_behavior=cloudfront.BehaviorOptions(origin=origins.RestApiOrigin(api, origin_path="/custom-origin-path"))
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eca8c8f76c90eb80c45563b1a8eb9b9f1868ad621b45412a4cb935297b4d303)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument keepalive_timeout", value=keepalive_timeout, expected_type=type_hints["keepalive_timeout"])
            check_type(argname="argument read_timeout", value=read_timeout, expected_type=type_hints["read_timeout"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if keepalive_timeout is not None:
            self._values["keepalive_timeout"] = keepalive_timeout
        if read_timeout is not None:
            self._values["read_timeout"] = read_timeout

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def keepalive_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront persists its connection to the origin.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(5)
        '''
        result = self._values.get("keepalive_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def read_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''Specifies how long, in seconds, CloudFront waits for a response from the origin, also known as the origin response timeout.

        The valid range is from 1 to 180 seconds, inclusive.

        Note that values over 60 seconds are possible only after a limit increase request for the origin response timeout quota
        has been approved in the target account; otherwise, values over 60 seconds will produce an error at deploy time.

        :default: Duration.seconds(30)
        '''
        result = self._values.get("read_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RestApiOriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IOrigin_83d4c1fa)
class S3Origin(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3Origin",
):
    '''An Origin that is backed by an S3 bucket.

    If the bucket is configured for website hosting, this origin will be configured to use the bucket as an
    HTTP server origin and will use the bucket's configured website redirects and error handling. Otherwise,
    the origin is created as a bucket origin and will use CloudFront's redirect and error handling.

    :exampleMetadata: infused

    Example::

        # Adding an existing Lambda@Edge function created in a different stack
        # to a CloudFront distribution.
        # s3_bucket: s3.Bucket
        
        function_version = lambda_.Version.from_version_arn(self, "Version", "arn:aws:lambda:us-east-1:123456789012:function:functionName:1")
        
        cloudfront.Distribution(self, "distro",
            default_behavior=cloudfront.BehaviorOptions(
                origin=origins.S3Origin(s3_bucket),
                edge_lambdas=[cloudfront.EdgeLambda(
                    function_version=function_version,
                    event_type=cloudfront.LambdaEdgeEventType.VIEWER_REQUEST
                )
                ]
            )
        )
    '''

    def __init__(
        self,
        bucket: _IBucket_42e086fd,
        *,
        origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
        origin_path: typing.Optional[builtins.str] = None,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param bucket: -
        :param origin_access_identity: An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: - An Origin Access Identity will be created.
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ba8623373b0faa9ac55c816167da21a58e0753e0dd032b1f3e6ccd0bd977994)
            check_type(argname="argument bucket", value=bucket, expected_type=type_hints["bucket"])
        props = S3OriginProps(
            origin_access_identity=origin_access_identity,
            origin_path=origin_path,
            connection_attempts=connection_attempts,
            connection_timeout=connection_timeout,
            custom_headers=custom_headers,
            origin_id=origin_id,
            origin_shield_enabled=origin_shield_enabled,
            origin_shield_region=origin_shield_region,
        )

        jsii.create(self.__class__, self, [bucket, props])

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        scope: _constructs_77d1e7e8.Construct,
        *,
        origin_id: builtins.str,
    ) -> _OriginBindConfig_25a57096:
        '''The method called when a given Origin is added (for the first time) to a Distribution.

        :param scope: -
        :param origin_id: The identifier of this Origin, as assigned by the Distribution this Origin has been used added to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1731b0d7a385b196730b287be11e2cb13fa03d064ae3ffbfd55c5422a8f2c430)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
        options = _OriginBindOptions_088c2b51(origin_id=origin_id)

        return typing.cast(_OriginBindConfig_25a57096, jsii.invoke(self, "bind", [scope, options]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_cloudfront_origins.S3OriginProps",
    jsii_struct_bases=[_OriginProps_0675928d],
    name_mapping={
        "connection_attempts": "connectionAttempts",
        "connection_timeout": "connectionTimeout",
        "custom_headers": "customHeaders",
        "origin_id": "originId",
        "origin_shield_enabled": "originShieldEnabled",
        "origin_shield_region": "originShieldRegion",
        "origin_path": "originPath",
        "origin_access_identity": "originAccessIdentity",
    },
)
class S3OriginProps(_OriginProps_0675928d):
    def __init__(
        self,
        *,
        connection_attempts: typing.Optional[jsii.Number] = None,
        connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
        custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        origin_id: typing.Optional[builtins.str] = None,
        origin_shield_enabled: typing.Optional[builtins.bool] = None,
        origin_shield_region: typing.Optional[builtins.str] = None,
        origin_path: typing.Optional[builtins.str] = None,
        origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
    ) -> None:
        '''Properties to use to customize an S3 Origin.

        :param connection_attempts: The number of times that CloudFront attempts to connect to the origin; valid values are 1, 2, or 3 attempts. Default: 3
        :param connection_timeout: The number of seconds that CloudFront waits when trying to establish a connection to the origin. Valid values are 1-10 seconds, inclusive. Default: Duration.seconds(10)
        :param custom_headers: A list of HTTP header names and values that CloudFront adds to requests it sends to the origin. Default: {}
        :param origin_id: A unique identifier for the origin. This value must be unique within the distribution. Default: - an originid will be generated for you
        :param origin_shield_enabled: Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false. Default: - true
        :param origin_shield_region: When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance. Default: - origin shield not enabled
        :param origin_path: An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin. Must begin, but not end, with '/' (e.g., '/production/images'). Default: '/'
        :param origin_access_identity: An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket. Default: - An Origin Access Identity will be created.

        :exampleMetadata: infused

        Example::

            my_bucket = s3.Bucket(self, "myBucket")
            cloudfront.Distribution(self, "myDist",
                default_behavior=cloudfront.BehaviorOptions(origin=origins.S3Origin(my_bucket,
                    custom_headers={
                        "Foo": "bar"
                    }
                ))
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bbd2a0ca1bf4d32899d90ea633e3ac416a6fa29972ee055a5866ec269b24307e)
            check_type(argname="argument connection_attempts", value=connection_attempts, expected_type=type_hints["connection_attempts"])
            check_type(argname="argument connection_timeout", value=connection_timeout, expected_type=type_hints["connection_timeout"])
            check_type(argname="argument custom_headers", value=custom_headers, expected_type=type_hints["custom_headers"])
            check_type(argname="argument origin_id", value=origin_id, expected_type=type_hints["origin_id"])
            check_type(argname="argument origin_shield_enabled", value=origin_shield_enabled, expected_type=type_hints["origin_shield_enabled"])
            check_type(argname="argument origin_shield_region", value=origin_shield_region, expected_type=type_hints["origin_shield_region"])
            check_type(argname="argument origin_path", value=origin_path, expected_type=type_hints["origin_path"])
            check_type(argname="argument origin_access_identity", value=origin_access_identity, expected_type=type_hints["origin_access_identity"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if connection_attempts is not None:
            self._values["connection_attempts"] = connection_attempts
        if connection_timeout is not None:
            self._values["connection_timeout"] = connection_timeout
        if custom_headers is not None:
            self._values["custom_headers"] = custom_headers
        if origin_id is not None:
            self._values["origin_id"] = origin_id
        if origin_shield_enabled is not None:
            self._values["origin_shield_enabled"] = origin_shield_enabled
        if origin_shield_region is not None:
            self._values["origin_shield_region"] = origin_shield_region
        if origin_path is not None:
            self._values["origin_path"] = origin_path
        if origin_access_identity is not None:
            self._values["origin_access_identity"] = origin_access_identity

    @builtins.property
    def connection_attempts(self) -> typing.Optional[jsii.Number]:
        '''The number of times that CloudFront attempts to connect to the origin;

        valid values are 1, 2, or 3 attempts.

        :default: 3
        '''
        result = self._values.get("connection_attempts")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def connection_timeout(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The number of seconds that CloudFront waits when trying to establish a connection to the origin.

        Valid values are 1-10 seconds, inclusive.

        :default: Duration.seconds(10)
        '''
        result = self._values.get("connection_timeout")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def custom_headers(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A list of HTTP header names and values that CloudFront adds to requests it sends to the origin.

        :default: {}
        '''
        result = self._values.get("custom_headers")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def origin_id(self) -> typing.Optional[builtins.str]:
        '''A unique identifier for the origin.

        This value must be unique within the distribution.

        :default: - an originid will be generated for you
        '''
        result = self._values.get("origin_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_shield_enabled(self) -> typing.Optional[builtins.bool]:
        '''Origin Shield is enabled by setting originShieldRegion to a valid region, after this to disable Origin Shield again you must set this flag to false.

        :default: - true
        '''
        result = self._values.get("origin_shield_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def origin_shield_region(self) -> typing.Optional[builtins.str]:
        '''When you enable Origin Shield in the AWS Region that has the lowest latency to your origin, you can get better network performance.

        :default: - origin shield not enabled

        :see: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/origin-shield.html
        '''
        result = self._values.get("origin_shield_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_path(self) -> typing.Optional[builtins.str]:
        '''An optional path that CloudFront appends to the origin domain name when CloudFront requests content from the origin.

        Must begin, but not end, with '/' (e.g., '/production/images').

        :default: '/'
        '''
        result = self._values.get("origin_path")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def origin_access_identity(
        self,
    ) -> typing.Optional[_IOriginAccessIdentity_a922494c]:
        '''An optional Origin Access Identity of the origin identity cloudfront will use when calling your s3 bucket.

        :default: - An Origin Access Identity will be created.
        '''
        result = self._values.get("origin_access_identity")
        return typing.cast(typing.Optional[_IOriginAccessIdentity_a922494c], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3OriginProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HttpOrigin",
    "HttpOriginProps",
    "LoadBalancerV2Origin",
    "LoadBalancerV2OriginProps",
    "OriginGroup",
    "OriginGroupProps",
    "RestApiOrigin",
    "RestApiOriginProps",
    "S3Origin",
    "S3OriginProps",
]

publication.publish()

def _typecheckingstub__57d13f69f251622e0723aa73c3eb93e482e0deb7a7b1e8439c7d7ad35cfc0cc5(
    domain_name: builtins.str,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13f43bf70f0a97ee8ca0e4f7aca38d43089ed2bc254d5c2b57c73b51c1c2b9df(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e5124d4f469d6539077a529c09cfba685fe4a7037b9417216b18f6ccdba96c0(
    load_balancer: _ILoadBalancerV2_4c5c0fbb,
    *,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c72b63200b184ae3f51c9b6a19be2eef9bddae313ee00c7378396c0dcf586887(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    http_port: typing.Optional[jsii.Number] = None,
    https_port: typing.Optional[jsii.Number] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_ssl_protocols: typing.Optional[typing.Sequence[_OriginSslPolicy_d65cede2]] = None,
    protocol_policy: typing.Optional[_OriginProtocolPolicy_967ed73c] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__428f309ea8c48c002d77db24802c77164c9607d40492e08c4b243080f941ff61(
    scope: _constructs_77d1e7e8.Construct,
    *,
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3d6baf80fcac5a22fc2c985c83f9022e23b11075b338c076ac86172fff7d7e8b(
    *,
    fallback_origin: _IOrigin_83d4c1fa,
    primary_origin: _IOrigin_83d4c1fa,
    fallback_status_codes: typing.Optional[typing.Sequence[jsii.Number]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56b6a9ee9b4e8ac821a25cc86fc2ff9f7490081ff9a35a5c551216af6a6ab722(
    rest_api: _RestApi_777c8238,
    *,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eca8c8f76c90eb80c45563b1a8eb9b9f1868ad621b45412a4cb935297b4d303(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    keepalive_timeout: typing.Optional[_Duration_4839e8c3] = None,
    read_timeout: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ba8623373b0faa9ac55c816167da21a58e0753e0dd032b1f3e6ccd0bd977994(
    bucket: _IBucket_42e086fd,
    *,
    origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
    origin_path: typing.Optional[builtins.str] = None,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1731b0d7a385b196730b287be11e2cb13fa03d064ae3ffbfd55c5422a8f2c430(
    scope: _constructs_77d1e7e8.Construct,
    *,
    origin_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bbd2a0ca1bf4d32899d90ea633e3ac416a6fa29972ee055a5866ec269b24307e(
    *,
    connection_attempts: typing.Optional[jsii.Number] = None,
    connection_timeout: typing.Optional[_Duration_4839e8c3] = None,
    custom_headers: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    origin_id: typing.Optional[builtins.str] = None,
    origin_shield_enabled: typing.Optional[builtins.bool] = None,
    origin_shield_region: typing.Optional[builtins.str] = None,
    origin_path: typing.Optional[builtins.str] = None,
    origin_access_identity: typing.Optional[_IOriginAccessIdentity_a922494c] = None,
) -> None:
    """Type checking stubs"""
    pass
