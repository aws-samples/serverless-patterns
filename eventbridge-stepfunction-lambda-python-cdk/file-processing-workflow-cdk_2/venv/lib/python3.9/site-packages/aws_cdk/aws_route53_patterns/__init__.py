'''
# CDK Construct library for higher-level Route 53 Constructs

This library provides higher-level Amazon Route 53 constructs which follow common
architectural patterns.

## HTTPS Redirect

If you want to speed up delivery of your web content, you can use Amazon CloudFront,
the AWS content delivery network (CDN). CloudFront can deliver your entire website
—including dynamic, static, streaming, and interactive content—by using a global
network of edge locations. Requests for your content are automatically routed to the
edge location that gives your users the lowest latency.

This construct allows creating a redirect from domainA to domainB using Amazon
CloudFront and Amazon S3. You can specify multiple domains to be redirected.
[Learn more](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html) about routing traffic to a CloudFront web distribution.

The `HttpsRedirect` constructs creates:

* Amazon CloudFront distribution - makes website available from data centres
  around the world
* Amazon S3 bucket - empty bucket used for website hosting redirect (`websiteRedirect`) capabilities.
* Amazon Route 53 A/AAAA Alias records - routes traffic to the CloudFront distribution
* AWS Certificate Manager certificate - SSL/TLS certificate used by
  CloudFront for your domain

⚠️ The stack/construct can be used in any region for configuring an HTTPS redirect.
The certificate created in Amazon Certificate Manager (ACM) will be in US East (N. Virginia)
region. If you use an existing certificate, the AWS region of the certificate
must be in US East (N. Virginia).

The following example creates an HTTPS redirect from `foo.example.com` to `bar.example.com`
As an existing certificate is not provided, one will be created in `us-east-1` by the CDK.

```python
patterns.HttpsRedirect(self, "Redirect",
    record_names=["foo.example.com"],
    target_domain="bar.example.com",
    zone=route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
        hosted_zone_id="ID",
        zone_name="example.com"
    )
)
```

To have `HttpsRedirect` use the `Certificate` construct as the default
created certificate instead of the deprecated `DnsValidatedCertificate`
construct, enable the `@aws-cdk/aws-route53-patters:useCertificate`
feature flag. If you are creating the stack in a region other than `us-east-1`
you must also enable `crossRegionReferences` on the stack.

```python
# app: App

stack = Stack(app, "Stack",
    cross_region_references=True,
    env=Environment(
        region="us-east-2"
    )
)

patterns.HttpsRedirect(self, "Redirect",
    record_names=["foo.example.com"],
    target_domain="bar.example.com",
    zone=route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
        hosted_zone_id="ID",
        zone_name="example.com"
    )
)
```

It is safe to upgrade to `@aws-cdk/aws-route53-patterns:useCertificate` since
the new certificate will be created and updated on the CloudFront distribution
before the old certificate is deleted.
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
from ..aws_certificatemanager import ICertificate as _ICertificate_c194c70b
from ..aws_route53 import IHostedZone as _IHostedZone_9a6907ad


class HttpsRedirect(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53_patterns.HttpsRedirect",
):
    '''Allows creating a domainA -> domainB redirect using CloudFront and S3.

    You can specify multiple domains to be redirected.

    :exampleMetadata: infused

    Example::

        patterns.HttpsRedirect(self, "Redirect",
            record_names=["foo.example.com"],
            target_domain="bar.example.com",
            zone=route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                hosted_zone_id="ID",
                zone_name="example.com"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        target_domain: builtins.str,
        zone: _IHostedZone_9a6907ad,
        certificate: typing.Optional[_ICertificate_c194c70b] = None,
        record_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param target_domain: The redirect target fully qualified domain name (FQDN). An alias record will be created that points to your CloudFront distribution. Root domain or sub-domain can be supplied.
        :param zone: Hosted zone of the domain which will be used to create alias record(s) from domain names in the hosted zone to the target domain. The hosted zone must contain entries for the domain name(s) supplied through ``recordNames`` that will redirect to the target domain. Domain names in the hosted zone can include a specific domain (example.com) and its subdomains (acme.example.com, zenith.example.com).
        :param certificate: The AWS Certificate Manager (ACM) certificate that will be associated with the CloudFront distribution that will be created. If provided, the certificate must be stored in us-east-1 (N. Virginia) Default: - A new certificate is created in us-east-1 (N. Virginia)
        :param record_names: The domain names that will redirect to ``targetDomain``. Default: - the domain name of the hosted zone
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ff68f7e0dc1eec5dad60ae4c71e2f21e862d0a1879bb52d096b24101764cf058)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HttpsRedirectProps(
            target_domain=target_domain,
            zone=zone,
            certificate=certificate,
            record_names=record_names,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53_patterns.HttpsRedirectProps",
    jsii_struct_bases=[],
    name_mapping={
        "target_domain": "targetDomain",
        "zone": "zone",
        "certificate": "certificate",
        "record_names": "recordNames",
    },
)
class HttpsRedirectProps:
    def __init__(
        self,
        *,
        target_domain: builtins.str,
        zone: _IHostedZone_9a6907ad,
        certificate: typing.Optional[_ICertificate_c194c70b] = None,
        record_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties to configure an HTTPS Redirect.

        :param target_domain: The redirect target fully qualified domain name (FQDN). An alias record will be created that points to your CloudFront distribution. Root domain or sub-domain can be supplied.
        :param zone: Hosted zone of the domain which will be used to create alias record(s) from domain names in the hosted zone to the target domain. The hosted zone must contain entries for the domain name(s) supplied through ``recordNames`` that will redirect to the target domain. Domain names in the hosted zone can include a specific domain (example.com) and its subdomains (acme.example.com, zenith.example.com).
        :param certificate: The AWS Certificate Manager (ACM) certificate that will be associated with the CloudFront distribution that will be created. If provided, the certificate must be stored in us-east-1 (N. Virginia) Default: - A new certificate is created in us-east-1 (N. Virginia)
        :param record_names: The domain names that will redirect to ``targetDomain``. Default: - the domain name of the hosted zone

        :exampleMetadata: infused

        Example::

            patterns.HttpsRedirect(self, "Redirect",
                record_names=["foo.example.com"],
                target_domain="bar.example.com",
                zone=route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                    hosted_zone_id="ID",
                    zone_name="example.com"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__72f6f834d63b74800825b794cdf644f1464edeeadd63af405be3512f22b37c7d)
            check_type(argname="argument target_domain", value=target_domain, expected_type=type_hints["target_domain"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument certificate", value=certificate, expected_type=type_hints["certificate"])
            check_type(argname="argument record_names", value=record_names, expected_type=type_hints["record_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "target_domain": target_domain,
            "zone": zone,
        }
        if certificate is not None:
            self._values["certificate"] = certificate
        if record_names is not None:
            self._values["record_names"] = record_names

    @builtins.property
    def target_domain(self) -> builtins.str:
        '''The redirect target fully qualified domain name (FQDN).

        An alias record
        will be created that points to your CloudFront distribution. Root domain
        or sub-domain can be supplied.
        '''
        result = self._values.get("target_domain")
        assert result is not None, "Required property 'target_domain' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone(self) -> _IHostedZone_9a6907ad:
        '''Hosted zone of the domain which will be used to create alias record(s) from domain names in the hosted zone to the target domain.

        The hosted zone must
        contain entries for the domain name(s) supplied through ``recordNames`` that
        will redirect to the target domain.

        Domain names in the hosted zone can include a specific domain (example.com)
        and its subdomains (acme.example.com, zenith.example.com).
        '''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(_IHostedZone_9a6907ad, result)

    @builtins.property
    def certificate(self) -> typing.Optional[_ICertificate_c194c70b]:
        '''The AWS Certificate Manager (ACM) certificate that will be associated with the CloudFront distribution that will be created.

        If provided, the certificate must be
        stored in us-east-1 (N. Virginia)

        :default: - A new certificate is created in us-east-1 (N. Virginia)
        '''
        result = self._values.get("certificate")
        return typing.cast(typing.Optional[_ICertificate_c194c70b], result)

    @builtins.property
    def record_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The domain names that will redirect to ``targetDomain``.

        :default: - the domain name of the hosted zone
        '''
        result = self._values.get("record_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HttpsRedirectProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "HttpsRedirect",
    "HttpsRedirectProps",
]

publication.publish()

def _typecheckingstub__ff68f7e0dc1eec5dad60ae4c71e2f21e862d0a1879bb52d096b24101764cf058(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target_domain: builtins.str,
    zone: _IHostedZone_9a6907ad,
    certificate: typing.Optional[_ICertificate_c194c70b] = None,
    record_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__72f6f834d63b74800825b794cdf644f1464edeeadd63af405be3512f22b37c7d(
    *,
    target_domain: builtins.str,
    zone: _IHostedZone_9a6907ad,
    certificate: typing.Optional[_ICertificate_c194c70b] = None,
    record_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass
