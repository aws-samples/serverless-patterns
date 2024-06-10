'''
# Amazon Route53 Construct Library

To add a public hosted zone:

```python
route53.PublicHostedZone(self, "HostedZone",
    zone_name="fully.qualified.domain.com"
)
```

To add a private hosted zone, use `PrivateHostedZone`. Note that
`enableDnsHostnames` and `enableDnsSupport` must have been enabled for the
VPC you're configuring for private hosted zones.

```python
# vpc: ec2.Vpc


zone = route53.PrivateHostedZone(self, "HostedZone",
    zone_name="fully.qualified.domain.com",
    vpc=vpc
)
```

Additional VPCs can be added with `zone.addVpc()`.

## Adding Records

To add a TXT record to your zone:

```python
# my_zone: route53.HostedZone


route53.TxtRecord(self, "TXTRecord",
    zone=my_zone,
    record_name="_foo",  # If the name ends with a ".", it will be used as-is;
    # if it ends with a "." followed by the zone name, a trailing "." will be added automatically;
    # otherwise, a ".", the zone name, and a trailing "." will be added automatically.
    # Defaults to zone root if not specified.
    values=["Bar!", "Baz?"],
    ttl=Duration.minutes(90)
)
```

To add a NS record to your zone:

```python
# my_zone: route53.HostedZone


route53.NsRecord(self, "NSRecord",
    zone=my_zone,
    record_name="foo",
    values=["ns-1.awsdns.co.uk.", "ns-2.awsdns.com."
    ],
    ttl=Duration.minutes(90)
)
```

To add a DS record to your zone:

```python
# my_zone: route53.HostedZone


route53.DsRecord(self, "DSRecord",
    zone=my_zone,
    record_name="foo",
    values=["12345 3 1 123456789abcdef67890123456789abcdef67890"
    ],
    ttl=Duration.minutes(90)
)
```

To add an A record to your zone:

```python
# my_zone: route53.HostedZone


route53.ARecord(self, "ARecord",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.4", "5.6.7.8")
)
```

To add an A record for an EC2 instance with an Elastic IP (EIP) to your zone:

```python
# instance: ec2.Instance

# my_zone: route53.HostedZone


elastic_ip = ec2.CfnEIP(self, "EIP",
    domain="vpc",
    instance_id=instance.instance_id
)
route53.ARecord(self, "ARecord",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses(elastic_ip.ref)
)
```

To create an A record of type alias with target set to another record created outside CDK:

### This function registers the given input i.e. DNS Name(string) of an existing record as an AliasTarget to the new ARecord. To register a target that is created as part of CDK use this instead https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_route53_targets-readme.html

```python
# my_zone: route53.HostedZone

target_record = "existing.record.cdk.local"
record = route53.ARecord.from_aRecord_attributes(self, "A",
    zone=my_zone,
    record_name="test",
    target_dNS=target_record
)
```

To add an AAAA record pointing to a CloudFront distribution:

```python
import aws_cdk.aws_cloudfront as cloudfront

# my_zone: route53.HostedZone
# distribution: cloudfront.CloudFrontWebDistribution

route53.AaaaRecord(self, "Alias",
    zone=my_zone,
    target=route53.RecordTarget.from_alias(targets.CloudFrontTarget(distribution))
)
```

[Geolocation routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geo.html) can be enabled for continent, country or subdivision:

```python
# my_zone: route53.HostedZone


# continent
route53.ARecord(self, "ARecordGeoLocationContinent",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.0", "5.6.7.0"),
    geo_location=route53.GeoLocation.continent(route53.Continent.EUROPE)
)

# country
route53.ARecord(self, "ARecordGeoLocationCountry",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.1", "5.6.7.1"),
    geo_location=route53.GeoLocation.country("DE")
)

# subdivision
route53.ARecord(self, "ARecordGeoLocationSubDividion",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.2", "5.6.7.2"),
    geo_location=route53.GeoLocation.subdivision("WA")
)

# default (wildcard record if no specific record is found)
route53.ARecord(self, "ARecordGeoLocationDefault",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.3", "5.6.7.3"),
    geo_location=route53.GeoLocation.default()
)
```

To enable [weighted routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html), use the `weight` parameter:

```python
# my_zone: route53.HostedZone


route53.ARecord(self, "ARecordWeighted1",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.4"),
    weight=10
)
```

To enable [latency based routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-latency.html), use the `region` parameter:

```python
# my_zone: route53.HostedZone


route53.ARecord(self, "ARecordLatency1",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.4"),
    region="us-east-1"
)
```

To enable [multivalue answer routing](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-multivalue.html), use the `multivalueAnswer` parameter:

```python
# my_zone: route53.HostedZone


route53.ARecord(self, "ARecordMultiValue1",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.4"),
    multi_value_answer=True
)
```

To specify a unique identifier to differentiate among multiple resource record sets that have the same combination of name and type, use the `setIdentifier` parameter:

```python
# my_zone: route53.HostedZone


route53.ARecord(self, "ARecordWeighted1",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.4"),
    weight=10,
    set_identifier="weighted-record-id"
)
```

**Warning** It is not possible to specify `setIdentifier` for a simple routing policy.

Constructs are available for A, AAAA, CAA, CNAME, MX, NS, SRV and TXT records.

Use the `CaaAmazonRecord` construct to easily restrict certificate authorities
allowed to issue certificates for a domain to Amazon only.

### Replacing existing record sets (dangerous!)

Use the `deleteExisting` prop to delete an existing record set before deploying the new one.
This is useful if you want to minimize downtime and avoid "manual" actions while deploying a
stack with a record set that already exists. This is typically the case for record sets that
are not already "owned" by CloudFormation or "owned" by another stack or construct that is
going to be deleted (migration).

> **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
> `deleteExisting` is set to `true` as soon as the resource is added to the stack. Changing
> an existing Record Set's `deleteExisting` property from `false -> true` after deployment
> will delete the record!

```python
# my_zone: route53.HostedZone


route53.ARecord(self, "ARecord",
    zone=my_zone,
    target=route53.RecordTarget.from_ip_addresses("1.2.3.4", "5.6.7.8"),
    delete_existing=True
)
```

### Cross Account Zone Delegation

If you want to have your root domain hosted zone in one account and your subdomain hosted
zone in a different one, you can use `CrossAccountZoneDelegationRecord` to set up delegation
between them.

In the account containing the parent hosted zone:

```python
parent_zone = route53.PublicHostedZone(self, "HostedZone",
    zone_name="someexample.com"
)
cross_account_role = iam.Role(self, "CrossAccountRole",
    # The role name must be predictable
    role_name="MyDelegationRole",
    # The other account
    assumed_by=iam.AccountPrincipal("12345678901"),
    # You can scope down this role policy to be least privileged.
    # If you want the other account to be able to manage specific records,
    # you can scope down by resource and/or normalized record names
    inline_policies={
        "cross_account_policy": iam.PolicyDocument(
            statements=[
                iam.PolicyStatement(
                    sid="ListHostedZonesByName",
                    effect=iam.Effect.ALLOW,
                    actions=["route53:ListHostedZonesByName"],
                    resources=["*"]
                ),
                iam.PolicyStatement(
                    sid="GetHostedZoneAndChangeResourceRecordSets",
                    effect=iam.Effect.ALLOW,
                    actions=["route53:GetHostedZone", "route53:ChangeResourceRecordSets"],
                    # This example assumes the RecordSet subdomain.somexample.com
                    # is contained in the HostedZone
                    resources=["arn:aws:route53:::hostedzone/HZID00000000000000000"],
                    conditions={
                        "ForAllValues:StringLike": {
                            "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["subdomain.someexample.com"
                            ]
                        }
                    }
                )
            ]
        )
    }
)
parent_zone.grant_delegation(cross_account_role)
```

In the account containing the child zone to be delegated:

```python
sub_zone = route53.PublicHostedZone(self, "SubZone",
    zone_name="sub.someexample.com"
)

# import the delegation role by constructing the roleArn
delegation_role_arn = Stack.of(self).format_arn(
    region="",  # IAM is global in each partition
    service="iam",
    account="parent-account-id",
    resource="role",
    resource_name="MyDelegationRole"
)
delegation_role = iam.Role.from_role_arn(self, "DelegationRole", delegation_role_arn)

# create the record
route53.CrossAccountZoneDelegationRecord(self, "delegate",
    delegated_zone=sub_zone,
    parent_hosted_zone_name="someexample.com",  # or you can use parentHostedZoneId
    delegation_role=delegation_role
)
```

Delegating the hosted zone requires assuming a role in the parent hosted zone's account.
In order for the assumed credentials to be valid, the resource must assume the role using
an STS endpoint in a region where both the subdomain's account and the parent's account
are opted-in. By default, this region is determined automatically, but if you need to
change the region used for the AssumeRole call, specify `assumeRoleRegion`:

```python
sub_zone = route53.PublicHostedZone(self, "SubZone",
    zone_name="sub.someexample.com"
)

# import the delegation role by constructing the roleArn
delegation_role_arn = Stack.of(self).format_arn(
    region="",  # IAM is global in each partition
    service="iam",
    account="parent-account-id",
    resource="role",
    resource_name="MyDelegationRole"
)
delegation_role = iam.Role.from_role_arn(self, "DelegationRole", delegation_role_arn)

route53.CrossAccountZoneDelegationRecord(self, "delegate",
    delegated_zone=sub_zone,
    parent_hosted_zone_name="someexample.com",  # or you can use parentHostedZoneId
    delegation_role=delegation_role,
    assume_role_region="us-east-1"
)
```

### Add Trailing Dot to Domain Names

In order to continue managing existing domain names with trailing dots using CDK, you can set `addTrailingDot: false` to prevent the Construct from adding a dot at the end of the domain name.

```python
route53.PublicHostedZone(self, "HostedZone",
    zone_name="fully.qualified.domain.com.",
    add_trailing_dot=False
)
```

## Enabling DNSSEC

DNSSEC can be enabled for Hosted Zones. For detailed information, see
[Configuring DNSSEC signing in Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec.html).

Enabling DNSSEC requires an asymmetric KMS Customer-Managed Key using the `ECC_NIST_P256` key spec.
Additionally, that KMS key must be in `us-east-1`.

```python
kms_key = kms.Key(self, "KmsCMK",
    key_spec=kms.KeySpec.ECC_NIST_P256,
    key_usage=kms.KeyUsage.SIGN_VERIFY
)
hosted_zone = route53.HostedZone(self, "HostedZone",
    zone_name="example.com"
)
# Enable DNSSEC signing for the zone
hosted_zone.enable_dnssec(kms_key=kms_key)
```

The necessary permissions for Route 53 to use the key will automatically be added when using
this configuration. If it is necessary to create a key signing key manually, that can be done
using the `KeySigningKey` construct:

```python
# hosted_zone: route53.HostedZone
# kms_key: kms.Key

route53.KeySigningKey(self, "KeySigningKey",
    hosted_zone=hosted_zone,
    kms_key=kms_key,
    key_signing_key_name="ksk",
    status=route53.KeySigningKeyStatus.ACTIVE
)
```

When directly constructing the `KeySigningKey` resource, enabling DNSSEC signing for the hosted
zone will be need to be done explicitly (either using the `CfnDNSSEC` construct or via another
means).

## Imports

If you don't know the ID of the Hosted Zone to import, you can use the
`HostedZone.fromLookup`:

```python
route53.HostedZone.from_lookup(self, "MyZone",
    domain_name="example.com"
)
```

`HostedZone.fromLookup` requires an environment to be configured. Check
out the [documentation](https://docs.aws.amazon.com/cdk/latest/guide/environments.html) for more documentation and examples. CDK
automatically looks into your `~/.aws/config` file for the `[default]` profile.
If you want to specify a different account run `cdk deploy --profile [profile]`.

```text
new MyDevStack(app, 'dev', {
  env: {
    account: process.env.CDK_DEFAULT_ACCOUNT,
    region: process.env.CDK_DEFAULT_REGION,
  },
});
```

If you know the ID and Name of a Hosted Zone, you can import it directly:

```python
zone = route53.HostedZone.from_hosted_zone_attributes(self, "MyZone",
    zone_name="example.com",
    hosted_zone_id="ZOJJZC49E0EPZ"
)
```

Alternatively, use the `HostedZone.fromHostedZoneId` to import hosted zones if
you know the ID and the retrieval for the `zoneName` is undesirable.

```python
zone = route53.HostedZone.from_hosted_zone_id(self, "MyZone", "ZOJJZC49E0EPZ")
```

You can import a Public Hosted Zone as well with the similar `PublicHostedZone.fromPublicHostedZoneId` and `PublicHostedZone.fromPublicHostedZoneAttributes` methods:

```python
zone_from_attributes = route53.PublicHostedZone.from_public_hosted_zone_attributes(self, "MyZone",
    zone_name="example.com",
    hosted_zone_id="ZOJJZC49E0EPZ"
)

# Does not know zoneName
zone_from_id = route53.PublicHostedZone.from_public_hosted_zone_id(self, "MyZone", "ZOJJZC49E0EPZ")
```

You can use `CrossAccountZoneDelegationRecord` on imported Hosted Zones with the `grantDelegation` method:

```python
cross_account_role = iam.Role(self, "CrossAccountRole",
    # The role name must be predictable
    role_name="MyDelegationRole",
    # The other account
    assumed_by=iam.AccountPrincipal("12345678901")
)

zone_from_id = route53.HostedZone.from_hosted_zone_id(self, "MyZone", "zone-id")
zone_from_id.grant_delegation(cross_account_role)

public_zone_from_id = route53.PublicHostedZone.from_public_hosted_zone_id(self, "MyPublicZone", "public-zone-id")
public_zone_from_id.grant_delegation(cross_account_role)

private_zone_from_id = route53.PrivateHostedZone.from_private_hosted_zone_id(self, "MyPrivateZone", "private-zone-id")
private_zone_from_id.grant_delegation(cross_account_role)
```

## VPC Endpoint Service Private DNS

When you create a VPC endpoint service, AWS generates endpoint-specific DNS hostnames that consumers use to communicate with the service.
For example, vpce-1234-abcdev-us-east-1.vpce-svc-123345.us-east-1.vpce.amazonaws.com.
By default, your consumers access the service with that DNS name.
This can cause problems with HTTPS traffic because the DNS will not match the backend certificate:

```console
curl: (60) SSL: no alternative certificate subject name matches target host name 'vpce-abcdefghijklmnopq-rstuvwx.vpce-svc-abcdefghijklmnopq.us-east-1.vpce.amazonaws.com'
```

Effectively, the endpoint appears untrustworthy. To mitigate this, clients have to create an alias for this DNS name in Route53.

Private DNS for an endpoint service lets you configure a private DNS name so consumers can
access the service using an existing DNS name without creating this Route53 DNS alias
This DNS name can also be guaranteed to match up with the backend certificate.

Before consumers can use the private DNS name, you must verify that you have control of the domain/subdomain.

Assuming your account has ownership of the particular domain/subdomain,
this construct sets up the private DNS configuration on the endpoint service,
creates all the necessary Route53 entries, and verifies domain ownership.

```python
from aws_cdk.aws_elasticloadbalancingv2 import NetworkLoadBalancer


vpc = ec2.Vpc(self, "VPC")
nlb = NetworkLoadBalancer(self, "NLB",
    vpc=vpc
)
vpces = ec2.VpcEndpointService(self, "VPCES",
    vpc_endpoint_service_load_balancers=[nlb]
)
# You must use a public hosted zone so domain ownership can be verified
zone = route53.PublicHostedZone(self, "PHZ",
    zone_name="aws-cdk.dev"
)
route53.VpcEndpointServiceDomainName(self, "EndpointDomain",
    endpoint_service=vpces,
    domain_name="my-stuff.aws-cdk.dev",
    public_hosted_zone=zone
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
from ..aws_ec2 import (
    IVpc as _IVpc_f30d5663, IVpcEndpointService as _IVpcEndpointService_4ddddab0
)
from ..aws_iam import (
    Grant as _Grant_a7ae64f8,
    IGrantable as _IGrantable_71c4f5de,
    IPrincipal as _IPrincipal_539bb2fd,
    IRole as _IRole_235f5d8e,
    Role as _Role_e8c6e11f,
)
from ..aws_kms import IKey as _IKey_5f11635f


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.AliasRecordTargetConfig",
    jsii_struct_bases=[],
    name_mapping={"dns_name": "dnsName", "hosted_zone_id": "hostedZoneId"},
)
class AliasRecordTargetConfig:
    def __init__(self, *, dns_name: builtins.str, hosted_zone_id: builtins.str) -> None:
        '''Represents the properties of an alias target destination.

        :param dns_name: DNS name of the target.
        :param hosted_zone_id: Hosted zone ID of the target.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            alias_record_target_config = route53.AliasRecordTargetConfig(
                dns_name="dnsName",
                hosted_zone_id="hostedZoneId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__387b486cd004971b31128e4032ad0c37e74eea08888305d1660803aa68158e99)
            check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "dns_name": dns_name,
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def dns_name(self) -> builtins.str:
        '''DNS name of the target.'''
        result = self._values.get("dns_name")
        assert result is not None, "Required property 'dns_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''Hosted zone ID of the target.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AliasRecordTargetConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CaaRecordValue",
    jsii_struct_bases=[],
    name_mapping={"flag": "flag", "tag": "tag", "value": "value"},
)
class CaaRecordValue:
    def __init__(
        self,
        *,
        flag: jsii.Number,
        tag: "CaaTag",
        value: builtins.str,
    ) -> None:
        '''Properties for a CAA record value.

        :param flag: The flag.
        :param tag: The tag.
        :param value: The value associated with the tag.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            caa_record_value = route53.CaaRecordValue(
                flag=123,
                tag=route53.CaaTag.ISSUE,
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__355c998e142d682fe0d90395cdf5ae7e566c2548633a9f8a48ab352707f13361)
            check_type(argname="argument flag", value=flag, expected_type=type_hints["flag"])
            check_type(argname="argument tag", value=tag, expected_type=type_hints["tag"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "flag": flag,
            "tag": tag,
            "value": value,
        }

    @builtins.property
    def flag(self) -> jsii.Number:
        '''The flag.'''
        result = self._values.get("flag")
        assert result is not None, "Required property 'flag' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def tag(self) -> "CaaTag":
        '''The tag.'''
        result = self._values.get("tag")
        assert result is not None, "Required property 'tag' is missing"
        return typing.cast("CaaTag", result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value associated with the tag.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaaRecordValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_route53.CaaTag")
class CaaTag(enum.Enum):
    '''The CAA tag.'''

    ISSUE = "ISSUE"
    '''Explicity authorizes a single certificate authority to issue a certificate (any type) for the hostname.'''
    ISSUEWILD = "ISSUEWILD"
    '''Explicity authorizes a single certificate authority to issue a wildcard certificate (and only wildcard) for the hostname.'''
    IODEF = "IODEF"
    '''Specifies a URL to which a certificate authority may report policy violations.'''


@jsii.implements(_IInspectable_c2943556)
class CfnCidrCollection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnCidrCollection",
):
    '''Creates a CIDR collection in the current AWS account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html
    :cloudformationResource: AWS::Route53::CidrCollection
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_cidr_collection = route53.CfnCidrCollection(self, "MyCfnCidrCollection",
            name="name",
        
            # the properties below are optional
            locations=[route53.CfnCidrCollection.LocationProperty(
                cidr_list=["cidrList"],
                location_name="locationName"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCidrCollection.LocationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of a CIDR collection.
        :param locations: A complex type that contains information about the list of CIDR locations.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__720011c856c32f90a3b681a917c19dc88c61ef6e87f090867debab9dfca1faf1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCidrCollectionProps(name=name, locations=locations)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__865b77e8db2784e62d9e80de9ac08effc2203aeaed71fa8db00bdb6a95e02f25)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d0eb630c9850982ace69736bf02f1ce226a32e6e83e5ba91717759cff2a08f89)
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
        '''"The Amazon resource name (ARN) to uniquely identify the AWS resource.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The UUID of the CIDR collection.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of a CIDR collection.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e50d4b886f4c0718571d1dc70a97b0a1880f116a72668e2684b19ec718caa527)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="locations")
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCidrCollection.LocationProperty"]]]]:
        '''A complex type that contains information about the list of CIDR locations.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCidrCollection.LocationProperty"]]]], jsii.get(self, "locations"))

    @locations.setter
    def locations(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCidrCollection.LocationProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d1ed42461528e34721c33b3493a2297bae3e47c0fe29589882e2a685605d968)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "locations", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnCidrCollection.LocationProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr_list": "cidrList", "location_name": "locationName"},
    )
    class LocationProperty:
        def __init__(
            self,
            *,
            cidr_list: typing.Sequence[builtins.str],
            location_name: builtins.str,
        ) -> None:
            '''Specifies the list of CIDR blocks for a CIDR location.

            :param cidr_list: List of CIDR blocks.
            :param location_name: The CIDR collection location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                location_property = route53.CfnCidrCollection.LocationProperty(
                    cidr_list=["cidrList"],
                    location_name="locationName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7cfc9caaf4289bb14df94cc4a6cf31b8d96395a13a1721c994701cc500d10b0d)
                check_type(argname="argument cidr_list", value=cidr_list, expected_type=type_hints["cidr_list"])
                check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr_list": cidr_list,
                "location_name": location_name,
            }

        @builtins.property
        def cidr_list(self) -> typing.List[builtins.str]:
            '''List of CIDR blocks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html#cfn-route53-cidrcollection-location-cidrlist
            '''
            result = self._values.get("cidr_list")
            assert result is not None, "Required property 'cidr_list' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def location_name(self) -> builtins.str:
            '''The CIDR collection location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-cidrcollection-location.html#cfn-route53-cidrcollection-location-locationname
            '''
            result = self._values.get("location_name")
            assert result is not None, "Required property 'location_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnCidrCollectionProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "locations": "locations"},
)
class CfnCidrCollectionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCidrCollection.LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCidrCollection``.

        :param name: The name of a CIDR collection.
        :param locations: A complex type that contains information about the list of CIDR locations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_cidr_collection_props = route53.CfnCidrCollectionProps(
                name="name",
            
                # the properties below are optional
                locations=[route53.CfnCidrCollection.LocationProperty(
                    cidr_list=["cidrList"],
                    location_name="locationName"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24748dfd73812a9d4b13a11033c37a21e1e477a613964e42f30b373347e6bd62)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument locations", value=locations, expected_type=type_hints["locations"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if locations is not None:
            self._values["locations"] = locations

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a CIDR collection.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html#cfn-route53-cidrcollection-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def locations(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCidrCollection.LocationProperty]]]]:
        '''A complex type that contains information about the list of CIDR locations.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-cidrcollection.html#cfn-route53-cidrcollection-locations
        '''
        result = self._values.get("locations")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCidrCollection.LocationProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCidrCollectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDNSSEC(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnDNSSEC",
):
    '''The ``AWS::Route53::DNSSEC`` resource is used to enable DNSSEC signing in a hosted zone.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html
    :cloudformationResource: AWS::Route53::DNSSEC
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_dNSSEC = route53.CfnDNSSEC(self, "MyCfnDNSSEC",
            hosted_zone_id="hostedZoneId"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param hosted_zone_id: A unique string (ID) that is used to identify a hosted zone. For example: ``Z00001111A1ABCaaABC11`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e9e7f472bcf8cedfa8847e5068cd1eac8f74894399d2da52c0efb5f9d06b2bb)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDNSSECProps(hosted_zone_id=hosted_zone_id)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec856d544beda6c45f1608de4feeffbddf087e8459029522c89b9df33f5cb959)
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
            type_hints = typing.get_type_hints(_typecheckingstub__f6989c5ddbfcb06ca392c2069a93d1577d4cf37dbb55219f8b2099854e7e6865)
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
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        '''A unique string (ID) that is used to identify a hosted zone.'''
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__49aa879587d46704e9e1a930ff6b1127ca5bcd3a356f6eb50d8324ca68c299b4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneId", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnDNSSECProps",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId"},
)
class CfnDNSSECProps:
    def __init__(self, *, hosted_zone_id: builtins.str) -> None:
        '''Properties for defining a ``CfnDNSSEC``.

        :param hosted_zone_id: A unique string (ID) that is used to identify a hosted zone. For example: ``Z00001111A1ABCaaABC11`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_dNSSECProps = route53.CfnDNSSECProps(
                hosted_zone_id="hostedZoneId"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2167da58835c803c2916942ed2ea650abb900936cf0014848489e6c72545f5ed)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''A unique string (ID) that is used to identify a hosted zone.

        For example: ``Z00001111A1ABCaaABC11`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-dnssec.html#cfn-route53-dnssec-hostedzoneid
        '''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDNSSECProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnHealthCheck(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnHealthCheck",
):
    '''The ``AWS::Route53::HealthCheck`` resource is a Route 53 resource type that contains settings for a Route 53 health check.

    For information about associating health checks with records, see `HealthCheckId <https://docs.aws.amazon.com/Route53/latest/APIReference/API_ResourceRecordSet.html#Route53-Type-ResourceRecordSet-HealthCheckId>`_ in `ChangeResourceRecordSets <https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html>`_ .
    .. epigraph::

       You can't create a health check with simple routing.

    *ELB Load Balancers*

    If you're registering EC2 instances with an Elastic Load Balancing (ELB) load balancer, do not create Amazon Route 53 health checks for the EC2 instances. When you register an EC2 instance with a load balancer, you configure settings for an ELB health check, which performs a similar function to a Route 53 health check.

    *Private Hosted Zones*

    You can associate health checks with failover records in a private hosted zone. Note the following:

    - Route 53 health checkers are outside the VPC. To check the health of an endpoint within a VPC by IP address, you must assign a public IP address to the instance in the VPC.
    - You can configure a health checker to check the health of an external resource that the instance relies on, such as a database server.
    - You can create a CloudWatch metric, associate an alarm with the metric, and then create a health check that is based on the state of the alarm. For example, you might create a CloudWatch metric that checks the status of the Amazon EC2 ``StatusCheckFailed`` metric, add an alarm to the metric, and then create a health check that is based on the state of the alarm. For information about creating CloudWatch metrics and alarms by using the CloudWatch console, see the `Amazon CloudWatch User Guide <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.html>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
    :cloudformationResource: AWS::Route53::HealthCheck
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_health_check = route53.CfnHealthCheck(self, "MyCfnHealthCheck",
            health_check_config=route53.CfnHealthCheck.HealthCheckConfigProperty(
                type="type",
        
                # the properties below are optional
                alarm_identifier=route53.CfnHealthCheck.AlarmIdentifierProperty(
                    name="name",
                    region="region"
                ),
                child_health_checks=["childHealthChecks"],
                enable_sni=False,
                failure_threshold=123,
                fully_qualified_domain_name="fullyQualifiedDomainName",
                health_threshold=123,
                insufficient_data_health_status="insufficientDataHealthStatus",
                inverted=False,
                ip_address="ipAddress",
                measure_latency=False,
                port=123,
                regions=["regions"],
                request_interval=123,
                resource_path="resourcePath",
                routing_control_arn="routingControlArn",
                search_string="searchString"
            ),
        
            # the properties below are optional
            health_check_tags=[route53.CfnHealthCheck.HealthCheckTagProperty(
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
        health_check_config: typing.Union[_IResolvable_da3f097b, typing.Union["CfnHealthCheck.HealthCheckConfigProperty", typing.Dict[builtins.str, typing.Any]]],
        health_check_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHealthCheck.HealthCheckTagProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param health_check_config: A complex type that contains detailed information about one health check. For the values to enter for ``HealthCheckConfig`` , see `HealthCheckConfig <https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html>`_
        :param health_check_tags: The ``HealthCheckTags`` property describes key-value pairs that are associated with an ``AWS::Route53::HealthCheck`` resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__469f7fe3ad975c091ea64f8ce59060016c4769f6532660a91964f093088b495c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHealthCheckProps(
            health_check_config=health_check_config,
            health_check_tags=health_check_tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__92eef426989e6d56f38b29af5b8a36178998c16c96fb7222ce9f5538f6972709)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b0a64c35de99e287eed1f250bb5b41772f3dbba1a8ad5b6ced21bbde215943f8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrHealthCheckId")
    def attr_health_check_id(self) -> builtins.str:
        '''The identifier that Amazon Route 53 assigned to the health check when you created it.

        When you add or update a resource record set, you use this value to specify which health check to use. The value can be up to 64 characters long.

        :cloudformationAttribute: HealthCheckId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrHealthCheckId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="healthCheckConfig")
    def health_check_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.HealthCheckConfigProperty"]:
        '''A complex type that contains detailed information about one health check.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.HealthCheckConfigProperty"], jsii.get(self, "healthCheckConfig"))

    @health_check_config.setter
    def health_check_config(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.HealthCheckConfigProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8b0df7baae49dfed1fb95576ba5c0e5d51660f268bef2a4d82fca32324f94689)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckConfig", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckTags")
    def health_check_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.HealthCheckTagProperty"]]]]:
        '''The ``HealthCheckTags`` property describes key-value pairs that are associated with an ``AWS::Route53::HealthCheck`` resource.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.HealthCheckTagProperty"]]]], jsii.get(self, "healthCheckTags"))

    @health_check_tags.setter
    def health_check_tags(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.HealthCheckTagProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1d1493e762a114933a5a3775c215007c8d522e932362ff7c530eb00b515208ff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckTags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHealthCheck.AlarmIdentifierProperty",
        jsii_struct_bases=[],
        name_mapping={"name": "name", "region": "region"},
    )
    class AlarmIdentifierProperty:
        def __init__(self, *, name: builtins.str, region: builtins.str) -> None:
            '''A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

            :param name: The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy. .. epigraph:: Route 53 supports CloudWatch alarms with the following features: - Standard-resolution metrics. High-resolution metrics aren't supported. For more information, see `High-Resolution Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`_ in the *Amazon CloudWatch User Guide* . - Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't supported.
            :param region: For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in. For the current list of CloudWatch regions, see `Amazon CloudWatch endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/cw_region.html>`_ in the *Amazon Web Services General Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                alarm_identifier_property = route53.CfnHealthCheck.AlarmIdentifierProperty(
                    name="name",
                    region="region"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0e113166210d02eb6e0f8c59a042f052d80d619370b1e9fe97a7a04b51014736)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "region": region,
            }

        @builtins.property
        def name(self) -> builtins.str:
            '''The name of the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether this health check is healthy.

            .. epigraph::

               Route 53 supports CloudWatch alarms with the following features:

               - Standard-resolution metrics. High-resolution metrics aren't supported. For more information, see `High-Resolution Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`_ in the *Amazon CloudWatch User Guide* .
               - Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't supported.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def region(self) -> builtins.str:
            '''For the CloudWatch alarm that you want Route 53 health checkers to use to determine whether this health check is healthy, the region that the alarm was created in.

            For the current list of CloudWatch regions, see `Amazon CloudWatch endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/cw_region.html>`_ in the *Amazon Web Services General Reference* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-alarmidentifier.html#cfn-route53-healthcheck-alarmidentifier-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AlarmIdentifierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHealthCheck.HealthCheckConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "alarm_identifier": "alarmIdentifier",
            "child_health_checks": "childHealthChecks",
            "enable_sni": "enableSni",
            "failure_threshold": "failureThreshold",
            "fully_qualified_domain_name": "fullyQualifiedDomainName",
            "health_threshold": "healthThreshold",
            "insufficient_data_health_status": "insufficientDataHealthStatus",
            "inverted": "inverted",
            "ip_address": "ipAddress",
            "measure_latency": "measureLatency",
            "port": "port",
            "regions": "regions",
            "request_interval": "requestInterval",
            "resource_path": "resourcePath",
            "routing_control_arn": "routingControlArn",
            "search_string": "searchString",
        },
    )
    class HealthCheckConfigProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            alarm_identifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHealthCheck.AlarmIdentifierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            child_health_checks: typing.Optional[typing.Sequence[builtins.str]] = None,
            enable_sni: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            failure_threshold: typing.Optional[jsii.Number] = None,
            fully_qualified_domain_name: typing.Optional[builtins.str] = None,
            health_threshold: typing.Optional[jsii.Number] = None,
            insufficient_data_health_status: typing.Optional[builtins.str] = None,
            inverted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            ip_address: typing.Optional[builtins.str] = None,
            measure_latency: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            port: typing.Optional[jsii.Number] = None,
            regions: typing.Optional[typing.Sequence[builtins.str]] = None,
            request_interval: typing.Optional[jsii.Number] = None,
            resource_path: typing.Optional[builtins.str] = None,
            routing_control_arn: typing.Optional[builtins.str] = None,
            search_string: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A complex type that contains information about the health check.

            :param type: The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy. .. epigraph:: You can't change the value of ``Type`` after you create a health check. You can create the following types of health checks: - *HTTP* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400. - *HTTPS* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400. .. epigraph:: If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later. - *HTTP_STR_MATCH* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . - *HTTPS_STR_MATCH* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` . - *TCP* : Route 53 tries to establish a TCP connection. - *CLOUDWATCH_METRIC* : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` . .. epigraph:: Route 53 supports CloudWatch alarms with the following features: - Standard-resolution metrics. High-resolution metrics aren't supported. For more information, see `High-Resolution Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`_ in the *Amazon CloudWatch User Guide* . - Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't supported. - *CALCULATED* : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` . - *RECOVERY_CONTROL* : The health check is assocated with a Route53 Application Recovery Controller routing control. If the routing control state is ``ON`` , the health check is considered healthy. If the state is ``OFF`` , the health check is considered unhealthy. For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ in the *Amazon Route 53 Developer Guide* .
            :param alarm_identifier: A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.
            :param child_health_checks: (CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.
            :param enable_sni: Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation. This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate. Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid. The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.
            :param failure_threshold: The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa. For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ in the *Amazon Route 53 Developer Guide* . If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.
            :param fully_qualified_domain_name: Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` . *If you specify a value for* ``IPAddress`` : Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks. When Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header: - If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header. - If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header. - If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header. If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases. *If you don't specify a value for ``IPAddress``* : Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint. .. epigraph:: If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health checks to the endpoint. If there's no record with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error. If you want to check the health of multiple records that have the same name and type, such as multiple weighted records, and if you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the records (www.example.com). .. epigraph:: In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the records and you then associate the health check with those records, health check results will be unpredictable. In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a ``Host`` header.
            :param health_threshold: The number of child health checks that are associated with a ``CALCULATED`` health check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy. To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the `ChildHealthChecks <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`_ element. Note the following: - If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy. - If you specify ``0`` , Route 53 always considers this health check to be healthy.
            :param insufficient_data_health_status: When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check: - ``Healthy`` : Route 53 considers the health check to be healthy. - ``Unhealthy`` : Route 53 considers the health check to be unhealthy. - ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.
            :param inverted: Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.
            :param ip_address: The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on. If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint. Use one of the following formats for the value of ``IPAddress`` : - *IPv4 address* : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` . - *IPv6 address* : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` . If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change. For more information, see `FullyQualifiedDomainName <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`_ . Constraints: Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents: - `RFC 5735, Special Use IPv4 Addresses <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5735>`_ - `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc6598>`_ - `RFC 5156, Special-Use IPv6 Addresses <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5156>`_ When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .
            :param measure_latency: Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the *Health Checks* page in the Route 53 console. .. epigraph:: You can't change the value of ``MeasureLatency`` after you create a health check.
            :param port: The port on the endpoint that you want Amazon Route 53 to perform health checks on. .. epigraph:: Don't specify a value for ``Port`` when you specify a value for `Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-type>`_ of ``CLOUDWATCH_METRIC`` or ``CALCULATED`` .
            :param regions: A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint. If you don't specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under *Valid Values* . If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).
            :param request_interval: The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request. Each Route 53 health checker makes requests at this interval. .. epigraph:: You can't change the value of ``RequestInterval`` after you create a health check. If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.
            :param resource_path: The path, if any, that you want Amazon Route 53 to request when performing health checks. The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, ``/welcome.html?language=jp&login=y`` .
            :param routing_control_arn: The Amazon Resource Name (ARN) for the Route 53 Application Recovery Controller routing control. For more information about Route 53 Application Recovery Controller, see `Route 53 Application Recovery Controller Developer Guide. <https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route-53-recovery.html>`_ .
            :param search_string: If the value of Type is ``HTTP_STR_MATCH`` or ``HTTPS_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource. If the string appears in the response body, Route 53 considers the resource healthy. Route 53 considers case when searching for ``SearchString`` in the response body.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                health_check_config_property = route53.CfnHealthCheck.HealthCheckConfigProperty(
                    type="type",
                
                    # the properties below are optional
                    alarm_identifier=route53.CfnHealthCheck.AlarmIdentifierProperty(
                        name="name",
                        region="region"
                    ),
                    child_health_checks=["childHealthChecks"],
                    enable_sni=False,
                    failure_threshold=123,
                    fully_qualified_domain_name="fullyQualifiedDomainName",
                    health_threshold=123,
                    insufficient_data_health_status="insufficientDataHealthStatus",
                    inverted=False,
                    ip_address="ipAddress",
                    measure_latency=False,
                    port=123,
                    regions=["regions"],
                    request_interval=123,
                    resource_path="resourcePath",
                    routing_control_arn="routingControlArn",
                    search_string="searchString"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5f6870a18d2b0b32e1b106470763dd03bb4bfa75e0234e29a176b8b5127252e0)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument alarm_identifier", value=alarm_identifier, expected_type=type_hints["alarm_identifier"])
                check_type(argname="argument child_health_checks", value=child_health_checks, expected_type=type_hints["child_health_checks"])
                check_type(argname="argument enable_sni", value=enable_sni, expected_type=type_hints["enable_sni"])
                check_type(argname="argument failure_threshold", value=failure_threshold, expected_type=type_hints["failure_threshold"])
                check_type(argname="argument fully_qualified_domain_name", value=fully_qualified_domain_name, expected_type=type_hints["fully_qualified_domain_name"])
                check_type(argname="argument health_threshold", value=health_threshold, expected_type=type_hints["health_threshold"])
                check_type(argname="argument insufficient_data_health_status", value=insufficient_data_health_status, expected_type=type_hints["insufficient_data_health_status"])
                check_type(argname="argument inverted", value=inverted, expected_type=type_hints["inverted"])
                check_type(argname="argument ip_address", value=ip_address, expected_type=type_hints["ip_address"])
                check_type(argname="argument measure_latency", value=measure_latency, expected_type=type_hints["measure_latency"])
                check_type(argname="argument port", value=port, expected_type=type_hints["port"])
                check_type(argname="argument regions", value=regions, expected_type=type_hints["regions"])
                check_type(argname="argument request_interval", value=request_interval, expected_type=type_hints["request_interval"])
                check_type(argname="argument resource_path", value=resource_path, expected_type=type_hints["resource_path"])
                check_type(argname="argument routing_control_arn", value=routing_control_arn, expected_type=type_hints["routing_control_arn"])
                check_type(argname="argument search_string", value=search_string, expected_type=type_hints["search_string"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if alarm_identifier is not None:
                self._values["alarm_identifier"] = alarm_identifier
            if child_health_checks is not None:
                self._values["child_health_checks"] = child_health_checks
            if enable_sni is not None:
                self._values["enable_sni"] = enable_sni
            if failure_threshold is not None:
                self._values["failure_threshold"] = failure_threshold
            if fully_qualified_domain_name is not None:
                self._values["fully_qualified_domain_name"] = fully_qualified_domain_name
            if health_threshold is not None:
                self._values["health_threshold"] = health_threshold
            if insufficient_data_health_status is not None:
                self._values["insufficient_data_health_status"] = insufficient_data_health_status
            if inverted is not None:
                self._values["inverted"] = inverted
            if ip_address is not None:
                self._values["ip_address"] = ip_address
            if measure_latency is not None:
                self._values["measure_latency"] = measure_latency
            if port is not None:
                self._values["port"] = port
            if regions is not None:
                self._values["regions"] = regions
            if request_interval is not None:
                self._values["request_interval"] = request_interval
            if resource_path is not None:
                self._values["resource_path"] = resource_path
            if routing_control_arn is not None:
                self._values["routing_control_arn"] = routing_control_arn
            if search_string is not None:
                self._values["search_string"] = search_string

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of health check that you want to create, which indicates how Amazon Route 53 determines whether an endpoint is healthy.

            .. epigraph::

               You can't change the value of ``Type`` after you create a health check.

            You can create the following types of health checks:

            - *HTTP* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and waits for an HTTP status code of 200 or greater and less than 400.
            - *HTTPS* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTPS request and waits for an HTTP status code of 200 or greater and less than 400.

            .. epigraph::

               If you specify ``HTTPS`` for the value of ``Type`` , the endpoint must support TLS v1.0 or later.

            - *HTTP_STR_MATCH* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an HTTP request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` .
            - *HTTPS_STR_MATCH* : Route 53 tries to establish a TCP connection. If successful, Route 53 submits an ``HTTPS`` request and searches the first 5,120 bytes of the response body for the string that you specify in ``SearchString`` .
            - *TCP* : Route 53 tries to establish a TCP connection.
            - *CLOUDWATCH_METRIC* : The health check is associated with a CloudWatch alarm. If the state of the alarm is ``OK`` , the health check is considered healthy. If the state is ``ALARM`` , the health check is considered unhealthy. If CloudWatch doesn't have sufficient data to determine whether the state is ``OK`` or ``ALARM`` , the health check status depends on the setting for ``InsufficientDataHealthStatus`` : ``Healthy`` , ``Unhealthy`` , or ``LastKnownStatus`` .

            .. epigraph::

               Route 53 supports CloudWatch alarms with the following features:

               - Standard-resolution metrics. High-resolution metrics aren't supported. For more information, see `High-Resolution Metrics <https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/publishingMetrics.html#high-resolution-metrics>`_ in the *Amazon CloudWatch User Guide* .
               - Statistics: Average, Minimum, Maximum, Sum, and SampleCount. Extended statistics aren't supported.

            - *CALCULATED* : For health checks that monitor the status of other health checks, Route 53 adds up the number of health checks that Route 53 health checkers consider to be healthy and compares that number with the value of ``HealthThreshold`` .
            - *RECOVERY_CONTROL* : The health check is assocated with a Route53 Application Recovery Controller routing control. If the routing control state is ``ON`` , the health check is considered healthy. If the state is ``OFF`` , the health check is considered unhealthy.

            For more information, see `How Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alarm_identifier(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.AlarmIdentifierProperty"]]:
            '''A complex type that identifies the CloudWatch alarm that you want Amazon Route 53 health checkers to use to determine whether the specified health check is healthy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-alarmidentifier
            '''
            result = self._values.get("alarm_identifier")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHealthCheck.AlarmIdentifierProperty"]], result)

        @builtins.property
        def child_health_checks(self) -> typing.Optional[typing.List[builtins.str]]:
            '''(CALCULATED Health Checks Only) A complex type that contains one ``ChildHealthCheck`` element for each health check that you want to associate with a ``CALCULATED`` health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-childhealthchecks
            '''
            result = self._values.get("child_health_checks")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def enable_sni(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify whether you want Amazon Route 53 to send the value of ``FullyQualifiedDomainName`` to the endpoint in the ``client_hello`` message during TLS negotiation.

            This allows the endpoint to respond to ``HTTPS`` health check requests with the applicable SSL/TLS certificate.

            Some endpoints require that ``HTTPS`` requests include the host name in the ``client_hello`` message. If you don't enable SNI, the status of the health check will be ``SSL alert handshake_failure`` . A health check can also have that status for other reasons. If SNI is enabled and you're still getting the error, check the SSL/TLS configuration on your endpoint and confirm that your certificate is valid.

            The SSL/TLS certificate on your endpoint includes a domain name in the ``Common Name`` field and possibly several more in the ``Subject Alternative Names`` field. One of the domain names in the certificate should match the value that you specify for ``FullyQualifiedDomainName`` . If the endpoint responds to the ``client_hello`` message with a certificate that does not include the domain name that you specified in ``FullyQualifiedDomainName`` , a health checker will retry the handshake. In the second attempt, the health checker will omit ``FullyQualifiedDomainName`` from the ``client_hello`` message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-enablesni
            '''
            result = self._values.get("enable_sni")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def failure_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of consecutive health checks that an endpoint must pass or fail for Amazon Route 53 to change the current status of the endpoint from unhealthy to healthy or vice versa.

            For more information, see `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ in the *Amazon Route 53 Developer Guide* .

            If you don't specify a value for ``FailureThreshold`` , the default value is three health checks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-failurethreshold
            '''
            result = self._values.get("failure_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def fully_qualified_domain_name(self) -> typing.Optional[builtins.str]:
            '''Amazon Route 53 behavior depends on whether you specify a value for ``IPAddress`` .

            *If you specify a value for* ``IPAddress`` :

            Amazon Route 53 sends health check requests to the specified IPv4 or IPv6 address and passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header for all health checks except TCP health checks. This is typically the fully qualified DNS name of the endpoint on which you want Route 53 to perform health checks.

            When Route 53 checks the health of an endpoint, here is how it constructs the ``Host`` header:

            - If you specify a value of ``80`` for ``Port`` and ``HTTP`` or ``HTTP_STR_MATCH`` for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the Host header.
            - If you specify a value of ``443`` for ``Port`` and ``HTTPS`` or ``HTTPS_STR_MATCH`` for ``Type`` , Route 53 passes the value of ``FullyQualifiedDomainName`` to the endpoint in the ``Host`` header.
            - If you specify another value for ``Port`` and any value except ``TCP`` for ``Type`` , Route 53 passes ``FullyQualifiedDomainName:Port`` to the endpoint in the ``Host`` header.

            If you don't specify a value for ``FullyQualifiedDomainName`` , Route 53 substitutes the value of ``IPAddress`` in the ``Host`` header in each of the preceding cases.

            *If you don't specify a value for ``IPAddress``* :

            Route 53 sends a DNS request to the domain that you specify for ``FullyQualifiedDomainName`` at the interval that you specify for ``RequestInterval`` . Using an IPv4 address that DNS returns, Route 53 then checks the health of the endpoint.
            .. epigraph::

               If you don't specify a value for ``IPAddress`` , Route 53 uses only IPv4 to send health checks to the endpoint. If there's no record with a type of A for the name that you specify for ``FullyQualifiedDomainName`` , the health check fails with a "DNS resolution failed" error.

            If you want to check the health of multiple records that have the same name and type, such as multiple weighted records, and if you choose to specify the endpoint only by ``FullyQualifiedDomainName`` , we recommend that you create a separate health check for each endpoint. For example, create a health check for each HTTP server that is serving content for www.example.com. For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as us-east-2-www.example.com), not the name of the records (www.example.com).
            .. epigraph::

               In this configuration, if you create a health check for which the value of ``FullyQualifiedDomainName`` matches the name of the records and you then associate the health check with those records, health check results will be unpredictable.

            In addition, if the value that you specify for ``Type`` is ``HTTP`` , ``HTTPS`` , ``HTTP_STR_MATCH`` , or ``HTTPS_STR_MATCH`` , Route 53 passes the value of ``FullyQualifiedDomainName`` in the ``Host`` header, as it does when you specify a value for ``IPAddress`` . If the value of ``Type`` is ``TCP`` , Route 53 doesn't pass a ``Host`` header.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-fullyqualifieddomainname
            '''
            result = self._values.get("fully_qualified_domain_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def health_threshold(self) -> typing.Optional[jsii.Number]:
            '''The number of child health checks that are associated with a ``CALCULATED`` health check that Amazon Route 53 must consider healthy for the ``CALCULATED`` health check to be considered healthy.

            To specify the child health checks that you want to associate with a ``CALCULATED`` health check, use the `ChildHealthChecks <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-ChildHealthChecks>`_ element.

            Note the following:

            - If you specify a number greater than the number of child health checks, Route 53 always considers this health check to be unhealthy.
            - If you specify ``0`` , Route 53 always considers this health check to be healthy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-healththreshold
            '''
            result = self._values.get("health_threshold")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def insufficient_data_health_status(self) -> typing.Optional[builtins.str]:
            '''When CloudWatch has insufficient data about the metric to determine the alarm state, the status that you want Amazon Route 53 to assign to the health check:  - ``Healthy`` : Route 53 considers the health check to be healthy.

            - ``Unhealthy`` : Route 53 considers the health check to be unhealthy.
            - ``LastKnownStatus`` : Route 53 uses the status of the health check from the last time that CloudWatch had sufficient data to determine the alarm state. For new health checks that have no last known status, the default status for the health check is healthy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-insufficientdatahealthstatus
            '''
            result = self._values.get("insufficient_data_health_status")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inverted(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify whether you want Amazon Route 53 to invert the status of a health check, for example, to consider a health check unhealthy when it otherwise would be considered healthy.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-inverted
            '''
            result = self._values.get("inverted")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def ip_address(self) -> typing.Optional[builtins.str]:
            '''The IPv4 or IPv6 IP address of the endpoint that you want Amazon Route 53 to perform health checks on.

            If you don't specify a value for ``IPAddress`` , Route 53 sends a DNS request to resolve the domain name that you specify in ``FullyQualifiedDomainName`` at the interval that you specify in ``RequestInterval`` . Using an IP address returned by DNS, Route 53 then checks the health of the endpoint.

            Use one of the following formats for the value of ``IPAddress`` :

            - *IPv4 address* : four values between 0 and 255, separated by periods (.), for example, ``192.0.2.44`` .
            - *IPv6 address* : eight groups of four hexadecimal values, separated by colons (:), for example, ``2001:0db8:85a3:0000:0000:abcd:0001:2345`` . You can also shorten IPv6 addresses as described in RFC 5952, for example, ``2001:db8:85a3::abcd:1:2345`` .

            If the endpoint is an EC2 instance, we recommend that you create an Elastic IP address, associate it with your EC2 instance, and specify the Elastic IP address for ``IPAddress`` . This ensures that the IP address of your instance will never change.

            For more information, see `FullyQualifiedDomainName <https://docs.aws.amazon.com/Route53/latest/APIReference/API_UpdateHealthCheck.html#Route53-UpdateHealthCheck-request-FullyQualifiedDomainName>`_ .

            Constraints: Route 53 can't check the health of endpoints for which the IP address is in local, private, non-routable, or multicast ranges. For more information about IP addresses for which you can't create health checks, see the following documents:

            - `RFC 5735, Special Use IPv4 Addresses <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5735>`_
            - `RFC 6598, IANA-Reserved IPv4 Prefix for Shared Address Space <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc6598>`_
            - `RFC 5156, Special-Use IPv6 Addresses <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5156>`_

            When the value of ``Type`` is ``CALCULATED`` or ``CLOUDWATCH_METRIC`` , omit ``IPAddress`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-ipaddress
            '''
            result = self._values.get("ip_address")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def measure_latency(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specify whether you want Amazon Route 53 to measure the latency between health checkers in multiple AWS regions and your endpoint, and to display CloudWatch latency graphs on the *Health Checks* page in the Route 53 console.

            .. epigraph::

               You can't change the value of ``MeasureLatency`` after you create a health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-measurelatency
            '''
            result = self._values.get("measure_latency")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def port(self) -> typing.Optional[jsii.Number]:
            '''The port on the endpoint that you want Amazon Route 53 to perform health checks on.

            .. epigraph::

               Don't specify a value for ``Port`` when you specify a value for `Type <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-type>`_ of ``CLOUDWATCH_METRIC`` or ``CALCULATED`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-port
            '''
            result = self._values.get("port")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def regions(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A complex type that contains one ``Region`` element for each region from which you want Amazon Route 53 health checkers to check the specified endpoint.

            If you don't specify any regions, Route 53 health checkers automatically performs checks from all of the regions that are listed under *Valid Values* .

            If you update a health check to remove a region that has been performing health checks, Route 53 will briefly continue to perform checks from that region to ensure that some health checkers are always checking the endpoint (for example, if you replace three regions with four different regions).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-regions
            '''
            result = self._values.get("regions")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def request_interval(self) -> typing.Optional[jsii.Number]:
            '''The number of seconds between the time that Amazon Route 53 gets a response from your endpoint and the time that it sends the next health check request.

            Each Route 53 health checker makes requests at this interval.
            .. epigraph::

               You can't change the value of ``RequestInterval`` after you create a health check.

            If you don't specify a value for ``RequestInterval`` , the default value is ``30`` seconds.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-requestinterval
            '''
            result = self._values.get("request_interval")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def resource_path(self) -> typing.Optional[builtins.str]:
            '''The path, if any, that you want Amazon Route 53 to request when performing health checks.

            The path can be any value for which your endpoint will return an HTTP status code of 2xx or 3xx when the endpoint is healthy, for example, the file /docs/route53-health-check.html. You can also include query string parameters, for example, ``/welcome.html?language=jp&login=y`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-resourcepath
            '''
            result = self._values.get("resource_path")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def routing_control_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) for the Route 53 Application Recovery Controller routing control.

            For more information about Route 53 Application Recovery Controller, see `Route 53 Application Recovery Controller Developer Guide. <https://docs.aws.amazon.com/r53recovery/latest/dg/what-is-route-53-recovery.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-routingcontrolarn
            '''
            result = self._values.get("routing_control_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def search_string(self) -> typing.Optional[builtins.str]:
            '''If the value of Type is ``HTTP_STR_MATCH`` or ``HTTPS_STR_MATCH`` , the string that you want Amazon Route 53 to search for in the response body from the specified resource.

            If the string appears in the response body, Route 53 considers the resource healthy.

            Route 53 considers case when searching for ``SearchString`` in the response body.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthcheckconfig.html#cfn-route53-healthcheck-healthcheckconfig-searchstring
            '''
            result = self._values.get("search_string")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHealthCheck.HealthCheckTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class HealthCheckTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''The ``HealthCheckTag`` property describes one key-value pair that is associated with an ``AWS::Route53::HealthCheck`` resource.

            :param key: The value of ``Key`` depends on the operation that you want to perform:. - *Add a tag to a health check or hosted zone* : ``Key`` is the name that you want to give the new tag. - *Edit a tag* : ``Key`` is the name of the tag that you want to change the ``Value`` for. - *Delete a key* : ``Key`` is the name of the tag you want to remove. - *Give a name to a health check* : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a *Name* column that lets you see the name that you've given to each health check.
            :param value: The value of ``Value`` depends on the operation that you want to perform:. - *Add a tag to a health check or hosted zone* : ``Value`` is the value that you want to give the new tag. - *Edit a tag* : ``Value`` is the new value that you want to assign the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                health_check_tag_property = route53.CfnHealthCheck.HealthCheckTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b181f58da0d2eb6f8c9ba8be7f7b44f29a68b4d09e2f4c600ab9522e6f52f880)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The value of ``Key`` depends on the operation that you want to perform:.

            - *Add a tag to a health check or hosted zone* : ``Key`` is the name that you want to give the new tag.
            - *Edit a tag* : ``Key`` is the name of the tag that you want to change the ``Value`` for.
            - *Delete a key* : ``Key`` is the name of the tag you want to remove.
            - *Give a name to a health check* : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a *Name* column that lets you see the name that you've given to each health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthcheck-healthchecktag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of ``Value`` depends on the operation that you want to perform:.

            - *Add a tag to a health check or hosted zone* : ``Value`` is the value that you want to give the new tag.
            - *Edit a tag* : ``Value`` is the new value that you want to assign the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-healthcheck-healthchecktag.html#cfn-route53-healthcheck-healthchecktag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HealthCheckTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnHealthCheckProps",
    jsii_struct_bases=[],
    name_mapping={
        "health_check_config": "healthCheckConfig",
        "health_check_tags": "healthCheckTags",
    },
)
class CfnHealthCheckProps:
    def __init__(
        self,
        *,
        health_check_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.HealthCheckConfigProperty, typing.Dict[builtins.str, typing.Any]]],
        health_check_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.HealthCheckTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHealthCheck``.

        :param health_check_config: A complex type that contains detailed information about one health check. For the values to enter for ``HealthCheckConfig`` , see `HealthCheckConfig <https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html>`_
        :param health_check_tags: The ``HealthCheckTags`` property describes key-value pairs that are associated with an ``AWS::Route53::HealthCheck`` resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_health_check_props = route53.CfnHealthCheckProps(
                health_check_config=route53.CfnHealthCheck.HealthCheckConfigProperty(
                    type="type",
            
                    # the properties below are optional
                    alarm_identifier=route53.CfnHealthCheck.AlarmIdentifierProperty(
                        name="name",
                        region="region"
                    ),
                    child_health_checks=["childHealthChecks"],
                    enable_sni=False,
                    failure_threshold=123,
                    fully_qualified_domain_name="fullyQualifiedDomainName",
                    health_threshold=123,
                    insufficient_data_health_status="insufficientDataHealthStatus",
                    inverted=False,
                    ip_address="ipAddress",
                    measure_latency=False,
                    port=123,
                    regions=["regions"],
                    request_interval=123,
                    resource_path="resourcePath",
                    routing_control_arn="routingControlArn",
                    search_string="searchString"
                ),
            
                # the properties below are optional
                health_check_tags=[route53.CfnHealthCheck.HealthCheckTagProperty(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcc59bb963f4ce3a4eb461ecda6f194c9faa6eea0ca5960c91dfd950e626f687)
            check_type(argname="argument health_check_config", value=health_check_config, expected_type=type_hints["health_check_config"])
            check_type(argname="argument health_check_tags", value=health_check_tags, expected_type=type_hints["health_check_tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "health_check_config": health_check_config,
        }
        if health_check_tags is not None:
            self._values["health_check_tags"] = health_check_tags

    @builtins.property
    def health_check_config(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnHealthCheck.HealthCheckConfigProperty]:
        '''A complex type that contains detailed information about one health check.

        For the values to enter for ``HealthCheckConfig`` , see `HealthCheckConfig <https://docs.aws.amazon.com/Route53/latest/APIReference/API_HealthCheckConfig.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthcheckconfig
        '''
        result = self._values.get("health_check_config")
        assert result is not None, "Required property 'health_check_config' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnHealthCheck.HealthCheckConfigProperty], result)

    @builtins.property
    def health_check_tags(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHealthCheck.HealthCheckTagProperty]]]]:
        '''The ``HealthCheckTags`` property describes key-value pairs that are associated with an ``AWS::Route53::HealthCheck`` resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-healthcheck.html#cfn-route53-healthcheck-healthchecktags
        '''
        result = self._values.get("health_check_tags")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHealthCheck.HealthCheckTagProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHealthCheckProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnHostedZone(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnHostedZone",
):
    '''Creates a new public or private hosted zone.

    You create records in a public hosted zone to define how you want to route traffic on the internet for a domain, such as example.com, and its subdomains (apex.example.com, acme.example.com). You create records in a private hosted zone to define how you want to route traffic for a domain and its subdomains within one or more Amazon Virtual Private Clouds (Amazon VPCs).
    .. epigraph::

       You can't convert a public hosted zone to a private hosted zone or vice versa. Instead, you must create a new hosted zone with the same name and create new resource record sets.

    For more information about charges for hosted zones, see `Amazon Route 53 Pricing <https://docs.aws.amazon.com/route53/pricing/>`_ .

    Note the following:

    - You can't create a hosted zone for a top-level domain (TLD) such as .com.
    - If your domain is registered with a registrar other than Route 53, you must update the name servers with your registrar to make Route 53 the DNS service for the domain. For more information, see `Migrating DNS Service for an Existing Domain to Amazon Route 53 <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/MigratingDNS.html>`_ in the *Amazon Route 53 Developer Guide* .

    When you submit a ``CreateHostedZone`` request, the initial status of the hosted zone is ``PENDING`` . For public hosted zones, this means that the NS and SOA records are not yet available on all Route 53 DNS servers. When the NS and SOA records are available, the status of the zone changes to ``INSYNC`` .

    The ``CreateHostedZone`` request requires the caller to have an ``ec2:DescribeVpcs`` permission.
    .. epigraph::

       When creating private hosted zones, the Amazon VPC must belong to the same partition where the hosted zone is created. A partition is a group of AWS Regions . Each AWS account is scoped to one partition.

       The following are the supported partitions:

       - ``aws`` - AWS Regions
       - ``aws-cn`` - China Regions
       - ``aws-us-gov`` - AWS GovCloud (US) Region

       For more information, see `Access Management <https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html>`_ in the *AWS General Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
    :cloudformationResource: AWS::Route53::HostedZone
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_hosted_zone = route53.CfnHostedZone(self, "MyCfnHostedZone",
            hosted_zone_config=route53.CfnHostedZone.HostedZoneConfigProperty(
                comment="comment"
            ),
            hosted_zone_tags=[route53.CfnHostedZone.HostedZoneTagProperty(
                key="key",
                value="value"
            )],
            name="name",
            query_logging_config=route53.CfnHostedZone.QueryLoggingConfigProperty(
                cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn"
            ),
            vpcs=[route53.CfnHostedZone.VPCProperty(
                vpc_id="vpcId",
                vpc_region="vpcRegion"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHostedZone.HostedZoneConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        hosted_zone_tags: typing.Optional[typing.Sequence[typing.Union["CfnHostedZone.HostedZoneTagProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        query_logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHostedZone.QueryLoggingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vpcs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnHostedZone.VPCProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param hosted_zone_config: A complex type that contains an optional comment. If you don't want to specify a comment, omit the ``HostedZoneConfig`` and ``Comment`` elements.
        :param hosted_zone_tags: Adds, edits, or deletes tags for a health check or a hosted zone. For information about using tags for cost allocation, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the *AWS Billing and Cost Management User Guide* .
        :param name: The name of the domain. Specify a fully qualified domain name, for example, *www.example.com* . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical. If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of ``NameServers`` that are returned by the ``Fn::GetAtt`` intrinsic function.
        :param query_logging_config: Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group. DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following: - Route 53 edge location that responded to the DNS query - Domain or subdomain that was requested - DNS record type, such as A or AAAA - DNS response code, such as ``NoError`` or ``ServFail`` - **Log Group and Resource Policy** - Before you create a query logging configuration, perform the following operations. .. epigraph:: If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically. - Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following: - You must create the log group in the us-east-1 region. - You must use the same AWS account to create the log group and the hosted zone that you want to configure query logging for. - When you create log groups for query logging, we recommend that you use a consistent prefix, for example: ``/aws/route53/ *hosted zone name*`` In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated AWS resources, such as Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging. - Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. You must create the CloudWatch Logs resource policy in the us-east-1 region. For the value of ``Resource`` , specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with ``*`` , for example: ``arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*`` To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values: - For ``aws:SourceArn`` , supply the hosted zone ARN used in creating the query logging configuration. For example, ``aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID`` . - For ``aws:SourceAccount`` , supply the account ID for the account that creates the query logging configuration. For example, ``aws:SourceAccount:111111111111`` . For more information, see `The confused deputy problem <https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html>`_ in the *AWS IAM User Guide* . .. epigraph:: You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the AWS SDKs, or the AWS CLI . - **Log Streams and Edge Locations** - When Route 53 finishes creating the configuration for DNS query logging, it does the following: - Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location. - Begins to send query logs to the applicable log stream. The name of each log stream is in the following format: ``*hosted zone ID* / *edge location code*`` The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the `Route 53 Product Details <https://docs.aws.amazon.com/route53/details/>`_ page. - **Queries That Are Logged** - Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see `Routing Internet Traffic to Your Website or Web Application <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html>`_ in the *Amazon Route 53 Developer Guide* . - **Log File Format** - For a list of the values in each query log and the format of each value, see `Logging DNS Queries <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html>`_ in the *Amazon Route 53 Developer Guide* . - **Pricing** - For information about charges for query logs, see `Amazon CloudWatch Pricing <https://docs.aws.amazon.com/cloudwatch/pricing/>`_ . - **How to Stop Logging** - If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see `DeleteQueryLoggingConfig <https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html>`_ .
        :param vpcs: *Private hosted zones:* A complex type that contains information about the VPCs that are associated with the specified hosted zone. .. epigraph:: For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07dce28bc78bd7a648e7920a0cb1bee52b579eae30c6d32918696dd2fecf73a0)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnHostedZoneProps(
            hosted_zone_config=hosted_zone_config,
            hosted_zone_tags=hosted_zone_tags,
            name=name,
            query_logging_config=query_logging_config,
            vpcs=vpcs,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ec471122074c4efc9cfaeb7b7bef0731889f8080ae94fce69befda5f9fe2e7af)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ef86462d5cfa65a428a6e6bb1b1ba218d87770c0e1448ff8d57375ca2a36ae7)
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
        '''The ID that Amazon Route 53 assigned to the hosted zone when you created it.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrNameServers")
    def attr_name_servers(self) -> typing.List[builtins.str]:
        '''Returns the set of name servers for the specific hosted zone. For example: ``ns1.example.com`` .

        This attribute is not supported for private hosted zones.

        :cloudformationAttribute: NameServers
        '''
        return typing.cast(typing.List[builtins.str], jsii.get(self, "attrNameServers"))

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
    @jsii.member(jsii_name="hostedZoneConfig")
    def hosted_zone_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.HostedZoneConfigProperty"]]:
        '''A complex type that contains an optional comment.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.HostedZoneConfigProperty"]], jsii.get(self, "hostedZoneConfig"))

    @hosted_zone_config.setter
    def hosted_zone_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.HostedZoneConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e764c4ae257c91c5d5b032fbe4eb718b4851ccc5750ef5bd3b5214ef2b4684fd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneConfig", value)

    @builtins.property
    @jsii.member(jsii_name="hostedZoneTagsRaw")
    def hosted_zone_tags_raw(
        self,
    ) -> typing.Optional[typing.List["CfnHostedZone.HostedZoneTagProperty"]]:
        '''Adds, edits, or deletes tags for a health check or a hosted zone.'''
        return typing.cast(typing.Optional[typing.List["CfnHostedZone.HostedZoneTagProperty"]], jsii.get(self, "hostedZoneTagsRaw"))

    @hosted_zone_tags_raw.setter
    def hosted_zone_tags_raw(
        self,
        value: typing.Optional[typing.List["CfnHostedZone.HostedZoneTagProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93e68861780d2e75a54677985f3c250e924418dc9e1ac1cc200b770e633acbb6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneTagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__91099dfc3159698491b9498cddba1ba706c12aeede11ee9ccadf937019c2ae08)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="queryLoggingConfig")
    def query_logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.QueryLoggingConfigProperty"]]:
        '''Creates a configuration for DNS query logging.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.QueryLoggingConfigProperty"]], jsii.get(self, "queryLoggingConfig"))

    @query_logging_config.setter
    def query_logging_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.QueryLoggingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02d1784db152ce69ef63512574d41672ddd53e2038e23c71ff72325772d8b489)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryLoggingConfig", value)

    @builtins.property
    @jsii.member(jsii_name="vpcs")
    def vpcs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.VPCProperty"]]]]:
        '''*Private hosted zones:* A complex type that contains information about the VPCs that are associated with the specified hosted zone.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.VPCProperty"]]]], jsii.get(self, "vpcs"))

    @vpcs.setter
    def vpcs(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnHostedZone.VPCProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__45fa6589ea7645f299a1666ba66ea7f49172916fae56fe49b48ee2d8bfa87241)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vpcs", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHostedZone.HostedZoneConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"comment": "comment"},
    )
    class HostedZoneConfigProperty:
        def __init__(self, *, comment: typing.Optional[builtins.str] = None) -> None:
            '''A complex type that contains an optional comment about your hosted zone.

            If you don't want to specify a comment, omit both the ``HostedZoneConfig`` and ``Comment`` elements.

            :param comment: Any comments that you want to include about the hosted zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                hosted_zone_config_property = route53.CfnHostedZone.HostedZoneConfigProperty(
                    comment="comment"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b9b576716f26dcf7d2edeb0bc854e42f45e229b4fdb03469e0a6e4aa92f0c562)
                check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if comment is not None:
                self._values["comment"] = comment

        @builtins.property
        def comment(self) -> typing.Optional[builtins.str]:
            '''Any comments that you want to include about the hosted zone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzoneconfig.html#cfn-route53-hostedzone-hostedzoneconfig-comment
            '''
            result = self._values.get("comment")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HostedZoneConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHostedZone.HostedZoneTagProperty",
        jsii_struct_bases=[],
        name_mapping={"key": "key", "value": "value"},
    )
    class HostedZoneTagProperty:
        def __init__(self, *, key: builtins.str, value: builtins.str) -> None:
            '''A complex type that contains information about a tag that you want to add or edit for the specified health check or hosted zone.

            :param key: The value of ``Key`` depends on the operation that you want to perform:. - *Add a tag to a health check or hosted zone* : ``Key`` is the name that you want to give the new tag. - *Edit a tag* : ``Key`` is the name of the tag that you want to change the ``Value`` for. - *Delete a key* : ``Key`` is the name of the tag you want to remove. - *Give a name to a health check* : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a *Name* column that lets you see the name that you've given to each health check.
            :param value: The value of ``Value`` depends on the operation that you want to perform:. - *Add a tag to a health check or hosted zone* : ``Value`` is the value that you want to give the new tag. - *Edit a tag* : ``Value`` is the new value that you want to assign the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                hosted_zone_tag_property = route53.CfnHostedZone.HostedZoneTagProperty(
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2ab436cec7f17cd6450fc80b9013e4f05f3f7a983561430595251215b5aedec6)
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "key": key,
                "value": value,
            }

        @builtins.property
        def key(self) -> builtins.str:
            '''The value of ``Key`` depends on the operation that you want to perform:.

            - *Add a tag to a health check or hosted zone* : ``Key`` is the name that you want to give the new tag.
            - *Edit a tag* : ``Key`` is the name of the tag that you want to change the ``Value`` for.
            - *Delete a key* : ``Key`` is the name of the tag you want to remove.
            - *Give a name to a health check* : Edit the default ``Name`` tag. In the Amazon Route 53 console, the list of your health checks includes a *Name* column that lets you see the name that you've given to each health check.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html#cfn-route53-hostedzone-hostedzonetag-key
            '''
            result = self._values.get("key")
            assert result is not None, "Required property 'key' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value of ``Value`` depends on the operation that you want to perform:.

            - *Add a tag to a health check or hosted zone* : ``Value`` is the value that you want to give the new tag.
            - *Edit a tag* : ``Value`` is the new value that you want to assign the tag.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-hostedzonetag.html#cfn-route53-hostedzone-hostedzonetag-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HostedZoneTagProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHostedZone.QueryLoggingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={"cloud_watch_logs_log_group_arn": "cloudWatchLogsLogGroupArn"},
    )
    class QueryLoggingConfigProperty:
        def __init__(self, *, cloud_watch_logs_log_group_arn: builtins.str) -> None:
            '''A complex type that contains information about a configuration for DNS query logging.

            :param cloud_watch_logs_log_group_arn: The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                query_logging_config_property = route53.CfnHostedZone.QueryLoggingConfigProperty(
                    cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3de80e7a9d7826feae12622cf83906c147b708a387e427ae161c27ac169ea16a)
                check_type(argname="argument cloud_watch_logs_log_group_arn", value=cloud_watch_logs_log_group_arn, expected_type=type_hints["cloud_watch_logs_log_group_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cloud_watch_logs_log_group_arn": cloud_watch_logs_log_group_arn,
            }

        @builtins.property
        def cloud_watch_logs_log_group_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the CloudWatch Logs log group that Amazon Route 53 is publishing logs to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-queryloggingconfig.html#cfn-route53-hostedzone-queryloggingconfig-cloudwatchlogsloggrouparn
            '''
            result = self._values.get("cloud_watch_logs_log_group_arn")
            assert result is not None, "Required property 'cloud_watch_logs_log_group_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "QueryLoggingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnHostedZone.VPCProperty",
        jsii_struct_bases=[],
        name_mapping={"vpc_id": "vpcId", "vpc_region": "vpcRegion"},
    )
    class VPCProperty:
        def __init__(self, *, vpc_id: builtins.str, vpc_region: builtins.str) -> None:
            '''*Private hosted zones only:* A complex type that contains information about an Amazon VPC.

            Route 53 Resolver uses the records in the private hosted zone to route traffic in that VPC.
            .. epigraph::

               For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .

            :param vpc_id: *Private hosted zones only:* The ID of an Amazon VPC. .. epigraph:: For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .
            :param vpc_region: *Private hosted zones only:* The region that an Amazon VPC was created in. .. epigraph:: For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                v_pCProperty = route53.CfnHostedZone.VPCProperty(
                    vpc_id="vpcId",
                    vpc_region="vpcRegion"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c68e5afe07b3a7edc63a606f85f787c4486a2bfba1793f83271989294f5d6970)
                check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
                check_type(argname="argument vpc_region", value=vpc_region, expected_type=type_hints["vpc_region"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "vpc_id": vpc_id,
                "vpc_region": vpc_region,
            }

        @builtins.property
        def vpc_id(self) -> builtins.str:
            '''*Private hosted zones only:* The ID of an Amazon VPC.

            .. epigraph::

               For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html#cfn-route53-hostedzone-vpc-vpcid
            '''
            result = self._values.get("vpc_id")
            assert result is not None, "Required property 'vpc_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def vpc_region(self) -> builtins.str:
            '''*Private hosted zones only:* The region that an Amazon VPC was created in.

            .. epigraph::

               For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-hostedzone-vpc.html#cfn-route53-hostedzone-vpc-vpcregion
            '''
            result = self._values.get("vpc_region")
            assert result is not None, "Required property 'vpc_region' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VPCProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnHostedZoneProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_config": "hostedZoneConfig",
        "hosted_zone_tags": "hostedZoneTags",
        "name": "name",
        "query_logging_config": "queryLoggingConfig",
        "vpcs": "vpcs",
    },
)
class CfnHostedZoneProps:
    def __init__(
        self,
        *,
        hosted_zone_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.HostedZoneConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        hosted_zone_tags: typing.Optional[typing.Sequence[typing.Union[CfnHostedZone.HostedZoneTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        query_logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.QueryLoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        vpcs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.VPCProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnHostedZone``.

        :param hosted_zone_config: A complex type that contains an optional comment. If you don't want to specify a comment, omit the ``HostedZoneConfig`` and ``Comment`` elements.
        :param hosted_zone_tags: Adds, edits, or deletes tags for a health check or a hosted zone. For information about using tags for cost allocation, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the *AWS Billing and Cost Management User Guide* .
        :param name: The name of the domain. Specify a fully qualified domain name, for example, *www.example.com* . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical. If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of ``NameServers`` that are returned by the ``Fn::GetAtt`` intrinsic function.
        :param query_logging_config: Creates a configuration for DNS query logging. After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group. DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following: - Route 53 edge location that responded to the DNS query - Domain or subdomain that was requested - DNS record type, such as A or AAAA - DNS response code, such as ``NoError`` or ``ServFail`` - **Log Group and Resource Policy** - Before you create a query logging configuration, perform the following operations. .. epigraph:: If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically. - Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following: - You must create the log group in the us-east-1 region. - You must use the same AWS account to create the log group and the hosted zone that you want to configure query logging for. - When you create log groups for query logging, we recommend that you use a consistent prefix, for example: ``/aws/route53/ *hosted zone name*`` In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated AWS resources, such as Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging. - Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. You must create the CloudWatch Logs resource policy in the us-east-1 region. For the value of ``Resource`` , specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with ``*`` , for example: ``arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*`` To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values: - For ``aws:SourceArn`` , supply the hosted zone ARN used in creating the query logging configuration. For example, ``aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID`` . - For ``aws:SourceAccount`` , supply the account ID for the account that creates the query logging configuration. For example, ``aws:SourceAccount:111111111111`` . For more information, see `The confused deputy problem <https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html>`_ in the *AWS IAM User Guide* . .. epigraph:: You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the AWS SDKs, or the AWS CLI . - **Log Streams and Edge Locations** - When Route 53 finishes creating the configuration for DNS query logging, it does the following: - Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location. - Begins to send query logs to the applicable log stream. The name of each log stream is in the following format: ``*hosted zone ID* / *edge location code*`` The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the `Route 53 Product Details <https://docs.aws.amazon.com/route53/details/>`_ page. - **Queries That Are Logged** - Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see `Routing Internet Traffic to Your Website or Web Application <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html>`_ in the *Amazon Route 53 Developer Guide* . - **Log File Format** - For a list of the values in each query log and the format of each value, see `Logging DNS Queries <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html>`_ in the *Amazon Route 53 Developer Guide* . - **Pricing** - For information about charges for query logs, see `Amazon CloudWatch Pricing <https://docs.aws.amazon.com/cloudwatch/pricing/>`_ . - **How to Stop Logging** - If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see `DeleteQueryLoggingConfig <https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html>`_ .
        :param vpcs: *Private hosted zones:* A complex type that contains information about the VPCs that are associated with the specified hosted zone. .. epigraph:: For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_hosted_zone_props = route53.CfnHostedZoneProps(
                hosted_zone_config=route53.CfnHostedZone.HostedZoneConfigProperty(
                    comment="comment"
                ),
                hosted_zone_tags=[route53.CfnHostedZone.HostedZoneTagProperty(
                    key="key",
                    value="value"
                )],
                name="name",
                query_logging_config=route53.CfnHostedZone.QueryLoggingConfigProperty(
                    cloud_watch_logs_log_group_arn="cloudWatchLogsLogGroupArn"
                ),
                vpcs=[route53.CfnHostedZone.VPCProperty(
                    vpc_id="vpcId",
                    vpc_region="vpcRegion"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__490d21becaf73ea78f8b34688d2d62e4e21d941f510e74d0a5acce1c9a8a35c3)
            check_type(argname="argument hosted_zone_config", value=hosted_zone_config, expected_type=type_hints["hosted_zone_config"])
            check_type(argname="argument hosted_zone_tags", value=hosted_zone_tags, expected_type=type_hints["hosted_zone_tags"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument query_logging_config", value=query_logging_config, expected_type=type_hints["query_logging_config"])
            check_type(argname="argument vpcs", value=vpcs, expected_type=type_hints["vpcs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if hosted_zone_config is not None:
            self._values["hosted_zone_config"] = hosted_zone_config
        if hosted_zone_tags is not None:
            self._values["hosted_zone_tags"] = hosted_zone_tags
        if name is not None:
            self._values["name"] = name
        if query_logging_config is not None:
            self._values["query_logging_config"] = query_logging_config
        if vpcs is not None:
            self._values["vpcs"] = vpcs

    @builtins.property
    def hosted_zone_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHostedZone.HostedZoneConfigProperty]]:
        '''A complex type that contains an optional comment.

        If you don't want to specify a comment, omit the ``HostedZoneConfig`` and ``Comment`` elements.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzoneconfig
        '''
        result = self._values.get("hosted_zone_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHostedZone.HostedZoneConfigProperty]], result)

    @builtins.property
    def hosted_zone_tags(
        self,
    ) -> typing.Optional[typing.List[CfnHostedZone.HostedZoneTagProperty]]:
        '''Adds, edits, or deletes tags for a health check or a hosted zone.

        For information about using tags for cost allocation, see `Using Cost Allocation Tags <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html>`_ in the *AWS Billing and Cost Management User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-hostedzonetags
        '''
        result = self._values.get("hosted_zone_tags")
        return typing.cast(typing.Optional[typing.List[CfnHostedZone.HostedZoneTagProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the domain.

        Specify a fully qualified domain name, for example, *www.example.com* . The trailing dot is optional; Amazon Route 53 assumes that the domain name is fully qualified. This means that Route 53 treats *www.example.com* (without a trailing dot) and *www.example.com.* (with a trailing dot) as identical.

        If you're creating a public hosted zone, this is the name you have registered with your DNS registrar. If your domain name is registered with a registrar other than Route 53, change the name servers for your domain to the set of ``NameServers`` that are returned by the ``Fn::GetAtt`` intrinsic function.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_logging_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHostedZone.QueryLoggingConfigProperty]]:
        '''Creates a configuration for DNS query logging.

        After you create a query logging configuration, Amazon Route 53 begins to publish log data to an Amazon CloudWatch Logs log group.

        DNS query logs contain information about the queries that Route 53 receives for a specified public hosted zone, such as the following:

        - Route 53 edge location that responded to the DNS query
        - Domain or subdomain that was requested
        - DNS record type, such as A or AAAA
        - DNS response code, such as ``NoError`` or ``ServFail``
        - **Log Group and Resource Policy** - Before you create a query logging configuration, perform the following operations.

        .. epigraph::

           If you create a query logging configuration using the Route 53 console, Route 53 performs these operations automatically.

        - Create a CloudWatch Logs log group, and make note of the ARN, which you specify when you create a query logging configuration. Note the following:
        - You must create the log group in the us-east-1 region.
        - You must use the same AWS account to create the log group and the hosted zone that you want to configure query logging for.
        - When you create log groups for query logging, we recommend that you use a consistent prefix, for example:

        ``/aws/route53/ *hosted zone name*``

        In the next step, you'll create a resource policy, which controls access to one or more log groups and the associated AWS resources, such as Route 53 hosted zones. There's a limit on the number of resource policies that you can create, so we recommend that you use a consistent prefix so you can use the same resource policy for all the log groups that you create for query logging.

        - Create a CloudWatch Logs resource policy, and give it the permissions that Route 53 needs to create log streams and to send query logs to log streams. You must create the CloudWatch Logs resource policy in the us-east-1 region. For the value of ``Resource`` , specify the ARN for the log group that you created in the previous step. To use the same resource policy for all the CloudWatch Logs log groups that you created for query logging configurations, replace the hosted zone name with ``*`` , for example:

        ``arn:aws:logs:us-east-1:123412341234:log-group:/aws/route53/*``

        To avoid the confused deputy problem, a security issue where an entity without a permission for an action can coerce a more-privileged entity to perform it, you can optionally limit the permissions that a service has to a resource in a resource-based policy by supplying the following values:

        - For ``aws:SourceArn`` , supply the hosted zone ARN used in creating the query logging configuration. For example, ``aws:SourceArn: arn:aws:route53:::hostedzone/hosted zone ID`` .
        - For ``aws:SourceAccount`` , supply the account ID for the account that creates the query logging configuration. For example, ``aws:SourceAccount:111111111111`` .

        For more information, see `The confused deputy problem <https://docs.aws.amazon.com/IAM/latest/UserGuide/confused-deputy.html>`_ in the *AWS IAM User Guide* .
        .. epigraph::

           You can't use the CloudWatch console to create or edit a resource policy. You must use the CloudWatch API, one of the AWS SDKs, or the AWS CLI .

        - **Log Streams and Edge Locations** - When Route 53 finishes creating the configuration for DNS query logging, it does the following:
        - Creates a log stream for an edge location the first time that the edge location responds to DNS queries for the specified hosted zone. That log stream is used to log all queries that Route 53 responds to for that edge location.
        - Begins to send query logs to the applicable log stream.

        The name of each log stream is in the following format:

        ``*hosted zone ID* / *edge location code*``

        The edge location code is a three-letter code and an arbitrarily assigned number, for example, DFW3. The three-letter code typically corresponds with the International Air Transport Association airport code for an airport near the edge location. (These abbreviations might change in the future.) For a list of edge locations, see "The Route 53 Global Network" on the `Route 53 Product Details <https://docs.aws.amazon.com/route53/details/>`_ page.

        - **Queries That Are Logged** - Query logs contain only the queries that DNS resolvers forward to Route 53. If a DNS resolver has already cached the response to a query (such as the IP address for a load balancer for example.com), the resolver will continue to return the cached response. It doesn't forward another query to Route 53 until the TTL for the corresponding resource record set expires. Depending on how many DNS queries are submitted for a resource record set, and depending on the TTL for that resource record set, query logs might contain information about only one query out of every several thousand queries that are submitted to DNS. For more information about how DNS works, see `Routing Internet Traffic to Your Website or Web Application <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/welcome-dns-service.html>`_ in the *Amazon Route 53 Developer Guide* .
        - **Log File Format** - For a list of the values in each query log and the format of each value, see `Logging DNS Queries <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/query-logs.html>`_ in the *Amazon Route 53 Developer Guide* .
        - **Pricing** - For information about charges for query logs, see `Amazon CloudWatch Pricing <https://docs.aws.amazon.com/cloudwatch/pricing/>`_ .
        - **How to Stop Logging** - If you want Route 53 to stop sending query logs to CloudWatch Logs, delete the query logging configuration. For more information, see `DeleteQueryLoggingConfig <https://docs.aws.amazon.com/Route53/latest/APIReference/API_DeleteQueryLoggingConfig.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-queryloggingconfig
        '''
        result = self._values.get("query_logging_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHostedZone.QueryLoggingConfigProperty]], result)

    @builtins.property
    def vpcs(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHostedZone.VPCProperty]]]]:
        '''*Private hosted zones:* A complex type that contains information about the VPCs that are associated with the specified hosted zone.

        .. epigraph::

           For public hosted zones, omit ``VPCs`` , ``VPCId`` , and ``VPCRegion`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-hostedzone.html#cfn-route53-hostedzone-vpcs
        '''
        result = self._values.get("vpcs")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHostedZone.VPCProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnKeySigningKey(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnKeySigningKey",
):
    '''The ``AWS::Route53::KeySigningKey`` resource creates a new key-signing key (KSK) in a hosted zone.

    The hosted zone ID is passed as a parameter in the KSK properties. You can specify the properties of this KSK using the ``Name`` , ``Status`` , and ``KeyManagementServiceArn`` properties of the resource.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html
    :cloudformationResource: AWS::Route53::KeySigningKey
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_key_signing_key = route53.CfnKeySigningKey(self, "MyCfnKeySigningKey",
            hosted_zone_id="hostedZoneId",
            key_management_service_arn="keyManagementServiceArn",
            name="name",
            status="status"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
        key_management_service_arn: builtins.str,
        name: builtins.str,
        status: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param hosted_zone_id: The unique string (ID) that is used to identify a hosted zone. For example: ``Z00001111A1ABCaaABC11`` .
        :param key_management_service_arn: The Amazon resource name (ARN) for a customer managed customer master key (CMK) in AWS Key Management Service ( AWS KMS ). The ``KeyManagementServiceArn`` must be unique for each key-signing key (KSK) in a single hosted zone. For example: ``arn:aws:kms:us-east-1:111122223333:key/111a2222-a11b-1ab1-2ab2-1ab21a2b3a111`` .
        :param name: A string used to identify a key-signing key (KSK). ``Name`` can include numbers, letters, and underscores (_). ``Name`` must be unique for each key-signing key in the same hosted zone.
        :param status: A string that represents the current key-signing key (KSK) status. Status can have one of the following values: - **ACTIVE** - The KSK is being used for signing. - **INACTIVE** - The KSK is not being used for signing. - **DELETING** - The KSK is in the process of being deleted. - **ACTION_NEEDED** - There is a problem with the KSK that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed. - **INTERNAL_FAILURE** - There was an error during a request. Before you can continue to work with DNSSEC signing, including actions that involve this KSK, you must correct the problem. For example, you may need to activate or deactivate the KSK.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1ab2cf8ecb830d1da730f1aa8733016826e21289a18b31b5c2960242217b6d2d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnKeySigningKeyProps(
            hosted_zone_id=hosted_zone_id,
            key_management_service_arn=key_management_service_arn,
            name=name,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6cd424602d0e47520e23aa4bb0661d6d253dfaa1526f46b316cc886c1c8e3c90)
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
            type_hints = typing.get_type_hints(_typecheckingstub__0a974a23e0b44cc31e19609aafb595755d873d5b149a168373eca42644ebb067)
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
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        '''The unique string (ID) that is used to identify a hosted zone.'''
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a977d3e0b2b3f9a9e1ffa361297317c52032e041b63d5aea96d7b3236e1bcc76)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="keyManagementServiceArn")
    def key_management_service_arn(self) -> builtins.str:
        '''The Amazon resource name (ARN) for a customer managed customer master key (CMK) in AWS Key Management Service ( AWS KMS ).'''
        return typing.cast(builtins.str, jsii.get(self, "keyManagementServiceArn"))

    @key_management_service_arn.setter
    def key_management_service_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b11e2fadcc2e7f8dd0b969ae638b6fef820af613ac524490a21fcfa87cbe4b1b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyManagementServiceArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''A string used to identify a key-signing key (KSK).'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c99ca2799db6059925703f6f02ff9fa298bf7e6106b621b1f66a86e2928f1a56)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> builtins.str:
        '''A string that represents the current key-signing key (KSK) status.'''
        return typing.cast(builtins.str, jsii.get(self, "status"))

    @status.setter
    def status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8a53087887c17259968953d4112cc4979b6d97d83c742c614204a0840acd1951)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "status", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnKeySigningKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone_id": "hostedZoneId",
        "key_management_service_arn": "keyManagementServiceArn",
        "name": "name",
        "status": "status",
    },
)
class CfnKeySigningKeyProps:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        key_management_service_arn: builtins.str,
        name: builtins.str,
        status: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnKeySigningKey``.

        :param hosted_zone_id: The unique string (ID) that is used to identify a hosted zone. For example: ``Z00001111A1ABCaaABC11`` .
        :param key_management_service_arn: The Amazon resource name (ARN) for a customer managed customer master key (CMK) in AWS Key Management Service ( AWS KMS ). The ``KeyManagementServiceArn`` must be unique for each key-signing key (KSK) in a single hosted zone. For example: ``arn:aws:kms:us-east-1:111122223333:key/111a2222-a11b-1ab1-2ab2-1ab21a2b3a111`` .
        :param name: A string used to identify a key-signing key (KSK). ``Name`` can include numbers, letters, and underscores (_). ``Name`` must be unique for each key-signing key in the same hosted zone.
        :param status: A string that represents the current key-signing key (KSK) status. Status can have one of the following values: - **ACTIVE** - The KSK is being used for signing. - **INACTIVE** - The KSK is not being used for signing. - **DELETING** - The KSK is in the process of being deleted. - **ACTION_NEEDED** - There is a problem with the KSK that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed. - **INTERNAL_FAILURE** - There was an error during a request. Before you can continue to work with DNSSEC signing, including actions that involve this KSK, you must correct the problem. For example, you may need to activate or deactivate the KSK.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_key_signing_key_props = route53.CfnKeySigningKeyProps(
                hosted_zone_id="hostedZoneId",
                key_management_service_arn="keyManagementServiceArn",
                name="name",
                status="status"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34f881609091b0893ac028adbb4be46f434c735b3d01e67b1aefcf17bc0abb02)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument key_management_service_arn", value=key_management_service_arn, expected_type=type_hints["key_management_service_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "key_management_service_arn": key_management_service_arn,
            "name": name,
            "status": status,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''The unique string (ID) that is used to identify a hosted zone.

        For example: ``Z00001111A1ABCaaABC11`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-hostedzoneid
        '''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def key_management_service_arn(self) -> builtins.str:
        '''The Amazon resource name (ARN) for a customer managed customer master key (CMK) in AWS Key Management Service ( AWS KMS ).

        The ``KeyManagementServiceArn`` must be unique for each key-signing key (KSK) in a single hosted zone. For example: ``arn:aws:kms:us-east-1:111122223333:key/111a2222-a11b-1ab1-2ab2-1ab21a2b3a111`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-keymanagementservicearn
        '''
        result = self._values.get("key_management_service_arn")
        assert result is not None, "Required property 'key_management_service_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''A string used to identify a key-signing key (KSK).

        ``Name`` can include numbers, letters, and underscores (_). ``Name`` must be unique for each key-signing key in the same hosted zone.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status(self) -> builtins.str:
        '''A string that represents the current key-signing key (KSK) status.

        Status can have one of the following values:

        - **ACTIVE** - The KSK is being used for signing.
        - **INACTIVE** - The KSK is not being used for signing.
        - **DELETING** - The KSK is in the process of being deleted.
        - **ACTION_NEEDED** - There is a problem with the KSK that requires you to take action to resolve. For example, the customer managed key might have been deleted, or the permissions for the customer managed key might have been changed.
        - **INTERNAL_FAILURE** - There was an error during a request. Before you can continue to work with DNSSEC signing, including actions that involve this KSK, you must correct the problem. For example, you may need to activate or deactivate the KSK.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-keysigningkey.html#cfn-route53-keysigningkey-status
        '''
        result = self._values.get("status")
        assert result is not None, "Required property 'status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnKeySigningKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnRecordSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnRecordSet",
):
    '''Information about the record that you want to create.

    The ``AWS::Route53::RecordSet`` type can be used as a standalone resource or as an embedded property in the ``AWS::Route53::RecordSetGroup`` type. Note that some ``AWS::Route53::RecordSet`` properties are valid only when used within ``AWS::Route53::RecordSetGroup`` .

    For more information, see `ChangeResourceRecordSets <https://docs.aws.amazon.com/Route53/latest/APIReference/API_ChangeResourceRecordSets.html>`_ in the *Amazon Route 53 API Reference* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html
    :cloudformationResource: AWS::Route53::RecordSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_record_set = route53.CfnRecordSet(self, "MyCfnRecordSet",
            name="name",
            type="type",
        
            # the properties below are optional
            alias_target=route53.CfnRecordSet.AliasTargetProperty(
                dns_name="dnsName",
                hosted_zone_id="hostedZoneId",
        
                # the properties below are optional
                evaluate_target_health=False
            ),
            cidr_routing_config=route53.CfnRecordSet.CidrRoutingConfigProperty(
                collection_id="collectionId",
                location_name="locationName"
            ),
            comment="comment",
            failover="failover",
            geo_location=route53.CfnRecordSet.GeoLocationProperty(
                continent_code="continentCode",
                country_code="countryCode",
                subdivision_code="subdivisionCode"
            ),
            geo_proximity_location=route53.CfnRecordSet.GeoProximityLocationProperty(
                aws_region="awsRegion",
                bias=123,
                coordinates=route53.CfnRecordSet.CoordinatesProperty(
                    latitude="latitude",
                    longitude="longitude"
                ),
                local_zone_group="localZoneGroup"
            ),
            health_check_id="healthCheckId",
            hosted_zone_id="hostedZoneId",
            hosted_zone_name="hostedZoneName",
            multi_value_answer=False,
            region="region",
            resource_records=["resourceRecords"],
            set_identifier="setIdentifier",
            ttl="ttl",
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        type: builtins.str,
        alias_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSet.AliasTargetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        cidr_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSet.CidrRoutingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        comment: typing.Optional[builtins.str] = None,
        failover: typing.Optional[builtins.str] = None,
        geo_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSet.GeoLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        geo_proximity_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSet.GeoProximityLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        health_check_id: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        region: typing.Optional[builtins.str] = None,
        resource_records: typing.Optional[typing.Sequence[builtins.str]] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record in the specified hosted zone. *ChangeResourceRecordSets Only* Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical. For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`_ in the *Amazon Route 53 Developer Guide* . You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following: - The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` . - The * can't replace any of the middle labels, for example, marketing.*.example.com. - If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. .. epigraph:: You can't use the * wildcard for resource records sets that have a type of NS.
        :param type: The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* . Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``DS`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT`` Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group. Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` | ``CAA`` .. epigraph:: SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <https://docs.aws.amazon.com/http://tools.ietf.org/html/rfc7208#section-14.1>`_ . Values for alias resource record sets: - *Amazon API Gateway custom regional APIs and edge-optimized APIs:* ``A`` - *CloudFront distributions:* ``A`` If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` . - *Amazon API Gateway environment that has a regionalized subdomain* : ``A`` - *ELB load balancers:* ``A`` | ``AAAA`` - *Amazon S3 buckets:* ``A`` - *Amazon Virtual Private Cloud interface VPC endpoints* ``A`` - *Another resource record set in this hosted zone:* Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` . .. epigraph:: If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't route traffic to a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.
        :param alias_target: *Alias resource record sets only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to. If you're creating resource records sets for a private hosted zone, note the following: - You can't create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution. - For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ in the *Amazon Route 53 Developer Guide* .
        :param cidr_routing_config: The object that is specified in resource record set object when you are linking a resource record set to a CIDR location. A ``LocationName`` with an asterisk “*” can be used to create a default CIDR record. ``CollectionId`` is still required for default record.
        :param comment: *Optional:* Any comments you want to include about a change batch request.
        :param failover: *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set. Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets: - When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. - When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set. - When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. - If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets. For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true. For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_
        :param geo_location: *Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` . If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource. You can't create two geolocation resource record sets that specify the same geographic location. The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements. .. epigraph:: Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Route 53 returns a "no answer" response for queries from those locations. You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.
        :param geo_proximity_location: *GeoproximityLocation resource record sets only:* A complex type that lets you control how Route 53 responds to DNS queries based on the geographic origin of the query and your resources.
        :param health_check_id: If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check. Route 53 determines whether a resource record set is healthy based on one of the following: - By periodically sending a request to the endpoint that is specified in the health check - By aggregating the status of a specified group of health checks (calculated health checks) - By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) .. epigraph:: Route 53 doesn't check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check. For more information, see the following topics in the *Amazon Route 53 Developer Guide* : - `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ *When to Specify HealthCheckId* Specifying a value for ``HealthCheckId`` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations: - *Non-alias resource record sets* : You're checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets. If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly. - *Alias resource record sets* : You specify the following settings: - You set ``EvaluateTargetHealth`` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A). - You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone. - You specify a health check ID for the non-alias resource record set. If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with. If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set. .. epigraph:: The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets. *Geolocation Routing* For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has ``*`` for ``CountryCode`` is ``*`` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy: - The United States - North America - The default resource record set *Specifying the Health Check Endpoint by Domain Name* If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets ( ``www.example.com`` ). .. epigraph:: Health check results will be unpredictable if you do the following: - Create a health check that has the same value for ``FullyQualifiedDomainName`` as the name of a resource record set. - Associate that health check with the resource record set.
        :param hosted_zone_id: The ID of the hosted zone that you want to create records in. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param hosted_zone_name: The name of the hosted zone that you want to create records in. You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` . When you create a stack using an AWS::Route53::RecordSet that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the HostedZoneName. If AWS CloudFormation cannot find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param multi_value_answer: *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following: - If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. - If you don't associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy. - Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records. - If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records. - When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records. - If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. You can't create multivalue answer alias records.
        :param region: *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Note the following: - You can only specify one ``ResourceRecord`` per latency resource record set. - You can only create one latency resource record set for each Amazon EC2 Region. - You aren't required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. - You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets.
        :param resource_records: One or more values that correspond with the value that you specified for the ``Type`` property. For example, if you specified ``A`` for ``Type`` , you specify one or more IP addresses in IPv4 format for ``ResourceRecords`` . For information about the format of values for each record type, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* . Note the following: - You can specify more than one value for all record types except CNAME and SOA. - The maximum length of a value is 4000 characters. - If you're creating an alias record, omit ``ResourceRecords`` .
        :param set_identifier: *Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set. For information about routing policies, see `Choosing a Routing Policy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`_ in the *Amazon Route 53 Developer Guide* .
        :param ttl: The resource record cache time to live (TTL), in seconds. Note the following:. - If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target. - If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. - All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . - If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` .
        :param weight: *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following: - You must specify a value for the ``Weight`` element for every weighted resource record set. - You can only specify one ``ResourceRecord`` per weighted resource record set. - You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. - You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. - For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Route 53 Active-Active and Active-Passive Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`_ in the *Amazon Route 53 Developer Guide* .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5260f62d2297374b2126da361d614f7922d306048a751f4287d4f7b25251b21f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRecordSetProps(
            name=name,
            type=type,
            alias_target=alias_target,
            cidr_routing_config=cidr_routing_config,
            comment=comment,
            failover=failover,
            geo_location=geo_location,
            geo_proximity_location=geo_proximity_location,
            health_check_id=health_check_id,
            hosted_zone_id=hosted_zone_id,
            hosted_zone_name=hosted_zone_name,
            multi_value_answer=multi_value_answer,
            region=region,
            resource_records=resource_records,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3b594e45af3ec7b4a87f2e38151e582ff1da92bd5457b214b477cfd403181bea)
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
            type_hints = typing.get_type_hints(_typecheckingstub__df3adfbdf92c6a814f5e524f14898f0c7ffdd8d142085c462e1fe287a77fe1ba)
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
        '''Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__173457195308ceadf9faa78064a52b9ebc4a356fcff5446dce5527a0f82366c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The DNS record type.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0d764bdec1a7fb5aef453f572d560d1b8aed69fb8dcfec021e5660608a78cd63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="aliasTarget")
    def alias_target(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.AliasTargetProperty"]]:
        '''*Alias resource record sets only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.AliasTargetProperty"]], jsii.get(self, "aliasTarget"))

    @alias_target.setter
    def alias_target(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.AliasTargetProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0a16cf391736226a70d1a59be2ffd652193be54e61b33e07b2b502b7444ebc0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aliasTarget", value)

    @builtins.property
    @jsii.member(jsii_name="cidrRoutingConfig")
    def cidr_routing_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.CidrRoutingConfigProperty"]]:
        '''The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.CidrRoutingConfigProperty"]], jsii.get(self, "cidrRoutingConfig"))

    @cidr_routing_config.setter
    def cidr_routing_config(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.CidrRoutingConfigProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9573d618d7f59fad50ecf9e676d892ccfe65d8be595e465b068eec35f7931458)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "cidrRoutingConfig", value)

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[builtins.str]:
        '''*Optional:* Any comments you want to include about a change batch request.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8e87d623f2ac71368cf9931ccdeb8214817a43ef5c3db34b4027a16981eba4e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="failover")
    def failover(self) -> typing.Optional[builtins.str]:
        '''*Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "failover"))

    @failover.setter
    def failover(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__79006fc8c23dbed3ebc1e2c4a59dbaef71eada9146612d1d44ad17bf006a1f70)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "failover", value)

    @builtins.property
    @jsii.member(jsii_name="geoLocation")
    def geo_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.GeoLocationProperty"]]:
        '''*Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.GeoLocationProperty"]], jsii.get(self, "geoLocation"))

    @geo_location.setter
    def geo_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.GeoLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e7b257b8973ecbc1eff717cef5d9e9a86a7e93521a1f67acf22b2e8461e1b642)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoLocation", value)

    @builtins.property
    @jsii.member(jsii_name="geoProximityLocation")
    def geo_proximity_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.GeoProximityLocationProperty"]]:
        '''*GeoproximityLocation resource record sets only:* A complex type that lets you control how Route 53 responds to DNS queries based on the geographic origin of the query and your resources.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.GeoProximityLocationProperty"]], jsii.get(self, "geoProximityLocation"))

    @geo_proximity_location.setter
    def geo_proximity_location(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.GeoProximityLocationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ac8d1aee0fc5c4e2eba653391bb8b61826a08b6708db398bae5b22b4e13fcf05)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "geoProximityLocation", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckId")
    def health_check_id(self) -> typing.Optional[builtins.str]:
        '''If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "healthCheckId"))

    @health_check_id.setter
    def health_check_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6008831249a60a522c31e8ed28371a87feee29b69976deadfbbb7939c49e5a0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckId", value)

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the hosted zone that you want to create records in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostedZoneId"))

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3afc428680f9605da623df52766517926597c1cedf85b11836d156e5b0492fff)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''The name of the hosted zone that you want to create records in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostedZoneName"))

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a7ed3b70491b7ea26f2195c97e2146c9f0e7366194f534e8a71a2dbcde9c7634)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneName", value)

    @builtins.property
    @jsii.member(jsii_name="multiValueAnswer")
    def multi_value_answer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` .'''
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], jsii.get(self, "multiValueAnswer"))

    @multi_value_answer.setter
    def multi_value_answer(
        self,
        value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc829fb8c432409e77ff577c111238c3b8554f78a040b7ecdffeb62edb27cf24)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "multiValueAnswer", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> typing.Optional[builtins.str]:
        '''*Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "region"))

    @region.setter
    def region(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4e8e56811d430d9adaea085bb5b15a937d1a1a06eb6f77c3eb66770f6f8b5073)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)

    @builtins.property
    @jsii.member(jsii_name="resourceRecords")
    def resource_records(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more values that correspond with the value that you specified for the ``Type`` property.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "resourceRecords"))

    @resource_records.setter
    def resource_records(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b020353bfb0b9ee7bc698effc5888164835bd548ead89bdc9fd99a31474d7cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceRecords", value)

    @builtins.property
    @jsii.member(jsii_name="setIdentifier")
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''*Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "setIdentifier"))

    @set_identifier.setter
    def set_identifier(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b95c315d1a586fa24b707f1b31210ab6858b88d54fc32c5fab80e08220930c7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "setIdentifier", value)

    @builtins.property
    @jsii.member(jsii_name="ttl")
    def ttl(self) -> typing.Optional[builtins.str]:
        '''The resource record cache time to live (TTL), in seconds.

        Note the following:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ttl"))

    @ttl.setter
    def ttl(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6235e7f8dad691c76887db81a7b5573fb5ed22b4706905208bbca87c9087002d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ttl", value)

    @builtins.property
    @jsii.member(jsii_name="weight")
    def weight(self) -> typing.Optional[jsii.Number]:
        '''*Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "weight"))

    @weight.setter
    def weight(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__166c0517a88d98d1b7fe07fa34082de049ec954fde21b5c1376524e3c7146134)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "weight", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSet.AliasTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_name": "dnsName",
            "hosted_zone_id": "hostedZoneId",
            "evaluate_target_health": "evaluateTargetHealth",
        },
    )
    class AliasTargetProperty:
        def __init__(
            self,
            *,
            dns_name: builtins.str,
            hosted_zone_id: builtins.str,
            evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''*Alias records only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.

            When creating records for a private hosted zone, note the following:

            - Creating geolocation alias and latency alias records in a private hosted zone is allowed but not supported.
            - For information about creating failover records in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ .

            :param dns_name: *Alias records only:* The value that you specify depends on where you want to route queries:. - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the applicable domain name for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ : - For regional APIs, specify the value of ``regionalDomainName`` . - For edge-optimized APIs, specify the value of ``distributionDomainName`` . This is the name of the associated CloudFront distribution, such as ``da1b2c3d4e5.cloudfront.net`` . .. epigraph:: The name of the record that you're creating must match a custom domain name for your API, such as ``api.example.com`` . - **Amazon Virtual Private Cloud interface VPC endpoint** - Enter the API endpoint for the interface endpoint, such as ``vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com`` . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of ``DnsName`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ . - **CloudFront distribution** - Specify the domain name that CloudFront assigned when you created your distribution. Your CloudFront distribution must include an alternate domain name that matches the name of the record. For example, if the name of the record is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`_ in the *Amazon CloudFront Developer Guide* . You can't create a record in a private hosted zone to route traffic to a CloudFront distribution. .. epigraph:: For failover alias records, you can't specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can't include the same alternate domain name in more than one distribution. - **Elastic Beanstalk environment** - If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name ``my-environment. *us-west-2* .elasticbeanstalk.com`` is a regionalized domain name. .. epigraph:: For environments that were created before early 2016, the domain name doesn't include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can't create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can't create a record that routes traffic for example.com to your Elastic Beanstalk environment. For Elastic Beanstalk environments that have regionalized subdomains, specify the ``CNAME`` attribute for the environment. You can use the following methods to get the value of the CNAME attribute: - *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . - *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`_ in the *AWS Elastic Beanstalk API Reference* . - *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`_ in the *AWS CLI* . - **ELB load balancer** - Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console , the ELB API, or the AWS CLI . - *AWS Management Console* : Go to the EC2 page, choose *Load Balancers* in the navigation pane, choose the load balancer, choose the *Description* tab, and get the value of the *DNS name* field. If you're routing traffic to a Classic Load Balancer, get the value that begins with *dualstack* . If you're routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA. - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: - Classic Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_ - Application and Network Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the value of ``DNSName`` : - `Classic Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ . - `Application and Network Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ . - *AWS CLI* : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: - Classic Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_ - Application and Network Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_ - **Global Accelerator accelerator** - Specify the DNS name for your accelerator: - *Global Accelerator API* : To get the DNS name, use `DescribeAccelerator <https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html>`_ . - *AWS CLI* : To get the DNS name, use `describe-accelerator <https://docs.aws.amazon.com/cli/latest/reference/globalaccelerator/describe-accelerator.html>`_ . - **Amazon S3 bucket that is configured as a static website** - Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, ``s3-website.us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`_ in the *Amazon Route 53 Developer Guide.* - **Another Route 53 record** - Specify the value of the ``Name`` element for a record in the current hosted zone. .. epigraph:: If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't specify the domain name for a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record that you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.
            :param hosted_zone_id: *Alias resource records sets only* : The value used depends on where you want to route traffic:. - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ : - For regional APIs, specify the value of ``regionalHostedZoneId`` . - For edge-optimized APIs, specify the value of ``distributionHostedZoneId`` . - **Amazon Virtual Private Cloud interface VPC endpoint** - Specify the hosted zone ID for your interface endpoint. You can get the value of ``HostedZoneId`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ . - **CloudFront distribution** - Specify ``Z2FDTNDATAQYW2`` . This is always the hosted zone ID when you create an alias record that routes traffic to a CloudFront distribution. .. epigraph:: Alias records for CloudFront can't be created in a private zone. - **Elastic Beanstalk environment** - Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html>`_ in the *Amazon Web Services General Reference* . - **ELB load balancer** - Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID: - `Service Endpoints <https://docs.aws.amazon.com/general/latest/gr/elb.html>`_ table in the "Elastic Load Balancing Endpoints and Quotas" topic in the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers. - *AWS Management Console* : Go to the Amazon EC2 page, choose *Load Balancers* in the navigation pane, select the load balancer, and get the value of the *Hosted zone* field on the *Description* tab. - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide: - Classic Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` . - Application and Network Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneID`` . - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the applicable value: - Classic Load Balancers: Get `CanonicalHostedZoneNameID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ . - Application and Network Load Balancers: Get `CanonicalHostedZoneID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ . - *AWS CLI* : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide: - Classic Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` . - Application and Network Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneID`` . - **Global Accelerator accelerator** - Specify ``Z2BJ6XQ5FK7U4H`` . - **An Amazon S3 bucket configured as a static website** - Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* . - **Another Route 53 record in your hosted zone** - Specify the hosted zone ID of your hosted zone. (An alias record can't reference a record in a different hosted zone.)
            :param evaluate_target_health: *Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When ``EvaluateTargetHealth`` is ``true`` , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer or another resource record set in the hosted zone. Note the following: - **CloudFront distributions** - You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution. - **Elastic Beanstalk environments that have regionalized subdomains** - If you specify an Elastic Beanstalk environment in ``DNSName`` and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single Amazon EC2 instance, there are no special requirements. - **ELB load balancers** - Health checking behavior depends on the type of load balancer: - *Classic Load Balancers* : If you specify an ELB Classic Load Balancer in ``DNSName`` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources. - *Application and Network Load Balancers* : If you specify an ELB Application or Network Load Balancer and you set ``EvaluateTargetHealth`` to ``true`` , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer: - For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources. - A target group that has no registered targets is considered unhealthy. .. epigraph:: When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer. - **S3 buckets** - There are no special requirements for setting ``EvaluateTargetHealth`` to ``true`` when the alias target is an S3 bucket. - **Other records in the same hosted zone** - If the AWS resource that you specify in ``DNSName`` is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see `What Happens When You Omit Health Checks? <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`_ in the *Amazon Route 53 Developer Guide* . For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-aliastarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                alias_target_property = route53.CfnRecordSet.AliasTargetProperty(
                    dns_name="dnsName",
                    hosted_zone_id="hostedZoneId",
                
                    # the properties below are optional
                    evaluate_target_health=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a1143e059c44e7a7f16565322a7c9305d2eb0d507ef54d57d3dab326b7f69648)
                check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dns_name": dns_name,
                "hosted_zone_id": hosted_zone_id,
            }
            if evaluate_target_health is not None:
                self._values["evaluate_target_health"] = evaluate_target_health

        @builtins.property
        def dns_name(self) -> builtins.str:
            '''*Alias records only:* The value that you specify depends on where you want to route queries:.

            - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the applicable domain name for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ :
            - For regional APIs, specify the value of ``regionalDomainName`` .
            - For edge-optimized APIs, specify the value of ``distributionDomainName`` . This is the name of the associated CloudFront distribution, such as ``da1b2c3d4e5.cloudfront.net`` .

            .. epigraph::

               The name of the record that you're creating must match a custom domain name for your API, such as ``api.example.com`` .

            - **Amazon Virtual Private Cloud interface VPC endpoint** - Enter the API endpoint for the interface endpoint, such as ``vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com`` . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of ``DnsName`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ .
            - **CloudFront distribution** - Specify the domain name that CloudFront assigned when you created your distribution.

            Your CloudFront distribution must include an alternate domain name that matches the name of the record. For example, if the name of the record is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`_ in the *Amazon CloudFront Developer Guide* .

            You can't create a record in a private hosted zone to route traffic to a CloudFront distribution.
            .. epigraph::

               For failover alias records, you can't specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can't include the same alternate domain name in more than one distribution.

            - **Elastic Beanstalk environment** - If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name ``my-environment. *us-west-2* .elasticbeanstalk.com`` is a regionalized domain name.

            .. epigraph::

               For environments that were created before early 2016, the domain name doesn't include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can't create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can't create a record that routes traffic for example.com to your Elastic Beanstalk environment.

            For Elastic Beanstalk environments that have regionalized subdomains, specify the ``CNAME`` attribute for the environment. You can use the following methods to get the value of the CNAME attribute:

            - *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .
            - *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`_ in the *AWS Elastic Beanstalk API Reference* .
            - *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`_ in the *AWS CLI* .
            - **ELB load balancer** - Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console , the ELB API, or the AWS CLI .
            - *AWS Management Console* : Go to the EC2 page, choose *Load Balancers* in the navigation pane, choose the load balancer, choose the *Description* tab, and get the value of the *DNS name* field.

            If you're routing traffic to a Classic Load Balancer, get the value that begins with *dualstack* . If you're routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA.

            - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide:
            - Classic Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_
            - Application and Network Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_
            - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the value of ``DNSName`` :
            - `Classic Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ .
            - `Application and Network Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ .
            - *AWS CLI* : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide:
            - Classic Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_
            - Application and Network Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_
            - **Global Accelerator accelerator** - Specify the DNS name for your accelerator:
            - *Global Accelerator API* : To get the DNS name, use `DescribeAccelerator <https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html>`_ .
            - *AWS CLI* : To get the DNS name, use `describe-accelerator <https://docs.aws.amazon.com/cli/latest/reference/globalaccelerator/describe-accelerator.html>`_ .
            - **Amazon S3 bucket that is configured as a static website** - Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, ``s3-website.us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`_ in the *Amazon Route 53 Developer Guide.*
            - **Another Route 53 record** - Specify the value of the ``Name`` element for a record in the current hosted zone.

            .. epigraph::

               If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't specify the domain name for a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record that you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-aliastarget.html#cfn-route53-recordset-aliastarget-dnsname
            '''
            result = self._values.get("dns_name")
            assert result is not None, "Required property 'dns_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hosted_zone_id(self) -> builtins.str:
            '''*Alias resource records sets only* : The value used depends on where you want to route traffic:.

            - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ :
            - For regional APIs, specify the value of ``regionalHostedZoneId`` .
            - For edge-optimized APIs, specify the value of ``distributionHostedZoneId`` .
            - **Amazon Virtual Private Cloud interface VPC endpoint** - Specify the hosted zone ID for your interface endpoint. You can get the value of ``HostedZoneId`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ .
            - **CloudFront distribution** - Specify ``Z2FDTNDATAQYW2`` . This is always the hosted zone ID when you create an alias record that routes traffic to a CloudFront distribution.

            .. epigraph::

               Alias records for CloudFront can't be created in a private zone.

            - **Elastic Beanstalk environment** - Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html>`_ in the *Amazon Web Services General Reference* .
            - **ELB load balancer** - Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:
            - `Service Endpoints <https://docs.aws.amazon.com/general/latest/gr/elb.html>`_ table in the "Elastic Load Balancing Endpoints and Quotas" topic in the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers.
            - *AWS Management Console* : Go to the Amazon EC2 page, choose *Load Balancers* in the navigation pane, select the load balancer, and get the value of the *Hosted zone* field on the *Description* tab.
            - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide:
            - Classic Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` .
            - Application and Network Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneID`` .
            - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the applicable value:
            - Classic Load Balancers: Get `CanonicalHostedZoneNameID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ .
            - Application and Network Load Balancers: Get `CanonicalHostedZoneID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ .
            - *AWS CLI* : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide:
            - Classic Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` .
            - Application and Network Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneID`` .
            - **Global Accelerator accelerator** - Specify ``Z2BJ6XQ5FK7U4H`` .
            - **An Amazon S3 bucket configured as a static website** - Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* .
            - **Another Route 53 record in your hosted zone** - Specify the hosted zone ID of your hosted zone. (An alias record can't reference a record in a different hosted zone.)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-aliastarget.html#cfn-route53-recordset-aliastarget-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            assert result is not None, "Required property 'hosted_zone_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def evaluate_target_health(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*Applies only to alias, failover alias, geolocation alias, latency alias, and weighted alias resource record sets:* When ``EvaluateTargetHealth`` is ``true`` , an alias resource record set inherits the health of the referenced AWS resource, such as an ELB load balancer or another resource record set in the hosted zone.

            Note the following:

            - **CloudFront distributions** - You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution.
            - **Elastic Beanstalk environments that have regionalized subdomains** - If you specify an Elastic Beanstalk environment in ``DNSName`` and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any.

            If the environment contains a single Amazon EC2 instance, there are no special requirements.

            - **ELB load balancers** - Health checking behavior depends on the type of load balancer:
            - *Classic Load Balancers* : If you specify an ELB Classic Load Balancer in ``DNSName`` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources.
            - *Application and Network Load Balancers* : If you specify an ELB Application or Network Load Balancer and you set ``EvaluateTargetHealth`` to ``true`` , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer:
            - For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources.
            - A target group that has no registered targets is considered unhealthy.

            .. epigraph::

               When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer.

            - **S3 buckets** - There are no special requirements for setting ``EvaluateTargetHealth`` to ``true`` when the alias target is an S3 bucket.
            - **Other records in the same hosted zone** - If the AWS resource that you specify in ``DNSName`` is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see `What Happens When You Omit Health Checks? <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`_ in the *Amazon Route 53 Developer Guide* .

            For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-aliastarget.html#cfn-route53-recordset-aliastarget-evaluatetargethealth
            '''
            result = self._values.get("evaluate_target_health")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AliasTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSet.CidrRoutingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "collection_id": "collectionId",
            "location_name": "locationName",
        },
    )
    class CidrRoutingConfigProperty:
        def __init__(
            self,
            *,
            collection_id: builtins.str,
            location_name: builtins.str,
        ) -> None:
            '''The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

            A ``LocationName`` with an asterisk “*” can be used to create a default CIDR record. ``CollectionId`` is still required for default record.

            :param collection_id: The CIDR collection ID.
            :param location_name: The CIDR collection location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-cidrroutingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                cidr_routing_config_property = route53.CfnRecordSet.CidrRoutingConfigProperty(
                    collection_id="collectionId",
                    location_name="locationName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cc6569566583d30a42a983532b11cef6d6313d0666f46f50d599eabd1e5d4837)
                check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
                check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "collection_id": collection_id,
                "location_name": location_name,
            }

        @builtins.property
        def collection_id(self) -> builtins.str:
            '''The CIDR collection ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-cidrroutingconfig.html#cfn-route53-recordset-cidrroutingconfig-collectionid
            '''
            result = self._values.get("collection_id")
            assert result is not None, "Required property 'collection_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def location_name(self) -> builtins.str:
            '''The CIDR collection location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-cidrroutingconfig.html#cfn-route53-recordset-cidrroutingconfig-locationname
            '''
            result = self._values.get("location_name")
            assert result is not None, "Required property 'location_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CidrRoutingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSet.CoordinatesProperty",
        jsii_struct_bases=[],
        name_mapping={"latitude": "latitude", "longitude": "longitude"},
    )
    class CoordinatesProperty:
        def __init__(self, *, latitude: builtins.str, longitude: builtins.str) -> None:
            '''A complex type that lists the coordinates for a geoproximity resource record.

            :param latitude: Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).
            :param longitude: Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-coordinates.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                coordinates_property = route53.CfnRecordSet.CoordinatesProperty(
                    latitude="latitude",
                    longitude="longitude"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__29683fc8d824969c71955a00cda4d10dde445180eb16e6a17c990ec1252a893a)
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "latitude": latitude,
                "longitude": longitude,
            }

        @builtins.property
        def latitude(self) -> builtins.str:
            '''Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-coordinates.html#cfn-route53-recordset-coordinates-latitude
            '''
            result = self._values.get("latitude")
            assert result is not None, "Required property 'latitude' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def longitude(self) -> builtins.str:
            '''Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-coordinates.html#cfn-route53-recordset-coordinates-longitude
            '''
            result = self._values.get("longitude")
            assert result is not None, "Required property 'longitude' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoordinatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSet.GeoLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "continent_code": "continentCode",
            "country_code": "countryCode",
            "subdivision_code": "subdivisionCode",
        },
    )
    class GeoLocationProperty:
        def __init__(
            self,
            *,
            continent_code: typing.Optional[builtins.str] = None,
            country_code: typing.Optional[builtins.str] = None,
            subdivision_code: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A complex type that contains information about a geographic location.

            :param continent_code: For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Route 53 supports the following continent codes:. - *AF* : Africa - *AN* : Antarctica - *AS* : Asia - *EU* : Europe - *OC* : Oceania - *NA* : North America - *SA* : South America Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.
            :param country_code: For geolocation resource record sets, the two-letter code for a country. Route 53 uses the two-letter country codes that are specified in `ISO standard 3166-1 alpha-2 <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .
            :param subdivision_code: For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn't support any other values for ``SubdivisionCode`` . For a list of state abbreviations, see `Appendix B: Two–Letter State and Possession Abbreviations <https://docs.aws.amazon.com/https://pe.usps.com/text/pub28/28apb.htm>`_ on the United States Postal Service website. If you specify ``subdivisioncode`` , you must also specify ``US`` for ``CountryCode`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                geo_location_property = route53.CfnRecordSet.GeoLocationProperty(
                    continent_code="continentCode",
                    country_code="countryCode",
                    subdivision_code="subdivisionCode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc6e59779782a9e8ecceda7a67dfa9c21d257bdac8db0558def7239dd1d167a5)
                check_type(argname="argument continent_code", value=continent_code, expected_type=type_hints["continent_code"])
                check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
                check_type(argname="argument subdivision_code", value=subdivision_code, expected_type=type_hints["subdivision_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if continent_code is not None:
                self._values["continent_code"] = continent_code
            if country_code is not None:
                self._values["country_code"] = country_code
            if subdivision_code is not None:
                self._values["subdivision_code"] = subdivision_code

        @builtins.property
        def continent_code(self) -> typing.Optional[builtins.str]:
            '''For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Route 53 supports the following continent codes:.

            - *AF* : Africa
            - *AN* : Antarctica
            - *AS* : Asia
            - *EU* : Europe
            - *OC* : Oceania
            - *NA* : North America
            - *SA* : South America

            Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-continentcode
            '''
            result = self._values.get("continent_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country_code(self) -> typing.Optional[builtins.str]:
            '''For geolocation resource record sets, the two-letter code for a country.

            Route 53 uses the two-letter country codes that are specified in `ISO standard 3166-1 alpha-2 <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-countrycode
            '''
            result = self._values.get("country_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subdivision_code(self) -> typing.Optional[builtins.str]:
            '''For geolocation resource record sets, the two-letter code for a state of the United States.

            Route 53 doesn't support any other values for ``SubdivisionCode`` . For a list of state abbreviations, see `Appendix B: Two–Letter State and Possession Abbreviations <https://docs.aws.amazon.com/https://pe.usps.com/text/pub28/28apb.htm>`_ on the United States Postal Service website.

            If you specify ``subdivisioncode`` , you must also specify ``US`` for ``CountryCode`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geolocation.html#cfn-route53-recordset-geolocation-subdivisioncode
            '''
            result = self._values.get("subdivision_code")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSet.GeoProximityLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "bias": "bias",
            "coordinates": "coordinates",
            "local_zone_group": "localZoneGroup",
        },
    )
    class GeoProximityLocationProperty:
        def __init__(
            self,
            *,
            aws_region: typing.Optional[builtins.str] = None,
            bias: typing.Optional[jsii.Number] = None,
            coordinates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSet.CoordinatesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            local_zone_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''(Resource record sets only): A complex type that lets you specify where your resources are located.

            Only one of ``LocalZoneGroup`` , ``Coordinates`` , or ``AWS Region`` is allowed per request at a time.

            For more information about geoproximity routing, see `Geoproximity routing <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html>`_ in the *Amazon Route 53 Developer Guide* .

            :param aws_region: The AWS Region the resource you are directing DNS traffic to, is in.
            :param bias: The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource. To use ``Bias`` to change the size of the geographic region, specify the applicable value for the bias: - To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions. - To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.
            :param coordinates: Contains the longitude and latitude for a geographic region.
            :param local_zone_group: Specifies an AWS Local Zone Group. A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is ``us-east-1-bue-1a`` the Local Zone Group is ``us-east-1-bue-1`` . You can identify the Local Zones Group for a specific Local Zone by using the `describe-availability-zones <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html>`_ CLI command: This command returns: ``"GroupName": "us-west-2-den-1"`` , specifying that the Local Zone ``us-west-2-den-1a`` belongs to the Local Zone Group ``us-west-2-den-1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geoproximitylocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                geo_proximity_location_property = route53.CfnRecordSet.GeoProximityLocationProperty(
                    aws_region="awsRegion",
                    bias=123,
                    coordinates=route53.CfnRecordSet.CoordinatesProperty(
                        latitude="latitude",
                        longitude="longitude"
                    ),
                    local_zone_group="localZoneGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9bbef31bd9d19fea78e067206e8cea17ada33bda9853588d7a99d66d91f15555)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument bias", value=bias, expected_type=type_hints["bias"])
                check_type(argname="argument coordinates", value=coordinates, expected_type=type_hints["coordinates"])
                check_type(argname="argument local_zone_group", value=local_zone_group, expected_type=type_hints["local_zone_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if bias is not None:
                self._values["bias"] = bias
            if coordinates is not None:
                self._values["coordinates"] = coordinates
            if local_zone_group is not None:
                self._values["local_zone_group"] = local_zone_group

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region the resource you are directing DNS traffic to, is in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geoproximitylocation.html#cfn-route53-recordset-geoproximitylocation-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bias(self) -> typing.Optional[jsii.Number]:
            '''The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource.

            To use ``Bias`` to change the size of the geographic region, specify the applicable value for the bias:

            - To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions.
            - To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geoproximitylocation.html#cfn-route53-recordset-geoproximitylocation-bias
            '''
            result = self._values.get("bias")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def coordinates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.CoordinatesProperty"]]:
            '''Contains the longitude and latitude for a geographic region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geoproximitylocation.html#cfn-route53-recordset-geoproximitylocation-coordinates
            '''
            result = self._values.get("coordinates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSet.CoordinatesProperty"]], result)

        @builtins.property
        def local_zone_group(self) -> typing.Optional[builtins.str]:
            '''Specifies an AWS Local Zone Group.

            A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is ``us-east-1-bue-1a`` the Local Zone Group is ``us-east-1-bue-1`` .

            You can identify the Local Zones Group for a specific Local Zone by using the `describe-availability-zones <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html>`_ CLI command:

            This command returns: ``"GroupName": "us-west-2-den-1"`` , specifying that the Local Zone ``us-west-2-den-1a`` belongs to the Local Zone Group ``us-west-2-den-1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordset-geoproximitylocation.html#cfn-route53-recordset-geoproximitylocation-localzonegroup
            '''
            result = self._values.get("local_zone_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoProximityLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnRecordSetGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup",
):
    '''A complex type that contains an optional comment, the name and ID of the hosted zone that you want to make changes in, and values for the records that you want to create.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
    :cloudformationResource: AWS::Route53::RecordSetGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_route53 as route53
        
        cfn_record_set_group = route53.CfnRecordSetGroup(self, "MyCfnRecordSetGroup",
            comment="comment",
            hosted_zone_id="hostedZoneId",
            hosted_zone_name="hostedZoneName",
            record_sets=[route53.CfnRecordSetGroup.RecordSetProperty(
                name="name",
                type="type",
        
                # the properties below are optional
                alias_target=route53.CfnRecordSetGroup.AliasTargetProperty(
                    dns_name="dnsName",
                    hosted_zone_id="hostedZoneId",
        
                    # the properties below are optional
                    evaluate_target_health=False
                ),
                cidr_routing_config=route53.CfnRecordSetGroup.CidrRoutingConfigProperty(
                    collection_id="collectionId",
                    location_name="locationName"
                ),
                failover="failover",
                geo_location=route53.CfnRecordSetGroup.GeoLocationProperty(
                    continent_code="continentCode",
                    country_code="countryCode",
                    subdivision_code="subdivisionCode"
                ),
                geo_proximity_location=route53.CfnRecordSetGroup.GeoProximityLocationProperty(
                    aws_region="awsRegion",
                    bias=123,
                    coordinates=route53.CfnRecordSetGroup.CoordinatesProperty(
                        latitude="latitude",
                        longitude="longitude"
                    ),
                    local_zone_group="localZoneGroup"
                ),
                health_check_id="healthCheckId",
                hosted_zone_id="hostedZoneId",
                hosted_zone_name="hostedZoneName",
                multi_value_answer=False,
                region="region",
                resource_records=["resourceRecords"],
                set_identifier="setIdentifier",
                ttl="ttl",
                weight=123
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        comment: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        record_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSetGroup.RecordSetProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param comment: *Optional:* Any comments you want to include about a change batch request.
        :param hosted_zone_id: The ID of the hosted zone that you want to create records in. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param hosted_zone_name: The name of the hosted zone that you want to create records in. You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` . When you create a stack using an ``AWS::Route53::RecordSet`` that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the ``HostedZoneName`` . If AWS CloudFormation can't find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param record_sets: A complex type that contains one ``RecordSet`` element for each record that you want to create.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__88410dc2301961a44d6910ee0de13aa8273ce0fa1b93daca4141c18b5fa3d03b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnRecordSetGroupProps(
            comment=comment,
            hosted_zone_id=hosted_zone_id,
            hosted_zone_name=hosted_zone_name,
            record_sets=record_sets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48ca705812043ff12ec21cb444124f3be1a7ab3431425e66de023724f6a298c6)
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
            type_hints = typing.get_type_hints(_typecheckingstub__14a869585b3959be67c777f304411c15da58891cbbb6c3ffb41dcdf3dade3c2d)
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
        '''Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="comment")
    def comment(self) -> typing.Optional[builtins.str]:
        '''*Optional:* Any comments you want to include about a change batch request.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "comment"))

    @comment.setter
    def comment(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c97ac966771356be453e30c879df180c0ddc8815675496dd0165606bedf4c9e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "comment", value)

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the hosted zone that you want to create records in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostedZoneId"))

    @hosted_zone_id.setter
    def hosted_zone_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1424150c5729da24929b30da713b6d33d1015579282157aecedd97e989f6938f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneId", value)

    @builtins.property
    @jsii.member(jsii_name="hostedZoneName")
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''The name of the hosted zone that you want to create records in.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "hostedZoneName"))

    @hosted_zone_name.setter
    def hosted_zone_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9f9f2119ab4a72afe07344595f0bb4fb1b9015e2e273b9dea6abcfbafa762ed4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "hostedZoneName", value)

    @builtins.property
    @jsii.member(jsii_name="recordSets")
    def record_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.RecordSetProperty"]]]]:
        '''A complex type that contains one ``RecordSet`` element for each record that you want to create.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.RecordSetProperty"]]]], jsii.get(self, "recordSets"))

    @record_sets.setter
    def record_sets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.RecordSetProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9fb00744f239be86927ab07333f9aa97d44af1dbaabd6b50dc186a5a6f344824)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "recordSets", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup.AliasTargetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dns_name": "dnsName",
            "hosted_zone_id": "hostedZoneId",
            "evaluate_target_health": "evaluateTargetHealth",
        },
    )
    class AliasTargetProperty:
        def __init__(
            self,
            *,
            dns_name: builtins.str,
            hosted_zone_id: builtins.str,
            evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''*Alias records only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.

            When creating records for a private hosted zone, note the following:

            - Creating geolocation alias and latency alias records in a private hosted zone is allowed but not supported.
            - For information about creating failover records in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ .

            :param dns_name: *Alias records only:* The value that you specify depends on where you want to route queries:. - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the applicable domain name for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ : - For regional APIs, specify the value of ``regionalDomainName`` . - For edge-optimized APIs, specify the value of ``distributionDomainName`` . This is the name of the associated CloudFront distribution, such as ``da1b2c3d4e5.cloudfront.net`` . .. epigraph:: The name of the record that you're creating must match a custom domain name for your API, such as ``api.example.com`` . - **Amazon Virtual Private Cloud interface VPC endpoint** - Enter the API endpoint for the interface endpoint, such as ``vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com`` . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of ``DnsName`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ . - **CloudFront distribution** - Specify the domain name that CloudFront assigned when you created your distribution. Your CloudFront distribution must include an alternate domain name that matches the name of the record. For example, if the name of the record is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`_ in the *Amazon CloudFront Developer Guide* . You can't create a record in a private hosted zone to route traffic to a CloudFront distribution. .. epigraph:: For failover alias records, you can't specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can't include the same alternate domain name in more than one distribution. - **Elastic Beanstalk environment** - If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name ``my-environment. *us-west-2* .elasticbeanstalk.com`` is a regionalized domain name. .. epigraph:: For environments that were created before early 2016, the domain name doesn't include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can't create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can't create a record that routes traffic for example.com to your Elastic Beanstalk environment. For Elastic Beanstalk environments that have regionalized subdomains, specify the ``CNAME`` attribute for the environment. You can use the following methods to get the value of the CNAME attribute: - *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`_ in the *AWS Elastic Beanstalk Developer Guide* . - *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`_ in the *AWS Elastic Beanstalk API Reference* . - *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`_ in the *AWS CLI* . - **ELB load balancer** - Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console , the ELB API, or the AWS CLI . - *AWS Management Console* : Go to the EC2 page, choose *Load Balancers* in the navigation pane, choose the load balancer, choose the *Description* tab, and get the value of the *DNS name* field. If you're routing traffic to a Classic Load Balancer, get the value that begins with *dualstack* . If you're routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA. - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: - Classic Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_ - Application and Network Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the value of ``DNSName`` : - `Classic Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ . - `Application and Network Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ . - *AWS CLI* : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide: - Classic Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_ - Application and Network Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_ - **Global Accelerator accelerator** - Specify the DNS name for your accelerator: - *Global Accelerator API* : To get the DNS name, use `DescribeAccelerator <https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html>`_ . - *AWS CLI* : To get the DNS name, use `describe-accelerator <https://docs.aws.amazon.com/cli/latest/reference/globalaccelerator/describe-accelerator.html>`_ . - **Amazon S3 bucket that is configured as a static website** - Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, ``s3-website.us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`_ in the *Amazon Route 53 Developer Guide.* - **Another Route 53 record** - Specify the value of the ``Name`` element for a record in the current hosted zone. .. epigraph:: If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't specify the domain name for a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record that you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.
            :param hosted_zone_id: *Alias resource records sets only* : The value used depends on where you want to route traffic:. - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ : - For regional APIs, specify the value of ``regionalHostedZoneId`` . - For edge-optimized APIs, specify the value of ``distributionHostedZoneId`` . - **Amazon Virtual Private Cloud interface VPC endpoint** - Specify the hosted zone ID for your interface endpoint. You can get the value of ``HostedZoneId`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ . - **CloudFront distribution** - Specify ``Z2FDTNDATAQYW2`` . This is always the hosted zone ID when you create an alias record that routes traffic to a CloudFront distribution. .. epigraph:: Alias records for CloudFront can't be created in a private zone. - **Elastic Beanstalk environment** - Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html>`_ in the *Amazon Web Services General Reference* . - **ELB load balancer** - Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID: - `Service Endpoints <https://docs.aws.amazon.com/general/latest/gr/elb.html>`_ table in the "Elastic Load Balancing endpoints and quotas" topic in the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers. - *AWS Management Console* : Go to the Amazon EC2 page, choose *Load Balancers* in the navigation pane, select the load balancer, and get the value of the *Hosted zone* field on the *Description* tab. - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide: - Classic Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` . - Application and Network Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneID`` . - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the applicable value: - Classic Load Balancers: Get `CanonicalHostedZoneNameID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ . - Application and Network Load Balancers: Get `CanonicalHostedZoneID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ . - *AWS CLI* : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide: - Classic Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` . - Application and Network Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneID`` . - **Global Accelerator accelerator** - Specify ``Z2BJ6XQ5FK7U4H`` . - **An Amazon S3 bucket configured as a static website** - Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* . - **Another Route 53 record in your hosted zone** - Specify the hosted zone ID of your hosted zone. (An alias record can't reference a record in a different hosted zone.)
            :param evaluate_target_health: *Applies only to alias records with any routing policy:* When ``EvaluateTargetHealth`` is ``true`` , an alias record inherits the health of the referenced AWS resource, such as an ELB load balancer or another record in the hosted zone. Note the following: - **CloudFront distributions** - You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution. - **Elastic Beanstalk environments that have regionalized subdomains** - If you specify an Elastic Beanstalk environment in ``DNSName`` and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any. If the environment contains a single Amazon EC2 instance, there are no special requirements. - **ELB load balancers** - Health checking behavior depends on the type of load balancer: - *Classic Load Balancers* : If you specify an ELB Classic Load Balancer in ``DNSName`` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources. - *Application and Network Load Balancers* : If you specify an ELB Application or Network Load Balancer and you set ``EvaluateTargetHealth`` to ``true`` , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer: - For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources. - A target group that has no registered targets is considered unhealthy. .. epigraph:: When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer. - **S3 buckets** - There are no special requirements for setting ``EvaluateTargetHealth`` to ``true`` when the alias target is an S3 bucket. - **Other records in the same hosted zone** - If the AWS resource that you specify in ``DNSName`` is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see `What Happens When You Omit Health Checks? <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`_ in the *Amazon Route 53 Developer Guide* . For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-aliastarget.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                alias_target_property = route53.CfnRecordSetGroup.AliasTargetProperty(
                    dns_name="dnsName",
                    hosted_zone_id="hostedZoneId",
                
                    # the properties below are optional
                    evaluate_target_health=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__47266159f3c04590ed7485f833b949a10c311800ebfa01351a5f55ffc0c4fcfe)
                check_type(argname="argument dns_name", value=dns_name, expected_type=type_hints["dns_name"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument evaluate_target_health", value=evaluate_target_health, expected_type=type_hints["evaluate_target_health"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "dns_name": dns_name,
                "hosted_zone_id": hosted_zone_id,
            }
            if evaluate_target_health is not None:
                self._values["evaluate_target_health"] = evaluate_target_health

        @builtins.property
        def dns_name(self) -> builtins.str:
            '''*Alias records only:* The value that you specify depends on where you want to route queries:.

            - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the applicable domain name for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ :
            - For regional APIs, specify the value of ``regionalDomainName`` .
            - For edge-optimized APIs, specify the value of ``distributionDomainName`` . This is the name of the associated CloudFront distribution, such as ``da1b2c3d4e5.cloudfront.net`` .

            .. epigraph::

               The name of the record that you're creating must match a custom domain name for your API, such as ``api.example.com`` .

            - **Amazon Virtual Private Cloud interface VPC endpoint** - Enter the API endpoint for the interface endpoint, such as ``vpce-123456789abcdef01-example-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com`` . For edge-optimized APIs, this is the domain name for the corresponding CloudFront distribution. You can get the value of ``DnsName`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ .
            - **CloudFront distribution** - Specify the domain name that CloudFront assigned when you created your distribution.

            Your CloudFront distribution must include an alternate domain name that matches the name of the record. For example, if the name of the record is *acme.example.com* , your CloudFront distribution must include *acme.example.com* as one of the alternate domain names. For more information, see `Using Alternate Domain Names (CNAMEs) <https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html>`_ in the *Amazon CloudFront Developer Guide* .

            You can't create a record in a private hosted zone to route traffic to a CloudFront distribution.
            .. epigraph::

               For failover alias records, you can't specify a CloudFront distribution for both the primary and secondary records. A distribution must include an alternate domain name that matches the name of the record. However, the primary and secondary records have the same name, and you can't include the same alternate domain name in more than one distribution.

            - **Elastic Beanstalk environment** - If the domain name for your Elastic Beanstalk environment includes the region that you deployed the environment in, you can create an alias record that routes traffic to the environment. For example, the domain name ``my-environment. *us-west-2* .elasticbeanstalk.com`` is a regionalized domain name.

            .. epigraph::

               For environments that were created before early 2016, the domain name doesn't include the region. To route traffic to these environments, you must create a CNAME record instead of an alias record. Note that you can't create a CNAME record for the root domain name. For example, if your domain name is example.com, you can create a record that routes traffic for acme.example.com to your Elastic Beanstalk environment, but you can't create a record that routes traffic for example.com to your Elastic Beanstalk environment.

            For Elastic Beanstalk environments that have regionalized subdomains, specify the ``CNAME`` attribute for the environment. You can use the following methods to get the value of the CNAME attribute:

            - *AWS Management Console* : For information about how to get the value by using the console, see `Using Custom Domains with AWS Elastic Beanstalk <https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/customdomains.html>`_ in the *AWS Elastic Beanstalk Developer Guide* .
            - *Elastic Beanstalk API* : Use the ``DescribeEnvironments`` action to get the value of the ``CNAME`` attribute. For more information, see `DescribeEnvironments <https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_DescribeEnvironments.html>`_ in the *AWS Elastic Beanstalk API Reference* .
            - *AWS CLI* : Use the ``describe-environments`` command to get the value of the ``CNAME`` attribute. For more information, see `describe-environments <https://docs.aws.amazon.com/cli/latest/reference/elasticbeanstalk/describe-environments.html>`_ in the *AWS CLI* .
            - **ELB load balancer** - Specify the DNS name that is associated with the load balancer. Get the DNS name by using the AWS Management Console , the ELB API, or the AWS CLI .
            - *AWS Management Console* : Go to the EC2 page, choose *Load Balancers* in the navigation pane, choose the load balancer, choose the *Description* tab, and get the value of the *DNS name* field.

            If you're routing traffic to a Classic Load Balancer, get the value that begins with *dualstack* . If you're routing traffic to another type of load balancer, get the value that applies to the record type, A or AAAA.

            - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the value of ``DNSName`` . For more information, see the applicable guide:
            - Classic Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_
            - Application and Network Load Balancers: `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_
            - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the value of ``DNSName`` :
            - `Classic Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ .
            - `Application and Network Load Balancers <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ .
            - *AWS CLI* : Use ``describe-load-balancers`` to get the value of ``DNSName`` . For more information, see the applicable guide:
            - Classic Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_
            - Application and Network Load Balancers: `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_
            - **Global Accelerator accelerator** - Specify the DNS name for your accelerator:
            - *Global Accelerator API* : To get the DNS name, use `DescribeAccelerator <https://docs.aws.amazon.com/global-accelerator/latest/api/API_DescribeAccelerator.html>`_ .
            - *AWS CLI* : To get the DNS name, use `describe-accelerator <https://docs.aws.amazon.com/cli/latest/reference/globalaccelerator/describe-accelerator.html>`_ .
            - **Amazon S3 bucket that is configured as a static website** - Specify the domain name of the Amazon S3 website endpoint that you created the bucket in, for example, ``s3-website.us-east-2.amazonaws.com`` . For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* . For more information about using S3 buckets for websites, see `Getting Started with Amazon Route 53 <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/getting-started.html>`_ in the *Amazon Route 53 Developer Guide.*
            - **Another Route 53 record** - Specify the value of the ``Name`` element for a record in the current hosted zone.

            .. epigraph::

               If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't specify the domain name for a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record that you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-aliastarget.html#cfn-route53-recordsetgroup-aliastarget-dnsname
            '''
            result = self._values.get("dns_name")
            assert result is not None, "Required property 'dns_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def hosted_zone_id(self) -> builtins.str:
            '''*Alias resource records sets only* : The value used depends on where you want to route traffic:.

            - **Amazon API Gateway custom regional APIs and edge-optimized APIs** - Specify the hosted zone ID for your API. You can get the applicable value using the AWS CLI command `get-domain-names <https://docs.aws.amazon.com/cli/latest/reference/apigateway/get-domain-names.html>`_ :
            - For regional APIs, specify the value of ``regionalHostedZoneId`` .
            - For edge-optimized APIs, specify the value of ``distributionHostedZoneId`` .
            - **Amazon Virtual Private Cloud interface VPC endpoint** - Specify the hosted zone ID for your interface endpoint. You can get the value of ``HostedZoneId`` using the AWS CLI command `describe-vpc-endpoints <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoints.html>`_ .
            - **CloudFront distribution** - Specify ``Z2FDTNDATAQYW2`` . This is always the hosted zone ID when you create an alias record that routes traffic to a CloudFront distribution.

            .. epigraph::

               Alias records for CloudFront can't be created in a private zone.

            - **Elastic Beanstalk environment** - Specify the hosted zone ID for the region that you created the environment in. The environment must have a regionalized subdomain. For a list of regions and the corresponding hosted zone IDs, see `AWS Elastic Beanstalk endpoints and quotas <https://docs.aws.amazon.com/general/latest/gr/elasticbeanstalk.html>`_ in the *Amazon Web Services General Reference* .
            - **ELB load balancer** - Specify the value of the hosted zone ID for the load balancer. Use the following methods to get the hosted zone ID:
            - `Service Endpoints <https://docs.aws.amazon.com/general/latest/gr/elb.html>`_ table in the "Elastic Load Balancing endpoints and quotas" topic in the *Amazon Web Services General Reference* : Use the value that corresponds with the region that you created your load balancer in. Note that there are separate columns for Application and Classic Load Balancers and for Network Load Balancers.
            - *AWS Management Console* : Go to the Amazon EC2 page, choose *Load Balancers* in the navigation pane, select the load balancer, and get the value of the *Hosted zone* field on the *Description* tab.
            - *Elastic Load Balancing API* : Use ``DescribeLoadBalancers`` to get the applicable value. For more information, see the applicable guide:
            - Classic Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` .
            - Application and Network Load Balancers: Use `DescribeLoadBalancers <https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html>`_ to get the value of ``CanonicalHostedZoneID`` .
            - *CloudFormation Fn::GetAtt intrinsic function* : Use the `Fn::GetAtt <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html>`_ intrinsic function to get the applicable value:
            - Classic Load Balancers: Get `CanonicalHostedZoneNameID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-elb.html#aws-properties-ec2-elb-return-values>`_ .
            - Application and Network Load Balancers: Get `CanonicalHostedZoneID <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-elasticloadbalancingv2-loadbalancer.html#aws-resource-elasticloadbalancingv2-loadbalancer-return-values>`_ .
            - *AWS CLI* : Use ``describe-load-balancers`` to get the applicable value. For more information, see the applicable guide:
            - Classic Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneNameID`` .
            - Application and Network Load Balancers: Use `describe-load-balancers <https://docs.aws.amazon.com/cli/latest/reference/elbv2/describe-load-balancers.html>`_ to get the value of ``CanonicalHostedZoneID`` .
            - **Global Accelerator accelerator** - Specify ``Z2BJ6XQ5FK7U4H`` .
            - **An Amazon S3 bucket configured as a static website** - Specify the hosted zone ID for the region that you created the bucket in. For more information about valid values, see the table `Amazon S3 Website Endpoints <https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_website_region_endpoints>`_ in the *Amazon Web Services General Reference* .
            - **Another Route 53 record in your hosted zone** - Specify the hosted zone ID of your hosted zone. (An alias record can't reference a record in a different hosted zone.)

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-aliastarget.html#cfn-route53-recordsetgroup-aliastarget-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            assert result is not None, "Required property 'hosted_zone_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def evaluate_target_health(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*Applies only to alias records with any routing policy:* When ``EvaluateTargetHealth`` is ``true`` , an alias record inherits the health of the referenced AWS resource, such as an ELB load balancer or another record in the hosted zone.

            Note the following:

            - **CloudFront distributions** - You can't set ``EvaluateTargetHealth`` to ``true`` when the alias target is a CloudFront distribution.
            - **Elastic Beanstalk environments that have regionalized subdomains** - If you specify an Elastic Beanstalk environment in ``DNSName`` and the environment contains an ELB load balancer, Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. (An environment automatically contains an ELB load balancer if it includes more than one Amazon EC2 instance.) If you set ``EvaluateTargetHealth`` to ``true`` and either no Amazon EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other available resources that are healthy, if any.

            If the environment contains a single Amazon EC2 instance, there are no special requirements.

            - **ELB load balancers** - Health checking behavior depends on the type of load balancer:
            - *Classic Load Balancers* : If you specify an ELB Classic Load Balancer in ``DNSName`` , Elastic Load Balancing routes queries only to the healthy Amazon EC2 instances that are registered with the load balancer. If you set ``EvaluateTargetHealth`` to ``true`` and either no EC2 instances are healthy or the load balancer itself is unhealthy, Route 53 routes queries to other resources.
            - *Application and Network Load Balancers* : If you specify an ELB Application or Network Load Balancer and you set ``EvaluateTargetHealth`` to ``true`` , Route 53 routes queries to the load balancer based on the health of the target groups that are associated with the load balancer:
            - For an Application or Network Load Balancer to be considered healthy, every target group that contains targets must contain at least one healthy target. If any target group contains only unhealthy targets, the load balancer is considered unhealthy, and Route 53 routes queries to other resources.
            - A target group that has no registered targets is considered unhealthy.

            .. epigraph::

               When you create a load balancer, you configure settings for Elastic Load Balancing health checks; they're not Route 53 health checks, but they perform a similar function. Do not create Route 53 health checks for the EC2 instances that you register with an ELB load balancer.

            - **S3 buckets** - There are no special requirements for setting ``EvaluateTargetHealth`` to ``true`` when the alias target is an S3 bucket.
            - **Other records in the same hosted zone** - If the AWS resource that you specify in ``DNSName`` is a record or a group of records (for example, a group of weighted records) but is not another alias record, we recommend that you associate a health check with all of the records in the alias target. For more information, see `What Happens When You Omit Health Checks? <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-complex-configs.html#dns-failover-complex-configs-hc-omitting>`_ in the *Amazon Route 53 Developer Guide* .

            For more information and examples, see `Amazon Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-aliastarget.html#cfn-route53-recordsetgroup-aliastarget-evaluatetargethealth
            '''
            result = self._values.get("evaluate_target_health")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AliasTargetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup.CidrRoutingConfigProperty",
        jsii_struct_bases=[],
        name_mapping={
            "collection_id": "collectionId",
            "location_name": "locationName",
        },
    )
    class CidrRoutingConfigProperty:
        def __init__(
            self,
            *,
            collection_id: builtins.str,
            location_name: builtins.str,
        ) -> None:
            '''The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

            A ``LocationName`` with an asterisk “*” can be used to create a default CIDR record. ``CollectionId`` is still required for default record.

            :param collection_id: The CIDR collection ID.
            :param location_name: The CIDR collection location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-cidrroutingconfig.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                cidr_routing_config_property = route53.CfnRecordSetGroup.CidrRoutingConfigProperty(
                    collection_id="collectionId",
                    location_name="locationName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c25a6f79ee876d62204e1e24470518bddae21e675bc5258cc7766c8a345ae1a2)
                check_type(argname="argument collection_id", value=collection_id, expected_type=type_hints["collection_id"])
                check_type(argname="argument location_name", value=location_name, expected_type=type_hints["location_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "collection_id": collection_id,
                "location_name": location_name,
            }

        @builtins.property
        def collection_id(self) -> builtins.str:
            '''The CIDR collection ID.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-cidrroutingconfig.html#cfn-route53-recordsetgroup-cidrroutingconfig-collectionid
            '''
            result = self._values.get("collection_id")
            assert result is not None, "Required property 'collection_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def location_name(self) -> builtins.str:
            '''The CIDR collection location name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-cidrroutingconfig.html#cfn-route53-recordsetgroup-cidrroutingconfig-locationname
            '''
            result = self._values.get("location_name")
            assert result is not None, "Required property 'location_name' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CidrRoutingConfigProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup.CoordinatesProperty",
        jsii_struct_bases=[],
        name_mapping={"latitude": "latitude", "longitude": "longitude"},
    )
    class CoordinatesProperty:
        def __init__(self, *, latitude: builtins.str, longitude: builtins.str) -> None:
            '''A complex type that lists the coordinates for a geoproximity resource record.

            :param latitude: Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).
            :param longitude: Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-coordinates.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                coordinates_property = route53.CfnRecordSetGroup.CoordinatesProperty(
                    latitude="latitude",
                    longitude="longitude"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__3ebaae8a752b3b1dfff4bf671352e45cbd7c98fa0058ccfb5170085a3e53f8cb)
                check_type(argname="argument latitude", value=latitude, expected_type=type_hints["latitude"])
                check_type(argname="argument longitude", value=longitude, expected_type=type_hints["longitude"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "latitude": latitude,
                "longitude": longitude,
            }

        @builtins.property
        def latitude(self) -> builtins.str:
            '''Specifies a coordinate of the north–south position of a geographic point on the surface of the Earth (-90 - 90).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-coordinates.html#cfn-route53-recordsetgroup-coordinates-latitude
            '''
            result = self._values.get("latitude")
            assert result is not None, "Required property 'latitude' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def longitude(self) -> builtins.str:
            '''Specifies a coordinate of the east–west position of a geographic point on the surface of the Earth (-180 - 180).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-coordinates.html#cfn-route53-recordsetgroup-coordinates-longitude
            '''
            result = self._values.get("longitude")
            assert result is not None, "Required property 'longitude' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CoordinatesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup.GeoLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "continent_code": "continentCode",
            "country_code": "countryCode",
            "subdivision_code": "subdivisionCode",
        },
    )
    class GeoLocationProperty:
        def __init__(
            self,
            *,
            continent_code: typing.Optional[builtins.str] = None,
            country_code: typing.Optional[builtins.str] = None,
            subdivision_code: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A complex type that contains information about a geographic location.

            :param continent_code: For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Route 53 supports the following continent codes:. - *AF* : Africa - *AN* : Antarctica - *AS* : Asia - *EU* : Europe - *OC* : Oceania - *NA* : North America - *SA* : South America Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.
            :param country_code: For geolocation resource record sets, the two-letter code for a country. Route 53 uses the two-letter country codes that are specified in `ISO standard 3166-1 alpha-2 <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .
            :param subdivision_code: For geolocation resource record sets, the two-letter code for a state of the United States. Route 53 doesn't support any other values for ``SubdivisionCode`` . For a list of state abbreviations, see `Appendix B: Two–Letter State and Possession Abbreviations <https://docs.aws.amazon.com/https://pe.usps.com/text/pub28/28apb.htm>`_ on the United States Postal Service website. If you specify ``subdivisioncode`` , you must also specify ``US`` for ``CountryCode`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geolocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                geo_location_property = route53.CfnRecordSetGroup.GeoLocationProperty(
                    continent_code="continentCode",
                    country_code="countryCode",
                    subdivision_code="subdivisionCode"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2815193fa29c379ea003dd9391a70d63f49989043e7f24e220ccebb1143c1026)
                check_type(argname="argument continent_code", value=continent_code, expected_type=type_hints["continent_code"])
                check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
                check_type(argname="argument subdivision_code", value=subdivision_code, expected_type=type_hints["subdivision_code"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if continent_code is not None:
                self._values["continent_code"] = continent_code
            if country_code is not None:
                self._values["country_code"] = country_code
            if subdivision_code is not None:
                self._values["subdivision_code"] = subdivision_code

        @builtins.property
        def continent_code(self) -> typing.Optional[builtins.str]:
            '''For geolocation resource record sets, a two-letter abbreviation that identifies a continent. Route 53 supports the following continent codes:.

            - *AF* : Africa
            - *AN* : Antarctica
            - *AS* : Asia
            - *EU* : Europe
            - *OC* : Oceania
            - *NA* : North America
            - *SA* : South America

            Constraint: Specifying ``ContinentCode`` with either ``CountryCode`` or ``SubdivisionCode`` returns an ``InvalidInput`` error.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geolocation.html#cfn-route53-recordsetgroup-geolocation-continentcode
            '''
            result = self._values.get("continent_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def country_code(self) -> typing.Optional[builtins.str]:
            '''For geolocation resource record sets, the two-letter code for a country.

            Route 53 uses the two-letter country codes that are specified in `ISO standard 3166-1 alpha-2 <https://docs.aws.amazon.com/https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geolocation.html#cfn-route53-recordsetgroup-geolocation-countrycode
            '''
            result = self._values.get("country_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def subdivision_code(self) -> typing.Optional[builtins.str]:
            '''For geolocation resource record sets, the two-letter code for a state of the United States.

            Route 53 doesn't support any other values for ``SubdivisionCode`` . For a list of state abbreviations, see `Appendix B: Two–Letter State and Possession Abbreviations <https://docs.aws.amazon.com/https://pe.usps.com/text/pub28/28apb.htm>`_ on the United States Postal Service website.

            If you specify ``subdivisioncode`` , you must also specify ``US`` for ``CountryCode`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geolocation.html#cfn-route53-recordsetgroup-geolocation-subdivisioncode
            '''
            result = self._values.get("subdivision_code")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup.GeoProximityLocationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_region": "awsRegion",
            "bias": "bias",
            "coordinates": "coordinates",
            "local_zone_group": "localZoneGroup",
        },
    )
    class GeoProximityLocationProperty:
        def __init__(
            self,
            *,
            aws_region: typing.Optional[builtins.str] = None,
            bias: typing.Optional[jsii.Number] = None,
            coordinates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSetGroup.CoordinatesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            local_zone_group: typing.Optional[builtins.str] = None,
        ) -> None:
            '''(Resource record sets only): A complex type that lets you specify where your resources are located.

            Only one of ``LocalZoneGroup`` , ``Coordinates`` , or ``AWS Region`` is allowed per request at a time.

            For more information about geoproximity routing, see `Geoproximity routing <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-geoproximity.html>`_ in the *Amazon Route 53 Developer Guide* .

            :param aws_region: The AWS Region the resource you are directing DNS traffic to, is in.
            :param bias: The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource. To use ``Bias`` to change the size of the geographic region, specify the applicable value for the bias: - To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions. - To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.
            :param coordinates: Contains the longitude and latitude for a geographic region.
            :param local_zone_group: Specifies an AWS Local Zone Group. A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is ``us-east-1-bue-1a`` the Local Zone Group is ``us-east-1-bue-1`` . You can identify the Local Zones Group for a specific Local Zone by using the `describe-availability-zones <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html>`_ CLI command: This command returns: ``"GroupName": "us-west-2-den-1"`` , specifying that the Local Zone ``us-west-2-den-1a`` belongs to the Local Zone Group ``us-west-2-den-1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geoproximitylocation.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                geo_proximity_location_property = route53.CfnRecordSetGroup.GeoProximityLocationProperty(
                    aws_region="awsRegion",
                    bias=123,
                    coordinates=route53.CfnRecordSetGroup.CoordinatesProperty(
                        latitude="latitude",
                        longitude="longitude"
                    ),
                    local_zone_group="localZoneGroup"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5430af5a2d4636b1244b53f4c6759f6d1ffde530908e449cf4bc90b0d9de5ec8)
                check_type(argname="argument aws_region", value=aws_region, expected_type=type_hints["aws_region"])
                check_type(argname="argument bias", value=bias, expected_type=type_hints["bias"])
                check_type(argname="argument coordinates", value=coordinates, expected_type=type_hints["coordinates"])
                check_type(argname="argument local_zone_group", value=local_zone_group, expected_type=type_hints["local_zone_group"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_region is not None:
                self._values["aws_region"] = aws_region
            if bias is not None:
                self._values["bias"] = bias
            if coordinates is not None:
                self._values["coordinates"] = coordinates
            if local_zone_group is not None:
                self._values["local_zone_group"] = local_zone_group

        @builtins.property
        def aws_region(self) -> typing.Optional[builtins.str]:
            '''The AWS Region the resource you are directing DNS traffic to, is in.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geoproximitylocation.html#cfn-route53-recordsetgroup-geoproximitylocation-awsregion
            '''
            result = self._values.get("aws_region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def bias(self) -> typing.Optional[jsii.Number]:
            '''The bias increases or decreases the size of the geographic region from which Route 53 routes traffic to a resource.

            To use ``Bias`` to change the size of the geographic region, specify the applicable value for the bias:

            - To expand the size of the geographic region from which Route 53 routes traffic to a resource, specify a positive integer from 1 to 99 for the bias. Route 53 shrinks the size of adjacent regions.
            - To shrink the size of the geographic region from which Route 53 routes traffic to a resource, specify a negative bias of -1 to -99. Route 53 expands the size of adjacent regions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geoproximitylocation.html#cfn-route53-recordsetgroup-geoproximitylocation-bias
            '''
            result = self._values.get("bias")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def coordinates(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.CoordinatesProperty"]]:
            '''Contains the longitude and latitude for a geographic region.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geoproximitylocation.html#cfn-route53-recordsetgroup-geoproximitylocation-coordinates
            '''
            result = self._values.get("coordinates")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.CoordinatesProperty"]], result)

        @builtins.property
        def local_zone_group(self) -> typing.Optional[builtins.str]:
            '''Specifies an AWS Local Zone Group.

            A local Zone Group is usually the Local Zone code without the ending character. For example, if the Local Zone is ``us-east-1-bue-1a`` the Local Zone Group is ``us-east-1-bue-1`` .

            You can identify the Local Zones Group for a specific Local Zone by using the `describe-availability-zones <https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html>`_ CLI command:

            This command returns: ``"GroupName": "us-west-2-den-1"`` , specifying that the Local Zone ``us-west-2-den-1a`` belongs to the Local Zone Group ``us-west-2-den-1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-geoproximitylocation.html#cfn-route53-recordsetgroup-geoproximitylocation-localzonegroup
            '''
            result = self._values.get("local_zone_group")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GeoProximityLocationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroup.RecordSetProperty",
        jsii_struct_bases=[],
        name_mapping={
            "name": "name",
            "type": "type",
            "alias_target": "aliasTarget",
            "cidr_routing_config": "cidrRoutingConfig",
            "failover": "failover",
            "geo_location": "geoLocation",
            "geo_proximity_location": "geoProximityLocation",
            "health_check_id": "healthCheckId",
            "hosted_zone_id": "hostedZoneId",
            "hosted_zone_name": "hostedZoneName",
            "multi_value_answer": "multiValueAnswer",
            "region": "region",
            "resource_records": "resourceRecords",
            "set_identifier": "setIdentifier",
            "ttl": "ttl",
            "weight": "weight",
        },
    )
    class RecordSetProperty:
        def __init__(
            self,
            *,
            name: builtins.str,
            type: builtins.str,
            alias_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSetGroup.AliasTargetProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            cidr_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSetGroup.CidrRoutingConfigProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            failover: typing.Optional[builtins.str] = None,
            geo_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSetGroup.GeoLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            geo_proximity_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnRecordSetGroup.GeoProximityLocationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            health_check_id: typing.Optional[builtins.str] = None,
            hosted_zone_id: typing.Optional[builtins.str] = None,
            hosted_zone_name: typing.Optional[builtins.str] = None,
            multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            region: typing.Optional[builtins.str] = None,
            resource_records: typing.Optional[typing.Sequence[builtins.str]] = None,
            set_identifier: typing.Optional[builtins.str] = None,
            ttl: typing.Optional[builtins.str] = None,
            weight: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Information about one record that you want to create.

            :param name: For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record in the specified hosted zone. *ChangeResourceRecordSets Only* Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical. For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`_ in the *Amazon Route 53 Developer Guide* . You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following: - The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` . - The * can't replace any of the middle labels, for example, marketing.*.example.com. - If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. .. epigraph:: You can't use the * wildcard for resource records sets that have a type of NS.
            :param type: The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* . Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``DS`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT`` Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group. Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` | ``CAA`` .. epigraph:: SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <https://docs.aws.amazon.com/http://tools.ietf.org/html/rfc7208#section-14.1>`_ . Values for alias resource record sets: - *Amazon API Gateway custom regional APIs and edge-optimized APIs:* ``A`` - *CloudFront distributions:* ``A`` If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` . - *Amazon API Gateway environment that has a regionalized subdomain* : ``A`` - *ELB load balancers:* ``A`` | ``AAAA`` - *Amazon S3 buckets:* ``A`` - *Amazon Virtual Private Cloud interface VPC endpoints* ``A`` - *Another resource record set in this hosted zone:* Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` . .. epigraph:: If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't route traffic to a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.
            :param alias_target: *Alias resource record sets only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to. If you're creating resource records sets for a private hosted zone, note the following: - You can't create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution. - For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ in the *Amazon Route 53 Developer Guide* .
            :param cidr_routing_config: 
            :param failover: *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set. Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets: - When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. - When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set. - When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. - If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets. For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true. For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_
            :param geo_location: *Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` . If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource. You can't create two geolocation resource record sets that specify the same geographic location. The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements. .. epigraph:: Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Route 53 returns a "no answer" response for queries from those locations. You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.
            :param geo_proximity_location: A complex type that contains information about a geographic location.
            :param health_check_id: If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check. Route 53 determines whether a resource record set is healthy based on one of the following: - By periodically sending a request to the endpoint that is specified in the health check - By aggregating the status of a specified group of health checks (calculated health checks) - By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) .. epigraph:: Route 53 doesn't check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check. For more information, see the following topics in the *Amazon Route 53 Developer Guide* : - `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ *When to Specify HealthCheckId* Specifying a value for ``HealthCheckId`` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations: - *Non-alias resource record sets* : You're checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets. If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly. - *Alias resource record sets* : You specify the following settings: - You set ``EvaluateTargetHealth`` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A). - You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone. - You specify a health check ID for the non-alias resource record set. If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with. If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set. .. epigraph:: The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets. *Geolocation Routing* For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has ``*`` for ``CountryCode`` is ``*`` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy: - The United States - North America - The default resource record set *Specifying the Health Check Endpoint by Domain Name* If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets ( ``www.example.com`` ). .. epigraph:: Health check results will be unpredictable if you do the following: - Create a health check that has the same value for ``FullyQualifiedDomainName`` as the name of a resource record set. - Associate that health check with the resource record set.
            :param hosted_zone_id: The ID of the hosted zone that you want to create records in. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` . Do not provide the ``HostedZoneId`` if it is already defined in ``AWS::Route53::RecordSetGroup`` . The creation fails if ``HostedZoneId`` is defined in both.
            :param hosted_zone_name: The name of the hosted zone that you want to create records in. You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` . When you create a stack using an ``AWS::Route53::RecordSet`` that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the ``HostedZoneName`` . If AWS CloudFormation can't find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
            :param multi_value_answer: *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following: - If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. - If you don't associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy. - Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records. - If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records. - When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records. - If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. You can't create multivalue answer alias records.
            :param region: *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Note the following: - You can only specify one ``ResourceRecord`` per latency resource record set. - You can only create one latency resource record set for each Amazon EC2 Region. - You aren't required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. - You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets.
            :param resource_records: Information about the records that you want to create. Each record should be in the format appropriate for the record type specified by the ``Type`` property. For information about different record types and their record formats, see `Values That You Specify When You Create or Edit Amazon Route 53 Records <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html>`_ in the *Amazon Route 53 Developer Guide* .
            :param set_identifier: *Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set. For information about routing policies, see `Choosing a Routing Policy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`_ in the *Amazon Route 53 Developer Guide* .
            :param ttl: The resource record cache time to live (TTL), in seconds. Note the following:. - If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target. - If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. - All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . - If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` .
            :param weight: *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following: - You must specify a value for the ``Weight`` element for every weighted resource record set. - You can only specify one ``ResourceRecord`` per weighted resource record set. - You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. - You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. - For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Route 53 Active-Active and Active-Passive Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_route53 as route53
                
                record_set_property = route53.CfnRecordSetGroup.RecordSetProperty(
                    name="name",
                    type="type",
                
                    # the properties below are optional
                    alias_target=route53.CfnRecordSetGroup.AliasTargetProperty(
                        dns_name="dnsName",
                        hosted_zone_id="hostedZoneId",
                
                        # the properties below are optional
                        evaluate_target_health=False
                    ),
                    cidr_routing_config=route53.CfnRecordSetGroup.CidrRoutingConfigProperty(
                        collection_id="collectionId",
                        location_name="locationName"
                    ),
                    failover="failover",
                    geo_location=route53.CfnRecordSetGroup.GeoLocationProperty(
                        continent_code="continentCode",
                        country_code="countryCode",
                        subdivision_code="subdivisionCode"
                    ),
                    geo_proximity_location=route53.CfnRecordSetGroup.GeoProximityLocationProperty(
                        aws_region="awsRegion",
                        bias=123,
                        coordinates=route53.CfnRecordSetGroup.CoordinatesProperty(
                            latitude="latitude",
                            longitude="longitude"
                        ),
                        local_zone_group="localZoneGroup"
                    ),
                    health_check_id="healthCheckId",
                    hosted_zone_id="hostedZoneId",
                    hosted_zone_name="hostedZoneName",
                    multi_value_answer=False,
                    region="region",
                    resource_records=["resourceRecords"],
                    set_identifier="setIdentifier",
                    ttl="ttl",
                    weight=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__11ff291a729fd95a26a222e98e883239191c114a9dd6e70516ac2fe433d4b95d)
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument alias_target", value=alias_target, expected_type=type_hints["alias_target"])
                check_type(argname="argument cidr_routing_config", value=cidr_routing_config, expected_type=type_hints["cidr_routing_config"])
                check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
                check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
                check_type(argname="argument geo_proximity_location", value=geo_proximity_location, expected_type=type_hints["geo_proximity_location"])
                check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
                check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
                check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
                check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument resource_records", value=resource_records, expected_type=type_hints["resource_records"])
                check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
                check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
                check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "name": name,
                "type": type,
            }
            if alias_target is not None:
                self._values["alias_target"] = alias_target
            if cidr_routing_config is not None:
                self._values["cidr_routing_config"] = cidr_routing_config
            if failover is not None:
                self._values["failover"] = failover
            if geo_location is not None:
                self._values["geo_location"] = geo_location
            if geo_proximity_location is not None:
                self._values["geo_proximity_location"] = geo_proximity_location
            if health_check_id is not None:
                self._values["health_check_id"] = health_check_id
            if hosted_zone_id is not None:
                self._values["hosted_zone_id"] = hosted_zone_id
            if hosted_zone_name is not None:
                self._values["hosted_zone_name"] = hosted_zone_name
            if multi_value_answer is not None:
                self._values["multi_value_answer"] = multi_value_answer
            if region is not None:
                self._values["region"] = region
            if resource_records is not None:
                self._values["resource_records"] = resource_records
            if set_identifier is not None:
                self._values["set_identifier"] = set_identifier
            if ttl is not None:
                self._values["ttl"] = ttl
            if weight is not None:
                self._values["weight"] = weight

        @builtins.property
        def name(self) -> builtins.str:
            '''For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete.

            For ``ListResourceRecordSets`` responses, the name of a record in the specified hosted zone.

            *ChangeResourceRecordSets Only*

            Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical.

            For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`_ in the *Amazon Route 53 Developer Guide* .

            You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following:

            - The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` .
            - The * can't replace any of the middle labels, for example, marketing.*.example.com.
            - If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.

            .. epigraph::

               You can't use the * wildcard for resource records sets that have a type of NS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-name
            '''
            result = self._values.get("name")
            assert result is not None, "Required property 'name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The DNS record type.

            For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* .

            Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``DS`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``

            Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.

            Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` | ``CAA``
            .. epigraph::

               SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <https://docs.aws.amazon.com/http://tools.ietf.org/html/rfc7208#section-14.1>`_ .

            Values for alias resource record sets:

            - *Amazon API Gateway custom regional APIs and edge-optimized APIs:* ``A``
            - *CloudFront distributions:* ``A``

            If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` .

            - *Amazon API Gateway environment that has a regionalized subdomain* : ``A``
            - *ELB load balancers:* ``A`` | ``AAAA``
            - *Amazon S3 buckets:* ``A``
            - *Amazon Virtual Private Cloud interface VPC endpoints* ``A``
            - *Another resource record set in this hosted zone:* Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` .

            .. epigraph::

               If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't route traffic to a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def alias_target(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.AliasTargetProperty"]]:
            '''*Alias resource record sets only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.

            If you're creating resource records sets for a private hosted zone, note the following:

            - You can't create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution.
            - For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-aliastarget
            '''
            result = self._values.get("alias_target")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.AliasTargetProperty"]], result)

        @builtins.property
        def cidr_routing_config(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.CidrRoutingConfigProperty"]]:
            '''
            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-cidrroutingconfig
            '''
            result = self._values.get("cidr_routing_config")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.CidrRoutingConfigProperty"]], result)

        @builtins.property
        def failover(self) -> typing.Optional[builtins.str]:
            '''*Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets.

            For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

            Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets:

            - When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
            - When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
            - When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
            - If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.

            You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets.

            For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true.

            For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* :

            - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_
            - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-failover
            '''
            result = self._values.get("failover")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def geo_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.GeoLocationProperty"]]:
            '''*Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query.

            For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` .

            If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.

            You can't create two geolocation resource record sets that specify the same geographic location.

            The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements.
            .. epigraph::

               Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Route 53 returns a "no answer" response for queries from those locations.

            You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-geolocation
            '''
            result = self._values.get("geo_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.GeoLocationProperty"]], result)

        @builtins.property
        def geo_proximity_location(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.GeoProximityLocationProperty"]]:
            '''A complex type that contains information about a geographic location.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-geoproximitylocation
            '''
            result = self._values.get("geo_proximity_location")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnRecordSetGroup.GeoProximityLocationProperty"]], result)

        @builtins.property
        def health_check_id(self) -> typing.Optional[builtins.str]:
            '''If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check.

            Route 53 determines whether a resource record set is healthy based on one of the following:

            - By periodically sending a request to the endpoint that is specified in the health check
            - By aggregating the status of a specified group of health checks (calculated health checks)
            - By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)

            .. epigraph::

               Route 53 doesn't check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check.

            For more information, see the following topics in the *Amazon Route 53 Developer Guide* :

            - `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_
            - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_
            - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_

            *When to Specify HealthCheckId*

            Specifying a value for ``HealthCheckId`` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:

            - *Non-alias resource record sets* : You're checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets.

            If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with.

            If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set.

            If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.

            - *Alias resource record sets* : You specify the following settings:
            - You set ``EvaluateTargetHealth`` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).
            - You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone.
            - You specify a health check ID for the non-alias resource record set.

            If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.

            If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.
            .. epigraph::

               The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.

            *Geolocation Routing*

            For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has ``*`` for ``CountryCode`` is ``*`` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:

            - The United States
            - North America
            - The default resource record set

            *Specifying the Health Check Endpoint by Domain Name*

            If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets ( ``www.example.com`` ).
            .. epigraph::

               Health check results will be unpredictable if you do the following:

               - Create a health check that has the same value for ``FullyQualifiedDomainName`` as the name of a resource record set.
               - Associate that health check with the resource record set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-healthcheckid
            '''
            result = self._values.get("health_check_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_id(self) -> typing.Optional[builtins.str]:
            '''The ID of the hosted zone that you want to create records in.

            Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .

            Do not provide the ``HostedZoneId`` if it is already defined in ``AWS::Route53::RecordSetGroup`` . The creation fails if ``HostedZoneId`` is defined in both.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-hostedzoneid
            '''
            result = self._values.get("hosted_zone_id")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def hosted_zone_name(self) -> typing.Optional[builtins.str]:
            '''The name of the hosted zone that you want to create records in.

            You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` .

            When you create a stack using an ``AWS::Route53::RecordSet`` that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the ``HostedZoneName`` . If AWS CloudFormation can't find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack.

            Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-hostedzonename
            '''
            result = self._values.get("hosted_zone_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def multi_value_answer(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''*Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` .

            Note the following:

            - If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy.
            - If you don't associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy.
            - Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records.
            - If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records.
            - When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records.
            - If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response.

            You can't create multivalue answer alias records.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-multivalueanswer
            '''
            result = self._values.get("multi_value_answer")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def region(self) -> typing.Optional[builtins.str]:
            '''*Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to.

            The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

            When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.

            Note the following:

            - You can only specify one ``ResourceRecord`` per latency resource record set.
            - You can only create one latency resource record set for each Amazon EC2 Region.
            - You aren't required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for.
            - You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-region
            '''
            result = self._values.get("region")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def resource_records(self) -> typing.Optional[typing.List[builtins.str]]:
            '''Information about the records that you want to create.

            Each record should be in the format appropriate for the record type specified by the ``Type`` property. For information about different record types and their record formats, see `Values That You Specify When You Create or Edit Amazon Route 53 Records <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resource-record-sets-values.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-resourcerecords
            '''
            result = self._values.get("resource_records")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def set_identifier(self) -> typing.Optional[builtins.str]:
            '''*Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set.

            For information about routing policies, see `Choosing a Routing Policy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-setidentifier
            '''
            result = self._values.get("set_identifier")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def ttl(self) -> typing.Optional[builtins.str]:
            '''The resource record cache time to live (TTL), in seconds. Note the following:.

            - If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target.
            - If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status.
            - All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` .
            - If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-ttl
            '''
            result = self._values.get("ttl")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def weight(self) -> typing.Optional[jsii.Number]:
            '''*Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

            Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:

            - You must specify a value for the ``Weight`` element for every weighted resource record set.
            - You can only specify one ``ResourceRecord`` per weighted resource record set.
            - You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets.
            - You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements.
            - For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability.

            The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Route 53 Active-Active and Active-Passive Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`_ in the *Amazon Route 53 Developer Guide* .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-route53-recordsetgroup-recordset.html#cfn-route53-recordsetgroup-recordset-weight
            '''
            result = self._values.get("weight")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RecordSetProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "comment": "comment",
        "hosted_zone_id": "hostedZoneId",
        "hosted_zone_name": "hostedZoneName",
        "record_sets": "recordSets",
    },
)
class CfnRecordSetGroupProps:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        record_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.RecordSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnRecordSetGroup``.

        :param comment: *Optional:* Any comments you want to include about a change batch request.
        :param hosted_zone_id: The ID of the hosted zone that you want to create records in. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param hosted_zone_name: The name of the hosted zone that you want to create records in. You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` . When you create a stack using an ``AWS::Route53::RecordSet`` that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the ``HostedZoneName`` . If AWS CloudFormation can't find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param record_sets: A complex type that contains one ``RecordSet`` element for each record that you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_record_set_group_props = route53.CfnRecordSetGroupProps(
                comment="comment",
                hosted_zone_id="hostedZoneId",
                hosted_zone_name="hostedZoneName",
                record_sets=[route53.CfnRecordSetGroup.RecordSetProperty(
                    name="name",
                    type="type",
            
                    # the properties below are optional
                    alias_target=route53.CfnRecordSetGroup.AliasTargetProperty(
                        dns_name="dnsName",
                        hosted_zone_id="hostedZoneId",
            
                        # the properties below are optional
                        evaluate_target_health=False
                    ),
                    cidr_routing_config=route53.CfnRecordSetGroup.CidrRoutingConfigProperty(
                        collection_id="collectionId",
                        location_name="locationName"
                    ),
                    failover="failover",
                    geo_location=route53.CfnRecordSetGroup.GeoLocationProperty(
                        continent_code="continentCode",
                        country_code="countryCode",
                        subdivision_code="subdivisionCode"
                    ),
                    geo_proximity_location=route53.CfnRecordSetGroup.GeoProximityLocationProperty(
                        aws_region="awsRegion",
                        bias=123,
                        coordinates=route53.CfnRecordSetGroup.CoordinatesProperty(
                            latitude="latitude",
                            longitude="longitude"
                        ),
                        local_zone_group="localZoneGroup"
                    ),
                    health_check_id="healthCheckId",
                    hosted_zone_id="hostedZoneId",
                    hosted_zone_name="hostedZoneName",
                    multi_value_answer=False,
                    region="region",
                    resource_records=["resourceRecords"],
                    set_identifier="setIdentifier",
                    ttl="ttl",
                    weight=123
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__550eb58db998305b4dd78ae1bd39e80af0e9376310d796614d4bcd99a1dd82b6)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
            check_type(argname="argument record_sets", value=record_sets, expected_type=type_hints["record_sets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if hosted_zone_id is not None:
            self._values["hosted_zone_id"] = hosted_zone_id
        if hosted_zone_name is not None:
            self._values["hosted_zone_name"] = hosted_zone_name
        if record_sets is not None:
            self._values["record_sets"] = record_sets

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''*Optional:* Any comments you want to include about a change batch request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the hosted zone that you want to create records in.

        Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzoneid
        '''
        result = self._values.get("hosted_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''The name of the hosted zone that you want to create records in.

        You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` .

        When you create a stack using an ``AWS::Route53::RecordSet`` that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the ``HostedZoneName`` . If AWS CloudFormation can't find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack.

        Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-hostedzonename
        '''
        result = self._values.get("hosted_zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def record_sets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRecordSetGroup.RecordSetProperty]]]]:
        '''A complex type that contains one ``RecordSet`` element for each record that you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordsetgroup.html#cfn-route53-recordsetgroup-recordsets
        '''
        result = self._values.get("record_sets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRecordSetGroup.RecordSetProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordSetGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CfnRecordSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "type": "type",
        "alias_target": "aliasTarget",
        "cidr_routing_config": "cidrRoutingConfig",
        "comment": "comment",
        "failover": "failover",
        "geo_location": "geoLocation",
        "geo_proximity_location": "geoProximityLocation",
        "health_check_id": "healthCheckId",
        "hosted_zone_id": "hostedZoneId",
        "hosted_zone_name": "hostedZoneName",
        "multi_value_answer": "multiValueAnswer",
        "region": "region",
        "resource_records": "resourceRecords",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
    },
)
class CfnRecordSetProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        type: builtins.str,
        alias_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.AliasTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        cidr_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.CidrRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        comment: typing.Optional[builtins.str] = None,
        failover: typing.Optional[builtins.str] = None,
        geo_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.GeoLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        geo_proximity_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.GeoProximityLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        health_check_id: typing.Optional[builtins.str] = None,
        hosted_zone_id: typing.Optional[builtins.str] = None,
        hosted_zone_name: typing.Optional[builtins.str] = None,
        multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        region: typing.Optional[builtins.str] = None,
        resource_records: typing.Optional[typing.Sequence[builtins.str]] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[builtins.str] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Properties for defining a ``CfnRecordSet``.

        :param name: For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete. For ``ListResourceRecordSets`` responses, the name of a record in the specified hosted zone. *ChangeResourceRecordSets Only* Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical. For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`_ in the *Amazon Route 53 Developer Guide* . You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following: - The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` . - The * can't replace any of the middle labels, for example, marketing.*.example.com. - If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard. .. epigraph:: You can't use the * wildcard for resource records sets that have a type of NS.
        :param type: The DNS record type. For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* . Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``DS`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT`` Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group. Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` | ``CAA`` .. epigraph:: SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <https://docs.aws.amazon.com/http://tools.ietf.org/html/rfc7208#section-14.1>`_ . Values for alias resource record sets: - *Amazon API Gateway custom regional APIs and edge-optimized APIs:* ``A`` - *CloudFront distributions:* ``A`` If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` . - *Amazon API Gateway environment that has a regionalized subdomain* : ``A`` - *ELB load balancers:* ``A`` | ``AAAA`` - *Amazon S3 buckets:* ``A`` - *Amazon Virtual Private Cloud interface VPC endpoints* ``A`` - *Another resource record set in this hosted zone:* Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` . .. epigraph:: If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't route traffic to a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.
        :param alias_target: *Alias resource record sets only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to. If you're creating resource records sets for a private hosted zone, note the following: - You can't create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution. - For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ in the *Amazon Route 53 Developer Guide* .
        :param cidr_routing_config: The object that is specified in resource record set object when you are linking a resource record set to a CIDR location. A ``LocationName`` with an asterisk “*” can be used to create a default CIDR record. ``CollectionId`` is still required for default record.
        :param comment: *Optional:* Any comments you want to include about a change batch request.
        :param failover: *Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets. For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set. Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets: - When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set. - When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set. - When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set. - If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint. You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets. For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true. For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* : - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_
        :param geo_location: *Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query. For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` . If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource. You can't create two geolocation resource record sets that specify the same geographic location. The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements. .. epigraph:: Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Route 53 returns a "no answer" response for queries from those locations. You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.
        :param geo_proximity_location: *GeoproximityLocation resource record sets only:* A complex type that lets you control how Route 53 responds to DNS queries based on the geographic origin of the query and your resources.
        :param health_check_id: If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check. Route 53 determines whether a resource record set is healthy based on one of the following: - By periodically sending a request to the endpoint that is specified in the health check - By aggregating the status of a specified group of health checks (calculated health checks) - By determining the current state of a CloudWatch alarm (CloudWatch metric health checks) .. epigraph:: Route 53 doesn't check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check. For more information, see the following topics in the *Amazon Route 53 Developer Guide* : - `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_ - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_ - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ *When to Specify HealthCheckId* Specifying a value for ``HealthCheckId`` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations: - *Non-alias resource record sets* : You're checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets. If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with. If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set. If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly. - *Alias resource record sets* : You specify the following settings: - You set ``EvaluateTargetHealth`` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A). - You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone. - You specify a health check ID for the non-alias resource record set. If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with. If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set. .. epigraph:: The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets. *Geolocation Routing* For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has ``*`` for ``CountryCode`` is ``*`` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy: - The United States - North America - The default resource record set *Specifying the Health Check Endpoint by Domain Name* If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets ( ``www.example.com`` ). .. epigraph:: Health check results will be unpredictable if you do the following: - Create a health check that has the same value for ``FullyQualifiedDomainName`` as the name of a resource record set. - Associate that health check with the resource record set.
        :param hosted_zone_id: The ID of the hosted zone that you want to create records in. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param hosted_zone_name: The name of the hosted zone that you want to create records in. You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` . When you create a stack using an AWS::Route53::RecordSet that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the HostedZoneName. If AWS CloudFormation cannot find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack. Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .
        :param multi_value_answer: *Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` . Note the following: - If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy. - If you don't associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy. - Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records. - If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records. - When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records. - If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response. You can't create multivalue answer alias records.
        :param region: *Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Note the following: - You can only specify one ``ResourceRecord`` per latency resource record set. - You can only create one latency resource record set for each Amazon EC2 Region. - You aren't required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for. - You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets.
        :param resource_records: One or more values that correspond with the value that you specified for the ``Type`` property. For example, if you specified ``A`` for ``Type`` , you specify one or more IP addresses in IPv4 format for ``ResourceRecords`` . For information about the format of values for each record type, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* . Note the following: - You can specify more than one value for all record types except CNAME and SOA. - The maximum length of a value is 4000 characters. - If you're creating an alias record, omit ``ResourceRecords`` .
        :param set_identifier: *Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set. For information about routing policies, see `Choosing a Routing Policy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`_ in the *Amazon Route 53 Developer Guide* .
        :param ttl: The resource record cache time to live (TTL), in seconds. Note the following:. - If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target. - If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status. - All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` . - If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` .
        :param weight: *Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following: - You must specify a value for the ``Weight`` element for every weighted resource record set. - You can only specify one ``ResourceRecord`` per weighted resource record set. - You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets. - You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements. - For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability. The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Route 53 Active-Active and Active-Passive Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`_ in the *Amazon Route 53 Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            cfn_record_set_props = route53.CfnRecordSetProps(
                name="name",
                type="type",
            
                # the properties below are optional
                alias_target=route53.CfnRecordSet.AliasTargetProperty(
                    dns_name="dnsName",
                    hosted_zone_id="hostedZoneId",
            
                    # the properties below are optional
                    evaluate_target_health=False
                ),
                cidr_routing_config=route53.CfnRecordSet.CidrRoutingConfigProperty(
                    collection_id="collectionId",
                    location_name="locationName"
                ),
                comment="comment",
                failover="failover",
                geo_location=route53.CfnRecordSet.GeoLocationProperty(
                    continent_code="continentCode",
                    country_code="countryCode",
                    subdivision_code="subdivisionCode"
                ),
                geo_proximity_location=route53.CfnRecordSet.GeoProximityLocationProperty(
                    aws_region="awsRegion",
                    bias=123,
                    coordinates=route53.CfnRecordSet.CoordinatesProperty(
                        latitude="latitude",
                        longitude="longitude"
                    ),
                    local_zone_group="localZoneGroup"
                ),
                health_check_id="healthCheckId",
                hosted_zone_id="hostedZoneId",
                hosted_zone_name="hostedZoneName",
                multi_value_answer=False,
                region="region",
                resource_records=["resourceRecords"],
                set_identifier="setIdentifier",
                ttl="ttl",
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__07806684fd0bcb683322d42ae67181582216fa4e1371a7133012bf4898a3d7d5)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument alias_target", value=alias_target, expected_type=type_hints["alias_target"])
            check_type(argname="argument cidr_routing_config", value=cidr_routing_config, expected_type=type_hints["cidr_routing_config"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument failover", value=failover, expected_type=type_hints["failover"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument geo_proximity_location", value=geo_proximity_location, expected_type=type_hints["geo_proximity_location"])
            check_type(argname="argument health_check_id", value=health_check_id, expected_type=type_hints["health_check_id"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument hosted_zone_name", value=hosted_zone_name, expected_type=type_hints["hosted_zone_name"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument resource_records", value=resource_records, expected_type=type_hints["resource_records"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "type": type,
        }
        if alias_target is not None:
            self._values["alias_target"] = alias_target
        if cidr_routing_config is not None:
            self._values["cidr_routing_config"] = cidr_routing_config
        if comment is not None:
            self._values["comment"] = comment
        if failover is not None:
            self._values["failover"] = failover
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if geo_proximity_location is not None:
            self._values["geo_proximity_location"] = geo_proximity_location
        if health_check_id is not None:
            self._values["health_check_id"] = health_check_id
        if hosted_zone_id is not None:
            self._values["hosted_zone_id"] = hosted_zone_id
        if hosted_zone_name is not None:
            self._values["hosted_zone_name"] = hosted_zone_name
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if region is not None:
            self._values["region"] = region
        if resource_records is not None:
            self._values["resource_records"] = resource_records
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def name(self) -> builtins.str:
        '''For ``ChangeResourceRecordSets`` requests, the name of the record that you want to create, update, or delete.

        For ``ListResourceRecordSets`` responses, the name of a record in the specified hosted zone.

        *ChangeResourceRecordSets Only*

        Enter a fully qualified domain name, for example, ``www.example.com`` . You can optionally include a trailing dot. If you omit the trailing dot, Amazon Route 53 assumes that the domain name that you specify is fully qualified. This means that Route 53 treats ``www.example.com`` (without a trailing dot) and ``www.example.com.`` (with a trailing dot) as identical.

        For information about how to specify characters other than ``a-z`` , ``0-9`` , and ``-`` (hyphen) and how to specify internationalized domain names, see `DNS Domain Name Format <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DomainNameFormat.html>`_ in the *Amazon Route 53 Developer Guide* .

        You can use the asterisk (*) wildcard to replace the leftmost label in a domain name, for example, ``*.example.com`` . Note the following:

        - The * must replace the entire label. For example, you can't specify ``*prod.example.com`` or ``prod*.example.com`` .
        - The * can't replace any of the middle labels, for example, marketing.*.example.com.
        - If you include * in any position other than the leftmost label in a domain name, DNS treats it as an * character (ASCII 42), not as a wildcard.

        .. epigraph::

           You can't use the * wildcard for resource records sets that have a type of NS.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The DNS record type.

        For information about different record types and how data is encoded for them, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* .

        Valid values for basic resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``DS`` | ``MX`` | ``NAPTR`` | ``NS`` | ``PTR`` | ``SOA`` | ``SPF`` | ``SRV`` | ``TXT``

        Values for weighted, latency, geolocation, and failover resource record sets: ``A`` | ``AAAA`` | ``CAA`` | ``CNAME`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` . When creating a group of weighted, latency, geolocation, or failover resource record sets, specify the same value for all of the resource record sets in the group.

        Valid values for multivalue answer resource record sets: ``A`` | ``AAAA`` | ``MX`` | ``NAPTR`` | ``PTR`` | ``SPF`` | ``SRV`` | ``TXT`` | ``CAA``
        .. epigraph::

           SPF records were formerly used to verify the identity of the sender of email messages. However, we no longer recommend that you create resource record sets for which the value of ``Type`` is ``SPF`` . RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1* , has been updated to say, "...[I]ts existence and mechanism defined in [RFC4408] have led to some interoperability issues. Accordingly, its use is no longer appropriate for SPF version 1; implementations are not to use it." In RFC 7208, see section 14.1, `The SPF DNS Record Type <https://docs.aws.amazon.com/http://tools.ietf.org/html/rfc7208#section-14.1>`_ .

        Values for alias resource record sets:

        - *Amazon API Gateway custom regional APIs and edge-optimized APIs:* ``A``
        - *CloudFront distributions:* ``A``

        If IPv6 is enabled for the distribution, create two resource record sets to route traffic to your distribution, one with a value of ``A`` and one with a value of ``AAAA`` .

        - *Amazon API Gateway environment that has a regionalized subdomain* : ``A``
        - *ELB load balancers:* ``A`` | ``AAAA``
        - *Amazon S3 buckets:* ``A``
        - *Amazon Virtual Private Cloud interface VPC endpoints* ``A``
        - *Another resource record set in this hosted zone:* Specify the type of the resource record set that you're creating the alias for. All values are supported except ``NS`` and ``SOA`` .

        .. epigraph::

           If you're creating an alias record that has the same name as the hosted zone (known as the zone apex), you can't route traffic to a record for which the value of ``Type`` is ``CNAME`` . This is because the alias record must have the same type as the record you're routing traffic to, and creating a CNAME record for the zone apex isn't supported even for an alias record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def alias_target(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.AliasTargetProperty]]:
        '''*Alias resource record sets only:* Information about the AWS resource, such as a CloudFront distribution or an Amazon S3 bucket, that you want to route traffic to.

        If you're creating resource records sets for a private hosted zone, note the following:

        - You can't create an alias resource record set in a private hosted zone to route traffic to a CloudFront distribution.
        - For information about creating failover resource record sets in a private hosted zone, see `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_ in the *Amazon Route 53 Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-aliastarget
        '''
        result = self._values.get("alias_target")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.AliasTargetProperty]], result)

    @builtins.property
    def cidr_routing_config(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.CidrRoutingConfigProperty]]:
        '''The object that is specified in resource record set object when you are linking a resource record set to a CIDR location.

        A ``LocationName`` with an asterisk “*” can be used to create a default CIDR record. ``CollectionId`` is still required for default record.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-cidrroutingconfig
        '''
        result = self._values.get("cidr_routing_config")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.CidrRoutingConfigProperty]], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''*Optional:* Any comments you want to include about a change batch request.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def failover(self) -> typing.Optional[builtins.str]:
        '''*Failover resource record sets only:* To configure failover, you add the ``Failover`` element to two resource record sets.

        For one resource record set, you specify ``PRIMARY`` as the value for ``Failover`` ; for the other resource record set, you specify ``SECONDARY`` . In addition, you include the ``HealthCheckId`` element and specify the health check that you want Amazon Route 53 to perform for each resource record set.

        Except where noted, the following failover behaviors assume that you have included the ``HealthCheckId`` element in both resource record sets:

        - When the primary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the secondary resource record set.
        - When the primary resource record set is unhealthy and the secondary resource record set is healthy, Route 53 responds to DNS queries with the applicable value from the secondary resource record set.
        - When the secondary resource record set is unhealthy, Route 53 responds to DNS queries with the applicable value from the primary resource record set regardless of the health of the primary resource record set.
        - If you omit the ``HealthCheckId`` element for the secondary resource record set, and if the primary resource record set is unhealthy, Route 53 always responds to DNS queries with the applicable value from the secondary resource record set. This is true regardless of the health of the associated endpoint.

        You can't create non-failover resource record sets that have the same values for the ``Name`` and ``Type`` elements as failover resource record sets.

        For failover alias resource record sets, you must also include the ``EvaluateTargetHealth`` element and set the value to true.

        For more information about configuring failover for Route 53, see the following topics in the *Amazon Route 53 Developer Guide* :

        - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_
        - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-failover
        '''
        result = self._values.get("failover")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def geo_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.GeoLocationProperty]]:
        '''*Geolocation resource record sets only:* A complex type that lets you control how Amazon Route 53 responds to DNS queries based on the geographic origin of the query.

        For example, if you want all queries from Africa to be routed to a web server with an IP address of ``192.0.2.111`` , create a resource record set with a ``Type`` of ``A`` and a ``ContinentCode`` of ``AF`` .

        If you create separate resource record sets for overlapping geographic regions (for example, one resource record set for a continent and one for a country on the same continent), priority goes to the smallest geographic region. This allows you to route most queries for a continent to one resource and to route queries for a country on that continent to a different resource.

        You can't create two geolocation resource record sets that specify the same geographic location.

        The value ``*`` in the ``CountryCode`` element matches all geographic locations that aren't specified in other geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements.
        .. epigraph::

           Geolocation works by mapping IP addresses to locations. However, some IP addresses aren't mapped to geographic locations, so even if you create geolocation resource record sets that cover all seven continents, Route 53 will receive some DNS queries from locations that it can't identify. We recommend that you create a resource record set for which the value of ``CountryCode`` is ``*`` . Two groups of queries are routed to the resource that you specify in this record: queries that come from locations for which you haven't created geolocation resource record sets and queries from IP addresses that aren't mapped to a location. If you don't create a ``*`` resource record set, Route 53 returns a "no answer" response for queries from those locations.

        You can't create non-geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as geolocation resource record sets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-geolocation
        '''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.GeoLocationProperty]], result)

    @builtins.property
    def geo_proximity_location(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.GeoProximityLocationProperty]]:
        '''*GeoproximityLocation resource record sets only:* A complex type that lets you control how Route 53 responds to DNS queries based on the geographic origin of the query and your resources.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-geoproximitylocation
        '''
        result = self._values.get("geo_proximity_location")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.GeoProximityLocationProperty]], result)

    @builtins.property
    def health_check_id(self) -> typing.Optional[builtins.str]:
        '''If you want Amazon Route 53 to return this resource record set in response to a DNS query only when the status of a health check is healthy, include the ``HealthCheckId`` element and specify the ID of the applicable health check.

        Route 53 determines whether a resource record set is healthy based on one of the following:

        - By periodically sending a request to the endpoint that is specified in the health check
        - By aggregating the status of a specified group of health checks (calculated health checks)
        - By determining the current state of a CloudWatch alarm (CloudWatch metric health checks)

        .. epigraph::

           Route 53 doesn't check the health of the endpoint that is specified in the resource record set, for example, the endpoint specified by the IP address in the ``Value`` element. When you add a ``HealthCheckId`` element to a resource record set, Route 53 checks the health of the endpoint that you specified in the health check.

        For more information, see the following topics in the *Amazon Route 53 Developer Guide* :

        - `How Amazon Route 53 Determines Whether an Endpoint Is Healthy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-determining-health-of-endpoints.html>`_
        - `Route 53 Health Checks and DNS Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover.html>`_
        - `Configuring Failover in a Private Hosted Zone <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-private-hosted-zones.html>`_

        *When to Specify HealthCheckId*

        Specifying a value for ``HealthCheckId`` is useful only when Route 53 is choosing between two or more resource record sets to respond to a DNS query, and you want Route 53 to base the choice in part on the status of a health check. Configuring health checks makes sense only in the following configurations:

        - *Non-alias resource record sets* : You're checking the health of a group of non-alias resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A) and you specify health check IDs for all the resource record sets.

        If the health check status for a resource record set is healthy, Route 53 includes the record among the records that it responds to DNS queries with.

        If the health check status for a resource record set is unhealthy, Route 53 stops responding to DNS queries using the value for that resource record set.

        If the health check status for all resource record sets in the group is unhealthy, Route 53 considers all resource record sets in the group healthy and responds to DNS queries accordingly.

        - *Alias resource record sets* : You specify the following settings:
        - You set ``EvaluateTargetHealth`` to true for an alias resource record set in a group of resource record sets that have the same routing policy, name, and type (such as multiple weighted records named www.example.com with a type of A).
        - You configure the alias resource record set to route traffic to a non-alias resource record set in the same hosted zone.
        - You specify a health check ID for the non-alias resource record set.

        If the health check status is healthy, Route 53 considers the alias resource record set to be healthy and includes the alias record among the records that it responds to DNS queries with.

        If the health check status is unhealthy, Route 53 stops responding to DNS queries using the alias resource record set.
        .. epigraph::

           The alias resource record set can also route traffic to a *group* of non-alias resource record sets that have the same routing policy, name, and type. In that configuration, associate health checks with all of the resource record sets in the group of non-alias resource record sets.

        *Geolocation Routing*

        For geolocation resource record sets, if an endpoint is unhealthy, Route 53 looks for a resource record set for the larger, associated geographic region. For example, suppose you have resource record sets for a state in the United States, for the entire United States, for North America, and a resource record set that has ``*`` for ``CountryCode`` is ``*`` , which applies to all locations. If the endpoint for the state resource record set is unhealthy, Route 53 checks for healthy resource record sets in the following order until it finds a resource record set for which the endpoint is healthy:

        - The United States
        - North America
        - The default resource record set

        *Specifying the Health Check Endpoint by Domain Name*

        If your health checks specify the endpoint only by domain name, we recommend that you create a separate health check for each endpoint. For example, create a health check for each ``HTTP`` server that is serving content for ``www.example.com`` . For the value of ``FullyQualifiedDomainName`` , specify the domain name of the server (such as ``us-east-2-www.example.com`` ), not the name of the resource record sets ( ``www.example.com`` ).
        .. epigraph::

           Health check results will be unpredictable if you do the following:

           - Create a health check that has the same value for ``FullyQualifiedDomainName`` as the name of a resource record set.
           - Associate that health check with the resource record set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-healthcheckid
        '''
        result = self._values.get("health_check_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the hosted zone that you want to create records in.

        Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-hostedzoneid
        '''
        result = self._values.get("hosted_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''The name of the hosted zone that you want to create records in.

        You must include a trailing dot (for example, ``www.example.com.`` ) as part of the ``HostedZoneName`` .

        When you create a stack using an AWS::Route53::RecordSet that specifies ``HostedZoneName`` , AWS CloudFormation attempts to find a hosted zone whose name matches the HostedZoneName. If AWS CloudFormation cannot find a hosted zone with a matching domain name, or if there is more than one hosted zone with the specified domain name, AWS CloudFormation will not create the stack.

        Specify either ``HostedZoneName`` or ``HostedZoneId`` , but not both. If you have multiple hosted zones with the same domain name, you must specify the hosted zone using ``HostedZoneId`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-hostedzonename
        '''
        result = self._values.get("hosted_zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def multi_value_answer(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
        '''*Multivalue answer resource record sets only* : To route traffic approximately randomly to multiple resources, such as web servers, create one multivalue answer record for each resource and specify ``true`` for ``MultiValueAnswer`` .

        Note the following:

        - If you associate a health check with a multivalue answer resource record set, Amazon Route 53 responds to DNS queries with the corresponding IP address only when the health check is healthy.
        - If you don't associate a health check with a multivalue answer record, Route 53 always considers the record to be healthy.
        - Route 53 responds to DNS queries with up to eight healthy records; if you have eight or fewer healthy records, Route 53 responds to all DNS queries with all the healthy records.
        - If you have more than eight healthy records, Route 53 responds to different DNS resolvers with different combinations of healthy records.
        - When all records are unhealthy, Route 53 responds to DNS queries with up to eight unhealthy records.
        - If a resource becomes unavailable after a resolver caches a response, client software typically tries another of the IP addresses in the response.

        You can't create multivalue answer alias records.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-multivalueanswer
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''*Latency-based resource record sets only:* The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set.

        Note the following:

        - You can only specify one ``ResourceRecord`` per latency resource record set.
        - You can only create one latency resource record set for each Amazon EC2 Region.
        - You aren't required to create latency resource record sets for all Amazon EC2 Regions. Route 53 will choose the region with the best latency from among the regions that you create latency resource record sets for.
        - You can't create non-latency resource record sets that have the same values for the ``Name`` and ``Type`` elements as latency resource record sets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_records(self) -> typing.Optional[typing.List[builtins.str]]:
        '''One or more values that correspond with the value that you specified for the ``Type`` property.

        For example, if you specified ``A`` for ``Type`` , you specify one or more IP addresses in IPv4 format for ``ResourceRecords`` . For information about the format of values for each record type, see `Supported DNS Resource Record Types <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html>`_ in the *Amazon Route 53 Developer Guide* .

        Note the following:

        - You can specify more than one value for all record types except CNAME and SOA.
        - The maximum length of a value is 4000 characters.
        - If you're creating an alias record, omit ``ResourceRecords`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-resourcerecords
        '''
        result = self._values.get("resource_records")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''*Resource record sets that have a routing policy other than simple:* An identifier that differentiates among multiple resource record sets that have the same combination of name and type, such as multiple weighted resource record sets named acme.example.com that have a type of A. In a group of resource record sets that have the same name and type, the value of ``SetIdentifier`` must be unique for each resource record set.

        For information about routing policies, see `Choosing a Routing Policy <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy.html>`_ in the *Amazon Route 53 Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-setidentifier
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[builtins.str]:
        '''The resource record cache time to live (TTL), in seconds. Note the following:.

        - If you're creating or updating an alias resource record set, omit ``TTL`` . Amazon Route 53 uses the value of ``TTL`` for the alias target.
        - If you're associating this resource record set with a health check (if you're adding a ``HealthCheckId`` element), we recommend that you specify a ``TTL`` of 60 seconds or less so clients respond quickly to changes in health status.
        - All of the resource record sets in a group of weighted resource record sets must have the same value for ``TTL`` .
        - If a group of weighted resource record sets includes one or more weighted alias resource record sets for which the alias target is an ELB load balancer, we recommend that you specify a ``TTL`` of 60 seconds for all of the non-alias weighted resource record sets that have the same name and type. Values other than 60 seconds (the TTL for load balancers) will change the effect of the values that you specify for ``Weight`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-ttl
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''*Weighted resource record sets only:* Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. Note the following:

        - You must specify a value for the ``Weight`` element for every weighted resource record set.
        - You can only specify one ``ResourceRecord`` per weighted resource record set.
        - You can't create latency, failover, or geolocation resource record sets that have the same values for the ``Name`` and ``Type`` elements as weighted resource record sets.
        - You can create a maximum of 100 weighted resource record sets that have the same values for the ``Name`` and ``Type`` elements.
        - For weighted (but not weighted alias) resource record sets, if you set ``Weight`` to ``0`` for a resource record set, Route 53 never responds to queries with the applicable value for that resource record set. However, if you set ``Weight`` to ``0`` for all resource record sets that have the same combination of DNS name and type, traffic is routed to all resources with equal probability.

        The effect of setting ``Weight`` to ``0`` is different when you associate health checks with weighted resource record sets. For more information, see `Options for Configuring Route 53 Active-Active and Active-Passive Failover <https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-failover-configuring-options.html>`_ in the *Amazon Route 53 Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-weight
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnRecordSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CommonHostedZoneProps",
    jsii_struct_bases=[],
    name_mapping={
        "zone_name": "zoneName",
        "add_trailing_dot": "addTrailingDot",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
    },
)
class CommonHostedZoneProps:
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Common properties to create a Route 53 hosted zone.

        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            common_hosted_zone_props = route53.CommonHostedZoneProps(
                zone_name="zoneName",
            
                # the properties below are optional
                add_trailing_dot=False,
                comment="comment",
                query_logs_log_group_arn="queryLogsLogGroupArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3c0a60680828ad59f14d241729df78a8969a23a13155e2327837897bb4545149)
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
            check_type(argname="argument add_trailing_dot", value=add_trailing_dot, expected_type=type_hints["add_trailing_dot"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument query_logs_log_group_arn", value=query_logs_log_group_arn, expected_type=type_hints["query_logs_log_group_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone_name": zone_name,
        }
        if add_trailing_dot is not None:
            self._values["add_trailing_dot"] = add_trailing_dot
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn

    @builtins.property
    def zone_name(self) -> builtins.str:
        '''The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.
        '''
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_trailing_dot(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a trailing dot to the zone name.

        :default: true
        '''
        result = self._values.get("add_trailing_dot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments that you want to include about the hosted zone.

        :default: none
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled
        '''
        result = self._values.get("query_logs_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CommonHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_route53.Continent")
class Continent(enum.Enum):
    '''Continents for geolocation routing.

    :exampleMetadata: infused

    Example::

        # my_zone: route53.HostedZone
        
        
        # continent
        route53.ARecord(self, "ARecordGeoLocationContinent",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.0", "5.6.7.0"),
            geo_location=route53.GeoLocation.continent(route53.Continent.EUROPE)
        )
        
        # country
        route53.ARecord(self, "ARecordGeoLocationCountry",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.1", "5.6.7.1"),
            geo_location=route53.GeoLocation.country("DE")
        )
        
        # subdivision
        route53.ARecord(self, "ARecordGeoLocationSubDividion",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.2", "5.6.7.2"),
            geo_location=route53.GeoLocation.subdivision("WA")
        )
        
        # default (wildcard record if no specific record is found)
        route53.ARecord(self, "ARecordGeoLocationDefault",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.3", "5.6.7.3"),
            geo_location=route53.GeoLocation.default()
        )
    '''

    AFRICA = "AFRICA"
    '''Africa.'''
    ANTARCTICA = "ANTARCTICA"
    '''Antarctica.'''
    ASIA = "ASIA"
    '''Asia.'''
    EUROPE = "EUROPE"
    '''Europe.'''
    OCEANIA = "OCEANIA"
    '''Oceania.'''
    NORTH_AMERICA = "NORTH_AMERICA"
    '''North America.'''
    SOUTH_AMERICA = "SOUTH_AMERICA"
    '''South America.'''


class CrossAccountZoneDelegationRecord(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CrossAccountZoneDelegationRecord",
):
    '''A Cross Account Zone Delegation record.

    :exampleMetadata: infused

    Example::

        sub_zone = route53.PublicHostedZone(self, "SubZone",
            zone_name="sub.someexample.com"
        )
        
        # import the delegation role by constructing the roleArn
        delegation_role_arn = Stack.of(self).format_arn(
            region="",  # IAM is global in each partition
            service="iam",
            account="parent-account-id",
            resource="role",
            resource_name="MyDelegationRole"
        )
        delegation_role = iam.Role.from_role_arn(self, "DelegationRole", delegation_role_arn)
        
        # create the record
        route53.CrossAccountZoneDelegationRecord(self, "delegate",
            delegated_zone=sub_zone,
            parent_hosted_zone_name="someexample.com",  # or you can use parentHostedZoneId
            delegation_role=delegation_role
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        delegated_zone: "IHostedZone",
        delegation_role: _IRole_235f5d8e,
        assume_role_region: typing.Optional[builtins.str] = None,
        parent_hosted_zone_id: typing.Optional[builtins.str] = None,
        parent_hosted_zone_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param delegated_zone: The zone to be delegated.
        :param delegation_role: The delegation role in the parent account.
        :param assume_role_region: Region from which to obtain temporary credentials. Default: - the Route53 signing region in the current partition
        :param parent_hosted_zone_id: The hosted zone id in the parent account. Default: - no zone id
        :param parent_hosted_zone_name: The hosted zone name in the parent account. Default: - no zone name
        :param removal_policy: The removal policy to apply to the record set. Default: RemovalPolicy.DESTROY
        :param ttl: The resource record cache time to live (TTL). Default: Duration.days(2)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f4115d484cd67a76fbe1e4ea37dbe01bb97e2d8816dda058f0ba904769173c46)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CrossAccountZoneDelegationRecordProps(
            delegated_zone=delegated_zone,
            delegation_role=delegation_role,
            assume_role_region=assume_role_region,
            parent_hosted_zone_id=parent_hosted_zone_id,
            parent_hosted_zone_name=parent_hosted_zone_name,
            removal_policy=removal_policy,
            ttl=ttl,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CrossAccountZoneDelegationRecordProps",
    jsii_struct_bases=[],
    name_mapping={
        "delegated_zone": "delegatedZone",
        "delegation_role": "delegationRole",
        "assume_role_region": "assumeRoleRegion",
        "parent_hosted_zone_id": "parentHostedZoneId",
        "parent_hosted_zone_name": "parentHostedZoneName",
        "removal_policy": "removalPolicy",
        "ttl": "ttl",
    },
)
class CrossAccountZoneDelegationRecordProps:
    def __init__(
        self,
        *,
        delegated_zone: "IHostedZone",
        delegation_role: _IRole_235f5d8e,
        assume_role_region: typing.Optional[builtins.str] = None,
        parent_hosted_zone_id: typing.Optional[builtins.str] = None,
        parent_hosted_zone_name: typing.Optional[builtins.str] = None,
        removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Construction properties for a CrossAccountZoneDelegationRecord.

        :param delegated_zone: The zone to be delegated.
        :param delegation_role: The delegation role in the parent account.
        :param assume_role_region: Region from which to obtain temporary credentials. Default: - the Route53 signing region in the current partition
        :param parent_hosted_zone_id: The hosted zone id in the parent account. Default: - no zone id
        :param parent_hosted_zone_name: The hosted zone name in the parent account. Default: - no zone name
        :param removal_policy: The removal policy to apply to the record set. Default: RemovalPolicy.DESTROY
        :param ttl: The resource record cache time to live (TTL). Default: Duration.days(2)

        :exampleMetadata: infused

        Example::

            sub_zone = route53.PublicHostedZone(self, "SubZone",
                zone_name="sub.someexample.com"
            )
            
            # import the delegation role by constructing the roleArn
            delegation_role_arn = Stack.of(self).format_arn(
                region="",  # IAM is global in each partition
                service="iam",
                account="parent-account-id",
                resource="role",
                resource_name="MyDelegationRole"
            )
            delegation_role = iam.Role.from_role_arn(self, "DelegationRole", delegation_role_arn)
            
            # create the record
            route53.CrossAccountZoneDelegationRecord(self, "delegate",
                delegated_zone=sub_zone,
                parent_hosted_zone_name="someexample.com",  # or you can use parentHostedZoneId
                delegation_role=delegation_role
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2f26cbe17fefc3bd3765d1fcc9084ddb3aa18526e669cad5ba4011ccbc2b3d7f)
            check_type(argname="argument delegated_zone", value=delegated_zone, expected_type=type_hints["delegated_zone"])
            check_type(argname="argument delegation_role", value=delegation_role, expected_type=type_hints["delegation_role"])
            check_type(argname="argument assume_role_region", value=assume_role_region, expected_type=type_hints["assume_role_region"])
            check_type(argname="argument parent_hosted_zone_id", value=parent_hosted_zone_id, expected_type=type_hints["parent_hosted_zone_id"])
            check_type(argname="argument parent_hosted_zone_name", value=parent_hosted_zone_name, expected_type=type_hints["parent_hosted_zone_name"])
            check_type(argname="argument removal_policy", value=removal_policy, expected_type=type_hints["removal_policy"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "delegated_zone": delegated_zone,
            "delegation_role": delegation_role,
        }
        if assume_role_region is not None:
            self._values["assume_role_region"] = assume_role_region
        if parent_hosted_zone_id is not None:
            self._values["parent_hosted_zone_id"] = parent_hosted_zone_id
        if parent_hosted_zone_name is not None:
            self._values["parent_hosted_zone_name"] = parent_hosted_zone_name
        if removal_policy is not None:
            self._values["removal_policy"] = removal_policy
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def delegated_zone(self) -> "IHostedZone":
        '''The zone to be delegated.'''
        result = self._values.get("delegated_zone")
        assert result is not None, "Required property 'delegated_zone' is missing"
        return typing.cast("IHostedZone", result)

    @builtins.property
    def delegation_role(self) -> _IRole_235f5d8e:
        '''The delegation role in the parent account.'''
        result = self._values.get("delegation_role")
        assert result is not None, "Required property 'delegation_role' is missing"
        return typing.cast(_IRole_235f5d8e, result)

    @builtins.property
    def assume_role_region(self) -> typing.Optional[builtins.str]:
        '''Region from which to obtain temporary credentials.

        :default: - the Route53 signing region in the current partition
        '''
        result = self._values.get("assume_role_region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_hosted_zone_id(self) -> typing.Optional[builtins.str]:
        '''The hosted zone id in the parent account.

        :default: - no zone id
        '''
        result = self._values.get("parent_hosted_zone_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parent_hosted_zone_name(self) -> typing.Optional[builtins.str]:
        '''The hosted zone name in the parent account.

        :default: - no zone name
        '''
        result = self._values.get("parent_hosted_zone_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def removal_policy(self) -> typing.Optional[_RemovalPolicy_9f93c814]:
        '''The removal policy to apply to the record set.

        :default: RemovalPolicy.DESTROY
        '''
        result = self._values.get("removal_policy")
        return typing.cast(typing.Optional[_RemovalPolicy_9f93c814], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.days(2)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CrossAccountZoneDelegationRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GeoLocation(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.GeoLocation",
):
    '''Routing based on geographical location.

    :exampleMetadata: infused

    Example::

        # my_zone: route53.HostedZone
        
        
        # continent
        route53.ARecord(self, "ARecordGeoLocationContinent",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.0", "5.6.7.0"),
            geo_location=route53.GeoLocation.continent(route53.Continent.EUROPE)
        )
        
        # country
        route53.ARecord(self, "ARecordGeoLocationCountry",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.1", "5.6.7.1"),
            geo_location=route53.GeoLocation.country("DE")
        )
        
        # subdivision
        route53.ARecord(self, "ARecordGeoLocationSubDividion",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.2", "5.6.7.2"),
            geo_location=route53.GeoLocation.subdivision("WA")
        )
        
        # default (wildcard record if no specific record is found)
        route53.ARecord(self, "ARecordGeoLocationDefault",
            zone=my_zone,
            target=route53.RecordTarget.from_ip_addresses("1.2.3.3", "5.6.7.3"),
            geo_location=route53.GeoLocation.default()
        )
    '''

    @jsii.member(jsii_name="continent")
    @builtins.classmethod
    def continent(cls, continent_code: Continent) -> "GeoLocation":
        '''Geolocation resource record based on continent code.

        :param continent_code: Continent.

        :return: Continent-based geolocation record
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__082626770a86bf939ef1cae8f42886e56e872994e6ff75c90019d66a2dbbbbbe)
            check_type(argname="argument continent_code", value=continent_code, expected_type=type_hints["continent_code"])
        return typing.cast("GeoLocation", jsii.sinvoke(cls, "continent", [continent_code]))

    @jsii.member(jsii_name="country")
    @builtins.classmethod
    def country(cls, country_code: builtins.str) -> "GeoLocation":
        '''Geolocation resource record based on country code.

        :param country_code: Two-letter, uppercase country code for the country. See ISO 3166-1-alpha-2 code on the *International Organization for Standardization* website

        :return: Country-based geolocation record

        :see: https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__634d2e960bf8ca83032f62602012c316f523f02ccdc11b960ac7a1818f6088f9)
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
        return typing.cast("GeoLocation", jsii.sinvoke(cls, "country", [country_code]))

    @jsii.member(jsii_name="default")
    @builtins.classmethod
    def default(cls) -> "GeoLocation":
        '''Default (wildcard) routing record if no specific geolocation record is found.

        :return: Wildcard routing record
        '''
        return typing.cast("GeoLocation", jsii.sinvoke(cls, "default", []))

    @jsii.member(jsii_name="subdivision")
    @builtins.classmethod
    def subdivision(
        cls,
        subdivision_code: builtins.str,
        country_code: typing.Optional[builtins.str] = None,
    ) -> "GeoLocation":
        '''Geolocation resource record based on subdivision code (e.g. state of the United States).

        :param subdivision_code: Code of the subdivision (e.g. state of the United States).
        :param country_code: Country code (ISO 3166-1-alpha-2) of this record, by default US (United States).

        :see: https://docs.aws.amazon.com/Route53/latest/APIReference/API_GeoLocation.html#Route53-Type-GeoLocation-SubdivisionCode
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13d57b34e60c4361c1d97c820e69f3a9c16ba208b123a261ee081931be34cf02)
            check_type(argname="argument subdivision_code", value=subdivision_code, expected_type=type_hints["subdivision_code"])
            check_type(argname="argument country_code", value=country_code, expected_type=type_hints["country_code"])
        return typing.cast("GeoLocation", jsii.sinvoke(cls, "subdivision", [subdivision_code, country_code]))

    @builtins.property
    @jsii.member(jsii_name="continentCode")
    def continent_code(self) -> typing.Optional[Continent]:
        return typing.cast(typing.Optional[Continent], jsii.get(self, "continentCode"))

    @builtins.property
    @jsii.member(jsii_name="countryCode")
    def country_code(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "countryCode"))

    @builtins.property
    @jsii.member(jsii_name="subdivisionCode")
    def subdivision_code(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "subdivisionCode"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.HostedZoneAttributes",
    jsii_struct_bases=[],
    name_mapping={"hosted_zone_id": "hostedZoneId", "zone_name": "zoneName"},
)
class HostedZoneAttributes:
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        zone_name: builtins.str,
    ) -> None:
        '''Reference to a hosted zone.

        :param hosted_zone_id: Identifier of the hosted zone.
        :param zone_name: Name of the hosted zone.

        :exampleMetadata: infused

        Example::

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
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e5fad1cc6999b94bd845480426db92d5bb3ac0208bca78f9cf984e5ce4ccd701)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "zone_name": zone_name,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''Identifier of the hosted zone.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_name(self) -> builtins.str:
        '''Name of the hosted zone.'''
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.HostedZoneProps",
    jsii_struct_bases=[CommonHostedZoneProps],
    name_mapping={
        "zone_name": "zoneName",
        "add_trailing_dot": "addTrailingDot",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
        "vpcs": "vpcs",
    },
)
class HostedZoneProps(CommonHostedZoneProps):
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
        vpcs: typing.Optional[typing.Sequence[_IVpc_f30d5663]] = None,
    ) -> None:
        '''Properties of a new hosted zone.

        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        :param vpcs: A VPC that you want to associate with this hosted zone. When you specify this property, a private hosted zone will be created. You can associate additional VPCs to this private zone using ``addVpc(vpc)``. Default: public (no VPCs associated)

        :exampleMetadata: infused

        Example::

            hosted_zone = route53.HostedZone(self, "MyHostedZone", zone_name="example.org")
            metric = cloudwatch.Metric(
                namespace="AWS/Route53",
                metric_name="DNSQueries",
                dimensions_map={
                    "HostedZoneId": hosted_zone.hosted_zone_id
                }
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f1711cf7af2ab26c7be8b7aad54fc7158d3e50d0205dd9b87989812878e88e96)
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
            check_type(argname="argument add_trailing_dot", value=add_trailing_dot, expected_type=type_hints["add_trailing_dot"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument query_logs_log_group_arn", value=query_logs_log_group_arn, expected_type=type_hints["query_logs_log_group_arn"])
            check_type(argname="argument vpcs", value=vpcs, expected_type=type_hints["vpcs"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone_name": zone_name,
        }
        if add_trailing_dot is not None:
            self._values["add_trailing_dot"] = add_trailing_dot
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn
        if vpcs is not None:
            self._values["vpcs"] = vpcs

    @builtins.property
    def zone_name(self) -> builtins.str:
        '''The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.
        '''
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_trailing_dot(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a trailing dot to the zone name.

        :default: true
        '''
        result = self._values.get("add_trailing_dot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments that you want to include about the hosted zone.

        :default: none
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled
        '''
        result = self._values.get("query_logs_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpcs(self) -> typing.Optional[typing.List[_IVpc_f30d5663]]:
        '''A VPC that you want to associate with this hosted zone.

        When you specify
        this property, a private hosted zone will be created.

        You can associate additional VPCs to this private zone using ``addVpc(vpc)``.

        :default: public (no VPCs associated)
        '''
        result = self._values.get("vpcs")
        return typing.cast(typing.Optional[typing.List[_IVpc_f30d5663]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.HostedZoneProviderProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "private_zone": "privateZone",
        "vpc_id": "vpcId",
    },
)
class HostedZoneProviderProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        private_zone: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Zone properties for looking up the Hosted Zone.

        :param domain_name: The zone domain e.g. example.com.
        :param private_zone: Whether the zone that is being looked up is a private hosted zone. Default: false
        :param vpc_id: Specifies the ID of the VPC associated with a private hosted zone. If a VPC ID is provided and privateZone is false, no results will be returned and an error will be raised Default: - No VPC ID

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
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__77dfce5cb4e026f34aa8dfde1dcd4aacac66aa9d7b2466bbb97ebb9db7b5de4c)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument private_zone", value=private_zone, expected_type=type_hints["private_zone"])
            check_type(argname="argument vpc_id", value=vpc_id, expected_type=type_hints["vpc_id"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
        }
        if private_zone is not None:
            self._values["private_zone"] = private_zone
        if vpc_id is not None:
            self._values["vpc_id"] = vpc_id

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The zone domain e.g. example.com.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def private_zone(self) -> typing.Optional[builtins.bool]:
        '''Whether the zone that is being looked up is a private hosted zone.

        :default: false
        '''
        result = self._values.get("private_zone")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def vpc_id(self) -> typing.Optional[builtins.str]:
        '''Specifies the ID of the VPC associated with a private hosted zone.

        If a VPC ID is provided and privateZone is false, no results will be returned
        and an error will be raised

        :default: - No VPC ID
        '''
        result = self._values.get("vpc_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "HostedZoneProviderProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.interface(jsii_type="aws-cdk-lib.aws_route53.IAliasRecordTarget")
class IAliasRecordTarget(typing_extensions.Protocol):
    '''Classes that are valid alias record targets, like CloudFront distributions and load balancers, should implement this interface.'''

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        record: "IRecordSet",
        zone: typing.Optional["IHostedZone"] = None,
    ) -> AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param record: -
        :param zone: -
        '''
        ...


class _IAliasRecordTargetProxy:
    '''Classes that are valid alias record targets, like CloudFront distributions and load balancers, should implement this interface.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_route53.IAliasRecordTarget"

    @jsii.member(jsii_name="bind")
    def bind(
        self,
        record: "IRecordSet",
        zone: typing.Optional["IHostedZone"] = None,
    ) -> AliasRecordTargetConfig:
        '''Return hosted zone ID and DNS name, usable for Route53 alias targets.

        :param record: -
        :param zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__162b54c0ae9f493edc12c5cba6aa323333c184d03d9332edaab8e4f75c7f74cd)
            check_type(argname="argument record", value=record, expected_type=type_hints["record"])
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
        return typing.cast(AliasRecordTargetConfig, jsii.invoke(self, "bind", [record, zone]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IAliasRecordTarget).__jsii_proxy_class__ = lambda : _IAliasRecordTargetProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_route53.IHostedZone")
class IHostedZone(_IResource_c80c4260, typing_extensions.Protocol):
    '''Imported or created hosted zone.'''

    @builtins.property
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        '''ARN of this hosted zone, such as arn:${Partition}:route53:::hostedzone/${Id}.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        '''ID of this hosted zone, such as "Z23ABC4XYZL05B".

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> builtins.str:
        '''FQDN of this hosted zone.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="grantDelegation")
    def grant_delegation(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to add delegation records to this zone.

        :param grantee: -
        '''
        ...


class _IHostedZoneProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Imported or created hosted zone.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_route53.IHostedZone"

    @builtins.property
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        '''ARN of this hosted zone, such as arn:${Partition}:route53:::hostedzone/${Id}.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneArn"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        '''ID of this hosted zone, such as "Z23ABC4XYZL05B".

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> builtins.str:
        '''FQDN of this hosted zone.'''
        return typing.cast(builtins.str, jsii.get(self, "zoneName"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.

        :attribute: true
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostedZoneNameServers"))

    @jsii.member(jsii_name="grantDelegation")
    def grant_delegation(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to add delegation records to this zone.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97ae48bcbfd92ef96c96db6d1d972ddd9b889f01bba1ab2a3819d9faa9eb4a18)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDelegation", [grantee]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IHostedZone).__jsii_proxy_class__ = lambda : _IHostedZoneProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_route53.IKeySigningKey")
class IKeySigningKey(_IResource_c80c4260, typing_extensions.Protocol):
    '''A Key Signing Key for a Route 53 Hosted Zone.'''

    @builtins.property
    @jsii.member(jsii_name="hostedZone")
    def hosted_zone(self) -> IHostedZone:
        '''The hosted zone that the key signing key signs.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyId")
    def key_signing_key_id(self) -> builtins.str:
        '''The ID of the key signing key, derived from the hosted zone ID and its name.

        :attribute: true
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyName")
    def key_signing_key_name(self) -> builtins.str:
        '''The name of the key signing key.

        :attribute: true
        '''
        ...


class _IKeySigningKeyProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A Key Signing Key for a Route 53 Hosted Zone.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_route53.IKeySigningKey"

    @builtins.property
    @jsii.member(jsii_name="hostedZone")
    def hosted_zone(self) -> IHostedZone:
        '''The hosted zone that the key signing key signs.

        :attribute: true
        '''
        return typing.cast(IHostedZone, jsii.get(self, "hostedZone"))

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyId")
    def key_signing_key_id(self) -> builtins.str:
        '''The ID of the key signing key, derived from the hosted zone ID and its name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "keySigningKeyId"))

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyName")
    def key_signing_key_name(self) -> builtins.str:
        '''The name of the key signing key.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "keySigningKeyName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IKeySigningKey).__jsii_proxy_class__ = lambda : _IKeySigningKeyProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_route53.IPrivateHostedZone")
class IPrivateHostedZone(IHostedZone, typing_extensions.Protocol):
    '''Represents a Route 53 private hosted zone.'''

    pass


class _IPrivateHostedZoneProxy(
    jsii.proxy_for(IHostedZone), # type: ignore[misc]
):
    '''Represents a Route 53 private hosted zone.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_route53.IPrivateHostedZone"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPrivateHostedZone).__jsii_proxy_class__ = lambda : _IPrivateHostedZoneProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_route53.IPublicHostedZone")
class IPublicHostedZone(IHostedZone, typing_extensions.Protocol):
    '''Represents a Route 53 public hosted zone.'''

    pass


class _IPublicHostedZoneProxy(
    jsii.proxy_for(IHostedZone), # type: ignore[misc]
):
    '''Represents a Route 53 public hosted zone.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_route53.IPublicHostedZone"
    pass

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IPublicHostedZone).__jsii_proxy_class__ = lambda : _IPublicHostedZoneProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_route53.IRecordSet")
class IRecordSet(_IResource_c80c4260, typing_extensions.Protocol):
    '''A record set.'''

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name of the record.'''
        ...


class _IRecordSetProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A record set.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_route53.IRecordSet"

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name of the record.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IRecordSet).__jsii_proxy_class__ = lambda : _IRecordSetProxy


@jsii.implements(IKeySigningKey)
class KeySigningKey(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.KeySigningKey",
):
    '''A Key Signing Key for a Route 53 Hosted Zone.

    :resource: AWS::Route53::KeySigningKey
    :exampleMetadata: infused

    Example::

        # hosted_zone: route53.HostedZone
        # kms_key: kms.Key
        
        route53.KeySigningKey(self, "KeySigningKey",
            hosted_zone=hosted_zone,
            kms_key=kms_key,
            key_signing_key_name="ksk",
            status=route53.KeySigningKeyStatus.ACTIVE
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone: IHostedZone,
        kms_key: _IKey_5f11635f,
        key_signing_key_name: typing.Optional[builtins.str] = None,
        status: typing.Optional["KeySigningKeyStatus"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param hosted_zone: The hosted zone that this key will be used to sign.
        :param kms_key: The customer-managed KMS key that that will be used to sign the records. The KMS Key must be unique for each KSK within a hosted zone. Additionally, the KMS key must be an asymetric customer-managed key using the ECC_NIST_P256 algorithm.
        :param key_signing_key_name: The name for the key signing key. This name must be unique within a hosted zone. Default: an autogenerated name
        :param status: The status of the key signing key. Default: ACTIVE
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__63b944f82a919a5a1fc9b8c1ec885ffe1d509c5cec2bb324d9b5ed7df171b437)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = KeySigningKeyProps(
            hosted_zone=hosted_zone,
            kms_key=kms_key,
            key_signing_key_name=key_signing_key_name,
            status=status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromKeySigningKeyAttributes")
    @builtins.classmethod
    def from_key_signing_key_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone: IHostedZone,
        key_signing_key_name: builtins.str,
    ) -> IKeySigningKey:
        '''Imports a key signing key from its attributes.

        :param scope: -
        :param id: -
        :param hosted_zone: The hosted zone that the key signing key signs.
        :param key_signing_key_name: The name of the key signing key.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9aae6d3147d941495289a363f03a080316f20c479e0fa8646cf10ec995d1635a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = KeySigningKeyAttributes(
            hosted_zone=hosted_zone, key_signing_key_name=key_signing_key_name
        )

        return typing.cast(IKeySigningKey, jsii.sinvoke(cls, "fromKeySigningKeyAttributes", [scope, id, attrs]))

    @builtins.property
    @jsii.member(jsii_name="hostedZone")
    def hosted_zone(self) -> IHostedZone:
        '''The hosted zone that the key signing key signs.'''
        return typing.cast(IHostedZone, jsii.get(self, "hostedZone"))

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyId")
    def key_signing_key_id(self) -> builtins.str:
        '''The ID of the key signing key, derived from the hosted zone ID and its name.'''
        return typing.cast(builtins.str, jsii.get(self, "keySigningKeyId"))

    @builtins.property
    @jsii.member(jsii_name="keySigningKeyName")
    def key_signing_key_name(self) -> builtins.str:
        '''The name of the key signing key.'''
        return typing.cast(builtins.str, jsii.get(self, "keySigningKeyName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.KeySigningKeyAttributes",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone": "hostedZone",
        "key_signing_key_name": "keySigningKeyName",
    },
)
class KeySigningKeyAttributes:
    def __init__(
        self,
        *,
        hosted_zone: IHostedZone,
        key_signing_key_name: builtins.str,
    ) -> None:
        '''The attributes of a key signing key.

        :param hosted_zone: The hosted zone that the key signing key signs.
        :param key_signing_key_name: The name of the key signing key.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            # hosted_zone: route53.HostedZone
            
            key_signing_key_attributes = route53.KeySigningKeyAttributes(
                hosted_zone=hosted_zone,
                key_signing_key_name="keySigningKeyName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a1262fd4a880b25e9ef115da3b6b790a7b24acf9d121372595ab3087a5442d2)
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
            check_type(argname="argument key_signing_key_name", value=key_signing_key_name, expected_type=type_hints["key_signing_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone": hosted_zone,
            "key_signing_key_name": key_signing_key_name,
        }

    @builtins.property
    def hosted_zone(self) -> IHostedZone:
        '''The hosted zone that the key signing key signs.

        :attribute: true
        '''
        result = self._values.get("hosted_zone")
        assert result is not None, "Required property 'hosted_zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def key_signing_key_name(self) -> builtins.str:
        '''The name of the key signing key.

        :attribute: true
        '''
        result = self._values.get("key_signing_key_name")
        assert result is not None, "Required property 'key_signing_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeySigningKeyAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.KeySigningKeyProps",
    jsii_struct_bases=[],
    name_mapping={
        "hosted_zone": "hostedZone",
        "kms_key": "kmsKey",
        "key_signing_key_name": "keySigningKeyName",
        "status": "status",
    },
)
class KeySigningKeyProps:
    def __init__(
        self,
        *,
        hosted_zone: IHostedZone,
        kms_key: _IKey_5f11635f,
        key_signing_key_name: typing.Optional[builtins.str] = None,
        status: typing.Optional["KeySigningKeyStatus"] = None,
    ) -> None:
        '''Properties for constructing a Key Signing Key.

        :param hosted_zone: The hosted zone that this key will be used to sign.
        :param kms_key: The customer-managed KMS key that that will be used to sign the records. The KMS Key must be unique for each KSK within a hosted zone. Additionally, the KMS key must be an asymetric customer-managed key using the ECC_NIST_P256 algorithm.
        :param key_signing_key_name: The name for the key signing key. This name must be unique within a hosted zone. Default: an autogenerated name
        :param status: The status of the key signing key. Default: ACTIVE

        :exampleMetadata: infused

        Example::

            # hosted_zone: route53.HostedZone
            # kms_key: kms.Key
            
            route53.KeySigningKey(self, "KeySigningKey",
                hosted_zone=hosted_zone,
                kms_key=kms_key,
                key_signing_key_name="ksk",
                status=route53.KeySigningKeyStatus.ACTIVE
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3e92b54737c8cb2969b649108716a37fd8e380a8e41cfefef3229c1d92acdf40)
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument key_signing_key_name", value=key_signing_key_name, expected_type=type_hints["key_signing_key_name"])
            check_type(argname="argument status", value=status, expected_type=type_hints["status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone": hosted_zone,
            "kms_key": kms_key,
        }
        if key_signing_key_name is not None:
            self._values["key_signing_key_name"] = key_signing_key_name
        if status is not None:
            self._values["status"] = status

    @builtins.property
    def hosted_zone(self) -> IHostedZone:
        '''The hosted zone that this key will be used to sign.'''
        result = self._values.get("hosted_zone")
        assert result is not None, "Required property 'hosted_zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def kms_key(self) -> _IKey_5f11635f:
        '''The customer-managed KMS key that that will be used to sign the records.

        The KMS Key must be unique for each KSK within a hosted zone. Additionally, the
        KMS key must be an asymetric customer-managed key using the ECC_NIST_P256 algorithm.

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-cmk-requirements.html
        '''
        result = self._values.get("kms_key")
        assert result is not None, "Required property 'kms_key' is missing"
        return typing.cast(_IKey_5f11635f, result)

    @builtins.property
    def key_signing_key_name(self) -> typing.Optional[builtins.str]:
        '''The name for the key signing key.

        This name must be unique within a hosted zone.

        :default: an autogenerated name
        '''
        result = self._values.get("key_signing_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def status(self) -> typing.Optional["KeySigningKeyStatus"]:
        '''The status of the key signing key.

        :default: ACTIVE
        '''
        result = self._values.get("status")
        return typing.cast(typing.Optional["KeySigningKeyStatus"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "KeySigningKeyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_route53.KeySigningKeyStatus")
class KeySigningKeyStatus(enum.Enum):
    '''The status for a Key Signing Key.

    :exampleMetadata: infused

    Example::

        # hosted_zone: route53.HostedZone
        # kms_key: kms.Key
        
        route53.KeySigningKey(self, "KeySigningKey",
            hosted_zone=hosted_zone,
            kms_key=kms_key,
            key_signing_key_name="ksk",
            status=route53.KeySigningKeyStatus.ACTIVE
        )
    '''

    ACTIVE = "ACTIVE"
    '''The KSK is being used for signing.'''
    INACTIVE = "INACTIVE"
    '''The KSK is not being used for signing.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.MxRecordValue",
    jsii_struct_bases=[],
    name_mapping={"host_name": "hostName", "priority": "priority"},
)
class MxRecordValue:
    def __init__(self, *, host_name: builtins.str, priority: jsii.Number) -> None:
        '''Properties for a MX record value.

        :param host_name: The mail server host name.
        :param priority: The priority.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            mx_record_value = route53.MxRecordValue(
                host_name="hostName",
                priority=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2600b3ca2027fe7d531738c20a112cef3282c7ef114758a51ee3863608c7aa72)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_name": host_name,
            "priority": priority,
        }

    @builtins.property
    def host_name(self) -> builtins.str:
        '''The mail server host name.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MxRecordValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.PrivateHostedZoneProps",
    jsii_struct_bases=[CommonHostedZoneProps],
    name_mapping={
        "zone_name": "zoneName",
        "add_trailing_dot": "addTrailingDot",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
        "vpc": "vpc",
    },
)
class PrivateHostedZoneProps(CommonHostedZoneProps):
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
        vpc: _IVpc_f30d5663,
    ) -> None:
        '''Properties to create a Route 53 private hosted zone.

        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        :param vpc: A VPC that you want to associate with this hosted zone. Private hosted zones must be associated with at least one VPC. You can associated additional VPCs using ``addVpc(vpc)``.

        :exampleMetadata: infused

        Example::

            # vpc: ec2.Vpc
            
            
            zone = route53.PrivateHostedZone(self, "HostedZone",
                zone_name="fully.qualified.domain.com",
                vpc=vpc
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3dc8529d9382b27a0613e5ea30e125e3af07550dc23754412bd1f99368cfc62d)
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
            check_type(argname="argument add_trailing_dot", value=add_trailing_dot, expected_type=type_hints["add_trailing_dot"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument query_logs_log_group_arn", value=query_logs_log_group_arn, expected_type=type_hints["query_logs_log_group_arn"])
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone_name": zone_name,
            "vpc": vpc,
        }
        if add_trailing_dot is not None:
            self._values["add_trailing_dot"] = add_trailing_dot
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn

    @builtins.property
    def zone_name(self) -> builtins.str:
        '''The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.
        '''
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_trailing_dot(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a trailing dot to the zone name.

        :default: true
        '''
        result = self._values.get("add_trailing_dot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments that you want to include about the hosted zone.

        :default: none
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled
        '''
        result = self._values.get("query_logs_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def vpc(self) -> _IVpc_f30d5663:
        '''A VPC that you want to associate with this hosted zone.

        Private hosted zones must be associated with at least one VPC. You can
        associated additional VPCs using ``addVpc(vpc)``.
        '''
        result = self._values.get("vpc")
        assert result is not None, "Required property 'vpc' is missing"
        return typing.cast(_IVpc_f30d5663, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PrivateHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.PublicHostedZoneAttributes",
    jsii_struct_bases=[HostedZoneAttributes],
    name_mapping={"hosted_zone_id": "hostedZoneId", "zone_name": "zoneName"},
)
class PublicHostedZoneAttributes(HostedZoneAttributes):
    def __init__(
        self,
        *,
        hosted_zone_id: builtins.str,
        zone_name: builtins.str,
    ) -> None:
        '''Reference to a public hosted zone.

        :param hosted_zone_id: Identifier of the hosted zone.
        :param zone_name: Name of the hosted zone.

        :exampleMetadata: infused

        Example::

            zone_from_attributes = route53.PublicHostedZone.from_public_hosted_zone_attributes(self, "MyZone",
                zone_name="example.com",
                hosted_zone_id="ZOJJZC49E0EPZ"
            )
            
            # Does not know zoneName
            zone_from_id = route53.PublicHostedZone.from_public_hosted_zone_id(self, "MyZone", "ZOJJZC49E0EPZ")
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7cb1c7902828774b44c85c0a2b07314a2458b9752803df59926e9e7cd9f9b4f4)
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "hosted_zone_id": hosted_zone_id,
            "zone_name": zone_name,
        }

    @builtins.property
    def hosted_zone_id(self) -> builtins.str:
        '''Identifier of the hosted zone.'''
        result = self._values.get("hosted_zone_id")
        assert result is not None, "Required property 'hosted_zone_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def zone_name(self) -> builtins.str:
        '''Name of the hosted zone.'''
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicHostedZoneAttributes(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.PublicHostedZoneProps",
    jsii_struct_bases=[CommonHostedZoneProps],
    name_mapping={
        "zone_name": "zoneName",
        "add_trailing_dot": "addTrailingDot",
        "comment": "comment",
        "query_logs_log_group_arn": "queryLogsLogGroupArn",
        "caa_amazon": "caaAmazon",
        "cross_account_zone_delegation_principal": "crossAccountZoneDelegationPrincipal",
        "cross_account_zone_delegation_role_name": "crossAccountZoneDelegationRoleName",
    },
)
class PublicHostedZoneProps(CommonHostedZoneProps):
    def __init__(
        self,
        *,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
        caa_amazon: typing.Optional[builtins.bool] = None,
        cross_account_zone_delegation_principal: typing.Optional[_IPrincipal_539bb2fd] = None,
        cross_account_zone_delegation_role_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a PublicHostedZone.

        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        :param caa_amazon: Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only. Default: false
        :param cross_account_zone_delegation_principal: (deprecated) A principal which is trusted to assume a role for zone delegation. If supplied, this will create a Role in the same account as the Hosted Zone, which can be assumed by the ``CrossAccountZoneDelegationRecord`` to create a delegation record to a zone in a different account. Be sure to indicate the account(s) that you trust to create delegation records, using either ``iam.AccountPrincipal`` or ``iam.OrganizationPrincipal``. If you are planning to use ``iam.ServicePrincipal``s here, be sure to include region-specific service principals for every opt-in region you are going to be delegating to; or don't use this feature and create separate roles with appropriate permissions for every opt-in region instead. Default: - No delegation configuration
        :param cross_account_zone_delegation_role_name: (deprecated) The name of the role created for cross account delegation. Default: - A role name is generated automatically

        :exampleMetadata: infused

        Example::

            parent_zone = route53.PublicHostedZone(self, "HostedZone",
                zone_name="someexample.com"
            )
            cross_account_role = iam.Role(self, "CrossAccountRole",
                # The role name must be predictable
                role_name="MyDelegationRole",
                # The other account
                assumed_by=iam.AccountPrincipal("12345678901"),
                # You can scope down this role policy to be least privileged.
                # If you want the other account to be able to manage specific records,
                # you can scope down by resource and/or normalized record names
                inline_policies={
                    "cross_account_policy": iam.PolicyDocument(
                        statements=[
                            iam.PolicyStatement(
                                sid="ListHostedZonesByName",
                                effect=iam.Effect.ALLOW,
                                actions=["route53:ListHostedZonesByName"],
                                resources=["*"]
                            ),
                            iam.PolicyStatement(
                                sid="GetHostedZoneAndChangeResourceRecordSets",
                                effect=iam.Effect.ALLOW,
                                actions=["route53:GetHostedZone", "route53:ChangeResourceRecordSets"],
                                # This example assumes the RecordSet subdomain.somexample.com
                                # is contained in the HostedZone
                                resources=["arn:aws:route53:::hostedzone/HZID00000000000000000"],
                                conditions={
                                    "ForAllValues:StringLike": {
                                        "route53:ChangeResourceRecordSetsNormalizedRecordNames": ["subdomain.someexample.com"
                                        ]
                                    }
                                }
                            )
                        ]
                    )
                }
            )
            parent_zone.grant_delegation(cross_account_role)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b51e553dd18a8a033ac24f091492db4b2bc8c672421ced82613174be3995dcdf)
            check_type(argname="argument zone_name", value=zone_name, expected_type=type_hints["zone_name"])
            check_type(argname="argument add_trailing_dot", value=add_trailing_dot, expected_type=type_hints["add_trailing_dot"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument query_logs_log_group_arn", value=query_logs_log_group_arn, expected_type=type_hints["query_logs_log_group_arn"])
            check_type(argname="argument caa_amazon", value=caa_amazon, expected_type=type_hints["caa_amazon"])
            check_type(argname="argument cross_account_zone_delegation_principal", value=cross_account_zone_delegation_principal, expected_type=type_hints["cross_account_zone_delegation_principal"])
            check_type(argname="argument cross_account_zone_delegation_role_name", value=cross_account_zone_delegation_role_name, expected_type=type_hints["cross_account_zone_delegation_role_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone_name": zone_name,
        }
        if add_trailing_dot is not None:
            self._values["add_trailing_dot"] = add_trailing_dot
        if comment is not None:
            self._values["comment"] = comment
        if query_logs_log_group_arn is not None:
            self._values["query_logs_log_group_arn"] = query_logs_log_group_arn
        if caa_amazon is not None:
            self._values["caa_amazon"] = caa_amazon
        if cross_account_zone_delegation_principal is not None:
            self._values["cross_account_zone_delegation_principal"] = cross_account_zone_delegation_principal
        if cross_account_zone_delegation_role_name is not None:
            self._values["cross_account_zone_delegation_role_name"] = cross_account_zone_delegation_role_name

    @builtins.property
    def zone_name(self) -> builtins.str:
        '''The name of the domain.

        For resource record types that include a domain
        name, specify a fully qualified domain name.
        '''
        result = self._values.get("zone_name")
        assert result is not None, "Required property 'zone_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def add_trailing_dot(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a trailing dot to the zone name.

        :default: true
        '''
        result = self._values.get("add_trailing_dot")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''Any comments that you want to include about the hosted zone.

        :default: none
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_logs_log_group_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to.

        :default: disabled
        '''
        result = self._values.get("query_logs_log_group_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def caa_amazon(self) -> typing.Optional[builtins.bool]:
        '''Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only.

        :default: false
        '''
        result = self._values.get("caa_amazon")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def cross_account_zone_delegation_principal(
        self,
    ) -> typing.Optional[_IPrincipal_539bb2fd]:
        '''(deprecated) A principal which is trusted to assume a role for zone delegation.

        If supplied, this will create a Role in the same account as the Hosted
        Zone, which can be assumed by the ``CrossAccountZoneDelegationRecord`` to
        create a delegation record to a zone in a different account.

        Be sure to indicate the account(s) that you trust to create delegation
        records, using either ``iam.AccountPrincipal`` or ``iam.OrganizationPrincipal``.

        If you are planning to use ``iam.ServicePrincipal``s here, be sure to include
        region-specific service principals for every opt-in region you are going to
        be delegating to; or don't use this feature and create separate roles
        with appropriate permissions for every opt-in region instead.

        :default: - No delegation configuration

        :deprecated: Create the Role yourself and call ``hostedZone.grantDelegation()``.

        :stability: deprecated
        '''
        result = self._values.get("cross_account_zone_delegation_principal")
        return typing.cast(typing.Optional[_IPrincipal_539bb2fd], result)

    @builtins.property
    def cross_account_zone_delegation_role_name(self) -> typing.Optional[builtins.str]:
        '''(deprecated) The name of the role created for cross account delegation.

        :default: - A role name is generated automatically

        :deprecated: Create the Role yourself and call ``hostedZone.grantDelegation()``.

        :stability: deprecated
        '''
        result = self._values.get("cross_account_zone_delegation_role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "PublicHostedZoneProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IRecordSet)
class RecordSet(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.RecordSet",
):
    '''A record set.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_route53 as route53
        
        # geo_location: route53.GeoLocation
        # hosted_zone: route53.HostedZone
        # record_target: route53.RecordTarget
        
        record_set = route53.RecordSet(self, "MyRecordSet",
            record_type=route53.RecordType.A,
            target=record_target,
            zone=hosted_zone,
        
            # the properties below are optional
            comment="comment",
            delete_existing=False,
            geo_location=geo_location,
            multi_value_answer=False,
            record_name="recordName",
            region="region",
            set_identifier="setIdentifier",
            ttl=cdk.Duration.minutes(30),
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        record_type: "RecordType",
        target: "RecordTarget",
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param record_type: The record type.
        :param target: The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b92f4bc0484ad6fe8cce3c7e37b4ee3cd051b8f325d16efd23f92476703d09ac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = RecordSetProps(
            record_type=record_type,
            target=target,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name of the record.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.RecordSetOptions",
    jsii_struct_bases=[],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
    },
)
class RecordSetOptions:
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Options for a RecordSet.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            
            record_set_options = route53.RecordSetOptions(
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c44f39638a001e90bc1175667e4764c4cbde27cade202d52a4f4d87246c57781)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.RecordSetProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "record_type": "recordType",
        "target": "target",
    },
)
class RecordSetProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        record_type: "RecordType",
        target: "RecordTarget",
    ) -> None:
        '''Construction properties for a RecordSet.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param record_type: The record type.
        :param target: The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            # record_target: route53.RecordTarget
            
            record_set_props = route53.RecordSetProps(
                record_type=route53.RecordType.A,
                target=record_target,
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__038200686c47ef30f81bc5289a6235e766372281295129670053b793d545dfca)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument record_type", value=record_type, expected_type=type_hints["record_type"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "record_type": record_type,
            "target": target,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def record_type(self) -> "RecordType":
        '''The record type.'''
        result = self._values.get("record_type")
        assert result is not None, "Required property 'record_type' is missing"
        return typing.cast("RecordType", result)

    @builtins.property
    def target(self) -> "RecordTarget":
        '''The target for this record, either ``RecordTarget.fromValues()`` or ``RecordTarget.fromAlias()``.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast("RecordTarget", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "RecordSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class RecordTarget(
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.RecordTarget",
):
    '''Type union for a record that accepts multiple types of target.

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

    def __init__(
        self,
        values: typing.Optional[typing.Sequence[builtins.str]] = None,
        alias_target: typing.Optional[IAliasRecordTarget] = None,
    ) -> None:
        '''
        :param values: correspond with the chosen record type (e.g. for 'A' Type, specify one or more IP addresses).
        :param alias_target: alias for targets such as CloudFront distribution to route traffic to.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93edac882a461453a0fceb6451d524a95c372910790d1fb9ddc60080e15f3ff7)
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            check_type(argname="argument alias_target", value=alias_target, expected_type=type_hints["alias_target"])
        jsii.create(self.__class__, self, [values, alias_target])

    @jsii.member(jsii_name="fromAlias")
    @builtins.classmethod
    def from_alias(cls, alias_target: IAliasRecordTarget) -> "RecordTarget":
        '''Use an alias as target.

        :param alias_target: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__97eabbebabcd2acf6973571f8976591eb52a27f549b4c3abd23d91ac7ceba37e)
            check_type(argname="argument alias_target", value=alias_target, expected_type=type_hints["alias_target"])
        return typing.cast("RecordTarget", jsii.sinvoke(cls, "fromAlias", [alias_target]))

    @jsii.member(jsii_name="fromIpAddresses")
    @builtins.classmethod
    def from_ip_addresses(cls, *ip_addresses: builtins.str) -> "RecordTarget":
        '''Use ip addresses as target.

        :param ip_addresses: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__22a2cb83387a6785138daa53fc8099f2fd85af4d7ddd997da2d563ba3e4801d9)
            check_type(argname="argument ip_addresses", value=ip_addresses, expected_type=typing.Tuple[type_hints["ip_addresses"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("RecordTarget", jsii.sinvoke(cls, "fromIpAddresses", [*ip_addresses]))

    @jsii.member(jsii_name="fromValues")
    @builtins.classmethod
    def from_values(cls, *values: builtins.str) -> "RecordTarget":
        '''Use string values as target.

        :param values: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8d9f2d233732c1eae777eca34e2d8eeada36e28a2ad8db6f1b5673ec203a071c)
            check_type(argname="argument values", value=values, expected_type=typing.Tuple[type_hints["values"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast("RecordTarget", jsii.sinvoke(cls, "fromValues", [*values]))

    @builtins.property
    @jsii.member(jsii_name="aliasTarget")
    def alias_target(self) -> typing.Optional[IAliasRecordTarget]:
        '''alias for targets such as CloudFront distribution to route traffic to.'''
        return typing.cast(typing.Optional[IAliasRecordTarget], jsii.get(self, "aliasTarget"))

    @builtins.property
    @jsii.member(jsii_name="values")
    def values(self) -> typing.Optional[typing.List[builtins.str]]:
        '''correspond with the chosen record type (e.g. for 'A' Type, specify one or more IP addresses).'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "values"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_route53.RecordType")
class RecordType(enum.Enum):
    '''The record type.'''

    A = "A"
    '''route traffic to a resource, such as a web server, using an IPv4 address in dotted decimal notation.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#AFormat
    '''
    AAAA = "AAAA"
    '''route traffic to a resource, such as a web server, using an IPv6 address in colon-separated hexadecimal format.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#AAAAFormat
    '''
    CAA = "CAA"
    '''A CAA record specifies which certificate authorities (CAs) are allowed to issue certificates for a domain or subdomain.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CAAFormat
    '''
    CNAME = "CNAME"
    '''A CNAME record maps DNS queries for the name of the current record, such as acme.example.com, to another domain (example.com or example.net) or subdomain (acme.example.com or zenith.example.org).

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#CNAMEFormat
    '''
    DS = "DS"
    '''A delegation signer (DS) record refers a zone key for a delegated subdomain zone.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#DSFormat
    '''
    MX = "MX"
    '''An MX record specifies the names of your mail servers and, if you have two or more mail servers, the priority order.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#MXFormat
    '''
    NAPTR = "NAPTR"
    '''A Name Authority Pointer (NAPTR) is a type of record that is used by Dynamic Delegation Discovery System (DDDS) applications to convert one value to another or to replace one value with another.

    For example, one common use is to convert phone numbers into SIP URIs.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#NAPTRFormat
    '''
    NS = "NS"
    '''An NS record identifies the name servers for the hosted zone.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#NSFormat
    '''
    PTR = "PTR"
    '''A PTR record maps an IP address to the corresponding domain name.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#PTRFormat
    '''
    SOA = "SOA"
    '''A start of authority (SOA) record provides information about a domain and the corresponding Amazon Route 53 hosted zone.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SOAFormat
    '''
    SPF = "SPF"
    '''SPF records were formerly used to verify the identity of the sender of email messages.

    Instead of an SPF record, we recommend that you create a TXT record that contains the applicable value.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SPFFormat
    '''
    SRV = "SRV"
    '''An SRV record Value element consists of four space-separated values.

    The first three values are
    decimal numbers representing priority, weight, and port. The fourth value is a domain name.

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#SRVFormat
    '''
    TXT = "TXT"
    '''A TXT record contains one or more strings that are enclosed in double quotation marks (").

    :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/ResourceRecordTypes.html#TXTFormat
    '''


class SrvRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.SrvRecord",
):
    '''A DNS SRV record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_route53 as route53
        
        # geo_location: route53.GeoLocation
        # hosted_zone: route53.HostedZone
        
        srv_record = route53.SrvRecord(self, "MySrvRecord",
            values=[route53.SrvRecordValue(
                host_name="hostName",
                port=123,
                priority=123,
                weight=123
            )],
            zone=hosted_zone,
        
            # the properties below are optional
            comment="comment",
            delete_existing=False,
            geo_location=geo_location,
            multi_value_answer=False,
            record_name="recordName",
            region="region",
            set_identifier="setIdentifier",
            ttl=cdk.Duration.minutes(30),
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        values: typing.Sequence[typing.Union["SrvRecordValue", typing.Dict[builtins.str, typing.Any]]],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param values: The values.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d52a70fbe22ca5e13acce72254719ea0dd37b436de0640b65774aadd9c6fe954)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = SrvRecordProps(
            values=values,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.SrvRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "values": "values",
    },
)
class SrvRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        values: typing.Sequence[typing.Union["SrvRecordValue", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Construction properties for a SrvRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param values: The values.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            
            srv_record_props = route53.SrvRecordProps(
                values=[route53.SrvRecordValue(
                    host_name="hostName",
                    port=123,
                    priority=123,
                    weight=123
                )],
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__803828161f541995c058596dab53102f2eccd14ba565bbe715a5ac29353f6db9)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def values(self) -> typing.List["SrvRecordValue"]:
        '''The values.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List["SrvRecordValue"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SrvRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.SrvRecordValue",
    jsii_struct_bases=[],
    name_mapping={
        "host_name": "hostName",
        "port": "port",
        "priority": "priority",
        "weight": "weight",
    },
)
class SrvRecordValue:
    def __init__(
        self,
        *,
        host_name: builtins.str,
        port: jsii.Number,
        priority: jsii.Number,
        weight: jsii.Number,
    ) -> None:
        '''Properties for a SRV record value.

        :param host_name: The server host name.
        :param port: The port.
        :param priority: The priority.
        :param weight: The weight.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_route53 as route53
            
            srv_record_value = route53.SrvRecordValue(
                host_name="hostName",
                port=123,
                priority=123,
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6c9da4f91ee9021e13a985564e2b781386a5d9cfc61b96742f9b71034f358a9)
            check_type(argname="argument host_name", value=host_name, expected_type=type_hints["host_name"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "host_name": host_name,
            "port": port,
            "priority": priority,
            "weight": weight,
        }

    @builtins.property
    def host_name(self) -> builtins.str:
        '''The server host name.'''
        result = self._values.get("host_name")
        assert result is not None, "Required property 'host_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def port(self) -> jsii.Number:
        '''The port.'''
        result = self._values.get("port")
        assert result is not None, "Required property 'port' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def priority(self) -> jsii.Number:
        '''The priority.'''
        result = self._values.get("priority")
        assert result is not None, "Required property 'priority' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def weight(self) -> jsii.Number:
        '''The weight.'''
        result = self._values.get("weight")
        assert result is not None, "Required property 'weight' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SrvRecordValue(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class TxtRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.TxtRecord",
):
    '''A DNS TXT record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: infused

    Example::

        # my_zone: route53.HostedZone
        
        
        route53.TxtRecord(self, "TXTRecord",
            zone=my_zone,
            record_name="_foo",  # If the name ends with a ".", it will be used as-is;
            # if it ends with a "." followed by the zone name, a trailing "." will be added automatically;
            # otherwise, a ".", the zone name, and a trailing "." will be added automatically.
            # Defaults to zone root if not specified.
            values=["Bar!", "Baz?"],
            ttl=Duration.minutes(90)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        values: typing.Sequence[builtins.str],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param values: The text values.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__df1e0c1447d860a09246a7ec54507ca123346e57365df024460258839b4bd48b)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = TxtRecordProps(
            values=values,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.TxtRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "values": "values",
    },
)
class TxtRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''Construction properties for a TxtRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param values: The text values.

        :exampleMetadata: infused

        Example::

            # my_zone: route53.HostedZone
            
            
            route53.TxtRecord(self, "TXTRecord",
                zone=my_zone,
                record_name="_foo",  # If the name ends with a ".", it will be used as-is;
                # if it ends with a "." followed by the zone name, a trailing "." will be added automatically;
                # otherwise, a ".", the zone name, and a trailing "." will be added automatically.
                # Defaults to zone root if not specified.
                values=["Bar!", "Baz?"],
                ttl=Duration.minutes(90)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1925dd23d881cbbf99625b9a5fe0ef65b92a92359376c46e49b6690f1a4a9dab)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''The text values.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "TxtRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VpcEndpointServiceDomainName(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.VpcEndpointServiceDomainName",
):
    '''A Private DNS configuration for a VPC endpoint service.

    :exampleMetadata: infused

    Example::

        from aws_cdk.aws_route53 import PublicHostedZone, VpcEndpointServiceDomainName
        # zone: PublicHostedZone
        # vpces: ec2.VpcEndpointService
        
        
        VpcEndpointServiceDomainName(self, "EndpointDomain",
            endpoint_service=vpces,
            domain_name="my-stuff.aws-cdk.dev",
            public_hosted_zone=zone
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        endpoint_service: _IVpcEndpointService_4ddddab0,
        public_hosted_zone: IPublicHostedZone,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain_name: The domain name to use. This domain name must be owned by this account (registered through Route53), or delegated to this account. Domain ownership will be verified by AWS before private DNS can be used.
        :param endpoint_service: The VPC Endpoint Service to configure Private DNS for.
        :param public_hosted_zone: The public hosted zone to use for the domain.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0f1e0787b803b3e6b7bc1893af9e2bd854989d8ecc1ee95b572a359f686c4bd)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = VpcEndpointServiceDomainNameProps(
            domain_name=domain_name,
            endpoint_service=endpoint_service,
            public_hosted_zone=public_hosted_zone,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="domainName")
    def domain_name(self) -> builtins.str:
        '''The domain name associated with the private DNS configuration.'''
        return typing.cast(builtins.str, jsii.get(self, "domainName"))

    @domain_name.setter
    def domain_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb8d9c4cf0d124563d17362021e80fc8fa146791616e752bd4a8ccb6df767280)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "domainName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.VpcEndpointServiceDomainNameProps",
    jsii_struct_bases=[],
    name_mapping={
        "domain_name": "domainName",
        "endpoint_service": "endpointService",
        "public_hosted_zone": "publicHostedZone",
    },
)
class VpcEndpointServiceDomainNameProps:
    def __init__(
        self,
        *,
        domain_name: builtins.str,
        endpoint_service: _IVpcEndpointService_4ddddab0,
        public_hosted_zone: IPublicHostedZone,
    ) -> None:
        '''Properties to configure a VPC Endpoint Service domain name.

        :param domain_name: The domain name to use. This domain name must be owned by this account (registered through Route53), or delegated to this account. Domain ownership will be verified by AWS before private DNS can be used.
        :param endpoint_service: The VPC Endpoint Service to configure Private DNS for.
        :param public_hosted_zone: The public hosted zone to use for the domain.

        :exampleMetadata: infused

        Example::

            from aws_cdk.aws_route53 import PublicHostedZone, VpcEndpointServiceDomainName
            # zone: PublicHostedZone
            # vpces: ec2.VpcEndpointService
            
            
            VpcEndpointServiceDomainName(self, "EndpointDomain",
                endpoint_service=vpces,
                domain_name="my-stuff.aws-cdk.dev",
                public_hosted_zone=zone
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6355fbcde34ee994597b3b647c64b65eb32833843e3bc72c5479e8a6ad7fb623)
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
            check_type(argname="argument endpoint_service", value=endpoint_service, expected_type=type_hints["endpoint_service"])
            check_type(argname="argument public_hosted_zone", value=public_hosted_zone, expected_type=type_hints["public_hosted_zone"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "domain_name": domain_name,
            "endpoint_service": endpoint_service,
            "public_hosted_zone": public_hosted_zone,
        }

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name to use.

        This domain name must be owned by this account (registered through Route53),
        or delegated to this account. Domain ownership will be verified by AWS before
        private DNS can be used.

        :see: https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-services-dns-validation.html
        '''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def endpoint_service(self) -> _IVpcEndpointService_4ddddab0:
        '''The VPC Endpoint Service to configure Private DNS for.'''
        result = self._values.get("endpoint_service")
        assert result is not None, "Required property 'endpoint_service' is missing"
        return typing.cast(_IVpcEndpointService_4ddddab0, result)

    @builtins.property
    def public_hosted_zone(self) -> IPublicHostedZone:
        '''The public hosted zone to use for the domain.'''
        result = self._values.get("public_hosted_zone")
        assert result is not None, "Required property 'public_hosted_zone' is missing"
        return typing.cast(IPublicHostedZone, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VpcEndpointServiceDomainNameProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.ZoneDelegationOptions",
    jsii_struct_bases=[],
    name_mapping={"comment": "comment", "ttl": "ttl"},
)
class ZoneDelegationOptions:
    def __init__(
        self,
        *,
        comment: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Options available when creating a delegation relationship from one PublicHostedZone to another.

        :param comment: A comment to add on the DNS record created to incorporate the delegation. Default: none
        :param ttl: The TTL (Time To Live) of the DNS delegation record in DNS caches. Default: 172800

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            zone_delegation_options = route53.ZoneDelegationOptions(
                comment="comment",
                ttl=cdk.Duration.minutes(30)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0efd84c1e481104af0fc88e047ca0cffa51a834020eec2f9c9cfee5df2642f84)
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if comment is not None:
            self._values["comment"] = comment
        if ttl is not None:
            self._values["ttl"] = ttl

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the DNS record created to incorporate the delegation.

        :default: none
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The TTL (Time To Live) of the DNS delegation record in DNS caches.

        :default: 172800
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneDelegationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ZoneDelegationRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.ZoneDelegationRecord",
):
    '''A record to delegate further lookups to a different set of name servers.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_route53 as route53
        
        # geo_location: route53.GeoLocation
        # hosted_zone: route53.HostedZone
        
        zone_delegation_record = route53.ZoneDelegationRecord(self, "MyZoneDelegationRecord",
            name_servers=["nameServers"],
            zone=hosted_zone,
        
            # the properties below are optional
            comment="comment",
            delete_existing=False,
            geo_location=geo_location,
            multi_value_answer=False,
            record_name="recordName",
            region="region",
            set_identifier="setIdentifier",
            ttl=cdk.Duration.minutes(30),
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name_servers: typing.Sequence[builtins.str],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param name_servers: The name servers to report in the delegation records.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1f8360676c13e2167bb58d36e1b6384ba70f036979aa9c80cac046e12779c594)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ZoneDelegationRecordProps(
            name_servers=name_servers,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.ZoneDelegationRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "name_servers": "nameServers",
    },
)
class ZoneDelegationRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        name_servers: typing.Sequence[builtins.str],
    ) -> None:
        '''Construction properties for a ZoneDelegationRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param name_servers: The name servers to report in the delegation records.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            
            zone_delegation_record_props = route53.ZoneDelegationRecordProps(
                name_servers=["nameServers"],
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__240a965753acb9488d02c120074027364f5e85a8ec585205a863174feadd7582)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument name_servers", value=name_servers, expected_type=type_hints["name_servers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "name_servers": name_servers,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def name_servers(self) -> typing.List[builtins.str]:
        '''The name servers to report in the delegation records.'''
        result = self._values.get("name_servers")
        assert result is not None, "Required property 'name_servers' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneDelegationRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.ZoneSigningOptions",
    jsii_struct_bases=[],
    name_mapping={"kms_key": "kmsKey", "key_signing_key_name": "keySigningKeyName"},
)
class ZoneSigningOptions:
    def __init__(
        self,
        *,
        kms_key: _IKey_5f11635f,
        key_signing_key_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for enabling key signing from a hosted zone.

        :param kms_key: The customer-managed KMS key that that will be used to sign the records. The KMS Key must be unique for each KSK within a hosted zone. Additionally, the KMS key must be an asymetric customer-managed key using the ECC_NIST_P256 algorithm.
        :param key_signing_key_name: The name for the key signing key. This name must be unique within a hosted zone. Default: an autogenerated name

        :exampleMetadata: infused

        Example::

            kms_key = kms.Key(self, "KmsCMK",
                key_spec=kms.KeySpec.ECC_NIST_P256,
                key_usage=kms.KeyUsage.SIGN_VERIFY
            )
            hosted_zone = route53.HostedZone(self, "HostedZone",
                zone_name="example.com"
            )
            # Enable DNSSEC signing for the zone
            hosted_zone.enable_dnssec(kms_key=kms_key)
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c024f1ad9949a250bc85eb88751e2c625dd1a6679c33a35a4add759a0404b95c)
            check_type(argname="argument kms_key", value=kms_key, expected_type=type_hints["kms_key"])
            check_type(argname="argument key_signing_key_name", value=key_signing_key_name, expected_type=type_hints["key_signing_key_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "kms_key": kms_key,
        }
        if key_signing_key_name is not None:
            self._values["key_signing_key_name"] = key_signing_key_name

    @builtins.property
    def kms_key(self) -> _IKey_5f11635f:
        '''The customer-managed KMS key that that will be used to sign the records.

        The KMS Key must be unique for each KSK within a hosted zone. Additionally, the
        KMS key must be an asymetric customer-managed key using the ECC_NIST_P256 algorithm.

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/dns-configuring-dnssec-cmk-requirements.html
        '''
        result = self._values.get("kms_key")
        assert result is not None, "Required property 'kms_key' is missing"
        return typing.cast(_IKey_5f11635f, result)

    @builtins.property
    def key_signing_key_name(self) -> typing.Optional[builtins.str]:
        '''The name for the key signing key.

        This name must be unique within a hosted zone.

        :default: an autogenerated name
        '''
        result = self._values.get("key_signing_key_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ZoneSigningOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class ARecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.ARecord",
):
    '''A DNS A record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_apigateway as apigw
        
        # zone: route53.HostedZone
        # rest_api: apigw.LambdaRestApi
        
        
        route53.ARecord(self, "AliasRecord",
            zone=zone,
            target=route53.RecordTarget.from_alias(targets.ApiGateway(rest_api))
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        target: RecordTarget,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param target: The target.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca2e60ba6b2baeeff2cc875c86af94b4b26d6f11c1cfcca09280ac533b792230)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ARecordProps(
            target=target,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromARecordAttributes")
    @builtins.classmethod
    def from_a_record_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        target_dns: builtins.str,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> "ARecord":
        '''Creates new A record of type alias with target set to an existing A Record DNS.

        Use when the target A record is created outside of CDK
        For records created as part of CDK use

        :param scope: the parent Construct for this Construct.
        :param id: Logical Id of the resource.
        :param target_dns: Existing A record DNS name to set RecordTarget.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing

        :return: AWS::Route53::RecordSet of type A with target alias set to existing A record

        :aws-cdk-lib: /aws-route53-targets/route53-record.ts
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c76ad72e64542d58d5e33c28ccaca560dac09b21c920d094b7a0c2386fe42886)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = ARecordAttrs(
            target_dns=target_dns,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        return typing.cast("ARecord", jsii.sinvoke(cls, "fromARecordAttributes", [scope, id, attrs]))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.ARecordAttrs",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "target_dns": "targetDNS",
    },
)
class ARecordAttrs(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        target_dns: builtins.str,
    ) -> None:
        '''Construction properties to import existing ARecord as target.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param target_dns: Existing A record DNS name to set RecordTarget.

        :exampleMetadata: infused

        Example::

            # my_zone: route53.HostedZone
            
            target_record = "existing.record.cdk.local"
            record = route53.ARecord.from_aRecord_attributes(self, "A",
                zone=my_zone,
                record_name="test",
                target_dNS=target_record
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__514d7eccc21be019febe80e121fd7d979162668b63cb99051c629ef087f5fe9a)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument target_dns", value=target_dns, expected_type=type_hints["target_dns"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "target_dns": target_dns,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target_dns(self) -> builtins.str:
        '''Existing A record DNS name to set RecordTarget.'''
        result = self._values.get("target_dns")
        assert result is not None, "Required property 'target_dns' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ARecordAttrs(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.ARecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "target": "target",
    },
)
class ARecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        target: RecordTarget,
    ) -> None:
        '''Construction properties for a ARecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param target: The target.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_apigateway as apigw
            
            # zone: route53.HostedZone
            # rest_api: apigw.LambdaRestApi
            
            
            route53.ARecord(self, "AliasRecord",
                zone=zone,
                target=route53.RecordTarget.from_alias(targets.ApiGateway(rest_api))
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a73a5c86411a0d853fcfad820ed58f5a5c19df65a7b2756560958db5cbe36569)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "target": target,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target(self) -> RecordTarget:
        '''The target.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(RecordTarget, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ARecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AaaaRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.AaaaRecord",
):
    '''A DNS AAAA record.

    :resource: AWS::Route53::RecordSet
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

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        target: RecordTarget,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param target: The target.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d5345c027ebd51f32f58fdeb055904a5c4dd3f5523f55954f8a191ae8bf29ee)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AaaaRecordProps(
            target=target,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.AaaaRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "target": "target",
    },
)
class AaaaRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        target: RecordTarget,
    ) -> None:
        '''Construction properties for a AaaaRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param target: The target.

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
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c051ff70083b2ae68889d3f02be8344125acf64b4768d5f5df3298ba8a8d6a32)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument target", value=target, expected_type=type_hints["target"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "target": target,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def target(self) -> RecordTarget:
        '''The target.'''
        result = self._values.get("target")
        assert result is not None, "Required property 'target' is missing"
        return typing.cast(RecordTarget, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AaaaRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CaaAmazonRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
    },
)
class CaaAmazonRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''Construction properties for a CaaAmazonRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            
            caa_amazon_record_props = route53.CaaAmazonRecordProps(
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14055fdb7d9f4b55091295996ec92db8d73fa789a21fca2664da1242ae89f859)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaaAmazonRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CaaRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CaaRecord",
):
    '''A DNS CAA record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_route53 as route53
        
        # geo_location: route53.GeoLocation
        # hosted_zone: route53.HostedZone
        
        caa_record = route53.CaaRecord(self, "MyCaaRecord",
            values=[route53.CaaRecordValue(
                flag=123,
                tag=route53.CaaTag.ISSUE,
                value="value"
            )],
            zone=hosted_zone,
        
            # the properties below are optional
            comment="comment",
            delete_existing=False,
            geo_location=geo_location,
            multi_value_answer=False,
            record_name="recordName",
            region="region",
            set_identifier="setIdentifier",
            ttl=cdk.Duration.minutes(30),
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        values: typing.Sequence[typing.Union[CaaRecordValue, typing.Dict[builtins.str, typing.Any]]],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param values: The values.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3a2502cdc1fe021e837217ab0d96b9fa6ea450a68c089482935b695f7943ff3c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CaaRecordProps(
            values=values,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CaaRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "values": "values",
    },
)
class CaaRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        values: typing.Sequence[typing.Union[CaaRecordValue, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Construction properties for a CaaRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param values: The values.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            
            caa_record_props = route53.CaaRecordProps(
                values=[route53.CaaRecordValue(
                    flag=123,
                    tag=route53.CaaTag.ISSUE,
                    value="value"
                )],
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__349a94b990ddb833b270dc692692a8b37187c6f17114e02514f44accfb8de443)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def values(self) -> typing.List[CaaRecordValue]:
        '''The values.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[CaaRecordValue], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CaaRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class CnameRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CnameRecord",
):
    '''A DNS CNAME record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: infused

    Example::

        import aws_cdk.aws_certificatemanager as acm
        import aws_cdk.aws_route53 as route53
        
        # hosted zone and route53 features
        # hosted_zone_id: str
        zone_name = "example.com"
        
        
        my_domain_name = "api.example.com"
        certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
        schema = appsync.SchemaFile(file_path="mySchemaFile")
        api = appsync.GraphqlApi(self, "api",
            name="myApi",
            definition=appsync.Definition.from_schema(schema),
            domain_name=appsync.DomainOptions(
                certificate=certificate,
                domain_name=my_domain_name
            )
        )
        
        # hosted zone for adding appsync domain
        zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
            hosted_zone_id=hosted_zone_id,
            zone_name=zone_name
        )
        
        # create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
        route53.CnameRecord(self, "CnameApiRecord",
            record_name="api",
            zone=zone,
            domain_name=api.app_sync_domain_name
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param domain_name: The domain name of the target that this record should point to.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e8dfccd8504bb3c0a779b42a665f362282b1083fe52a95b450d1ac1eb3622c80)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CnameRecordProps(
            domain_name=domain_name,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.CnameRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "domain_name": "domainName",
    },
)
class CnameRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        domain_name: builtins.str,
    ) -> None:
        '''Construction properties for a CnameRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param domain_name: The domain name of the target that this record should point to.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_certificatemanager as acm
            import aws_cdk.aws_route53 as route53
            
            # hosted zone and route53 features
            # hosted_zone_id: str
            zone_name = "example.com"
            
            
            my_domain_name = "api.example.com"
            certificate = acm.Certificate(self, "cert", domain_name=my_domain_name)
            schema = appsync.SchemaFile(file_path="mySchemaFile")
            api = appsync.GraphqlApi(self, "api",
                name="myApi",
                definition=appsync.Definition.from_schema(schema),
                domain_name=appsync.DomainOptions(
                    certificate=certificate,
                    domain_name=my_domain_name
                )
            )
            
            # hosted zone for adding appsync domain
            zone = route53.HostedZone.from_hosted_zone_attributes(self, "HostedZone",
                hosted_zone_id=hosted_zone_id,
                zone_name=zone_name
            )
            
            # create a cname to the appsync domain. will map to something like xxxx.cloudfront.net
            route53.CnameRecord(self, "CnameApiRecord",
                record_name="api",
                zone=zone,
                domain_name=api.app_sync_domain_name
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__43b5fc8ccb719e2580c804225e8258b57b1700a701203416558eb2d76a86f86f)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument domain_name", value=domain_name, expected_type=type_hints["domain_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "domain_name": domain_name,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def domain_name(self) -> builtins.str:
        '''The domain name of the target that this record should point to.'''
        result = self._values.get("domain_name")
        assert result is not None, "Required property 'domain_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CnameRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DsRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.DsRecord",
):
    '''A DNS DS record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: infused

    Example::

        # my_zone: route53.HostedZone
        
        
        route53.DsRecord(self, "DSRecord",
            zone=my_zone,
            record_name="foo",
            values=["12345 3 1 123456789abcdef67890123456789abcdef67890"
            ],
            ttl=Duration.minutes(90)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        values: typing.Sequence[builtins.str],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param values: The DS values.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24205d1a44dcefb992b7bd9b6d91d8b6396f8498224c30876fe8a0673c4dc790)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DsRecordProps(
            values=values,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.DsRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "values": "values",
    },
)
class DsRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''Construction properties for a DSRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param values: The DS values.

        :exampleMetadata: infused

        Example::

            # my_zone: route53.HostedZone
            
            
            route53.DsRecord(self, "DSRecord",
                zone=my_zone,
                record_name="foo",
                values=["12345 3 1 123456789abcdef67890123456789abcdef67890"
                ],
                ttl=Duration.minutes(90)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f86f16d9f2de8fe03cc1189a56a86c4888d20f69dc0f241aa21b50fdf34d4645)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''The DS values.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DsRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IHostedZone)
class HostedZone(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.HostedZone",
):
    '''Container for records, and records contain information about how to route traffic for a specific domain, such as example.com and its subdomains (acme.example.com, zenith.example.com).

    :exampleMetadata: infused

    Example::

        kms_key = kms.Key(self, "KmsCMK",
            key_spec=kms.KeySpec.ECC_NIST_P256,
            key_usage=kms.KeyUsage.SIGN_VERIFY
        )
        hosted_zone = route53.HostedZone(self, "HostedZone",
            zone_name="example.com"
        )
        # Enable DNSSEC signing for the zone
        hosted_zone.enable_dnssec(kms_key=kms_key)
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        vpcs: typing.Optional[typing.Sequence[_IVpc_f30d5663]] = None,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpcs: A VPC that you want to associate with this hosted zone. When you specify this property, a private hosted zone will be created. You can associate additional VPCs to this private zone using ``addVpc(vpc)``. Default: public (no VPCs associated)
        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1e5b9f9d7aa4bc16fced3cc22e63b14cbf590c498be223e588483a72fb0b4233)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = HostedZoneProps(
            vpcs=vpcs,
            zone_name=zone_name,
            add_trailing_dot=add_trailing_dot,
            comment=comment,
            query_logs_log_group_arn=query_logs_log_group_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromHostedZoneAttributes")
    @builtins.classmethod
    def from_hosted_zone_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
        zone_name: builtins.str,
    ) -> IHostedZone:
        '''Imports a hosted zone from another stack.

        Use when both hosted zone ID and hosted zone name are known.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param hosted_zone_id: Identifier of the hosted zone.
        :param zone_name: Name of the hosted zone.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__24a9e3565a26d4d6d8a3c0d4406ef8f6cce5e0e48dc1145dc090f7db4581c0ac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = HostedZoneAttributes(
            hosted_zone_id=hosted_zone_id, zone_name=zone_name
        )

        return typing.cast(IHostedZone, jsii.sinvoke(cls, "fromHostedZoneAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromHostedZoneId")
    @builtins.classmethod
    def from_hosted_zone_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        hosted_zone_id: builtins.str,
    ) -> IHostedZone:
        '''Import a Route 53 hosted zone defined either outside the CDK, or in a different CDK stack.

        Use when hosted zone ID is known. If a HostedZone is imported with this method the zoneName cannot be referenced.
        If the zoneName is needed then the HostedZone should be imported with ``fromHostedZoneAttributes()`` or ``fromLookup()``

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param hosted_zone_id: the ID of the hosted zone to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dc5da03bfe3e7000e80ebfbe7cb3c5c23ab3e97f4e6c670a8eb0ef036d099c78)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument hosted_zone_id", value=hosted_zone_id, expected_type=type_hints["hosted_zone_id"])
        return typing.cast(IHostedZone, jsii.sinvoke(cls, "fromHostedZoneId", [scope, id, hosted_zone_id]))

    @jsii.member(jsii_name="fromLookup")
    @builtins.classmethod
    def from_lookup(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        domain_name: builtins.str,
        private_zone: typing.Optional[builtins.bool] = None,
        vpc_id: typing.Optional[builtins.str] = None,
    ) -> IHostedZone:
        '''Lookup a hosted zone in the current account/region based on query parameters.

        Requires environment, you must specify env for the stack.

        Use to easily query hosted zones.

        :param scope: -
        :param id: -
        :param domain_name: The zone domain e.g. example.com.
        :param private_zone: Whether the zone that is being looked up is a private hosted zone. Default: false
        :param vpc_id: Specifies the ID of the VPC associated with a private hosted zone. If a VPC ID is provided and privateZone is false, no results will be returned and an error will be raised Default: - No VPC ID

        :see: https://docs.aws.amazon.com/cdk/latest/guide/environments.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bdb223a28519af08e8a4de265a9236844a06052261acd92d02cc9634acf56a8c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        query = HostedZoneProviderProps(
            domain_name=domain_name, private_zone=private_zone, vpc_id=vpc_id
        )

        return typing.cast(IHostedZone, jsii.sinvoke(cls, "fromLookup", [scope, id, query]))

    @jsii.member(jsii_name="addVpc")
    def add_vpc(self, vpc: _IVpc_f30d5663) -> None:
        '''Add another VPC to this private hosted zone.

        :param vpc: the other VPC to add.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5c63a3fccbc53f093c8e4d46a2848bf83b386d2ca5206e82ecd8ecd3d61a0ccb)
            check_type(argname="argument vpc", value=vpc, expected_type=type_hints["vpc"])
        return typing.cast(None, jsii.invoke(self, "addVpc", [vpc]))

    @jsii.member(jsii_name="enableDnssec")
    def enable_dnssec(
        self,
        *,
        kms_key: _IKey_5f11635f,
        key_signing_key_name: typing.Optional[builtins.str] = None,
    ) -> IKeySigningKey:
        '''Enable DNSSEC for this hosted zone.

        This will create a key signing key with the given options and enable DNSSEC signing
        for the hosted zone.

        :param kms_key: The customer-managed KMS key that that will be used to sign the records. The KMS Key must be unique for each KSK within a hosted zone. Additionally, the KMS key must be an asymetric customer-managed key using the ECC_NIST_P256 algorithm.
        :param key_signing_key_name: The name for the key signing key. This name must be unique within a hosted zone. Default: an autogenerated name
        '''
        options = ZoneSigningOptions(
            kms_key=kms_key, key_signing_key_name=key_signing_key_name
        )

        return typing.cast(IKeySigningKey, jsii.invoke(self, "enableDnssec", [options]))

    @jsii.member(jsii_name="grantDelegation")
    def grant_delegation(self, grantee: _IGrantable_71c4f5de) -> _Grant_a7ae64f8:
        '''Grant permissions to add delegation records to this zone.

        :param grantee: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8e256ece77d93011f031e05a119f03b248a4b68d267c298052b0cea131943ab5)
            check_type(argname="argument grantee", value=grantee, expected_type=type_hints["grantee"])
        return typing.cast(_Grant_a7ae64f8, jsii.invoke(self, "grantDelegation", [grantee]))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneArn")
    def hosted_zone_arn(self) -> builtins.str:
        '''ARN of this hosted zone, such as arn:${Partition}:route53:::hostedzone/${Id}.'''
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneArn"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneId")
    def hosted_zone_id(self) -> builtins.str:
        '''ID of this hosted zone, such as "Z23ABC4XYZL05B".'''
        return typing.cast(builtins.str, jsii.get(self, "hostedZoneId"))

    @builtins.property
    @jsii.member(jsii_name="vpcs")
    def _vpcs(self) -> typing.List[CfnHostedZone.VPCProperty]:
        '''VPCs to which this hosted zone will be added.'''
        return typing.cast(typing.List[CfnHostedZone.VPCProperty], jsii.get(self, "vpcs"))

    @builtins.property
    @jsii.member(jsii_name="zoneName")
    def zone_name(self) -> builtins.str:
        '''FQDN of this hosted zone.'''
        return typing.cast(builtins.str, jsii.get(self, "zoneName"))

    @builtins.property
    @jsii.member(jsii_name="hostedZoneNameServers")
    def hosted_zone_name_servers(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Returns the set of name servers for the specific hosted zone. For example: ns1.example.com.

        This attribute will be undefined for private hosted zones or hosted zones imported from another stack.
        '''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "hostedZoneNameServers"))


class MxRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.MxRecord",
):
    '''A DNS MX record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_route53 as route53
        
        # geo_location: route53.GeoLocation
        # hosted_zone: route53.HostedZone
        
        mx_record = route53.MxRecord(self, "MyMxRecord",
            values=[route53.MxRecordValue(
                host_name="hostName",
                priority=123
            )],
            zone=hosted_zone,
        
            # the properties below are optional
            comment="comment",
            delete_existing=False,
            geo_location=geo_location,
            multi_value_answer=False,
            record_name="recordName",
            region="region",
            set_identifier="setIdentifier",
            ttl=cdk.Duration.minutes(30),
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        values: typing.Sequence[typing.Union[MxRecordValue, typing.Dict[builtins.str, typing.Any]]],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param values: The values.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__615153e942ef5cdcb0022d4565e0ec8b8c5554594bfe7221366ad5c83a3b679e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = MxRecordProps(
            values=values,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.MxRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "values": "values",
    },
)
class MxRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        values: typing.Sequence[typing.Union[MxRecordValue, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Construction properties for a MxRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param values: The values.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            import aws_cdk as cdk
            from aws_cdk import aws_route53 as route53
            
            # geo_location: route53.GeoLocation
            # hosted_zone: route53.HostedZone
            
            mx_record_props = route53.MxRecordProps(
                values=[route53.MxRecordValue(
                    host_name="hostName",
                    priority=123
                )],
                zone=hosted_zone,
            
                # the properties below are optional
                comment="comment",
                delete_existing=False,
                geo_location=geo_location,
                multi_value_answer=False,
                record_name="recordName",
                region="region",
                set_identifier="setIdentifier",
                ttl=cdk.Duration.minutes(30),
                weight=123
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b259122626a3ba94eebff0b5f692944df4aa55dc550b7d113eec491e1c57307d)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def values(self) -> typing.List[MxRecordValue]:
        '''The values.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[MxRecordValue], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "MxRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class NsRecord(
    RecordSet,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.NsRecord",
):
    '''A DNS NS record.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: infused

    Example::

        # my_zone: route53.HostedZone
        
        
        route53.NsRecord(self, "NSRecord",
            zone=my_zone,
            record_name="foo",
            values=["ns-1.awsdns.co.uk.", "ns-2.awsdns.com."
            ],
            ttl=Duration.minutes(90)
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        values: typing.Sequence[builtins.str],
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param values: The NS values.
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7f3bbcb4bd5bcd8978ae60eaac5ea2c6ab0bb8357a389e9b981e63291cdcc3ab)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = NsRecordProps(
            values=values,
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_route53.NsRecordProps",
    jsii_struct_bases=[RecordSetOptions],
    name_mapping={
        "zone": "zone",
        "comment": "comment",
        "delete_existing": "deleteExisting",
        "geo_location": "geoLocation",
        "multi_value_answer": "multiValueAnswer",
        "record_name": "recordName",
        "region": "region",
        "set_identifier": "setIdentifier",
        "ttl": "ttl",
        "weight": "weight",
        "values": "values",
    },
)
class NsRecordProps(RecordSetOptions):
    def __init__(
        self,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
        values: typing.Sequence[builtins.str],
    ) -> None:
        '''Construction properties for a NSRecord.

        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        :param values: The NS values.

        :exampleMetadata: infused

        Example::

            # my_zone: route53.HostedZone
            
            
            route53.NsRecord(self, "NSRecord",
                zone=my_zone,
                record_name="foo",
                values=["ns-1.awsdns.co.uk.", "ns-2.awsdns.com."
                ],
                ttl=Duration.minutes(90)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__33cda5fac8572316158161da713e2ceea9d3f7f56b5ee9a2a25acf331e737e86)
            check_type(argname="argument zone", value=zone, expected_type=type_hints["zone"])
            check_type(argname="argument comment", value=comment, expected_type=type_hints["comment"])
            check_type(argname="argument delete_existing", value=delete_existing, expected_type=type_hints["delete_existing"])
            check_type(argname="argument geo_location", value=geo_location, expected_type=type_hints["geo_location"])
            check_type(argname="argument multi_value_answer", value=multi_value_answer, expected_type=type_hints["multi_value_answer"])
            check_type(argname="argument record_name", value=record_name, expected_type=type_hints["record_name"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument set_identifier", value=set_identifier, expected_type=type_hints["set_identifier"])
            check_type(argname="argument ttl", value=ttl, expected_type=type_hints["ttl"])
            check_type(argname="argument weight", value=weight, expected_type=type_hints["weight"])
            check_type(argname="argument values", value=values, expected_type=type_hints["values"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "zone": zone,
            "values": values,
        }
        if comment is not None:
            self._values["comment"] = comment
        if delete_existing is not None:
            self._values["delete_existing"] = delete_existing
        if geo_location is not None:
            self._values["geo_location"] = geo_location
        if multi_value_answer is not None:
            self._values["multi_value_answer"] = multi_value_answer
        if record_name is not None:
            self._values["record_name"] = record_name
        if region is not None:
            self._values["region"] = region
        if set_identifier is not None:
            self._values["set_identifier"] = set_identifier
        if ttl is not None:
            self._values["ttl"] = ttl
        if weight is not None:
            self._values["weight"] = weight

    @builtins.property
    def zone(self) -> IHostedZone:
        '''The hosted zone in which to define the new record.'''
        result = self._values.get("zone")
        assert result is not None, "Required property 'zone' is missing"
        return typing.cast(IHostedZone, result)

    @builtins.property
    def comment(self) -> typing.Optional[builtins.str]:
        '''A comment to add on the record.

        :default: no comment
        '''
        result = self._values.get("comment")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete_existing(self) -> typing.Optional[builtins.bool]:
        '''Whether to delete the same record set in the hosted zone if it already exists (dangerous!).

        This allows to deploy a new record set while minimizing the downtime because the
        new record set will be created immediately after the existing one is deleted. It
        also avoids "manual" actions to delete existing record sets.
        .. epigraph::

           **N.B.:** this feature is dangerous, use with caution! It can only be used safely when
           ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing
           an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment
           will delete the record!

        :default: false
        '''
        result = self._values.get("delete_existing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def geo_location(self) -> typing.Optional[GeoLocation]:
        '''The geographical origin for this record to return DNS records based on the user's location.'''
        result = self._values.get("geo_location")
        return typing.cast(typing.Optional[GeoLocation], result)

    @builtins.property
    def multi_value_answer(self) -> typing.Optional[builtins.bool]:
        '''Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries.

        :default: false
        '''
        result = self._values.get("multi_value_answer")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def record_name(self) -> typing.Optional[builtins.str]:
        '''The subdomain name for this record. This should be relative to the zone root name.

        For example, if you want to create a record for acme.example.com, specify
        "acme".

        You can also specify the fully qualified domain name which terminates with a
        ".". For example, "acme.example.com.".

        :default: zone root
        '''
        result = self._values.get("record_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Amazon EC2 Region where you created the resource that this resource record set refers to.

        The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer,
        and is referred to by an IP address or a DNS domain name, depending on the record type.

        When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets,
        Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region.
        Route 53 then returns the value that is associated with the selected resource record set.

        :default: - Do not set latency based routing

        :see: https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-route53-recordset.html#cfn-route53-recordset-region
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def set_identifier(self) -> typing.Optional[builtins.str]:
        '''A string used to distinguish between different records with the same combination of DNS name and type.

        It can only be set when either weight or geoLocation is defined.

        This parameter must be between 1 and 128 characters in length.

        :default: - Auto generated string
        '''
        result = self._values.get("set_identifier")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ttl(self) -> typing.Optional[_Duration_4839e8c3]:
        '''The resource record cache time to live (TTL).

        :default: Duration.minutes(30)
        '''
        result = self._values.get("ttl")
        return typing.cast(typing.Optional[_Duration_4839e8c3], result)

    @builtins.property
    def weight(self) -> typing.Optional[jsii.Number]:
        '''Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set.

        Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type.
        Route 53 then responds to queries based on the ratio of a resource's weight to the total.

        This value can be a number between 0 and 255.

        :default: - Do not set weighted routing

        :see: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-policy-weighted.html
        '''
        result = self._values.get("weight")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def values(self) -> typing.List[builtins.str]:
        '''The NS values.'''
        result = self._values.get("values")
        assert result is not None, "Required property 'values' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "NsRecordProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IPrivateHostedZone)
class PrivateHostedZone(
    HostedZone,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.PrivateHostedZone",
):
    '''Create a Route53 private hosted zone for use in one or more VPCs.

    Note that ``enableDnsHostnames`` and ``enableDnsSupport`` must have been enabled
    for the VPC you're configuring for private hosted zones.

    :resource: AWS::Route53::HostedZone
    :exampleMetadata: infused

    Example::

        # vpc: ec2.Vpc
        
        
        zone = route53.PrivateHostedZone(self, "HostedZone",
            zone_name="fully.qualified.domain.com",
            vpc=vpc
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        vpc: _IVpc_f30d5663,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param vpc: A VPC that you want to associate with this hosted zone. Private hosted zones must be associated with at least one VPC. You can associated additional VPCs using ``addVpc(vpc)``.
        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5513b0f840f5eafaeee3e3a9c7776204d075ee417c3cce2c38a14213814eb75)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PrivateHostedZoneProps(
            vpc=vpc,
            zone_name=zone_name,
            add_trailing_dot=add_trailing_dot,
            comment=comment,
            query_logs_log_group_arn=query_logs_log_group_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPrivateHostedZoneId")
    @builtins.classmethod
    def from_private_hosted_zone_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        private_hosted_zone_id: builtins.str,
    ) -> IPrivateHostedZone:
        '''Import a Route 53 private hosted zone defined either outside the CDK, or in a different CDK stack.

        Use when hosted zone ID is known. If a HostedZone is imported with this method the zoneName cannot be referenced.
        If the zoneName is needed then you cannot import a PrivateHostedZone.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param private_hosted_zone_id: the ID of the private hosted zone to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b376eac72cdb24a91e277cf6c9c277d3ed571280fb5b90bd23b7e1e1d5f88dac)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument private_hosted_zone_id", value=private_hosted_zone_id, expected_type=type_hints["private_hosted_zone_id"])
        return typing.cast(IPrivateHostedZone, jsii.sinvoke(cls, "fromPrivateHostedZoneId", [scope, id, private_hosted_zone_id]))


@jsii.implements(IPublicHostedZone)
class PublicHostedZone(
    HostedZone,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.PublicHostedZone",
):
    '''Create a Route53 public hosted zone.

    :resource: AWS::Route53::HostedZone
    :exampleMetadata: infused

    Example::

        stack1 = Stack(app, "Stack1",
            env=Environment(
                region="us-east-1"
            ),
            cross_region_references=True
        )
        cert = acm.Certificate(stack1, "Cert",
            domain_name="*.example.com",
            validation=acm.CertificateValidation.from_dns(route53.PublicHostedZone.from_hosted_zone_id(stack1, "Zone", "Z0329774B51CGXTDQV3X"))
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
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        caa_amazon: typing.Optional[builtins.bool] = None,
        cross_account_zone_delegation_principal: typing.Optional[_IPrincipal_539bb2fd] = None,
        cross_account_zone_delegation_role_name: typing.Optional[builtins.str] = None,
        zone_name: builtins.str,
        add_trailing_dot: typing.Optional[builtins.bool] = None,
        comment: typing.Optional[builtins.str] = None,
        query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param caa_amazon: Whether to create a CAA record to restrict certificate authorities allowed to issue certificates for this domain to Amazon only. Default: false
        :param cross_account_zone_delegation_principal: (deprecated) A principal which is trusted to assume a role for zone delegation. If supplied, this will create a Role in the same account as the Hosted Zone, which can be assumed by the ``CrossAccountZoneDelegationRecord`` to create a delegation record to a zone in a different account. Be sure to indicate the account(s) that you trust to create delegation records, using either ``iam.AccountPrincipal`` or ``iam.OrganizationPrincipal``. If you are planning to use ``iam.ServicePrincipal``s here, be sure to include region-specific service principals for every opt-in region you are going to be delegating to; or don't use this feature and create separate roles with appropriate permissions for every opt-in region instead. Default: - No delegation configuration
        :param cross_account_zone_delegation_role_name: (deprecated) The name of the role created for cross account delegation. Default: - A role name is generated automatically
        :param zone_name: The name of the domain. For resource record types that include a domain name, specify a fully qualified domain name.
        :param add_trailing_dot: Whether to add a trailing dot to the zone name. Default: true
        :param comment: Any comments that you want to include about the hosted zone. Default: none
        :param query_logs_log_group_arn: The Amazon Resource Name (ARN) for the log group that you want Amazon Route 53 to send query logs to. Default: disabled
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6f67fd33cdf6043dd6c0a287fb380d5704e93c1d3a80eabf2da05bc363d681c5)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = PublicHostedZoneProps(
            caa_amazon=caa_amazon,
            cross_account_zone_delegation_principal=cross_account_zone_delegation_principal,
            cross_account_zone_delegation_role_name=cross_account_zone_delegation_role_name,
            zone_name=zone_name,
            add_trailing_dot=add_trailing_dot,
            comment=comment,
            query_logs_log_group_arn=query_logs_log_group_arn,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromPublicHostedZoneAttributes")
    @builtins.classmethod
    def from_public_hosted_zone_attributes(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        hosted_zone_id: builtins.str,
        zone_name: builtins.str,
    ) -> IPublicHostedZone:
        '''Imports a public hosted zone from another stack.

        Use when both hosted zone ID and hosted zone name are known.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param hosted_zone_id: Identifier of the hosted zone.
        :param zone_name: Name of the hosted zone.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d8382b2aa9cdf1e089241eda9e9d1e17d1003056fa5fe78dfbc64017f2f83d5f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        attrs = PublicHostedZoneAttributes(
            hosted_zone_id=hosted_zone_id, zone_name=zone_name
        )

        return typing.cast(IPublicHostedZone, jsii.sinvoke(cls, "fromPublicHostedZoneAttributes", [scope, id, attrs]))

    @jsii.member(jsii_name="fromPublicHostedZoneId")
    @builtins.classmethod
    def from_public_hosted_zone_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        public_hosted_zone_id: builtins.str,
    ) -> IPublicHostedZone:
        '''Import a Route 53 public hosted zone defined either outside the CDK, or in a different CDK stack.

        Use when hosted zone ID is known. If a PublicHostedZone is imported with this method the zoneName cannot be referenced.
        If the zoneName is needed then the PublicHostedZone should be imported with ``fromPublicHostedZoneAttributes()``.

        :param scope: the parent Construct for this Construct.
        :param id: the logical name of this Construct.
        :param public_hosted_zone_id: the ID of the public hosted zone to import.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__919d0fe07f8f277a34fdf761ddcb6a1b0c7a81c9d3bd726e69bc5c6b6fbcd53e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument public_hosted_zone_id", value=public_hosted_zone_id, expected_type=type_hints["public_hosted_zone_id"])
        return typing.cast(IPublicHostedZone, jsii.sinvoke(cls, "fromPublicHostedZoneId", [scope, id, public_hosted_zone_id]))

    @jsii.member(jsii_name="addDelegation")
    def add_delegation(
        self,
        delegate: IPublicHostedZone,
        *,
        comment: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
    ) -> None:
        '''Adds a delegation from this zone to a designated zone.

        :param delegate: the zone being delegated to.
        :param comment: A comment to add on the DNS record created to incorporate the delegation. Default: none
        :param ttl: The TTL (Time To Live) of the DNS delegation record in DNS caches. Default: 172800
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ca14815188563abe1058cb85558750303980b4542afbe253885064f9c3fff98c)
            check_type(argname="argument delegate", value=delegate, expected_type=type_hints["delegate"])
        opts = ZoneDelegationOptions(comment=comment, ttl=ttl)

        return typing.cast(None, jsii.invoke(self, "addDelegation", [delegate, opts]))

    @jsii.member(jsii_name="addVpc")
    def add_vpc(self, _vpc: _IVpc_f30d5663) -> None:
        '''Add another VPC to this private hosted zone.

        :param _vpc: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3e8e9627c25114e462dc3af379684d0d3fba38262bae897187e8d8faa087102)
            check_type(argname="argument _vpc", value=_vpc, expected_type=type_hints["_vpc"])
        return typing.cast(None, jsii.invoke(self, "addVpc", [_vpc]))

    @builtins.property
    @jsii.member(jsii_name="crossAccountZoneDelegationRole")
    def cross_account_zone_delegation_role(self) -> typing.Optional[_Role_e8c6e11f]:
        '''Role for cross account zone delegation.'''
        return typing.cast(typing.Optional[_Role_e8c6e11f], jsii.get(self, "crossAccountZoneDelegationRole"))


class CaaAmazonRecord(
    CaaRecord,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_route53.CaaAmazonRecord",
):
    '''A DNS Amazon CAA record.

    A CAA record to restrict certificate authorities allowed
    to issue certificates for a domain to Amazon only.

    :resource: AWS::Route53::RecordSet
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        import aws_cdk as cdk
        from aws_cdk import aws_route53 as route53
        
        # geo_location: route53.GeoLocation
        # hosted_zone: route53.HostedZone
        
        caa_amazon_record = route53.CaaAmazonRecord(self, "MyCaaAmazonRecord",
            zone=hosted_zone,
        
            # the properties below are optional
            comment="comment",
            delete_existing=False,
            geo_location=geo_location,
            multi_value_answer=False,
            record_name="recordName",
            region="region",
            set_identifier="setIdentifier",
            ttl=cdk.Duration.minutes(30),
            weight=123
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        zone: IHostedZone,
        comment: typing.Optional[builtins.str] = None,
        delete_existing: typing.Optional[builtins.bool] = None,
        geo_location: typing.Optional[GeoLocation] = None,
        multi_value_answer: typing.Optional[builtins.bool] = None,
        record_name: typing.Optional[builtins.str] = None,
        region: typing.Optional[builtins.str] = None,
        set_identifier: typing.Optional[builtins.str] = None,
        ttl: typing.Optional[_Duration_4839e8c3] = None,
        weight: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param zone: The hosted zone in which to define the new record.
        :param comment: A comment to add on the record. Default: no comment
        :param delete_existing: Whether to delete the same record set in the hosted zone if it already exists (dangerous!). This allows to deploy a new record set while minimizing the downtime because the new record set will be created immediately after the existing one is deleted. It also avoids "manual" actions to delete existing record sets. .. epigraph:: **N.B.:** this feature is dangerous, use with caution! It can only be used safely when ``deleteExisting`` is set to ``true`` as soon as the resource is added to the stack. Changing an existing Record Set's ``deleteExisting`` property from ``false -> true`` after deployment will delete the record! Default: false
        :param geo_location: The geographical origin for this record to return DNS records based on the user's location.
        :param multi_value_answer: Whether to return multiple values, such as IP addresses for your web servers, in response to DNS queries. Default: false
        :param record_name: The subdomain name for this record. This should be relative to the zone root name. For example, if you want to create a record for acme.example.com, specify "acme". You can also specify the fully qualified domain name which terminates with a ".". For example, "acme.example.com.". Default: zone root
        :param region: The Amazon EC2 Region where you created the resource that this resource record set refers to. The resource typically is an AWS resource, such as an EC2 instance or an ELB load balancer, and is referred to by an IP address or a DNS domain name, depending on the record type. When Amazon Route 53 receives a DNS query for a domain name and type for which you have created latency resource record sets, Route 53 selects the latency resource record set that has the lowest latency between the end user and the associated Amazon EC2 Region. Route 53 then returns the value that is associated with the selected resource record set. Default: - Do not set latency based routing
        :param set_identifier: A string used to distinguish between different records with the same combination of DNS name and type. It can only be set when either weight or geoLocation is defined. This parameter must be between 1 and 128 characters in length. Default: - Auto generated string
        :param ttl: The resource record cache time to live (TTL). Default: Duration.minutes(30)
        :param weight: Among resource record sets that have the same combination of DNS name and type, a value that determines the proportion of DNS queries that Amazon Route 53 responds to using the current resource record set. Route 53 calculates the sum of the weights for the resource record sets that have the same combination of DNS name and type. Route 53 then responds to queries based on the ratio of a resource's weight to the total. This value can be a number between 0 and 255. Default: - Do not set weighted routing
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f189380057459afbeff6d38749625e3756c4572dec90f74ca7a400dcb8ac94da)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CaaAmazonRecordProps(
            zone=zone,
            comment=comment,
            delete_existing=delete_existing,
            geo_location=geo_location,
            multi_value_answer=multi_value_answer,
            record_name=record_name,
            region=region,
            set_identifier=set_identifier,
            ttl=ttl,
            weight=weight,
        )

        jsii.create(self.__class__, self, [scope, id, props])


__all__ = [
    "ARecord",
    "ARecordAttrs",
    "ARecordProps",
    "AaaaRecord",
    "AaaaRecordProps",
    "AliasRecordTargetConfig",
    "CaaAmazonRecord",
    "CaaAmazonRecordProps",
    "CaaRecord",
    "CaaRecordProps",
    "CaaRecordValue",
    "CaaTag",
    "CfnCidrCollection",
    "CfnCidrCollectionProps",
    "CfnDNSSEC",
    "CfnDNSSECProps",
    "CfnHealthCheck",
    "CfnHealthCheckProps",
    "CfnHostedZone",
    "CfnHostedZoneProps",
    "CfnKeySigningKey",
    "CfnKeySigningKeyProps",
    "CfnRecordSet",
    "CfnRecordSetGroup",
    "CfnRecordSetGroupProps",
    "CfnRecordSetProps",
    "CnameRecord",
    "CnameRecordProps",
    "CommonHostedZoneProps",
    "Continent",
    "CrossAccountZoneDelegationRecord",
    "CrossAccountZoneDelegationRecordProps",
    "DsRecord",
    "DsRecordProps",
    "GeoLocation",
    "HostedZone",
    "HostedZoneAttributes",
    "HostedZoneProps",
    "HostedZoneProviderProps",
    "IAliasRecordTarget",
    "IHostedZone",
    "IKeySigningKey",
    "IPrivateHostedZone",
    "IPublicHostedZone",
    "IRecordSet",
    "KeySigningKey",
    "KeySigningKeyAttributes",
    "KeySigningKeyProps",
    "KeySigningKeyStatus",
    "MxRecord",
    "MxRecordProps",
    "MxRecordValue",
    "NsRecord",
    "NsRecordProps",
    "PrivateHostedZone",
    "PrivateHostedZoneProps",
    "PublicHostedZone",
    "PublicHostedZoneAttributes",
    "PublicHostedZoneProps",
    "RecordSet",
    "RecordSetOptions",
    "RecordSetProps",
    "RecordTarget",
    "RecordType",
    "SrvRecord",
    "SrvRecordProps",
    "SrvRecordValue",
    "TxtRecord",
    "TxtRecordProps",
    "VpcEndpointServiceDomainName",
    "VpcEndpointServiceDomainNameProps",
    "ZoneDelegationOptions",
    "ZoneDelegationRecord",
    "ZoneDelegationRecordProps",
    "ZoneSigningOptions",
]

publication.publish()

def _typecheckingstub__387b486cd004971b31128e4032ad0c37e74eea08888305d1660803aa68158e99(
    *,
    dns_name: builtins.str,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__355c998e142d682fe0d90395cdf5ae7e566c2548633a9f8a48ab352707f13361(
    *,
    flag: jsii.Number,
    tag: CaaTag,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__720011c856c32f90a3b681a917c19dc88c61ef6e87f090867debab9dfca1faf1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCidrCollection.LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__865b77e8db2784e62d9e80de9ac08effc2203aeaed71fa8db00bdb6a95e02f25(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d0eb630c9850982ace69736bf02f1ce226a32e6e83e5ba91717759cff2a08f89(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e50d4b886f4c0718571d1dc70a97b0a1880f116a72668e2684b19ec718caa527(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d1ed42461528e34721c33b3493a2297bae3e47c0fe29589882e2a685605d968(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnCidrCollection.LocationProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cfc9caaf4289bb14df94cc4a6cf31b8d96395a13a1721c994701cc500d10b0d(
    *,
    cidr_list: typing.Sequence[builtins.str],
    location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24748dfd73812a9d4b13a11033c37a21e1e477a613964e42f30b373347e6bd62(
    *,
    name: builtins.str,
    locations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCidrCollection.LocationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e9e7f472bcf8cedfa8847e5068cd1eac8f74894399d2da52c0efb5f9d06b2bb(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec856d544beda6c45f1608de4feeffbddf087e8459029522c89b9df33f5cb959(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6989c5ddbfcb06ca392c2069a93d1577d4cf37dbb55219f8b2099854e7e6865(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__49aa879587d46704e9e1a930ff6b1127ca5bcd3a356f6eb50d8324ca68c299b4(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2167da58835c803c2916942ed2ea650abb900936cf0014848489e6c72545f5ed(
    *,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__469f7fe3ad975c091ea64f8ce59060016c4769f6532660a91964f093088b495c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    health_check_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.HealthCheckConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    health_check_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.HealthCheckTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__92eef426989e6d56f38b29af5b8a36178998c16c96fb7222ce9f5538f6972709(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a64c35de99e287eed1f250bb5b41772f3dbba1a8ad5b6ced21bbde215943f8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8b0df7baae49dfed1fb95576ba5c0e5d51660f268bef2a4d82fca32324f94689(
    value: typing.Union[_IResolvable_da3f097b, CfnHealthCheck.HealthCheckConfigProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1d1493e762a114933a5a3775c215007c8d522e932362ff7c530eb00b515208ff(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHealthCheck.HealthCheckTagProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e113166210d02eb6e0f8c59a042f052d80d619370b1e9fe97a7a04b51014736(
    *,
    name: builtins.str,
    region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5f6870a18d2b0b32e1b106470763dd03bb4bfa75e0234e29a176b8b5127252e0(
    *,
    type: builtins.str,
    alarm_identifier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.AlarmIdentifierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    child_health_checks: typing.Optional[typing.Sequence[builtins.str]] = None,
    enable_sni: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    failure_threshold: typing.Optional[jsii.Number] = None,
    fully_qualified_domain_name: typing.Optional[builtins.str] = None,
    health_threshold: typing.Optional[jsii.Number] = None,
    insufficient_data_health_status: typing.Optional[builtins.str] = None,
    inverted: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    ip_address: typing.Optional[builtins.str] = None,
    measure_latency: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    port: typing.Optional[jsii.Number] = None,
    regions: typing.Optional[typing.Sequence[builtins.str]] = None,
    request_interval: typing.Optional[jsii.Number] = None,
    resource_path: typing.Optional[builtins.str] = None,
    routing_control_arn: typing.Optional[builtins.str] = None,
    search_string: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b181f58da0d2eb6f8c9ba8be7f7b44f29a68b4d09e2f4c600ab9522e6f52f880(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcc59bb963f4ce3a4eb461ecda6f194c9faa6eea0ca5960c91dfd950e626f687(
    *,
    health_check_config: typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.HealthCheckConfigProperty, typing.Dict[builtins.str, typing.Any]]],
    health_check_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHealthCheck.HealthCheckTagProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07dce28bc78bd7a648e7920a0cb1bee52b579eae30c6d32918696dd2fecf73a0(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.HostedZoneConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hosted_zone_tags: typing.Optional[typing.Sequence[typing.Union[CfnHostedZone.HostedZoneTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    query_logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.QueryLoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpcs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.VPCProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ec471122074c4efc9cfaeb7b7bef0731889f8080ae94fce69befda5f9fe2e7af(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ef86462d5cfa65a428a6e6bb1b1ba218d87770c0e1448ff8d57375ca2a36ae7(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e764c4ae257c91c5d5b032fbe4eb718b4851ccc5750ef5bd3b5214ef2b4684fd(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHostedZone.HostedZoneConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93e68861780d2e75a54677985f3c250e924418dc9e1ac1cc200b770e633acbb6(
    value: typing.Optional[typing.List[CfnHostedZone.HostedZoneTagProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__91099dfc3159698491b9498cddba1ba706c12aeede11ee9ccadf937019c2ae08(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02d1784db152ce69ef63512574d41672ddd53e2038e23c71ff72325772d8b489(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnHostedZone.QueryLoggingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45fa6589ea7645f299a1666ba66ea7f49172916fae56fe49b48ee2d8bfa87241(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnHostedZone.VPCProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b9b576716f26dcf7d2edeb0bc854e42f45e229b4fdb03469e0a6e4aa92f0c562(
    *,
    comment: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ab436cec7f17cd6450fc80b9013e4f05f3f7a983561430595251215b5aedec6(
    *,
    key: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3de80e7a9d7826feae12622cf83906c147b708a387e427ae161c27ac169ea16a(
    *,
    cloud_watch_logs_log_group_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c68e5afe07b3a7edc63a606f85f787c4486a2bfba1793f83271989294f5d6970(
    *,
    vpc_id: builtins.str,
    vpc_region: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__490d21becaf73ea78f8b34688d2d62e4e21d941f510e74d0a5acce1c9a8a35c3(
    *,
    hosted_zone_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.HostedZoneConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    hosted_zone_tags: typing.Optional[typing.Sequence[typing.Union[CfnHostedZone.HostedZoneTagProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    query_logging_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.QueryLoggingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vpcs: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnHostedZone.VPCProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1ab2cf8ecb830d1da730f1aa8733016826e21289a18b31b5c2960242217b6d2d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone_id: builtins.str,
    key_management_service_arn: builtins.str,
    name: builtins.str,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6cd424602d0e47520e23aa4bb0661d6d253dfaa1526f46b316cc886c1c8e3c90(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a974a23e0b44cc31e19609aafb595755d873d5b149a168373eca42644ebb067(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a977d3e0b2b3f9a9e1ffa361297317c52032e041b63d5aea96d7b3236e1bcc76(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b11e2fadcc2e7f8dd0b969ae638b6fef820af613ac524490a21fcfa87cbe4b1b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c99ca2799db6059925703f6f02ff9fa298bf7e6106b621b1f66a86e2928f1a56(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8a53087887c17259968953d4112cc4979b6d97d83c742c614204a0840acd1951(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__34f881609091b0893ac028adbb4be46f434c735b3d01e67b1aefcf17bc0abb02(
    *,
    hosted_zone_id: builtins.str,
    key_management_service_arn: builtins.str,
    name: builtins.str,
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5260f62d2297374b2126da361d614f7922d306048a751f4287d4f7b25251b21f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    type: builtins.str,
    alias_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.AliasTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cidr_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.CidrRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    comment: typing.Optional[builtins.str] = None,
    failover: typing.Optional[builtins.str] = None,
    geo_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.GeoLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    geo_proximity_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.GeoProximityLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_id: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    region: typing.Optional[builtins.str] = None,
    resource_records: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[builtins.str] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3b594e45af3ec7b4a87f2e38151e582ff1da92bd5457b214b477cfd403181bea(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df3adfbdf92c6a814f5e524f14898f0c7ffdd8d142085c462e1fe287a77fe1ba(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__173457195308ceadf9faa78064a52b9ebc4a356fcff5446dce5527a0f82366c1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0d764bdec1a7fb5aef453f572d560d1b8aed69fb8dcfec021e5660608a78cd63(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0a16cf391736226a70d1a59be2ffd652193be54e61b33e07b2b502b7444ebc0(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.AliasTargetProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9573d618d7f59fad50ecf9e676d892ccfe65d8be595e465b068eec35f7931458(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.CidrRoutingConfigProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8e87d623f2ac71368cf9931ccdeb8214817a43ef5c3db34b4027a16981eba4e(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__79006fc8c23dbed3ebc1e2c4a59dbaef71eada9146612d1d44ad17bf006a1f70(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e7b257b8973ecbc1eff717cef5d9e9a86a7e93521a1f67acf22b2e8461e1b642(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.GeoLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ac8d1aee0fc5c4e2eba653391bb8b61826a08b6708db398bae5b22b4e13fcf05(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnRecordSet.GeoProximityLocationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6008831249a60a522c31e8ed28371a87feee29b69976deadfbbb7939c49e5a0a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3afc428680f9605da623df52766517926597c1cedf85b11836d156e5b0492fff(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a7ed3b70491b7ea26f2195c97e2146c9f0e7366194f534e8a71a2dbcde9c7634(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc829fb8c432409e77ff577c111238c3b8554f78a040b7ecdffeb62edb27cf24(
    value: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e8e56811d430d9adaea085bb5b15a937d1a1a06eb6f77c3eb66770f6f8b5073(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b020353bfb0b9ee7bc698effc5888164835bd548ead89bdc9fd99a31474d7cd(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b95c315d1a586fa24b707f1b31210ab6858b88d54fc32c5fab80e08220930c7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6235e7f8dad691c76887db81a7b5573fb5ed22b4706905208bbca87c9087002d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__166c0517a88d98d1b7fe07fa34082de049ec954fde21b5c1376524e3c7146134(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1143e059c44e7a7f16565322a7c9305d2eb0d507ef54d57d3dab326b7f69648(
    *,
    dns_name: builtins.str,
    hosted_zone_id: builtins.str,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc6569566583d30a42a983532b11cef6d6313d0666f46f50d599eabd1e5d4837(
    *,
    collection_id: builtins.str,
    location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29683fc8d824969c71955a00cda4d10dde445180eb16e6a17c990ec1252a893a(
    *,
    latitude: builtins.str,
    longitude: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc6e59779782a9e8ecceda7a67dfa9c21d257bdac8db0558def7239dd1d167a5(
    *,
    continent_code: typing.Optional[builtins.str] = None,
    country_code: typing.Optional[builtins.str] = None,
    subdivision_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9bbef31bd9d19fea78e067206e8cea17ada33bda9853588d7a99d66d91f15555(
    *,
    aws_region: typing.Optional[builtins.str] = None,
    bias: typing.Optional[jsii.Number] = None,
    coordinates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.CoordinatesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    local_zone_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__88410dc2301961a44d6910ee0de13aa8273ce0fa1b93daca4141c18b5fa3d03b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    comment: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    record_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.RecordSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48ca705812043ff12ec21cb444124f3be1a7ab3431425e66de023724f6a298c6(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14a869585b3959be67c777f304411c15da58891cbbb6c3ffb41dcdf3dade3c2d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c97ac966771356be453e30c879df180c0ddc8815675496dd0165606bedf4c9e7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1424150c5729da24929b30da713b6d33d1015579282157aecedd97e989f6938f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9f9f2119ab4a72afe07344595f0bb4fb1b9015e2e273b9dea6abcfbafa762ed4(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fb00744f239be86927ab07333f9aa97d44af1dbaabd6b50dc186a5a6f344824(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnRecordSetGroup.RecordSetProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__47266159f3c04590ed7485f833b949a10c311800ebfa01351a5f55ffc0c4fcfe(
    *,
    dns_name: builtins.str,
    hosted_zone_id: builtins.str,
    evaluate_target_health: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25a6f79ee876d62204e1e24470518bddae21e675bc5258cc7766c8a345ae1a2(
    *,
    collection_id: builtins.str,
    location_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ebaae8a752b3b1dfff4bf671352e45cbd7c98fa0058ccfb5170085a3e53f8cb(
    *,
    latitude: builtins.str,
    longitude: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2815193fa29c379ea003dd9391a70d63f49989043e7f24e220ccebb1143c1026(
    *,
    continent_code: typing.Optional[builtins.str] = None,
    country_code: typing.Optional[builtins.str] = None,
    subdivision_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5430af5a2d4636b1244b53f4c6759f6d1ffde530908e449cf4bc90b0d9de5ec8(
    *,
    aws_region: typing.Optional[builtins.str] = None,
    bias: typing.Optional[jsii.Number] = None,
    coordinates: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.CoordinatesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    local_zone_group: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__11ff291a729fd95a26a222e98e883239191c114a9dd6e70516ac2fe433d4b95d(
    *,
    name: builtins.str,
    type: builtins.str,
    alias_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.AliasTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cidr_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.CidrRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    failover: typing.Optional[builtins.str] = None,
    geo_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.GeoLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    geo_proximity_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.GeoProximityLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_id: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    region: typing.Optional[builtins.str] = None,
    resource_records: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[builtins.str] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__550eb58db998305b4dd78ae1bd39e80af0e9376310d796614d4bcd99a1dd82b6(
    *,
    comment: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    record_sets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSetGroup.RecordSetProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07806684fd0bcb683322d42ae67181582216fa4e1371a7133012bf4898a3d7d5(
    *,
    name: builtins.str,
    type: builtins.str,
    alias_target: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.AliasTargetProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    cidr_routing_config: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.CidrRoutingConfigProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    comment: typing.Optional[builtins.str] = None,
    failover: typing.Optional[builtins.str] = None,
    geo_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.GeoLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    geo_proximity_location: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnRecordSet.GeoProximityLocationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_id: typing.Optional[builtins.str] = None,
    hosted_zone_id: typing.Optional[builtins.str] = None,
    hosted_zone_name: typing.Optional[builtins.str] = None,
    multi_value_answer: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    region: typing.Optional[builtins.str] = None,
    resource_records: typing.Optional[typing.Sequence[builtins.str]] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[builtins.str] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3c0a60680828ad59f14d241729df78a8969a23a13155e2327837897bb4545149(
    *,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f4115d484cd67a76fbe1e4ea37dbe01bb97e2d8816dda058f0ba904769173c46(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    delegated_zone: IHostedZone,
    delegation_role: _IRole_235f5d8e,
    assume_role_region: typing.Optional[builtins.str] = None,
    parent_hosted_zone_id: typing.Optional[builtins.str] = None,
    parent_hosted_zone_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2f26cbe17fefc3bd3765d1fcc9084ddb3aa18526e669cad5ba4011ccbc2b3d7f(
    *,
    delegated_zone: IHostedZone,
    delegation_role: _IRole_235f5d8e,
    assume_role_region: typing.Optional[builtins.str] = None,
    parent_hosted_zone_id: typing.Optional[builtins.str] = None,
    parent_hosted_zone_name: typing.Optional[builtins.str] = None,
    removal_policy: typing.Optional[_RemovalPolicy_9f93c814] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__082626770a86bf939ef1cae8f42886e56e872994e6ff75c90019d66a2dbbbbbe(
    continent_code: Continent,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__634d2e960bf8ca83032f62602012c316f523f02ccdc11b960ac7a1818f6088f9(
    country_code: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13d57b34e60c4361c1d97c820e69f3a9c16ba208b123a261ee081931be34cf02(
    subdivision_code: builtins.str,
    country_code: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5fad1cc6999b94bd845480426db92d5bb3ac0208bca78f9cf984e5ce4ccd701(
    *,
    hosted_zone_id: builtins.str,
    zone_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f1711cf7af2ab26c7be8b7aad54fc7158d3e50d0205dd9b87989812878e88e96(
    *,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    vpcs: typing.Optional[typing.Sequence[_IVpc_f30d5663]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77dfce5cb4e026f34aa8dfde1dcd4aacac66aa9d7b2466bbb97ebb9db7b5de4c(
    *,
    domain_name: builtins.str,
    private_zone: typing.Optional[builtins.bool] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__162b54c0ae9f493edc12c5cba6aa323333c184d03d9332edaab8e4f75c7f74cd(
    record: IRecordSet,
    zone: typing.Optional[IHostedZone] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97ae48bcbfd92ef96c96db6d1d972ddd9b889f01bba1ab2a3819d9faa9eb4a18(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__63b944f82a919a5a1fc9b8c1ec885ffe1d509c5cec2bb324d9b5ed7df171b437(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone: IHostedZone,
    kms_key: _IKey_5f11635f,
    key_signing_key_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[KeySigningKeyStatus] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9aae6d3147d941495289a363f03a080316f20c479e0fa8646cf10ec995d1635a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone: IHostedZone,
    key_signing_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1262fd4a880b25e9ef115da3b6b790a7b24acf9d121372595ab3087a5442d2(
    *,
    hosted_zone: IHostedZone,
    key_signing_key_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3e92b54737c8cb2969b649108716a37fd8e380a8e41cfefef3229c1d92acdf40(
    *,
    hosted_zone: IHostedZone,
    kms_key: _IKey_5f11635f,
    key_signing_key_name: typing.Optional[builtins.str] = None,
    status: typing.Optional[KeySigningKeyStatus] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2600b3ca2027fe7d531738c20a112cef3282c7ef114758a51ee3863608c7aa72(
    *,
    host_name: builtins.str,
    priority: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3dc8529d9382b27a0613e5ea30e125e3af07550dc23754412bd1f99368cfc62d(
    *,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    vpc: _IVpc_f30d5663,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7cb1c7902828774b44c85c0a2b07314a2458b9752803df59926e9e7cd9f9b4f4(
    *,
    hosted_zone_id: builtins.str,
    zone_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b51e553dd18a8a033ac24f091492db4b2bc8c672421ced82613174be3995dcdf(
    *,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
    caa_amazon: typing.Optional[builtins.bool] = None,
    cross_account_zone_delegation_principal: typing.Optional[_IPrincipal_539bb2fd] = None,
    cross_account_zone_delegation_role_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b92f4bc0484ad6fe8cce3c7e37b4ee3cd051b8f325d16efd23f92476703d09ac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    record_type: RecordType,
    target: RecordTarget,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c44f39638a001e90bc1175667e4764c4cbde27cade202d52a4f4d87246c57781(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__038200686c47ef30f81bc5289a6235e766372281295129670053b793d545dfca(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    record_type: RecordType,
    target: RecordTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93edac882a461453a0fceb6451d524a95c372910790d1fb9ddc60080e15f3ff7(
    values: typing.Optional[typing.Sequence[builtins.str]] = None,
    alias_target: typing.Optional[IAliasRecordTarget] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__97eabbebabcd2acf6973571f8976591eb52a27f549b4c3abd23d91ac7ceba37e(
    alias_target: IAliasRecordTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22a2cb83387a6785138daa53fc8099f2fd85af4d7ddd997da2d563ba3e4801d9(
    *ip_addresses: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9f2d233732c1eae777eca34e2d8eeada36e28a2ad8db6f1b5673ec203a071c(
    *values: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d52a70fbe22ca5e13acce72254719ea0dd37b436de0640b65774aadd9c6fe954(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    values: typing.Sequence[typing.Union[SrvRecordValue, typing.Dict[builtins.str, typing.Any]]],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__803828161f541995c058596dab53102f2eccd14ba565bbe715a5ac29353f6db9(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    values: typing.Sequence[typing.Union[SrvRecordValue, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6c9da4f91ee9021e13a985564e2b781386a5d9cfc61b96742f9b71034f358a9(
    *,
    host_name: builtins.str,
    port: jsii.Number,
    priority: jsii.Number,
    weight: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__df1e0c1447d860a09246a7ec54507ca123346e57365df024460258839b4bd48b(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    values: typing.Sequence[builtins.str],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1925dd23d881cbbf99625b9a5fe0ef65b92a92359376c46e49b6690f1a4a9dab(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0f1e0787b803b3e6b7bc1893af9e2bd854989d8ecc1ee95b572a359f686c4bd(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    endpoint_service: _IVpcEndpointService_4ddddab0,
    public_hosted_zone: IPublicHostedZone,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb8d9c4cf0d124563d17362021e80fc8fa146791616e752bd4a8ccb6df767280(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6355fbcde34ee994597b3b647c64b65eb32833843e3bc72c5479e8a6ad7fb623(
    *,
    domain_name: builtins.str,
    endpoint_service: _IVpcEndpointService_4ddddab0,
    public_hosted_zone: IPublicHostedZone,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0efd84c1e481104af0fc88e047ca0cffa51a834020eec2f9c9cfee5df2642f84(
    *,
    comment: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1f8360676c13e2167bb58d36e1b6384ba70f036979aa9c80cac046e12779c594(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name_servers: typing.Sequence[builtins.str],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__240a965753acb9488d02c120074027364f5e85a8ec585205a863174feadd7582(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    name_servers: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c024f1ad9949a250bc85eb88751e2c625dd1a6679c33a35a4add759a0404b95c(
    *,
    kms_key: _IKey_5f11635f,
    key_signing_key_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca2e60ba6b2baeeff2cc875c86af94b4b26d6f11c1cfcca09280ac533b792230(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target: RecordTarget,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c76ad72e64542d58d5e33c28ccaca560dac09b21c920d094b7a0c2386fe42886(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target_dns: builtins.str,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__514d7eccc21be019febe80e121fd7d979162668b63cb99051c629ef087f5fe9a(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    target_dns: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a73a5c86411a0d853fcfad820ed58f5a5c19df65a7b2756560958db5cbe36569(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    target: RecordTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d5345c027ebd51f32f58fdeb055904a5c4dd3f5523f55954f8a191ae8bf29ee(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    target: RecordTarget,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c051ff70083b2ae68889d3f02be8344125acf64b4768d5f5df3298ba8a8d6a32(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    target: RecordTarget,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14055fdb7d9f4b55091295996ec92db8d73fa789a21fca2664da1242ae89f859(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3a2502cdc1fe021e837217ab0d96b9fa6ea450a68c089482935b695f7943ff3c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    values: typing.Sequence[typing.Union[CaaRecordValue, typing.Dict[builtins.str, typing.Any]]],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__349a94b990ddb833b270dc692692a8b37187c6f17114e02514f44accfb8de443(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    values: typing.Sequence[typing.Union[CaaRecordValue, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8dfccd8504bb3c0a779b42a665f362282b1083fe52a95b450d1ac1eb3622c80(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__43b5fc8ccb719e2580c804225e8258b57b1700a701203416558eb2d76a86f86f(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    domain_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24205d1a44dcefb992b7bd9b6d91d8b6396f8498224c30876fe8a0673c4dc790(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    values: typing.Sequence[builtins.str],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f86f16d9f2de8fe03cc1189a56a86c4888d20f69dc0f241aa21b50fdf34d4645(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1e5b9f9d7aa4bc16fced3cc22e63b14cbf590c498be223e588483a72fb0b4233(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    vpcs: typing.Optional[typing.Sequence[_IVpc_f30d5663]] = None,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__24a9e3565a26d4d6d8a3c0d4406ef8f6cce5e0e48dc1145dc090f7db4581c0ac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone_id: builtins.str,
    zone_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dc5da03bfe3e7000e80ebfbe7cb3c5c23ab3e97f4e6c670a8eb0ef036d099c78(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bdb223a28519af08e8a4de265a9236844a06052261acd92d02cc9634acf56a8c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    domain_name: builtins.str,
    private_zone: typing.Optional[builtins.bool] = None,
    vpc_id: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5c63a3fccbc53f093c8e4d46a2848bf83b386d2ca5206e82ecd8ecd3d61a0ccb(
    vpc: _IVpc_f30d5663,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8e256ece77d93011f031e05a119f03b248a4b68d267c298052b0cea131943ab5(
    grantee: _IGrantable_71c4f5de,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__615153e942ef5cdcb0022d4565e0ec8b8c5554594bfe7221366ad5c83a3b679e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    values: typing.Sequence[typing.Union[MxRecordValue, typing.Dict[builtins.str, typing.Any]]],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b259122626a3ba94eebff0b5f692944df4aa55dc550b7d113eec491e1c57307d(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    values: typing.Sequence[typing.Union[MxRecordValue, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f3bbcb4bd5bcd8978ae60eaac5ea2c6ab0bb8357a389e9b981e63291cdcc3ab(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    values: typing.Sequence[builtins.str],
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__33cda5fac8572316158161da713e2ceea9d3f7f56b5ee9a2a25acf331e737e86(
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5513b0f840f5eafaeee3e3a9c7776204d075ee417c3cce2c38a14213814eb75(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    vpc: _IVpc_f30d5663,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b376eac72cdb24a91e277cf6c9c277d3ed571280fb5b90bd23b7e1e1d5f88dac(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    private_hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6f67fd33cdf6043dd6c0a287fb380d5704e93c1d3a80eabf2da05bc363d681c5(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    caa_amazon: typing.Optional[builtins.bool] = None,
    cross_account_zone_delegation_principal: typing.Optional[_IPrincipal_539bb2fd] = None,
    cross_account_zone_delegation_role_name: typing.Optional[builtins.str] = None,
    zone_name: builtins.str,
    add_trailing_dot: typing.Optional[builtins.bool] = None,
    comment: typing.Optional[builtins.str] = None,
    query_logs_log_group_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d8382b2aa9cdf1e089241eda9e9d1e17d1003056fa5fe78dfbc64017f2f83d5f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    hosted_zone_id: builtins.str,
    zone_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__919d0fe07f8f277a34fdf761ddcb6a1b0c7a81c9d3bd726e69bc5c6b6fbcd53e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    public_hosted_zone_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca14815188563abe1058cb85558750303980b4542afbe253885064f9c3fff98c(
    delegate: IPublicHostedZone,
    *,
    comment: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3e8e9627c25114e462dc3af379684d0d3fba38262bae897187e8d8faa087102(
    _vpc: _IVpc_f30d5663,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f189380057459afbeff6d38749625e3756c4572dec90f74ca7a400dcb8ac94da(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    zone: IHostedZone,
    comment: typing.Optional[builtins.str] = None,
    delete_existing: typing.Optional[builtins.bool] = None,
    geo_location: typing.Optional[GeoLocation] = None,
    multi_value_answer: typing.Optional[builtins.bool] = None,
    record_name: typing.Optional[builtins.str] = None,
    region: typing.Optional[builtins.str] = None,
    set_identifier: typing.Optional[builtins.str] = None,
    ttl: typing.Optional[_Duration_4839e8c3] = None,
    weight: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass
