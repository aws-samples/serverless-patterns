'''
# AWS::Shield Construct Library

<!--BEGIN STABILITY BANNER-->---


![cfn-resources: Stable](https://img.shields.io/badge/cfn--resources-stable-success.svg?style=for-the-badge)

> All classes with the `Cfn` prefix in this module ([CFN Resources](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) are always stable and safe to use.

---
<!--END STABILITY BANNER-->

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_shield as shield
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Shield construct libraries](https://constructs.dev/search?q=shield)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Shield resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Shield.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Shield](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Shield.html).

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
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnDRTAccess(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_shield.CfnDRTAccess",
):
    '''Provides permissions for the AWS Shield Advanced Shield response team (SRT) to access your account and your resource protections, to help you mitigate potential distributed denial of service (DDoS) attacks.

    .. epigraph::

       To configure this resource through AWS CloudFormation , you must be subscribed to AWS Shield Advanced . You can subscribe through the `Shield Advanced console <https://docs.aws.amazon.com/wafv2/shieldv2#/>`_ and through the APIs. For more information, see `Subscribe to AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html>`_ .

    See example templates for Shield Advanced in AWS CloudFormation at `aws-samples/aws-shield-advanced-examples <https://docs.aws.amazon.com/https://github.com/aws-samples/aws-shield-advanced-examples>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_shield as shield
        
        cfn_dRTAccess = shield.CfnDRTAccess(self, "MyCfnDRTAccess",
            role_arn="roleArn",
        
            # the properties below are optional
            log_bucket_list=["logBucketList"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        role_arn: builtins.str,
        log_bucket_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param role_arn: Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your AWS WAF configuration and logs and to create or update AWS WAF rules and web ACLs. You can associate only one ``RoleArn`` with your subscription. If you submit this update for an account that already has an associated role, the new ``RoleArn`` will replace the existing ``RoleArn`` . This change requires the following: - You must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ . - You must have the ``iam:PassRole`` permission. For more information, see `Granting a user permissions to pass a role to an AWS service <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`_ . - The ``AWSShieldDRTAccessPolicy`` managed policy must be attached to the role that you specify in the request. You can access this policy in the IAM console at `AWSShieldDRTAccessPolicy <https://docs.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy>`_ . For information, see `Adding and removing IAM identity permissions <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`_ . - The role must trust the service principal ``drt.shield.amazonaws.com`` . For information, see `IAM JSON policy elements: Principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html>`_ . The SRT will have access only to your AWS WAF and Shield resources. By submitting this request, you provide permissions to the SRT to inspect your AWS WAF and Shield configuration and logs, and to create and update AWS WAF rules and web ACLs on your behalf. The SRT takes these actions only if explicitly authorized by you.
        :param log_bucket_list: Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription. Use this to share information with the SRT that's not available in AWS WAF logs. To use the services of the SRT, you must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ .
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4a15a18e843fffdbb42d47fd2ac911234ec7893d81473ee5d084ecfea8549c95)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnDRTAccessProps(role_arn=role_arn, log_bucket_list=log_bucket_list)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1852e8b6dd2c25fa06e5e566839fd5a1f6a276b8b39e838b2b89482ea513bd65)
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
            type_hints = typing.get_type_hints(_typecheckingstub__8571297b6d69a16de38bab6d3f1dc92d7c9246c66b35f80febffdfb1f3b2e7c8)
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
        '''The ID of the account that submitted the template.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="roleArn")
    def role_arn(self) -> builtins.str:
        '''Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks.'''
        return typing.cast(builtins.str, jsii.get(self, "roleArn"))

    @role_arn.setter
    def role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__da38bba1d6994ae07694944aa4916a03f58a2c9485676c9085e1c314c3f2aa57)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleArn", value)

    @builtins.property
    @jsii.member(jsii_name="logBucketList")
    def log_bucket_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "logBucketList"))

    @log_bucket_list.setter
    def log_bucket_list(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c94abc39b038180b7b7b34ef27ad16e99c54c8cd1ff7e04fd4e4882047910e1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "logBucketList", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_shield.CfnDRTAccessProps",
    jsii_struct_bases=[],
    name_mapping={"role_arn": "roleArn", "log_bucket_list": "logBucketList"},
)
class CfnDRTAccessProps:
    def __init__(
        self,
        *,
        role_arn: builtins.str,
        log_bucket_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnDRTAccess``.

        :param role_arn: Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks. This enables the SRT to inspect your AWS WAF configuration and logs and to create or update AWS WAF rules and web ACLs. You can associate only one ``RoleArn`` with your subscription. If you submit this update for an account that already has an associated role, the new ``RoleArn`` will replace the existing ``RoleArn`` . This change requires the following: - You must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ . - You must have the ``iam:PassRole`` permission. For more information, see `Granting a user permissions to pass a role to an AWS service <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`_ . - The ``AWSShieldDRTAccessPolicy`` managed policy must be attached to the role that you specify in the request. You can access this policy in the IAM console at `AWSShieldDRTAccessPolicy <https://docs.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy>`_ . For information, see `Adding and removing IAM identity permissions <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`_ . - The role must trust the service principal ``drt.shield.amazonaws.com`` . For information, see `IAM JSON policy elements: Principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html>`_ . The SRT will have access only to your AWS WAF and Shield resources. By submitting this request, you provide permissions to the SRT to inspect your AWS WAF and Shield configuration and logs, and to create and update AWS WAF rules and web ACLs on your behalf. The SRT takes these actions only if explicitly authorized by you.
        :param log_bucket_list: Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources. You can associate up to 10 Amazon S3 buckets with your subscription. Use this to share information with the SRT that's not available in AWS WAF logs. To use the services of the SRT, you must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_shield as shield
            
            cfn_dRTAccess_props = shield.CfnDRTAccessProps(
                role_arn="roleArn",
            
                # the properties below are optional
                log_bucket_list=["logBucketList"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7eb7d0e0a686aa5ce41af2859848528d577aa001b693b180bf8c8c1cbe226c62)
            check_type(argname="argument role_arn", value=role_arn, expected_type=type_hints["role_arn"])
            check_type(argname="argument log_bucket_list", value=log_bucket_list, expected_type=type_hints["log_bucket_list"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "role_arn": role_arn,
        }
        if log_bucket_list is not None:
            self._values["log_bucket_list"] = log_bucket_list

    @builtins.property
    def role_arn(self) -> builtins.str:
        '''Authorizes the Shield Response Team (SRT) using the specified role, to access your AWS account to assist with DDoS attack mitigation during potential attacks.

        This enables the SRT to inspect your AWS WAF configuration and logs and to create or update AWS WAF rules and web ACLs.

        You can associate only one ``RoleArn`` with your subscription. If you submit this update for an account that already has an associated role, the new ``RoleArn`` will replace the existing ``RoleArn`` .

        This change requires the following:

        - You must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ .
        - You must have the ``iam:PassRole`` permission. For more information, see `Granting a user permissions to pass a role to an AWS service <https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_passrole.html>`_ .
        - The ``AWSShieldDRTAccessPolicy`` managed policy must be attached to the role that you specify in the request. You can access this policy in the IAM console at `AWSShieldDRTAccessPolicy <https://docs.aws.amazon.com/iam/home?#/policies/arn:aws:iam::aws:policy/service-role/AWSShieldDRTAccessPolicy>`_ . For information, see `Adding and removing IAM identity permissions <https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html>`_ .
        - The role must trust the service principal ``drt.shield.amazonaws.com`` . For information, see `IAM JSON policy elements: Principal <https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html>`_ .

        The SRT will have access only to your AWS WAF and Shield resources. By submitting this request, you provide permissions to the SRT to inspect your AWS WAF and Shield configuration and logs, and to create and update AWS WAF rules and web ACLs on your behalf. The SRT takes these actions only if explicitly authorized by you.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html#cfn-shield-drtaccess-rolearn
        '''
        result = self._values.get("role_arn")
        assert result is not None, "Required property 'role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def log_bucket_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Authorizes the Shield Response Team (SRT) to access the specified Amazon S3 bucket containing log data such as Application Load Balancer access logs, CloudFront logs, or logs from third party sources.

        You can associate up to 10 Amazon S3 buckets with your subscription.

        Use this to share information with the SRT that's not available in AWS WAF logs.

        To use the services of the SRT, you must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-drtaccess.html#cfn-shield-drtaccess-logbucketlist
        '''
        result = self._values.get("log_bucket_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnDRTAccessProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProactiveEngagement(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_shield.CfnProactiveEngagement",
):
    '''Authorizes the Shield Response Team (SRT) to use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.

    To enable proactive engagement, you must be subscribed to the `Business Support plan <https://docs.aws.amazon.com/premiumsupport/business-support/>`_ or the `Enterprise Support plan <https://docs.aws.amazon.com/premiumsupport/enterprise-support/>`_ .
    .. epigraph::

       To configure this resource through AWS CloudFormation , you must be subscribed to AWS Shield Advanced . You can subscribe through the `Shield Advanced console <https://docs.aws.amazon.com/wafv2/shieldv2#/>`_ and through the APIs. For more information, see `Subscribe to AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html>`_ .

    See example templates for Shield Advanced in AWS CloudFormation at `aws-samples/aws-shield-advanced-examples <https://docs.aws.amazon.com/https://github.com/aws-samples/aws-shield-advanced-examples>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_shield as shield
        
        cfn_proactive_engagement = shield.CfnProactiveEngagement(self, "MyCfnProactiveEngagement",
            emergency_contact_list=[shield.CfnProactiveEngagement.EmergencyContactProperty(
                email_address="emailAddress",
        
                # the properties below are optional
                contact_notes="contactNotes",
                phone_number="phoneNumber"
            )],
            proactive_engagement_status="proactiveEngagementStatus"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        emergency_contact_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProactiveEngagement.EmergencyContactProperty", typing.Dict[builtins.str, typing.Any]]]]],
        proactive_engagement_status: builtins.str,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param emergency_contact_list: The list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support, plus any relevant notes. To enable proactive engagement, the contact list must include at least one phone number. If you provide more than one contact, in the notes, indicate the circumstances under which each contact should be used. Include primary and secondary contact designations, and provide the hours of availability and time zones for each contact. Example contact notes: - This is a hotline that's staffed 24x7x365. Please work with the responding analyst and they will get the appropriate person on the call. - Please contact the secondary phone number if the hotline doesn't respond within 5 minutes.
        :param proactive_engagement_status: Specifies whether proactive engagement is enabled or disabled. Valid values: ``ENABLED`` - The Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support. ``DISABLED`` - The SRT will not proactively notify contacts about escalations or to initiate proactive customer support.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__75179b0b2a7390cfe8ff254cdce98b24f9e580040dddc66ad43b122c2b5e0c6d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProactiveEngagementProps(
            emergency_contact_list=emergency_contact_list,
            proactive_engagement_status=proactive_engagement_status,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d5a960f62ca304b7ebcf5e14298d60f742a16d5dbaf6f97f912470ede285d11e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__99229a0794c4f40e520680e633fa758c86f0b7d6e14e7081dd03b9a42c242a63)
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
        '''The ID of the account that submitted the template.

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="emergencyContactList")
    def emergency_contact_list(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProactiveEngagement.EmergencyContactProperty"]]]:
        '''The list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support, plus any relevant notes.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProactiveEngagement.EmergencyContactProperty"]]], jsii.get(self, "emergencyContactList"))

    @emergency_contact_list.setter
    def emergency_contact_list(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnProactiveEngagement.EmergencyContactProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__124fcf35e2a271c8af4d75b0cf5014b8ad1239720905927de40e52915ba3e15c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "emergencyContactList", value)

    @builtins.property
    @jsii.member(jsii_name="proactiveEngagementStatus")
    def proactive_engagement_status(self) -> builtins.str:
        '''Specifies whether proactive engagement is enabled or disabled.'''
        return typing.cast(builtins.str, jsii.get(self, "proactiveEngagementStatus"))

    @proactive_engagement_status.setter
    def proactive_engagement_status(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b037bb753d3225b693b8d381833edd00f55da5f9159d4af431e1e597b718015)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "proactiveEngagementStatus", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_shield.CfnProactiveEngagement.EmergencyContactProperty",
        jsii_struct_bases=[],
        name_mapping={
            "email_address": "emailAddress",
            "contact_notes": "contactNotes",
            "phone_number": "phoneNumber",
        },
    )
    class EmergencyContactProperty:
        def __init__(
            self,
            *,
            email_address: builtins.str,
            contact_notes: typing.Optional[builtins.str] = None,
            phone_number: typing.Optional[builtins.str] = None,
        ) -> None:
            '''Contact information that the SRT can use to contact you if you have proactive engagement enabled, for escalations to the SRT and to initiate proactive customer support.

            :param email_address: The email address for the contact.
            :param contact_notes: Additional notes regarding the contact.
            :param phone_number: The phone number for the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_shield as shield
                
                emergency_contact_property = shield.CfnProactiveEngagement.EmergencyContactProperty(
                    email_address="emailAddress",
                
                    # the properties below are optional
                    contact_notes="contactNotes",
                    phone_number="phoneNumber"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__943f9798df53d53e30978210d183db122bb3f1df5ce07ae3b7aaa70f1002896d)
                check_type(argname="argument email_address", value=email_address, expected_type=type_hints["email_address"])
                check_type(argname="argument contact_notes", value=contact_notes, expected_type=type_hints["contact_notes"])
                check_type(argname="argument phone_number", value=phone_number, expected_type=type_hints["phone_number"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "email_address": email_address,
            }
            if contact_notes is not None:
                self._values["contact_notes"] = contact_notes
            if phone_number is not None:
                self._values["phone_number"] = phone_number

        @builtins.property
        def email_address(self) -> builtins.str:
            '''The email address for the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html#cfn-shield-proactiveengagement-emergencycontact-emailaddress
            '''
            result = self._values.get("email_address")
            assert result is not None, "Required property 'email_address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def contact_notes(self) -> typing.Optional[builtins.str]:
            '''Additional notes regarding the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html#cfn-shield-proactiveengagement-emergencycontact-contactnotes
            '''
            result = self._values.get("contact_notes")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def phone_number(self) -> typing.Optional[builtins.str]:
            '''The phone number for the contact.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-proactiveengagement-emergencycontact.html#cfn-shield-proactiveengagement-emergencycontact-phonenumber
            '''
            result = self._values.get("phone_number")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "EmergencyContactProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_shield.CfnProactiveEngagementProps",
    jsii_struct_bases=[],
    name_mapping={
        "emergency_contact_list": "emergencyContactList",
        "proactive_engagement_status": "proactiveEngagementStatus",
    },
)
class CfnProactiveEngagementProps:
    def __init__(
        self,
        *,
        emergency_contact_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProactiveEngagement.EmergencyContactProperty, typing.Dict[builtins.str, typing.Any]]]]],
        proactive_engagement_status: builtins.str,
    ) -> None:
        '''Properties for defining a ``CfnProactiveEngagement``.

        :param emergency_contact_list: The list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support, plus any relevant notes. To enable proactive engagement, the contact list must include at least one phone number. If you provide more than one contact, in the notes, indicate the circumstances under which each contact should be used. Include primary and secondary contact designations, and provide the hours of availability and time zones for each contact. Example contact notes: - This is a hotline that's staffed 24x7x365. Please work with the responding analyst and they will get the appropriate person on the call. - Please contact the secondary phone number if the hotline doesn't respond within 5 minutes.
        :param proactive_engagement_status: Specifies whether proactive engagement is enabled or disabled. Valid values: ``ENABLED`` - The Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support. ``DISABLED`` - The SRT will not proactively notify contacts about escalations or to initiate proactive customer support.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_shield as shield
            
            cfn_proactive_engagement_props = shield.CfnProactiveEngagementProps(
                emergency_contact_list=[shield.CfnProactiveEngagement.EmergencyContactProperty(
                    email_address="emailAddress",
            
                    # the properties below are optional
                    contact_notes="contactNotes",
                    phone_number="phoneNumber"
                )],
                proactive_engagement_status="proactiveEngagementStatus"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a87e22725ebed99038c7fbf64e1b444b667784de63c1c0f1d6dd1233d0655684)
            check_type(argname="argument emergency_contact_list", value=emergency_contact_list, expected_type=type_hints["emergency_contact_list"])
            check_type(argname="argument proactive_engagement_status", value=proactive_engagement_status, expected_type=type_hints["proactive_engagement_status"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "emergency_contact_list": emergency_contact_list,
            "proactive_engagement_status": proactive_engagement_status,
        }

    @builtins.property
    def emergency_contact_list(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProactiveEngagement.EmergencyContactProperty]]]:
        '''The list of email addresses and phone numbers that the Shield Response Team (SRT) can use to contact you for escalations to the SRT and to initiate proactive customer support, plus any relevant notes.

        To enable proactive engagement, the contact list must include at least one phone number.

        If you provide more than one contact, in the notes, indicate the circumstances under which each contact should be used. Include primary and secondary contact designations, and provide the hours of availability and time zones for each contact.

        Example contact notes:

        - This is a hotline that's staffed 24x7x365. Please work with the responding analyst and they will get the appropriate person on the call.
        - Please contact the secondary phone number if the hotline doesn't respond within 5 minutes.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html#cfn-shield-proactiveengagement-emergencycontactlist
        '''
        result = self._values.get("emergency_contact_list")
        assert result is not None, "Required property 'emergency_contact_list' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProactiveEngagement.EmergencyContactProperty]]], result)

    @builtins.property
    def proactive_engagement_status(self) -> builtins.str:
        '''Specifies whether proactive engagement is enabled or disabled.

        Valid values:

        ``ENABLED`` - The Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.

        ``DISABLED`` - The SRT will not proactively notify contacts about escalations or to initiate proactive customer support.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-proactiveengagement.html#cfn-shield-proactiveengagement-proactiveengagementstatus
        '''
        result = self._values.get("proactive_engagement_status")
        assert result is not None, "Required property 'proactive_engagement_status' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProactiveEngagementProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnProtection(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_shield.CfnProtection",
):
    '''Enables AWS Shield Advanced for a specific AWS resource.

    The resource can be an Amazon CloudFront distribution, Amazon Route 53 hosted zone, AWS Global Accelerator standard accelerator, Elastic IP Address, Application Load Balancer, or a Classic Load Balancer. You can protect Amazon EC2 instances and Network Load Balancers by association with protected Amazon EC2 Elastic IP addresses.

    Use this to add protection to a single resource at a time. You can add protection to multiple resources at once through the `Shield Advanced console <https://docs.aws.amazon.com/wafv2/shieldv2#/>`_ . For more information see `Getting Started with AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/getting-started-ddos.html>`_ and `Managing resource protections in AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-manage-protected-resources.html>`_ .
    .. epigraph::

       To configure this resource through AWS CloudFormation , you must be subscribed to AWS Shield Advanced . You can subscribe through the `Shield Advanced console <https://docs.aws.amazon.com/wafv2/shieldv2#/>`_ and through the APIs. For more information, see `Subscribe to AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html>`_ .

    See example templates for Shield Advanced in AWS CloudFormation at `aws-samples/aws-shield-advanced-examples <https://docs.aws.amazon.com/https://github.com/aws-samples/aws-shield-advanced-examples>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_shield as shield
        
        # block: Any
        # count: Any
        
        cfn_protection = shield.CfnProtection(self, "MyCfnProtection",
            name="name",
            resource_arn="resourceArn",
        
            # the properties below are optional
            application_layer_automatic_response_configuration=shield.CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty(
                action=shield.CfnProtection.ActionProperty(
                    block=block,
                    count=count
                ),
                status="status"
            ),
            health_check_arns=["healthCheckArns"],
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
        resource_arn: builtins.str,
        application_layer_automatic_response_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        health_check_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of the protection. For example, ``My CloudFront distributions`` . .. epigraph:: If you change the name of an existing protection, Shield Advanced deletes the protection and replaces it with a new one. While this is happening, the protection isn't available on the AWS resource.
        :param resource_arn: The ARN (Amazon Resource Name) of the AWS resource that is protected.
        :param application_layer_automatic_response_configuration: The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.
        :param health_check_arns: The ARN (Amazon Resource Name) of the health check to associate with the protection. Health-based detection provides improved responsiveness and accuracy in attack detection and mitigation. You can use this option with any resource type except for Route 53 hosted zones. For more information, see `Configuring health-based detection using health checks <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-health-checks.html>`_ in the *AWS Shield Advanced Developer Guide* .
        :param tags: Key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c25ea3f87ade4afdbc73b2ca70b15ee669920a1fb5f0ed5803cfd112c3b70c11)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProtectionProps(
            name=name,
            resource_arn=resource_arn,
            application_layer_automatic_response_configuration=application_layer_automatic_response_configuration,
            health_check_arns=health_check_arns,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c6d6fd37913379ec3a2749bbbf52fd1927d9c61ec30884700bdad09f41bd423a)
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
            type_hints = typing.get_type_hints(_typecheckingstub__66cc1b7316da30a5a6580d88917c556d71192a4c006b273660d5ad02f215814e)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProtectionArn")
    def attr_protection_arn(self) -> builtins.str:
        '''The ARN (Amazon Resource Name) of the new protection.

        :cloudformationAttribute: ProtectionArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProtectionArn"))

    @builtins.property
    @jsii.member(jsii_name="attrProtectionId")
    def attr_protection_id(self) -> builtins.str:
        '''The ID of the new protection.

        :cloudformationAttribute: ProtectionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProtectionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the protection.

        For example, ``My CloudFront distributions`` .
        '''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f664fe46f1fe6ac65c7f4d1ffc5b08a87c78645927fdd0533b7477ee11e1f0e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="resourceArn")
    def resource_arn(self) -> builtins.str:
        '''The ARN (Amazon Resource Name) of the AWS resource that is protected.'''
        return typing.cast(builtins.str, jsii.get(self, "resourceArn"))

    @resource_arn.setter
    def resource_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c90c79a0e936546060dcc8c586dd2be6cd6ff32840ad1e49333ef28864e5dfa0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceArn", value)

    @builtins.property
    @jsii.member(jsii_name="applicationLayerAutomaticResponseConfiguration")
    def application_layer_automatic_response_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty"]]:
        '''The automatic application layer DDoS mitigation settings for the protection.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty"]], jsii.get(self, "applicationLayerAutomaticResponseConfiguration"))

    @application_layer_automatic_response_configuration.setter
    def application_layer_automatic_response_configuration(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__145ac68c42ad419925aa32644eea217eb08e6ce73993b51c7af4167aab4e13de)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "applicationLayerAutomaticResponseConfiguration", value)

    @builtins.property
    @jsii.member(jsii_name="healthCheckArns")
    def health_check_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN (Amazon Resource Name) of the health check to associate with the protection.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "healthCheckArns"))

    @health_check_arns.setter
    def health_check_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d98b040afae8b4f4d573af557d97a93bdf3dde17bbb8d705e4c6c0d0acc940aa)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "healthCheckArns", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key:value pairs associated with an AWS resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4cd697bbebfdef8296c6fa9e920e70bb9a5ed569b251c351c36b4e3edbdd61e0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_shield.CfnProtection.ActionProperty",
        jsii_struct_bases=[],
        name_mapping={"block": "block", "count": "count"},
    )
    class ActionProperty:
        def __init__(
            self,
            *,
            block: typing.Any = None,
            count: typing.Any = None,
        ) -> None:
            '''Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks.

            You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.

            :param block: Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF ``Block`` action. You must specify exactly one action, either ``Block`` or ``Count`` . Example JSON: ``{ "Block": {} }`` Example YAML: ``Block: {}``
            :param count: Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF ``Count`` action. You must specify exactly one action, either ``Block`` or ``Count`` . Example JSON: ``{ "Count": {} }`` Example YAML: ``Count: {}``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-action.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_shield as shield
                
                # block: Any
                # count: Any
                
                action_property = shield.CfnProtection.ActionProperty(
                    block=block,
                    count=count
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__10ad3bad839bf7f73612fddf37ab7b4b54806b3d7c6601e67b6e355265495610)
                check_type(argname="argument block", value=block, expected_type=type_hints["block"])
                check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if block is not None:
                self._values["block"] = block
            if count is not None:
                self._values["count"] = count

        @builtins.property
        def block(self) -> typing.Any:
            '''Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF ``Block`` action.

            You must specify exactly one action, either ``Block`` or ``Count`` .

            Example JSON: ``{ "Block": {} }``

            Example YAML: ``Block: {}``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-action.html#cfn-shield-protection-action-block
            '''
            result = self._values.get("block")
            return typing.cast(typing.Any, result)

        @builtins.property
        def count(self) -> typing.Any:
            '''Specifies that Shield Advanced should configure its AWS WAF rules with the AWS WAF ``Count`` action.

            You must specify exactly one action, either ``Block`` or ``Count`` .

            Example JSON: ``{ "Count": {} }``

            Example YAML: ``Count: {}``

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-action.html#cfn-shield-protection-action-count
            '''
            result = self._values.get("count")
            return typing.cast(typing.Any, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_shield.CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty",
        jsii_struct_bases=[],
        name_mapping={"action": "action", "status": "status"},
    )
    class ApplicationLayerAutomaticResponseConfigurationProperty:
        def __init__(
            self,
            *,
            action: typing.Union[_IResolvable_da3f097b, typing.Union["CfnProtection.ActionProperty", typing.Dict[builtins.str, typing.Any]]],
            status: builtins.str,
        ) -> None:
            '''The automatic application layer DDoS mitigation settings for a ``Protection`` .

            This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.

            :param action: Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.
            :param status: Indicates whether automatic application layer DDoS mitigation is enabled for the protection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_shield as shield
                
                # block: Any
                # count: Any
                
                application_layer_automatic_response_configuration_property = shield.CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty(
                    action=shield.CfnProtection.ActionProperty(
                        block=block,
                        count=count
                    ),
                    status="status"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4bb6af4792edfc92c1e9a35d69e7e3b4dea97cee90b65597ebf1f9e0777df0e2)
                check_type(argname="argument action", value=action, expected_type=type_hints["action"])
                check_type(argname="argument status", value=status, expected_type=type_hints["status"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "action": action,
                "status": status,
            }

        @builtins.property
        def action(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnProtection.ActionProperty"]:
            '''Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks.

            You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-action
            '''
            result = self._values.get("action")
            assert result is not None, "Required property 'action' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnProtection.ActionProperty"], result)

        @builtins.property
        def status(self) -> builtins.str:
            '''Indicates whether automatic application layer DDoS mitigation is enabled for the protection.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-shield-protection-applicationlayerautomaticresponseconfiguration.html#cfn-shield-protection-applicationlayerautomaticresponseconfiguration-status
            '''
            result = self._values.get("status")
            assert result is not None, "Required property 'status' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ApplicationLayerAutomaticResponseConfigurationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.implements(_IInspectable_c2943556)
class CfnProtectionGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_shield.CfnProtectionGroup",
):
    '''Creates a grouping of protected resources so they can be handled as a collective.

    This resource grouping improves the accuracy of detection and reduces false positives.
    .. epigraph::

       To configure this resource through AWS CloudFormation , you must be subscribed to AWS Shield Advanced . You can subscribe through the `Shield Advanced console <https://docs.aws.amazon.com/wafv2/shieldv2#/>`_ and through the APIs. For more information, see `Subscribe to AWS Shield Advanced <https://docs.aws.amazon.com/waf/latest/developerguide/enable-ddos-prem.html>`_ .

    See example templates for Shield Advanced in AWS CloudFormation at `aws-samples/aws-shield-advanced-examples <https://docs.aws.amazon.com/https://github.com/aws-samples/aws-shield-advanced-examples>`_ .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_shield as shield
        
        cfn_protection_group = shield.CfnProtectionGroup(self, "MyCfnProtectionGroup",
            aggregation="aggregation",
            pattern="pattern",
            protection_group_id="protectionGroupId",
        
            # the properties below are optional
            members=["members"],
            resource_type="resourceType",
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
        aggregation: builtins.str,
        pattern: builtins.str,
        protection_group_id: builtins.str,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param aggregation: Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events. - Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically. - Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers. - Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.
        :param pattern: The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource ARNs (Amazon Resource Names), or include all resources of a specified resource type.
        :param protection_group_id: The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
        :param members: The ARNs (Amazon Resource Names) of the resources to include in the protection group. You must set this when you set ``Pattern`` to ``ARBITRARY`` and you must not set it for any other ``Pattern`` setting.
        :param resource_type: The resource type to include in the protection group. All protected resources of this type are included in the protection group. You must set this when you set ``Pattern`` to ``BY_RESOURCE_TYPE`` and you must not set it for any other ``Pattern`` setting.
        :param tags: Key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__81da6ee581209a252a2406d5601c15a1be321e07fcf0aa646c27538a66db638c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnProtectionGroupProps(
            aggregation=aggregation,
            pattern=pattern,
            protection_group_id=protection_group_id,
            members=members,
            resource_type=resource_type,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76b88e310cde3207aac88376ade59343d5e539487019cd87c212616c6a70148e)
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
            type_hints = typing.get_type_hints(_typecheckingstub__db6feff847b2fccbd8fa083c92622d53c9bbea5c28c87fd70765fb2916691df0)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrProtectionGroupArn")
    def attr_protection_group_arn(self) -> builtins.str:
        '''The ARN (Amazon Resource Name) of the new protection group.

        :cloudformationAttribute: ProtectionGroupArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProtectionGroupArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="aggregation")
    def aggregation(self) -> builtins.str:
        '''Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.'''
        return typing.cast(builtins.str, jsii.get(self, "aggregation"))

    @aggregation.setter
    def aggregation(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5ab253e64e58318d6cd6e12bbf34c34aa957e343239b65290d697b1c872f243d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "aggregation", value)

    @builtins.property
    @jsii.member(jsii_name="pattern")
    def pattern(self) -> builtins.str:
        '''The criteria to use to choose the protected resources for inclusion in the group.'''
        return typing.cast(builtins.str, jsii.get(self, "pattern"))

    @pattern.setter
    def pattern(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__dd66def3c643e8068586fab8310be7a0bde4339a08f8f4c532ec845fe6c0181b)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pattern", value)

    @builtins.property
    @jsii.member(jsii_name="protectionGroupId")
    def protection_group_id(self) -> builtins.str:
        '''The name of the protection group.'''
        return typing.cast(builtins.str, jsii.get(self, "protectionGroupId"))

    @protection_group_id.setter
    def protection_group_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__843e37c61fb3edb2d8ae7c8a0c0a7ecfebcef61fe1f6b6bb7543d2d47a7b82c9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "protectionGroupId", value)

    @builtins.property
    @jsii.member(jsii_name="members")
    def members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs (Amazon Resource Names) of the resources to include in the protection group.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "members"))

    @members.setter
    def members(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c886ab822198804e227db899eaedff6f661d9a7e4eab802450270e17742b7115)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "members", value)

    @builtins.property
    @jsii.member(jsii_name="resourceType")
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The resource type to include in the protection group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceType"))

    @resource_type.setter
    def resource_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6e3d5c3c763d27892562b1771a153762a3d34df5cb316c0538590da13f506b36)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceType", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key:value pairs associated with an AWS resource.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tags"))

    @tags.setter
    def tags(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70ea7c7493bdebcbd30035fe4d1550d14d6af25225d32845d78baca96ef59493)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_shield.CfnProtectionGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "aggregation": "aggregation",
        "pattern": "pattern",
        "protection_group_id": "protectionGroupId",
        "members": "members",
        "resource_type": "resourceType",
        "tags": "tags",
    },
)
class CfnProtectionGroupProps:
    def __init__(
        self,
        *,
        aggregation: builtins.str,
        pattern: builtins.str,
        protection_group_id: builtins.str,
        members: typing.Optional[typing.Sequence[builtins.str]] = None,
        resource_type: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProtectionGroup``.

        :param aggregation: Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events. - Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically. - Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers. - Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.
        :param pattern: The criteria to use to choose the protected resources for inclusion in the group. You can include all resources that have protections, provide a list of resource ARNs (Amazon Resource Names), or include all resources of a specified resource type.
        :param protection_group_id: The name of the protection group. You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.
        :param members: The ARNs (Amazon Resource Names) of the resources to include in the protection group. You must set this when you set ``Pattern`` to ``ARBITRARY`` and you must not set it for any other ``Pattern`` setting.
        :param resource_type: The resource type to include in the protection group. All protected resources of this type are included in the protection group. You must set this when you set ``Pattern`` to ``BY_RESOURCE_TYPE`` and you must not set it for any other ``Pattern`` setting.
        :param tags: Key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_shield as shield
            
            cfn_protection_group_props = shield.CfnProtectionGroupProps(
                aggregation="aggregation",
                pattern="pattern",
                protection_group_id="protectionGroupId",
            
                # the properties below are optional
                members=["members"],
                resource_type="resourceType",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d3b2bbe1939f69f05c219f7f0fc8de5928677d1b98bdaefde53c2a2deaad182d)
            check_type(argname="argument aggregation", value=aggregation, expected_type=type_hints["aggregation"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument protection_group_id", value=protection_group_id, expected_type=type_hints["protection_group_id"])
            check_type(argname="argument members", value=members, expected_type=type_hints["members"])
            check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "aggregation": aggregation,
            "pattern": pattern,
            "protection_group_id": protection_group_id,
        }
        if members is not None:
            self._values["members"] = members
        if resource_type is not None:
            self._values["resource_type"] = resource_type
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def aggregation(self) -> builtins.str:
        '''Defines how AWS Shield combines resource data for the group in order to detect, mitigate, and report events.

        - Sum - Use the total traffic across the group. This is a good choice for most cases. Examples include Elastic IP addresses for EC2 instances that scale manually or automatically.
        - Mean - Use the average of the traffic across the group. This is a good choice for resources that share traffic uniformly. Examples include accelerators and load balancers.
        - Max - Use the highest traffic from each resource. This is useful for resources that don't share traffic and for resources that share that traffic in a non-uniform way. Examples include Amazon CloudFront distributions and origin resources for CloudFront distributions.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-aggregation
        '''
        result = self._values.get("aggregation")
        assert result is not None, "Required property 'aggregation' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pattern(self) -> builtins.str:
        '''The criteria to use to choose the protected resources for inclusion in the group.

        You can include all resources that have protections, provide a list of resource ARNs (Amazon Resource Names), or include all resources of a specified resource type.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-pattern
        '''
        result = self._values.get("pattern")
        assert result is not None, "Required property 'pattern' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def protection_group_id(self) -> builtins.str:
        '''The name of the protection group.

        You use this to identify the protection group in lists and to manage the protection group, for example to update, delete, or describe it.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-protectiongroupid
        '''
        result = self._values.get("protection_group_id")
        assert result is not None, "Required property 'protection_group_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def members(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARNs (Amazon Resource Names) of the resources to include in the protection group.

        You must set this when you set ``Pattern`` to ``ARBITRARY`` and you must not set it for any other ``Pattern`` setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-members
        '''
        result = self._values.get("members")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def resource_type(self) -> typing.Optional[builtins.str]:
        '''The resource type to include in the protection group.

        All protected resources of this type are included in the protection group. You must set this when you set ``Pattern`` to ``BY_RESOURCE_TYPE`` and you must not set it for any other ``Pattern`` setting.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-resourcetype
        '''
        result = self._values.get("resource_type")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key:value pairs associated with an AWS resource.

        The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protectiongroup.html#cfn-shield-protectiongroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProtectionGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_shield.CfnProtectionProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "resource_arn": "resourceArn",
        "application_layer_automatic_response_configuration": "applicationLayerAutomaticResponseConfiguration",
        "health_check_arns": "healthCheckArns",
        "tags": "tags",
    },
)
class CfnProtectionProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        resource_arn: builtins.str,
        application_layer_automatic_response_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        health_check_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnProtection``.

        :param name: The name of the protection. For example, ``My CloudFront distributions`` . .. epigraph:: If you change the name of an existing protection, Shield Advanced deletes the protection and replaces it with a new one. While this is happening, the protection isn't available on the AWS resource.
        :param resource_arn: The ARN (Amazon Resource Name) of the AWS resource that is protected.
        :param application_layer_automatic_response_configuration: The automatic application layer DDoS mitigation settings for the protection. This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.
        :param health_check_arns: The ARN (Amazon Resource Name) of the health check to associate with the protection. Health-based detection provides improved responsiveness and accuracy in attack detection and mitigation. You can use this option with any resource type except for Route 53 hosted zones. For more information, see `Configuring health-based detection using health checks <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-health-checks.html>`_ in the *AWS Shield Advanced Developer Guide* .
        :param tags: Key:value pairs associated with an AWS resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_shield as shield
            
            # block: Any
            # count: Any
            
            cfn_protection_props = shield.CfnProtectionProps(
                name="name",
                resource_arn="resourceArn",
            
                # the properties below are optional
                application_layer_automatic_response_configuration=shield.CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty(
                    action=shield.CfnProtection.ActionProperty(
                        block=block,
                        count=count
                    ),
                    status="status"
                ),
                health_check_arns=["healthCheckArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__611ea0b9dff6681de6e3f0cdb3f7a0ae092f6774ebe50cf733630b5b887c0d42)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument resource_arn", value=resource_arn, expected_type=type_hints["resource_arn"])
            check_type(argname="argument application_layer_automatic_response_configuration", value=application_layer_automatic_response_configuration, expected_type=type_hints["application_layer_automatic_response_configuration"])
            check_type(argname="argument health_check_arns", value=health_check_arns, expected_type=type_hints["health_check_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "resource_arn": resource_arn,
        }
        if application_layer_automatic_response_configuration is not None:
            self._values["application_layer_automatic_response_configuration"] = application_layer_automatic_response_configuration
        if health_check_arns is not None:
            self._values["health_check_arns"] = health_check_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the protection. For example, ``My CloudFront distributions`` .

        .. epigraph::

           If you change the name of an existing protection, Shield Advanced deletes the protection and replaces it with a new one. While this is happening, the protection isn't available on the AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def resource_arn(self) -> builtins.str:
        '''The ARN (Amazon Resource Name) of the AWS resource that is protected.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-resourcearn
        '''
        result = self._values.get("resource_arn")
        assert result is not None, "Required property 'resource_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def application_layer_automatic_response_configuration(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty]]:
        '''The automatic application layer DDoS mitigation settings for the protection.

        This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-applicationlayerautomaticresponseconfiguration
        '''
        result = self._values.get("application_layer_automatic_response_configuration")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty]], result)

    @builtins.property
    def health_check_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ARN (Amazon Resource Name) of the health check to associate with the protection.

        Health-based detection provides improved responsiveness and accuracy in attack detection and mitigation.

        You can use this option with any resource type except for Route 53 hosted zones.

        For more information, see `Configuring health-based detection using health checks <https://docs.aws.amazon.com/waf/latest/developerguide/ddos-advanced-health-checks.html>`_ in the *AWS Shield Advanced Developer Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-healthcheckarns
        '''
        result = self._values.get("health_check_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''Key:value pairs associated with an AWS resource.

        The key:value pair can be anything you define. Typically, the tag key represents a category (such as "environment") and the tag value represents a specific value within that category (such as "test," "development," or "production"). You can add up to 50 tags to each AWS resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-shield-protection.html#cfn-shield-protection-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnProtectionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnDRTAccess",
    "CfnDRTAccessProps",
    "CfnProactiveEngagement",
    "CfnProactiveEngagementProps",
    "CfnProtection",
    "CfnProtectionGroup",
    "CfnProtectionGroupProps",
    "CfnProtectionProps",
]

publication.publish()

def _typecheckingstub__4a15a18e843fffdbb42d47fd2ac911234ec7893d81473ee5d084ecfea8549c95(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    role_arn: builtins.str,
    log_bucket_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1852e8b6dd2c25fa06e5e566839fd5a1f6a276b8b39e838b2b89482ea513bd65(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8571297b6d69a16de38bab6d3f1dc92d7c9246c66b35f80febffdfb1f3b2e7c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__da38bba1d6994ae07694944aa4916a03f58a2c9485676c9085e1c314c3f2aa57(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c94abc39b038180b7b7b34ef27ad16e99c54c8cd1ff7e04fd4e4882047910e1(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7eb7d0e0a686aa5ce41af2859848528d577aa001b693b180bf8c8c1cbe226c62(
    *,
    role_arn: builtins.str,
    log_bucket_list: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__75179b0b2a7390cfe8ff254cdce98b24f9e580040dddc66ad43b122c2b5e0c6d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    emergency_contact_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProactiveEngagement.EmergencyContactProperty, typing.Dict[builtins.str, typing.Any]]]]],
    proactive_engagement_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d5a960f62ca304b7ebcf5e14298d60f742a16d5dbaf6f97f912470ede285d11e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__99229a0794c4f40e520680e633fa758c86f0b7d6e14e7081dd03b9a42c242a63(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__124fcf35e2a271c8af4d75b0cf5014b8ad1239720905927de40e52915ba3e15c(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnProactiveEngagement.EmergencyContactProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b037bb753d3225b693b8d381833edd00f55da5f9159d4af431e1e597b718015(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__943f9798df53d53e30978210d183db122bb3f1df5ce07ae3b7aaa70f1002896d(
    *,
    email_address: builtins.str,
    contact_notes: typing.Optional[builtins.str] = None,
    phone_number: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a87e22725ebed99038c7fbf64e1b444b667784de63c1c0f1d6dd1233d0655684(
    *,
    emergency_contact_list: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProactiveEngagement.EmergencyContactProperty, typing.Dict[builtins.str, typing.Any]]]]],
    proactive_engagement_status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c25ea3f87ade4afdbc73b2ca70b15ee669920a1fb5f0ed5803cfd112c3b70c11(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    resource_arn: builtins.str,
    application_layer_automatic_response_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c6d6fd37913379ec3a2749bbbf52fd1927d9c61ec30884700bdad09f41bd423a(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66cc1b7316da30a5a6580d88917c556d71192a4c006b273660d5ad02f215814e(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f664fe46f1fe6ac65c7f4d1ffc5b08a87c78645927fdd0533b7477ee11e1f0e3(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c90c79a0e936546060dcc8c586dd2be6cd6ff32840ad1e49333ef28864e5dfa0(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__145ac68c42ad419925aa32644eea217eb08e6ce73993b51c7af4167aab4e13de(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d98b040afae8b4f4d573af557d97a93bdf3dde17bbb8d705e4c6c0d0acc940aa(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4cd697bbebfdef8296c6fa9e920e70bb9a5ed569b251c351c36b4e3edbdd61e0(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__10ad3bad839bf7f73612fddf37ab7b4b54806b3d7c6601e67b6e355265495610(
    *,
    block: typing.Any = None,
    count: typing.Any = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4bb6af4792edfc92c1e9a35d69e7e3b4dea97cee90b65597ebf1f9e0777df0e2(
    *,
    action: typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtection.ActionProperty, typing.Dict[builtins.str, typing.Any]]],
    status: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__81da6ee581209a252a2406d5601c15a1be321e07fcf0aa646c27538a66db638c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    aggregation: builtins.str,
    pattern: builtins.str,
    protection_group_id: builtins.str,
    members: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76b88e310cde3207aac88376ade59343d5e539487019cd87c212616c6a70148e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db6feff847b2fccbd8fa083c92622d53c9bbea5c28c87fd70765fb2916691df0(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5ab253e64e58318d6cd6e12bbf34c34aa957e343239b65290d697b1c872f243d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__dd66def3c643e8068586fab8310be7a0bde4339a08f8f4c532ec845fe6c0181b(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__843e37c61fb3edb2d8ae7c8a0c0a7ecfebcef61fe1f6b6bb7543d2d47a7b82c9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c886ab822198804e227db899eaedff6f661d9a7e4eab802450270e17742b7115(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6e3d5c3c763d27892562b1771a153762a3d34df5cb316c0538590da13f506b36(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70ea7c7493bdebcbd30035fe4d1550d14d6af25225d32845d78baca96ef59493(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d3b2bbe1939f69f05c219f7f0fc8de5928677d1b98bdaefde53c2a2deaad182d(
    *,
    aggregation: builtins.str,
    pattern: builtins.str,
    protection_group_id: builtins.str,
    members: typing.Optional[typing.Sequence[builtins.str]] = None,
    resource_type: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__611ea0b9dff6681de6e3f0cdb3f7a0ae092f6774ebe50cf733630b5b887c0d42(
    *,
    name: builtins.str,
    resource_arn: builtins.str,
    application_layer_automatic_response_configuration: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnProtection.ApplicationLayerAutomaticResponseConfigurationProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    health_check_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
