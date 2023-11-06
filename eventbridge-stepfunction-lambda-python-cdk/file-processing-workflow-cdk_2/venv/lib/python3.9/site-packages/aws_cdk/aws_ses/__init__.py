'''
# Amazon Simple Email Service Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

## Email receiving

Create a receipt rule set with rules and actions (actions can be found in the
`aws-cdk-lib/aws-ses-actions` package):

```python
import aws_cdk.aws_s3 as s3
import aws_cdk.aws_ses_actions as actions


bucket = s3.Bucket(self, "Bucket")
topic = sns.Topic(self, "Topic")

ses.ReceiptRuleSet(self, "RuleSet",
    rules=[ses.ReceiptRuleOptions(
        recipients=["hello@aws.com"],
        actions=[
            actions.AddHeader(
                name="X-Special-Header",
                value="aws"
            ),
            actions.S3(
                bucket=bucket,
                object_key_prefix="emails/",
                topic=topic
            )
        ]
    ), ses.ReceiptRuleOptions(
        recipients=["aws.com"],
        actions=[
            actions.Sns(
                topic=topic
            )
        ]
    )
    ]
)
```

Alternatively, rules can be added to a rule set:

```python
rule_set = ses.ReceiptRuleSet(self, "RuleSet")

aws_rule = rule_set.add_rule("Aws",
    recipients=["aws.com"]
)
```

And actions to rules:

```python
import aws_cdk.aws_ses_actions as actions

# aws_rule: ses.ReceiptRule
# topic: sns.Topic

aws_rule.add_action(actions.Sns(
    topic=topic
))
```

When using `addRule`, the new rule is added after the last added rule unless `after` is specified.

### Drop spams

A rule to drop spam can be added by setting `dropSpam` to `true`:

```python
ses.ReceiptRuleSet(self, "RuleSet",
    drop_spam=True
)
```

This will add a rule at the top of the rule set with a Lambda action that stops processing messages that have at least one spam indicator. See [Lambda Function Examples](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda-example-functions.html).

### Receipt filter

Create a receipt filter:

```python
ses.ReceiptFilter(self, "Filter",
    ip="1.2.3.4/16"
)
```

An allow list filter is also available:

```python
ses.AllowListReceiptFilter(self, "AllowList",
    ips=["10.0.0.0/16", "1.2.3.4/16"
    ]
)
```

This will first create a block all filter and then create allow filters for the listed ip addresses.

## Email sending

### Dedicated IP pools

When you create a new Amazon SES account, your emails are sent from IP addresses that are shared with other
Amazon SES users. For [an additional monthly charge](https://aws.amazon.com/ses/pricing/), you can lease
dedicated IP addresses that are reserved for your exclusive use.

Use the `DedicatedIpPool` construct to create a pool of dedicated IP addresses:

```python
ses.DedicatedIpPool(self, "Pool")
```

The pool can then be used in a configuration set.

### Configuration sets

Configuration sets are groups of rules that you can apply to your verified identities. A verified identity is
a domain, subdomain, or email address you use to send email through Amazon SES. When you apply a configuration
set to an email, all of the rules in that configuration set are applied to the email.

Use the `ConfigurationSet` construct to create a configuration set:

```python
# my_pool: ses.IDedicatedIpPool


ses.ConfigurationSet(self, "ConfigurationSet",
    custom_tracking_redirect_domain="track.cdk.dev",
    suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
    tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
    dedicated_ip_pool=my_pool
)
```

Use `addEventDestination()` to publish email sending events to Amazon SNS or Amazon CloudWatch:

```python
# my_configuration_set: ses.ConfigurationSet
# my_topic: sns.Topic


my_configuration_set.add_event_destination("ToSns",
    destination=ses.EventDestination.sns_topic(my_topic)
)
```

### Email identity

In Amazon SES, a verified identity is a domain or email address that you use to send or receive email. Before you
can send an email using Amazon SES, you must create and verify each identity that you're going to use as a `From`,
`Source`, `Sender`, or `Return-Path` address. Verifying an identity with Amazon SES confirms that you own it and
helps prevent unauthorized use.

To verify an identity for a hosted zone, you create an `EmailIdentity`:

```python
# my_hosted_zone: route53.IPublicHostedZone


identity = ses.EmailIdentity(self, "Identity",
    identity=ses.Identity.public_hosted_zone(my_hosted_zone),
    mail_from_domain="mail.cdk.dev"
)
```

By default, [Easy DKIM](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html) with
a 2048-bit DKIM key is used.

You can instead configure DKIM authentication by using your own public-private key pair. This process is known
as [Bring Your Own DKIM (BYODKIM)](https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-bring-your-own.html):

```python
# my_hosted_zone: route53.IPublicHostedZone


ses.EmailIdentity(self, "Identity",
    identity=ses.Identity.public_hosted_zone(my_hosted_zone),
    dkim_identity=ses.DkimIdentity.byo_dkim(
        private_key=SecretValue.secrets_manager("dkim-private-key"),
        public_key="...base64-encoded-public-key...",
        selector="selector"
    )
)
```

When using `publicHostedZone()` for the identity, all necessary Amazon Route 53 records are created automatically:

* CNAME records for Easy DKIM
* TXT record for BYOD DKIM
* MX and TXT records for the custom MAIL FROM

When working with `domain()`, records must be created manually:

```python
identity = ses.EmailIdentity(self, "Identity",
    identity=ses.Identity.domain("cdk.dev")
)

for record in identity.dkim_records:
    pass
```

### Virtual Deliverability Manager (VDM)

Virtual Deliverability Manager is an Amazon SES feature that helps you enhance email deliverability,
like increasing inbox deliverability and email conversions, by providing insights into your sending
and delivery data, and giving advice on how to fix the issues that are negatively affecting your
delivery success rate and reputation.

Use the `VdmAttributes` construct to configure the Virtual Deliverability Manager for your account:

```python
# Enables engagement tracking and optimized shared delivery by default
ses.VdmAttributes(self, "Vdm")
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
from .. import (
    CfnResource as _CfnResource_9df397a6,
    CfnTag as _CfnTag_f6864754,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    IResource as _IResource_c80c4260,
    ITaggable as _ITaggable_36806126,
    Resource as _Resource_45bc6135,
    SecretValue as _SecretValue_3dd0ddae,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)
from ..aws_route53 import IPublicHostedZone as _IPublicHostedZone_9b6e7da4
from ..aws_sns import ITopic as _ITopic_9eca4852


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.AddHeaderActionConfig",
    jsii_struct_bases=[],
    name_mapping={"header_name": "headerName", "header_value": "headerValue"},
)
class AddHeaderActionConfig:
    def __init__(
        self,
        *,
        header_name: builtins.str,
        header_value: builtins.str,
    ) -> None:
        '''AddHeaderAction configuration.

        :param header_name: The name of the header that you want to add to the incoming message.
        :param header_value: The content that you want to include in the header.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            add_header_action_config = ses.AddHeaderActionConfig(
                header_name="headerName",
                header_value="headerValue"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a170d992f7b65fcd93ee761689bdfa76a44ecd1ea7edfc889f8823c2885ff1ab)
            check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
            check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "header_name": header_name,
            "header_value": header_value,
        }

    @builtins.property
    def header_name(self) -> builtins.str:
        '''The name of the header that you want to add to the incoming message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
        '''
        result = self._values.get("header_name")
        assert result is not None, "Required property 'header_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def header_value(self) -> builtins.str:
        '''The content that you want to include in the header.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
        '''
        result = self._values.get("header_value")
        assert result is not None, "Required property 'header_value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AddHeaderActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class AllowListReceiptFilter(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.AllowListReceiptFilter",
):
    '''An allow list receipt filter.

    :exampleMetadata: infused

    Example::

        ses.AllowListReceiptFilter(self, "AllowList",
            ips=["10.0.0.0/16", "1.2.3.4/16"
            ]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ips: typing.Sequence[builtins.str],
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ips: A list of ip addresses or ranges to allow list.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__945fe453cd006222ecf22c8ccfcce9d99dd299b11a1edd1f0b1103473142ada4)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = AllowListReceiptFilterProps(ips=ips)

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.AllowListReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={"ips": "ips"},
)
class AllowListReceiptFilterProps:
    def __init__(self, *, ips: typing.Sequence[builtins.str]) -> None:
        '''Construction properties for am AllowListReceiptFilter.

        :param ips: A list of ip addresses or ranges to allow list.

        :exampleMetadata: infused

        Example::

            ses.AllowListReceiptFilter(self, "AllowList",
                ips=["10.0.0.0/16", "1.2.3.4/16"
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4b81b4e341d87e039070ac9d2e5681f812a77ceb3a1c4c81466809dabc58bf7d)
            check_type(argname="argument ips", value=ips, expected_type=type_hints["ips"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "ips": ips,
        }

    @builtins.property
    def ips(self) -> typing.List[builtins.str]:
        '''A list of ip addresses or ranges to allow list.'''
        result = self._values.get("ips")
        assert result is not None, "Required property 'ips' is missing"
        return typing.cast(typing.List[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "AllowListReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.BounceActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "message": "message",
        "sender": "sender",
        "smtp_reply_code": "smtpReplyCode",
        "status_code": "statusCode",
        "topic_arn": "topicArn",
    },
)
class BounceActionConfig:
    def __init__(
        self,
        *,
        message: builtins.str,
        sender: builtins.str,
        smtp_reply_code: builtins.str,
        status_code: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''BoundAction configuration.

        :param message: Human-readable text to include in the bounce message.
        :param sender: The email address of the sender of the bounced email. This is the address that the bounce message is sent from.
        :param smtp_reply_code: The SMTP reply code, as defined by RFC 5321.
        :param status_code: The SMTP enhanced status code, as defined by RFC 3463. Default: - No status code.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            bounce_action_config = ses.BounceActionConfig(
                message="message",
                sender="sender",
                smtp_reply_code="smtpReplyCode",
            
                # the properties below are optional
                status_code="statusCode",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0ed2c8bc5cd582573c72e7ec8ce40272efe39b764d2bea49d78fc57f7929e4c0)
            check_type(argname="argument message", value=message, expected_type=type_hints["message"])
            check_type(argname="argument sender", value=sender, expected_type=type_hints["sender"])
            check_type(argname="argument smtp_reply_code", value=smtp_reply_code, expected_type=type_hints["smtp_reply_code"])
            check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "message": message,
            "sender": sender,
            "smtp_reply_code": smtp_reply_code,
        }
        if status_code is not None:
            self._values["status_code"] = status_code
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def message(self) -> builtins.str:
        '''Human-readable text to include in the bounce message.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
        '''
        result = self._values.get("message")
        assert result is not None, "Required property 'message' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def sender(self) -> builtins.str:
        '''The email address of the sender of the bounced email.

        This is the address that the bounce message is sent from.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
        '''
        result = self._values.get("sender")
        assert result is not None, "Required property 'sender' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def smtp_reply_code(self) -> builtins.str:
        '''The SMTP reply code, as defined by RFC 5321.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
        '''
        result = self._values.get("smtp_reply_code")
        assert result is not None, "Required property 'smtp_reply_code' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def status_code(self) -> typing.Optional[builtins.str]:
        '''The SMTP enhanced status code, as defined by RFC 3463.

        :default: - No status code.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
        '''
        result = self._values.get("status_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "BounceActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ByoDkimOptions",
    jsii_struct_bases=[],
    name_mapping={
        "private_key": "privateKey",
        "selector": "selector",
        "public_key": "publicKey",
    },
)
class ByoDkimOptions:
    def __init__(
        self,
        *,
        private_key: _SecretValue_3dd0ddae,
        selector: builtins.str,
        public_key: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Options for BYO DKIM.

        :param private_key: The private key that's used to generate a DKIM signature.
        :param selector: A string that's used to identify a public key in the DNS configuration for a domain.
        :param public_key: The public key. If specified, a TXT record with the public key is created. Default: - the validation TXT record with the public key is not created

        :exampleMetadata: infused

        Example::

            # my_hosted_zone: route53.IPublicHostedZone
            
            
            ses.EmailIdentity(self, "Identity",
                identity=ses.Identity.public_hosted_zone(my_hosted_zone),
                dkim_identity=ses.DkimIdentity.byo_dkim(
                    private_key=SecretValue.secrets_manager("dkim-private-key"),
                    public_key="...base64-encoded-public-key...",
                    selector="selector"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b4e23b7bc7e365a5b875e5ba4ad81ccfb3182ca4059f46dfe11066714a13fffb)
            check_type(argname="argument private_key", value=private_key, expected_type=type_hints["private_key"])
            check_type(argname="argument selector", value=selector, expected_type=type_hints["selector"])
            check_type(argname="argument public_key", value=public_key, expected_type=type_hints["public_key"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "private_key": private_key,
            "selector": selector,
        }
        if public_key is not None:
            self._values["public_key"] = public_key

    @builtins.property
    def private_key(self) -> _SecretValue_3dd0ddae:
        '''The private key that's used to generate a DKIM signature.'''
        result = self._values.get("private_key")
        assert result is not None, "Required property 'private_key' is missing"
        return typing.cast(_SecretValue_3dd0ddae, result)

    @builtins.property
    def selector(self) -> builtins.str:
        '''A string that's used to identify a public key in the DNS configuration for a domain.'''
        result = self._values.get("selector")
        assert result is not None, "Required property 'selector' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def public_key(self) -> typing.Optional[builtins.str]:
        '''The public key.

        If specified, a TXT record with the public key is created.

        :default: - the validation TXT record with the public key is not created
        '''
        result = self._values.get("public_key")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ByoDkimOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet",
):
    '''Configuration sets let you create groups of rules that you can apply to the emails you send using Amazon SES.

    For more information about using configuration sets, see `Using Amazon SES Configuration Sets <https://docs.aws.amazon.com/ses/latest/dg/using-configuration-sets.html>`_ in the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/>`_ .
    .. epigraph::

       *Required permissions:*

       To apply any of the resource options, you will need to have the corresponding AWS Identity and Access Management (IAM) SES API v2 permissions:

       - ``ses:GetConfigurationSet``
       - (This permission is replacing the v1 *ses:DescribeConfigurationSet* permission which will not work with these v2 resource options.)
       - ``ses:PutConfigurationSetDeliveryOptions``
       - ``ses:PutConfigurationSetReputationOptions``
       - ``ses:PutConfigurationSetSendingOptions``
       - ``ses:PutConfigurationSetSuppressionOptions``
       - ``ses:PutConfigurationSetTrackingOptions``

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_configuration_set = ses.CfnConfigurationSet(self, "MyCfnConfigurationSet",
            delivery_options=ses.CfnConfigurationSet.DeliveryOptionsProperty(
                sending_pool_name="sendingPoolName",
                tls_policy="tlsPolicy"
            ),
            name="name",
            reputation_options=ses.CfnConfigurationSet.ReputationOptionsProperty(
                reputation_metrics_enabled=False
            ),
            sending_options=ses.CfnConfigurationSet.SendingOptionsProperty(
                sending_enabled=False
            ),
            suppression_options=ses.CfnConfigurationSet.SuppressionOptionsProperty(
                suppressed_reasons=["suppressedReasons"]
            ),
            tracking_options=ses.CfnConfigurationSet.TrackingOptionsProperty(
                custom_redirect_domain="customRedirectDomain"
            ),
            vdm_options=ses.CfnConfigurationSet.VdmOptionsProperty(
                dashboard_options=ses.CfnConfigurationSet.DashboardOptionsProperty(
                    engagement_metrics="engagementMetrics"
                ),
                guardian_options=ses.CfnConfigurationSet.GuardianOptionsProperty(
                    optimized_shared_delivery="optimizedSharedDelivery"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.DeliveryOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.ReputationOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.SendingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        suppression_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.SuppressionOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.TrackingOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        vdm_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.VdmOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param delivery_options: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).
        :param name: The name of the configuration set. The name must meet the following requirements:. - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Contain 64 characters or fewer.
        :param reputation_options: An object that represents the reputation settings for the configuration set.
        :param sending_options: An object that defines whether or not Amazon SES can send email that you send using the configuration set.
        :param suppression_options: An object that contains information about the suppression list preferences for your account.
        :param tracking_options: The name of the custom open and click tracking domain associated with the configuration set.
        :param vdm_options: The Virtual Deliverability Manager (VDM) options that apply to the configuration set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ad84a733d05a7160c0517733c56c249f6a299231ebcf8e982ed1aeda9e9b3daf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetProps(
            delivery_options=delivery_options,
            name=name,
            reputation_options=reputation_options,
            sending_options=sending_options,
            suppression_options=suppression_options,
            tracking_options=tracking_options,
            vdm_options=vdm_options,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__703d8eb12ae21101f4f93e6ab7089d820f42a27a22e1028eee983deee4056343)
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
            type_hints = typing.get_type_hints(_typecheckingstub__3ec352b38e2d7189e23d09b362a1b86566764825e5e48e241ee1b2ef51c1b511)
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
    @jsii.member(jsii_name="deliveryOptions")
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DeliveryOptionsProperty"]]:
        '''Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DeliveryOptionsProperty"]], jsii.get(self, "deliveryOptions"))

    @delivery_options.setter
    def delivery_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DeliveryOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5255bb6021541c7e84379b09a4ffd806238f1ac83ad0e7000ea7e34028bc9a3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deliveryOptions", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration set.

        The name must meet the following requirements:.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "name"))

    @name.setter
    def name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9757b0b78870ccfafd1e870ca194f545ac0873693da40dc15e29ba8b5beb21b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="reputationOptions")
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.ReputationOptionsProperty"]]:
        '''An object that represents the reputation settings for the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.ReputationOptionsProperty"]], jsii.get(self, "reputationOptions"))

    @reputation_options.setter
    def reputation_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.ReputationOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dcb56d1f8e63eec7f19208aaf5c6887b110d769aa45bfe8a7329339a1cc321b6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "reputationOptions", value)

    @builtins.property
    @jsii.member(jsii_name="sendingOptions")
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SendingOptionsProperty"]]:
        '''An object that defines whether or not Amazon SES can send email that you send using the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SendingOptionsProperty"]], jsii.get(self, "sendingOptions"))

    @sending_options.setter
    def sending_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SendingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bfa327a56576655b9670d914964b52df069b29497d84b812a2f15586b1c5faa9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sendingOptions", value)

    @builtins.property
    @jsii.member(jsii_name="suppressionOptions")
    def suppression_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SuppressionOptionsProperty"]]:
        '''An object that contains information about the suppression list preferences for your account.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SuppressionOptionsProperty"]], jsii.get(self, "suppressionOptions"))

    @suppression_options.setter
    def suppression_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.SuppressionOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4d6e92203e0b0fb9ad18351409d2e930bd3b3881d922fcb2f2b38b337f5f4c55)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "suppressionOptions", value)

    @builtins.property
    @jsii.member(jsii_name="trackingOptions")
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.TrackingOptionsProperty"]]:
        '''The name of the custom open and click tracking domain associated with the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.TrackingOptionsProperty"]], jsii.get(self, "trackingOptions"))

    @tracking_options.setter
    def tracking_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.TrackingOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0e2738cc83fe741aa7d2c58d5db581a79f89d7427a9504ac697d8f7dd2004ea9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "trackingOptions", value)

    @builtins.property
    @jsii.member(jsii_name="vdmOptions")
    def vdm_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.VdmOptionsProperty"]]:
        '''The Virtual Deliverability Manager (VDM) options that apply to the configuration set.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.VdmOptionsProperty"]], jsii.get(self, "vdmOptions"))

    @vdm_options.setter
    def vdm_options(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.VdmOptionsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f115779032dd22d020f87b590d89ccdd0a4fc3f269b15bbecfde29ad92e4289)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "vdmOptions", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.DashboardOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"engagement_metrics": "engagementMetrics"},
    )
    class DashboardOptionsProperty:
        def __init__(self, *, engagement_metrics: builtins.str) -> None:
            '''Settings for your VDM configuration as applicable to the Dashboard.

            :param engagement_metrics: Specifies the status of your VDM engagement metrics collection. Can be one of the following:. - ``ENABLED`` – Amazon SES enables engagement metrics for the configuration set. - ``DISABLED`` – Amazon SES disables engagement metrics for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dashboard_options_property = ses.CfnConfigurationSet.DashboardOptionsProperty(
                    engagement_metrics="engagementMetrics"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e8d48d16888f580be3782790c85806d5e5ef5c592f9390a1048567593c281148)
                check_type(argname="argument engagement_metrics", value=engagement_metrics, expected_type=type_hints["engagement_metrics"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "engagement_metrics": engagement_metrics,
            }

        @builtins.property
        def engagement_metrics(self) -> builtins.str:
            '''Specifies the status of your VDM engagement metrics collection. Can be one of the following:.

            - ``ENABLED`` – Amazon SES enables engagement metrics for the configuration set.
            - ``DISABLED`` – Amazon SES disables engagement metrics for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-dashboardoptions.html#cfn-ses-configurationset-dashboardoptions-engagementmetrics
            '''
            result = self._values.get("engagement_metrics")
            assert result is not None, "Required property 'engagement_metrics' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.DeliveryOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "sending_pool_name": "sendingPoolName",
            "tls_policy": "tlsPolicy",
        },
    )
    class DeliveryOptionsProperty:
        def __init__(
            self,
            *,
            sending_pool_name: typing.Optional[builtins.str] = None,
            tls_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).

            :param sending_pool_name: The name of the dedicated IP pool to associate with the configuration set.
            :param tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is ``REQUIRE`` , messages are only delivered if a TLS connection can be established. If the value is ``OPTIONAL`` , messages can be delivered in plain text if a TLS connection can't be established. Valid Values: ``REQUIRE | OPTIONAL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                delivery_options_property = ses.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName",
                    tls_policy="tlsPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cad65d433b7328c2fe1d15052509478ad394628f7bbce8157ed352a3291b5d6f)
                check_type(argname="argument sending_pool_name", value=sending_pool_name, expected_type=type_hints["sending_pool_name"])
                check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_pool_name is not None:
                self._values["sending_pool_name"] = sending_pool_name
            if tls_policy is not None:
                self._values["tls_policy"] = tls_policy

        @builtins.property
        def sending_pool_name(self) -> typing.Optional[builtins.str]:
            '''The name of the dedicated IP pool to associate with the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-sendingpoolname
            '''
            result = self._values.get("sending_pool_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def tls_policy(self) -> typing.Optional[builtins.str]:
            '''Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).

            If the value is ``REQUIRE`` , messages are only delivered if a TLS connection can be established. If the value is ``OPTIONAL`` , messages can be delivered in plain text if a TLS connection can't be established.

            Valid Values: ``REQUIRE | OPTIONAL``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-deliveryoptions.html#cfn-ses-configurationset-deliveryoptions-tlspolicy
            '''
            result = self._values.get("tls_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DeliveryOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.GuardianOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"optimized_shared_delivery": "optimizedSharedDelivery"},
    )
    class GuardianOptionsProperty:
        def __init__(self, *, optimized_shared_delivery: builtins.str) -> None:
            '''Settings for your VDM configuration as applicable to the Guardian.

            :param optimized_shared_delivery: Specifies the status of your VDM optimized shared delivery. Can be one of the following:. - ``ENABLED`` – Amazon SES enables optimized shared delivery for the configuration set. - ``DISABLED`` – Amazon SES disables optimized shared delivery for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                guardian_options_property = ses.CfnConfigurationSet.GuardianOptionsProperty(
                    optimized_shared_delivery="optimizedSharedDelivery"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cabe5bd3bd3cb84baab32735da66eedb8e560e50da24718ab0d87b340502d858)
                check_type(argname="argument optimized_shared_delivery", value=optimized_shared_delivery, expected_type=type_hints["optimized_shared_delivery"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "optimized_shared_delivery": optimized_shared_delivery,
            }

        @builtins.property
        def optimized_shared_delivery(self) -> builtins.str:
            '''Specifies the status of your VDM optimized shared delivery. Can be one of the following:.

            - ``ENABLED`` – Amazon SES enables optimized shared delivery for the configuration set.
            - ``DISABLED`` – Amazon SES disables optimized shared delivery for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-guardianoptions.html#cfn-ses-configurationset-guardianoptions-optimizedshareddelivery
            '''
            result = self._values.get("optimized_shared_delivery")
            assert result is not None, "Required property 'optimized_shared_delivery' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardianOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.ReputationOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"reputation_metrics_enabled": "reputationMetricsEnabled"},
    )
    class ReputationOptionsProperty:
        def __init__(
            self,
            *,
            reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Contains information about the reputation settings for a configuration set.

            :param reputation_metrics_enabled: Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch. If the value is ``true`` , reputation metrics are published. If the value is ``false`` , reputation metrics are not published. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                reputation_options_property = ses.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__66f701bd9f49ad0c515c9634599b8e0616f4f3b15f2e4f6b9f906f2542e78676)
                check_type(argname="argument reputation_metrics_enabled", value=reputation_metrics_enabled, expected_type=type_hints["reputation_metrics_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if reputation_metrics_enabled is not None:
                self._values["reputation_metrics_enabled"] = reputation_metrics_enabled

        @builtins.property
        def reputation_metrics_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Describes whether or not Amazon SES publishes reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

            If the value is ``true`` , reputation metrics are published. If the value is ``false`` , reputation metrics are not published. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-reputationoptions.html#cfn-ses-configurationset-reputationoptions-reputationmetricsenabled
            '''
            result = self._values.get("reputation_metrics_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ReputationOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.SendingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"sending_enabled": "sendingEnabled"},
    )
    class SendingOptionsProperty:
        def __init__(
            self,
            *,
            sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Used to enable or disable email sending for messages that use this configuration set in the current AWS Region.

            :param sending_enabled: If ``true`` , email sending is enabled for the configuration set. If ``false`` , email sending is disabled for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                sending_options_property = ses.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a548843fec9d94e10684140077e38c05264eb17e9e2997b3e7a864cb183318b8)
                check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if sending_enabled is not None:
                self._values["sending_enabled"] = sending_enabled

        @builtins.property
        def sending_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , email sending is enabled for the configuration set.

            If ``false`` , email sending is disabled for the configuration set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-sendingoptions.html#cfn-ses-configurationset-sendingoptions-sendingenabled
            '''
            result = self._values.get("sending_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SendingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.SuppressionOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"suppressed_reasons": "suppressedReasons"},
    )
    class SuppressionOptionsProperty:
        def __init__(
            self,
            *,
            suppressed_reasons: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''An object that contains information about the suppression list preferences for your account.

            :param suppressed_reasons: A list that contains the reasons that email addresses are automatically added to the suppression list for your account. This list can contain any or all of the following: - ``COMPLAINT`` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint. - ``BOUNCE`` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                suppression_options_property = ses.CfnConfigurationSet.SuppressionOptionsProperty(
                    suppressed_reasons=["suppressedReasons"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8d9a9f4a0b048a750b42ffb05bbf2f29193ab82552fe268e651a27bc5bf661be)
                check_type(argname="argument suppressed_reasons", value=suppressed_reasons, expected_type=type_hints["suppressed_reasons"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if suppressed_reasons is not None:
                self._values["suppressed_reasons"] = suppressed_reasons

        @builtins.property
        def suppressed_reasons(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list that contains the reasons that email addresses are automatically added to the suppression list for your account.

            This list can contain any or all of the following:

            - ``COMPLAINT`` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.
            - ``BOUNCE`` – Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-suppressionoptions.html#cfn-ses-configurationset-suppressionoptions-suppressedreasons
            '''
            result = self._values.get("suppressed_reasons")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SuppressionOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.TrackingOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"custom_redirect_domain": "customRedirectDomain"},
    )
    class TrackingOptionsProperty:
        def __init__(
            self,
            *,
            custom_redirect_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A domain that is used to redirect email recipients to an Amazon SES-operated domain.

            This domain captures open and click events generated by Amazon SES emails.

            For more information, see `Configuring Custom Domains to Handle Open and Click Tracking <https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html>`_ in the *Amazon SES Developer Guide* .

            :param custom_redirect_domain: The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                tracking_options_property = ses.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__9cb3a7d8357d451a88f3bdd86fea15ef7d167ba61579a61a8e1fe9eb6bfa73f2)
                check_type(argname="argument custom_redirect_domain", value=custom_redirect_domain, expected_type=type_hints["custom_redirect_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if custom_redirect_domain is not None:
                self._values["custom_redirect_domain"] = custom_redirect_domain

        @builtins.property
        def custom_redirect_domain(self) -> typing.Optional[builtins.str]:
            '''The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-trackingoptions.html#cfn-ses-configurationset-trackingoptions-customredirectdomain
            '''
            result = self._values.get("custom_redirect_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TrackingOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSet.VdmOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "dashboard_options": "dashboardOptions",
            "guardian_options": "guardianOptions",
        },
    )
    class VdmOptionsProperty:
        def __init__(
            self,
            *,
            dashboard_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.DashboardOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            guardian_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSet.GuardianOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The Virtual Deliverability Manager (VDM) options that apply to a configuration set.

            :param dashboard_options: Settings for your VDM configuration as applicable to the Dashboard.
            :param guardian_options: Settings for your VDM configuration as applicable to the Guardian.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                vdm_options_property = ses.CfnConfigurationSet.VdmOptionsProperty(
                    dashboard_options=ses.CfnConfigurationSet.DashboardOptionsProperty(
                        engagement_metrics="engagementMetrics"
                    ),
                    guardian_options=ses.CfnConfigurationSet.GuardianOptionsProperty(
                        optimized_shared_delivery="optimizedSharedDelivery"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__94fcd9f4369b7da06731e9702fc08a13db56c4b817946b6fda1167dfc314ecd2)
                check_type(argname="argument dashboard_options", value=dashboard_options, expected_type=type_hints["dashboard_options"])
                check_type(argname="argument guardian_options", value=guardian_options, expected_type=type_hints["guardian_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dashboard_options is not None:
                self._values["dashboard_options"] = dashboard_options
            if guardian_options is not None:
                self._values["guardian_options"] = guardian_options

        @builtins.property
        def dashboard_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DashboardOptionsProperty"]]:
            '''Settings for your VDM configuration as applicable to the Dashboard.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-dashboardoptions
            '''
            result = self._values.get("dashboard_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.DashboardOptionsProperty"]], result)

        @builtins.property
        def guardian_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.GuardianOptionsProperty"]]:
            '''Settings for your VDM configuration as applicable to the Guardian.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationset-vdmoptions.html#cfn-ses-configurationset-vdmoptions-guardianoptions
            '''
            result = self._values.get("guardian_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSet.GuardianOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "VdmOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnConfigurationSetEventDestination(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination",
):
    '''Specifies a configuration set event destination.

    An event destination is an AWS service that Amazon SES publishes email sending events to. When you specify an event destination, you provide one, and only one, destination. You can send event data to Amazon CloudWatch, Amazon Kinesis Data Firehose, or Amazon Simple Notification Service (Amazon SNS).

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_configuration_set_event_destination = ses.CfnConfigurationSetEventDestination(self, "MyCfnConfigurationSetEventDestination",
            configuration_set_name="configurationSetName",
            event_destination=ses.CfnConfigurationSetEventDestination.EventDestinationProperty(
                matching_event_types=["matchingEventTypes"],
        
                # the properties below are optional
                cloud_watch_destination=ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                ),
                enabled=False,
                kinesis_firehose_destination=ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                ),
                name="name",
                sns_destination=ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_set_name: builtins.str,
        event_destination: typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.EventDestinationProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param configuration_set_name: The name of the configuration set that contains the event destination.
        :param event_destination: The event destination object.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e0376f935c1363b5c7cfddd668508c112d2a00f2637b1a84086b70c96af9e53c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnConfigurationSetEventDestinationProps(
            configuration_set_name=configuration_set_name,
            event_destination=event_destination,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d77d1e029fcf58a1f079cf11a321a2e3416ae4150d8df3576a09e3c62095ca35)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8650d4b56a0c900e4a255fe7bb98030ff250164d423e43ab113f0bcb3cad116e)
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
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

    @configuration_set_name.setter
    def configuration_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a9ebb672423cac8794fa77851a8fa78b27a8be4beabf8025723862ad9291d619)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetName", value)

    @builtins.property
    @jsii.member(jsii_name="eventDestination")
    def event_destination(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.EventDestinationProperty"]:
        '''The event destination object.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.EventDestinationProperty"], jsii.get(self, "eventDestination"))

    @event_destination.setter
    def event_destination(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.EventDestinationProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c5bde831b7591d8114916d0e9453c13daabe44cbe1f0da50b7cd72b598079dfa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "eventDestination", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"dimension_configurations": "dimensionConfigurations"},
    )
    class CloudWatchDestinationProperty:
        def __init__(
            self,
            *,
            dimension_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.DimensionConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Contains information associated with an Amazon CloudWatch event destination to which email sending events are published.

            Event destinations, such as Amazon CloudWatch, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param dimension_configurations: A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                cloud_watch_destination_property = ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                    dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                        default_dimension_value="defaultDimensionValue",
                        dimension_name="dimensionName",
                        dimension_value_source="dimensionValueSource"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e60b6436d0d38ae03fe0a4f110271b401e922dc980b2b61e9f401dd25eb1061c)
                check_type(argname="argument dimension_configurations", value=dimension_configurations, expected_type=type_hints["dimension_configurations"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if dimension_configurations is not None:
                self._values["dimension_configurations"] = dimension_configurations

        @builtins.property
        def dimension_configurations(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]]:
            '''A list of dimensions upon which to categorize your emails when you publish email sending events to Amazon CloudWatch.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-cloudwatchdestination.html#cfn-ses-configurationseteventdestination-cloudwatchdestination-dimensionconfigurations
            '''
            result = self._values.get("dimension_configurations")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.DimensionConfigurationProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CloudWatchDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_dimension_value": "defaultDimensionValue",
            "dimension_name": "dimensionName",
            "dimension_value_source": "dimensionValueSource",
        },
    )
    class DimensionConfigurationProperty:
        def __init__(
            self,
            *,
            default_dimension_value: builtins.str,
            dimension_name: builtins.str,
            dimension_value_source: builtins.str,
        ) -> None:
            '''Contains the dimension configuration to use when you publish email sending events to Amazon CloudWatch.

            For information about publishing email sending events to Amazon CloudWatch, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param default_dimension_value: The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email. The default value must meet the following requirements: - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), at signs (@), or periods (.). - Contain 256 characters or fewer.
            :param dimension_name: The name of an Amazon CloudWatch dimension associated with an email sending metric. The name must meet the following requirements: - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or colons (:). - Contain 256 characters or fewer.
            :param dimension_value_source: The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch. To use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` / ``SendRawEmail`` API, specify ``messageTag`` . To use your own email headers, specify ``emailHeader`` . To put a custom tag on any link included in your email, specify ``linkTag`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dimension_configuration_property = ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                    default_dimension_value="defaultDimensionValue",
                    dimension_name="dimensionName",
                    dimension_value_source="dimensionValueSource"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__cf76f41f2226fa19acdad1732c136b3ee21554d7f8458ed43f731c0fee88cbcc)
                check_type(argname="argument default_dimension_value", value=default_dimension_value, expected_type=type_hints["default_dimension_value"])
                check_type(argname="argument dimension_name", value=dimension_name, expected_type=type_hints["dimension_name"])
                check_type(argname="argument dimension_value_source", value=dimension_value_source, expected_type=type_hints["dimension_value_source"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_dimension_value": default_dimension_value,
                "dimension_name": dimension_name,
                "dimension_value_source": dimension_value_source,
            }

        @builtins.property
        def default_dimension_value(self) -> builtins.str:
            '''The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email.

            The default value must meet the following requirements:

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), at signs (@), or periods (.).
            - Contain 256 characters or fewer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-defaultdimensionvalue
            '''
            result = self._values.get("default_dimension_value")
            assert result is not None, "Required property 'default_dimension_value' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_name(self) -> builtins.str:
            '''The name of an Amazon CloudWatch dimension associated with an email sending metric.

            The name must meet the following requirements:

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or colons (:).
            - Contain 256 characters or fewer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionname
            '''
            result = self._values.get("dimension_name")
            assert result is not None, "Required property 'dimension_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def dimension_value_source(self) -> builtins.str:
            '''The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch.

            To use the message tags that you specify using an ``X-SES-MESSAGE-TAGS`` header or a parameter to the ``SendEmail`` / ``SendRawEmail`` API, specify ``messageTag`` . To use your own email headers, specify ``emailHeader`` . To put a custom tag on any link included in your email, specify ``linkTag`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-dimensionconfiguration.html#cfn-ses-configurationseteventdestination-dimensionconfiguration-dimensionvaluesource
            '''
            result = self._values.get("dimension_value_source")
            assert result is not None, "Required property 'dimension_value_source' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DimensionConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.EventDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "matching_event_types": "matchingEventTypes",
            "cloud_watch_destination": "cloudWatchDestination",
            "enabled": "enabled",
            "kinesis_firehose_destination": "kinesisFirehoseDestination",
            "name": "name",
            "sns_destination": "snsDestination",
        },
    )
    class EventDestinationProperty:
        def __init__(
            self,
            *,
            matching_event_types: typing.Sequence[builtins.str],
            cloud_watch_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.CloudWatchDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            kinesis_firehose_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[builtins.str] = None,
            sns_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnConfigurationSetEventDestination.SnsDestinationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information about an event destination.

            .. epigraph::

               When you create or update an event destination, you must provide one, and only one, destination. The destination can be Amazon CloudWatch, Amazon Kinesis Firehose or Amazon Simple Notification Service (Amazon SNS).

            Event destinations are associated with configuration sets, which enable you to publish email sending events to Amazon CloudWatch, Amazon Kinesis Firehose, or Amazon Simple Notification Service (Amazon SNS). For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param matching_event_types: The type of email sending events to publish to the event destination. - ``send`` - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.) - ``reject`` - SES accepted the email, but determined that it contained a virus and didn’t attempt to deliver it to the recipient’s mail server. - ``bounce`` - ( *Hard bounce* ) The recipient's mail server permanently rejected the email. ( *Soft bounces* are only included when SES fails to deliver the email after retrying for a period of time.) - ``complaint`` - The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam. - ``delivery`` - SES successfully delivered the email to the recipient's mail server. - ``open`` - The recipient received the message and opened it in their email client. - ``click`` - The recipient clicked one or more links in the email. - ``renderingFailure`` - The email wasn't sent because of a template rendering issue. This event type can occur when template data is missing, or when there is a mismatch between template parameters and data. (This event type only occurs when you send email using the ```SendTemplatedEmail`` <https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html>`_ or ```SendBulkTemplatedEmail`` <https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBulkTemplatedEmail.html>`_ API operations.) - ``deliveryDelay`` - The email couldn't be delivered to the recipient’s mail server because a temporary issue occurred. Delivery delays can occur, for example, when the recipient's inbox is full, or when the receiving email server experiences a transient issue. - ``subscription`` - The email was successfully delivered, but the recipient updated their subscription preferences by clicking on an *unsubscribe* link as part of your `subscription management <https://docs.aws.amazon.com/ses/latest/dg/sending-email-subscription-management.html>`_ .
            :param cloud_watch_destination: An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.
            :param enabled: Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set. Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .
            :param kinesis_firehose_destination: An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.
            :param name: The name of the event destination. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Contain 64 characters or fewer.
            :param sns_destination: An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                event_destination_property = ses.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
                
                    # the properties below are optional
                    cloud_watch_destination=ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    name="name",
                    sns_destination=ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b77a9a6a44a2946da816730acf4f2c79407a57e401fb25707130b8e68609c0b9)
                check_type(argname="argument matching_event_types", value=matching_event_types, expected_type=type_hints["matching_event_types"])
                check_type(argname="argument cloud_watch_destination", value=cloud_watch_destination, expected_type=type_hints["cloud_watch_destination"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument kinesis_firehose_destination", value=kinesis_firehose_destination, expected_type=type_hints["kinesis_firehose_destination"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument sns_destination", value=sns_destination, expected_type=type_hints["sns_destination"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "matching_event_types": matching_event_types,
            }
            if cloud_watch_destination is not None:
                self._values["cloud_watch_destination"] = cloud_watch_destination
            if enabled is not None:
                self._values["enabled"] = enabled
            if kinesis_firehose_destination is not None:
                self._values["kinesis_firehose_destination"] = kinesis_firehose_destination
            if name is not None:
                self._values["name"] = name
            if sns_destination is not None:
                self._values["sns_destination"] = sns_destination

        @builtins.property
        def matching_event_types(self) -> typing.List[builtins.str]:
            '''The type of email sending events to publish to the event destination.

            - ``send`` - The send request was successful and SES will attempt to deliver the message to the recipient’s mail server. (If account-level or global suppression is being used, SES will still count it as a send, but delivery is suppressed.)
            - ``reject`` - SES accepted the email, but determined that it contained a virus and didn’t attempt to deliver it to the recipient’s mail server.
            - ``bounce`` - ( *Hard bounce* ) The recipient's mail server permanently rejected the email. ( *Soft bounces* are only included when SES fails to deliver the email after retrying for a period of time.)
            - ``complaint`` - The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam.
            - ``delivery`` - SES successfully delivered the email to the recipient's mail server.
            - ``open`` - The recipient received the message and opened it in their email client.
            - ``click`` - The recipient clicked one or more links in the email.
            - ``renderingFailure`` - The email wasn't sent because of a template rendering issue. This event type can occur when template data is missing, or when there is a mismatch between template parameters and data. (This event type only occurs when you send email using the ```SendTemplatedEmail`` <https://docs.aws.amazon.com/ses/latest/APIReference/API_SendTemplatedEmail.html>`_ or ```SendBulkTemplatedEmail`` <https://docs.aws.amazon.com/ses/latest/APIReference/API_SendBulkTemplatedEmail.html>`_ API operations.)
            - ``deliveryDelay`` - The email couldn't be delivered to the recipient’s mail server because a temporary issue occurred. Delivery delays can occur, for example, when the recipient's inbox is full, or when the receiving email server experiences a transient issue.
            - ``subscription`` - The email was successfully delivered, but the recipient updated their subscription preferences by clicking on an *unsubscribe* link as part of your `subscription management <https://docs.aws.amazon.com/ses/latest/dg/sending-email-subscription-management.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-matchingeventtypes
            '''
            result = self._values.get("matching_event_types")
            assert result is not None, "Required property 'matching_event_types' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def cloud_watch_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]]:
            '''An object that contains the names, default values, and sources of the dimensions associated with an Amazon CloudWatch event destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-cloudwatchdestination
            '''
            result = self._values.get("cloud_watch_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.CloudWatchDestinationProperty"]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Sets whether Amazon SES publishes events to this destination when you send an email with the associated configuration set.

            Set to ``true`` to enable publishing to this destination; set to ``false`` to prevent publishing to this destination. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def kinesis_firehose_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]]:
            '''An object that contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-kinesisfirehosedestination
            '''
            result = self._values.get("kinesis_firehose_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty"]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the event destination. The name must meet the following requirements:.

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            - Contain 64 characters or fewer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def sns_destination(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]]:
            '''An object that contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-eventdestination.html#cfn-ses-configurationseteventdestination-eventdestination-snsdestination
            '''
            result = self._values.get("sns_destination")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnConfigurationSetEventDestination.SnsDestinationProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EventDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "delivery_stream_arn": "deliveryStreamArn",
            "iam_role_arn": "iamRoleArn",
        },
    )
    class KinesisFirehoseDestinationProperty:
        def __init__(
            self,
            *,
            delivery_stream_arn: builtins.str,
            iam_role_arn: builtins.str,
        ) -> None:
            '''Contains the delivery stream ARN and the IAM role ARN associated with an Amazon Kinesis Firehose event destination.

            Event destinations, such as Amazon Kinesis Firehose, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param delivery_stream_arn: The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.
            :param iam_role_arn: The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                kinesis_firehose_destination_property = ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                    delivery_stream_arn="deliveryStreamArn",
                    iam_role_arn="iamRoleArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ee1cd798be61243093d3e6c4cfddb9f06458011ead23160593d456863d3d8916)
                check_type(argname="argument delivery_stream_arn", value=delivery_stream_arn, expected_type=type_hints["delivery_stream_arn"])
                check_type(argname="argument iam_role_arn", value=iam_role_arn, expected_type=type_hints["iam_role_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "delivery_stream_arn": delivery_stream_arn,
                "iam_role_arn": iam_role_arn,
            }

        @builtins.property
        def delivery_stream_arn(self) -> builtins.str:
            '''The ARN of the Amazon Kinesis Firehose stream that email sending events should be published to.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-deliverystreamarn
            '''
            result = self._values.get("delivery_stream_arn")
            assert result is not None, "Required property 'delivery_stream_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def iam_role_arn(self) -> builtins.str:
            '''The ARN of the IAM role under which Amazon SES publishes email sending events to the Amazon Kinesis Firehose stream.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-kinesisfirehosedestination.html#cfn-ses-configurationseteventdestination-kinesisfirehosedestination-iamrolearn
            '''
            result = self._values.get("iam_role_arn")
            assert result is not None, "Required property 'iam_role_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "KinesisFirehoseDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestination.SnsDestinationProperty",
        jsii_struct_bases=[],
        name_mapping={"topic_arn": "topicArn"},
    )
    class SnsDestinationProperty:
        def __init__(self, *, topic_arn: builtins.str) -> None:
            '''Contains the topic ARN associated with an Amazon Simple Notification Service (Amazon SNS) event destination.

            Event destinations, such as Amazon SNS, are associated with configuration sets, which enable you to publish email sending events. For information about using configuration sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html>`_ .

            :param topic_arn: The ARN of the Amazon SNS topic for email sending events. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ Amazon SNS operation. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                sns_destination_property = ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__088fd890007dccc782783b2f90e64f8c72607c080bdc0d3a15c7d13f1adbcf2b)
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "topic_arn": topic_arn,
            }

        @builtins.property
        def topic_arn(self) -> builtins.str:
            '''The ARN of the Amazon SNS topic for email sending events.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ Amazon SNS operation.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-configurationseteventdestination-snsdestination.html#cfn-ses-configurationseteventdestination-snsdestination-topicarn
            '''
            result = self._values.get("topic_arn")
            assert result is not None, "Required property 'topic_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SnsDestinationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetEventDestinationProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "event_destination": "eventDestination",
    },
)
class CfnConfigurationSetEventDestinationProps:
    def __init__(
        self,
        *,
        configuration_set_name: builtins.str,
        event_destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSetEventDestination``.

        :param configuration_set_name: The name of the configuration set that contains the event destination.
        :param event_destination: The event destination object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_configuration_set_event_destination_props = ses.CfnConfigurationSetEventDestinationProps(
                configuration_set_name="configurationSetName",
                event_destination=ses.CfnConfigurationSetEventDestination.EventDestinationProperty(
                    matching_event_types=["matchingEventTypes"],
            
                    # the properties below are optional
                    cloud_watch_destination=ses.CfnConfigurationSetEventDestination.CloudWatchDestinationProperty(
                        dimension_configurations=[ses.CfnConfigurationSetEventDestination.DimensionConfigurationProperty(
                            default_dimension_value="defaultDimensionValue",
                            dimension_name="dimensionName",
                            dimension_value_source="dimensionValueSource"
                        )]
                    ),
                    enabled=False,
                    kinesis_firehose_destination=ses.CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty(
                        delivery_stream_arn="deliveryStreamArn",
                        iam_role_arn="iamRoleArn"
                    ),
                    name="name",
                    sns_destination=ses.CfnConfigurationSetEventDestination.SnsDestinationProperty(
                        topic_arn="topicArn"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5bf6472e974193204bd884002deb0a2d69e96cef811e1a0aa08aafb3997a9ca2)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument event_destination", value=event_destination, expected_type=type_hints["event_destination"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "configuration_set_name": configuration_set_name,
            "event_destination": event_destination,
        }

    @builtins.property
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set that contains the event destination.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-configurationsetname
        '''
        result = self._values.get("configuration_set_name")
        assert result is not None, "Required property 'configuration_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def event_destination(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnConfigurationSetEventDestination.EventDestinationProperty]:
        '''The event destination object.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationseteventdestination.html#cfn-ses-configurationseteventdestination-eventdestination
        '''
        result = self._values.get("event_destination")
        assert result is not None, "Required property 'event_destination' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnConfigurationSetEventDestination.EventDestinationProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "delivery_options": "deliveryOptions",
        "name": "name",
        "reputation_options": "reputationOptions",
        "sending_options": "sendingOptions",
        "suppression_options": "suppressionOptions",
        "tracking_options": "trackingOptions",
        "vdm_options": "vdmOptions",
    },
)
class CfnConfigurationSetProps:
    def __init__(
        self,
        *,
        delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        name: typing.Optional[builtins.str] = None,
        reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        suppression_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SuppressionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        vdm_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.VdmOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnConfigurationSet``.

        :param delivery_options: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).
        :param name: The name of the configuration set. The name must meet the following requirements:. - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Contain 64 characters or fewer.
        :param reputation_options: An object that represents the reputation settings for the configuration set.
        :param sending_options: An object that defines whether or not Amazon SES can send email that you send using the configuration set.
        :param suppression_options: An object that contains information about the suppression list preferences for your account.
        :param tracking_options: The name of the custom open and click tracking domain associated with the configuration set.
        :param vdm_options: The Virtual Deliverability Manager (VDM) options that apply to the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_configuration_set_props = ses.CfnConfigurationSetProps(
                delivery_options=ses.CfnConfigurationSet.DeliveryOptionsProperty(
                    sending_pool_name="sendingPoolName",
                    tls_policy="tlsPolicy"
                ),
                name="name",
                reputation_options=ses.CfnConfigurationSet.ReputationOptionsProperty(
                    reputation_metrics_enabled=False
                ),
                sending_options=ses.CfnConfigurationSet.SendingOptionsProperty(
                    sending_enabled=False
                ),
                suppression_options=ses.CfnConfigurationSet.SuppressionOptionsProperty(
                    suppressed_reasons=["suppressedReasons"]
                ),
                tracking_options=ses.CfnConfigurationSet.TrackingOptionsProperty(
                    custom_redirect_domain="customRedirectDomain"
                ),
                vdm_options=ses.CfnConfigurationSet.VdmOptionsProperty(
                    dashboard_options=ses.CfnConfigurationSet.DashboardOptionsProperty(
                        engagement_metrics="engagementMetrics"
                    ),
                    guardian_options=ses.CfnConfigurationSet.GuardianOptionsProperty(
                        optimized_shared_delivery="optimizedSharedDelivery"
                    )
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e27ed179dbf809eedecaf57207416cd1680782d0d3ab4c539486ad7038b09efa)
            check_type(argname="argument delivery_options", value=delivery_options, expected_type=type_hints["delivery_options"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument reputation_options", value=reputation_options, expected_type=type_hints["reputation_options"])
            check_type(argname="argument sending_options", value=sending_options, expected_type=type_hints["sending_options"])
            check_type(argname="argument suppression_options", value=suppression_options, expected_type=type_hints["suppression_options"])
            check_type(argname="argument tracking_options", value=tracking_options, expected_type=type_hints["tracking_options"])
            check_type(argname="argument vdm_options", value=vdm_options, expected_type=type_hints["vdm_options"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if delivery_options is not None:
            self._values["delivery_options"] = delivery_options
        if name is not None:
            self._values["name"] = name
        if reputation_options is not None:
            self._values["reputation_options"] = reputation_options
        if sending_options is not None:
            self._values["sending_options"] = sending_options
        if suppression_options is not None:
            self._values["suppression_options"] = suppression_options
        if tracking_options is not None:
            self._values["tracking_options"] = tracking_options
        if vdm_options is not None:
            self._values["vdm_options"] = vdm_options

    @builtins.property
    def delivery_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.DeliveryOptionsProperty]]:
        '''Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-deliveryoptions
        '''
        result = self._values.get("delivery_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.DeliveryOptionsProperty]], result)

    @builtins.property
    def name(self) -> typing.Optional[builtins.str]:
        '''The name of the configuration set. The name must meet the following requirements:.

        - Contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
        - Contain 64 characters or fewer.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-name
        '''
        result = self._values.get("name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def reputation_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.ReputationOptionsProperty]]:
        '''An object that represents the reputation settings for the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-reputationoptions
        '''
        result = self._values.get("reputation_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.ReputationOptionsProperty]], result)

    @builtins.property
    def sending_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SendingOptionsProperty]]:
        '''An object that defines whether or not Amazon SES can send email that you send using the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-sendingoptions
        '''
        result = self._values.get("sending_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SendingOptionsProperty]], result)

    @builtins.property
    def suppression_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SuppressionOptionsProperty]]:
        '''An object that contains information about the suppression list preferences for your account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-suppressionoptions
        '''
        result = self._values.get("suppression_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SuppressionOptionsProperty]], result)

    @builtins.property
    def tracking_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.TrackingOptionsProperty]]:
        '''The name of the custom open and click tracking domain associated with the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-trackingoptions
        '''
        result = self._values.get("tracking_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.TrackingOptionsProperty]], result)

    @builtins.property
    def vdm_options(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.VdmOptionsProperty]]:
        '''The Virtual Deliverability Manager (VDM) options that apply to the configuration set.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-configurationset.html#cfn-ses-configurationset-vdmoptions
        '''
        result = self._values.get("vdm_options")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.VdmOptionsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnContactList(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnContactList",
):
    '''A list that contains contacts that have subscribed to a particular topic or topics.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_contact_list = ses.CfnContactList(self, "MyCfnContactList",
            contact_list_name="contactListName",
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            topics=[ses.CfnContactList.TopicProperty(
                default_subscription_status="defaultSubscriptionStatus",
                display_name="displayName",
                topic_name="topicName",
        
                # the properties below are optional
                description="description"
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        contact_list_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        topics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnContactList.TopicProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param contact_list_name: The name of the contact list.
        :param description: A description of what the contact list is about.
        :param tags: The tags associated with a contact list.
        :param topics: An interest group, theme, or label within a list. A contact list can have multiple topics.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4f5901f6c4687a5069b93788dd46825d3f820617b06ab7617c713daa19e6b0a1)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnContactListProps(
            contact_list_name=contact_list_name,
            description=description,
            tags=tags,
            topics=topics,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__04e7980d7184167e42f7e01ae8cec876d43f150d71c7057fca33fc0a3e2d3e6b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__af7d95554a83c0f0d545d0786c20201ae723b64226988c31c92f93e116a98429)
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
    @jsii.member(jsii_name="tags")
    def tags(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "tags"))

    @builtins.property
    @jsii.member(jsii_name="contactListName")
    def contact_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the contact list.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "contactListName"))

    @contact_list_name.setter
    def contact_list_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fe87ab99d02860b4269adb497c2b85c5627baa1480977081d5983090e8f106cf)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "contactListName", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of what the contact list is about.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b772e4221fab9fd85e09441b0917a7c5c4c012cb7676e6a6ea38ce5c619a4431)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with a contact list.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f3ca0b0993b5ed610f353a70ff69c08d5866611a4967d6f45f069e82edf1d5a8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="topics")
    def topics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContactList.TopicProperty"]]]]:
        '''An interest group, theme, or label within a list.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContactList.TopicProperty"]]]], jsii.get(self, "topics"))

    @topics.setter
    def topics(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnContactList.TopicProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a1a4f7da14b40f7178c1c0c458459ea9ecbdb3914bfe6c065e5ff051b6bd8728)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "topics", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnContactList.TopicProperty",
        jsii_struct_bases=[],
        name_mapping={
            "default_subscription_status": "defaultSubscriptionStatus",
            "display_name": "displayName",
            "topic_name": "topicName",
            "description": "description",
        },
    )
    class TopicProperty:
        def __init__(
            self,
            *,
            default_subscription_status: builtins.str,
            display_name: builtins.str,
            topic_name: builtins.str,
            description: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An interest group, theme, or label within a list.

            Lists can have multiple topics.

            :param default_subscription_status: The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.
            :param display_name: The name of the topic the contact will see.
            :param topic_name: The name of the topic.
            :param description: A description of what the topic is about, which the contact will see.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                topic_property = ses.CfnContactList.TopicProperty(
                    default_subscription_status="defaultSubscriptionStatus",
                    display_name="displayName",
                    topic_name="topicName",
                
                    # the properties below are optional
                    description="description"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__51caf9f57b613a46837ae653fc48f880d6c601b01293293e456968c3aa00c3c7)
                check_type(argname="argument default_subscription_status", value=default_subscription_status, expected_type=type_hints["default_subscription_status"])
                check_type(argname="argument display_name", value=display_name, expected_type=type_hints["display_name"])
                check_type(argname="argument topic_name", value=topic_name, expected_type=type_hints["topic_name"])
                check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "default_subscription_status": default_subscription_status,
                "display_name": display_name,
                "topic_name": topic_name,
            }
            if description is not None:
                self._values["description"] = description

        @builtins.property
        def default_subscription_status(self) -> builtins.str:
            '''The default subscription status to be applied to a contact if the contact has not noted their preference for subscribing to a topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-defaultsubscriptionstatus
            '''
            result = self._values.get("default_subscription_status")
            assert result is not None, "Required property 'default_subscription_status' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def display_name(self) -> builtins.str:
            '''The name of the topic the contact will see.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-displayname
            '''
            result = self._values.get("display_name")
            assert result is not None, "Required property 'display_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_name(self) -> builtins.str:
            '''The name of the topic.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-topicname
            '''
            result = self._values.get("topic_name")
            assert result is not None, "Required property 'topic_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def description(self) -> typing.Optional[builtins.str]:
            '''A description of what the topic is about, which the contact will see.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-contactlist-topic.html#cfn-ses-contactlist-topic-description
            '''
            result = self._values.get("description")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TopicProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnContactListProps",
    jsii_struct_bases=[],
    name_mapping={
        "contact_list_name": "contactListName",
        "description": "description",
        "tags": "tags",
        "topics": "topics",
    },
)
class CfnContactListProps:
    def __init__(
        self,
        *,
        contact_list_name: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        topics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContactList.TopicProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnContactList``.

        :param contact_list_name: The name of the contact list.
        :param description: A description of what the contact list is about.
        :param tags: The tags associated with a contact list.
        :param topics: An interest group, theme, or label within a list. A contact list can have multiple topics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_contact_list_props = ses.CfnContactListProps(
                contact_list_name="contactListName",
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                topics=[ses.CfnContactList.TopicProperty(
                    default_subscription_status="defaultSubscriptionStatus",
                    display_name="displayName",
                    topic_name="topicName",
            
                    # the properties below are optional
                    description="description"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__072b7df8dc691d1a1cd6c9336ecf7d05df6b5b238b2a11c273d9ae0aaf2782c0)
            check_type(argname="argument contact_list_name", value=contact_list_name, expected_type=type_hints["contact_list_name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument topics", value=topics, expected_type=type_hints["topics"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if contact_list_name is not None:
            self._values["contact_list_name"] = contact_list_name
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if topics is not None:
            self._values["topics"] = topics

    @builtins.property
    def contact_list_name(self) -> typing.Optional[builtins.str]:
        '''The name of the contact list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-contactlistname
        '''
        result = self._values.get("contact_list_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of what the contact list is about.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''The tags associated with a contact list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def topics(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContactList.TopicProperty]]]]:
        '''An interest group, theme, or label within a list.

        A contact list can have multiple topics.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-contactlist.html#cfn-ses-contactlist-topics
        '''
        result = self._values.get("topics")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContactList.TopicProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnContactListProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnDedicatedIpPool(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnDedicatedIpPool",
):
    '''Create a new pool of dedicated IP addresses.

    A pool can include one or more dedicated IP addresses that are associated with your AWS account . You can associate a pool with a configuration set. When you send an email that uses that configuration set, the message is sent from one of the addresses in the associated pool.
    .. epigraph::

       You can't delete dedicated IP pools that have a ``STANDARD`` scaling mode with one or more dedicated IP addresses. This constraint doesn't apply to dedicated IP pools that have a ``MANAGED`` scaling mode.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_dedicated_ip_pool = ses.CfnDedicatedIpPool(self, "MyCfnDedicatedIpPool",
            pool_name="poolName",
            scaling_mode="scalingMode"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        pool_name: typing.Optional[builtins.str] = None,
        scaling_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param pool_name: The name of the dedicated IP pool that the IP address is associated with.
        :param scaling_mode: The type of scaling mode. The following options are available: - ``STANDARD`` - The customer controls which IPs are part of the dedicated IP pool. - ``MANAGED`` - The reputation and number of IPs are automatically managed by Amazon SES . The ``STANDARD`` option is selected by default if no value is specified. .. epigraph:: Updating *ScalingMode* doesn't require a replacement if you're updating its value from ``STANDARD`` to ``MANAGED`` . However, updating *ScalingMode* from ``MANAGED`` to ``STANDARD`` is not supported.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__86a024e58c5549e30a3beca5bb152d09219a0cb42e6e02b0e95395595c9930e2)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDedicatedIpPoolProps(pool_name=pool_name, scaling_mode=scaling_mode)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8104b1859d7ffadca75f36effd5e88f40353e147cbb9ff43a0adf3b020c8e7d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__d431f4fa3e72589a6c2f0607a33d0c813f15e49f2c036738c5ec863ee07438cc)
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
    @jsii.member(jsii_name="poolName")
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dedicated IP pool that the IP address is associated with.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "poolName"))

    @pool_name.setter
    def pool_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4397d06edc01bb178665cd7af2c334613e4b051f65bf7fc9a1638ae1775ed9cb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "poolName", value)

    @builtins.property
    @jsii.member(jsii_name="scalingMode")
    def scaling_mode(self) -> typing.Optional[builtins.str]:
        '''The type of scaling mode.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scalingMode"))

    @scaling_mode.setter
    def scaling_mode(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfe768b550097b0e81974377ae65fba6791743f6787f72492af555cd19e3685a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scalingMode", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnDedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"pool_name": "poolName", "scaling_mode": "scalingMode"},
)
class CfnDedicatedIpPoolProps:
    def __init__(
        self,
        *,
        pool_name: typing.Optional[builtins.str] = None,
        scaling_mode: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnDedicatedIpPool``.

        :param pool_name: The name of the dedicated IP pool that the IP address is associated with.
        :param scaling_mode: The type of scaling mode. The following options are available: - ``STANDARD`` - The customer controls which IPs are part of the dedicated IP pool. - ``MANAGED`` - The reputation and number of IPs are automatically managed by Amazon SES . The ``STANDARD`` option is selected by default if no value is specified. .. epigraph:: Updating *ScalingMode* doesn't require a replacement if you're updating its value from ``STANDARD`` to ``MANAGED`` . However, updating *ScalingMode* from ``MANAGED`` to ``STANDARD`` is not supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_dedicated_ip_pool_props = ses.CfnDedicatedIpPoolProps(
                pool_name="poolName",
                scaling_mode="scalingMode"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea1a308c0c75c9aabf33c8c8b6378da7534f946eff787acdd2dc100f0b482f56)
            check_type(argname="argument pool_name", value=pool_name, expected_type=type_hints["pool_name"])
            check_type(argname="argument scaling_mode", value=scaling_mode, expected_type=type_hints["scaling_mode"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if pool_name is not None:
            self._values["pool_name"] = pool_name
        if scaling_mode is not None:
            self._values["scaling_mode"] = scaling_mode

    @builtins.property
    def pool_name(self) -> typing.Optional[builtins.str]:
        '''The name of the dedicated IP pool that the IP address is associated with.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-poolname
        '''
        result = self._values.get("pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scaling_mode(self) -> typing.Optional[builtins.str]:
        '''The type of scaling mode.

        The following options are available:

        - ``STANDARD`` - The customer controls which IPs are part of the dedicated IP pool.
        - ``MANAGED`` - The reputation and number of IPs are automatically managed by Amazon SES .

        The ``STANDARD`` option is selected by default if no value is specified.
        .. epigraph::

           Updating *ScalingMode* doesn't require a replacement if you're updating its value from ``STANDARD`` to ``MANAGED`` . However, updating *ScalingMode* from ``MANAGED`` to ``STANDARD`` is not supported.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-dedicatedippool.html#cfn-ses-dedicatedippool-scalingmode
        '''
        result = self._values.get("scaling_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnEmailIdentity(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity",
):
    '''Specifies an identity for using within SES.

    An identity is an email address or domain that you use when you send email. Before you can use an identity to send email, you first have to verify it. By verifying an identity, you demonstrate that you're the owner of the identity, and that you've given Amazon SES API v2 permission to send email from the identity.

    When you verify an email address, SES sends an email to the address. Your email address is verified as soon as you follow the link in the verification email. When you verify a domain without specifying the DkimSigningAttributes properties, OR only the NextSigningKeyLength property of DkimSigningAttributes, this resource provides a set of CNAME token names and values (DkimDNSTokenName1, DkimDNSTokenValue1, DkimDNSTokenName2, DkimDNSTokenValue2, DkimDNSTokenName3, DkimDNSTokenValue3) as outputs. You can then add these to the DNS configuration for your domain. Your domain is verified when Amazon SES detects these records in the DNS configuration for your domain. This verification method is known as Easy DKIM.

    Alternatively, you can perform the verification process by providing your own public-private key pair. This verification method is known as Bring Your Own DKIM (BYODKIM). To use BYODKIM, your resource must include DkimSigningAttributes properties DomainSigningSelector and DomainSigningPrivateKey. When you specify this object, you provide a selector (DomainSigningSelector) (a component of the DNS record name that identifies the public key to use for DKIM authentication) and a private key (DomainSigningPrivateKey).

    Additionally, you can associate an existing configuration set with the email identity that you're verifying.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_email_identity = ses.CfnEmailIdentity(self, "MyCfnEmailIdentity",
            email_identity="emailIdentity",
        
            # the properties below are optional
            configuration_set_attributes=ses.CfnEmailIdentity.ConfigurationSetAttributesProperty(
                configuration_set_name="configurationSetName"
            ),
            dkim_attributes=ses.CfnEmailIdentity.DkimAttributesProperty(
                signing_enabled=False
            ),
            dkim_signing_attributes=ses.CfnEmailIdentity.DkimSigningAttributesProperty(
                domain_signing_private_key="domainSigningPrivateKey",
                domain_signing_selector="domainSigningSelector",
                next_signing_key_length="nextSigningKeyLength"
            ),
            feedback_attributes=ses.CfnEmailIdentity.FeedbackAttributesProperty(
                email_forwarding_enabled=False
            ),
            mail_from_attributes=ses.CfnEmailIdentity.MailFromAttributesProperty(
                behavior_on_mx_failure="behaviorOnMxFailure",
                mail_from_domain="mailFromDomain"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        email_identity: builtins.str,
        configuration_set_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEmailIdentity.ConfigurationSetAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dkim_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEmailIdentity.DkimAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        dkim_signing_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEmailIdentity.DkimSigningAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        feedback_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEmailIdentity.FeedbackAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnEmailIdentity.MailFromAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param email_identity: The email address or domain to verify.
        :param configuration_set_attributes: Used to associate a configuration set with an email identity.
        :param dkim_attributes: An object that contains information about the DKIM attributes for the identity.
        :param dkim_signing_attributes: If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for `Easy DKIM <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html>`_ .
        :param feedback_attributes: Used to enable or disable feedback forwarding for an identity.
        :param mail_from_attributes: Used to enable or disable the custom Mail-From domain configuration for an email identity.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6dd153888b73988faf47365b573ef9e102d03faf2ff7fc2112c9b85962c0cc81)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnEmailIdentityProps(
            email_identity=email_identity,
            configuration_set_attributes=configuration_set_attributes,
            dkim_attributes=dkim_attributes,
            dkim_signing_attributes=dkim_signing_attributes,
            feedback_attributes=feedback_attributes,
            mail_from_attributes=mail_from_attributes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2e59b4607b3737bad6d0d3dceb2602acfb4a055cf1db675a6a32c09ab24c984)
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
            type_hints = typing.get_type_hints(_typecheckingstub__89ed6968b3a6bd596dccac5a2250a9eaee13899cac4ddf323c6e8c46dae44315)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrDkimDnsTokenName1")
    def attr_dkim_dns_token_name1(self) -> builtins.str:
        '''The host name for the first token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: DkimDNSTokenName1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenName1"))

    @builtins.property
    @jsii.member(jsii_name="attrDkimDnsTokenName2")
    def attr_dkim_dns_token_name2(self) -> builtins.str:
        '''The host name for the second token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: DkimDNSTokenName2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenName2"))

    @builtins.property
    @jsii.member(jsii_name="attrDkimDnsTokenName3")
    def attr_dkim_dns_token_name3(self) -> builtins.str:
        '''The host name for the third token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: DkimDNSTokenName3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenName3"))

    @builtins.property
    @jsii.member(jsii_name="attrDkimDnsTokenValue1")
    def attr_dkim_dns_token_value1(self) -> builtins.str:
        '''The record value for the first token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: DkimDNSTokenValue1
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenValue1"))

    @builtins.property
    @jsii.member(jsii_name="attrDkimDnsTokenValue2")
    def attr_dkim_dns_token_value2(self) -> builtins.str:
        '''The record value for the second token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: DkimDNSTokenValue2
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenValue2"))

    @builtins.property
    @jsii.member(jsii_name="attrDkimDnsTokenValue3")
    def attr_dkim_dns_token_value3(self) -> builtins.str:
        '''The record value for the third token that you have to add to the DNS configuration for your domain.

        :cloudformationAttribute: DkimDNSTokenValue3
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrDkimDnsTokenValue3"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="emailIdentity")
    def email_identity(self) -> builtins.str:
        '''The email address or domain to verify.'''
        return typing.cast(builtins.str, jsii.get(self, "emailIdentity"))

    @email_identity.setter
    def email_identity(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfc02af0c8ad1580f31a20eefddf3de5c4670d5d0e9e982f351c0a3f7be2ae99)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emailIdentity", value)

    @builtins.property
    @jsii.member(jsii_name="configurationSetAttributes")
    def configuration_set_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.ConfigurationSetAttributesProperty"]]:
        '''Used to associate a configuration set with an email identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.ConfigurationSetAttributesProperty"]], jsii.get(self, "configurationSetAttributes"))

    @configuration_set_attributes.setter
    def configuration_set_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.ConfigurationSetAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9e09bbe6ddf5291794cc13ffe01ceeb6dcf8075492dc575256ad5b6bc2f17638)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "configurationSetAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="dkimAttributes")
    def dkim_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.DkimAttributesProperty"]]:
        '''An object that contains information about the DKIM attributes for the identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.DkimAttributesProperty"]], jsii.get(self, "dkimAttributes"))

    @dkim_attributes.setter
    def dkim_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.DkimAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0032af7abed57412a3e4cb21bdf05c96c4c8d5c6176a0fce6a2c461dbb5af5d8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="dkimSigningAttributes")
    def dkim_signing_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.DkimSigningAttributesProperty"]]:
        '''If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for `Easy DKIM <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html>`_ .'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.DkimSigningAttributesProperty"]], jsii.get(self, "dkimSigningAttributes"))

    @dkim_signing_attributes.setter
    def dkim_signing_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.DkimSigningAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__465a3dad3389da07777bdda5eb33e345536e854073c4b594e089dcd18dc12c5b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dkimSigningAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="feedbackAttributes")
    def feedback_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.FeedbackAttributesProperty"]]:
        '''Used to enable or disable feedback forwarding for an identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.FeedbackAttributesProperty"]], jsii.get(self, "feedbackAttributes"))

    @feedback_attributes.setter
    def feedback_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.FeedbackAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0a601ac2f79b10ccfae6354e861623ca5b230f127792ee0f9473a78ac29db37d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "feedbackAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="mailFromAttributes")
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.MailFromAttributesProperty"]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.MailFromAttributesProperty"]], jsii.get(self, "mailFromAttributes"))

    @mail_from_attributes.setter
    def mail_from_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnEmailIdentity.MailFromAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3bfc642d317ef43c146d5f2aed5754d7210e533815ccd7d6339a4f0946d9ad7c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mailFromAttributes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.ConfigurationSetAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"configuration_set_name": "configurationSetName"},
    )
    class ConfigurationSetAttributesProperty:
        def __init__(
            self,
            *,
            configuration_set_name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used to associate a configuration set with an email identity.

            :param configuration_set_name: The configuration set to associate with an email identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                configuration_set_attributes_property = ses.CfnEmailIdentity.ConfigurationSetAttributesProperty(
                    configuration_set_name="configurationSetName"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f43c178a47220933c21060d38f5105353a7af12378df167bc4dc7fca0fffa09c)
                check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if configuration_set_name is not None:
                self._values["configuration_set_name"] = configuration_set_name

        @builtins.property
        def configuration_set_name(self) -> typing.Optional[builtins.str]:
            '''The configuration set to associate with an email identity.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-configurationsetattributes.html#cfn-ses-emailidentity-configurationsetattributes-configurationsetname
            '''
            result = self._values.get("configuration_set_name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ConfigurationSetAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.DkimAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"signing_enabled": "signingEnabled"},
    )
    class DkimAttributesProperty:
        def __init__(
            self,
            *,
            signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Used to enable or disable DKIM authentication for an email identity.

            :param signing_enabled: Sets the DKIM signing configuration for the identity. When you set this value ``true`` , then the messages that are sent from the identity are signed using DKIM. If you set this value to ``false`` , your messages are sent without DKIM signing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dkim_attributes_property = ses.CfnEmailIdentity.DkimAttributesProperty(
                    signing_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b7e4c6c543bf26936e4c81fcb8702db27a3007ffd82e4712715e42011c5c1573)
                check_type(argname="argument signing_enabled", value=signing_enabled, expected_type=type_hints["signing_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if signing_enabled is not None:
                self._values["signing_enabled"] = signing_enabled

        @builtins.property
        def signing_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Sets the DKIM signing configuration for the identity.

            When you set this value ``true`` , then the messages that are sent from the identity are signed using DKIM. If you set this value to ``false`` , your messages are sent without DKIM signing.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimattributes.html#cfn-ses-emailidentity-dkimattributes-signingenabled
            '''
            result = self._values.get("signing_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DkimAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.DkimSigningAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "domain_signing_private_key": "domainSigningPrivateKey",
            "domain_signing_selector": "domainSigningSelector",
            "next_signing_key_length": "nextSigningKeyLength",
        },
    )
    class DkimSigningAttributesProperty:
        def __init__(
            self,
            *,
            domain_signing_private_key: typing.Optional[builtins.str] = None,
            domain_signing_selector: typing.Optional[builtins.str] = None,
            next_signing_key_length: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used to configure or change the DKIM authentication settings for an email domain identity.

            You can use this operation to do any of the following:

            - Update the signing attributes for an identity that uses Bring Your Own DKIM (BYODKIM).
            - Update the key length that should be used for Easy DKIM.
            - Change from using no DKIM authentication to using Easy DKIM.
            - Change from using no DKIM authentication to using BYODKIM.
            - Change from using Easy DKIM to using BYODKIM.
            - Change from using BYODKIM to using Easy DKIM.

            :param domain_signing_private_key: [Bring Your Own DKIM] A private key that's used to generate a DKIM signature. The private key must use 1024 or 2048-bit RSA encryption, and must be encoded using base64 encoding. .. epigraph:: Rather than embedding sensitive information directly in your CFN templates, we recommend you use dynamic parameters in the stack template to reference sensitive information that is stored and managed outside of CFN, such as in the AWS Systems Manager Parameter Store or AWS Secrets Manager. For more information, see the `Do not embed credentials in your templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#creds>`_ best practice.
            :param domain_signing_selector: [Bring Your Own DKIM] A string that's used to identify a public key in the DNS configuration for a domain.
            :param next_signing_key_length: [Easy DKIM] The key length of the future DKIM key pair to be generated. This can be changed at most once per day. Valid Values: ``RSA_1024_BIT | RSA_2048_BIT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dkim_signing_attributes_property = ses.CfnEmailIdentity.DkimSigningAttributesProperty(
                    domain_signing_private_key="domainSigningPrivateKey",
                    domain_signing_selector="domainSigningSelector",
                    next_signing_key_length="nextSigningKeyLength"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__fc9546dbbff56dcd597c3802b6ffb4259c44e6f78bb7195f924f2ee9ae6fc0a3)
                check_type(argname="argument domain_signing_private_key", value=domain_signing_private_key, expected_type=type_hints["domain_signing_private_key"])
                check_type(argname="argument domain_signing_selector", value=domain_signing_selector, expected_type=type_hints["domain_signing_selector"])
                check_type(argname="argument next_signing_key_length", value=next_signing_key_length, expected_type=type_hints["next_signing_key_length"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if domain_signing_private_key is not None:
                self._values["domain_signing_private_key"] = domain_signing_private_key
            if domain_signing_selector is not None:
                self._values["domain_signing_selector"] = domain_signing_selector
            if next_signing_key_length is not None:
                self._values["next_signing_key_length"] = next_signing_key_length

        @builtins.property
        def domain_signing_private_key(self) -> typing.Optional[builtins.str]:
            '''[Bring Your Own DKIM] A private key that's used to generate a DKIM signature.

            The private key must use 1024 or 2048-bit RSA encryption, and must be encoded using base64 encoding.
            .. epigraph::

               Rather than embedding sensitive information directly in your CFN templates, we recommend you use dynamic parameters in the stack template to reference sensitive information that is stored and managed outside of CFN, such as in the AWS Systems Manager Parameter Store or AWS Secrets Manager.

               For more information, see the `Do not embed credentials in your templates <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#creds>`_ best practice.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningprivatekey
            '''
            result = self._values.get("domain_signing_private_key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def domain_signing_selector(self) -> typing.Optional[builtins.str]:
            '''[Bring Your Own DKIM] A string that's used to identify a public key in the DNS configuration for a domain.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-domainsigningselector
            '''
            result = self._values.get("domain_signing_selector")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def next_signing_key_length(self) -> typing.Optional[builtins.str]:
            '''[Easy DKIM] The key length of the future DKIM key pair to be generated.

            This can be changed at most once per day.

            Valid Values: ``RSA_1024_BIT | RSA_2048_BIT``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-dkimsigningattributes.html#cfn-ses-emailidentity-dkimsigningattributes-nextsigningkeylength
            '''
            result = self._values.get("next_signing_key_length")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DkimSigningAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.FeedbackAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"email_forwarding_enabled": "emailForwardingEnabled"},
    )
    class FeedbackAttributesProperty:
        def __init__(
            self,
            *,
            email_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''Used to enable or disable feedback forwarding for an identity.

            This setting determines what happens when an identity is used to send an email that results in a bounce or complaint event.

            :param email_forwarding_enabled: Sets the feedback forwarding configuration for the identity. If the value is ``true`` , you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the ``Return-Path`` header of the original email. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                feedback_attributes_property = ses.CfnEmailIdentity.FeedbackAttributesProperty(
                    email_forwarding_enabled=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed64b7518613c037c1bda6f3af605613ea5857d02ec6233dbc9bb1eb38581b8c)
                check_type(argname="argument email_forwarding_enabled", value=email_forwarding_enabled, expected_type=type_hints["email_forwarding_enabled"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if email_forwarding_enabled is not None:
                self._values["email_forwarding_enabled"] = email_forwarding_enabled

        @builtins.property
        def email_forwarding_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Sets the feedback forwarding configuration for the identity.

            If the value is ``true`` , you receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the ``Return-Path`` header of the original email.

            You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-feedbackattributes.html#cfn-ses-emailidentity-feedbackattributes-emailforwardingenabled
            '''
            result = self._values.get("email_forwarding_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FeedbackAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentity.MailFromAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "behavior_on_mx_failure": "behaviorOnMxFailure",
            "mail_from_domain": "mailFromDomain",
        },
    )
    class MailFromAttributesProperty:
        def __init__(
            self,
            *,
            behavior_on_mx_failure: typing.Optional[builtins.str] = None,
            mail_from_domain: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

            :param behavior_on_mx_failure: The action to take if the required MX record isn't found when you send an email. When you set this value to ``USE_DEFAULT_VALUE`` , the mail is sent using *amazonses.com* as the MAIL FROM domain. When you set this value to ``REJECT_MESSAGE`` , the Amazon SES API v2 returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email. These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states. Valid Values: ``USE_DEFAULT_VALUE | REJECT_MESSAGE``
            :param mail_from_domain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria: - It has to be a subdomain of the verified identity. - It can't be used to receive email. - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                mail_from_attributes_property = ses.CfnEmailIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__172959be1e69fff5bd9bf8f0d9d248c8bcc08b8792f68376cb22ae4849263082)
                check_type(argname="argument behavior_on_mx_failure", value=behavior_on_mx_failure, expected_type=type_hints["behavior_on_mx_failure"])
                check_type(argname="argument mail_from_domain", value=mail_from_domain, expected_type=type_hints["mail_from_domain"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if behavior_on_mx_failure is not None:
                self._values["behavior_on_mx_failure"] = behavior_on_mx_failure
            if mail_from_domain is not None:
                self._values["mail_from_domain"] = mail_from_domain

        @builtins.property
        def behavior_on_mx_failure(self) -> typing.Optional[builtins.str]:
            '''The action to take if the required MX record isn't found when you send an email.

            When you set this value to ``USE_DEFAULT_VALUE`` , the mail is sent using *amazonses.com* as the MAIL FROM domain. When you set this value to ``REJECT_MESSAGE`` , the Amazon SES API v2 returns a ``MailFromDomainNotVerified`` error, and doesn't attempt to deliver the email.

            These behaviors are taken when the custom MAIL FROM domain configuration is in the ``Pending`` , ``Failed`` , and ``TemporaryFailure`` states.

            Valid Values: ``USE_DEFAULT_VALUE | REJECT_MESSAGE``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-behavioronmxfailure
            '''
            result = self._values.get("behavior_on_mx_failure")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def mail_from_domain(self) -> typing.Optional[builtins.str]:
            '''The custom MAIL FROM domain that you want the verified identity to use.

            The MAIL FROM domain must meet the following criteria:

            - It has to be a subdomain of the verified identity.
            - It can't be used to receive email.
            - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-emailidentity-mailfromattributes.html#cfn-ses-emailidentity-mailfromattributes-mailfromdomain
            '''
            result = self._values.get("mail_from_domain")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MailFromAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnEmailIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "email_identity": "emailIdentity",
        "configuration_set_attributes": "configurationSetAttributes",
        "dkim_attributes": "dkimAttributes",
        "dkim_signing_attributes": "dkimSigningAttributes",
        "feedback_attributes": "feedbackAttributes",
        "mail_from_attributes": "mailFromAttributes",
    },
)
class CfnEmailIdentityProps:
    def __init__(
        self,
        *,
        email_identity: builtins.str,
        configuration_set_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.ConfigurationSetAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dkim_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.DkimAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        dkim_signing_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.DkimSigningAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        feedback_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.FeedbackAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnEmailIdentity``.

        :param email_identity: The email address or domain to verify.
        :param configuration_set_attributes: Used to associate a configuration set with an email identity.
        :param dkim_attributes: An object that contains information about the DKIM attributes for the identity.
        :param dkim_signing_attributes: If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for `Easy DKIM <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html>`_ .
        :param feedback_attributes: Used to enable or disable feedback forwarding for an identity.
        :param mail_from_attributes: Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_email_identity_props = ses.CfnEmailIdentityProps(
                email_identity="emailIdentity",
            
                # the properties below are optional
                configuration_set_attributes=ses.CfnEmailIdentity.ConfigurationSetAttributesProperty(
                    configuration_set_name="configurationSetName"
                ),
                dkim_attributes=ses.CfnEmailIdentity.DkimAttributesProperty(
                    signing_enabled=False
                ),
                dkim_signing_attributes=ses.CfnEmailIdentity.DkimSigningAttributesProperty(
                    domain_signing_private_key="domainSigningPrivateKey",
                    domain_signing_selector="domainSigningSelector",
                    next_signing_key_length="nextSigningKeyLength"
                ),
                feedback_attributes=ses.CfnEmailIdentity.FeedbackAttributesProperty(
                    email_forwarding_enabled=False
                ),
                mail_from_attributes=ses.CfnEmailIdentity.MailFromAttributesProperty(
                    behavior_on_mx_failure="behaviorOnMxFailure",
                    mail_from_domain="mailFromDomain"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1981630fc48db9c9ef7ed37311c6a22c4456e2d316420d87e0ba41890a323f54)
            check_type(argname="argument email_identity", value=email_identity, expected_type=type_hints["email_identity"])
            check_type(argname="argument configuration_set_attributes", value=configuration_set_attributes, expected_type=type_hints["configuration_set_attributes"])
            check_type(argname="argument dkim_attributes", value=dkim_attributes, expected_type=type_hints["dkim_attributes"])
            check_type(argname="argument dkim_signing_attributes", value=dkim_signing_attributes, expected_type=type_hints["dkim_signing_attributes"])
            check_type(argname="argument feedback_attributes", value=feedback_attributes, expected_type=type_hints["feedback_attributes"])
            check_type(argname="argument mail_from_attributes", value=mail_from_attributes, expected_type=type_hints["mail_from_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "email_identity": email_identity,
        }
        if configuration_set_attributes is not None:
            self._values["configuration_set_attributes"] = configuration_set_attributes
        if dkim_attributes is not None:
            self._values["dkim_attributes"] = dkim_attributes
        if dkim_signing_attributes is not None:
            self._values["dkim_signing_attributes"] = dkim_signing_attributes
        if feedback_attributes is not None:
            self._values["feedback_attributes"] = feedback_attributes
        if mail_from_attributes is not None:
            self._values["mail_from_attributes"] = mail_from_attributes

    @builtins.property
    def email_identity(self) -> builtins.str:
        '''The email address or domain to verify.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-emailidentity
        '''
        result = self._values.get("email_identity")
        assert result is not None, "Required property 'email_identity' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def configuration_set_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.ConfigurationSetAttributesProperty]]:
        '''Used to associate a configuration set with an email identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-configurationsetattributes
        '''
        result = self._values.get("configuration_set_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.ConfigurationSetAttributesProperty]], result)

    @builtins.property
    def dkim_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.DkimAttributesProperty]]:
        '''An object that contains information about the DKIM attributes for the identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimattributes
        '''
        result = self._values.get("dkim_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.DkimAttributesProperty]], result)

    @builtins.property
    def dkim_signing_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.DkimSigningAttributesProperty]]:
        '''If your request includes this object, Amazon SES configures the identity to use Bring Your Own DKIM (BYODKIM) for DKIM authentication purposes, or, configures the key length to be used for `Easy DKIM <https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-dkimsigningattributes
        '''
        result = self._values.get("dkim_signing_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.DkimSigningAttributesProperty]], result)

    @builtins.property
    def feedback_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.FeedbackAttributesProperty]]:
        '''Used to enable or disable feedback forwarding for an identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-feedbackattributes
        '''
        result = self._values.get("feedback_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.FeedbackAttributesProperty]], result)

    @builtins.property
    def mail_from_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.MailFromAttributesProperty]]:
        '''Used to enable or disable the custom Mail-From domain configuration for an email identity.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-emailidentity.html#cfn-ses-emailidentity-mailfromattributes
        '''
        result = self._values.get("mail_from_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.MailFromAttributesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnEmailIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReceiptFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilter",
):
    '''Specify a new IP address filter.

    You use IP address filters when you receive email with Amazon SES.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_receipt_filter = ses.CfnReceiptFilter(self, "MyCfnReceiptFilter",
            filter=ses.CfnReceiptFilter.FilterProperty(
                ip_filter=ses.CfnReceiptFilter.IpFilterProperty(
                    cidr="cidr",
                    policy="policy"
                ),
        
                # the properties below are optional
                name="name"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        filter: typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptFilter.FilterProperty", typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param filter: A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a1615f3821db38c2d17213d45f5aaf7419e2ac2a387e68854a97ab1b660aa82)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReceiptFilterProps(filter=filter)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__68a616fc9bd0bc8eef7e85693c8a2bc90546b0b7c578a2cb94a4f7fa8c67f519)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1149bfa381ad182958c44071a0ae46750ca96fdf6137ff9e951ac1be17625bb1)
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
    @jsii.member(jsii_name="filter")
    def filter(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnReceiptFilter.FilterProperty"]:
        '''A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnReceiptFilter.FilterProperty"], jsii.get(self, "filter"))

    @filter.setter
    def filter(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnReceiptFilter.FilterProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3f3559694a52690944f1517571fda28128591a08e4458775af6322f62533e068)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filter", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilter.FilterProperty",
        jsii_struct_bases=[],
        name_mapping={"ip_filter": "ipFilter", "name": "name"},
    )
    class FilterProperty:
        def __init__(
            self,
            *,
            ip_filter: typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptFilter.IpFilterProperty", typing.Dict[builtins.str, typing.Any]]],
            name: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Specifies an IP address filter.

            :param ip_filter: A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.
            :param name: The name of the IP address filter. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). - Start and end with a letter or number. - Contain 64 characters or fewer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                filter_property = ses.CfnReceiptFilter.FilterProperty(
                    ip_filter=ses.CfnReceiptFilter.IpFilterProperty(
                        cidr="cidr",
                        policy="policy"
                    ),
                
                    # the properties below are optional
                    name="name"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a42218c982fb4338e6794b2fe9415b047ee10364d513a6dd4d4f68d79950fb97)
                check_type(argname="argument ip_filter", value=ip_filter, expected_type=type_hints["ip_filter"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "ip_filter": ip_filter,
            }
            if name is not None:
                self._values["name"] = name

        @builtins.property
        def ip_filter(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnReceiptFilter.IpFilterProperty"]:
            '''A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-ipfilter
            '''
            result = self._values.get("ip_filter")
            assert result is not None, "Required property 'ip_filter' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnReceiptFilter.IpFilterProperty"], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the IP address filter. The name must meet the following requirements:.

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
            - Start and end with a letter or number.
            - Contain 64 characters or fewer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-filter.html#cfn-ses-receiptfilter-filter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilter.IpFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"cidr": "cidr", "policy": "policy"},
    )
    class IpFilterProperty:
        def __init__(self, *, cidr: builtins.str, policy: builtins.str) -> None:
            '''A receipt IP address filter enables you to specify whether to accept or reject mail originating from an IP address or range of IP addresses.

            For information about setting up IP address filters, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-ip-filtering-console-walkthrough.html>`_ .

            :param cidr: A single IP address or a range of IP addresses to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation. An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see `RFC 2317 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2317>`_ .
            :param policy: Indicates whether to block or allow incoming mail from the specified IP addresses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                ip_filter_property = ses.CfnReceiptFilter.IpFilterProperty(
                    cidr="cidr",
                    policy="policy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__a491d6597c852f28ae26e9b6690598de1ef3f7a5ee8865818d9104b055030f97)
                check_type(argname="argument cidr", value=cidr, expected_type=type_hints["cidr"])
                check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "cidr": cidr,
                "policy": policy,
            }

        @builtins.property
        def cidr(self) -> builtins.str:
            '''A single IP address or a range of IP addresses to block or allow, specified in Classless Inter-Domain Routing (CIDR) notation.

            An example of a single email address is 10.0.0.1. An example of a range of IP addresses is 10.0.0.1/24. For more information about CIDR notation, see `RFC 2317 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc2317>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-cidr
            '''
            result = self._values.get("cidr")
            assert result is not None, "Required property 'cidr' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def policy(self) -> builtins.str:
            '''Indicates whether to block or allow incoming mail from the specified IP addresses.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptfilter-ipfilter.html#cfn-ses-receiptfilter-ipfilter-policy
            '''
            result = self._values.get("policy")
            assert result is not None, "Required property 'policy' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IpFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={"filter": "filter"},
)
class CfnReceiptFilterProps:
    def __init__(
        self,
        *,
        filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptFilter.FilterProperty, typing.Dict[builtins.str, typing.Any]]],
    ) -> None:
        '''Properties for defining a ``CfnReceiptFilter``.

        :param filter: A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_receipt_filter_props = ses.CfnReceiptFilterProps(
                filter=ses.CfnReceiptFilter.FilterProperty(
                    ip_filter=ses.CfnReceiptFilter.IpFilterProperty(
                        cidr="cidr",
                        policy="policy"
                    ),
            
                    # the properties below are optional
                    name="name"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0c3aafa7b21eb24b6b09cf371f4935926a3d6310d168a5ca16bcad331d2d6a1f)
            check_type(argname="argument filter", value=filter, expected_type=type_hints["filter"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter": filter,
        }

    @builtins.property
    def filter(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnReceiptFilter.FilterProperty]:
        '''A data structure that describes the IP address filter to create, which consists of a name, an IP address range, and whether to allow or block mail from it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptfilter.html#cfn-ses-receiptfilter-filter
        '''
        result = self._values.get("filter")
        assert result is not None, "Required property 'filter' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnReceiptFilter.FilterProperty], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReceiptRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule",
):
    '''Specifies a receipt rule.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_receipt_rule = ses.CfnReceiptRule(self, "MyCfnReceiptRule",
            rule=ses.CfnReceiptRule.RuleProperty(
                actions=[ses.CfnReceiptRule.ActionProperty(
                    add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                        header_name="headerName",
                        header_value="headerValue"
                    ),
                    bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                        message="message",
                        sender="sender",
                        smtp_reply_code="smtpReplyCode",
        
                        # the properties below are optional
                        status_code="statusCode",
                        topic_arn="topicArn"
                    ),
                    lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                        function_arn="functionArn",
        
                        # the properties below are optional
                        invocation_type="invocationType",
                        topic_arn="topicArn"
                    ),
                    s3_action=ses.CfnReceiptRule.S3ActionProperty(
                        bucket_name="bucketName",
        
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn",
                        object_key_prefix="objectKeyPrefix",
                        topic_arn="topicArn"
                    ),
                    sns_action=ses.CfnReceiptRule.SNSActionProperty(
                        encoding="encoding",
                        topic_arn="topicArn"
                    ),
                    stop_action=ses.CfnReceiptRule.StopActionProperty(
                        scope="scope",
        
                        # the properties below are optional
                        topic_arn="topicArn"
                    ),
                    workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                        organization_arn="organizationArn",
        
                        # the properties below are optional
                        topic_arn="topicArn"
                    )
                )],
                enabled=False,
                name="name",
                recipients=["recipients"],
                scan_enabled=False,
                tls_policy="tlsPolicy"
            ),
            rule_set_name="ruleSetName",
        
            # the properties below are optional
            after="after"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.RuleProperty", typing.Dict[builtins.str, typing.Any]]],
        rule_set_name: builtins.str,
        after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule: A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
        :param rule_set_name: The name of the rule set where the receipt rule is added.
        :param after: The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f11dbb9bc20b6ae8f4dbfe7500db6c36368680fbb7f5b0198623b727ca3fe253)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReceiptRuleProps(
            rule=rule, rule_set_name=rule_set_name, after=after
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0cc6c8bd23ccd04352f140aa0292c18970d3c08ee118a8a3b0fdf3f9d4ca1a77)
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
            type_hints = typing.get_type_hints(_typecheckingstub__94942bbf4a200e9bab75fe3f2144c540718074bf55275f72234642a257755afa)
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
    @jsii.member(jsii_name="rule")
    def rule(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.RuleProperty"]:
        '''A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.RuleProperty"], jsii.get(self, "rule"))

    @rule.setter
    def rule(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.RuleProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e2b7e7d80f05bbed4301e74bf1978bd0403bb680b80c53091fbc2d73a2feb77c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "rule", value)

    @builtins.property
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> builtins.str:
        '''The name of the rule set where the receipt rule is added.'''
        return typing.cast(builtins.str, jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a32508b7af75c5c3090736f7c37dc05f9a14f28535c005a911e735e4bf7360d9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetName", value)

    @builtins.property
    @jsii.member(jsii_name="after")
    def after(self) -> typing.Optional[builtins.str]:
        '''The name of an existing rule after which the new rule is placed.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "after"))

    @after.setter
    def after(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7e01f4460f2e7da87350c32dda6e4b23e8e3064fa60b2167f2ef07c44203cf85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "after", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "add_header_action": "addHeaderAction",
            "bounce_action": "bounceAction",
            "lambda_action": "lambdaAction",
            "s3_action": "s3Action",
            "sns_action": "snsAction",
            "stop_action": "stopAction",
            "workmail_action": "workmailAction",
        },
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            add_header_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.AddHeaderActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            bounce_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.BounceActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            lambda_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.LambdaActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            s3_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.S3ActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            sns_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.SNSActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            stop_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.StopActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            workmail_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.WorkmailActionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own.

            An instance of this data type can represent only one action.

            For information about setting up receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html>`_ .

            :param add_header_action: Adds a header to the received email.
            :param bounce_action: Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).
            :param lambda_action: Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
            :param s3_action: Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.
            :param sns_action: Publishes the email content within a notification to Amazon SNS.
            :param stop_action: Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
            :param workmail_action: Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                action_property = ses.CfnReceiptRule.ActionProperty(
                    add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                        header_name="headerName",
                        header_value="headerValue"
                    ),
                    bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                        message="message",
                        sender="sender",
                        smtp_reply_code="smtpReplyCode",
                
                        # the properties below are optional
                        status_code="statusCode",
                        topic_arn="topicArn"
                    ),
                    lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                        function_arn="functionArn",
                
                        # the properties below are optional
                        invocation_type="invocationType",
                        topic_arn="topicArn"
                    ),
                    s3_action=ses.CfnReceiptRule.S3ActionProperty(
                        bucket_name="bucketName",
                
                        # the properties below are optional
                        kms_key_arn="kmsKeyArn",
                        object_key_prefix="objectKeyPrefix",
                        topic_arn="topicArn"
                    ),
                    sns_action=ses.CfnReceiptRule.SNSActionProperty(
                        encoding="encoding",
                        topic_arn="topicArn"
                    ),
                    stop_action=ses.CfnReceiptRule.StopActionProperty(
                        scope="scope",
                
                        # the properties below are optional
                        topic_arn="topicArn"
                    ),
                    workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                        organization_arn="organizationArn",
                
                        # the properties below are optional
                        topic_arn="topicArn"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__2e23836e118e42c034b0eb896988a7fe715dbbacb7c1a69f5eabb3a0a74e54f3)
                check_type(argname="argument add_header_action", value=add_header_action, expected_type=type_hints["add_header_action"])
                check_type(argname="argument bounce_action", value=bounce_action, expected_type=type_hints["bounce_action"])
                check_type(argname="argument lambda_action", value=lambda_action, expected_type=type_hints["lambda_action"])
                check_type(argname="argument s3_action", value=s3_action, expected_type=type_hints["s3_action"])
                check_type(argname="argument sns_action", value=sns_action, expected_type=type_hints["sns_action"])
                check_type(argname="argument stop_action", value=stop_action, expected_type=type_hints["stop_action"])
                check_type(argname="argument workmail_action", value=workmail_action, expected_type=type_hints["workmail_action"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if add_header_action is not None:
                self._values["add_header_action"] = add_header_action
            if bounce_action is not None:
                self._values["bounce_action"] = bounce_action
            if lambda_action is not None:
                self._values["lambda_action"] = lambda_action
            if s3_action is not None:
                self._values["s3_action"] = s3_action
            if sns_action is not None:
                self._values["sns_action"] = sns_action
            if stop_action is not None:
                self._values["stop_action"] = stop_action
            if workmail_action is not None:
                self._values["workmail_action"] = workmail_action

        @builtins.property
        def add_header_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.AddHeaderActionProperty"]]:
            '''Adds a header to the received email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-addheaderaction
            '''
            result = self._values.get("add_header_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.AddHeaderActionProperty"]], result)

        @builtins.property
        def bounce_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.BounceActionProperty"]]:
            '''Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-bounceaction
            '''
            result = self._values.get("bounce_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.BounceActionProperty"]], result)

        @builtins.property
        def lambda_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.LambdaActionProperty"]]:
            '''Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-lambdaaction
            '''
            result = self._values.get("lambda_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.LambdaActionProperty"]], result)

        @builtins.property
        def s3_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.S3ActionProperty"]]:
            '''Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-s3action
            '''
            result = self._values.get("s3_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.S3ActionProperty"]], result)

        @builtins.property
        def sns_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.SNSActionProperty"]]:
            '''Publishes the email content within a notification to Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-snsaction
            '''
            result = self._values.get("sns_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.SNSActionProperty"]], result)

        @builtins.property
        def stop_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.StopActionProperty"]]:
            '''Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-stopaction
            '''
            result = self._values.get("stop_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.StopActionProperty"]], result)

        @builtins.property
        def workmail_action(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.WorkmailActionProperty"]]:
            '''Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-action.html#cfn-ses-receiptrule-action-workmailaction
            '''
            result = self._values.get("workmail_action")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.WorkmailActionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.AddHeaderActionProperty",
        jsii_struct_bases=[],
        name_mapping={"header_name": "headerName", "header_value": "headerValue"},
    )
    class AddHeaderActionProperty:
        def __init__(
            self,
            *,
            header_name: builtins.str,
            header_value: builtins.str,
        ) -> None:
            '''When included in a receipt rule, this action adds a header to the received email.

            For information about adding a header using a receipt rule, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-add-header.html>`_ .

            :param header_name: The name of the header to add to the incoming message. The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (a–z, A–Z, 0–9) characters and dashes.
            :param header_value: The content to include in the header. This value can contain up to 2048 characters. It can't contain newline ( ``\\n`` ) or carriage return ( ``\\r`` ) characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                add_header_action_property = ses.CfnReceiptRule.AddHeaderActionProperty(
                    header_name="headerName",
                    header_value="headerValue"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1a5686953122507299501d79da819371b0b28543d8d5b2e65f1ce0521437dedb)
                check_type(argname="argument header_name", value=header_name, expected_type=type_hints["header_name"])
                check_type(argname="argument header_value", value=header_value, expected_type=type_hints["header_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "header_name": header_name,
                "header_value": header_value,
            }

        @builtins.property
        def header_name(self) -> builtins.str:
            '''The name of the header to add to the incoming message.

            The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (a–z, A–Z, 0–9) characters and dashes.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headername
            '''
            result = self._values.get("header_name")
            assert result is not None, "Required property 'header_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def header_value(self) -> builtins.str:
            '''The content to include in the header.

            This value can contain up to 2048 characters. It can't contain newline ( ``\\n`` ) or carriage return ( ``\\r`` ) characters.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-addheaderaction.html#cfn-ses-receiptrule-addheaderaction-headervalue
            '''
            result = self._values.get("header_value")
            assert result is not None, "Required property 'header_value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AddHeaderActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.BounceActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "message": "message",
            "sender": "sender",
            "smtp_reply_code": "smtpReplyCode",
            "status_code": "statusCode",
            "topic_arn": "topicArn",
        },
    )
    class BounceActionProperty:
        def __init__(
            self,
            *,
            message: builtins.str,
            sender: builtins.str,
            smtp_reply_code: builtins.str,
            status_code: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            For information about sending a bounce message in response to a received email, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-bounce.html>`_ .

            :param message: Human-readable text to include in the bounce message.
            :param sender: The email address of the sender of the bounced email. This is the address from which the bounce message is sent.
            :param smtp_reply_code: The SMTP reply code, as defined by `RFC 5321 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5321>`_ .
            :param status_code: The SMTP enhanced status code, as defined by `RFC 3463 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3463>`_ .
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                bounce_action_property = ses.CfnReceiptRule.BounceActionProperty(
                    message="message",
                    sender="sender",
                    smtp_reply_code="smtpReplyCode",
                
                    # the properties below are optional
                    status_code="statusCode",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4b06ec88c0d55564d050fb3ddbd619284526dd4ec4bb0b1de97a62e89e1bbc82)
                check_type(argname="argument message", value=message, expected_type=type_hints["message"])
                check_type(argname="argument sender", value=sender, expected_type=type_hints["sender"])
                check_type(argname="argument smtp_reply_code", value=smtp_reply_code, expected_type=type_hints["smtp_reply_code"])
                check_type(argname="argument status_code", value=status_code, expected_type=type_hints["status_code"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "message": message,
                "sender": sender,
                "smtp_reply_code": smtp_reply_code,
            }
            if status_code is not None:
                self._values["status_code"] = status_code
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def message(self) -> builtins.str:
            '''Human-readable text to include in the bounce message.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-message
            '''
            result = self._values.get("message")
            assert result is not None, "Required property 'message' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def sender(self) -> builtins.str:
            '''The email address of the sender of the bounced email.

            This is the address from which the bounce message is sent.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-sender
            '''
            result = self._values.get("sender")
            assert result is not None, "Required property 'sender' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def smtp_reply_code(self) -> builtins.str:
            '''The SMTP reply code, as defined by `RFC 5321 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc5321>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-smtpreplycode
            '''
            result = self._values.get("smtp_reply_code")
            assert result is not None, "Required property 'smtp_reply_code' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def status_code(self) -> typing.Optional[builtins.str]:
            '''The SMTP enhanced status code, as defined by `RFC 3463 <https://docs.aws.amazon.com/https://tools.ietf.org/html/rfc3463>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-statuscode
            '''
            result = self._values.get("status_code")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-bounceaction.html#cfn-ses-receiptrule-bounceaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BounceActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.LambdaActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "function_arn": "functionArn",
            "invocation_type": "invocationType",
            "topic_arn": "topicArn",
        },
    )
    class LambdaActionProperty:
        def __init__(
            self,
            *,
            function_arn: builtins.str,
            invocation_type: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action calls an AWS Lambda function and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            To enable Amazon SES to call your AWS Lambda function or to publish to an Amazon SNS topic of another account, Amazon SES must have permission to access those resources. For information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .

            For information about using AWS Lambda actions in receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-lambda.html>`_ .

            :param function_arn: The Amazon Resource Name (ARN) of the AWS Lambda function. An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_ .
            :param invocation_type: The invocation type of the AWS Lambda function. An invocation type of ``RequestResponse`` means that the execution of the function immediately results in a response, and a value of ``Event`` means that the function is invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`_ . .. epigraph:: There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                lambda_action_property = ses.CfnReceiptRule.LambdaActionProperty(
                    function_arn="functionArn",
                
                    # the properties below are optional
                    invocation_type="invocationType",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e86c072abf438c4f550f87a4bbdea46bb58e82f5fe5547fafb68649041ba546f)
                check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
                check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "function_arn": function_arn,
            }
            if invocation_type is not None:
                self._values["invocation_type"] = invocation_type
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def function_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the AWS Lambda function.

            An example of an AWS Lambda function ARN is ``arn:aws:lambda:us-west-2:account-id:function:MyFunction`` . For more information about AWS Lambda, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/welcome.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
            '''
            result = self._values.get("function_arn")
            assert result is not None, "Required property 'function_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def invocation_type(self) -> typing.Optional[builtins.str]:
            '''The invocation type of the AWS Lambda function.

            An invocation type of ``RequestResponse`` means that the execution of the function immediately results in a response, and a value of ``Event`` means that the function is invoked asynchronously. The default value is ``Event`` . For information about AWS Lambda invocation types, see the `AWS Lambda Developer Guide <https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html>`_ .
            .. epigraph::

               There is a 30-second timeout on ``RequestResponse`` invocations. You should use ``Event`` invocation in most cases. Use ``RequestResponse`` only to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
            '''
            result = self._values.get("invocation_type")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LambdaActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.RuleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "actions": "actions",
            "enabled": "enabled",
            "name": "name",
            "recipients": "recipients",
            "scan_enabled": "scanEnabled",
            "tls_policy": "tlsPolicy",
        },
    )
    class RuleProperty:
        def __init__(
            self,
            *,
            actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnReceiptRule.ActionProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            name: typing.Optional[builtins.str] = None,
            recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
            scan_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            tls_policy: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.

            Each receipt rule defines a set of email addresses or domains that it applies to. If the email addresses or domains match at least one recipient address of the message, Amazon SES executes all of the receipt rule's actions on the message.

            For information about setting up receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html>`_ .

            :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.
            :param enabled: If ``true`` , the receipt rule is active. The default value is ``false`` .
            :param name: The name of the receipt rule. The name must meet the following requirements:. - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or periods (.). - Start and end with a letter or number. - Contain 64 characters or fewer.
            :param recipients: The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule matches all recipients on all verified domains.
            :param scan_enabled: If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is ``false`` .
            :param tls_policy: Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to ``Require`` , Amazon SES bounces emails that are not received over TLS. The default is ``Optional`` . Valid Values: ``Require | Optional``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                rule_property = ses.CfnReceiptRule.RuleProperty(
                    actions=[ses.CfnReceiptRule.ActionProperty(
                        add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                            header_name="headerName",
                            header_value="headerValue"
                        ),
                        bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                            message="message",
                            sender="sender",
                            smtp_reply_code="smtpReplyCode",
                
                            # the properties below are optional
                            status_code="statusCode",
                            topic_arn="topicArn"
                        ),
                        lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                            function_arn="functionArn",
                
                            # the properties below are optional
                            invocation_type="invocationType",
                            topic_arn="topicArn"
                        ),
                        s3_action=ses.CfnReceiptRule.S3ActionProperty(
                            bucket_name="bucketName",
                
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn",
                            object_key_prefix="objectKeyPrefix",
                            topic_arn="topicArn"
                        ),
                        sns_action=ses.CfnReceiptRule.SNSActionProperty(
                            encoding="encoding",
                            topic_arn="topicArn"
                        ),
                        stop_action=ses.CfnReceiptRule.StopActionProperty(
                            scope="scope",
                
                            # the properties below are optional
                            topic_arn="topicArn"
                        ),
                        workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                            organization_arn="organizationArn",
                
                            # the properties below are optional
                            topic_arn="topicArn"
                        )
                    )],
                    enabled=False,
                    name="name",
                    recipients=["recipients"],
                    scan_enabled=False,
                    tls_policy="tlsPolicy"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__597a4926fee926f01951cda574fa9265912d5bc1c5bf1e98c3410d25dd232a03)
                check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
                check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
                check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
                check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if actions is not None:
                self._values["actions"] = actions
            if enabled is not None:
                self._values["enabled"] = enabled
            if name is not None:
                self._values["name"] = name
            if recipients is not None:
                self._values["recipients"] = recipients
            if scan_enabled is not None:
                self._values["scan_enabled"] = scan_enabled
            if tls_policy is not None:
                self._values["tls_policy"] = tls_policy

        @builtins.property
        def actions(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.ActionProperty"]]]]:
            '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-actions
            '''
            result = self._values.get("actions")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnReceiptRule.ActionProperty"]]]], result)

        @builtins.property
        def enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , the receipt rule is active.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-enabled
            '''
            result = self._values.get("enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def name(self) -> typing.Optional[builtins.str]:
            '''The name of the receipt rule. The name must meet the following requirements:.

            - Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or periods (.).
            - Start and end with a letter or number.
            - Contain 64 characters or fewer.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
            '''The recipient domains and email addresses that the receipt rule applies to.

            If this field is not specified, this rule matches all recipients on all verified domains.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-recipients
            '''
            result = self._values.get("recipients")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def scan_enabled(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''If ``true`` , then messages that this receipt rule applies to are scanned for spam and viruses.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-scanenabled
            '''
            result = self._values.get("scan_enabled")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def tls_policy(self) -> typing.Optional[builtins.str]:
            '''Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

            If this parameter is set to ``Require`` , Amazon SES bounces emails that are not received over TLS. The default is ``Optional`` .

            Valid Values: ``Require | Optional``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-rule.html#cfn-ses-receiptrule-rule-tlspolicy
            '''
            result = self._values.get("tls_policy")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "RuleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.S3ActionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "bucket_name": "bucketName",
            "kms_key_arn": "kmsKeyArn",
            "object_key_prefix": "objectKeyPrefix",
            "topic_arn": "topicArn",
        },
    )
    class S3ActionProperty:
        def __init__(
            self,
            *,
            bucket_name: builtins.str,
            kms_key_arn: typing.Optional[builtins.str] = None,
            object_key_prefix: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            To enable Amazon SES to write emails to your Amazon S3 bucket, use an AWS KMS key to encrypt your emails, or publish to an Amazon SNS topic of another account, Amazon SES must have permission to access those resources. For information about granting permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .
            .. epigraph::

               When you save your emails to an Amazon S3 bucket, the maximum email size (including headers) is 40 MB. Emails larger than that bounces.

            For information about specifying Amazon S3 actions in receipt rules, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-s3.html>`_ .

            :param bucket_name: The name of the Amazon S3 bucket for incoming email.
            :param kms_key_arn: The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the default master key or a custom master key that you created in AWS KMS as follows: - To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) Region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key. - To use a custom master key that you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ . For more information about key policies, see the `AWS KMS Developer Guide <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`_ . If you do not specify a master key, Amazon SES does not encrypt your emails. .. epigraph:: Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS SDK for Java <https://docs.aws.amazon.com/sdk-for-java/>`_ and `AWS SDK for Ruby <https://docs.aws.amazon.com/sdk-for-ruby/>`_ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`_ .
            :param object_key_prefix: The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.
            :param topic_arn: The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                s3_action_property = ses.CfnReceiptRule.S3ActionProperty(
                    bucket_name="bucketName",
                
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn",
                    object_key_prefix="objectKeyPrefix",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__39d61a089bfe9f0df546774b89ce5903a571f298fca9c95b6767da42860a40aa)
                check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
                check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
                check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "bucket_name": bucket_name,
            }
            if kms_key_arn is not None:
                self._values["kms_key_arn"] = kms_key_arn
            if object_key_prefix is not None:
                self._values["object_key_prefix"] = object_key_prefix
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def bucket_name(self) -> builtins.str:
            '''The name of the Amazon S3 bucket for incoming email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
            '''
            result = self._values.get("bucket_name")
            assert result is not None, "Required property 'bucket_name' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def kms_key_arn(self) -> typing.Optional[builtins.str]:
            '''The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket.

            You can use the default master key or a custom master key that you created in AWS KMS as follows:

            - To use the default master key, provide an ARN in the form of ``arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses`` . For example, if your AWS account ID is 123456789012 and you want to use the default master key in the US West (Oregon) Region, the ARN of the default master key would be ``arn:aws:kms:us-west-2:123456789012:alias/aws/ses`` . If you use the default master key, you don't need to perform any extra steps to give Amazon SES permission to use the key.
            - To use a custom master key that you created in AWS KMS, provide the ARN of the master key and ensure that you add a statement to your key's policy to give Amazon SES permission to use it. For more information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .

            For more information about key policies, see the `AWS KMS Developer Guide <https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html>`_ . If you do not specify a master key, Amazon SES does not encrypt your emails.
            .. epigraph::

               Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your AWS KMS keys for decryption. This encryption client is currently available with the `AWS SDK for Java <https://docs.aws.amazon.com/sdk-for-java/>`_ and `AWS SDK for Ruby <https://docs.aws.amazon.com/sdk-for-ruby/>`_ only. For more information about client-side encryption using AWS KMS master keys, see the `Amazon S3 Developer Guide <https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
            '''
            result = self._values.get("kms_key_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def object_key_prefix(self) -> typing.Optional[builtins.str]:
            '''The key prefix of the Amazon S3 bucket.

            The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
            '''
            result = self._values.get("object_key_prefix")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "S3ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.SNSActionProperty",
        jsii_struct_bases=[],
        name_mapping={"encoding": "encoding", "topic_arn": "topicArn"},
    )
    class SNSActionProperty:
        def __init__(
            self,
            *,
            encoding: typing.Optional[builtins.str] = None,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            This action includes a complete copy of the email content in the Amazon SNS notifications. Amazon SNS notifications for all other actions simply provide information about the email. They do not include the email content itself.

            If you own the Amazon SNS topic, you don't need to do anything to give Amazon SES permission to publish emails to it. However, if you don't own the Amazon SNS topic, you need to attach a policy to the topic to give Amazon SES permissions to access it. For information about giving permissions, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html>`_ .
            .. epigraph::

               You can only publish emails that are 150 KB or less (including the header) to Amazon SNS. Larger emails bounce. If you anticipate emails larger than 150 KB, use the S3 action instead.

            For information about using a receipt rule to publish an Amazon SNS notification, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-sns.html>`_ .

            :param encoding: The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                s_nSAction_property = ses.CfnReceiptRule.SNSActionProperty(
                    encoding="encoding",
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c7b69991ab1bae6b3b263f1a32cdb917531b7939f873cf674e3a6f502dac1460)
                check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if encoding is not None:
                self._values["encoding"] = encoding
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def encoding(self) -> typing.Optional[builtins.str]:
            '''The encoding to use for the email within the Amazon SNS notification.

            UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
            '''
            result = self._values.get("encoding")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SNSActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.StopActionProperty",
        jsii_struct_bases=[],
        name_mapping={"scope": "scope", "topic_arn": "topicArn"},
    )
    class StopActionProperty:
        def __init__(
            self,
            *,
            scope: builtins.str,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action terminates the evaluation of the receipt rule set and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            For information about setting a stop action in a receipt rule, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-stop.html>`_ .

            :param scope: The scope of the StopAction. The only acceptable value is ``RuleSet`` .
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ Amazon SNS operation. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                stop_action_property = ses.CfnReceiptRule.StopActionProperty(
                    scope="scope",
                
                    # the properties below are optional
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__929ccdfb2c00fb70aa707e5c7a40fde32e556e0f220a13e8231bbacd2653b8a4)
                check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "scope": scope,
            }
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def scope(self) -> builtins.str:
            '''The scope of the StopAction.

            The only acceptable value is ``RuleSet`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
            '''
            result = self._values.get("scope")
            assert result is not None, "Required property 'scope' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ Amazon SNS operation.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StopActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRule.WorkmailActionProperty",
        jsii_struct_bases=[],
        name_mapping={"organization_arn": "organizationArn", "topic_arn": "topicArn"},
    )
    class WorkmailActionProperty:
        def __init__(
            self,
            *,
            organization_arn: builtins.str,
            topic_arn: typing.Optional[builtins.str] = None,
        ) -> None:
            '''When included in a receipt rule, this action calls Amazon WorkMail and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

            It usually isn't necessary to set this up manually, because Amazon WorkMail adds the rule automatically during its setup procedure.

            For information using a receipt rule to call Amazon WorkMail, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-action-workmail.html>`_ .

            :param organization_arn: The Amazon Resource Name (ARN) of the Amazon WorkMail organization. Amazon WorkMail ARNs use the following format:. ``arn:aws:workmail:<region>:<awsAccountId>:organization/<workmailOrganizationId>`` You can find the ID of your organization by using the `ListOrganizations <https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html>`_ operation in Amazon WorkMail. Amazon WorkMail organization IDs begin with " ``m-`` ", followed by a string of alphanumeric characters. For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`_ .
            :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS. For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                workmail_action_property = ses.CfnReceiptRule.WorkmailActionProperty(
                    organization_arn="organizationArn",
                
                    # the properties below are optional
                    topic_arn="topicArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__af2dae7f39846f3f50114d44fa542e8b0390a51e98f63405b5a32de3f95af669)
                check_type(argname="argument organization_arn", value=organization_arn, expected_type=type_hints["organization_arn"])
                check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "organization_arn": organization_arn,
            }
            if topic_arn is not None:
                self._values["topic_arn"] = topic_arn

        @builtins.property
        def organization_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the Amazon WorkMail organization. Amazon WorkMail ARNs use the following format:.

            ``arn:aws:workmail:<region>:<awsAccountId>:organization/<workmailOrganizationId>``

            You can find the ID of your organization by using the `ListOrganizations <https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html>`_ operation in Amazon WorkMail. Amazon WorkMail organization IDs begin with " ``m-`` ", followed by a string of alphanumeric characters.

            For information about Amazon WorkMail organizations, see the `Amazon WorkMail Administrator Guide <https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
            '''
            result = self._values.get("organization_arn")
            assert result is not None, "Required property 'organization_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def topic_arn(self) -> typing.Optional[builtins.str]:
            '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called.

            You can find the ARN of a topic by using the `ListTopics <https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html>`_ operation in Amazon SNS.

            For more information about Amazon SNS topics, see the `Amazon SNS Developer Guide <https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html>`_ .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
            '''
            result = self._values.get("topic_arn")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WorkmailActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRuleProps",
    jsii_struct_bases=[],
    name_mapping={"rule": "rule", "rule_set_name": "ruleSetName", "after": "after"},
)
class CfnReceiptRuleProps:
    def __init__(
        self,
        *,
        rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
        rule_set_name: builtins.str,
        after: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnReceiptRule``.

        :param rule: A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.
        :param rule_set_name: The name of the rule set where the receipt rule is added.
        :param after: The name of an existing rule after which the new rule is placed. If this parameter is null, the new rule is inserted at the beginning of the rule list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_receipt_rule_props = ses.CfnReceiptRuleProps(
                rule=ses.CfnReceiptRule.RuleProperty(
                    actions=[ses.CfnReceiptRule.ActionProperty(
                        add_header_action=ses.CfnReceiptRule.AddHeaderActionProperty(
                            header_name="headerName",
                            header_value="headerValue"
                        ),
                        bounce_action=ses.CfnReceiptRule.BounceActionProperty(
                            message="message",
                            sender="sender",
                            smtp_reply_code="smtpReplyCode",
            
                            # the properties below are optional
                            status_code="statusCode",
                            topic_arn="topicArn"
                        ),
                        lambda_action=ses.CfnReceiptRule.LambdaActionProperty(
                            function_arn="functionArn",
            
                            # the properties below are optional
                            invocation_type="invocationType",
                            topic_arn="topicArn"
                        ),
                        s3_action=ses.CfnReceiptRule.S3ActionProperty(
                            bucket_name="bucketName",
            
                            # the properties below are optional
                            kms_key_arn="kmsKeyArn",
                            object_key_prefix="objectKeyPrefix",
                            topic_arn="topicArn"
                        ),
                        sns_action=ses.CfnReceiptRule.SNSActionProperty(
                            encoding="encoding",
                            topic_arn="topicArn"
                        ),
                        stop_action=ses.CfnReceiptRule.StopActionProperty(
                            scope="scope",
            
                            # the properties below are optional
                            topic_arn="topicArn"
                        ),
                        workmail_action=ses.CfnReceiptRule.WorkmailActionProperty(
                            organization_arn="organizationArn",
            
                            # the properties below are optional
                            topic_arn="topicArn"
                        )
                    )],
                    enabled=False,
                    name="name",
                    recipients=["recipients"],
                    scan_enabled=False,
                    tls_policy="tlsPolicy"
                ),
                rule_set_name="ruleSetName",
            
                # the properties below are optional
                after="after"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__aab91d8adb8d443158cc46ba99ec820f62513cdec0b436079652f454fb21cfd1)
            check_type(argname="argument rule", value=rule, expected_type=type_hints["rule"])
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule": rule,
            "rule_set_name": rule_set_name,
        }
        if after is not None:
            self._values["after"] = after

    @builtins.property
    def rule(self) -> typing.Union[_IResolvable_da3f097b, CfnReceiptRule.RuleProperty]:
        '''A data structure that contains the specified rule's name, actions, recipients, domains, enabled status, scan status, and TLS policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rule
        '''
        result = self._values.get("rule")
        assert result is not None, "Required property 'rule' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnReceiptRule.RuleProperty], result)

    @builtins.property
    def rule_set_name(self) -> builtins.str:
        '''The name of the rule set where the receipt rule is added.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-rulesetname
        '''
        result = self._values.get("rule_set_name")
        assert result is not None, "Required property 'rule_set_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def after(self) -> typing.Optional[builtins.str]:
        '''The name of an existing rule after which the new rule is placed.

        If this parameter is null, the new rule is inserted at the beginning of the rule list.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptrule.html#cfn-ses-receiptrule-after
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnReceiptRuleSet(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRuleSet",
):
    '''Creates an empty receipt rule set.

    For information about setting up receipt rule sets, see the `Amazon SES Developer Guide <https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules>`_ .

    You can execute this operation no more than once per second.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_receipt_rule_set = ses.CfnReceiptRuleSet(self, "MyCfnReceiptRuleSet",
            rule_set_name="ruleSetName"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule_set_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param rule_set_name: The name of the receipt rule set to reorder.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c8e8c05ea09aa8fb4e787d2e45cbe7d16eaf164f24c154797b3e350dd0b5316c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnReceiptRuleSetProps(rule_set_name=rule_set_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7c30f7f0ed5cc61e57a58c5fb1de4ed0806ee6c9530ac2ce5ec04192a40fadbb)
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
            type_hints = typing.get_type_hints(_typecheckingstub__45b28225e64d365acc2eb75263d1547441c57ed192fa484b706bcc0a87784fb8)
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
    @jsii.member(jsii_name="ruleSetName")
    def rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the receipt rule set to reorder.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "ruleSetName"))

    @rule_set_name.setter
    def rule_set_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7df684309baff9de02a1535483083992de84a7e4b7e34279f0dd37bd4bb1fcb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ruleSetName", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnReceiptRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={"rule_set_name": "ruleSetName"},
)
class CfnReceiptRuleSetProps:
    def __init__(self, *, rule_set_name: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``CfnReceiptRuleSet``.

        :param rule_set_name: The name of the receipt rule set to reorder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_receipt_rule_set_props = ses.CfnReceiptRuleSetProps(
                rule_set_name="ruleSetName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ea296ac8e1ca4779dc1c9f1d5d572e1ae5dd8506ecf9694e2fb73b514ae26636)
            check_type(argname="argument rule_set_name", value=rule_set_name, expected_type=type_hints["rule_set_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if rule_set_name is not None:
            self._values["rule_set_name"] = rule_set_name

    @builtins.property
    def rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name of the receipt rule set to reorder.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-receiptruleset.html#cfn-ses-receiptruleset-rulesetname
        '''
        result = self._values.get("rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnReceiptRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnTemplate(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnTemplate",
):
    '''Specifies an email template.

    Email templates enable you to send personalized email to one or more destinations in a single API operation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_template = ses.CfnTemplate(self, "MyCfnTemplate",
            template=ses.CfnTemplate.TemplateProperty(
                subject_part="subjectPart",
        
                # the properties below are optional
                html_part="htmlPart",
                template_name="templateName",
                text_part="textPart"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnTemplate.TemplateProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param template: The content of the email, composed of a subject line and either an HTML part or a text-only part.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4c2a147151a6167a3d150f74c144fd60570fc7ac0777706d24a8e9f23813a8d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnTemplateProps(template=template)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d39d28f6ac0b8cfc4db621cda159b70e8ee1c7d0086afcb587c1b723beed970a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9fff6f1c96944fa0c793bff8f36a0f674d1885a636bfa82f985a29ba0ee07623)
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
    @jsii.member(jsii_name="template")
    def template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateProperty"]]:
        '''The content of the email, composed of a subject line and either an HTML part or a text-only part.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateProperty"]], jsii.get(self, "template"))

    @template.setter
    def template(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnTemplate.TemplateProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dfedec4ff1cee818b04e3b27b75fd775d9a21039cce2bb50f0eee75bbe3b7d0c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "template", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnTemplate.TemplateProperty",
        jsii_struct_bases=[],
        name_mapping={
            "subject_part": "subjectPart",
            "html_part": "htmlPart",
            "template_name": "templateName",
            "text_part": "textPart",
        },
    )
    class TemplateProperty:
        def __init__(
            self,
            *,
            subject_part: builtins.str,
            html_part: typing.Optional[builtins.str] = None,
            template_name: typing.Optional[builtins.str] = None,
            text_part: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The content of the email, composed of a subject line and either an HTML part or a text-only part.

            :param subject_part: The subject line of the email.
            :param html_part: The HTML body of the email.
            :param template_name: The name of the template.
            :param text_part: The email body that is visible to recipients whose email clients do not display HTML content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                template_property = ses.CfnTemplate.TemplateProperty(
                    subject_part="subjectPart",
                
                    # the properties below are optional
                    html_part="htmlPart",
                    template_name="templateName",
                    text_part="textPart"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__6894407236d481fe73e1d7b05b61377a9e1a2ea9e6ee4bfaa48a81bd5fb84352)
                check_type(argname="argument subject_part", value=subject_part, expected_type=type_hints["subject_part"])
                check_type(argname="argument html_part", value=html_part, expected_type=type_hints["html_part"])
                check_type(argname="argument template_name", value=template_name, expected_type=type_hints["template_name"])
                check_type(argname="argument text_part", value=text_part, expected_type=type_hints["text_part"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "subject_part": subject_part,
            }
            if html_part is not None:
                self._values["html_part"] = html_part
            if template_name is not None:
                self._values["template_name"] = template_name
            if text_part is not None:
                self._values["text_part"] = text_part

        @builtins.property
        def subject_part(self) -> builtins.str:
            '''The subject line of the email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-subjectpart
            '''
            result = self._values.get("subject_part")
            assert result is not None, "Required property 'subject_part' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def html_part(self) -> typing.Optional[builtins.str]:
            '''The HTML body of the email.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-htmlpart
            '''
            result = self._values.get("html_part")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def template_name(self) -> typing.Optional[builtins.str]:
            '''The name of the template.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-templatename
            '''
            result = self._values.get("template_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def text_part(self) -> typing.Optional[builtins.str]:
            '''The email body that is visible to recipients whose email clients do not display HTML content.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-template-template.html#cfn-ses-template-template-textpart
            '''
            result = self._values.get("text_part")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TemplateProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnTemplateProps",
    jsii_struct_bases=[],
    name_mapping={"template": "template"},
)
class CfnTemplateProps:
    def __init__(
        self,
        *,
        template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnTemplate``.

        :param template: The content of the email, composed of a subject line and either an HTML part or a text-only part.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_template_props = ses.CfnTemplateProps(
                template=ses.CfnTemplate.TemplateProperty(
                    subject_part="subjectPart",
            
                    # the properties below are optional
                    html_part="htmlPart",
                    template_name="templateName",
                    text_part="textPart"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6fbf4906a406135dc7de9d65c40076a5a27ccfef54ca9df5243bcf8ef9349317)
            check_type(argname="argument template", value=template, expected_type=type_hints["template"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if template is not None:
            self._values["template"] = template

    @builtins.property
    def template(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateProperty]]:
        '''The content of the email, composed of a subject line and either an HTML part or a text-only part.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-template.html#cfn-ses-template-template
        '''
        result = self._values.get("template")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnTemplateProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnVdmAttributes(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.CfnVdmAttributes",
):
    '''The Virtual Deliverability Manager (VDM) attributes that apply to your Amazon SES account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        cfn_vdm_attributes = ses.CfnVdmAttributes(self, "MyCfnVdmAttributes",
            dashboard_attributes=ses.CfnVdmAttributes.DashboardAttributesProperty(
                engagement_metrics="engagementMetrics"
            ),
            guardian_attributes=ses.CfnVdmAttributes.GuardianAttributesProperty(
                optimized_shared_delivery="optimizedSharedDelivery"
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dashboard_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnVdmAttributes.DashboardAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        guardian_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnVdmAttributes.GuardianAttributesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param dashboard_attributes: Specifies additional settings for your VDM configuration as applicable to the Dashboard.
        :param guardian_attributes: Specifies additional settings for your VDM configuration as applicable to the Guardian.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8da690d721f4dc54f54ac8a93b1521ab4f1dbb885e7ddaa381dfa79dcb6e469f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnVdmAttributesProps(
            dashboard_attributes=dashboard_attributes,
            guardian_attributes=guardian_attributes,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__19e20bbedca430ef6dc1634692c0b7c55c20f1fdf5542edb402f0e0b5bb364c7)
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
            type_hints = typing.get_type_hints(_typecheckingstub__08e60b0b9db028ea74a1508c4ca53cf07d947a35c08e25b8bd2e6c491ef82c63)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrVdmAttributesResourceId")
    def attr_vdm_attributes_resource_id(self) -> builtins.str:
        '''Unique identifier for this resource.

        :cloudformationAttribute: VdmAttributesResourceId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrVdmAttributesResourceId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="dashboardAttributes")
    def dashboard_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVdmAttributes.DashboardAttributesProperty"]]:
        '''Specifies additional settings for your VDM configuration as applicable to the Dashboard.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVdmAttributes.DashboardAttributesProperty"]], jsii.get(self, "dashboardAttributes"))

    @dashboard_attributes.setter
    def dashboard_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVdmAttributes.DashboardAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d6de577b4b973e97e1a4f2e820f91d3de6f0608ab40978d3d66537a9fc470544)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "dashboardAttributes", value)

    @builtins.property
    @jsii.member(jsii_name="guardianAttributes")
    def guardian_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVdmAttributes.GuardianAttributesProperty"]]:
        '''Specifies additional settings for your VDM configuration as applicable to the Guardian.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVdmAttributes.GuardianAttributesProperty"]], jsii.get(self, "guardianAttributes"))

    @guardian_attributes.setter
    def guardian_attributes(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnVdmAttributes.GuardianAttributesProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d777849ef648598e745e2dd5179eb670b0345a6656279e557481001d8bfa0419)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "guardianAttributes", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnVdmAttributes.DashboardAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"engagement_metrics": "engagementMetrics"},
    )
    class DashboardAttributesProperty:
        def __init__(
            self,
            *,
            engagement_metrics: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings for your VDM configuration as applicable to the Dashboard.

            :param engagement_metrics: Specifies the status of your VDM engagement metrics collection. Can be one of the following:. - ``ENABLED`` – Amazon SES enables engagement metrics for your account. - ``DISABLED`` – Amazon SES disables engagement metrics for your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                dashboard_attributes_property = ses.CfnVdmAttributes.DashboardAttributesProperty(
                    engagement_metrics="engagementMetrics"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7bb318ca7ff1c3e34c0a31904f95354c80864527eeb292bf9db6ea3ac8dab61c)
                check_type(argname="argument engagement_metrics", value=engagement_metrics, expected_type=type_hints["engagement_metrics"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if engagement_metrics is not None:
                self._values["engagement_metrics"] = engagement_metrics

        @builtins.property
        def engagement_metrics(self) -> typing.Optional[builtins.str]:
            '''Specifies the status of your VDM engagement metrics collection. Can be one of the following:.

            - ``ENABLED`` – Amazon SES enables engagement metrics for your account.
            - ``DISABLED`` – Amazon SES disables engagement metrics for your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-dashboardattributes.html#cfn-ses-vdmattributes-dashboardattributes-engagementmetrics
            '''
            result = self._values.get("engagement_metrics")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DashboardAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_ses.CfnVdmAttributes.GuardianAttributesProperty",
        jsii_struct_bases=[],
        name_mapping={"optimized_shared_delivery": "optimizedSharedDelivery"},
    )
    class GuardianAttributesProperty:
        def __init__(
            self,
            *,
            optimized_shared_delivery: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Settings for your VDM configuration as applicable to the Guardian.

            :param optimized_shared_delivery: Specifies the status of your VDM optimized shared delivery. Can be one of the following:. - ``ENABLED`` – Amazon SES enables optimized shared delivery for your account. - ``DISABLED`` – Amazon SES disables optimized shared delivery for your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_ses as ses
                
                guardian_attributes_property = ses.CfnVdmAttributes.GuardianAttributesProperty(
                    optimized_shared_delivery="optimizedSharedDelivery"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c129497041cde369dd20c917699582d68e5a27620a3bdb6da3a7048e743a3cdf)
                check_type(argname="argument optimized_shared_delivery", value=optimized_shared_delivery, expected_type=type_hints["optimized_shared_delivery"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if optimized_shared_delivery is not None:
                self._values["optimized_shared_delivery"] = optimized_shared_delivery

        @builtins.property
        def optimized_shared_delivery(self) -> typing.Optional[builtins.str]:
            '''Specifies the status of your VDM optimized shared delivery. Can be one of the following:.

            - ``ENABLED`` – Amazon SES enables optimized shared delivery for your account.
            - ``DISABLED`` – Amazon SES disables optimized shared delivery for your account.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-vdmattributes-guardianattributes.html#cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery
            '''
            result = self._values.get("optimized_shared_delivery")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "GuardianAttributesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CfnVdmAttributesProps",
    jsii_struct_bases=[],
    name_mapping={
        "dashboard_attributes": "dashboardAttributes",
        "guardian_attributes": "guardianAttributes",
    },
)
class CfnVdmAttributesProps:
    def __init__(
        self,
        *,
        dashboard_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVdmAttributes.DashboardAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        guardian_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVdmAttributes.GuardianAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnVdmAttributes``.

        :param dashboard_attributes: Specifies additional settings for your VDM configuration as applicable to the Dashboard.
        :param guardian_attributes: Specifies additional settings for your VDM configuration as applicable to the Guardian.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cfn_vdm_attributes_props = ses.CfnVdmAttributesProps(
                dashboard_attributes=ses.CfnVdmAttributes.DashboardAttributesProperty(
                    engagement_metrics="engagementMetrics"
                ),
                guardian_attributes=ses.CfnVdmAttributes.GuardianAttributesProperty(
                    optimized_shared_delivery="optimizedSharedDelivery"
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05720eed835713353d777877a75758a4e172dae5b79690ea107edcb7cf1e4825)
            check_type(argname="argument dashboard_attributes", value=dashboard_attributes, expected_type=type_hints["dashboard_attributes"])
            check_type(argname="argument guardian_attributes", value=guardian_attributes, expected_type=type_hints["guardian_attributes"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dashboard_attributes is not None:
            self._values["dashboard_attributes"] = dashboard_attributes
        if guardian_attributes is not None:
            self._values["guardian_attributes"] = guardian_attributes

    @builtins.property
    def dashboard_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVdmAttributes.DashboardAttributesProperty]]:
        '''Specifies additional settings for your VDM configuration as applicable to the Dashboard.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-dashboardattributes
        '''
        result = self._values.get("dashboard_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVdmAttributes.DashboardAttributesProperty]], result)

    @builtins.property
    def guardian_attributes(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVdmAttributes.GuardianAttributesProperty]]:
        '''Specifies additional settings for your VDM configuration as applicable to the Guardian.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ses-vdmattributes.html#cfn-ses-vdmattributes-guardianattributes
        '''
        result = self._values.get("guardian_attributes")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVdmAttributes.GuardianAttributesProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnVdmAttributesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.CloudWatchDimension",
    jsii_struct_bases=[],
    name_mapping={"default_value": "defaultValue", "name": "name", "source": "source"},
)
class CloudWatchDimension:
    def __init__(
        self,
        *,
        default_value: builtins.str,
        name: builtins.str,
        source: "CloudWatchDimensionSource",
    ) -> None:
        '''A CloudWatch dimension upon which to categorize your emails.

        :param default_value: The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email.
        :param name: The name of an Amazon CloudWatch dimension associated with an email sending metric.
        :param source: The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            cloud_watch_dimension = ses.CloudWatchDimension(
                default_value="defaultValue",
                name="name",
                source=ses.CloudWatchDimensionSource.EMAIL_HEADER
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c718e80d3dd746209ff12fd14d08ce529bed18f85e0af362c1a2df8b5adc173a)
            check_type(argname="argument default_value", value=default_value, expected_type=type_hints["default_value"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument source", value=source, expected_type=type_hints["source"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "default_value": default_value,
            "name": name,
            "source": source,
        }

    @builtins.property
    def default_value(self) -> builtins.str:
        '''The default value of the dimension that is published to Amazon CloudWatch if you do not provide the value of the dimension when you send an email.'''
        result = self._values.get("default_value")
        assert result is not None, "Required property 'default_value' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of an Amazon CloudWatch dimension associated with an email sending metric.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source(self) -> "CloudWatchDimensionSource":
        '''The place where Amazon SES finds the value of a dimension to publish to Amazon CloudWatch.'''
        result = self._values.get("source")
        assert result is not None, "Required property 'source' is missing"
        return typing.cast("CloudWatchDimensionSource", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CloudWatchDimension(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.CloudWatchDimensionSource")
class CloudWatchDimensionSource(enum.Enum):
    '''Source for CloudWatch dimension.'''

    EMAIL_HEADER = "EMAIL_HEADER"
    '''Amazon SES retrieves the dimension name and value from a header in the email.

    Note: You can't use any of the following email headers as the Dimension Name:
    ``Received``, ``To``, ``From``, ``DKIM-Signature``, ``CC``, ``message-id``, or ``Return-Path``.
    '''
    LINK_TAG = "LINK_TAG"
    '''Amazon SES retrieves the dimension name and value from a tag that you specified in a link.

    :see: https://docs.aws.amazon.com/ses/latest/dg/faqs-metrics.html#sending-metric-faqs-clicks-q5
    '''
    MESSAGE_TAG = "MESSAGE_TAG"
    '''Amazon SES retrieves the dimension name and value from a tag that you specify by using the ``X-SES-MESSAGE-TAGS`` header or the Tags API parameter.

    You can also use the Message Tag value source to create dimensions based on Amazon SES auto-tags.
    To use an auto-tag, type the complete name of the auto-tag as the Dimension Name. For example,
    to create a dimension based on the configuration set auto-tag, use ``ses:configuration-set`` for the
    Dimension Name, and the name of the configuration set for the Default Value.

    :see: https://docs.aws.amazon.com/ses/latest/dg/monitor-using-event-publishing.html#event-publishing-how-works
    '''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetEventDestinationOptions",
    jsii_struct_bases=[],
    name_mapping={
        "destination": "destination",
        "configuration_set_event_destination_name": "configurationSetEventDestinationName",
        "enabled": "enabled",
        "events": "events",
    },
)
class ConfigurationSetEventDestinationOptions:
    def __init__(
        self,
        *,
        destination: "EventDestination",
        configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        events: typing.Optional[typing.Sequence["EmailSendingEvent"]] = None,
    ) -> None:
        '''Options for a configuration set event destination.

        :param destination: The event destination.
        :param configuration_set_event_destination_name: A name for the configuration set event destination. Default: - a CloudFormation generated name
        :param enabled: Whether Amazon SES publishes events to this destination. Default: true
        :param events: The type of email sending events to publish to the event destination. Default: - send all event types

        :exampleMetadata: infused

        Example::

            # my_configuration_set: ses.ConfigurationSet
            # my_topic: sns.Topic
            
            
            my_configuration_set.add_event_destination("ToSns",
                destination=ses.EventDestination.sns_topic(my_topic)
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__80b5162c2d2ea9081e7450a4b5db43212eaf82f433a217fb2be6e012977034b6)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument configuration_set_event_destination_name", value=configuration_set_event_destination_name, expected_type=type_hints["configuration_set_event_destination_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
        }
        if configuration_set_event_destination_name is not None:
            self._values["configuration_set_event_destination_name"] = configuration_set_event_destination_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if events is not None:
            self._values["events"] = events

    @builtins.property
    def destination(self) -> "EventDestination":
        '''The event destination.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("EventDestination", result)

    @builtins.property
    def configuration_set_event_destination_name(self) -> typing.Optional[builtins.str]:
        '''A name for the configuration set event destination.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("configuration_set_event_destination_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether Amazon SES publishes events to this destination.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List["EmailSendingEvent"]]:
        '''The type of email sending events to publish to the event destination.

        :default: - send all event types
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List["EmailSendingEvent"]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetEventDestinationOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetEventDestinationProps",
    jsii_struct_bases=[ConfigurationSetEventDestinationOptions],
    name_mapping={
        "destination": "destination",
        "configuration_set_event_destination_name": "configurationSetEventDestinationName",
        "enabled": "enabled",
        "events": "events",
        "configuration_set": "configurationSet",
    },
)
class ConfigurationSetEventDestinationProps(ConfigurationSetEventDestinationOptions):
    def __init__(
        self,
        *,
        destination: "EventDestination",
        configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        events: typing.Optional[typing.Sequence["EmailSendingEvent"]] = None,
        configuration_set: "IConfigurationSet",
    ) -> None:
        '''Properties for a configuration set event destination.

        :param destination: The event destination.
        :param configuration_set_event_destination_name: A name for the configuration set event destination. Default: - a CloudFormation generated name
        :param enabled: Whether Amazon SES publishes events to this destination. Default: true
        :param events: The type of email sending events to publish to the event destination. Default: - send all event types
        :param configuration_set: The configuration set that contains the event destination.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            # configuration_set: ses.ConfigurationSet
            # event_destination: ses.EventDestination
            
            configuration_set_event_destination_props = ses.ConfigurationSetEventDestinationProps(
                configuration_set=configuration_set,
                destination=event_destination,
            
                # the properties below are optional
                configuration_set_event_destination_name="configurationSetEventDestinationName",
                enabled=False,
                events=[ses.EmailSendingEvent.SEND]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd3ac4f1af1f2fe9c11fa8894b2eae0f4b13c464b826cffda8b6937f4ab3e9c8)
            check_type(argname="argument destination", value=destination, expected_type=type_hints["destination"])
            check_type(argname="argument configuration_set_event_destination_name", value=configuration_set_event_destination_name, expected_type=type_hints["configuration_set_event_destination_name"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument events", value=events, expected_type=type_hints["events"])
            check_type(argname="argument configuration_set", value=configuration_set, expected_type=type_hints["configuration_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "destination": destination,
            "configuration_set": configuration_set,
        }
        if configuration_set_event_destination_name is not None:
            self._values["configuration_set_event_destination_name"] = configuration_set_event_destination_name
        if enabled is not None:
            self._values["enabled"] = enabled
        if events is not None:
            self._values["events"] = events

    @builtins.property
    def destination(self) -> "EventDestination":
        '''The event destination.'''
        result = self._values.get("destination")
        assert result is not None, "Required property 'destination' is missing"
        return typing.cast("EventDestination", result)

    @builtins.property
    def configuration_set_event_destination_name(self) -> typing.Optional[builtins.str]:
        '''A name for the configuration set event destination.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("configuration_set_event_destination_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether Amazon SES publishes events to this destination.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def events(self) -> typing.Optional[typing.List["EmailSendingEvent"]]:
        '''The type of email sending events to publish to the event destination.

        :default: - send all event types
        '''
        result = self._values.get("events")
        return typing.cast(typing.Optional[typing.List["EmailSendingEvent"]], result)

    @builtins.property
    def configuration_set(self) -> "IConfigurationSet":
        '''The configuration set that contains the event destination.'''
        result = self._values.get("configuration_set")
        assert result is not None, "Required property 'configuration_set' is missing"
        return typing.cast("IConfigurationSet", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetEventDestinationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "configuration_set_name": "configurationSetName",
        "custom_tracking_redirect_domain": "customTrackingRedirectDomain",
        "dedicated_ip_pool": "dedicatedIpPool",
        "reputation_metrics": "reputationMetrics",
        "sending_enabled": "sendingEnabled",
        "suppression_reasons": "suppressionReasons",
        "tls_policy": "tlsPolicy",
    },
)
class ConfigurationSetProps:
    def __init__(
        self,
        *,
        configuration_set_name: typing.Optional[builtins.str] = None,
        custom_tracking_redirect_domain: typing.Optional[builtins.str] = None,
        dedicated_ip_pool: typing.Optional["IDedicatedIpPool"] = None,
        reputation_metrics: typing.Optional[builtins.bool] = None,
        sending_enabled: typing.Optional[builtins.bool] = None,
        suppression_reasons: typing.Optional["SuppressionReasons"] = None,
        tls_policy: typing.Optional["ConfigurationSetTlsPolicy"] = None,
    ) -> None:
        '''Properties for a configuration set.

        :param configuration_set_name: A name for the configuration set. Default: - a CloudFormation generated name
        :param custom_tracking_redirect_domain: The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain. Default: - use the default awstrack.me domain
        :param dedicated_ip_pool: The dedicated IP pool to associate with the configuration set. Default: - do not use a dedicated IP pool
        :param reputation_metrics: Whether to publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch. Default: false
        :param sending_enabled: Whether email sending is enabled. Default: true
        :param suppression_reasons: The reasons for which recipient email addresses should be automatically added to your account's suppression list. Default: - use account level settings
        :param tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). Default: ConfigurationSetTlsPolicy.OPTIONAL

        :exampleMetadata: infused

        Example::

            # my_pool: ses.IDedicatedIpPool
            
            
            ses.ConfigurationSet(self, "ConfigurationSet",
                custom_tracking_redirect_domain="track.cdk.dev",
                suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
                tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
                dedicated_ip_pool=my_pool
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb010161f6c1e40b88122d9cb7754dae093e9cbe5bbfc72b19737729a4f4523d)
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
            check_type(argname="argument custom_tracking_redirect_domain", value=custom_tracking_redirect_domain, expected_type=type_hints["custom_tracking_redirect_domain"])
            check_type(argname="argument dedicated_ip_pool", value=dedicated_ip_pool, expected_type=type_hints["dedicated_ip_pool"])
            check_type(argname="argument reputation_metrics", value=reputation_metrics, expected_type=type_hints["reputation_metrics"])
            check_type(argname="argument sending_enabled", value=sending_enabled, expected_type=type_hints["sending_enabled"])
            check_type(argname="argument suppression_reasons", value=suppression_reasons, expected_type=type_hints["suppression_reasons"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if configuration_set_name is not None:
            self._values["configuration_set_name"] = configuration_set_name
        if custom_tracking_redirect_domain is not None:
            self._values["custom_tracking_redirect_domain"] = custom_tracking_redirect_domain
        if dedicated_ip_pool is not None:
            self._values["dedicated_ip_pool"] = dedicated_ip_pool
        if reputation_metrics is not None:
            self._values["reputation_metrics"] = reputation_metrics
        if sending_enabled is not None:
            self._values["sending_enabled"] = sending_enabled
        if suppression_reasons is not None:
            self._values["suppression_reasons"] = suppression_reasons
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def configuration_set_name(self) -> typing.Optional[builtins.str]:
        '''A name for the configuration set.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("configuration_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def custom_tracking_redirect_domain(self) -> typing.Optional[builtins.str]:
        '''The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain.

        :default: - use the default awstrack.me domain
        '''
        result = self._values.get("custom_tracking_redirect_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def dedicated_ip_pool(self) -> typing.Optional["IDedicatedIpPool"]:
        '''The dedicated IP pool to associate with the configuration set.

        :default: - do not use a dedicated IP pool
        '''
        result = self._values.get("dedicated_ip_pool")
        return typing.cast(typing.Optional["IDedicatedIpPool"], result)

    @builtins.property
    def reputation_metrics(self) -> typing.Optional[builtins.bool]:
        '''Whether to publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch.

        :default: false
        '''
        result = self._values.get("reputation_metrics")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def sending_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether email sending is enabled.

        :default: true
        '''
        result = self._values.get("sending_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def suppression_reasons(self) -> typing.Optional["SuppressionReasons"]:
        '''The reasons for which recipient email addresses should be automatically added to your account's suppression list.

        :default: - use account level settings
        '''
        result = self._values.get("suppression_reasons")
        return typing.cast(typing.Optional["SuppressionReasons"], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["ConfigurationSetTlsPolicy"]:
        '''Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS).

        :default: ConfigurationSetTlsPolicy.OPTIONAL
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["ConfigurationSetTlsPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ConfigurationSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetTlsPolicy")
class ConfigurationSetTlsPolicy(enum.Enum):
    '''TLS policy for a configuration set.

    :exampleMetadata: infused

    Example::

        # my_pool: ses.IDedicatedIpPool
        
        
        ses.ConfigurationSet(self, "ConfigurationSet",
            custom_tracking_redirect_domain="track.cdk.dev",
            suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
            tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
            dedicated_ip_pool=my_pool
        )
    '''

    REQUIRE = "REQUIRE"
    '''Messages are only delivered if a TLS connection can be established.'''
    OPTIONAL = "OPTIONAL"
    '''Messages can be delivered in plain text if a TLS connection can't be established.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DedicatedIpPoolProps",
    jsii_struct_bases=[],
    name_mapping={"dedicated_ip_pool_name": "dedicatedIpPoolName"},
)
class DedicatedIpPoolProps:
    def __init__(
        self,
        *,
        dedicated_ip_pool_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for a dedicated IP pool.

        :param dedicated_ip_pool_name: A name for the dedicated IP pool. Default: - a CloudFormation generated name

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            dedicated_ip_pool_props = ses.DedicatedIpPoolProps(
                dedicated_ip_pool_name="dedicatedIpPoolName"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cbbd68e1fe68b915968886e4089439bf017848bb3c0f82036ac33e6a6de46dd0)
            check_type(argname="argument dedicated_ip_pool_name", value=dedicated_ip_pool_name, expected_type=type_hints["dedicated_ip_pool_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if dedicated_ip_pool_name is not None:
            self._values["dedicated_ip_pool_name"] = dedicated_ip_pool_name

    @builtins.property
    def dedicated_ip_pool_name(self) -> typing.Optional[builtins.str]:
        '''A name for the dedicated IP pool.

        :default: - a CloudFormation generated name
        '''
        result = self._values.get("dedicated_ip_pool_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DedicatedIpPoolProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DkimIdentity(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_ses.DkimIdentity",
):
    '''The identity to use for DKIM.

    :exampleMetadata: infused

    Example::

        # my_hosted_zone: route53.IPublicHostedZone
        
        
        ses.EmailIdentity(self, "Identity",
            identity=ses.Identity.public_hosted_zone(my_hosted_zone),
            dkim_identity=ses.DkimIdentity.byo_dkim(
                private_key=SecretValue.secrets_manager("dkim-private-key"),
                public_key="...base64-encoded-public-key...",
                selector="selector"
            )
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="byoDkim")
    @builtins.classmethod
    def byo_dkim(
        cls,
        *,
        private_key: _SecretValue_3dd0ddae,
        selector: builtins.str,
        public_key: typing.Optional[builtins.str] = None,
    ) -> "DkimIdentity":
        '''Bring Your Own DKIM.

        :param private_key: The private key that's used to generate a DKIM signature.
        :param selector: A string that's used to identify a public key in the DNS configuration for a domain.
        :param public_key: The public key. If specified, a TXT record with the public key is created. Default: - the validation TXT record with the public key is not created

        :see: https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-bring-your-own.html
        '''
        options = ByoDkimOptions(
            private_key=private_key, selector=selector, public_key=public_key
        )

        return typing.cast("DkimIdentity", jsii.sinvoke(cls, "byoDkim", [options]))

    @jsii.member(jsii_name="easyDkim")
    @builtins.classmethod
    def easy_dkim(
        cls,
        signing_key_length: typing.Optional["EasyDkimSigningKeyLength"] = None,
    ) -> "DkimIdentity":
        '''Easy DKIM.

        :param signing_key_length: The length of the signing key. This can be changed at most once per day.

        :see: https://docs.aws.amazon.com/ses/latest/dg/send-email-authentication-dkim-easy.html
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__994835eb6fc73d3a1816da5c4409a2dda8bf60416433ec82d3c77e1b7f8801bc)
            check_type(argname="argument signing_key_length", value=signing_key_length, expected_type=type_hints["signing_key_length"])
        return typing.cast("DkimIdentity", jsii.sinvoke(cls, "easyDkim", [signing_key_length]))

    @jsii.member(jsii_name="bind")
    @abc.abstractmethod
    def bind(
        self,
        email_identity: "EmailIdentity",
        hosted_zone: typing.Optional[_IPublicHostedZone_9b6e7da4] = None,
    ) -> typing.Optional["DkimIdentityConfig"]:
        '''Binds this DKIM identity to the email identity.

        :param email_identity: -
        :param hosted_zone: -
        '''
        ...


class _DkimIdentityProxy(DkimIdentity):
    @jsii.member(jsii_name="bind")
    def bind(
        self,
        email_identity: "EmailIdentity",
        hosted_zone: typing.Optional[_IPublicHostedZone_9b6e7da4] = None,
    ) -> typing.Optional["DkimIdentityConfig"]:
        '''Binds this DKIM identity to the email identity.

        :param email_identity: -
        :param hosted_zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9b2a9a4d5a04b9eb8c5081160726f10e62e8072c32851a0ec47dc874a5ecd6db)
            check_type(argname="argument email_identity", value=email_identity, expected_type=type_hints["email_identity"])
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
        return typing.cast(typing.Optional["DkimIdentityConfig"], jsii.invoke(self, "bind", [email_identity, hosted_zone]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, DkimIdentity).__jsii_proxy_class__ = lambda : _DkimIdentityProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DkimIdentityConfig",
    jsii_struct_bases=[],
    name_mapping={
        "domain_signing_private_key": "domainSigningPrivateKey",
        "domain_signing_selector": "domainSigningSelector",
        "next_signing_key_length": "nextSigningKeyLength",
    },
)
class DkimIdentityConfig:
    def __init__(
        self,
        *,
        domain_signing_private_key: typing.Optional[builtins.str] = None,
        domain_signing_selector: typing.Optional[builtins.str] = None,
        next_signing_key_length: typing.Optional["EasyDkimSigningKeyLength"] = None,
    ) -> None:
        '''Configuration for DKIM identity.

        :param domain_signing_private_key: A private key that's used to generate a DKIM signature. Default: - use Easy DKIM
        :param domain_signing_selector: A string that's used to identify a public key in the DNS configuration for a domain. Default: - use Easy DKIM
        :param next_signing_key_length: The key length of the future DKIM key pair to be generated. This can be changed at most once per day. Default: EasyDkimSigningKeyLength.RSA_2048_BIT

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            dkim_identity_config = ses.DkimIdentityConfig(
                domain_signing_private_key="domainSigningPrivateKey",
                domain_signing_selector="domainSigningSelector",
                next_signing_key_length=ses.EasyDkimSigningKeyLength.RSA_1024_BIT
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a12b15597f5468ef7ba7f763da92c48506401bbeba665c431a78482dcb24b3bb)
            check_type(argname="argument domain_signing_private_key", value=domain_signing_private_key, expected_type=type_hints["domain_signing_private_key"])
            check_type(argname="argument domain_signing_selector", value=domain_signing_selector, expected_type=type_hints["domain_signing_selector"])
            check_type(argname="argument next_signing_key_length", value=next_signing_key_length, expected_type=type_hints["next_signing_key_length"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if domain_signing_private_key is not None:
            self._values["domain_signing_private_key"] = domain_signing_private_key
        if domain_signing_selector is not None:
            self._values["domain_signing_selector"] = domain_signing_selector
        if next_signing_key_length is not None:
            self._values["next_signing_key_length"] = next_signing_key_length

    @builtins.property
    def domain_signing_private_key(self) -> typing.Optional[builtins.str]:
        '''A private key that's used to generate a DKIM signature.

        :default: - use Easy DKIM
        '''
        result = self._values.get("domain_signing_private_key")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def domain_signing_selector(self) -> typing.Optional[builtins.str]:
        '''A string that's used to identify a public key in the DNS configuration for a domain.

        :default: - use Easy DKIM
        '''
        result = self._values.get("domain_signing_selector")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def next_signing_key_length(self) -> typing.Optional["EasyDkimSigningKeyLength"]:
        '''The key length of the future DKIM key pair to be generated.

        This can be changed
        at most once per day.

        :default: EasyDkimSigningKeyLength.RSA_2048_BIT
        '''
        result = self._values.get("next_signing_key_length")
        return typing.cast(typing.Optional["EasyDkimSigningKeyLength"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DkimIdentityConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DkimRecord",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "value": "value"},
)
class DkimRecord:
    def __init__(self, *, name: builtins.str, value: builtins.str) -> None:
        '''A DKIM record.

        :param name: The name of the record.
        :param value: The value of the record.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            dkim_record = ses.DkimRecord(
                name="name",
                value="value"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8446e7095e52fceeeac69f7c1807060cf3465e09ec2b3af84028d1df922471e6)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "value": value,
        }

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the record.'''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def value(self) -> builtins.str:
        '''The value of the record.'''
        result = self._values.get("value")
        assert result is not None, "Required property 'value' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DkimRecord(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class DropSpamReceiptRule(
    _constructs_77d1e7e8.Construct,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.DropSpamReceiptRule",
):
    '''A rule added at the top of the rule set to drop spam/virus.

    :see: https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-action-lambda-example-functions.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        # receipt_rule: ses.ReceiptRule
        # receipt_rule_action: ses.IReceiptRuleAction
        # receipt_rule_set: ses.ReceiptRuleSet
        
        drop_spam_receipt_rule = ses.DropSpamReceiptRule(self, "MyDropSpamReceiptRule",
            rule_set=receipt_rule_set,
        
            # the properties below are optional
            actions=[receipt_rule_action],
            after=receipt_rule,
            enabled=False,
            receipt_rule_name="receiptRuleName",
            recipients=["recipients"],
            scan_enabled=False,
            tls_policy=ses.TlsPolicy.OPTIONAL
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule_set: "IReceiptRuleSet",
        actions: typing.Optional[typing.Sequence["IReceiptRuleAction"]] = None,
        after: typing.Optional["IReceiptRule"] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__620f8d2305a209eeebb24bd2358ba969bde0f80c50a46c3fa91e56d814fa6152)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DropSpamReceiptRuleProps(
            rule_set=rule_set,
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @builtins.property
    @jsii.member(jsii_name="rule")
    def rule(self) -> "ReceiptRule":
        return typing.cast("ReceiptRule", jsii.get(self, "rule"))


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.EasyDkimSigningKeyLength")
class EasyDkimSigningKeyLength(enum.Enum):
    '''The signing key length for Easy DKIM.'''

    RSA_1024_BIT = "RSA_1024_BIT"
    '''RSA 1024-bit.'''
    RSA_2048_BIT = "RSA_2048_BIT"
    '''RSA 2048-bit.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.EmailIdentityProps",
    jsii_struct_bases=[],
    name_mapping={
        "identity": "identity",
        "configuration_set": "configurationSet",
        "dkim_identity": "dkimIdentity",
        "dkim_signing": "dkimSigning",
        "feedback_forwarding": "feedbackForwarding",
        "mail_from_behavior_on_mx_failure": "mailFromBehaviorOnMxFailure",
        "mail_from_domain": "mailFromDomain",
    },
)
class EmailIdentityProps:
    def __init__(
        self,
        *,
        identity: "Identity",
        configuration_set: typing.Optional["IConfigurationSet"] = None,
        dkim_identity: typing.Optional[DkimIdentity] = None,
        dkim_signing: typing.Optional[builtins.bool] = None,
        feedback_forwarding: typing.Optional[builtins.bool] = None,
        mail_from_behavior_on_mx_failure: typing.Optional["MailFromBehaviorOnMxFailure"] = None,
        mail_from_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for an email identity.

        :param identity: The email address or domain to verify.
        :param configuration_set: The configuration set to associate with the email identity. Default: - do not use a specific configuration set
        :param dkim_identity: The type of DKIM identity to use. Default: - Easy DKIM with a key length of 2048-bit
        :param dkim_signing: Whether the messages that are sent from the identity are signed using DKIM. Default: true
        :param feedback_forwarding: Whether to receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the ``Return-Path`` header of the original email. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled). Default: true
        :param mail_from_behavior_on_mx_failure: The action to take if the required MX record for the MAIL FROM domain isn't found when you send an email. Default: MailFromBehaviorOnMxFailure.USE_DEFAULT_VALUE
        :param mail_from_domain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria: - It has to be a subdomain of the verified identity - It can't be used to receive email - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails Default: - use amazonses.com

        :exampleMetadata: infused

        Example::

            # my_hosted_zone: route53.IPublicHostedZone
            
            
            identity = ses.EmailIdentity(self, "Identity",
                identity=ses.Identity.public_hosted_zone(my_hosted_zone),
                mail_from_domain="mail.cdk.dev"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53e1ee2f3b565a95ed952bf4ad2ae80cb7388ac4bd51d6eab5219f8a733ca030)
            check_type(argname="argument identity", value=identity, expected_type=type_hints["identity"])
            check_type(argname="argument configuration_set", value=configuration_set, expected_type=type_hints["configuration_set"])
            check_type(argname="argument dkim_identity", value=dkim_identity, expected_type=type_hints["dkim_identity"])
            check_type(argname="argument dkim_signing", value=dkim_signing, expected_type=type_hints["dkim_signing"])
            check_type(argname="argument feedback_forwarding", value=feedback_forwarding, expected_type=type_hints["feedback_forwarding"])
            check_type(argname="argument mail_from_behavior_on_mx_failure", value=mail_from_behavior_on_mx_failure, expected_type=type_hints["mail_from_behavior_on_mx_failure"])
            check_type(argname="argument mail_from_domain", value=mail_from_domain, expected_type=type_hints["mail_from_domain"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "identity": identity,
        }
        if configuration_set is not None:
            self._values["configuration_set"] = configuration_set
        if dkim_identity is not None:
            self._values["dkim_identity"] = dkim_identity
        if dkim_signing is not None:
            self._values["dkim_signing"] = dkim_signing
        if feedback_forwarding is not None:
            self._values["feedback_forwarding"] = feedback_forwarding
        if mail_from_behavior_on_mx_failure is not None:
            self._values["mail_from_behavior_on_mx_failure"] = mail_from_behavior_on_mx_failure
        if mail_from_domain is not None:
            self._values["mail_from_domain"] = mail_from_domain

    @builtins.property
    def identity(self) -> "Identity":
        '''The email address or domain to verify.'''
        result = self._values.get("identity")
        assert result is not None, "Required property 'identity' is missing"
        return typing.cast("Identity", result)

    @builtins.property
    def configuration_set(self) -> typing.Optional["IConfigurationSet"]:
        '''The configuration set to associate with the email identity.

        :default: - do not use a specific configuration set
        '''
        result = self._values.get("configuration_set")
        return typing.cast(typing.Optional["IConfigurationSet"], result)

    @builtins.property
    def dkim_identity(self) -> typing.Optional[DkimIdentity]:
        '''The type of DKIM identity to use.

        :default: - Easy DKIM with a key length of 2048-bit
        '''
        result = self._values.get("dkim_identity")
        return typing.cast(typing.Optional[DkimIdentity], result)

    @builtins.property
    def dkim_signing(self) -> typing.Optional[builtins.bool]:
        '''Whether the messages that are sent from the identity are signed using DKIM.

        :default: true
        '''
        result = self._values.get("dkim_signing")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def feedback_forwarding(self) -> typing.Optional[builtins.bool]:
        '''Whether to receive email notifications when bounce or complaint events occur.

        These notifications are sent to the address that you specified in the ``Return-Path``
        header of the original email.

        You're required to have a method of tracking bounces and complaints. If you haven't set
        up another mechanism for receiving bounce or complaint notifications (for example, by
        setting up an event destination), you receive an email notification when these events
        occur (even if this setting is disabled).

        :default: true
        '''
        result = self._values.get("feedback_forwarding")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def mail_from_behavior_on_mx_failure(
        self,
    ) -> typing.Optional["MailFromBehaviorOnMxFailure"]:
        '''The action to take if the required MX record for the MAIL FROM domain isn't found when you send an email.

        :default: MailFromBehaviorOnMxFailure.USE_DEFAULT_VALUE
        '''
        result = self._values.get("mail_from_behavior_on_mx_failure")
        return typing.cast(typing.Optional["MailFromBehaviorOnMxFailure"], result)

    @builtins.property
    def mail_from_domain(self) -> typing.Optional[builtins.str]:
        '''The custom MAIL FROM domain that you want the verified identity to use.

        The MAIL FROM domain
        must meet the following criteria:

        - It has to be a subdomain of the verified identity
        - It can't be used to receive email
        - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback
          forwarding emails

        :default: - use amazonses.com
        '''
        result = self._values.get("mail_from_domain")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "EmailIdentityProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.EmailSendingEvent")
class EmailSendingEvent(enum.Enum):
    '''Email sending event.'''

    SEND = "SEND"
    '''The send request was successful and SES will attempt to deliver the message to the recipient's mail server.

    (If account-level or global suppression is
    being used, SES will still count it as a send, but delivery is suppressed.)
    '''
    REJECT = "REJECT"
    '''SES accepted the email, but determined that it contained a virus and didn’t attempt to deliver it to the recipient’s mail server.'''
    BOUNCE = "BOUNCE"
    '''(Hard bounce) The recipient's mail server permanently rejected the email.

    (Soft bounces are only included when SES fails to deliver the email after
    retrying for a period of time.)
    '''
    COMPLAINT = "COMPLAINT"
    '''The email was successfully delivered to the recipient’s mail server, but the recipient marked it as spam.'''
    DELIVERY = "DELIVERY"
    '''SES successfully delivered the email to the recipient's mail server.'''
    OPEN = "OPEN"
    '''The recipient received the message and opened it in their email client.'''
    CLICK = "CLICK"
    '''The recipient clicked one or more links in the email.'''
    RENDERING_FAILURE = "RENDERING_FAILURE"
    '''The email wasn't sent because of a template rendering issue.

    This event type
    can occur when template data is missing, or when there is a mismatch between
    template parameters and data. (This event type only occurs when you send email
    using the ``SendTemplatedEmail`` or ``SendBulkTemplatedEmail`` API operations.)
    '''
    DELIVERY_DELAY = "DELIVERY_DELAY"
    '''The email couldn't be delivered to the recipient’s mail server because a temporary issue occurred.

    Delivery delays can occur, for example, when the recipient's inbox
    is full, or when the receiving email server experiences a transient issue.
    '''
    SUBSCRIPTION = "SUBSCRIPTION"
    '''The email was successfully delivered, but the recipient updated their subscription preferences by clicking on an unsubscribe link as part of your subscription management.'''


class EventDestination(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_ses.EventDestination",
):
    '''An event destination.

    :exampleMetadata: infused

    Example::

        # my_configuration_set: ses.ConfigurationSet
        # my_topic: sns.Topic
        
        
        my_configuration_set.add_event_destination("ToSns",
            destination=ses.EventDestination.sns_topic(my_topic)
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="cloudWatchDimensions")
    @builtins.classmethod
    def cloud_watch_dimensions(
        cls,
        dimensions: typing.Sequence[typing.Union[CloudWatchDimension, typing.Dict[builtins.str, typing.Any]]],
    ) -> "EventDestination":
        '''Use CloudWatch dimensions as event destination.

        :param dimensions: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__48f9cce8b82649ed9874f37f0ed571721b324063ca98764a07bb10a451e9fe92)
            check_type(argname="argument dimensions", value=dimensions, expected_type=type_hints["dimensions"])
        return typing.cast("EventDestination", jsii.sinvoke(cls, "cloudWatchDimensions", [dimensions]))

    @jsii.member(jsii_name="snsTopic")
    @builtins.classmethod
    def sns_topic(cls, topic: _ITopic_9eca4852) -> "EventDestination":
        '''Use a SNS topic as event destination.

        :param topic: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70dbe9528b7fbaa2cbed5b1def55a8c3126fbfed3ee256b878bbb907e4585c9c)
            check_type(argname="argument topic", value=topic, expected_type=type_hints["topic"])
        return typing.cast("EventDestination", jsii.sinvoke(cls, "snsTopic", [topic]))

    @builtins.property
    @jsii.member(jsii_name="dimensions")
    @abc.abstractmethod
    def dimensions(self) -> typing.Optional[typing.List[CloudWatchDimension]]:
        '''A list of CloudWatch dimensions upon which to categorize your emails.

        :default: - do not send events to CloudWatch
        '''
        ...

    @builtins.property
    @jsii.member(jsii_name="topic")
    @abc.abstractmethod
    def topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''A SNS topic to use as event destination.

        :default: - do not send events to a SNS topic
        '''
        ...


class _EventDestinationProxy(EventDestination):
    @builtins.property
    @jsii.member(jsii_name="dimensions")
    def dimensions(self) -> typing.Optional[typing.List[CloudWatchDimension]]:
        '''A list of CloudWatch dimensions upon which to categorize your emails.

        :default: - do not send events to CloudWatch
        '''
        return typing.cast(typing.Optional[typing.List[CloudWatchDimension]], jsii.get(self, "dimensions"))

    @builtins.property
    @jsii.member(jsii_name="topic")
    def topic(self) -> typing.Optional[_ITopic_9eca4852]:
        '''A SNS topic to use as event destination.

        :default: - do not send events to a SNS topic
        '''
        return typing.cast(typing.Optional[_ITopic_9eca4852], jsii.get(self, "topic"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, EventDestination).__jsii_proxy_class__ = lambda : _EventDestinationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IConfigurationSet")
class IConfigurationSet(_IResource_c80c4260, typing_extensions.Protocol):
    '''A configuration set.'''

    @builtins.property
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set.

        :attribute: true
        '''
        ...


class _IConfigurationSetProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A configuration set.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IConfigurationSet"

    @builtins.property
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSet).__jsii_proxy_class__ = lambda : _IConfigurationSetProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IConfigurationSetEventDestination")
class IConfigurationSetEventDestination(
    _IResource_c80c4260,
    typing_extensions.Protocol,
):
    '''A configuration set event destination.'''

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationId")
    def configuration_set_event_destination_id(self) -> builtins.str:
        '''The ID of the configuration set event destination.

        :attribute: true
        '''
        ...


class _IConfigurationSetEventDestinationProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A configuration set event destination.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IConfigurationSetEventDestination"

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationId")
    def configuration_set_event_destination_id(self) -> builtins.str:
        '''The ID of the configuration set event destination.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetEventDestinationId"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IConfigurationSetEventDestination).__jsii_proxy_class__ = lambda : _IConfigurationSetEventDestinationProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IDedicatedIpPool")
class IDedicatedIpPool(_IResource_c80c4260, typing_extensions.Protocol):
    '''A dedicated IP pool.'''

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolName")
    def dedicated_ip_pool_name(self) -> builtins.str:
        '''The name of the dedicated IP pool.

        :attribute: true
        '''
        ...


class _IDedicatedIpPoolProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A dedicated IP pool.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IDedicatedIpPool"

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolName")
    def dedicated_ip_pool_name(self) -> builtins.str:
        '''The name of the dedicated IP pool.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dedicatedIpPoolName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IDedicatedIpPool).__jsii_proxy_class__ = lambda : _IDedicatedIpPoolProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IEmailIdentity")
class IEmailIdentity(_IResource_c80c4260, typing_extensions.Protocol):
    '''An email identity.'''

    @builtins.property
    @jsii.member(jsii_name="emailIdentityName")
    def email_identity_name(self) -> builtins.str:
        '''The name of the email identity.

        :attribute: true
        '''
        ...


class _IEmailIdentityProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''An email identity.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IEmailIdentity"

    @builtins.property
    @jsii.member(jsii_name="emailIdentityName")
    def email_identity_name(self) -> builtins.str:
        '''The name of the email identity.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "emailIdentityName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IEmailIdentity).__jsii_proxy_class__ = lambda : _IEmailIdentityProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IReceiptRule")
class IReceiptRule(_IResource_c80c4260, typing_extensions.Protocol):
    '''A receipt rule.'''

    @builtins.property
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.

        :attribute: true
        '''
        ...


class _IReceiptRuleProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A receipt rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IReceiptRule"

    @builtins.property
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRule).__jsii_proxy_class__ = lambda : _IReceiptRuleProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IReceiptRuleAction")
class IReceiptRuleAction(typing_extensions.Protocol):
    '''An abstract action for a receipt rule.'''

    @jsii.member(jsii_name="bind")
    def bind(self, receipt_rule: IReceiptRule) -> "ReceiptRuleActionConfig":
        '''Returns the receipt rule action specification.

        :param receipt_rule: -
        '''
        ...


class _IReceiptRuleActionProxy:
    '''An abstract action for a receipt rule.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IReceiptRuleAction"

    @jsii.member(jsii_name="bind")
    def bind(self, receipt_rule: IReceiptRule) -> "ReceiptRuleActionConfig":
        '''Returns the receipt rule action specification.

        :param receipt_rule: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c0b08f3a2fda3c68a4ad951604e55664aeae1537b8b8eb996f95b6feedcf9b5)
            check_type(argname="argument receipt_rule", value=receipt_rule, expected_type=type_hints["receipt_rule"])
        return typing.cast("ReceiptRuleActionConfig", jsii.invoke(self, "bind", [receipt_rule]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleAction).__jsii_proxy_class__ = lambda : _IReceiptRuleActionProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IReceiptRuleSet")
class IReceiptRuleSet(_IResource_c80c4260, typing_extensions.Protocol):
    '''A receipt rule set.'''

    @builtins.property
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.

        :attribute: true
        '''
        ...

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> "ReceiptRule":
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        ...


class _IReceiptRuleSetProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''A receipt rule set.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IReceiptRuleSet"

    @builtins.property
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleSetName"))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> "ReceiptRule":
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__122fb3fdbd3a8f500e0f61c3d2533bd2f3c984f5adc4220663c7c60a5e6cad15)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ReceiptRuleOptions(
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        return typing.cast("ReceiptRule", jsii.invoke(self, "addRule", [id, options]))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IReceiptRuleSet).__jsii_proxy_class__ = lambda : _IReceiptRuleSetProxy


@jsii.interface(jsii_type="aws-cdk-lib.aws_ses.IVdmAttributes")
class IVdmAttributes(_IResource_c80c4260, typing_extensions.Protocol):
    '''Virtual Deliverablity Manager (VDM) attributes.'''

    @builtins.property
    @jsii.member(jsii_name="vdmAttributesName")
    def vdm_attributes_name(self) -> builtins.str:
        '''The name of the resource behind the Virtual Deliverablity Manager attributes.

        :attribute: true
        '''
        ...


class _IVdmAttributesProxy(
    jsii.proxy_for(_IResource_c80c4260), # type: ignore[misc]
):
    '''Virtual Deliverablity Manager (VDM) attributes.'''

    __jsii_type__: typing.ClassVar[str] = "aws-cdk-lib.aws_ses.IVdmAttributes"

    @builtins.property
    @jsii.member(jsii_name="vdmAttributesName")
    def vdm_attributes_name(self) -> builtins.str:
        '''The name of the resource behind the Virtual Deliverablity Manager attributes.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "vdmAttributesName"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the interface
typing.cast(typing.Any, IVdmAttributes).__jsii_proxy_class__ = lambda : _IVdmAttributesProxy


class Identity(
    metaclass=jsii.JSIIAbstractClass,
    jsii_type="aws-cdk-lib.aws_ses.Identity",
):
    '''Identity.

    :exampleMetadata: infused

    Example::

        # my_hosted_zone: route53.IPublicHostedZone
        
        
        identity = ses.EmailIdentity(self, "Identity",
            identity=ses.Identity.public_hosted_zone(my_hosted_zone),
            mail_from_domain="mail.cdk.dev"
        )
    '''

    def __init__(self) -> None:
        jsii.create(self.__class__, self, [])

    @jsii.member(jsii_name="domain")
    @builtins.classmethod
    def domain(cls, domain: builtins.str) -> "Identity":
        '''Verify a domain name.

        DKIM records will have to be added manually to complete the verification
        process

        :param domain: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__694ee3f881b596f644bf78eec0110a1de21fa0968b51aac198d16dc4300152a5)
            check_type(argname="argument domain", value=domain, expected_type=type_hints["domain"])
        return typing.cast("Identity", jsii.sinvoke(cls, "domain", [domain]))

    @jsii.member(jsii_name="email")
    @builtins.classmethod
    def email(cls, email: builtins.str) -> "Identity":
        '''Verify an email address.

        To complete the verification process look for an email from
        no-reply-aws@amazon.com, open it and click the link.

        :param email: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c4cd96b179380c844d33e1c8146fdcd73dda4442d8f15d6ec14f0d13964631f6)
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
        return typing.cast("Identity", jsii.sinvoke(cls, "email", [email]))

    @jsii.member(jsii_name="publicHostedZone")
    @builtins.classmethod
    def public_hosted_zone(cls, hosted_zone: _IPublicHostedZone_9b6e7da4) -> "Identity":
        '''Verify a public hosted zone.

        DKIM and MAIL FROM records will be added automatically to the hosted
        zone

        :param hosted_zone: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0eb32adc3b9ec102b9a239f5273e26b9dc183e06c2e841a07bb8e8865f65d776)
            check_type(argname="argument hosted_zone", value=hosted_zone, expected_type=type_hints["hosted_zone"])
        return typing.cast("Identity", jsii.sinvoke(cls, "publicHostedZone", [hosted_zone]))

    @builtins.property
    @jsii.member(jsii_name="value")
    @abc.abstractmethod
    def value(self) -> builtins.str:
        '''The value of the identity.'''
        ...

    @builtins.property
    @jsii.member(jsii_name="hostedZone")
    @abc.abstractmethod
    def hosted_zone(self) -> typing.Optional[_IPublicHostedZone_9b6e7da4]:
        '''The hosted zone associated with this identity.

        :default: - no hosted zone is associated and no records are created
        '''
        ...


class _IdentityProxy(Identity):
    @builtins.property
    @jsii.member(jsii_name="value")
    def value(self) -> builtins.str:
        '''The value of the identity.'''
        return typing.cast(builtins.str, jsii.get(self, "value"))

    @builtins.property
    @jsii.member(jsii_name="hostedZone")
    def hosted_zone(self) -> typing.Optional[_IPublicHostedZone_9b6e7da4]:
        '''The hosted zone associated with this identity.

        :default: - no hosted zone is associated and no records are created
        '''
        return typing.cast(typing.Optional[_IPublicHostedZone_9b6e7da4], jsii.get(self, "hostedZone"))

# Adding a "__jsii_proxy_class__(): typing.Type" function to the abstract class
typing.cast(typing.Any, Identity).__jsii_proxy_class__ = lambda : _IdentityProxy


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.LambdaActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "function_arn": "functionArn",
        "invocation_type": "invocationType",
        "topic_arn": "topicArn",
    },
)
class LambdaActionConfig:
    def __init__(
        self,
        *,
        function_arn: builtins.str,
        invocation_type: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''LambdaAction configuration.

        :param function_arn: The Amazon Resource Name (ARN) of the AWS Lambda function.
        :param invocation_type: The invocation type of the AWS Lambda function. Default: 'Event'
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            lambda_action_config = ses.LambdaActionConfig(
                function_arn="functionArn",
            
                # the properties below are optional
                invocation_type="invocationType",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2c5bf3251571f8d55618125a7248ae05fc227e5f493642b4ff5f700dfa8105fa)
            check_type(argname="argument function_arn", value=function_arn, expected_type=type_hints["function_arn"])
            check_type(argname="argument invocation_type", value=invocation_type, expected_type=type_hints["invocation_type"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "function_arn": function_arn,
        }
        if invocation_type is not None:
            self._values["invocation_type"] = invocation_type
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def function_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the AWS Lambda function.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-functionarn
        '''
        result = self._values.get("function_arn")
        assert result is not None, "Required property 'function_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def invocation_type(self) -> typing.Optional[builtins.str]:
        '''The invocation type of the AWS Lambda function.

        :default: 'Event'

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-invocationtype
        '''
        result = self._values.get("invocation_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-lambdaaction.html#cfn-ses-receiptrule-lambdaaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "LambdaActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.MailFromBehaviorOnMxFailure")
class MailFromBehaviorOnMxFailure(enum.Enum):
    '''The action to take if the required MX record for the MAIL FROM domain isn't found.'''

    USE_DEFAULT_VALUE = "USE_DEFAULT_VALUE"
    '''The mail is sent using amazonses.com as the MAIL FROM domain.'''
    REJECT_MESSAGE = "REJECT_MESSAGE"
    '''The Amazon SES API v2 returns a ``MailFromDomainNotVerified`` error and doesn't attempt to deliver the email.'''


class ReceiptFilter(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ReceiptFilter",
):
    '''A receipt filter.

    When instantiated without props, it creates a
    block all receipt filter.

    :exampleMetadata: infused

    Example::

        ses.ReceiptFilter(self, "Filter",
            ip="1.2.3.4/16"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        ip: typing.Optional[builtins.str] = None,
        policy: typing.Optional["ReceiptFilterPolicy"] = None,
        receipt_filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param ip: The ip address or range to filter. Default: 0.0.0.0/0
        :param policy: The policy for the filter. Default: Block
        :param receipt_filter_name: The name for the receipt filter. Default: a CloudFormation generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__be1bedd2ed98e8b9a5eafff592b3be89e41244d9b42293f0924022a7f27a537f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ReceiptFilterProps(
            ip=ip, policy=policy, receipt_filter_name=receipt_filter_name
        )

        jsii.create(self.__class__, self, [scope, id, props])


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.ReceiptFilterPolicy")
class ReceiptFilterPolicy(enum.Enum):
    '''The policy for the receipt filter.'''

    ALLOW = "ALLOW"
    '''Allow the ip address or range.'''
    BLOCK = "BLOCK"
    '''Block the ip address or range.'''


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "ip": "ip",
        "policy": "policy",
        "receipt_filter_name": "receiptFilterName",
    },
)
class ReceiptFilterProps:
    def __init__(
        self,
        *,
        ip: typing.Optional[builtins.str] = None,
        policy: typing.Optional[ReceiptFilterPolicy] = None,
        receipt_filter_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Construction properties for a ReceiptFilter.

        :param ip: The ip address or range to filter. Default: 0.0.0.0/0
        :param policy: The policy for the filter. Default: Block
        :param receipt_filter_name: The name for the receipt filter. Default: a CloudFormation generated name

        :exampleMetadata: infused

        Example::

            ses.ReceiptFilter(self, "Filter",
                ip="1.2.3.4/16"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__14330b86b5842b62205be575cd211ebe283567b16984be282e6ee5085d7777ce)
            check_type(argname="argument ip", value=ip, expected_type=type_hints["ip"])
            check_type(argname="argument policy", value=policy, expected_type=type_hints["policy"])
            check_type(argname="argument receipt_filter_name", value=receipt_filter_name, expected_type=type_hints["receipt_filter_name"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if ip is not None:
            self._values["ip"] = ip
        if policy is not None:
            self._values["policy"] = policy
        if receipt_filter_name is not None:
            self._values["receipt_filter_name"] = receipt_filter_name

    @builtins.property
    def ip(self) -> typing.Optional[builtins.str]:
        '''The ip address or range to filter.

        :default: 0.0.0.0/0
        '''
        result = self._values.get("ip")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def policy(self) -> typing.Optional[ReceiptFilterPolicy]:
        '''The policy for the filter.

        :default: Block
        '''
        result = self._values.get("policy")
        return typing.cast(typing.Optional[ReceiptFilterPolicy], result)

    @builtins.property
    def receipt_filter_name(self) -> typing.Optional[builtins.str]:
        '''The name for the receipt filter.

        :default: a CloudFormation generated name
        '''
        result = self._values.get("receipt_filter_name")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IReceiptRule)
class ReceiptRule(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRule",
):
    '''A new receipt rule.

    :exampleMetadata: infused

    Example::

        rule_set = ses.ReceiptRuleSet(self, "RuleSet")
        
        aws_rule = rule_set.add_rule("Aws",
            recipients=["aws.com"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        rule_set: IReceiptRuleSet,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param rule_set: The name of the rule set that the receipt rule will be added to.
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a6538ae0354b52c95d3f59e885aa37e670088031cd04d3731f535129e11231d3)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ReceiptRuleProps(
            rule_set=rule_set,
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromReceiptRuleName")
    @builtins.classmethod
    def from_receipt_rule_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        receipt_rule_name: builtins.str,
    ) -> IReceiptRule:
        '''
        :param scope: -
        :param id: -
        :param receipt_rule_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a2938a672425842bfae972477b62457f138b21842405c6d5cb21988892d92c7c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
        return typing.cast(IReceiptRule, jsii.sinvoke(cls, "fromReceiptRuleName", [scope, id, receipt_rule_name]))

    @jsii.member(jsii_name="addAction")
    def add_action(self, action: IReceiptRuleAction) -> None:
        '''Adds an action to this receipt rule.

        :param action: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e53269c4ea365e8ad5ea79b458ec9a4cd161a16b84e0de7f577a755251624a6b)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
        return typing.cast(None, jsii.invoke(self, "addAction", [action]))

    @builtins.property
    @jsii.member(jsii_name="receiptRuleName")
    def receipt_rule_name(self) -> builtins.str:
        '''The name of the receipt rule.'''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "add_header_action": "addHeaderAction",
        "bounce_action": "bounceAction",
        "lambda_action": "lambdaAction",
        "s3_action": "s3Action",
        "sns_action": "snsAction",
        "stop_action": "stopAction",
        "workmail_action": "workmailAction",
    },
)
class ReceiptRuleActionConfig:
    def __init__(
        self,
        *,
        add_header_action: typing.Optional[typing.Union[AddHeaderActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        bounce_action: typing.Optional[typing.Union[BounceActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        lambda_action: typing.Optional[typing.Union[LambdaActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
        s3_action: typing.Optional[typing.Union["S3ActionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        sns_action: typing.Optional[typing.Union["SNSActionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        stop_action: typing.Optional[typing.Union["StopActionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
        workmail_action: typing.Optional[typing.Union["WorkmailActionConfig", typing.Dict[builtins.str, typing.Any]]] = None,
    ) -> None:
        '''Properties for a receipt rule action.

        :param add_header_action: Adds a header to the received email.
        :param bounce_action: Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.
        :param lambda_action: Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.
        :param s3_action: Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.
        :param sns_action: Publishes the email content within a notification to Amazon SNS.
        :param stop_action: Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.
        :param workmail_action: Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            receipt_rule_action_config = ses.ReceiptRuleActionConfig(
                add_header_action=ses.AddHeaderActionConfig(
                    header_name="headerName",
                    header_value="headerValue"
                ),
                bounce_action=ses.BounceActionConfig(
                    message="message",
                    sender="sender",
                    smtp_reply_code="smtpReplyCode",
            
                    # the properties below are optional
                    status_code="statusCode",
                    topic_arn="topicArn"
                ),
                lambda_action=ses.LambdaActionConfig(
                    function_arn="functionArn",
            
                    # the properties below are optional
                    invocation_type="invocationType",
                    topic_arn="topicArn"
                ),
                s3_action=ses.S3ActionConfig(
                    bucket_name="bucketName",
            
                    # the properties below are optional
                    kms_key_arn="kmsKeyArn",
                    object_key_prefix="objectKeyPrefix",
                    topic_arn="topicArn"
                ),
                sns_action=ses.SNSActionConfig(
                    encoding="encoding",
                    topic_arn="topicArn"
                ),
                stop_action=ses.StopActionConfig(
                    scope="scope",
            
                    # the properties below are optional
                    topic_arn="topicArn"
                ),
                workmail_action=ses.WorkmailActionConfig(
                    organization_arn="organizationArn",
            
                    # the properties below are optional
                    topic_arn="topicArn"
                )
            )
        '''
        if isinstance(add_header_action, dict):
            add_header_action = AddHeaderActionConfig(**add_header_action)
        if isinstance(bounce_action, dict):
            bounce_action = BounceActionConfig(**bounce_action)
        if isinstance(lambda_action, dict):
            lambda_action = LambdaActionConfig(**lambda_action)
        if isinstance(s3_action, dict):
            s3_action = S3ActionConfig(**s3_action)
        if isinstance(sns_action, dict):
            sns_action = SNSActionConfig(**sns_action)
        if isinstance(stop_action, dict):
            stop_action = StopActionConfig(**stop_action)
        if isinstance(workmail_action, dict):
            workmail_action = WorkmailActionConfig(**workmail_action)
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e54c86543028b77ffed9d64cfee35a01463cb4a33a112de436e67beaf2b9608c)
            check_type(argname="argument add_header_action", value=add_header_action, expected_type=type_hints["add_header_action"])
            check_type(argname="argument bounce_action", value=bounce_action, expected_type=type_hints["bounce_action"])
            check_type(argname="argument lambda_action", value=lambda_action, expected_type=type_hints["lambda_action"])
            check_type(argname="argument s3_action", value=s3_action, expected_type=type_hints["s3_action"])
            check_type(argname="argument sns_action", value=sns_action, expected_type=type_hints["sns_action"])
            check_type(argname="argument stop_action", value=stop_action, expected_type=type_hints["stop_action"])
            check_type(argname="argument workmail_action", value=workmail_action, expected_type=type_hints["workmail_action"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if add_header_action is not None:
            self._values["add_header_action"] = add_header_action
        if bounce_action is not None:
            self._values["bounce_action"] = bounce_action
        if lambda_action is not None:
            self._values["lambda_action"] = lambda_action
        if s3_action is not None:
            self._values["s3_action"] = s3_action
        if sns_action is not None:
            self._values["sns_action"] = sns_action
        if stop_action is not None:
            self._values["stop_action"] = stop_action
        if workmail_action is not None:
            self._values["workmail_action"] = workmail_action

    @builtins.property
    def add_header_action(self) -> typing.Optional[AddHeaderActionConfig]:
        '''Adds a header to the received email.'''
        result = self._values.get("add_header_action")
        return typing.cast(typing.Optional[AddHeaderActionConfig], result)

    @builtins.property
    def bounce_action(self) -> typing.Optional[BounceActionConfig]:
        '''Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("bounce_action")
        return typing.cast(typing.Optional[BounceActionConfig], result)

    @builtins.property
    def lambda_action(self) -> typing.Optional[LambdaActionConfig]:
        '''Calls an AWS Lambda function, and optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("lambda_action")
        return typing.cast(typing.Optional[LambdaActionConfig], result)

    @builtins.property
    def s3_action(self) -> typing.Optional["S3ActionConfig"]:
        '''Saves the received message to an Amazon S3 bucket and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("s3_action")
        return typing.cast(typing.Optional["S3ActionConfig"], result)

    @builtins.property
    def sns_action(self) -> typing.Optional["SNSActionConfig"]:
        '''Publishes the email content within a notification to Amazon SNS.'''
        result = self._values.get("sns_action")
        return typing.cast(typing.Optional["SNSActionConfig"], result)

    @builtins.property
    def stop_action(self) -> typing.Optional["StopActionConfig"]:
        '''Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.'''
        result = self._values.get("stop_action")
        return typing.cast(typing.Optional["StopActionConfig"], result)

    @builtins.property
    def workmail_action(self) -> typing.Optional["WorkmailActionConfig"]:
        '''Calls Amazon WorkMail and, optionally, publishes a notification to Amazon SNS.'''
        result = self._values.get("workmail_action")
        return typing.cast(typing.Optional["WorkmailActionConfig"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleOptions",
    jsii_struct_bases=[],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
    },
)
class ReceiptRuleOptions:
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> None:
        '''Options to add a receipt rule to a receipt rule set.

        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.

        :exampleMetadata: infused

        Example::

            rule_set = ses.ReceiptRuleSet(self, "RuleSet")
            
            aws_rule = rule_set.add_rule("Aws",
                recipients=["aws.com"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__699a2986fda0df5077b1242432999d4d4b894d3e4dd15df070152fae49160eab)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["TlsPolicy"]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["TlsPolicy"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleProps",
    jsii_struct_bases=[ReceiptRuleOptions],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
        "rule_set": "ruleSet",
    },
)
class ReceiptRuleProps(ReceiptRuleOptions):
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
        rule_set: IReceiptRuleSet,
    ) -> None:
        '''Construction properties for a ReceiptRule.

        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        :param rule_set: The name of the rule set that the receipt rule will be added to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            # receipt_rule: ses.ReceiptRule
            # receipt_rule_action: ses.IReceiptRuleAction
            # receipt_rule_set: ses.ReceiptRuleSet
            
            receipt_rule_props = ses.ReceiptRuleProps(
                rule_set=receipt_rule_set,
            
                # the properties below are optional
                actions=[receipt_rule_action],
                after=receipt_rule,
                enabled=False,
                receipt_rule_name="receiptRuleName",
                recipients=["recipients"],
                scan_enabled=False,
                tls_policy=ses.TlsPolicy.OPTIONAL
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b6d8cc8ec3dfcf989e29bcbab39380e799bee428bb33c1fe79ab53debbc056b)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            check_type(argname="argument rule_set", value=rule_set, expected_type=type_hints["rule_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_set": rule_set,
        }
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional["TlsPolicy"]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional["TlsPolicy"], result)

    @builtins.property
    def rule_set(self) -> IReceiptRuleSet:
        '''The name of the rule set that the receipt rule will be added to.'''
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(IReceiptRuleSet, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IReceiptRuleSet)
class ReceiptRuleSet(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleSet",
):
    '''A new receipt rule set.

    :exampleMetadata: infused

    Example::

        rule_set = ses.ReceiptRuleSet(self, "RuleSet")
        
        aws_rule = rule_set.add_rule("Aws",
            recipients=["aws.com"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        drop_spam: typing.Optional[builtins.bool] = None,
        receipt_rule_set_name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[ReceiptRuleOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param drop_spam: Whether to add a first rule to stop processing messages that have at least one spam indicator. Default: false
        :param receipt_rule_set_name: The name for the receipt rule set. Default: - A CloudFormation generated name.
        :param rules: The list of rules to add to this rule set. Rules are added in the same order as they appear in the list. Default: - No rules are added to the rule set.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e30edd88543242272f6bbc66d4c1125786ce1237720d89b577e253760eb28e2a)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ReceiptRuleSetProps(
            drop_spam=drop_spam,
            receipt_rule_set_name=receipt_rule_set_name,
            rules=rules,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromReceiptRuleSetName")
    @builtins.classmethod
    def from_receipt_rule_set_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        receipt_rule_set_name: builtins.str,
    ) -> IReceiptRuleSet:
        '''Import an exported receipt rule set.

        :param scope: -
        :param id: -
        :param receipt_rule_set_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb544e652efede317fbc4b71b8f4c7e7ac6549e66fa70957106d0835bd174832)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument receipt_rule_set_name", value=receipt_rule_set_name, expected_type=type_hints["receipt_rule_set_name"])
        return typing.cast(IReceiptRuleSet, jsii.sinvoke(cls, "fromReceiptRuleSetName", [scope, id, receipt_rule_set_name]))

    @jsii.member(jsii_name="addDropSpamRule")
    def _add_drop_spam_rule(self) -> None:
        '''Adds a drop spam rule.'''
        return typing.cast(None, jsii.invoke(self, "addDropSpamRule", []))

    @jsii.member(jsii_name="addRule")
    def add_rule(
        self,
        id: builtins.str,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional["TlsPolicy"] = None,
    ) -> ReceiptRule:
        '''Adds a new receipt rule in this rule set.

        The new rule is added after
        the last added rule unless ``after`` is specified.

        :param id: -
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8cd532ef11b279fc4ddb81d21e2fd9962d1cc828cc92e5f4985bb2451030ca3a)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ReceiptRuleOptions(
            actions=actions,
            after=after,
            enabled=enabled,
            receipt_rule_name=receipt_rule_name,
            recipients=recipients,
            scan_enabled=scan_enabled,
            tls_policy=tls_policy,
        )

        return typing.cast(ReceiptRule, jsii.invoke(self, "addRule", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="receiptRuleSetName")
    def receipt_rule_set_name(self) -> builtins.str:
        '''The receipt rule set name.'''
        return typing.cast(builtins.str, jsii.get(self, "receiptRuleSetName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.ReceiptRuleSetProps",
    jsii_struct_bases=[],
    name_mapping={
        "drop_spam": "dropSpam",
        "receipt_rule_set_name": "receiptRuleSetName",
        "rules": "rules",
    },
)
class ReceiptRuleSetProps:
    def __init__(
        self,
        *,
        drop_spam: typing.Optional[builtins.bool] = None,
        receipt_rule_set_name: typing.Optional[builtins.str] = None,
        rules: typing.Optional[typing.Sequence[typing.Union[ReceiptRuleOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Construction properties for a ReceiptRuleSet.

        :param drop_spam: Whether to add a first rule to stop processing messages that have at least one spam indicator. Default: false
        :param receipt_rule_set_name: The name for the receipt rule set. Default: - A CloudFormation generated name.
        :param rules: The list of rules to add to this rule set. Rules are added in the same order as they appear in the list. Default: - No rules are added to the rule set.

        :exampleMetadata: infused

        Example::

            import aws_cdk.aws_s3 as s3
            import aws_cdk.aws_ses_actions as actions
            
            
            bucket = s3.Bucket(self, "Bucket")
            topic = sns.Topic(self, "Topic")
            
            ses.ReceiptRuleSet(self, "RuleSet",
                rules=[ses.ReceiptRuleOptions(
                    recipients=["hello@aws.com"],
                    actions=[
                        actions.AddHeader(
                            name="X-Special-Header",
                            value="aws"
                        ),
                        actions.S3(
                            bucket=bucket,
                            object_key_prefix="emails/",
                            topic=topic
                        )
                    ]
                ), ses.ReceiptRuleOptions(
                    recipients=["aws.com"],
                    actions=[
                        actions.Sns(
                            topic=topic
                        )
                    ]
                )
                ]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1cc19b30dc991a483fd278ee500d3d3e57d7a5a9ff95850a924babd266fac0fe)
            check_type(argname="argument drop_spam", value=drop_spam, expected_type=type_hints["drop_spam"])
            check_type(argname="argument receipt_rule_set_name", value=receipt_rule_set_name, expected_type=type_hints["receipt_rule_set_name"])
            check_type(argname="argument rules", value=rules, expected_type=type_hints["rules"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if drop_spam is not None:
            self._values["drop_spam"] = drop_spam
        if receipt_rule_set_name is not None:
            self._values["receipt_rule_set_name"] = receipt_rule_set_name
        if rules is not None:
            self._values["rules"] = rules

    @builtins.property
    def drop_spam(self) -> typing.Optional[builtins.bool]:
        '''Whether to add a first rule to stop processing messages that have at least one spam indicator.

        :default: false
        '''
        result = self._values.get("drop_spam")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_set_name(self) -> typing.Optional[builtins.str]:
        '''The name for the receipt rule set.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_set_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def rules(self) -> typing.Optional[typing.List[ReceiptRuleOptions]]:
        '''The list of rules to add to this rule set.

        Rules are added in the same
        order as they appear in the list.

        :default: - No rules are added to the rule set.
        '''
        result = self._values.get("rules")
        return typing.cast(typing.Optional[typing.List[ReceiptRuleOptions]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ReceiptRuleSetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.S3ActionConfig",
    jsii_struct_bases=[],
    name_mapping={
        "bucket_name": "bucketName",
        "kms_key_arn": "kmsKeyArn",
        "object_key_prefix": "objectKeyPrefix",
        "topic_arn": "topicArn",
    },
)
class S3ActionConfig:
    def __init__(
        self,
        *,
        bucket_name: builtins.str,
        kms_key_arn: typing.Optional[builtins.str] = None,
        object_key_prefix: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''S3Action configuration.

        :param bucket_name: The name of the Amazon S3 bucket that you want to send incoming mail to.
        :param kms_key_arn: The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. Default: - Emails are not encrypted.
        :param object_key_prefix: The key prefix of the Amazon S3 bucket. Default: - No prefix.
        :param topic_arn: The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            s3_action_config = ses.S3ActionConfig(
                bucket_name="bucketName",
            
                # the properties below are optional
                kms_key_arn="kmsKeyArn",
                object_key_prefix="objectKeyPrefix",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ef118e7dd1d569a24b4ab4f36d8ac563d485f357ed7b48efc12c802a2b6b2182)
            check_type(argname="argument bucket_name", value=bucket_name, expected_type=type_hints["bucket_name"])
            check_type(argname="argument kms_key_arn", value=kms_key_arn, expected_type=type_hints["kms_key_arn"])
            check_type(argname="argument object_key_prefix", value=object_key_prefix, expected_type=type_hints["object_key_prefix"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "bucket_name": bucket_name,
        }
        if kms_key_arn is not None:
            self._values["kms_key_arn"] = kms_key_arn
        if object_key_prefix is not None:
            self._values["object_key_prefix"] = object_key_prefix
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def bucket_name(self) -> builtins.str:
        '''The name of the Amazon S3 bucket that you want to send incoming mail to.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-bucketname
        '''
        result = self._values.get("bucket_name")
        assert result is not None, "Required property 'bucket_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def kms_key_arn(self) -> typing.Optional[builtins.str]:
        '''The customer master key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket.

        :default: - Emails are not encrypted.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-kmskeyarn
        '''
        result = self._values.get("kms_key_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def object_key_prefix(self) -> typing.Optional[builtins.str]:
        '''The key prefix of the Amazon S3 bucket.

        :default: - No prefix.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-objectkeyprefix
        '''
        result = self._values.get("object_key_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-s3action.html#cfn-ses-receiptrule-s3action-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "S3ActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.SNSActionConfig",
    jsii_struct_bases=[],
    name_mapping={"encoding": "encoding", "topic_arn": "topicArn"},
)
class SNSActionConfig:
    def __init__(
        self,
        *,
        encoding: typing.Optional[builtins.str] = None,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''SNSAction configuration.

        :param encoding: The encoding to use for the email within the Amazon SNS notification. Default: 'UTF-8'
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            s_nSAction_config = ses.SNSActionConfig(
                encoding="encoding",
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__173bb322225263bb156456dc72b3d2b251f55cd39ef1474dc97211e5e41f07af)
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if encoding is not None:
            self._values["encoding"] = encoding
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The encoding to use for the email within the Amazon SNS notification.

        :default: 'UTF-8'

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-encoding
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-snsaction.html#cfn-ses-receiptrule-snsaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "SNSActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.StopActionConfig",
    jsii_struct_bases=[],
    name_mapping={"scope": "scope", "topic_arn": "topicArn"},
)
class StopActionConfig:
    def __init__(
        self,
        *,
        scope: builtins.str,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''StopAction configuration.

        :param scope: The scope of the StopAction. The only acceptable value is RuleSet.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            stop_action_config = ses.StopActionConfig(
                scope="scope",
            
                # the properties below are optional
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d7e81c4cd24879569e0bdfa8c28a29714bdb254ca09f291cf53f0fddd448e9fc)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "scope": scope,
        }
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def scope(self) -> builtins.str:
        '''The scope of the StopAction.

        The only acceptable value is RuleSet.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-stopaction.html#cfn-ses-receiptrule-stopaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "StopActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.SuppressionReasons")
class SuppressionReasons(enum.Enum):
    '''Reasons for which recipient email addresses should be automatically added to your account's suppression list.

    :exampleMetadata: infused

    Example::

        # my_pool: ses.IDedicatedIpPool
        
        
        ses.ConfigurationSet(self, "ConfigurationSet",
            custom_tracking_redirect_domain="track.cdk.dev",
            suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
            tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
            dedicated_ip_pool=my_pool
        )
    '''

    BOUNCES_AND_COMPLAINTS = "BOUNCES_AND_COMPLAINTS"
    '''Bounces and complaints.'''
    BOUNCES_ONLY = "BOUNCES_ONLY"
    '''Bounces only.'''
    COMPLAINTS_ONLY = "COMPLAINTS_ONLY"
    '''Complaints only.'''


@jsii.enum(jsii_type="aws-cdk-lib.aws_ses.TlsPolicy")
class TlsPolicy(enum.Enum):
    '''The type of TLS policy for a receipt rule.'''

    OPTIONAL = "OPTIONAL"
    '''Do not check for TLS.'''
    REQUIRE = "REQUIRE"
    '''Bounce emails that are not received over TLS.'''


@jsii.implements(IVdmAttributes)
class VdmAttributes(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.VdmAttributes",
):
    '''Virtual Deliverablity Manager (VDM) attributes.

    :exampleMetadata: infused

    Example::

        # Enables engagement tracking and optimized shared delivery by default
        ses.VdmAttributes(self, "Vdm")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        engagement_metrics: typing.Optional[builtins.bool] = None,
        optimized_shared_delivery: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param engagement_metrics: Whether engagement metrics are enabled for your account. Default: true
        :param optimized_shared_delivery: Whether optimized shared delivery is enabled for your account. Default: true
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e90b2ec586dfbf0314232aaea6d64cdd5816072b0bcfed076d517ff63a3b1000)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = VdmAttributesProps(
            engagement_metrics=engagement_metrics,
            optimized_shared_delivery=optimized_shared_delivery,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromVdmAttributesName")
    @builtins.classmethod
    def from_vdm_attributes_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        vdm_attributes_name: builtins.str,
    ) -> IVdmAttributes:
        '''Use an existing Virtual Deliverablity Manager attributes resource.

        :param scope: -
        :param id: -
        :param vdm_attributes_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c4f2d4b83707480c9a8afc395f18812d02a2c5e0fc50cd63f1eb9d708176325)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument vdm_attributes_name", value=vdm_attributes_name, expected_type=type_hints["vdm_attributes_name"])
        return typing.cast(IVdmAttributes, jsii.sinvoke(cls, "fromVdmAttributesName", [scope, id, vdm_attributes_name]))

    @builtins.property
    @jsii.member(jsii_name="vdmAttributesName")
    def vdm_attributes_name(self) -> builtins.str:
        '''The name of the resource behind the Virtual Deliverablity Manager attributes.'''
        return typing.cast(builtins.str, jsii.get(self, "vdmAttributesName"))

    @builtins.property
    @jsii.member(jsii_name="vdmAttributesResourceId")
    def vdm_attributes_resource_id(self) -> builtins.str:
        '''Resource ID for the Virtual Deliverablity Manager attributes.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "vdmAttributesResourceId"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.VdmAttributesProps",
    jsii_struct_bases=[],
    name_mapping={
        "engagement_metrics": "engagementMetrics",
        "optimized_shared_delivery": "optimizedSharedDelivery",
    },
)
class VdmAttributesProps:
    def __init__(
        self,
        *,
        engagement_metrics: typing.Optional[builtins.bool] = None,
        optimized_shared_delivery: typing.Optional[builtins.bool] = None,
    ) -> None:
        '''Properties for the Virtual Deliverablity Manager (VDM) attributes.

        :param engagement_metrics: Whether engagement metrics are enabled for your account. Default: true
        :param optimized_shared_delivery: Whether optimized shared delivery is enabled for your account. Default: true

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            vdm_attributes_props = ses.VdmAttributesProps(
                engagement_metrics=False,
                optimized_shared_delivery=False
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1882e9d1289b07868b3ffcfb9d92629e699992b01e6475750adbffc0137815b0)
            check_type(argname="argument engagement_metrics", value=engagement_metrics, expected_type=type_hints["engagement_metrics"])
            check_type(argname="argument optimized_shared_delivery", value=optimized_shared_delivery, expected_type=type_hints["optimized_shared_delivery"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if engagement_metrics is not None:
            self._values["engagement_metrics"] = engagement_metrics
        if optimized_shared_delivery is not None:
            self._values["optimized_shared_delivery"] = optimized_shared_delivery

    @builtins.property
    def engagement_metrics(self) -> typing.Optional[builtins.bool]:
        '''Whether engagement metrics are enabled for your account.

        :default: true
        '''
        result = self._values.get("engagement_metrics")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def optimized_shared_delivery(self) -> typing.Optional[builtins.bool]:
        '''Whether optimized shared delivery is enabled for your account.

        :default: true
        '''
        result = self._values.get("optimized_shared_delivery")
        return typing.cast(typing.Optional[builtins.bool], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VdmAttributesProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.WorkmailActionConfig",
    jsii_struct_bases=[],
    name_mapping={"organization_arn": "organizationArn", "topic_arn": "topicArn"},
)
class WorkmailActionConfig:
    def __init__(
        self,
        *,
        organization_arn: builtins.str,
        topic_arn: typing.Optional[builtins.str] = None,
    ) -> None:
        '''WorkmailAction configuration.

        :param organization_arn: The Amazon Resource Name (ARN) of the Amazon WorkMail organization.
        :param topic_arn: The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. Default: - No notification is sent to SNS.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            workmail_action_config = ses.WorkmailActionConfig(
                organization_arn="organizationArn",
            
                # the properties below are optional
                topic_arn="topicArn"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08a56aa5b57fd1699d7c92c360d0709a2cfb31d3cb323b992c4b4e89432c836b)
            check_type(argname="argument organization_arn", value=organization_arn, expected_type=type_hints["organization_arn"])
            check_type(argname="argument topic_arn", value=topic_arn, expected_type=type_hints["topic_arn"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "organization_arn": organization_arn,
        }
        if topic_arn is not None:
            self._values["topic_arn"] = topic_arn

    @builtins.property
    def organization_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the Amazon WorkMail organization.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-organizationarn
        '''
        result = self._values.get("organization_arn")
        assert result is not None, "Required property 'organization_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def topic_arn(self) -> typing.Optional[builtins.str]:
        '''The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called.

        :default: - No notification is sent to SNS.

        :link: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ses-receiptrule-workmailaction.html#cfn-ses-receiptrule-workmailaction-topicarn
        '''
        result = self._values.get("topic_arn")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "WorkmailActionConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IConfigurationSet)
class ConfigurationSet(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSet",
):
    '''A configuration set.

    :exampleMetadata: infused

    Example::

        # my_pool: ses.IDedicatedIpPool
        
        
        ses.ConfigurationSet(self, "ConfigurationSet",
            custom_tracking_redirect_domain="track.cdk.dev",
            suppression_reasons=ses.SuppressionReasons.COMPLAINTS_ONLY,
            tls_policy=ses.ConfigurationSetTlsPolicy.REQUIRE,
            dedicated_ip_pool=my_pool
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_set_name: typing.Optional[builtins.str] = None,
        custom_tracking_redirect_domain: typing.Optional[builtins.str] = None,
        dedicated_ip_pool: typing.Optional[IDedicatedIpPool] = None,
        reputation_metrics: typing.Optional[builtins.bool] = None,
        sending_enabled: typing.Optional[builtins.bool] = None,
        suppression_reasons: typing.Optional[SuppressionReasons] = None,
        tls_policy: typing.Optional[ConfigurationSetTlsPolicy] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param configuration_set_name: A name for the configuration set. Default: - a CloudFormation generated name
        :param custom_tracking_redirect_domain: The custom subdomain that is used to redirect email recipients to the Amazon SES event tracking domain. Default: - use the default awstrack.me domain
        :param dedicated_ip_pool: The dedicated IP pool to associate with the configuration set. Default: - do not use a dedicated IP pool
        :param reputation_metrics: Whether to publish reputation metrics for the configuration set, such as bounce and complaint rates, to Amazon CloudWatch. Default: false
        :param sending_enabled: Whether email sending is enabled. Default: true
        :param suppression_reasons: The reasons for which recipient email addresses should be automatically added to your account's suppression list. Default: - use account level settings
        :param tls_policy: Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). Default: ConfigurationSetTlsPolicy.OPTIONAL
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__52b42851a408d3eb2b07399f2b34603200cef443be5e9f913f4a1d80a47ac83e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ConfigurationSetProps(
            configuration_set_name=configuration_set_name,
            custom_tracking_redirect_domain=custom_tracking_redirect_domain,
            dedicated_ip_pool=dedicated_ip_pool,
            reputation_metrics=reputation_metrics,
            sending_enabled=sending_enabled,
            suppression_reasons=suppression_reasons,
            tls_policy=tls_policy,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigurationSetName")
    @builtins.classmethod
    def from_configuration_set_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        configuration_set_name: builtins.str,
    ) -> IConfigurationSet:
        '''Use an existing configuration set.

        :param scope: -
        :param id: -
        :param configuration_set_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2ae99096d05b68163763ffbed7aafa034cd3a774f632bff2370d017f76194045)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument configuration_set_name", value=configuration_set_name, expected_type=type_hints["configuration_set_name"])
        return typing.cast(IConfigurationSet, jsii.sinvoke(cls, "fromConfigurationSetName", [scope, id, configuration_set_name]))

    @jsii.member(jsii_name="addEventDestination")
    def add_event_destination(
        self,
        id: builtins.str,
        *,
        destination: EventDestination,
        configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        events: typing.Optional[typing.Sequence[EmailSendingEvent]] = None,
    ) -> "ConfigurationSetEventDestination":
        '''Adds an event destination to this configuration set.

        :param id: -
        :param destination: The event destination.
        :param configuration_set_event_destination_name: A name for the configuration set event destination. Default: - a CloudFormation generated name
        :param enabled: Whether Amazon SES publishes events to this destination. Default: true
        :param events: The type of email sending events to publish to the event destination. Default: - send all event types
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__969c3bbc0e7891ce9eb910e67644f0f9bcb29f65f5ec021df94eed425cb0d707)
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        options = ConfigurationSetEventDestinationOptions(
            destination=destination,
            configuration_set_event_destination_name=configuration_set_event_destination_name,
            enabled=enabled,
            events=events,
        )

        return typing.cast("ConfigurationSetEventDestination", jsii.invoke(self, "addEventDestination", [id, options]))

    @builtins.property
    @jsii.member(jsii_name="configurationSetName")
    def configuration_set_name(self) -> builtins.str:
        '''The name of the configuration set.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetName"))


@jsii.implements(IConfigurationSetEventDestination)
class ConfigurationSetEventDestination(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.ConfigurationSetEventDestination",
):
    '''A configuration set event destination.

    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_ses as ses
        
        # configuration_set: ses.ConfigurationSet
        # event_destination: ses.EventDestination
        
        configuration_set_event_destination = ses.ConfigurationSetEventDestination(self, "MyConfigurationSetEventDestination",
            configuration_set=configuration_set,
            destination=event_destination,
        
            # the properties below are optional
            configuration_set_event_destination_name="configurationSetEventDestinationName",
            enabled=False,
            events=[ses.EmailSendingEvent.SEND]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        configuration_set: IConfigurationSet,
        destination: EventDestination,
        configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
        enabled: typing.Optional[builtins.bool] = None,
        events: typing.Optional[typing.Sequence[EmailSendingEvent]] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param configuration_set: The configuration set that contains the event destination.
        :param destination: The event destination.
        :param configuration_set_event_destination_name: A name for the configuration set event destination. Default: - a CloudFormation generated name
        :param enabled: Whether Amazon SES publishes events to this destination. Default: true
        :param events: The type of email sending events to publish to the event destination. Default: - send all event types
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cf213dc05e866bbe3e9422388bafa084e54ef674803fa10657e5b96b908d6965)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = ConfigurationSetEventDestinationProps(
            configuration_set=configuration_set,
            destination=destination,
            configuration_set_event_destination_name=configuration_set_event_destination_name,
            enabled=enabled,
            events=events,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromConfigurationSetEventDestinationId")
    @builtins.classmethod
    def from_configuration_set_event_destination_id(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        configuration_set_event_destination_id: builtins.str,
    ) -> IConfigurationSetEventDestination:
        '''Use an existing configuration set.

        :param scope: -
        :param id: -
        :param configuration_set_event_destination_id: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4740349c6047d2ad783d767c6424ac19156d882d3534207b1440beda62370433)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument configuration_set_event_destination_id", value=configuration_set_event_destination_id, expected_type=type_hints["configuration_set_event_destination_id"])
        return typing.cast(IConfigurationSetEventDestination, jsii.sinvoke(cls, "fromConfigurationSetEventDestinationId", [scope, id, configuration_set_event_destination_id]))

    @builtins.property
    @jsii.member(jsii_name="configurationSetEventDestinationId")
    def configuration_set_event_destination_id(self) -> builtins.str:
        '''The ID of the configuration set event destination.'''
        return typing.cast(builtins.str, jsii.get(self, "configurationSetEventDestinationId"))


@jsii.implements(IDedicatedIpPool)
class DedicatedIpPool(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.DedicatedIpPool",
):
    '''A dedicated IP pool.

    :exampleMetadata: infused

    Example::

        ses.DedicatedIpPool(self, "Pool")
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        dedicated_ip_pool_name: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param dedicated_ip_pool_name: A name for the dedicated IP pool. Default: - a CloudFormation generated name
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a4f168ec9aad173d023a8ac330a62f7c1ce87601f0a8876e8cbf35c7dcd89ead)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = DedicatedIpPoolProps(dedicated_ip_pool_name=dedicated_ip_pool_name)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromDedicatedIpPoolName")
    @builtins.classmethod
    def from_dedicated_ip_pool_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        dedicated_ip_pool_name: builtins.str,
    ) -> IDedicatedIpPool:
        '''Use an existing dedicated IP pool.

        :param scope: -
        :param id: -
        :param dedicated_ip_pool_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6d620bd493f43394b0479d58a02acf7d3c1644c63cc64fc186abe29e763516bf)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument dedicated_ip_pool_name", value=dedicated_ip_pool_name, expected_type=type_hints["dedicated_ip_pool_name"])
        return typing.cast(IDedicatedIpPool, jsii.sinvoke(cls, "fromDedicatedIpPoolName", [scope, id, dedicated_ip_pool_name]))

    @builtins.property
    @jsii.member(jsii_name="dedicatedIpPoolName")
    def dedicated_ip_pool_name(self) -> builtins.str:
        '''The name of the dedicated IP pool.'''
        return typing.cast(builtins.str, jsii.get(self, "dedicatedIpPoolName"))


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_ses.DropSpamReceiptRuleProps",
    jsii_struct_bases=[ReceiptRuleProps],
    name_mapping={
        "actions": "actions",
        "after": "after",
        "enabled": "enabled",
        "receipt_rule_name": "receiptRuleName",
        "recipients": "recipients",
        "scan_enabled": "scanEnabled",
        "tls_policy": "tlsPolicy",
        "rule_set": "ruleSet",
    },
)
class DropSpamReceiptRuleProps(ReceiptRuleProps):
    def __init__(
        self,
        *,
        actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
        after: typing.Optional[IReceiptRule] = None,
        enabled: typing.Optional[builtins.bool] = None,
        receipt_rule_name: typing.Optional[builtins.str] = None,
        recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
        scan_enabled: typing.Optional[builtins.bool] = None,
        tls_policy: typing.Optional[TlsPolicy] = None,
        rule_set: IReceiptRuleSet,
    ) -> None:
        '''
        :param actions: An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule. Default: - No actions.
        :param after: An existing rule after which the new rule will be placed. Default: - The new rule is inserted at the beginning of the rule list.
        :param enabled: Whether the rule is active. Default: true
        :param receipt_rule_name: The name for the rule. Default: - A CloudFormation generated name.
        :param recipients: The recipient domains and email addresses that the receipt rule applies to. Default: - Match all recipients under all verified domains.
        :param scan_enabled: Whether to scan for spam and viruses. Default: false
        :param tls_policy: Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). Default: - Optional which will not check for TLS.
        :param rule_set: The name of the rule set that the receipt rule will be added to.

        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_ses as ses
            
            # receipt_rule: ses.ReceiptRule
            # receipt_rule_action: ses.IReceiptRuleAction
            # receipt_rule_set: ses.ReceiptRuleSet
            
            drop_spam_receipt_rule_props = ses.DropSpamReceiptRuleProps(
                rule_set=receipt_rule_set,
            
                # the properties below are optional
                actions=[receipt_rule_action],
                after=receipt_rule,
                enabled=False,
                receipt_rule_name="receiptRuleName",
                recipients=["recipients"],
                scan_enabled=False,
                tls_policy=ses.TlsPolicy.OPTIONAL
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f78c7c8898fbe6486ab42279bd1b1abce1f0305e2d0cc19d79400e08c909951f)
            check_type(argname="argument actions", value=actions, expected_type=type_hints["actions"])
            check_type(argname="argument after", value=after, expected_type=type_hints["after"])
            check_type(argname="argument enabled", value=enabled, expected_type=type_hints["enabled"])
            check_type(argname="argument receipt_rule_name", value=receipt_rule_name, expected_type=type_hints["receipt_rule_name"])
            check_type(argname="argument recipients", value=recipients, expected_type=type_hints["recipients"])
            check_type(argname="argument scan_enabled", value=scan_enabled, expected_type=type_hints["scan_enabled"])
            check_type(argname="argument tls_policy", value=tls_policy, expected_type=type_hints["tls_policy"])
            check_type(argname="argument rule_set", value=rule_set, expected_type=type_hints["rule_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "rule_set": rule_set,
        }
        if actions is not None:
            self._values["actions"] = actions
        if after is not None:
            self._values["after"] = after
        if enabled is not None:
            self._values["enabled"] = enabled
        if receipt_rule_name is not None:
            self._values["receipt_rule_name"] = receipt_rule_name
        if recipients is not None:
            self._values["recipients"] = recipients
        if scan_enabled is not None:
            self._values["scan_enabled"] = scan_enabled
        if tls_policy is not None:
            self._values["tls_policy"] = tls_policy

    @builtins.property
    def actions(self) -> typing.Optional[typing.List[IReceiptRuleAction]]:
        '''An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

        :default: - No actions.
        '''
        result = self._values.get("actions")
        return typing.cast(typing.Optional[typing.List[IReceiptRuleAction]], result)

    @builtins.property
    def after(self) -> typing.Optional[IReceiptRule]:
        '''An existing rule after which the new rule will be placed.

        :default: - The new rule is inserted at the beginning of the rule list.
        '''
        result = self._values.get("after")
        return typing.cast(typing.Optional[IReceiptRule], result)

    @builtins.property
    def enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether the rule is active.

        :default: true
        '''
        result = self._values.get("enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def receipt_rule_name(self) -> typing.Optional[builtins.str]:
        '''The name for the rule.

        :default: - A CloudFormation generated name.
        '''
        result = self._values.get("receipt_rule_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def recipients(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The recipient domains and email addresses that the receipt rule applies to.

        :default: - Match all recipients under all verified domains.
        '''
        result = self._values.get("recipients")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def scan_enabled(self) -> typing.Optional[builtins.bool]:
        '''Whether to scan for spam and viruses.

        :default: false
        '''
        result = self._values.get("scan_enabled")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def tls_policy(self) -> typing.Optional[TlsPolicy]:
        '''Whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS).

        :default: - Optional which will not check for TLS.
        '''
        result = self._values.get("tls_policy")
        return typing.cast(typing.Optional[TlsPolicy], result)

    @builtins.property
    def rule_set(self) -> IReceiptRuleSet:
        '''The name of the rule set that the receipt rule will be added to.'''
        result = self._values.get("rule_set")
        assert result is not None, "Required property 'rule_set' is missing"
        return typing.cast(IReceiptRuleSet, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DropSpamReceiptRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(IEmailIdentity)
class EmailIdentity(
    _Resource_45bc6135,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_ses.EmailIdentity",
):
    '''An email identity.

    :exampleMetadata: infused

    Example::

        # my_hosted_zone: route53.IPublicHostedZone
        
        
        identity = ses.EmailIdentity(self, "Identity",
            identity=ses.Identity.public_hosted_zone(my_hosted_zone),
            mail_from_domain="mail.cdk.dev"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        identity: Identity,
        configuration_set: typing.Optional[IConfigurationSet] = None,
        dkim_identity: typing.Optional[DkimIdentity] = None,
        dkim_signing: typing.Optional[builtins.bool] = None,
        feedback_forwarding: typing.Optional[builtins.bool] = None,
        mail_from_behavior_on_mx_failure: typing.Optional[MailFromBehaviorOnMxFailure] = None,
        mail_from_domain: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: -
        :param id: -
        :param identity: The email address or domain to verify.
        :param configuration_set: The configuration set to associate with the email identity. Default: - do not use a specific configuration set
        :param dkim_identity: The type of DKIM identity to use. Default: - Easy DKIM with a key length of 2048-bit
        :param dkim_signing: Whether the messages that are sent from the identity are signed using DKIM. Default: true
        :param feedback_forwarding: Whether to receive email notifications when bounce or complaint events occur. These notifications are sent to the address that you specified in the ``Return-Path`` header of the original email. You're required to have a method of tracking bounces and complaints. If you haven't set up another mechanism for receiving bounce or complaint notifications (for example, by setting up an event destination), you receive an email notification when these events occur (even if this setting is disabled). Default: true
        :param mail_from_behavior_on_mx_failure: The action to take if the required MX record for the MAIL FROM domain isn't found when you send an email. Default: MailFromBehaviorOnMxFailure.USE_DEFAULT_VALUE
        :param mail_from_domain: The custom MAIL FROM domain that you want the verified identity to use. The MAIL FROM domain must meet the following criteria: - It has to be a subdomain of the verified identity - It can't be used to receive email - It can't be used in a "From" address if the MAIL FROM domain is a destination for feedback forwarding emails Default: - use amazonses.com
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0d44bf733be67b29d51a6c681c3faafee6103884474147b68d4b466a07017e9)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = EmailIdentityProps(
            identity=identity,
            configuration_set=configuration_set,
            dkim_identity=dkim_identity,
            dkim_signing=dkim_signing,
            feedback_forwarding=feedback_forwarding,
            mail_from_behavior_on_mx_failure=mail_from_behavior_on_mx_failure,
            mail_from_domain=mail_from_domain,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="fromEmailIdentityName")
    @builtins.classmethod
    def from_email_identity_name(
        cls,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        email_identity_name: builtins.str,
    ) -> IEmailIdentity:
        '''Use an existing email identity.

        :param scope: -
        :param id: -
        :param email_identity_name: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eb1cb50e69249e3f61387a80db0e14cc9a9790c024548390466a511484409a85)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument email_identity_name", value=email_identity_name, expected_type=type_hints["email_identity_name"])
        return typing.cast(IEmailIdentity, jsii.sinvoke(cls, "fromEmailIdentityName", [scope, id, email_identity_name]))

    @builtins.property
    @jsii.member(jsii_name="dkimDnsTokenName1")
    def dkim_dns_token_name1(self) -> builtins.str:
        '''The host name for the first token that you have to add to the DNS configurationfor your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenName1"))

    @builtins.property
    @jsii.member(jsii_name="dkimDnsTokenName2")
    def dkim_dns_token_name2(self) -> builtins.str:
        '''The host name for the second token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenName2"))

    @builtins.property
    @jsii.member(jsii_name="dkimDnsTokenName3")
    def dkim_dns_token_name3(self) -> builtins.str:
        '''The host name for the third token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenName3"))

    @builtins.property
    @jsii.member(jsii_name="dkimDnsTokenValue1")
    def dkim_dns_token_value1(self) -> builtins.str:
        '''The record value for the first token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenValue1"))

    @builtins.property
    @jsii.member(jsii_name="dkimDnsTokenValue2")
    def dkim_dns_token_value2(self) -> builtins.str:
        '''The record value for the second token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenValue2"))

    @builtins.property
    @jsii.member(jsii_name="dkimDnsTokenValue3")
    def dkim_dns_token_value3(self) -> builtins.str:
        '''The record value for the third token that you have to add to the DNS configuration for your domain.

        :attribute: true
        '''
        return typing.cast(builtins.str, jsii.get(self, "dkimDnsTokenValue3"))

    @builtins.property
    @jsii.member(jsii_name="dkimRecords")
    def dkim_records(self) -> typing.List[DkimRecord]:
        '''DKIM records for this identity.'''
        return typing.cast(typing.List[DkimRecord], jsii.get(self, "dkimRecords"))

    @builtins.property
    @jsii.member(jsii_name="emailIdentityName")
    def email_identity_name(self) -> builtins.str:
        '''The name of the email identity.'''
        return typing.cast(builtins.str, jsii.get(self, "emailIdentityName"))


__all__ = [
    "AddHeaderActionConfig",
    "AllowListReceiptFilter",
    "AllowListReceiptFilterProps",
    "BounceActionConfig",
    "ByoDkimOptions",
    "CfnConfigurationSet",
    "CfnConfigurationSetEventDestination",
    "CfnConfigurationSetEventDestinationProps",
    "CfnConfigurationSetProps",
    "CfnContactList",
    "CfnContactListProps",
    "CfnDedicatedIpPool",
    "CfnDedicatedIpPoolProps",
    "CfnEmailIdentity",
    "CfnEmailIdentityProps",
    "CfnReceiptFilter",
    "CfnReceiptFilterProps",
    "CfnReceiptRule",
    "CfnReceiptRuleProps",
    "CfnReceiptRuleSet",
    "CfnReceiptRuleSetProps",
    "CfnTemplate",
    "CfnTemplateProps",
    "CfnVdmAttributes",
    "CfnVdmAttributesProps",
    "CloudWatchDimension",
    "CloudWatchDimensionSource",
    "ConfigurationSet",
    "ConfigurationSetEventDestination",
    "ConfigurationSetEventDestinationOptions",
    "ConfigurationSetEventDestinationProps",
    "ConfigurationSetProps",
    "ConfigurationSetTlsPolicy",
    "DedicatedIpPool",
    "DedicatedIpPoolProps",
    "DkimIdentity",
    "DkimIdentityConfig",
    "DkimRecord",
    "DropSpamReceiptRule",
    "DropSpamReceiptRuleProps",
    "EasyDkimSigningKeyLength",
    "EmailIdentity",
    "EmailIdentityProps",
    "EmailSendingEvent",
    "EventDestination",
    "IConfigurationSet",
    "IConfigurationSetEventDestination",
    "IDedicatedIpPool",
    "IEmailIdentity",
    "IReceiptRule",
    "IReceiptRuleAction",
    "IReceiptRuleSet",
    "IVdmAttributes",
    "Identity",
    "LambdaActionConfig",
    "MailFromBehaviorOnMxFailure",
    "ReceiptFilter",
    "ReceiptFilterPolicy",
    "ReceiptFilterProps",
    "ReceiptRule",
    "ReceiptRuleActionConfig",
    "ReceiptRuleOptions",
    "ReceiptRuleProps",
    "ReceiptRuleSet",
    "ReceiptRuleSetProps",
    "S3ActionConfig",
    "SNSActionConfig",
    "StopActionConfig",
    "SuppressionReasons",
    "TlsPolicy",
    "VdmAttributes",
    "VdmAttributesProps",
    "WorkmailActionConfig",
]

publication.publish()

def _typecheckingstub__a170d992f7b65fcd93ee761689bdfa76a44ecd1ea7edfc889f8823c2885ff1ab(
    *,
    header_name: builtins.str,
    header_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__945fe453cd006222ecf22c8ccfcce9d99dd299b11a1edd1f0b1103473142ada4(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ips: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b81b4e341d87e039070ac9d2e5681f812a77ceb3a1c4c81466809dabc58bf7d(
    *,
    ips: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0ed2c8bc5cd582573c72e7ec8ce40272efe39b764d2bea49d78fc57f7929e4c0(
    *,
    message: builtins.str,
    sender: builtins.str,
    smtp_reply_code: builtins.str,
    status_code: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b4e23b7bc7e365a5b875e5ba4ad81ccfb3182ca4059f46dfe11066714a13fffb(
    *,
    private_key: _SecretValue_3dd0ddae,
    selector: builtins.str,
    public_key: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ad84a733d05a7160c0517733c56c249f6a299231ebcf8e982ed1aeda9e9b3daf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    suppression_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SuppressionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vdm_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.VdmOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__703d8eb12ae21101f4f93e6ab7089d820f42a27a22e1028eee983deee4056343(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3ec352b38e2d7189e23d09b362a1b86566764825e5e48e241ee1b2ef51c1b511(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5255bb6021541c7e84379b09a4ffd806238f1ac83ad0e7000ea7e34028bc9a3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.DeliveryOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9757b0b78870ccfafd1e870ca194f545ac0873693da40dc15e29ba8b5beb21b7(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dcb56d1f8e63eec7f19208aaf5c6887b110d769aa45bfe8a7329339a1cc321b6(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.ReputationOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bfa327a56576655b9670d914964b52df069b29497d84b812a2f15586b1c5faa9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SendingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4d6e92203e0b0fb9ad18351409d2e930bd3b3881d922fcb2f2b38b337f5f4c55(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.SuppressionOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0e2738cc83fe741aa7d2c58d5db581a79f89d7427a9504ac697d8f7dd2004ea9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.TrackingOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f115779032dd22d020f87b590d89ccdd0a4fc3f269b15bbecfde29ad92e4289(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnConfigurationSet.VdmOptionsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e8d48d16888f580be3782790c85806d5e5ef5c592f9390a1048567593c281148(
    *,
    engagement_metrics: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cad65d433b7328c2fe1d15052509478ad394628f7bbce8157ed352a3291b5d6f(
    *,
    sending_pool_name: typing.Optional[builtins.str] = None,
    tls_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cabe5bd3bd3cb84baab32735da66eedb8e560e50da24718ab0d87b340502d858(
    *,
    optimized_shared_delivery: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66f701bd9f49ad0c515c9634599b8e0616f4f3b15f2e4f6b9f906f2542e78676(
    *,
    reputation_metrics_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a548843fec9d94e10684140077e38c05264eb17e9e2997b3e7a864cb183318b8(
    *,
    sending_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8d9a9f4a0b048a750b42ffb05bbf2f29193ab82552fe268e651a27bc5bf661be(
    *,
    suppressed_reasons: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9cb3a7d8357d451a88f3bdd86fea15ef7d167ba61579a61a8e1fe9eb6bfa73f2(
    *,
    custom_redirect_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94fcd9f4369b7da06731e9702fc08a13db56c4b817946b6fda1167dfc314ecd2(
    *,
    dashboard_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DashboardOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    guardian_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.GuardianOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e0376f935c1363b5c7cfddd668508c112d2a00f2637b1a84086b70c96af9e53c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_set_name: builtins.str,
    event_destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d77d1e029fcf58a1f079cf11a321a2e3416ae4150d8df3576a09e3c62095ca35(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8650d4b56a0c900e4a255fe7bb98030ff250164d423e43ab113f0bcb3cad116e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a9ebb672423cac8794fa77851a8fa78b27a8be4beabf8025723862ad9291d619(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c5bde831b7591d8114916d0e9453c13daabe44cbe1f0da50b7cd72b598079dfa(
    value: typing.Union[_IResolvable_da3f097b, CfnConfigurationSetEventDestination.EventDestinationProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e60b6436d0d38ae03fe0a4f110271b401e922dc980b2b61e9f401dd25eb1061c(
    *,
    dimension_configurations: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.DimensionConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf76f41f2226fa19acdad1732c136b3ee21554d7f8458ed43f731c0fee88cbcc(
    *,
    default_dimension_value: builtins.str,
    dimension_name: builtins.str,
    dimension_value_source: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b77a9a6a44a2946da816730acf4f2c79407a57e401fb25707130b8e68609c0b9(
    *,
    matching_event_types: typing.Sequence[builtins.str],
    cloud_watch_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.CloudWatchDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    kinesis_firehose_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.KinesisFirehoseDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    sns_destination: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.SnsDestinationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee1cd798be61243093d3e6c4cfddb9f06458011ead23160593d456863d3d8916(
    *,
    delivery_stream_arn: builtins.str,
    iam_role_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__088fd890007dccc782783b2f90e64f8c72607c080bdc0d3a15c7d13f1adbcf2b(
    *,
    topic_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5bf6472e974193204bd884002deb0a2d69e96cef811e1a0aa08aafb3997a9ca2(
    *,
    configuration_set_name: builtins.str,
    event_destination: typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSetEventDestination.EventDestinationProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e27ed179dbf809eedecaf57207416cd1680782d0d3ab4c539486ad7038b09efa(
    *,
    delivery_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.DeliveryOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[builtins.str] = None,
    reputation_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.ReputationOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sending_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SendingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    suppression_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.SuppressionOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    tracking_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.TrackingOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    vdm_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnConfigurationSet.VdmOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4f5901f6c4687a5069b93788dd46825d3f820617b06ab7617c713daa19e6b0a1(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    contact_list_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    topics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContactList.TopicProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__04e7980d7184167e42f7e01ae8cec876d43f150d71c7057fca33fc0a3e2d3e6b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7d95554a83c0f0d545d0786c20201ae723b64226988c31c92f93e116a98429(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fe87ab99d02860b4269adb497c2b85c5627baa1480977081d5983090e8f106cf(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b772e4221fab9fd85e09441b0917a7c5c4c012cb7676e6a6ea38ce5c619a4431(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f3ca0b0993b5ed610f353a70ff69c08d5866611a4967d6f45f069e82edf1d5a8(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a1a4f7da14b40f7178c1c0c458459ea9ecbdb3914bfe6c065e5ff051b6bd8728(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnContactList.TopicProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__51caf9f57b613a46837ae653fc48f880d6c601b01293293e456968c3aa00c3c7(
    *,
    default_subscription_status: builtins.str,
    display_name: builtins.str,
    topic_name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__072b7df8dc691d1a1cd6c9336ecf7d05df6b5b238b2a11c273d9ae0aaf2782c0(
    *,
    contact_list_name: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    topics: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnContactList.TopicProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__86a024e58c5549e30a3beca5bb152d09219a0cb42e6e02b0e95395595c9930e2(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    pool_name: typing.Optional[builtins.str] = None,
    scaling_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8104b1859d7ffadca75f36effd5e88f40353e147cbb9ff43a0adf3b020c8e7d5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d431f4fa3e72589a6c2f0607a33d0c813f15e49f2c036738c5ec863ee07438cc(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4397d06edc01bb178665cd7af2c334613e4b051f65bf7fc9a1638ae1775ed9cb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfe768b550097b0e81974377ae65fba6791743f6787f72492af555cd19e3685a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea1a308c0c75c9aabf33c8c8b6378da7534f946eff787acdd2dc100f0b482f56(
    *,
    pool_name: typing.Optional[builtins.str] = None,
    scaling_mode: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6dd153888b73988faf47365b573ef9e102d03faf2ff7fc2112c9b85962c0cc81(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    email_identity: builtins.str,
    configuration_set_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.ConfigurationSetAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dkim_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.DkimAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dkim_signing_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.DkimSigningAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    feedback_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.FeedbackAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2e59b4607b3737bad6d0d3dceb2602acfb4a055cf1db675a6a32c09ab24c984(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__89ed6968b3a6bd596dccac5a2250a9eaee13899cac4ddf323c6e8c46dae44315(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfc02af0c8ad1580f31a20eefddf3de5c4670d5d0e9e982f351c0a3f7be2ae99(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9e09bbe6ddf5291794cc13ffe01ceeb6dcf8075492dc575256ad5b6bc2f17638(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.ConfigurationSetAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0032af7abed57412a3e4cb21bdf05c96c4c8d5c6176a0fce6a2c461dbb5af5d8(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.DkimAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__465a3dad3389da07777bdda5eb33e345536e854073c4b594e089dcd18dc12c5b(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.DkimSigningAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0a601ac2f79b10ccfae6354e861623ca5b230f127792ee0f9473a78ac29db37d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.FeedbackAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3bfc642d317ef43c146d5f2aed5754d7210e533815ccd7d6339a4f0946d9ad7c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnEmailIdentity.MailFromAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f43c178a47220933c21060d38f5105353a7af12378df167bc4dc7fca0fffa09c(
    *,
    configuration_set_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b7e4c6c543bf26936e4c81fcb8702db27a3007ffd82e4712715e42011c5c1573(
    *,
    signing_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fc9546dbbff56dcd597c3802b6ffb4259c44e6f78bb7195f924f2ee9ae6fc0a3(
    *,
    domain_signing_private_key: typing.Optional[builtins.str] = None,
    domain_signing_selector: typing.Optional[builtins.str] = None,
    next_signing_key_length: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed64b7518613c037c1bda6f3af605613ea5857d02ec6233dbc9bb1eb38581b8c(
    *,
    email_forwarding_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__172959be1e69fff5bd9bf8f0d9d248c8bcc08b8792f68376cb22ae4849263082(
    *,
    behavior_on_mx_failure: typing.Optional[builtins.str] = None,
    mail_from_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1981630fc48db9c9ef7ed37311c6a22c4456e2d316420d87e0ba41890a323f54(
    *,
    email_identity: builtins.str,
    configuration_set_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.ConfigurationSetAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dkim_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.DkimAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    dkim_signing_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.DkimSigningAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    feedback_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.FeedbackAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    mail_from_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnEmailIdentity.MailFromAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a1615f3821db38c2d17213d45f5aaf7419e2ac2a387e68854a97ab1b660aa82(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptFilter.FilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__68a616fc9bd0bc8eef7e85693c8a2bc90546b0b7c578a2cb94a4f7fa8c67f519(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1149bfa381ad182958c44071a0ae46750ca96fdf6137ff9e951ac1be17625bb1(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3f3559694a52690944f1517571fda28128591a08e4458775af6322f62533e068(
    value: typing.Union[_IResolvable_da3f097b, CfnReceiptFilter.FilterProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a42218c982fb4338e6794b2fe9415b047ee10364d513a6dd4d4f68d79950fb97(
    *,
    ip_filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptFilter.IpFilterProperty, typing.Dict[builtins.str, typing.Any]]],
    name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a491d6597c852f28ae26e9b6690598de1ef3f7a5ee8865818d9104b055030f97(
    *,
    cidr: builtins.str,
    policy: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0c3aafa7b21eb24b6b09cf371f4935926a3d6310d168a5ca16bcad331d2d6a1f(
    *,
    filter: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptFilter.FilterProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f11dbb9bc20b6ae8f4dbfe7500db6c36368680fbb7f5b0198623b727ca3fe253(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_set_name: builtins.str,
    after: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0cc6c8bd23ccd04352f140aa0292c18970d3c08ee118a8a3b0fdf3f9d4ca1a77(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__94942bbf4a200e9bab75fe3f2144c540718074bf55275f72234642a257755afa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e2b7e7d80f05bbed4301e74bf1978bd0403bb680b80c53091fbc2d73a2feb77c(
    value: typing.Union[_IResolvable_da3f097b, CfnReceiptRule.RuleProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a32508b7af75c5c3090736f7c37dc05f9a14f28535c005a911e735e4bf7360d9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7e01f4460f2e7da87350c32dda6e4b23e8e3064fa60b2167f2ef07c44203cf85(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2e23836e118e42c034b0eb896988a7fe715dbbacb7c1a69f5eabb3a0a74e54f3(
    *,
    add_header_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.AddHeaderActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    bounce_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.BounceActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    lambda_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.LambdaActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    s3_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.S3ActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    sns_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.SNSActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    stop_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.StopActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    workmail_action: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.WorkmailActionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a5686953122507299501d79da819371b0b28543d8d5b2e65f1ce0521437dedb(
    *,
    header_name: builtins.str,
    header_value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4b06ec88c0d55564d050fb3ddbd619284526dd4ec4bb0b1de97a62e89e1bbc82(
    *,
    message: builtins.str,
    sender: builtins.str,
    smtp_reply_code: builtins.str,
    status_code: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e86c072abf438c4f550f87a4bbdea46bb58e82f5fe5547fafb68649041ba546f(
    *,
    function_arn: builtins.str,
    invocation_type: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__597a4926fee926f01951cda574fa9265912d5bc1c5bf1e98c3410d25dd232a03(
    *,
    actions: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.ActionProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    tls_policy: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__39d61a089bfe9f0df546774b89ce5903a571f298fca9c95b6767da42860a40aa(
    *,
    bucket_name: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
    object_key_prefix: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7b69991ab1bae6b3b263f1a32cdb917531b7939f873cf674e3a6f502dac1460(
    *,
    encoding: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__929ccdfb2c00fb70aa707e5c7a40fde32e556e0f220a13e8231bbacd2653b8a4(
    *,
    scope: builtins.str,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af2dae7f39846f3f50114d44fa542e8b0390a51e98f63405b5a32de3f95af669(
    *,
    organization_arn: builtins.str,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__aab91d8adb8d443158cc46ba99ec820f62513cdec0b436079652f454fb21cfd1(
    *,
    rule: typing.Union[_IResolvable_da3f097b, typing.Union[CfnReceiptRule.RuleProperty, typing.Dict[builtins.str, typing.Any]]],
    rule_set_name: builtins.str,
    after: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c8e8c05ea09aa8fb4e787d2e45cbe7d16eaf164f24c154797b3e350dd0b5316c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule_set_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7c30f7f0ed5cc61e57a58c5fb1de4ed0806ee6c9530ac2ce5ec04192a40fadbb(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__45b28225e64d365acc2eb75263d1547441c57ed192fa484b706bcc0a87784fb8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7df684309baff9de02a1535483083992de84a7e4b7e34279f0dd37bd4bb1fcb(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea296ac8e1ca4779dc1c9f1d5d572e1ae5dd8506ecf9694e2fb73b514ae26636(
    *,
    rule_set_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4c2a147151a6167a3d150f74c144fd60570fc7ac0777706d24a8e9f23813a8d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d39d28f6ac0b8cfc4db621cda159b70e8ee1c7d0086afcb587c1b723beed970a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9fff6f1c96944fa0c793bff8f36a0f674d1885a636bfa82f985a29ba0ee07623(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dfedec4ff1cee818b04e3b27b75fd775d9a21039cce2bb50f0eee75bbe3b7d0c(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnTemplate.TemplateProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6894407236d481fe73e1d7b05b61377a9e1a2ea9e6ee4bfaa48a81bd5fb84352(
    *,
    subject_part: builtins.str,
    html_part: typing.Optional[builtins.str] = None,
    template_name: typing.Optional[builtins.str] = None,
    text_part: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6fbf4906a406135dc7de9d65c40076a5a27ccfef54ca9df5243bcf8ef9349317(
    *,
    template: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnTemplate.TemplateProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8da690d721f4dc54f54ac8a93b1521ab4f1dbb885e7ddaa381dfa79dcb6e469f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dashboard_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVdmAttributes.DashboardAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    guardian_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVdmAttributes.GuardianAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__19e20bbedca430ef6dc1634692c0b7c55c20f1fdf5542edb402f0e0b5bb364c7(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e60b0b9db028ea74a1508c4ca53cf07d947a35c08e25b8bd2e6c491ef82c63(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d6de577b4b973e97e1a4f2e820f91d3de6f0608ab40978d3d66537a9fc470544(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVdmAttributes.DashboardAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d777849ef648598e745e2dd5179eb670b0345a6656279e557481001d8bfa0419(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnVdmAttributes.GuardianAttributesProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7bb318ca7ff1c3e34c0a31904f95354c80864527eeb292bf9db6ea3ac8dab61c(
    *,
    engagement_metrics: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c129497041cde369dd20c917699582d68e5a27620a3bdb6da3a7048e743a3cdf(
    *,
    optimized_shared_delivery: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05720eed835713353d777877a75758a4e172dae5b79690ea107edcb7cf1e4825(
    *,
    dashboard_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVdmAttributes.DashboardAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    guardian_attributes: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnVdmAttributes.GuardianAttributesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c718e80d3dd746209ff12fd14d08ce529bed18f85e0af362c1a2df8b5adc173a(
    *,
    default_value: builtins.str,
    name: builtins.str,
    source: CloudWatchDimensionSource,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80b5162c2d2ea9081e7450a4b5db43212eaf82f433a217fb2be6e012977034b6(
    *,
    destination: EventDestination,
    configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    events: typing.Optional[typing.Sequence[EmailSendingEvent]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd3ac4f1af1f2fe9c11fa8894b2eae0f4b13c464b826cffda8b6937f4ab3e9c8(
    *,
    destination: EventDestination,
    configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    events: typing.Optional[typing.Sequence[EmailSendingEvent]] = None,
    configuration_set: IConfigurationSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb010161f6c1e40b88122d9cb7754dae093e9cbe5bbfc72b19737729a4f4523d(
    *,
    configuration_set_name: typing.Optional[builtins.str] = None,
    custom_tracking_redirect_domain: typing.Optional[builtins.str] = None,
    dedicated_ip_pool: typing.Optional[IDedicatedIpPool] = None,
    reputation_metrics: typing.Optional[builtins.bool] = None,
    sending_enabled: typing.Optional[builtins.bool] = None,
    suppression_reasons: typing.Optional[SuppressionReasons] = None,
    tls_policy: typing.Optional[ConfigurationSetTlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cbbd68e1fe68b915968886e4089439bf017848bb3c0f82036ac33e6a6de46dd0(
    *,
    dedicated_ip_pool_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__994835eb6fc73d3a1816da5c4409a2dda8bf60416433ec82d3c77e1b7f8801bc(
    signing_key_length: typing.Optional[EasyDkimSigningKeyLength] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9b2a9a4d5a04b9eb8c5081160726f10e62e8072c32851a0ec47dc874a5ecd6db(
    email_identity: EmailIdentity,
    hosted_zone: typing.Optional[_IPublicHostedZone_9b6e7da4] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a12b15597f5468ef7ba7f763da92c48506401bbeba665c431a78482dcb24b3bb(
    *,
    domain_signing_private_key: typing.Optional[builtins.str] = None,
    domain_signing_selector: typing.Optional[builtins.str] = None,
    next_signing_key_length: typing.Optional[EasyDkimSigningKeyLength] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8446e7095e52fceeeac69f7c1807060cf3465e09ec2b3af84028d1df922471e6(
    *,
    name: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__620f8d2305a209eeebb24bd2358ba969bde0f80c50a46c3fa91e56d814fa6152(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule_set: IReceiptRuleSet,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53e1ee2f3b565a95ed952bf4ad2ae80cb7388ac4bd51d6eab5219f8a733ca030(
    *,
    identity: Identity,
    configuration_set: typing.Optional[IConfigurationSet] = None,
    dkim_identity: typing.Optional[DkimIdentity] = None,
    dkim_signing: typing.Optional[builtins.bool] = None,
    feedback_forwarding: typing.Optional[builtins.bool] = None,
    mail_from_behavior_on_mx_failure: typing.Optional[MailFromBehaviorOnMxFailure] = None,
    mail_from_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48f9cce8b82649ed9874f37f0ed571721b324063ca98764a07bb10a451e9fe92(
    dimensions: typing.Sequence[typing.Union[CloudWatchDimension, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70dbe9528b7fbaa2cbed5b1def55a8c3126fbfed3ee256b878bbb907e4585c9c(
    topic: _ITopic_9eca4852,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c0b08f3a2fda3c68a4ad951604e55664aeae1537b8b8eb996f95b6feedcf9b5(
    receipt_rule: IReceiptRule,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__122fb3fdbd3a8f500e0f61c3d2533bd2f3c984f5adc4220663c7c60a5e6cad15(
    id: builtins.str,
    *,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__694ee3f881b596f644bf78eec0110a1de21fa0968b51aac198d16dc4300152a5(
    domain: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c4cd96b179380c844d33e1c8146fdcd73dda4442d8f15d6ec14f0d13964631f6(
    email: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0eb32adc3b9ec102b9a239f5273e26b9dc183e06c2e841a07bb8e8865f65d776(
    hosted_zone: _IPublicHostedZone_9b6e7da4,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2c5bf3251571f8d55618125a7248ae05fc227e5f493642b4ff5f700dfa8105fa(
    *,
    function_arn: builtins.str,
    invocation_type: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__be1bedd2ed98e8b9a5eafff592b3be89e41244d9b42293f0924022a7f27a537f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    ip: typing.Optional[builtins.str] = None,
    policy: typing.Optional[ReceiptFilterPolicy] = None,
    receipt_filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__14330b86b5842b62205be575cd211ebe283567b16984be282e6ee5085d7777ce(
    *,
    ip: typing.Optional[builtins.str] = None,
    policy: typing.Optional[ReceiptFilterPolicy] = None,
    receipt_filter_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a6538ae0354b52c95d3f59e885aa37e670088031cd04d3731f535129e11231d3(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    rule_set: IReceiptRuleSet,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a2938a672425842bfae972477b62457f138b21842405c6d5cb21988892d92c7c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    receipt_rule_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e53269c4ea365e8ad5ea79b458ec9a4cd161a16b84e0de7f577a755251624a6b(
    action: IReceiptRuleAction,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e54c86543028b77ffed9d64cfee35a01463cb4a33a112de436e67beaf2b9608c(
    *,
    add_header_action: typing.Optional[typing.Union[AddHeaderActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    bounce_action: typing.Optional[typing.Union[BounceActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    lambda_action: typing.Optional[typing.Union[LambdaActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    s3_action: typing.Optional[typing.Union[S3ActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    sns_action: typing.Optional[typing.Union[SNSActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    stop_action: typing.Optional[typing.Union[StopActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
    workmail_action: typing.Optional[typing.Union[WorkmailActionConfig, typing.Dict[builtins.str, typing.Any]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__699a2986fda0df5077b1242432999d4d4b894d3e4dd15df070152fae49160eab(
    *,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b6d8cc8ec3dfcf989e29bcbab39380e799bee428bb33c1fe79ab53debbc056b(
    *,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
    rule_set: IReceiptRuleSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e30edd88543242272f6bbc66d4c1125786ce1237720d89b577e253760eb28e2a(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    drop_spam: typing.Optional[builtins.bool] = None,
    receipt_rule_set_name: typing.Optional[builtins.str] = None,
    rules: typing.Optional[typing.Sequence[typing.Union[ReceiptRuleOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb544e652efede317fbc4b71b8f4c7e7ac6549e66fa70957106d0835bd174832(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    receipt_rule_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8cd532ef11b279fc4ddb81d21e2fd9962d1cc828cc92e5f4985bb2451030ca3a(
    id: builtins.str,
    *,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1cc19b30dc991a483fd278ee500d3d3e57d7a5a9ff95850a924babd266fac0fe(
    *,
    drop_spam: typing.Optional[builtins.bool] = None,
    receipt_rule_set_name: typing.Optional[builtins.str] = None,
    rules: typing.Optional[typing.Sequence[typing.Union[ReceiptRuleOptions, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ef118e7dd1d569a24b4ab4f36d8ac563d485f357ed7b48efc12c802a2b6b2182(
    *,
    bucket_name: builtins.str,
    kms_key_arn: typing.Optional[builtins.str] = None,
    object_key_prefix: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__173bb322225263bb156456dc72b3d2b251f55cd39ef1474dc97211e5e41f07af(
    *,
    encoding: typing.Optional[builtins.str] = None,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d7e81c4cd24879569e0bdfa8c28a29714bdb254ca09f291cf53f0fddd448e9fc(
    *,
    scope: builtins.str,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e90b2ec586dfbf0314232aaea6d64cdd5816072b0bcfed076d517ff63a3b1000(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    engagement_metrics: typing.Optional[builtins.bool] = None,
    optimized_shared_delivery: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c4f2d4b83707480c9a8afc395f18812d02a2c5e0fc50cd63f1eb9d708176325(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    vdm_attributes_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1882e9d1289b07868b3ffcfb9d92629e699992b01e6475750adbffc0137815b0(
    *,
    engagement_metrics: typing.Optional[builtins.bool] = None,
    optimized_shared_delivery: typing.Optional[builtins.bool] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08a56aa5b57fd1699d7c92c360d0709a2cfb31d3cb323b992c4b4e89432c836b(
    *,
    organization_arn: builtins.str,
    topic_arn: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__52b42851a408d3eb2b07399f2b34603200cef443be5e9f913f4a1d80a47ac83e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_set_name: typing.Optional[builtins.str] = None,
    custom_tracking_redirect_domain: typing.Optional[builtins.str] = None,
    dedicated_ip_pool: typing.Optional[IDedicatedIpPool] = None,
    reputation_metrics: typing.Optional[builtins.bool] = None,
    sending_enabled: typing.Optional[builtins.bool] = None,
    suppression_reasons: typing.Optional[SuppressionReasons] = None,
    tls_policy: typing.Optional[ConfigurationSetTlsPolicy] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2ae99096d05b68163763ffbed7aafa034cd3a774f632bff2370d017f76194045(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    configuration_set_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__969c3bbc0e7891ce9eb910e67644f0f9bcb29f65f5ec021df94eed425cb0d707(
    id: builtins.str,
    *,
    destination: EventDestination,
    configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    events: typing.Optional[typing.Sequence[EmailSendingEvent]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cf213dc05e866bbe3e9422388bafa084e54ef674803fa10657e5b96b908d6965(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    configuration_set: IConfigurationSet,
    destination: EventDestination,
    configuration_set_event_destination_name: typing.Optional[builtins.str] = None,
    enabled: typing.Optional[builtins.bool] = None,
    events: typing.Optional[typing.Sequence[EmailSendingEvent]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4740349c6047d2ad783d767c6424ac19156d882d3534207b1440beda62370433(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    configuration_set_event_destination_id: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a4f168ec9aad173d023a8ac330a62f7c1ce87601f0a8876e8cbf35c7dcd89ead(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    dedicated_ip_pool_name: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6d620bd493f43394b0479d58a02acf7d3c1644c63cc64fc186abe29e763516bf(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    dedicated_ip_pool_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f78c7c8898fbe6486ab42279bd1b1abce1f0305e2d0cc19d79400e08c909951f(
    *,
    actions: typing.Optional[typing.Sequence[IReceiptRuleAction]] = None,
    after: typing.Optional[IReceiptRule] = None,
    enabled: typing.Optional[builtins.bool] = None,
    receipt_rule_name: typing.Optional[builtins.str] = None,
    recipients: typing.Optional[typing.Sequence[builtins.str]] = None,
    scan_enabled: typing.Optional[builtins.bool] = None,
    tls_policy: typing.Optional[TlsPolicy] = None,
    rule_set: IReceiptRuleSet,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0d44bf733be67b29d51a6c681c3faafee6103884474147b68d4b466a07017e9(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    identity: Identity,
    configuration_set: typing.Optional[IConfigurationSet] = None,
    dkim_identity: typing.Optional[DkimIdentity] = None,
    dkim_signing: typing.Optional[builtins.bool] = None,
    feedback_forwarding: typing.Optional[builtins.bool] = None,
    mail_from_behavior_on_mx_failure: typing.Optional[MailFromBehaviorOnMxFailure] = None,
    mail_from_domain: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eb1cb50e69249e3f61387a80db0e14cc9a9790c024548390466a511484409a85(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    email_identity_name: builtins.str,
) -> None:
    """Type checking stubs"""
    pass
