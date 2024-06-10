'''
# AWS Certificate Manager Construct Library

AWS Certificate Manager (ACM) handles the complexity of creating, storing, and renewing public and private SSL/TLS X.509 certificates and keys that
protect your AWS websites and applications. ACM certificates can secure singular domain names, multiple specific domain names, wildcard domains, or
combinations of these. ACM wildcard certificates can protect an unlimited number of subdomains.

This package provides Constructs for provisioning and referencing ACM certificates which can be used with CloudFront and ELB.

After requesting a certificate, you will need to prove that you own the
domain in question before the certificate will be granted. The CloudFormation
deployment will wait until this verification process has been completed.

Because of this wait time, when using manual validation methods, it's better
to provision your certificates either in a separate stack from your main
service, or provision them manually and import them into your CDK application.

**Note:** There is a limit on total number of ACM certificates that can be requested on an account and region within a year.
The default limit is 2000, but this limit may be (much) lower on new AWS accounts.
See https://docs.aws.amazon.com/acm/latest/userguide/acm-limits.html for more information.

## DNS validation

DNS validation is the preferred method to validate domain ownership, as it has a number of advantages over email validation.
See also [Validate with DNS](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html)
in the AWS Certificate Manager User Guide.

If Amazon Route 53 is your DNS provider for the requested domain, the DNS record can be
created automatically:

```python
my_hosted_zone = route53.HostedZone(self, "HostedZone",
    zone_name="example.com"
)
acm.Certificate(self, "Certificate",
    domain_name="hello.example.com",
    certificate_name="Hello World Service",  # Optionally provide an certificate name
    validation=acm.CertificateValidation.from_dns(my_hosted_zone)
)
```

If Route 53 is not your DNS provider, the DNS records must be added manually and the stack will not complete
creating until the records are added.

```python
acm.Certificate(self, "Certificate",
    domain_name="hello.example.com",
    validation=acm.CertificateValidation.from_dns()
)
```

When working with multiple domains, use the `CertificateValidation.fromDnsMultiZone()`:

```python
example_com = route53.HostedZone(self, "ExampleCom",
    zone_name="example.com"
)
example_net = route53.HostedZone(self, "ExampleNet",
    zone_name="example.net"
)

cert = acm.Certificate(self, "Certificate",
    domain_name="test.example.com",
    subject_alternative_names=["cool.example.com", "test.example.net"],
    validation=acm.CertificateValidation.from_dns_multi_zone({
        "test.example.com": example_com,
        "cool.example.com": example_com,
        "test.example.net": example_net
    })
)
```

## Email validation

Email-validated certificates (the default) are validated by receiving an
email on one of a number of predefined domains and following the instructions
in the email.

See [Validate with Email](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html)
in the AWS Certificate Manager User Guide.

```python
acm.Certificate(self, "Certificate",
    domain_name="hello.example.com",
    validation=acm.CertificateValidation.from_email()
)
```

## Cross-region Certificates

ACM certificates that are used with CloudFront -- or higher-level constructs which rely on CloudFront -- must be in the `us-east-1` region.
CloudFormation allows you to create a Stack with a CloudFront distribution in any region. In order
to create an ACM certificate in us-east-1 and reference it in a CloudFront distribution is a
different region, it is recommended to perform a multi stack deployment.

Enable the Stack property `crossRegionReferences`
in order to access the cross stack/region certificate.

> **This feature is currently experimental**

```python
from aws_cdk import aws_cloudfront as cloudfront, aws_cloudfront_origins as origins
# app: App


stack1 = Stack(app, "Stack1",
    env=Environment(
        region="us-east-1"
    ),
    cross_region_references=True
)
cert = acm.Certificate(stack1, "Cert",
    domain_name="*.example.com",
    validation=acm.CertificateValidation.from_dns(PublicHostedZone.from_hosted_zone_id(stack1, "Zone", "ZONE_ID"))
)

stack2 = Stack(app, "Stack2",
    env=Environment(
        region="us-east-2"
    ),
    cross_region_references=True
)

cloudfront.Distribution(stack2, "Distribution",
    default_behavior=cloudfront.BehaviorOptions(
        origin=origins.HttpOrigin("example.com")
    ),
    domain_names=["dev.example.com"],
    certificate=cert
)
```

## Requesting private certificates

AWS Certificate Manager can create [private certificates](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html) issued by [Private Certificate Authority (PCA)](https://docs.aws.amazon.com/acm-pca/latest/userguide/PcaWelcome.html). Validation of private certificates is not necessary.

```python
import aws_cdk.aws_acmpca as acmpca


acm.PrivateCertificate(self, "PrivateCertificate",
    domain_name="test.example.com",
    subject_alternative_names=["cool.example.com", "test.example.net"],  # optional
    certificate_authority=acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CA", "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/023077d8-2bfa-4eb0-8f22-05c96deade77"),
    key_algorithm=acm.KeyAlgorithm.RSA_2048
)
```

## Requesting certificates without transparency logging

Transparency logging can be opted out of for AWS Certificate Manager certificates. See [opting out of certificate transparency logging](https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency) for limits.

```python
acm.Certificate(self, "Certificate",
    domain_name="test.example.com",
    transparency_logging_enabled=False
)
```

## Key Algorithms

To specify the algorithm of the public and private key pair that your certificate uses to encrypt data use the `keyAlgorithm` property.

Algorithms supported for an ACM certificate request include:

* `RSA_2048`
* `EC_prime256v1`
* `EC_secp384r1`

```python
acm.Certificate(self, "Certificate",
    domain_name="test.example.com",
    key_algorithm=acm.KeyAlgorithm.EC_PRIME256V1
)
```

> Visit [Key algorithms](https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms.title) for more details.

## Importing

If you want to import an existing certificate, you can do so from its ARN:

```python
arn = "arn:aws:..."
certificate = acm.Certificate.from_certificate_arn(self, "Certificate", arn)
```

## Sharing between Stacks

To share the certificate between stacks in the same CDK application, simply
pass the `Certificate` object between the stacks.

## Metrics

The `DaysToExpiry` metric is available via the `metricDaysToExpiry` method for
all certificates. This metric is emitted by AWS Certificates Manager once per
day until the certificate has effectively expired.

An alarm can be created to determine whether a certificate is soon due for
renewal ussing the following code:

```python
import aws_cdk.aws_cloudwatch as cloudwatch

# my_hosted_zone: route53.HostedZone

certificate = acm.Certificate(self, "Certificate",
    domain_name="hello.example.com",
    validation=acm.CertificateValidation.from_dns(my_hosted_zone)
)
certificate.metric_days_to_expiry().create_alarm(self, "Alarm",
    comparison_operator=cloudwatch.ComparisonOperator.LESS_THAN_THRESHOLD,
    evaluation_periods=1,
    threshold=45
)
```
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
    CfnTag as _CfnTag_f6864754,
    Duration as _Duration_4839e8c3,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    RemovalPolicy as _RemovalPolicy_9f93c814,
    Resource as _Resource_45bc6135,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_acmpca import ICertificateAuthority as _ICertificateAuthority_26727cab
from ..aws_cloudwatch import (
    Metric as _Metric_e396a4dc,
    MetricOptions as _MetricOptions_1788b62f,
    Unit as _Unit_61bc6f70,
)
from ..aws_iam import IRole as _IRole_235f5d8e
from ..aws_route53 import IHostedZone as _IHostedZone_9a6907ad


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_certificatemanager.CertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "certificate_name": "certificateName",
        "key_algorithm": "keyAlgorithm",
        "subject_alternative_names": "subjectAlternativeNames",
        "transparency_logging_enabled": "transparencyLoggingEnabled",
        "validation": "validation",
    },
)
class CertificateProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        certificate_name: typing.Optional[builtins.str] = None,
        key_algorithm: typing.Optional["KeyAlgorithm"] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        transparency_logging_enabled: typing.Optional[builtins.bool] = None,
        validation: typing.Optional["CertificateValidation"] = None,
    ) -> None:
        '''Properties for your certificate.

        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param certificate_name: The Certificate name. Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: the full, absolute path of this construct
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param transparency_logging_enabled: Enable or disable transparency logging for this certificate. Once a certificate has been logged, it cannot be removed from the log. Opting out at that point will have no effect. If you opt out of logging when you request a certificate and then choose later to opt back in, your certificate will not be logged until it is renewed. If you want the certificate to be logged immediately, we recommend that you issue a new one. Default: true
        :param validation: How to validate this certificate. Default: CertificateValidation.fromEmail()

        :exampleMetadata: infused

        Example::

            example_com = route53.HostedZone(self, "ExampleCom",
                zone_name="example.com"
            )
            example_net = route53.HostedZone(self, "ExampleNet",
                zone_name="example.net"
            )
            
            cert = acm.Certificate(self, "Certificate",
                domain_name="test.example.com",
                subject_alternative_names=["cool.example.com", "test.example.net"],
                validation=acm.CertificateValidation.from_dns_multi_zone({
                    "test.example.com": example_com,
                    "cool.example.com": example_com,
                    "test.example.net": example_net
                })
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0454180af2ed6575d11cf361cd5374f722ba32d4007970472aca57751d85258f)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
            check_type(argname="argument transparency_logging_enabled", value=transparency_logging_enabled, expected_type=type_hints["transparency_logging_enabled"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if key_algorithm is not None:
            self._values["key_algorithm"] = key_algorithm
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if transparency_logging_enabled is not None:
            self._values["transparency_logging_enabled"] = transparency_logging_enabled
        if validation is not None:
            self._values["validation"] = validation

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Fully-qualified domain name to request a certificate for.

        May contain wildcards, such as ``*.domain.com``.
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''The Certificate name.

        Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag

        :default: the full, absolute path of this construct
        '''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_algorithm(self) -> typing.Optional["KeyAlgorithm"]:
        '''Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data.

        :default: KeyAlgorithm.RSA_2048

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms.title
        '''
        result = self._values.get("key_algorithm")
        return typing.cast(typing.Optional["KeyAlgorithm"], result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names on your certificate.

        Use this to register alternative domain names that represent the same site.

        :default: - No additional FQDNs will be included as alternative domain names.
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def transparency_logging_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable transparency logging for this certificate.

        Once a certificate has been logged, it cannot be removed from the log.
        Opting out at that point will have no effect. If you opt out of logging
        when you request a certificate and then choose later to opt back in,
        your certificate will not be logged until it is renewed.
        If you want the certificate to be logged immediately, we recommend that you issue a new one.

        :default: true

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency
        '''
        result = self._values.get("transparency_logging_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validation(self) -> typing.Optional["CertificateValidation"]:
        '''How to validate this certificate.

        :default: CertificateValidation.fromEmail()
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional["CertificateValidation"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CertificateValidation(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.CertificateValidation",
):
    '''How to validate a certificate.

    :exampleMetadata: infused

    Example::

        example_com = route53.HostedZone(self, "ExampleCom",
            zone_name="example.com"
        )
        example_net = route53.HostedZone(self, "ExampleNet",
            zone_name="example.net"
        )
        
        cert = acm.Certificate(self, "Certificate",
            domain_name="test.example.com",
            subject_alternative_names=["cool.example.com", "test.example.net"],
            validation=acm.CertificateValidation.from_dns_multi_zone({
                "test.example.com": example_com,
                "cool.example.com": example_com,
                "test.example.net": example_net
            })
        )
    '''

    @jsii.member(jsii_name="fromDns")
    @builtins.classmethod
    def from_dns(
        cls,
        hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    ) -> "CertificateValidation":
        '''Validate the certificate with DNS.

        IMPORTANT: If ``hostedZone`` is not specified, DNS records must be added
        manually and the stack will not complete creating until the records are
        added.

        :param hosted_zone: the hosted zone where DNS records must be created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d311e81288c218c157a69a30ff08393bdbd454a8fc61208beab60d43ceb0d073)
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
        return typing.cast("CertificateValidation", jsii.sinvoke(cls, "fromDns", [hosted_zone]))

    @jsii.member(jsii_name="fromDnsMultiZone")
    @builtins.classmethod
    def from_dns_multi_zone(
        cls,
        hosted_zones: typing.Mapping[builtins.str, _IHostedZone_9a6907ad],
    ) -> "CertificateValidation":
        '''Validate the certificate with automatically created DNS records in multiple Amazon Route 53 hosted zones.

        :param hosted_zones: a map of hosted zones where DNS records must be created for the domains in the certificate.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e9e19a57c59056b6522867e062779dfe13086b375805e7484ac5b3b16e1288bc)
            check_type(argname="argument hosted_zones", value=hosted_zones, expected_type=type_hints["hosted_zones"])
        return typing.cast("CertificateValidation", jsii.sinvoke(cls, "fromDnsMultiZone", [hosted_zones]))

    @jsii.member(jsii_name="fromEmail")
    @builtins.classmethod
    def from_email(
        cls,
        validation_domains: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> "CertificateValidation":
        '''Validate the certificate with Email.

        IMPORTANT: if you are creating a certificate as part of your stack, the stack
        will not complete creating until you read and follow the instructions in the
        email that you will receive.

        ACM will send validation emails to the following addresses:

        admin@domain.com
        administrator@domain.com
        hostmaster@domain.com
        postmaster@domain.com
        webmaster@domain.com

        For every domain that you register.

        :param validation_domains: a map of validation domains to use for domains in the certificate.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e646dcc4d629169bb4daf43ef7ab70c779d7251a8c4a7997d32b8bd3627adc32)
            check_type(argname="argument validation_domains", value=validation_domains, expected_type=type_hints["validation_domains"])
        return typing.cast("CertificateValidation", jsii.sinvoke(cls, "fromEmail", [validation_domains]))

    @builtins.property
    @jsii.member(jsii_name="method")
    def method(self) -> "ValidationMethod":
        '''The validation method.'''
        return typing.cast("ValidationMethod", jsii.get(self, "method"))

    @builtins.property
    @jsii.member(jsii_name="props")
    def props(self) -> "CertificationValidationProps":
        '''Certification validation properties.'''
        return typing.cast("CertificationValidationProps", jsii.get(self, "props"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_certificatemanager.CertificationValidationProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone": "hostedZone",
        "hosted_zones": "hostedZones",
        "method": "method",
        "validation_domains": "validationDomains",
    },
)
class CertificationValidationProps:
    def __init__(
        self,
        *,
        hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
        hosted_zones: typing.Optional[typing.Mapping[builtins.str, _IHostedZone_9a6907ad]] = None,
        method: typing.Optional["ValidationMethod"] = None,
        validation_domains: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''Properties for certificate validation.

        :param hosted_zone: Hosted zone to use for DNS validation. Default: - use email validation
        :param hosted_zones: A map of hosted zones to use for DNS validation. Default: - use ``hostedZone``
        :param method: Validation method. Default: ValidationMethod.EMAIL
        :param validation_domains: Validation domains to use for email validation. Default: - Apex domain

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_certificatemanager as certificatemanager
            from aws_cdk import aws_route53 as route53
            
            # hosted_zone: route53.HostedZone
            
            certification_validation_props = certificatemanager.CertificationValidationProps(
                hosted_zone=hosted_zone,
                hosted_zones={
                    "hosted_zones_key": hosted_zone
                },
                method=certificatemanager.ValidationMethod.EMAIL,
                validation_domains={
                    "validation_domains_key": "validationDomains"
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e752fd91fd754625f454d3983095bf28bb2a1e1fbd5d307a0d1662659800154)
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
            check_type(argname="argument hosted_zones", value=hosted_zones, expected_type=type_hints["hosted_zones"])
            check_type(argname="argument method", value=method, expected_type=type_hints["method"])
            check_type(argname="argument validation_domains", value=validation_domains, expected_type=type_hints["validation_domains"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hosted_zone is not None:
            self._values["hosted_zone"] = hosted_zone
        if hosted_zones is not None:
            self._values["hosted_zones"] = hosted_zones
        if method is not None:
            self._values["method"] = method
        if validation_domains is not None:
            self._values["validation_domains"] = validation_domains

    @builtins.property
    def hosted_zone(self) -> typing.Optional[_IHostedZone_9a6907ad]:
        '''Hosted zone to use for DNS validation.

        :default: - use email validation
        '''
        result = self._values.get("hosted_zone")
        return typing.cast(typing.Optional[_IHostedZone_9a6907ad], result)

    @builtins.property
    def hosted_zones(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, _IHostedZone_9a6907ad]]:
        '''A map of hosted zones to use for DNS validation.

        :default: - use ``hostedZone``
        '''
        result = self._values.get("hosted_zones")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, _IHostedZone_9a6907ad]], result)

    @builtins.property
    def method(self) -> typing.Optional["ValidationMethod"]:
        '''Validation method.

        :default: ValidationMethod.EMAIL
        '''
        result = self._values.get("method")
        return typing.cast(typing.Optional["ValidationMethod"], result)

    @builtins.property
    def validation_domains(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Validation domains to use for email validation.

        :default: - Apex domain
        '''
        result = self._values.get("validation_domains")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CertificationValidationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnAccount(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.CfnAccount",
):
    '''The ``AWS::CertificateManager::Account`` resource defines the expiry event configuration that determines the number of days prior to expiry when ACM starts generating EventBridge events.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html
    :cloudformationResource: AWS::CertificateManager::Account
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_certificatemanager as certificatemanager
        
        cfn_account = certificatemanager.CfnAccount(self, "MyCfnAccount",
            expiry_events_configuration=certificatemanager.CfnAccount.ExpiryEventsConfigurationProperty(
                days_before_expiry=123
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        expiry_events_configuration: typing.Union[_IResolvable_da3f097b, typing.Union["CfnAccount.ExpiryEventsConfigurationProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param expiry_events_configuration: Object containing expiration events options associated with an AWS account . For more information, see `ExpiryEventsConfiguration <https://docs.aws.amazon.com/acm/latest/APIReference/API_ExpiryEventsConfiguration.html>`_ in the API reference.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__db4f656c3005938d36870ee742d58c361b2595cfa8e6518fe38589b36fa0255d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountProps(
            expiry_events_configuration=expiry_events_configuration
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb75c7a5c08bac926fc28e0787cb2048b7cf11214a8eb2398e88170bf00af154)
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
            type_hints = typing.get_type_hints(_typecheckingstub__c8ba0fa95f8656708a4d80a6f060f0f04c7d3ec6e81e8476b2d640250b079a7e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrAccountId")
    def attr_account_id(self) -> builtins.str:
        '''ID of the AWS account that owns the certificate.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="expiryEventsConfiguration")
    def expiry_events_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnAccount.ExpiryEventsConfigurationProperty"]:
        '''Object containing expiration events options associated with an AWS account .'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnAccount.ExpiryEventsConfigurationProperty"], jsii.get(self, "expiryEventsConfiguration"))

    @expiry_events_configuration.setter
    def expiry_events_configuration(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnAccount.ExpiryEventsConfigurationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c44e33adc270e269d609b1c233392549a56a49e07e3459a57e1ecdb35bebeba3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expiryEventsConfiguration", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_certificatemanager.CfnAccount.ExpiryEventsConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"days_before_expiry": "daysBeforeExpiry"},
    )
    class ExpiryEventsConfigurationProperty:
        def __init__(
            self,
            *,
            days_before_expiry: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Object containing expiration events options associated with an AWS account .

            For more information, see `ExpiryEventsConfiguration <https://docs.aws.amazon.com/acm/latest/APIReference/API_ExpiryEventsConfiguration.html>`_ in the API reference.

            :param days_before_expiry: This option specifies the number of days prior to certificate expiration when ACM starts generating ``EventBridge`` events. ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_certificatemanager as certificatemanager
                
                expiry_events_configuration_property = certificatemanager.CfnAccount.ExpiryEventsConfigurationProperty(
                    days_before_expiry=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ad7aae0c4eae9319d3ebf2aff5a7a88275d784bac367f81cdc0d088e05e5a1fa)
                check_type(argname="argument days_before_expiry", value=days_before_expiry, expected_type=type_hints["days_before_expiry"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if days_before_expiry is not None:
                self._values["days_before_expiry"] = days_before_expiry

        @builtins.property
        def days_before_expiry(self) -> typing.Optional[jsii.Number]:
            '''This option specifies the number of days prior to certificate expiration when ACM starts generating ``EventBridge`` events.

            ACM sends one event per day per certificate until the certificate expires. By default, accounts receive events starting 45 days before certificate expiration.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-account-expiryeventsconfiguration.html#cfn-certificatemanager-account-expiryeventsconfiguration-daysbeforeexpiry
            '''
            result = self._values.get("days_before_expiry")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ExpiryEventsConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_certificatemanager.CfnAccountProps",
    jsii_struct_bases=[],
    name_mapping={"expiry_events_configuration": "expiryEventsConfiguration"},
)
class CfnAccountProps:
    def __init__(
        self,
        *,
        expiry_events_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccount.ExpiryEventsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnAccount``.

        :param expiry_events_configuration: Object containing expiration events options associated with an AWS account . For more information, see `ExpiryEventsConfiguration <https://docs.aws.amazon.com/acm/latest/APIReference/API_ExpiryEventsConfiguration.html>`_ in the API reference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_certificatemanager as certificatemanager
            
            cfn_account_props = certificatemanager.CfnAccountProps(
                expiry_events_configuration=certificatemanager.CfnAccount.ExpiryEventsConfigurationProperty(
                    days_before_expiry=123
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9591bf61584c328c9d03002934487f830e54f9aa231b003bcd4999ac2d265c5e)
            check_type(argname="argument expiry_events_configuration", value=expiry_events_configuration, expected_type=type_hints["expiry_events_configuration"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "expiry_events_configuration": expiry_events_configuration,
        }

    @builtins.property
    def expiry_events_configuration(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnAccount.ExpiryEventsConfigurationProperty]:
        '''Object containing expiration events options associated with an AWS account .

        For more information, see `ExpiryEventsConfiguration <https://docs.aws.amazon.com/acm/latest/APIReference/API_ExpiryEventsConfiguration.html>`_ in the API reference.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-account.html#cfn-certificatemanager-account-expiryeventsconfiguration
        '''
        result = self._values.get("expiry_events_configuration")
        assert result is not None, "Required property 'expiry_events_configuration' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnAccount.ExpiryEventsConfigurationProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCertificate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.CfnCertificate",
):
    '''The ``AWS::CertificateManager::Certificate`` resource requests an AWS Certificate Manager ( ACM ) certificate that you can use to enable secure connections.

    For example, you can deploy an ACM certificate to an Elastic Load Balancer to enable HTTPS support. For more information, see `RequestCertificate <https://docs.aws.amazon.com/acm/latest/APIReference/API_RequestCertificate.html>`_ in the AWS Certificate Manager API Reference.
    .. epigraph::

       When you use the ``AWS::CertificateManager::Certificate`` resource in a CloudFormation stack, domain validation is handled automatically if all three of the following are true: The certificate domain is hosted in Amazon Route 53, the domain resides in your AWS account , and you are using DNS validation.

       However, if the certificate uses email validation, or if the domain is not hosted in Route 53, then the stack will remain in the ``CREATE_IN_PROGRESS`` state. Further stack operations are delayed until you validate the certificate request, either by acting upon the instructions in the validation email, or by adding a CNAME record to your DNS configuration. For more information, see `Option 1: DNS Validation <https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html>`_ and `Option 2: Email Validation <https://docs.aws.amazon.com/acm/latest/userguide/email-validation.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html
    :cloudformationResource: AWS::CertificateManager::Certificate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_certificatemanager as certificatemanager
        
        cfn_certificate = certificatemanager.CfnCertificate(self, "MyCfnCertificate",
            domain_name="domainName",
        
            # the properties below are optional
            certificate_authority_arn="certificateAuthorityArn",
            certificate_transparency_logging_preference="certificateTransparencyLoggingPreference",
            domain_validation_options=[certificatemanager.CfnCertificate.DomainValidationOptionProperty(
                domain_name="domainName",
        
                # the properties below are optional
                hosted_zone_id="hostedZoneId",
                validation_domain="validationDomain"
            )],
            key_algorithm="keyAlgorithm",
            subject_alternative_names=["subjectAlternativeNames"],
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            validation_method="validationMethod"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        certificate_authority_arn: typing.Optional[builtins.str] = None,
        certificate_transparency_logging_preference: typing.Optional[builtins.str] = None,
        domain_validation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCertificate.DomainValidationOptionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        key_algorithm: typing.Optional[builtins.str] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        validation_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param domain_name: The fully qualified domain name (FQDN), such as www.example.com, with which you want to secure an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, ``*.example.com`` protects ``www.example.com`` , ``site.example.com`` , and ``images.example.com.``.
        :param certificate_authority_arn: The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the `AWS Private Certificate Authority <https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html>`_ user guide. The ARN must have the following form: ``arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012``
        :param certificate_transparency_logging_preference: You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt in by specifying ``ENABLED`` . If you do not specify a certificate transparency logging preference on a new CloudFormation template, or if you remove the logging preference from an existing template, this is the same as explicitly enabling the preference. Changing the certificate transparency logging preference will update the existing resource by calling ``UpdateCertificateOptions`` on the certificate. This action will not create a new resource.
        :param domain_validation_options: Domain information that domain name registrars use to verify your identity. .. epigraph:: In order for a AWS::CertificateManager::Certificate to be provisioned and validated in CloudFormation automatically, the ``DomainName`` property needs to be identical to one of the ``DomainName`` property supplied in DomainValidationOptions, if the ValidationMethod is **DNS**. Failing to keep them like-for-like will result in failure to create the domain validation records in Route53.
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some AWS services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the AWS service where you plan to deploy your certificate. For more information about selecting an algorithm, see `Key algorithms <https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms>`_ . .. epigraph:: Algorithms supported for an ACM certificate request include: - ``RSA_2048`` - ``EC_prime256v1`` - ``EC_secp384r1`` Other listed algorithms are for imported certificates only. > When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key. Default: RSA_2048
        :param subject_alternative_names: Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, you can add www.example.net to a certificate for which the ``DomainName`` field is www.example.com if users can reach your site by using either name.
        :param tags: Key-value pairs that can identify the certificate.
        :param validation_method: The method you want to use to validate that you own or control the domain associated with a public certificate. You can `validate with DNS <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`_ or `validate with email <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html>`_ . We recommend that you use DNS validation. If not specified, this property defaults to email validation.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f094b3f6a318b9501162c46d45eaf42466c16a9c333dd4021dc90258cf9f035)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCertificateProps(
            domain_name=domain_name,
            certificate_authority_arn=certificate_authority_arn,
            certificate_transparency_logging_preference=certificate_transparency_logging_preference,
            domain_validation_options=domain_validation_options,
            key_algorithm=key_algorithm,
            subject_alternative_names=subject_alternative_names,
            tags=tags,
            validation_method=validation_method,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cc2233ca7729f72437c57a4d626536c7b9150faa120045db48045a6b05d1e2a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__faa3f6cb4a71f233ceb715be42dc7e73f8cafc61728bc988a89693de4a66c690)
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
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The fully qualified domain name (FQDN), such as www.example.com, with which you want to secure an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, ``*.example.com`` protects ``www.example.com`` , ``site.example.com`` , and ``images.example.com.``.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ecc9a53026b3797b0ea9be214e046e5e413153b784ae59d56029cc943cad72d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)

    @builtins.property
    @jsii.member(jsii_name="certificateAuthorityArn")
    def certificate_authority_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateAuthorityArn"))

    @certificate_authority_arn.setter
    def certificate_authority_arn(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__58a46e864da863431c56823a56fc6f403857fef239765fe1b0400f623ed3493c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateAuthorityArn", value)

    @builtins.property
    @jsii.member(jsii_name="certificateTransparencyLoggingPreference")
    def certificate_transparency_logging_preference(
        self,
    ) -> typing.Optional[builtins.str]:
        '''You can opt out of certificate transparency logging by specifying the ``DISABLED`` option.

        Opt in by specifying ``ENABLED`` .
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "certificateTransparencyLoggingPreference"))

    @certificate_transparency_logging_preference.setter
    def certificate_transparency_logging_preference(
        self,
        value: typing.Optional[builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6946e1448636db36ed5e4ce9c801fc6db4c58d0f89d88789b24f93a2628abc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "certificateTransparencyLoggingPreference", value)

    @builtins.property
    @jsii.member(jsii_name="domainValidationOptions")
    def domain_validation_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.DomainValidationOptionProperty"]]]]:
        '''Domain information that domain name registrars use to verify your identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.DomainValidationOptionProperty"]]]], jsii.get(self, "domainValidationOptions"))

    @domain_validation_options.setter
    def domain_validation_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCertificate.DomainValidationOptionProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__56d2ab51aeb5167d471668b88dc595eaa9bda575e9837a78ce2083f388a77963)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainValidationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="keyAlgorithm")
    def key_algorithm(self) -> typing.Optional[builtins.str]:
        '''Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyAlgorithm"))

    @key_algorithm.setter
    def key_algorithm(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f976aa6e608ce4d5147cacebbe2f5d9a9585636c73462d403fcc81233f3bbd6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyAlgorithm", value)

    @builtins.property
    @jsii.member(jsii_name="subjectAlternativeNames")
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "subjectAlternativeNames"))

    @subject_alternative_names.setter
    def subject_alternative_names(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91f98018864a0f9c4b1051b73b5346df1e3dc533c89e840a02c7184c60f56d3a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subjectAlternativeNames", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can identify the certificate.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__42ebedfc2551a20aee372ba1bddbbd7ce73218848ab3d71aad89b1d372061b64)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="validationMethod")
    def validation_method(self) -> typing.Optional[builtins.str]:
        '''The method you want to use to validate that you own or control the domain associated with a public certificate.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "validationMethod"))

    @validation_method.setter
    def validation_method(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__234f3afa18fce0171662dad033e06d37b968d809b62314c6e62f4c1a4817ad7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "validationMethod", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_certificatemanager.CfnCertificate.DomainValidationOptionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_name": "domainName",
            "hosted_zone_id": "hostedZoneId",
            "validation_domain": "validationDomain",
        },
    )
    class DomainValidationOptionProperty:
        def __init__(
            self,
            *,
            domain_name: builtins.str,
            hosted_zone_id: typing.Optional[builtins.str] = None,
            validation_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''``DomainValidationOption`` is a property of the `AWS::CertificateManager::Certificate <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html>`_ resource that specifies the AWS Certificate Manager ( ACM ) certificate domain to validate. Depending on the chosen validation method, ACM checks the domain's DNS record for a validation CNAME, or it attempts to send a validation email message to the domain owner.

            :param domain_name: A fully qualified domain name (FQDN) in the certificate request.
            :param hosted_zone_id: The ``HostedZoneId`` option, which is available if you are using Route 53 as your domain registrar, causes ACM to add your CNAME to the domain record. Your list of ``DomainValidationOptions`` must contain one and only one of the domain-validation options, and the ``HostedZoneId`` can be used only when ``DNS`` is specified as your validation method. Use the Route 53 ``ListHostedZones`` API to discover IDs for available hosted zones. This option is required for publicly trusted certificates. .. epigraph:: The ``ListHostedZones`` API returns IDs in the format "/hostedzone/Z111111QQQQQQQ", but CloudFormation requires the IDs to be in the format "Z111111QQQQQQQ". When you change your ``DomainValidationOptions`` , a new resource is created.
            :param validation_domain: The domain name to which you want ACM to send validation emails. This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the ``DomainName`` value or a superdomain of the ``DomainName`` value. For example, if you request a certificate for ``testing.example.com`` , you can specify ``example.com`` as this value. In that case, ACM sends domain validation emails to the following five addresses: - admin@example.com - administrator@example.com - hostmaster@example.com - postmaster@example.com - webmaster@example.com

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_certificatemanager as certificatemanager
                
                domain_validation_option_property = certificatemanager.CfnCertificate.DomainValidationOptionProperty(
                    domain_name="domainName",
                
                    # the properties below are optional
                    hosted_zone_id="hostedZoneId",
                    validation_domain="validationDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c300d5c33d86322345b2adb8237375463f7f5ab1e486b11b34f49a04524807a3)
                check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument validation_domain", value=validation_domain, expected_type=type_hints["validation_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "domain_name": domain_name,
            }
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id
            if validation_domain is not None:
                self._values["validation_domain"] = validation_domain

        @builtins.property
        def domain_name(self) -> builtins.str:
            '''A fully qualified domain name (FQDN) in the certificate request.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-domainname
            '''
            result = self._values.get("domain_name")
            assert result is not None, "Required property 'domain_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            '''The ``HostedZoneId`` option, which is available if you are using Route 53 as your domain registrar, causes ACM to add your CNAME to the domain record.

            Your list of ``DomainValidationOptions`` must contain one and only one of the domain-validation options, and the ``HostedZoneId`` can be used only when ``DNS`` is specified as your validation method.

            Use the Route 53 ``ListHostedZones`` API to discover IDs for available hosted zones.

            This option is required for publicly trusted certificates.
            .. epigraph::

               The ``ListHostedZones`` API returns IDs in the format "/hostedzone/Z111111QQQQQQQ", but CloudFormation requires the IDs to be in the format "Z111111QQQQQQQ".

            When you change your ``DomainValidationOptions`` , a new resource is created.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def validation_domain(self) -> typing.Optional[builtins.str]:
            '''The domain name to which you want ACM to send validation emails.

            This domain name is the suffix of the email addresses that you want ACM to use. This must be the same as the ``DomainName`` value or a superdomain of the ``DomainName`` value. For example, if you request a certificate for ``testing.example.com`` , you can specify ``example.com`` as this value. In that case, ACM sends domain validation emails to the following five addresses:

            - admin@example.com
            - administrator@example.com
            - hostmaster@example.com
            - postmaster@example.com
            - webmaster@example.com

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-certificatemanager-certificate-domainvalidationoption.html#cfn-certificatemanager-certificate-domainvalidationoption-validationdomain
            '''
            result = self._values.get("validation_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DomainValidationOptionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_certificatemanager.CfnCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "certificate_authority_arn": "certificateAuthorityArn",
        "certificate_transparency_logging_preference": "certificateTransparencyLoggingPreference",
        "domain_validation_options": "domainValidationOptions",
        "key_algorithm": "keyAlgorithm",
        "subject_alternative_names": "subjectAlternativeNames",
        "tags": "tags",
        "validation_method": "validationMethod",
    },
)
class CfnCertificateProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        certificate_authority_arn: typing.Optional[builtins.str] = None,
        certificate_transparency_logging_preference: typing.Optional[builtins.str] = None,
        domain_validation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.DomainValidationOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
        key_algorithm: typing.Optional[builtins.str] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        validation_method: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnCertificate``.

        :param domain_name: The fully qualified domain name (FQDN), such as www.example.com, with which you want to secure an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, ``*.example.com`` protects ``www.example.com`` , ``site.example.com`` , and ``images.example.com.``.
        :param certificate_authority_arn: The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate. If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the `AWS Private Certificate Authority <https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html>`_ user guide. The ARN must have the following form: ``arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012``
        :param certificate_transparency_logging_preference: You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt in by specifying ``ENABLED`` . If you do not specify a certificate transparency logging preference on a new CloudFormation template, or if you remove the logging preference from an existing template, this is the same as explicitly enabling the preference. Changing the certificate transparency logging preference will update the existing resource by calling ``UpdateCertificateOptions`` on the certificate. This action will not create a new resource.
        :param domain_validation_options: Domain information that domain name registrars use to verify your identity. .. epigraph:: In order for a AWS::CertificateManager::Certificate to be provisioned and validated in CloudFormation automatically, the ``DomainName`` property needs to be identical to one of the ``DomainName`` property supplied in DomainValidationOptions, if the ValidationMethod is **DNS**. Failing to keep them like-for-like will result in failure to create the domain validation records in Route53.
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some AWS services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the AWS service where you plan to deploy your certificate. For more information about selecting an algorithm, see `Key algorithms <https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms>`_ . .. epigraph:: Algorithms supported for an ACM certificate request include: - ``RSA_2048`` - ``EC_prime256v1`` - ``EC_secp384r1`` Other listed algorithms are for imported certificates only. > When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key. Default: RSA_2048
        :param subject_alternative_names: Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate. For example, you can add www.example.net to a certificate for which the ``DomainName`` field is www.example.com if users can reach your site by using either name.
        :param tags: Key-value pairs that can identify the certificate.
        :param validation_method: The method you want to use to validate that you own or control the domain associated with a public certificate. You can `validate with DNS <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`_ or `validate with email <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html>`_ . We recommend that you use DNS validation. If not specified, this property defaults to email validation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_certificatemanager as certificatemanager
            
            cfn_certificate_props = certificatemanager.CfnCertificateProps(
                domain_name="domainName",
            
                # the properties below are optional
                certificate_authority_arn="certificateAuthorityArn",
                certificate_transparency_logging_preference="certificateTransparencyLoggingPreference",
                domain_validation_options=[certificatemanager.CfnCertificate.DomainValidationOptionProperty(
                    domain_name="domainName",
            
                    # the properties below are optional
                    hosted_zone_id="hostedZoneId",
                    validation_domain="validationDomain"
                )],
                key_algorithm="keyAlgorithm",
                subject_alternative_names=["subjectAlternativeNames"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                validation_method="validationMethod"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e42a641d895acaee35ba9ec88335a357b8cbfb64b98867f1792ccd63242a79d)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate_authority_arn", value=certificate_authority_arn, expected_type=type_hints["certificate_authority_arn"])
            check_type(argname="argument certificate_transparency_logging_preference", value=certificate_transparency_logging_preference, expected_type=type_hints["certificate_transparency_logging_preference"])
            check_type(argname="argument domain_validation_options", value=domain_validation_options, expected_type=type_hints["domain_validation_options"])
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument validation_method", value=validation_method, expected_type=type_hints["validation_method"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if certificate_authority_arn is not None:
            self._values["certificate_authority_arn"] = certificate_authority_arn
        if certificate_transparency_logging_preference is not None:
            self._values["certificate_transparency_logging_preference"] = certificate_transparency_logging_preference
        if domain_validation_options is not None:
            self._values["domain_validation_options"] = domain_validation_options
        if key_algorithm is not None:
            self._values["key_algorithm"] = key_algorithm
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if tags is not None:
            self._values["tags"] = tags
        if validation_method is not None:
            self._values["validation_method"] = validation_method

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The fully qualified domain name (FQDN), such as www.example.com, with which you want to secure an ACM certificate. Use an asterisk (*) to create a wildcard certificate that protects several sites in the same domain. For example, ``*.example.com`` protects ``www.example.com`` , ``site.example.com`` , and ``images.example.com.``.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainname
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_authority_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the private certificate authority (CA) that will be used to issue the certificate.

        If you do not provide an ARN and you are trying to request a private certificate, ACM will attempt to issue a public certificate. For more information about private CAs, see the `AWS Private Certificate Authority <https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html>`_ user guide. The ARN must have the following form:

        ``arn:aws:acm-pca:region:account:certificate-authority/12345678-1234-1234-1234-123456789012``

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificateauthorityarn
        '''
        result = self._values.get("certificate_authority_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def certificate_transparency_logging_preference(
        self,
    ) -> typing.Optional[builtins.str]:
        '''You can opt out of certificate transparency logging by specifying the ``DISABLED`` option. Opt in by specifying ``ENABLED`` .

        If you do not specify a certificate transparency logging preference on a new CloudFormation template, or if you remove the logging preference from an existing template, this is the same as explicitly enabling the preference.

        Changing the certificate transparency logging preference will update the existing resource by calling ``UpdateCertificateOptions`` on the certificate. This action will not create a new resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-certificatetransparencyloggingpreference
        '''
        result = self._values.get("certificate_transparency_logging_preference")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_validation_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCertificate.DomainValidationOptionProperty]]]]:
        '''Domain information that domain name registrars use to verify your identity.

        .. epigraph::

           In order for a AWS::CertificateManager::Certificate to be provisioned and validated in CloudFormation automatically, the ``DomainName`` property needs to be identical to one of the ``DomainName`` property supplied in DomainValidationOptions, if the ValidationMethod is **DNS**. Failing to keep them like-for-like will result in failure to create the domain validation records in Route53.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-domainvalidationoptions
        '''
        result = self._values.get("domain_validation_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCertificate.DomainValidationOptionProperty]]]], result)

    @builtins.property
    def key_algorithm(self) -> typing.Optional[builtins.str]:
        '''Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data.

        RSA is the default key algorithm for ACM certificates. Elliptic Curve Digital Signature Algorithm (ECDSA) keys are smaller, offering security comparable to RSA keys but with greater computing efficiency. However, ECDSA is not supported by all network clients. Some AWS services may require RSA keys, or only support ECDSA keys of a particular size, while others allow the use of either RSA and ECDSA keys to ensure that compatibility is not broken. Check the requirements for the AWS service where you plan to deploy your certificate. For more information about selecting an algorithm, see `Key algorithms <https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms>`_ .
        .. epigraph::

           Algorithms supported for an ACM certificate request include:

           - ``RSA_2048``
           - ``EC_prime256v1``
           - ``EC_secp384r1``

           Other listed algorithms are for imported certificates only. > When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key.

        Default: RSA_2048

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-keyalgorithm
        '''
        result = self._values.get("key_algorithm")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Additional FQDNs to be included in the Subject Alternative Name extension of the ACM certificate.

        For example, you can add www.example.net to a certificate for which the ``DomainName`` field is www.example.com if users can reach your site by using either name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-subjectalternativenames
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key-value pairs that can identify the certificate.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def validation_method(self) -> typing.Optional[builtins.str]:
        '''The method you want to use to validate that you own or control the domain associated with a public certificate.

        You can `validate with DNS <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html>`_ or `validate with email <https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html>`_ . We recommend that you use DNS validation.

        If not specified, this property defaults to email validation.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-validationmethod
        '''
        result = self._values.get("validation_method")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_certificatemanager.DnsValidatedCertificateProps",
    jsii_struct_bases=[CertificateProps],
    name_mapping={
        "domain_name": "domainName",
        "certificate_name": "certificateName",
        "key_algorithm": "keyAlgorithm",
        "subject_alternative_names": "subjectAlternativeNames",
        "transparency_logging_enabled": "transparencyLoggingEnabled",
        "validation": "validation",
        "hosted_zone": "hostedZone",
        "cleanup_route53_records": "cleanupRoute53Records",
        "custom_resource_role": "customResourceRole",
        "region": "region",
        "route53_endpoint": "route53Endpoint",
    },
)
class DnsValidatedCertificateProps(CertificateProps):
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        certificate_name: typing.Optional[builtins.str] = None,
        key_algorithm: typing.Optional["KeyAlgorithm"] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        transparency_logging_enabled: typing.Optional[builtins.bool] = None,
        validation: typing.Optional[CertificateValidation] = None,
        hosted_zone: _IHostedZone_9a6907ad,
        cleanup_route53_records: typing.Optional[builtins.bool] = None,
        custom_resource_role: typing.Optional[_IRole_235f5d8e] = None,
        region: typing.Optional[builtins.str] = None,
        route53_endpoint: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties to create a DNS validated certificate managed by AWS Certificate Manager.

        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param certificate_name: The Certificate name. Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: the full, absolute path of this construct
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param transparency_logging_enabled: Enable or disable transparency logging for this certificate. Once a certificate has been logged, it cannot be removed from the log. Opting out at that point will have no effect. If you opt out of logging when you request a certificate and then choose later to opt back in, your certificate will not be logged until it is renewed. If you want the certificate to be logged immediately, we recommend that you issue a new one. Default: true
        :param validation: How to validate this certificate. Default: CertificateValidation.fromEmail()
        :param hosted_zone: Route 53 Hosted Zone used to perform DNS validation of the request. The zone must be authoritative for the domain name specified in the Certificate Request.
        :param cleanup_route53_records: When set to true, when the DnsValidatedCertificate is deleted, the associated Route53 validation records are removed. CAUTION: If multiple certificates share the same domains (and same validation records), this can cause the other certificates to fail renewal and/or not validate. Not recommended for production use. Default: false
        :param custom_resource_role: Role to use for the custom resource that creates the validated certificate. Default: - A new role will be created
        :param region: AWS region that will host the certificate. This is needed especially for certificates used for CloudFront distributions, which require the region to be us-east-1. Default: the region the stack is deployed in.
        :param route53_endpoint: An endpoint of Route53 service, which is not necessary as AWS SDK could figure out the right endpoints for most regions, but for some regions such as those in aws-cn partition, the default endpoint is not working now, hence the right endpoint need to be specified through this prop. Route53 is not been officially launched in China, it is only available for AWS internal accounts now. To make DnsValidatedCertificate work for internal accounts now, a special endpoint needs to be provided. Default: - The AWS SDK will determine the Route53 endpoint to use based on region

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_certificatemanager as certificatemanager
            from aws_cdk import aws_iam as iam
            from aws_cdk import aws_route53 as route53
            
            # certificate_validation: certificatemanager.CertificateValidation
            # hosted_zone: route53.HostedZone
            # key_algorithm: certificatemanager.KeyAlgorithm
            # role: iam.Role
            
            dns_validated_certificate_props = certificatemanager.DnsValidatedCertificateProps(
                domain_name="domainName",
                hosted_zone=hosted_zone,
            
                # the properties below are optional
                certificate_name="certificateName",
                cleanup_route53_records=False,
                custom_resource_role=role,
                key_algorithm=key_algorithm,
                region="region",
                route53_endpoint="route53Endpoint",
                subject_alternative_names=["subjectAlternativeNames"],
                transparency_logging_enabled=False,
                validation=certificate_validation
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f8749c95da859ba878861eff7c4231de11fa86681f0df8dbe02a3b4e4f5128b6)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument certificate_name", value=certificate_name, expected_type=type_hints["certificate_name"])
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
            check_type(argname="argument transparency_logging_enabled", value=transparency_logging_enabled, expected_type=type_hints["transparency_logging_enabled"])
            check_type(argname="argument validation", value=validation, expected_type=type_hints["validation"])
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
            check_type(argname="argument cleanup_route53_records", value=cleanup_route53_records, expected_type=type_hints["cleanup_route53_records"])
            check_type(argname="argument custom_resource_role", value=custom_resource_role, expected_type=type_hints["custom_resource_role"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument route53_endpoint", value=route53_endpoint, expected_type=type_hints["route53_endpoint"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "hosted_zone": hosted_zone,
        }
        if certificate_name is not None:
            self._values["certificate_name"] = certificate_name
        if key_algorithm is not None:
            self._values["key_algorithm"] = key_algorithm
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names
        if transparency_logging_enabled is not None:
            self._values["transparency_logging_enabled"] = transparency_logging_enabled
        if validation is not None:
            self._values["validation"] = validation
        if cleanup_route53_records is not None:
            self._values["cleanup_route53_records"] = cleanup_route53_records
        if custom_resource_role is not None:
            self._values["custom_resource_role"] = custom_resource_role
        if region is not None:
            self._values["region"] = region
        if route53_endpoint is not None:
            self._values["route53_endpoint"] = route53_endpoint

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Fully-qualified domain name to request a certificate for.

        May contain wildcards, such as ``*.domain.com``.
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def certificate_name(self) -> typing.Optional[builtins.str]:
        '''The Certificate name.

        Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag

        :default: the full, absolute path of this construct
        '''
        result = self._values.get("certificate_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def key_algorithm(self) -> typing.Optional["KeyAlgorithm"]:
        '''Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data.

        :default: KeyAlgorithm.RSA_2048

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms.title
        '''
        result = self._values.get("key_algorithm")
        return typing.cast(typing.Optional["KeyAlgorithm"], result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names on your certificate.

        Use this to register alternative domain names that represent the same site.

        :default: - No additional FQDNs will be included as alternative domain names.
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def transparency_logging_enabled(self) -> typing.Optional[builtins.bool]:
        '''Enable or disable transparency logging for this certificate.

        Once a certificate has been logged, it cannot be removed from the log.
        Opting out at that point will have no effect. If you opt out of logging
        when you request a certificate and then choose later to opt back in,
        your certificate will not be logged until it is renewed.
        If you want the certificate to be logged immediately, we recommend that you issue a new one.

        :default: true

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-bestpractices.html#best-practices-transparency
        '''
        result = self._values.get("transparency_logging_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def validation(self) -> typing.Optional[CertificateValidation]:
        '''How to validate this certificate.

        :default: CertificateValidation.fromEmail()
        '''
        result = self._values.get("validation")
        return typing.cast(typing.Optional[CertificateValidation], result)

    @builtins.property
    def hosted_zone(self) -> _IHostedZone_9a6907ad:
        '''Route 53 Hosted Zone used to perform DNS validation of the request.

        The zone
        must be authoritative for the domain name specified in the Certificate Request.
        '''
        result = self._values.get("hosted_zone")
        assert result is not None, "Required property 'hosted_zone' is missing"
        return typing.cast(_IHostedZone_9a6907ad, result)

    @builtins.property
    def cleanup_route53_records(self) -> typing.Optional[builtins.bool]:
        '''When set to true, when the DnsValidatedCertificate is deleted, the associated Route53 validation records are removed.

        CAUTION: If multiple certificates share the same domains (and same validation records),
        this can cause the other certificates to fail renewal and/or not validate.
        Not recommended for production use.

        :default: false
        '''
        result = self._values.get("cleanup_route53_records")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def custom_resource_role(self) -> typing.Optional[_IRole_235f5d8e]:
        '''Role to use for the custom resource that creates the validated certificate.

        :default: - A new role will be created
        '''
        result = self._values.get("custom_resource_role")
        return typing.cast(typing.Optional[_IRole_235f5d8e], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''AWS region that will host the certificate.

        This is needed especially
        for certificates used for CloudFront distributions, which require the region
        to be us-east-1.

        :default: the region the stack is deployed in.
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def route53_endpoint(self) -> typing.Optional[builtins.str]:
        '''An endpoint of Route53 service, which is not necessary as AWS SDK could figure out the right endpoints for most regions, but for some regions such as those in aws-cn partition, the default endpoint is not working now, hence the right endpoint need to be specified through this prop.

        Route53 is not been officially launched in China, it is only available for AWS
        internal accounts now. To make DnsValidatedCertificate work for internal accounts
        now, a special endpoint needs to be provided.

        :default: - The AWS SDK will determine the Route53 endpoint to use based on region
        '''
        result = self._values.get("route53_endpoint")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DnsValidatedCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_certificatemanager.ICertificate")
class ICertificate(_IResource_c80c4260, typing_extensions.Protocol):
    '''Represents a certificate in AWS Certificate Manager.'''

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''The certificate's ARN.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="metricDaysToExpiry")
    def metric_days_to_expiry(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the DaysToExpiry metric for this AWS Certificate Manager Certificate. By default, this is the minimum value over 1 day.

        This metric is no longer emitted once the certificate has effectively
        expired, so alarms configured on this metric should probably treat missing
        data as "breaching".

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        ...


class _ICertificateProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Represents a certificate in AWS Certificate Manager.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_certificatemanager.ICertificate"

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''The certificate's ARN.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @jsii.member(jsii_name="metricDaysToExpiry")
    def metric_days_to_expiry(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the DaysToExpiry metric for this AWS Certificate Manager Certificate. By default, this is the minimum value over 1 day.

        This metric is no longer emitted once the certificate has effectively
        expired, so alarms configured on this metric should probably treat missing
        data as "breaching".

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDaysToExpiry", [props]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, ICertificate).__jsii_proxy_class__ = lambda : _ICertificateProxy


class KeyAlgorithm(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.KeyAlgorithm",
):
    '''Certificate Manager key algorithm.

    If you need to use an algorithm that doesn't exist as a static member, you
    can instantiate a ``KeyAlgorithm`` object, e.g: ``new KeyAlgorithm('RSA_2048')``.

    :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-keyalgorithm
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_acmpca as acmpca
        
        
        acm.PrivateCertificate(self, "PrivateCertificate",
            domain_name="test.example.com",
            subject_alternative_names=["cool.example.com", "test.example.net"],  # optional
            certificate_authority=acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CA", "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/023077d8-2bfa-4eb0-8f22-05c96deade77"),
            key_algorithm=acm.KeyAlgorithm.RSA_2048
        )
    '''

    def __init__(self, name: builtins.str) -> None:
        '''
        :param name: The name of the algorithm.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cad5e05f7974be056d9b0af63d73115399c3a158fbaae8fc08f093bd54934b5b)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
        jsii.create(self.__class__, self, [name])

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC_PRIME256V1")
    def EC_PRIME256_V1(cls) -> "KeyAlgorithm":
        '''EC_prime256v1 algorithm.'''
        return typing.cast("KeyAlgorithm", jsii.sget(cls, "EC_PRIME256V1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="EC_SECP384R1")
    def EC_SECP384_R1(cls) -> "KeyAlgorithm":
        '''EC_secp384r1 algorithm.'''
        return typing.cast("KeyAlgorithm", jsii.sget(cls, "EC_SECP384R1"))

    @jsii.python.classproperty
    @jsii.member(jsii_name="RSA_2048")
    def RSA_2048(cls) -> "KeyAlgorithm":
        '''RSA_2048 algorithm.'''
        return typing.cast("KeyAlgorithm", jsii.sget(cls, "RSA_2048"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the algorithm.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))


@jsii.implements(ICertificate)
class PrivateCertificate(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.PrivateCertificate",
):
    '''A private certificate managed by AWS Certificate Manager.

    :resource: AWS::CertificateManager::Certificate
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_acmpca as acmpca
        
        
        acm.PrivateCertificate(self, "PrivateCertificate",
            domain_name="test.example.com",
            subject_alternative_names=["cool.example.com", "test.example.net"],  # optional
            certificate_authority=acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CA", "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/023077d8-2bfa-4eb0-8f22-05c96deade77"),
            key_algorithm=acm.KeyAlgorithm.RSA_2048
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        certificate_authority: _ICertificateAuthority_26727cab,
        domain_name: builtins.str,
        key_algorithm: typing.Optional[KeyAlgorithm] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param certificate_authority: Private certificate authority (CA) that will be used to issue the certificate.
        :param domain_name: Fully-qualified domain name to request a private certificate for. May contain wildcards, such as ``*.domain.com``.
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your private certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f15cee4bdac8e70000027c8ca1386d49408a399d3919aa965c46bb68facc21a4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PrivateCertificateProps(
            certificate_authority=certificate_authority,
            domain_name=domain_name,
            key_algorithm=key_algorithm,
            subject_alternative_names=subject_alternative_names,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromCertificateArn")
    @builtins.classmethod
    def from_certificate_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        certificate_arn: builtins.str,
    ) -> ICertificate:
        '''Import a certificate.

        :param scope: -
        :param id: -
        :param certificate_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eafcf5967e32f6f738871dd474ec031ff15891454da458a2b6e15d1b85b72b9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
        return typing.cast(ICertificate, jsii.sinvoke(cls, "fromCertificateArn", [scope, id, certificate_arn]))

    @jsii.member(jsii_name="metricDaysToExpiry")
    def metric_days_to_expiry(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the DaysToExpiry metric for this AWS Certificate Manager Certificate. By default, this is the minimum value over 1 day.

        This metric is no longer emitted once the certificate has effectively
        expired, so alarms configured on this metric should probably treat missing
        data as "breaching".

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDaysToExpiry", [props]))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''The certificate's ARN.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def _region(self) -> typing.Optional[builtins.str]:
        '''If the certificate is provisionned in a different region than the containing stack, this should be the region in which the certificate lives so we can correctly create ``Metric`` instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_certificatemanager.PrivateCertificateProps",
    jsii_struct_bases=[],
    name_mapping={
        "certificate_authority": "certificateAuthority",
        "domain_name": "domainName",
        "key_algorithm": "keyAlgorithm",
        "subject_alternative_names": "subjectAlternativeNames",
    },
)
class PrivateCertificateProps:
    def __init__(
        self,
        *,
        certificate_authority: _ICertificateAuthority_26727cab,
        domain_name: builtins.str,
        key_algorithm: typing.Optional[KeyAlgorithm] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for your private certificate.

        :param certificate_authority: Private certificate authority (CA) that will be used to issue the certificate.
        :param domain_name: Fully-qualified domain name to request a private certificate for. May contain wildcards, such as ``*.domain.com``.
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family (RSA or ECDSA) must match the algorithm family of the CA's secret key. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your private certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_acmpca as acmpca
            
            
            acm.PrivateCertificate(self, "PrivateCertificate",
                domain_name="test.example.com",
                subject_alternative_names=["cool.example.com", "test.example.net"],  # optional
                certificate_authority=acmpca.CertificateAuthority.from_certificate_authority_arn(self, "CA", "arn:aws:acm-pca:us-east-1:123456789012:certificate-authority/023077d8-2bfa-4eb0-8f22-05c96deade77"),
                key_algorithm=acm.KeyAlgorithm.RSA_2048
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74588c43933e5f34a3203601cc823ca974676f71701280dcd43e9f037bba43e3)
            check_type(argname="argument certificate_authority", value=certificate_authority, expected_type=type_hints["certificate_authority"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument key_algorithm", value=key_algorithm, expected_type=type_hints["key_algorithm"])
            check_type(argname="argument subject_alternative_names", value=subject_alternative_names, expected_type=type_hints["subject_alternative_names"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "certificate_authority": certificate_authority,
            "domain_name": domain_name,
        }
        if key_algorithm is not None:
            self._values["key_algorithm"] = key_algorithm
        if subject_alternative_names is not None:
            self._values["subject_alternative_names"] = subject_alternative_names

    @builtins.property
    def certificate_authority(self) -> _ICertificateAuthority_26727cab:
        '''Private certificate authority (CA) that will be used to issue the certificate.'''
        result = self._values.get("certificate_authority")
        assert result is not None, "Required property 'certificate_authority' is missing"
        return typing.cast(_ICertificateAuthority_26727cab, result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''Fully-qualified domain name to request a private certificate for.

        May contain wildcards, such as ``*.domain.com``.
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_algorithm(self) -> typing.Optional[KeyAlgorithm]:
        '''Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data.

        When you request a private PKI certificate signed by a CA from AWS Private CA, the specified signing algorithm family
        (RSA or ECDSA) must match the algorithm family of the CA's secret key.

        :default: KeyAlgorithm.RSA_2048

        :see: https://docs.aws.amazon.com/acm/latest/userguide/acm-certificate.html#algorithms.title
        '''
        result = self._values.get("key_algorithm")
        return typing.cast(typing.Optional[KeyAlgorithm], result)

    @builtins.property
    def subject_alternative_names(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Alternative domain names on your private certificate.

        Use this to register alternative domain names that represent the same site.

        :default: - No additional FQDNs will be included as alternative domain names.
        '''
        result = self._values.get("subject_alternative_names")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateCertificateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_certificatemanager.ValidationMethod")
class ValidationMethod(enum.Enum):
    '''Method used to assert ownership of the domain.'''

    EMAIL = "EMAIL"
    '''Send email to a number of email addresses associated with the domain.

    :see: https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-email.html
    '''
    DNS = "DNS"
    '''Validate ownership by adding appropriate DNS records.

    :see: https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html
    '''


@jsii.implements(ICertificate)
class Certificate(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.Certificate",
):
    '''A certificate managed by AWS Certificate Manager.

    :exampleMetadata: infused

    Example::

        pool = cognito.UserPool(self, "Pool")
        
        pool.add_domain("CognitoDomain",
            cognito_domain=cognito.CognitoDomainOptions(
                domain_prefix="my-awesome-app"
            )
        )
        
        certificate_arn = "arn:aws:acm:us-east-1:123456789012:certificate/11-3336f1-44483d-adc7-9cd375c5169d"
        
        domain_cert = certificatemanager.Certificate.from_certificate_arn(self, "domainCert", certificate_arn)
        pool.add_domain("CustomDomain",
            custom_domain=cognito.CustomDomainOptions(
                domain_name="user.myapp.com",
                certificate=domain_cert
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        certificate_name: typing.Optional[builtins.str] = None,
        key_algorithm: typing.Optional[KeyAlgorithm] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        transparency_logging_enabled: typing.Optional[builtins.bool] = None,
        validation: typing.Optional[CertificateValidation] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param certificate_name: The Certificate name. Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: the full, absolute path of this construct
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param transparency_logging_enabled: Enable or disable transparency logging for this certificate. Once a certificate has been logged, it cannot be removed from the log. Opting out at that point will have no effect. If you opt out of logging when you request a certificate and then choose later to opt back in, your certificate will not be logged until it is renewed. If you want the certificate to be logged immediately, we recommend that you issue a new one. Default: true
        :param validation: How to validate this certificate. Default: CertificateValidation.fromEmail()
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__64139efa4ed87482ec95b7e38ad6cf94c6873d02b05ba33c374316868eb40e3e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CertificateProps(
            domain_name=domain_name,
            certificate_name=certificate_name,
            key_algorithm=key_algorithm,
            subject_alternative_names=subject_alternative_names,
            transparency_logging_enabled=transparency_logging_enabled,
            validation=validation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromCertificateArn")
    @builtins.classmethod
    def from_certificate_arn(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        certificate_arn: builtins.str,
    ) -> ICertificate:
        '''Import a certificate.

        :param scope: -
        :param id: -
        :param certificate_arn: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ba32788b9a2bfc34b86b3a3dcc7804b0e9dd3af66d552dc97e35c49bf2c959e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument certificate_arn", value=certificate_arn, expected_type=type_hints["certificate_arn"])
        return typing.cast(ICertificate, jsii.sinvoke(cls, "fromCertificateArn", [scope, id, certificate_arn]))

    @jsii.member(jsii_name="metricDaysToExpiry")
    def metric_days_to_expiry(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''Return the DaysToExpiry metric for this AWS Certificate Manager Certificate. By default, this is the minimum value over 1 day.

        This metric is no longer emitted once the certificate has effectively
        expired, so alarms configured on this metric should probably treat missing
        data as "breaching".

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDaysToExpiry", [props]))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''The certificate's ARN.'''
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def _region(self) -> typing.Optional[builtins.str]:
        '''If the certificate is provisionned in a different region than the containing stack, this should be the region in which the certificate lives so we can correctly create ``Metric`` instances.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


@jsii.implements(ICertificate, _ITaggable_36806126)
class DnsValidatedCertificate(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_certificatemanager.DnsValidatedCertificate",
):
    '''(deprecated) A certificate managed by AWS Certificate Manager.

    Will be automatically
    validated using DNS validation against the specified Route 53 hosted zone.

    :deprecated: use {@link Certificate } instead

    :stability: deprecated
    :resource: AWS::CertificateManager::Certificate
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_certificatemanager as certificatemanager
        from aws_cdk import aws_iam as iam
        from aws_cdk import aws_route53 as route53
        
        # certificate_validation: certificatemanager.CertificateValidation
        # hosted_zone: route53.HostedZone
        # key_algorithm: certificatemanager.KeyAlgorithm
        # role: iam.Role
        
        dns_validated_certificate = certificatemanager.DnsValidatedCertificate(self, "MyDnsValidatedCertificate",
            domain_name="domainName",
            hosted_zone=hosted_zone,
        
            # the properties below are optional
            certificate_name="certificateName",
            cleanup_route53_records=False,
            custom_resource_role=role,
            key_algorithm=key_algorithm,
            region="region",
            route53_endpoint="route53Endpoint",
            subject_alternative_names=["subjectAlternativeNames"],
            transparency_logging_enabled=False,
            validation=certificate_validation
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone: _IHostedZone_9a6907ad,
        cleanup_route53_records: typing.Optional[builtins.bool] = None,
        custom_resource_role: typing.Optional[_IRole_235f5d8e] = None,
        region: typing.Optional[builtins.str] = None,
        route53_endpoint: typing.Optional[builtins.str] = None,
        domain_name: builtins.str,
        certificate_name: typing.Optional[builtins.str] = None,
        key_algorithm: typing.Optional[KeyAlgorithm] = None,
        subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
        transparency_logging_enabled: typing.Optional[builtins.bool] = None,
        validation: typing.Optional[CertificateValidation] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param hosted_zone: Route 53 Hosted Zone used to perform DNS validation of the request. The zone must be authoritative for the domain name specified in the Certificate Request.
        :param cleanup_route53_records: When set to true, when the DnsValidatedCertificate is deleted, the associated Route53 validation records are removed. CAUTION: If multiple certificates share the same domains (and same validation records), this can cause the other certificates to fail renewal and/or not validate. Not recommended for production use. Default: false
        :param custom_resource_role: Role to use for the custom resource that creates the validated certificate. Default: - A new role will be created
        :param region: AWS region that will host the certificate. This is needed especially for certificates used for CloudFront distributions, which require the region to be us-east-1. Default: the region the stack is deployed in.
        :param route53_endpoint: An endpoint of Route53 service, which is not necessary as AWS SDK could figure out the right endpoints for most regions, but for some regions such as those in aws-cn partition, the default endpoint is not working now, hence the right endpoint need to be specified through this prop. Route53 is not been officially launched in China, it is only available for AWS internal accounts now. To make DnsValidatedCertificate work for internal accounts now, a special endpoint needs to be provided. Default: - The AWS SDK will determine the Route53 endpoint to use based on region
        :param domain_name: Fully-qualified domain name to request a certificate for. May contain wildcards, such as ``*.domain.com``.
        :param certificate_name: The Certificate name. Since the Certificate resource doesn't support providing a physical name, the value provided here will be recorded in the ``Name`` tag Default: the full, absolute path of this construct
        :param key_algorithm: Specifies the algorithm of the public and private key pair that your certificate uses to encrypt data. Default: KeyAlgorithm.RSA_2048
        :param subject_alternative_names: Alternative domain names on your certificate. Use this to register alternative domain names that represent the same site. Default: - No additional FQDNs will be included as alternative domain names.
        :param transparency_logging_enabled: Enable or disable transparency logging for this certificate. Once a certificate has been logged, it cannot be removed from the log. Opting out at that point will have no effect. If you opt out of logging when you request a certificate and then choose later to opt back in, your certificate will not be logged until it is renewed. If you want the certificate to be logged immediately, we recommend that you issue a new one. Default: true
        :param validation: How to validate this certificate. Default: CertificateValidation.fromEmail()

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9ce11c00a812f11e5a7783956e3e90d7c684153bef62852779a324183af0e49b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DnsValidatedCertificateProps(
            hosted_zone=hosted_zone,
            cleanup_route53_records=cleanup_route53_records,
            custom_resource_role=custom_resource_role,
            region=region,
            route53_endpoint=route53_endpoint,
            domain_name=domain_name,
            certificate_name=certificate_name,
            key_algorithm=key_algorithm,
            subject_alternative_names=subject_alternative_names,
            transparency_logging_enabled=transparency_logging_enabled,
            validation=validation,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="applyRemovalPolicy")
    def apply_removal_policy(self, policy: _RemovalPolicy_9f93c814) -> None:
        '''(deprecated) Apply the given removal policy to this resource.

        The Removal Policy controls what happens to this resource when it stops
        being managed by CloudFormation, either because you've removed it from the
        CDK application or because you've made a change that requires the resource
        to be replaced.

        The resource can be deleted (``RemovalPolicy.DESTROY``), or left in your AWS
        account for data recovery and cleanup later (``RemovalPolicy.RETAIN``).

        :param policy: -

        :stability: deprecated
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ba22afa55d26d44bc7ab216beab4c3cde2bb1d3e614622e603aa02f7a0682b65)
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
        return typing.cast(None, jsii.invoke(self, "applyRemovalPolicy", [policy]))

    @jsii.member(jsii_name="metricDaysToExpiry")
    def metric_days_to_expiry(
        self,
        *,
        account: typing.Optional[builtins.str] = None,
        color: typing.Optional[builtins.str] = None,
        dimensions_map: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        label: typing.Optional[builtins.str] = None,
        period: typing.Optional[_Duration_4839e8c3] = None,
        region: typing.Optional[builtins.str] = None,
        statistic: typing.Optional[builtins.str] = None,
        unit: typing.Optional[_Unit_61bc6f70] = None,
    ) -> _Metric_e396a4dc:
        '''(deprecated) Return the DaysToExpiry metric for this AWS Certificate Manager Certificate. By default, this is the minimum value over 1 day.

        This metric is no longer emitted once the certificate has effectively
        expired, so alarms configured on this metric should probably treat missing
        data as "breaching".

        :param account: Account which this metric comes from. Default: - Deployment account.
        :param color: The hex color code, prefixed with '#' (e.g. '#00ff00'), to use when this metric is rendered on a graph. The ``Color`` class has a set of standard colors that can be used here. Default: - Automatic color
        :param dimensions_map: Dimensions of the metric. Default: - No dimensions.
        :param label: Label for this metric when added to a Graph in a Dashboard. You can use `dynamic labels <https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/graph-dynamic-labels.html>`_ to show summary information about the entire displayed time series in the legend. For example, if you use:: [max: ${MAX}] MyMetric As the metric label, the maximum value in the visible range will be shown next to the time series name in the graph's legend. Default: - No label
        :param period: The period over which the specified statistic is applied. Default: Duration.minutes(5)
        :param region: Region which this metric comes from. Default: - Deployment region.
        :param statistic: What function to use for aggregating. Use the ``aws_cloudwatch.Stats`` helper class to construct valid input strings. Can be one of the following: - "Minimum" | "min" - "Maximum" | "max" - "Average" | "avg" - "Sum" | "sum" - "SampleCount | "n" - "pNN.NN" - "tmNN.NN" | "tm(NN.NN%:NN.NN%)" - "iqm" - "wmNN.NN" | "wm(NN.NN%:NN.NN%)" - "tcNN.NN" | "tc(NN.NN%:NN.NN%)" - "tsNN.NN" | "ts(NN.NN%:NN.NN%)" Default: Average
        :param unit: Unit used to filter the metric stream. Only refer to datums emitted to the metric stream with the given unit and ignore all others. Only useful when datums are being emitted to the same metric stream under different units. The default is to use all matric datums in the stream, regardless of unit, which is recommended in nearly all cases. CloudWatch does not honor this property for graphs. Default: - All metric datums in the given metric stream

        :stability: deprecated
        '''
        props = _MetricOptions_1788b62f(
            account=account,
            color=color,
            dimensions_map=dimensions_map,
            label=label,
            period=period,
            region=region,
            statistic=statistic,
            unit=unit,
        )

        return typing.cast(_Metric_e396a4dc, jsii.invoke(self, "metricDaysToExpiry", [props]))

    @builtins.property
    @jsii.member(jsii_name="certificateArn")
    def certificate_arn(self) -> builtins.str:
        '''(deprecated) The certificate's ARN.

        :stability: deprecated
        '''
        return typing.cast(builtins.str, jsii.get(self, "certificateArn"))

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''(deprecated) Resource Tags.

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-certificatemanager-certificate.html#cfn-certificatemanager-certificate-tags
        :stability: deprecated
        '''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="region")
    def _region(self) -> typing.Optional[builtins.str]:
        '''(deprecated) If the certificate is provisionned in a different region than the containing stack, this should be the region in which the certificate lives so we can correctly create ``Metric`` instances.

        :stability: deprecated
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))


__all__ = [
    "Certificate",
    "CertificateProps",
    "CertificateValidation",
    "CertificationValidationProps",
    "CfnAccount",
    "CfnAccountProps",
    "CfnCertificate",
    "CfnCertificateProps",
    "DnsValidatedCertificate",
    "DnsValidatedCertificateProps",
    "ICertificate",
    "KeyAlgorithm",
    "PrivateCertificate",
    "PrivateCertificateProps",
    "ValidationMethod",
]

publication.publish()

def _typecheckingstub__0454180af2ed6575d11cf361cd5374f722ba32d4007970472aca57751d85258f(
    *,
    domain_name: builtins.str,
    certificate_name: typing.Optional[builtins.str] = None,
    key_algorithm: typing.Optional[KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    transparency_logging_enabled: typing.Optional[builtins.bool] = None,
    validation: typing.Optional[CertificateValidation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d311e81288c218c157a69a30ff08393bdbd454a8fc61208beab60d43ceb0d073(
    hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e9e19a57c59056b6522867e062779dfe13086b375805e7484ac5b3b16e1288bc(
    hosted_zones: typing.Mapping[builtins.str, _IHostedZone_9a6907ad],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e646dcc4d629169bb4daf43ef7ab70c779d7251a8c4a7997d32b8bd3627adc32(
    validation_domains: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e752fd91fd754625f454d3983095bf28bb2a1e1fbd5d307a0d1662659800154(
    *,
    hosted_zone: typing.Optional[_IHostedZone_9a6907ad] = None,
    hosted_zones: typing.Optional[typing.Mapping[builtins.str, _IHostedZone_9a6907ad]] = None,
    method: typing.Optional[ValidationMethod] = None,
    validation_domains: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db4f656c3005938d36870ee742d58c361b2595cfa8e6518fe38589b36fa0255d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    expiry_events_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccount.ExpiryEventsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb75c7a5c08bac926fc28e0787cb2048b7cf11214a8eb2398e88170bf00af154(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8ba0fa95f8656708a4d80a6f060f0f04c7d3ec6e81e8476b2d640250b079a7e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44e33adc270e269d609b1c233392549a56a49e07e3459a57e1ecdb35bebeba3(
    value: typing.Union[_IResolvable_da3f097b, CfnAccount.ExpiryEventsConfigurationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad7aae0c4eae9319d3ebf2aff5a7a88275d784bac367f81cdc0d088e05e5a1fa(
    *,
    days_before_expiry: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9591bf61584c328c9d03002934487f830e54f9aa231b003bcd4999ac2d265c5e(
    *,
    expiry_events_configuration: typing.Union[_IResolvable_da3f097b, typing.Union[CfnAccount.ExpiryEventsConfigurationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f094b3f6a318b9501162c46d45eaf42466c16a9c333dd4021dc90258cf9f035(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    certificate_authority_arn: typing.Optional[builtins.str] = None,
    certificate_transparency_logging_preference: typing.Optional[builtins.str] = None,
    domain_validation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.DomainValidationOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    key_algorithm: typing.Optional[builtins.str] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    validation_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cc2233ca7729f72437c57a4d626536c7b9150faa120045db48045a6b05d1e2a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__faa3f6cb4a71f233ceb715be42dc7e73f8cafc61728bc988a89693de4a66c690(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ecc9a53026b3797b0ea9be214e046e5e413153b784ae59d56029cc943cad72d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__58a46e864da863431c56823a56fc6f403857fef239765fe1b0400f623ed3493c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6946e1448636db36ed5e4ce9c801fc6db4c58d0f89d88789b24f93a2628abc0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__56d2ab51aeb5167d471668b88dc595eaa9bda575e9837a78ce2083f388a77963(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCertificate.DomainValidationOptionProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f976aa6e608ce4d5147cacebbe2f5d9a9585636c73462d403fcc81233f3bbd6(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91f98018864a0f9c4b1051b73b5346df1e3dc533c89e840a02c7184c60f56d3a(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__42ebedfc2551a20aee372ba1bddbbd7ce73218848ab3d71aad89b1d372061b64(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__234f3afa18fce0171662dad033e06d37b968d809b62314c6e62f4c1a4817ad7c(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c300d5c33d86322345b2adb8237375463f7f5ab1e486b11b34f49a04524807a3(
    *,
    domain_name: builtins.str,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    validation_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e42a641d895acaee35ba9ec88335a357b8cbfb64b98867f1792ccd63242a79d(
    *,
    domain_name: builtins.str,
    certificate_authority_arn: typing.Optional[builtins.str] = None,
    certificate_transparency_logging_preference: typing.Optional[builtins.str] = None,
    domain_validation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCertificate.DomainValidationOptionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    key_algorithm: typing.Optional[builtins.str] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    validation_method: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f8749c95da859ba878861eff7c4231de11fa86681f0df8dbe02a3b4e4f5128b6(
    *,
    domain_name: builtins.str,
    certificate_name: typing.Optional[builtins.str] = None,
    key_algorithm: typing.Optional[KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    transparency_logging_enabled: typing.Optional[builtins.bool] = None,
    validation: typing.Optional[CertificateValidation] = None,
    hosted_zone: _IHostedZone_9a6907ad,
    cleanup_route53_records: typing.Optional[builtins.bool] = None,
    custom_resource_role: typing.Optional[_IRole_235f5d8e] = None,
    region: typing.Optional[builtins.str] = None,
    route53_endpoint: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad5e05f7974be056d9b0af63d73115399c3a158fbaae8fc08f093bd54934b5b(
    name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f15cee4bdac8e70000027c8ca1386d49408a399d3919aa965c46bb68facc21a4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    certificate_authority: _ICertificateAuthority_26727cab,
    domain_name: builtins.str,
    key_algorithm: typing.Optional[KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eafcf5967e32f6f738871dd474ec031ff15891454da458a2b6e15d1b85b72b9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    certificate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74588c43933e5f34a3203601cc823ca974676f71701280dcd43e9f037bba43e3(
    *,
    certificate_authority: _ICertificateAuthority_26727cab,
    domain_name: builtins.str,
    key_algorithm: typing.Optional[KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__64139efa4ed87482ec95b7e38ad6cf94c6873d02b05ba33c374316868eb40e3e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    certificate_name: typing.Optional[builtins.str] = None,
    key_algorithm: typing.Optional[KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    transparency_logging_enabled: typing.Optional[builtins.bool] = None,
    validation: typing.Optional[CertificateValidation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ba32788b9a2bfc34b86b3a3dcc7804b0e9dd3af66d552dc97e35c49bf2c959e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    certificate_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9ce11c00a812f11e5a7783956e3e90d7c684153bef62852779a324183af0e49b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone: _IHostedZone_9a6907ad,
    cleanup_route53_records: typing.Optional[builtins.bool] = None,
    custom_resource_role: typing.Optional[_IRole_235f5d8e] = None,
    region: typing.Optional[builtins.str] = None,
    route53_endpoint: typing.Optional[builtins.str] = None,
    domain_name: builtins.str,
    certificate_name: typing.Optional[builtins.str] = None,
    key_algorithm: typing.Optional[KeyAlgorithm] = None,
    subject_alternative_names: typing.Optional[typing.Sequence[builtins.str]] = None,
    transparency_logging_enabled: typing.Optional[builtins.bool] = None,
    validation: typing.Optional[CertificateValidation] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba22afa55d26d44bc7ab216beab4c3cde2bb1d3e614622e603aa02f7a0682b65(
    policy: _RemovalPolicy_9f93c814,
) -> None:
    """Type checking stubs"""
    pass
