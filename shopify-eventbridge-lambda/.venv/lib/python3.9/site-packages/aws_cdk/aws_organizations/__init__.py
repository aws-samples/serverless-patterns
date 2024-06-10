'''
# AWS::Organizations Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_organizations as organizations
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Organizations construct libraries](https://constructs.dev/search?q=organizations)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Organizations resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Organizations.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Organizations](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Organizations.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggable as _ITaggable_36806126,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnAccount(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_organizations.CfnAccount",
):
    '''Creates an AWS account that is automatically a member of the organization whose credentials made the request.

    AWS CloudFormation uses the ```CreateAccount`` <https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html>`_ operation to create accounts. This is an asynchronous request that AWS performs in the background. Because ``CreateAccount`` operates asynchronously, it can return a successful completion message even though account initialization might still be in progress. You might need to wait a few minutes before you can successfully access the account. To check the status of the request, do one of the following:

    - Use the ``Id`` value of the ``CreateAccountStatus`` response element from the ``CreateAccount`` operation to provide as a parameter to the ```DescribeCreateAccountStatus`` <https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeCreateAccountStatus.html>`_ operation.
    - Check the CloudTrail log for the ``CreateAccountResult`` event. For information on using CloudTrail with AWS Organizations , see `Logging and monitoring in AWS Organizations <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_security_incident-response.html#orgs_cloudtrail-integration>`_ in the *AWS Organizations User Guide* .

    The user who calls the API to create an account must have the ``organizations:CreateAccount`` permission. If you enabled all features in the organization, AWS Organizations creates the required service-linked role named ``AWSServiceRoleForOrganizations`` . For more information, see `AWS Organizations and service-linked roles <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html#orgs_integrate_services-using_slrs>`_ in the *AWS Organizations User Guide* .

    If the request includes tags, then the requester must have the ``organizations:TagResource`` permission.

    AWS Organizations preconfigures the new member account with a role (named ``OrganizationAccountAccessRole`` by default) that grants users in the management account administrator permissions in the new member account. Principals in the management account can assume the role. AWS Organizations clones the company name and address information for the new account from the organization's management account.

    For more information about creating accounts, see `Creating a member account in your organization <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_create.html>`_ in the *AWS Organizations User Guide* .

    This operation can be called only from the organization's management account.

    *Deleting Account resources*

    The default ``DeletionPolicy`` for resource ``AWS::Organizations::Account`` is ``Retain`` . For more information about how AWS CloudFormation deletes resources, see `DeletionPolicy Attribute <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-deletionpolicy.html>`_ .
    .. epigraph::

       - If you include multiple accounts in a single template, you must use the ``DependsOn`` attribute on each account resource type so that the accounts are created sequentially. If you create multiple accounts at the same time, Organizations returns an error and the stack operation fails.
       - You can't modify the following list of ``Account`` resource parameters using AWS CloudFormation updates.
       - AccountName
       - Email
       - RoleName

       If you attempt to update the listed parameters, CloudFormation will attempt the update, but you will receive an error message as those updates are not supported from an Organizations management account or a `registered delegated administrator <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html>`_ account. Both the update and the update roll-back will fail, so you must skip the account resource update. To update parameters ``AccountName`` and ``Email`` , you must sign in to the AWS Management Console as the AWS account root user. For more information, see `Update the AWS account name, email address, or password for the root user <https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-root-user.html>`_ in the *AWS Account Management Reference Guide* .

       - When you create an account in an organization using the AWS Organizations console, API, or AWS CLI commands, we don't automatically collect the information required for the account to operate as a standalone account. That includes collecting the payment method and signing the end user license agreement (EULA). If you must remove an account from your organization later, you can do so only after you provide the missing information. For more information, see `Considerations before removing an account from an organization <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_account-before-remove.html>`_ in the *AWS Organizations User Guide* .
       - When you create an account in an organization using AWS CloudFormation , you can't specify a value for the ``CreateAccount`` operation parameter ``IamUserAccessToBilling`` . The default value for parameter ``IamUserAccessToBilling`` is ``ALLOW`` , and IAM users and roles with the required permissions can access billing information for the new account.
       - If you get an exception that indicates ``DescribeCreateAccountStatus returns IN_PROGRESS state before time out`` . You must check the account creation status using the ```DescribeCreateAccountStatus`` <https://docs.aws.amazon.com/organizations/latest/APIReference/API_DescribeCreateAccountStatus.html>`_ operation. If the account state returns as ``SUCCEEDED`` , you can import the account into AWS CloudFormation management using ```resource import`` <https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import.html>`_ .
       - If you get an exception that indicates you have exceeded your account quota for the organization, you can request an increase by using the `Service Quotas console <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html>`_ .
       - If you get an exception that indicates the operation failed because your organization is still initializing, wait one hour and then try again. If the error persists, contact `AWS Support <https://docs.aws.amazon.com/support/home#/>`_ .
       - We don't recommend that you use the ``CreateAccount`` operation to create multiple temporary accounts. You can close accounts using the ```CloseAccount`` <https://docs.aws.amazon.com/organizations/latest/APIReference/API_CloseAccount.html>`_ operation or from the AWS Organizations console in the organization's management account. For information on the requirements and process for closing an account, see `Closing a member account in your organization <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_close.html>`_ in the *AWS Organizations User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html
    :cloudformationResource: AWS::Organizations::Account
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_organizations as organizations
        
        cfn_account = organizations.CfnAccount(self, "MyCfnAccount",
            account_name="accountName",
            email="email",
        
            # the properties below are optional
            parent_ids=["parentIds"],
            role_name="roleName",
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
        account_name: builtins.str,
        email: builtins.str,
        parent_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_name: The account name given to the account when it was created.
        :param email: The email address associated with the AWS account. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for this parameter is a string of characters that represents a standard internet email address.
        :param parent_ids: The unique identifier (ID) of the root or organizational unit (OU) that you want to create the new account in. If you don't specify this parameter, the ``ParentId`` defaults to the root ID. This parameter only accepts a string array with one string value. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a parent ID string requires one of the following: - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
        :param role_name: The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account. If you don't specify this parameter, the role name defaults to ``OrganizationAccountAccessRole`` . For more information about how to use this role to access the member account, see the following links: - `Creating the OrganizationAccountAccessRole in an invited member account <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-cross-account-role>`_ in the *AWS Organizations User Guide* - Steps 2 and 3 in `IAM Tutorial: Delegate access across AWS accounts using IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html>`_ in the *IAM User Guide* The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter. The pattern can include uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@- Default: - "OrganizationAccountAccessRole"
        :param tags: A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide. .. epigraph:: If any one of the tags is not valid or if you exceed the maximum allowed number of tags for an account, then the entire request fails and the account is not created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__717b5f787efa43cf2d1c6b1edf32de9bd64cd50c67b6e29cf7e1d6df0f5f1b60)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnAccountProps(
            account_name=account_name,
            email=email,
            parent_ids=parent_ids,
            role_name=role_name,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee3ea086c724fb0935ee8a727937a17ae19b987a8ade49b1405a7787feb7e3bc)
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
            type_hints = typing.get_type_hints(_typecheckingstub__80bdf2bd3ebcd33351d23efb5a5fbe768927b4510acf316c02ac29e5ffcca33a)
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
        '''Returns the unique identifier (ID) of the account.

        For example: ``123456789012`` .

        :cloudformationAttribute: AccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''Returns the Amazon Resource Name (ARN) of the account.

        For example: ``arn:aws:organizations::111111111111:account/o-exampleorgid/555555555555`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrJoinedMethod")
    def attr_joined_method(self) -> builtins.str:
        '''Returns the method by which the account joined the organization.

        For example: ``INVITED | CREATED`` .

        :cloudformationAttribute: JoinedMethod
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJoinedMethod"))

    @builtins.property
    @jsii.member(jsii_name="attrJoinedTimestamp")
    def attr_joined_timestamp(self) -> builtins.str:
        '''Returns the date the account became a part of the organization.

        For example: ``2016-11-24T11:11:48-08:00`` .

        :cloudformationAttribute: JoinedTimestamp
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrJoinedTimestamp"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''Returns the status of the account in the organization.

        For example: ``ACTIVE | SUSPENDED | PENDING_CLOSURE`` .

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

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
    @jsii.member(jsii_name="accountName")
    def account_name(self) -> builtins.str:
        '''The account name given to the account when it was created.'''
        return typing.cast(builtins.str, jsii.get(self, "accountName"))

    @account_name.setter
    def account_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c7cb80343b6f0f43ba7a94207203ab7cefaa6c6f61ec38391afffdb4896b52f1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountName", value)

    @builtins.property
    @jsii.member(jsii_name="email")
    def email(self) -> builtins.str:
        '''The email address associated with the AWS account.'''
        return typing.cast(builtins.str, jsii.get(self, "email"))

    @email.setter
    def email(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fb3017540fda5760817d479375b8f0ba4860d2d1001cb43056042fc31d63a8f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "email", value)

    @builtins.property
    @jsii.member(jsii_name="parentIds")
    def parent_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The unique identifier (ID) of the root or organizational unit (OU) that you want to create the new account in.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "parentIds"))

    @parent_ids.setter
    def parent_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4341d69ba10680d0ef646a879e2ef2e66709e58b62fb62e8d3e1b8008424fd63)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentIds", value)

    @builtins.property
    @jsii.member(jsii_name="roleName")
    def role_name(self) -> typing.Optional[builtins.str]:
        '''The name of an IAM role that AWS Organizations automatically preconfigures in the new member account.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "roleName"))

    @role_name.setter
    def role_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__70acd1418e03b2ec3a6e3ad06a5c89c09a87bc96955d07b91a2af5820d3ded62)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "roleName", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created account.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__797fecb1b9a4bafd998e385c8ea18d8b31431a28a593cf9eba2da34a96ca8e0a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_organizations.CfnAccountProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_name": "accountName",
        "email": "email",
        "parent_ids": "parentIds",
        "role_name": "roleName",
        "tags": "tags",
    },
)
class CfnAccountProps:
    def __init__(
        self,
        *,
        account_name: builtins.str,
        email: builtins.str,
        parent_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
        role_name: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnAccount``.

        :param account_name: The account name given to the account when it was created.
        :param email: The email address associated with the AWS account. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for this parameter is a string of characters that represents a standard internet email address.
        :param parent_ids: The unique identifier (ID) of the root or organizational unit (OU) that you want to create the new account in. If you don't specify this parameter, the ``ParentId`` defaults to the root ID. This parameter only accepts a string array with one string value. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a parent ID string requires one of the following: - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
        :param role_name: The name of an IAM role that AWS Organizations automatically preconfigures in the new member account. This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account. If you don't specify this parameter, the role name defaults to ``OrganizationAccountAccessRole`` . For more information about how to use this role to access the member account, see the following links: - `Creating the OrganizationAccountAccessRole in an invited member account <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-cross-account-role>`_ in the *AWS Organizations User Guide* - Steps 2 and 3 in `IAM Tutorial: Delegate access across AWS accounts using IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html>`_ in the *IAM User Guide* The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter. The pattern can include uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@- Default: - "OrganizationAccountAccessRole"
        :param tags: A list of tags that you want to attach to the newly created account. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide. .. epigraph:: If any one of the tags is not valid or if you exceed the maximum allowed number of tags for an account, then the entire request fails and the account is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_organizations as organizations
            
            cfn_account_props = organizations.CfnAccountProps(
                account_name="accountName",
                email="email",
            
                # the properties below are optional
                parent_ids=["parentIds"],
                role_name="roleName",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a77bb3f433e62d91418b11b634f558fe79904da5ba0000f7cb7c650162add452)
            check_type(argname="argument account_name", value=account_name, expected_type=type_hints["account_name"])
            check_type(argname="argument email", value=email, expected_type=type_hints["email"])
            check_type(argname="argument parent_ids", value=parent_ids, expected_type=type_hints["parent_ids"])
            check_type(argname="argument role_name", value=role_name, expected_type=type_hints["role_name"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_name": account_name,
            "email": email,
        }
        if parent_ids is not None:
            self._values["parent_ids"] = parent_ids
        if role_name is not None:
            self._values["role_name"] = role_name
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_name(self) -> builtins.str:
        '''The account name given to the account when it was created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-accountname
        '''
        result = self._values.get("account_name")
        assert result is not None, "Required property 'account_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def email(self) -> builtins.str:
        '''The email address associated with the AWS account.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for this parameter is a string of characters that represents a standard internet email address.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-email
        '''
        result = self._values.get("email")
        assert result is not None, "Required property 'email' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The unique identifier (ID) of the root or organizational unit (OU) that you want to create the new account in.

        If you don't specify this parameter, the ``ParentId`` defaults to the root ID.

        This parameter only accepts a string array with one string value.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a parent ID string requires one of the following:

        - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
        - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-parentids
        '''
        result = self._values.get("parent_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def role_name(self) -> typing.Optional[builtins.str]:
        '''The name of an IAM role that AWS Organizations automatically preconfigures in the new member account.

        This role trusts the management account, allowing users in the management account to assume the role, as permitted by the management account administrator. The role has administrator permissions in the new member account.

        If you don't specify this parameter, the role name defaults to ``OrganizationAccountAccessRole`` .

        For more information about how to use this role to access the member account, see the following links:

        - `Creating the OrganizationAccountAccessRole in an invited member account <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html#orgs_manage_accounts_create-cross-account-role>`_ in the *AWS Organizations User Guide*
        - Steps 2 and 3 in `IAM Tutorial: Delegate access across AWS accounts using IAM roles <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html>`_ in the *IAM User Guide*

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter. The pattern can include uppercase letters, lowercase letters, digits with no spaces, and any of the following characters: =,.@-

        :default: - "OrganizationAccountAccessRole"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-rolename
        '''
        result = self._values.get("role_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created account.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide.
        .. epigraph::

           If any one of the tags is not valid or if you exceed the maximum allowed number of tags for an account, then the entire request fails and the account is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-account.html#cfn-organizations-account-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnAccountProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnOrganization(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_organizations.CfnOrganization",
):
    '''Creates an AWS organization.

    The account whose user is calling the ```CreateOrganization`` <https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateOrganization.html>`_ operation automatically becomes the `management account <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account>`_ of the new organization.

    This operation must be called using credentials from the account that is to become the new organization's management account. The principal must also have the `relevant IAM permissions <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_create.html>`_ .
    .. epigraph::

       - If you delete an organization, you can't recover it. If you created any policies inside of the organization, they're also deleted and you can't recover them.
       - You can delete an organization only after you remove all member accounts from the organization. If you created some of your member accounts using AWS Organizations , you might be blocked from removing those accounts. You can remove a member account only if it has all the information that's required to operate as a standalone AWS account. For more information about how to provide that information and then remove the account, see `Leave an organization from your member account <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_leave-as-member.html>`_ in the *AWS Organizations User Guide* .
       - If you closed a member account before you remove it from the organization, it enters a 'suspended' state for a period of time and you can't remove the account from the organization until it is finally closed. This can take up to 90 days and can prevent you from deleting the organization until all member accounts are completely closed.

       For more information, see `Deleting an organization <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_delete.html>`_ in the *AWS Organizations User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html
    :cloudformationResource: AWS::Organizations::Organization
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_organizations as organizations
        
        cfn_organization = organizations.CfnOrganization(self, "MyCfnOrganization",
            feature_set="featureSet"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        feature_set: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param feature_set: Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality. - ``ALL`` In addition to all the features supported by the consolidated billing feature set, the management account gains access to advanced features that give you more control over accounts in your organization. By default or if you set the ``FeatureSet`` property to ``ALL`` , the new organization is created with all features enabled and service control policies automatically enabled in the `root <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#root>`_ . For more information, see `All features <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all>`_ in the *AWS Organizations User Guide* . - ``CONSOLIDATED_BILLING`` All member accounts have their bills consolidated to and paid by the management account. For more information, see `Consolidated billing <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only>`_ in the *AWS Organizations User Guide* . The consolidated billing feature subset isn't available for organizations in the AWS GovCloud (US) Region. Feature set ``ALL`` provides the following advanced features: - Apply any `policy type <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#orgs-policy-types>`_ to any member account in the organization. - Apply `service control policies (SCPs) <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html>`_ to member accounts that restrict the services and actions that users (including the root user) and roles in an account can access. Using SCPs you can prevent member accounts from leaving the organization. - Enable `integration with supported AWS services <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html>`_ to let those services provide functionality across all of the accounts in your organization. If you don't specify this property, the default value is ``ALL`` . Default: - "ALL"
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__450a54c6b7334fcb8f406a9a29b8e1f90a618bcbd127f2d5a6a9fa43ff254400)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationProps(feature_set=feature_set)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a0b1a88993c76738edf5e9d3584d058cabe1cfc259fb5d620589d5c23507de91)
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
            type_hints = typing.get_type_hints(_typecheckingstub__96e2cf417d73c47f4cdfd81355199f9352be808cebdc6968077c1559c996fd16)
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
        '''The Amazon Resource Name (ARN) of an organization.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier (ID) of an organization.

        :cloudformationAttribute: Id
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrId"))

    @builtins.property
    @jsii.member(jsii_name="attrManagementAccountArn")
    def attr_management_account_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) of the account that is designated as the management account for the organization.

        :cloudformationAttribute: ManagementAccountArn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagementAccountArn"))

    @builtins.property
    @jsii.member(jsii_name="attrManagementAccountEmail")
    def attr_management_account_email(self) -> builtins.str:
        '''The email address that is associated with the AWS account that is designated as the management account for the organization.

        :cloudformationAttribute: ManagementAccountEmail
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagementAccountEmail"))

    @builtins.property
    @jsii.member(jsii_name="attrManagementAccountId")
    def attr_management_account_id(self) -> builtins.str:
        '''The unique identifier (ID) of the management account of an organization.

        :cloudformationAttribute: ManagementAccountId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrManagementAccountId"))

    @builtins.property
    @jsii.member(jsii_name="attrRootId")
    def attr_root_id(self) -> builtins.str:
        '''The unique identifier (ID) for the root.

        :cloudformationAttribute: RootId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrRootId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="featureSet")
    def feature_set(self) -> typing.Optional[builtins.str]:
        '''Specifies the feature set supported by the new organization.

        Each feature set supports different levels of functionality.
        '''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "featureSet"))

    @feature_set.setter
    def feature_set(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bba27bb9e125d71f0e3f25eaa03ce169e5b7e47cf184fcaeb273ce584181b51d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "featureSet", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_organizations.CfnOrganizationProps",
    jsii_struct_bases=[],
    name_mapping={"feature_set": "featureSet"},
)
class CfnOrganizationProps:
    def __init__(self, *, feature_set: typing.Optional[builtins.str] = None) -> None:
        '''Properties for defining a ``CfnOrganization``.

        :param feature_set: Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality. - ``ALL`` In addition to all the features supported by the consolidated billing feature set, the management account gains access to advanced features that give you more control over accounts in your organization. By default or if you set the ``FeatureSet`` property to ``ALL`` , the new organization is created with all features enabled and service control policies automatically enabled in the `root <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#root>`_ . For more information, see `All features <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all>`_ in the *AWS Organizations User Guide* . - ``CONSOLIDATED_BILLING`` All member accounts have their bills consolidated to and paid by the management account. For more information, see `Consolidated billing <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only>`_ in the *AWS Organizations User Guide* . The consolidated billing feature subset isn't available for organizations in the AWS GovCloud (US) Region. Feature set ``ALL`` provides the following advanced features: - Apply any `policy type <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#orgs-policy-types>`_ to any member account in the organization. - Apply `service control policies (SCPs) <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html>`_ to member accounts that restrict the services and actions that users (including the root user) and roles in an account can access. Using SCPs you can prevent member accounts from leaving the organization. - Enable `integration with supported AWS services <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html>`_ to let those services provide functionality across all of the accounts in your organization. If you don't specify this property, the default value is ``ALL`` . Default: - "ALL"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_organizations as organizations
            
            cfn_organization_props = organizations.CfnOrganizationProps(
                feature_set="featureSet"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__232c106aefcec7adaf1b3c73c0f809bd72527d672e2faf2ac3e81e72e8f01c48)
            check_type(argname="argument feature_set", value=feature_set, expected_type=type_hints["feature_set"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if feature_set is not None:
            self._values["feature_set"] = feature_set

    @builtins.property
    def feature_set(self) -> typing.Optional[builtins.str]:
        '''Specifies the feature set supported by the new organization. Each feature set supports different levels of functionality.

        - ``ALL``  In addition to all the features supported by the consolidated billing feature set, the management account gains access to advanced features that give you more control over accounts in your organization. By default or if you set the ``FeatureSet`` property to ``ALL`` , the new organization is created with all features enabled and service control policies automatically enabled in the `root <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#root>`_ . For more information, see `All features <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-all>`_ in the *AWS Organizations User Guide* .
        - ``CONSOLIDATED_BILLING``  All member accounts have their bills consolidated to and paid by the management account. For more information, see `Consolidated billing <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#feature-set-cb-only>`_ in the *AWS Organizations User Guide* .

        The consolidated billing feature subset isn't available for organizations in the AWS GovCloud (US) Region.

        Feature set ``ALL`` provides the following advanced features:

        - Apply any `policy type <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html#orgs-policy-types>`_ to any member account in the organization.
        - Apply `service control policies (SCPs) <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html>`_ to member accounts that restrict the services and actions that users (including the root user) and roles in an account can access. Using SCPs you can prevent member accounts from leaving the organization.
        - Enable `integration with supported AWS services <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services_list.html>`_ to let those services provide functionality across all of the accounts in your organization.

        If you don't specify this property, the default value is ``ALL`` .

        :default: - "ALL"

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organization.html#cfn-organizations-organization-featureset
        '''
        result = self._values.get("feature_set")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnOrganizationalUnit(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_organizations.CfnOrganizationalUnit",
):
    '''Creates an organizational unit (OU) within a root or parent OU.

    An OU is a container for accounts that enables you to organize your accounts to apply policies according to your business requirements. The number of levels deep that you can nest OUs is dependent upon the policy types enabled for that root. For service control policies, the limit is five.

    For more information about OUs, see `Managing organizational units (OUs) <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_ous.html>`_ in the *AWS Organizations User Guide* .

    If the request includes tags, then the requester must have the ``organizations:TagResource`` permission.

    This operation can be called only from the organization's management account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html
    :cloudformationResource: AWS::Organizations::OrganizationalUnit
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_organizations as organizations
        
        cfn_organizational_unit = organizations.CfnOrganizationalUnit(self, "MyCfnOrganizationalUnit",
            name="name",
            parent_id="parentId",
        
            # the properties below are optional
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
        parent_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The friendly name of this OU. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        :param parent_id: The unique identifier (ID) of the parent root or OU that you want to create the new OU in. .. epigraph:: To update the ``ParentId`` parameter value, you must first remove all accounts attached to the organizational unit (OU). OUs can't be moved within the organization with accounts still attached. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a parent ID string requires one of the following: - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
        :param tags: A list of tags that you want to attach to the newly created OU. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide. .. epigraph:: If any one of the tags is not valid or if you exceed the allowed number of tags for an OU, then the entire request fails and the OU is not created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__05eb3e3a6c1c8de7f03913252600dcc42e4c1e99dbbab3f47a3fb8e4ce5ffcec)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnOrganizationalUnitProps(name=name, parent_id=parent_id, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b0f1c1e40ee57749b1e3e89c931bad8d33532e5bc09dccfa20942e74efb5d7d5)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ca29cbd7f58c4e45178ac57de78ce34d515cd266bd0b2ba6e89c48cdf3ddfc0d)
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
        '''The Amazon Resource Name (ARN) of this OU.

        For example: ``arn:aws:organizations::111111111111:ou/o-exampleorgid/ou-examplerootid111-exampleouid111`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''The unique identifier (ID) associated with this OU.

        For example: ``ou-examplerootid111-exampleouid111`` .

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
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The friendly name of this OU.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2fc5c2614f792a6493956c330d3c0260c5284cf30143bd369380d3522da66691)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="parentId")
    def parent_id(self) -> builtins.str:
        '''The unique identifier (ID) of the parent root or OU that you want to create the new OU in.'''
        return typing.cast(builtins.str, jsii.get(self, "parentId"))

    @parent_id.setter
    def parent_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e484a48f669e683ffa481185c24f4c123298d1a7e9bbf68822a98598a2faaa02)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parentId", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created OU.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__eabed8f386c5c6fcea2646194b0879df9b16b1d40979baac245b456985dfa3e7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_organizations.CfnOrganizationalUnitProps",
    jsii_struct_bases=[],
    name_mapping={"name": "name", "parent_id": "parentId", "tags": "tags"},
)
class CfnOrganizationalUnitProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        parent_id: builtins.str,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnOrganizationalUnit``.

        :param name: The friendly name of this OU. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        :param parent_id: The unique identifier (ID) of the parent root or OU that you want to create the new OU in. .. epigraph:: To update the ``ParentId`` parameter value, you must first remove all accounts attached to the organizational unit (OU). OUs can't be moved within the organization with accounts still attached. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a parent ID string requires one of the following: - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
        :param tags: A list of tags that you want to attach to the newly created OU. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide. .. epigraph:: If any one of the tags is not valid or if you exceed the allowed number of tags for an OU, then the entire request fails and the OU is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_organizations as organizations
            
            cfn_organizational_unit_props = organizations.CfnOrganizationalUnitProps(
                name="name",
                parent_id="parentId",
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0140abb0fae0d0670b748f08be863eb25b5afb304506c41736e4ebe5046a1191)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument parent_id", value=parent_id, expected_type=type_hints["parent_id"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "parent_id": parent_id,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The friendly name of this OU.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html#cfn-organizations-organizationalunit-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def parent_id(self) -> builtins.str:
        '''The unique identifier (ID) of the parent root or OU that you want to create the new OU in.

        .. epigraph::

           To update the ``ParentId`` parameter value, you must first remove all accounts attached to the organizational unit (OU). OUs can't be moved within the organization with accounts still attached.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a parent ID string requires one of the following:

        - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
        - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html#cfn-organizations-organizationalunit-parentid
        '''
        result = self._values.get("parent_id")
        assert result is not None, "Required property 'parent_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created OU.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide.
        .. epigraph::

           If any one of the tags is not valid or if you exceed the allowed number of tags for an OU, then the entire request fails and the OU is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-organizationalunit.html#cfn-organizations-organizationalunit-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnOrganizationalUnitProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_organizations.CfnPolicy",
):
    '''Creates a policy of a specified type that you can attach to a root, an organizational unit (OU), or an individual AWS account .

    For more information about policies and their use, see `Managing AWS Organizations policies <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies.html>`_ .

    If the request includes tags, then the requester must have the ``organizations:TagResource`` permission.

    This operation can be called only from the organization's management account.
    .. epigraph::

       Before you can create a policy of a given type, you must first `enable that policy type <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_enable-disable.html>`_ in your organization.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html
    :cloudformationResource: AWS::Organizations::Policy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_organizations as organizations
        
        # content: Any
        
        cfn_policy = organizations.CfnPolicy(self, "MyCfnPolicy",
            content=content,
            name="name",
            type="type",
        
            # the properties below are optional
            description="description",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            target_ids=["targetIds"]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        content: typing.Any,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The policy text content. You can specify the policy content as a JSON object or a JSON string. .. epigraph:: When you specify the policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the policy content as a JSON object instead. The text that you supply must adhere to the rules of the policy type you specify in the ``Type`` parameter. The following AWS Organizations quotas are enforced for the maximum size of a policy document: - Service control policies: 5,120 characters - AI services opt-out policies: 2,500 characters - Backup policies: 10,000 characters - Tag policies: 10,000 characters For more information about Organizations service quotas, see `Quotas for AWS Organizations <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html>`_ in the *AWS Organizations User Guide* .
        :param name: Name of the policy. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        :param type: The type of policy to create.
        :param description: Human readable description of the policy.
        :param tags: A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide. .. epigraph:: If any one of the tags is not valid or if you exceed the allowed number of tags for a policy, then the entire request fails and the policy is not created.
        :param target_ids: List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the `ListRoots <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html>`_ , `ListOrganizationalUnitsForParent <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html>`_ , or `ListAccounts <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html>`_ operations. If you don't specify this parameter, the policy is created but not attached to any organization resource. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a target ID string requires one of the following: - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. - *Account* - A string that consists of exactly 12 digits. - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9c8ac465f7818132d3539ff8d8e22250305dad104185434533d033da8a80adad)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPolicyProps(
            content=content,
            name=name,
            type=type,
            description=description,
            tags=tags,
            target_ids=target_ids,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__08e107e9c8d61d1f582ba132c6a4d229d6f0e045a4e54986638403cf2fea7f0d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__1174ab6fdd21c443893a2bf14c16d0f3d4c868f39d0a37fefcfb8a7714bd3ffa)
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
        '''Returns the Amazon Resource Name (ARN) of the policy.

        For example: ``arn:aws:organizations::111111111111:policy/o-exampleorgid/service_control_policy/p-examplepolicyid111`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAwsManaged")
    def attr_aws_managed(self) -> _IResolvable_da3f097b:
        '''Returns a boolean value that indicates whether the specified policy is an AWS managed policy.

        If true, then you can attach the policy to roots, OUs, or accounts, but you cannot edit it. For example: ``true | false`` .

        :cloudformationAttribute: AwsManaged
        '''
        return typing.cast(_IResolvable_da3f097b, jsii.get(self, "attrAwsManaged"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Returns the unique identifier (ID) of the policy.

        For example: ``p-examplepolicyid111`` .

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
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Any:
        '''The policy text content.

        You can specify the policy content as a JSON object or a JSON string.
        '''
        return typing.cast(typing.Any, jsii.get(self, "content"))

    @content.setter
    def content(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1191c6f193a4faa8d4257d158518469a85c6127f725cdf681af3d969aea39846)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''Name of the policy.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cb096f73e44ea3f62f85c771fef970b636d4d893157d1035d741a52506ae20f6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of policy to create.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9823ab486df28286ddcf2d4e607740eed95089b4d80a6e2a7a858e37af2e521a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''Human readable description of the policy.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__15f0eb8f96a555ab850e02c78f1d5319de15607de2d6cecc5449543f8a58d24d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created policy.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__9caafe6d9a16db2e71e0d35514c7cc53b1f7f3b30806cee494691748e49625f2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="targetIds")
    def target_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "targetIds"))

    @target_ids.setter
    def target_ids(self, value: typing.Optional[typing.List[builtins.str]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b5e07984d6cb568abac54dca9143f32081c21cefa3f9f57283a87b6c35a1fd90)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targetIds", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_organizations.CfnPolicyProps",
    jsii_struct_bases=[],
    name_mapping={
        "content": "content",
        "name": "name",
        "type": "type",
        "description": "description",
        "tags": "tags",
        "target_ids": "targetIds",
    },
)
class CfnPolicyProps:
    def __init__(
        self,
        *,
        content: typing.Any,
        name: builtins.str,
        type: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        target_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPolicy``.

        :param content: The policy text content. You can specify the policy content as a JSON object or a JSON string. .. epigraph:: When you specify the policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the policy content as a JSON object instead. The text that you supply must adhere to the rules of the policy type you specify in the ``Type`` parameter. The following AWS Organizations quotas are enforced for the maximum size of a policy document: - Service control policies: 5,120 characters - AI services opt-out policies: 2,500 characters - Backup policies: 10,000 characters - Tag policies: 10,000 characters For more information about Organizations service quotas, see `Quotas for AWS Organizations <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html>`_ in the *AWS Organizations User Guide* .
        :param name: Name of the policy. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter is a string of any of the characters in the ASCII character range.
        :param type: The type of policy to create.
        :param description: Human readable description of the policy.
        :param tags: A list of tags that you want to attach to the newly created policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide. .. epigraph:: If any one of the tags is not valid or if you exceed the allowed number of tags for a policy, then the entire request fails and the policy is not created.
        :param target_ids: List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to. You can get the ID by calling the `ListRoots <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html>`_ , `ListOrganizationalUnitsForParent <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html>`_ , or `ListAccounts <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html>`_ operations. If you don't specify this parameter, the policy is created but not attached to any organization resource. The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a target ID string requires one of the following: - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits. - *Account* - A string that consists of exactly 12 digits. - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_organizations as organizations
            
            # content: Any
            
            cfn_policy_props = organizations.CfnPolicyProps(
                content=content,
                name="name",
                type="type",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                target_ids=["targetIds"]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__544be01c589611e04faed808433966307bb111627f81a689fb735a3a6ff28a47)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument target_ids", value=target_ids, expected_type=type_hints["target_ids"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
            "name": name,
            "type": type,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags
        if target_ids is not None:
            self._values["target_ids"] = target_ids

    @builtins.property
    def content(self) -> typing.Any:
        '''The policy text content. You can specify the policy content as a JSON object or a JSON string.

        .. epigraph::

           When you specify the policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the policy content as a JSON object instead.

        The text that you supply must adhere to the rules of the policy type you specify in the ``Type`` parameter. The following AWS Organizations quotas are enforced for the maximum size of a policy document:

        - Service control policies: 5,120 characters
        - AI services opt-out policies: 2,500 characters
        - Backup policies: 10,000 characters
        - Tag policies: 10,000 characters

        For more information about Organizations service quotas, see `Quotas for AWS Organizations <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_reference_limits.html>`_ in the *AWS Organizations User Guide* .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''Name of the policy.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ that is used to validate this parameter is a string of any of the characters in the ASCII character range.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of policy to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''Human readable description of the policy.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created policy.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the AWS Organizations User Guide.
        .. epigraph::

           If any one of the tags is not valid or if you exceed the allowed number of tags for a policy, then the entire request fails and the policy is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def target_ids(self) -> typing.Optional[typing.List[builtins.str]]:
        '''List of unique identifiers (IDs) of the root, OU, or account that you want to attach the policy to.

        You can get the ID by calling the `ListRoots <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListRoots.html>`_ , `ListOrganizationalUnitsForParent <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListOrganizationalUnitsForParent.html>`_ , or `ListAccounts <https://docs.aws.amazon.com/organizations/latest/APIReference/API_ListAccounts.html>`_ operations. If you don't specify this parameter, the policy is created but not attached to any organization resource.

        The `regex pattern <https://docs.aws.amazon.com/http://wikipedia.org/wiki/regex>`_ for a target ID string requires one of the following:

        - *Root* - A string that begins with "r-" followed by from 4 to 32 lowercase letters or digits.
        - *Account* - A string that consists of exactly 12 digits.
        - *Organizational unit (OU)* - A string that begins with "ou-" followed by from 4 to 32 lowercase letters or digits (the ID of the root that the OU is in). This string is followed by a second "-" dash and from 8 to 32 additional lowercase letters or digits.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-policy.html#cfn-organizations-policy-targetids
        '''
        result = self._values.get("target_ids")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnResourcePolicy(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_organizations.CfnResourcePolicy",
):
    '''Creates or updates a resource-based delegation policy that can be used to delegate policy management for AWS Organizations to specified member accounts to perform policy actions that are by default available only to the management account.

    For more information about delegated policy management, see `Delegated administrator for AWS Organizations <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_delegate_policies.html>`_ in the *AWS Organizations User Guide* .

    You can only call this operation from the organization's management account.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html
    :cloudformationResource: AWS::Organizations::ResourcePolicy
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_organizations as organizations
        
        # content: Any
        
        cfn_resource_policy = organizations.CfnResourcePolicy(self, "MyCfnResourcePolicy",
            content=content,
        
            # the properties below are optional
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
        content: typing.Any,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param content: The policy text of the organization resource policy. You can specify the resource policy content as a JSON object or a JSON string. .. epigraph:: When you specify the resource policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the resource policy content as a JSON object instead.
        :param tags: A list of tags that you want to attach to the newly created resource policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the *AWS Organizations User Guide* . .. epigraph:: If any one of the tags is not valid or if you exceed the allowed number of tags for the resource policy, then the entire request fails and the resource policy is not created.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9208421dfafb85e674bb3b797871f578fa0566480e15ed57d8dbc67fd20d87f)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnResourcePolicyProps(content=content, tags=tags)

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3580a73dde22a778909b428073f1b84b8c546326b9e40056a8a6853799683bf)
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
            type_hints = typing.get_type_hints(_typecheckingstub__ba3e9444ffb4b11756c647f1666a242a0bb6d1c2dbb0fd52752f94205ac09af2)
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
        '''Returns the Amazon Resource Name (ARN) of the policy.

        For example: ``arn:aws:organizations::111111111111:resourcepolicy/o-exampleorgid/rp-examplepolicyid111`` .

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrId")
    def attr_id(self) -> builtins.str:
        '''Returns the unique identifier (ID) of the resource policy.

        For example: ``rp-examplepolicyid111`` .

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
    @jsii.member(jsii_name="content")
    def content(self) -> typing.Any:
        '''The policy text of the organization resource policy.'''
        return typing.cast(typing.Any, jsii.get(self, "content"))

    @content.setter
    def content(self, value: typing.Any) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1a62f3cef96b84d09856779bec28b78a1d418f3c268511a050c8b1af032a00bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "content", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created resource policy.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__164d77bb0e3c4701ced04ca47a3969c95a5eff28be165197ce2e498bf32cedd1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_organizations.CfnResourcePolicyProps",
    jsii_struct_bases=[],
    name_mapping={"content": "content", "tags": "tags"},
)
class CfnResourcePolicyProps:
    def __init__(
        self,
        *,
        content: typing.Any,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnResourcePolicy``.

        :param content: The policy text of the organization resource policy. You can specify the resource policy content as a JSON object or a JSON string. .. epigraph:: When you specify the resource policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the resource policy content as a JSON object instead.
        :param tags: A list of tags that you want to attach to the newly created resource policy. For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the *AWS Organizations User Guide* . .. epigraph:: If any one of the tags is not valid or if you exceed the allowed number of tags for the resource policy, then the entire request fails and the resource policy is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_organizations as organizations
            
            # content: Any
            
            cfn_resource_policy_props = organizations.CfnResourcePolicyProps(
                content=content,
            
                # the properties below are optional
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37cd3de3e4908cd34c5eb0c9d1d4d248a5bbe3e921f6d262efcfbc7acdd5bf4d)
            check_type(argname="argument content", value=content, expected_type=type_hints["content"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "content": content,
        }
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def content(self) -> typing.Any:
        '''The policy text of the organization resource policy.

        You can specify the resource policy content as a JSON object or a JSON string.
        .. epigraph::

           When you specify the resource policy content as a JSON string, you can't perform drift detection on the CloudFormation stack. For this reason, we recommend specifying the resource policy content as a JSON object instead.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html#cfn-organizations-resourcepolicy-content
        '''
        result = self._values.get("content")
        assert result is not None, "Required property 'content' is missing"
        return typing.cast(typing.Any, result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A list of tags that you want to attach to the newly created resource policy.

        For each tag in the list, you must specify both a tag key and a value. You can set the value to an empty string, but you can't set it to ``null`` . For more information about tagging, see `Tagging AWS Organizations resources <https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html>`_ in the *AWS Organizations User Guide* .
        .. epigraph::

           If any one of the tags is not valid or if you exceed the allowed number of tags for the resource policy, then the entire request fails and the resource policy is not created.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-organizations-resourcepolicy.html#cfn-organizations-resourcepolicy-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnResourcePolicyProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnAccount",
    "CfnAccountProps",
    "CfnOrganization",
    "CfnOrganizationProps",
    "CfnOrganizationalUnit",
    "CfnOrganizationalUnitProps",
    "CfnPolicy",
    "CfnPolicyProps",
    "CfnResourcePolicy",
    "CfnResourcePolicyProps",
]

publication.publish()

def _typecheckingstub__717b5f787efa43cf2d1c6b1edf32de9bd64cd50c67b6e29cf7e1d6df0f5f1b60(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_name: builtins.str,
    email: builtins.str,
    parent_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ee3ea086c724fb0935ee8a727937a17ae19b987a8ade49b1405a7787feb7e3bc(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__80bdf2bd3ebcd33351d23efb5a5fbe768927b4510acf316c02ac29e5ffcca33a(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c7cb80343b6f0f43ba7a94207203ab7cefaa6c6f61ec38391afffdb4896b52f1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fb3017540fda5760817d479375b8f0ba4860d2d1001cb43056042fc31d63a8f9(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4341d69ba10680d0ef646a879e2ef2e66709e58b62fb62e8d3e1b8008424fd63(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70acd1418e03b2ec3a6e3ad06a5c89c09a87bc96955d07b91a2af5820d3ded62(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__797fecb1b9a4bafd998e385c8ea18d8b31431a28a593cf9eba2da34a96ca8e0a(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a77bb3f433e62d91418b11b634f558fe79904da5ba0000f7cb7c650162add452(
    *,
    account_name: builtins.str,
    email: builtins.str,
    parent_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
    role_name: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__450a54c6b7334fcb8f406a9a29b8e1f90a618bcbd127f2d5a6a9fa43ff254400(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    feature_set: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a0b1a88993c76738edf5e9d3584d058cabe1cfc259fb5d620589d5c23507de91(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96e2cf417d73c47f4cdfd81355199f9352be808cebdc6968077c1559c996fd16(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bba27bb9e125d71f0e3f25eaa03ce169e5b7e47cf184fcaeb273ce584181b51d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__232c106aefcec7adaf1b3c73c0f809bd72527d672e2faf2ac3e81e72e8f01c48(
    *,
    feature_set: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__05eb3e3a6c1c8de7f03913252600dcc42e4c1e99dbbab3f47a3fb8e4ce5ffcec(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    parent_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b0f1c1e40ee57749b1e3e89c931bad8d33532e5bc09dccfa20942e74efb5d7d5(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca29cbd7f58c4e45178ac57de78ce34d515cd266bd0b2ba6e89c48cdf3ddfc0d(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2fc5c2614f792a6493956c330d3c0260c5284cf30143bd369380d3522da66691(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e484a48f669e683ffa481185c24f4c123298d1a7e9bbf68822a98598a2faaa02(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__eabed8f386c5c6fcea2646194b0879df9b16b1d40979baac245b456985dfa3e7(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0140abb0fae0d0670b748f08be863eb25b5afb304506c41736e4ebe5046a1191(
    *,
    name: builtins.str,
    parent_id: builtins.str,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9c8ac465f7818132d3539ff8d8e22250305dad104185434533d033da8a80adad(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: typing.Any,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__08e107e9c8d61d1f582ba132c6a4d229d6f0e045a4e54986638403cf2fea7f0d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1174ab6fdd21c443893a2bf14c16d0f3d4c868f39d0a37fefcfb8a7714bd3ffa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1191c6f193a4faa8d4257d158518469a85c6127f725cdf681af3d969aea39846(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cb096f73e44ea3f62f85c771fef970b636d4d893157d1035d741a52506ae20f6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9823ab486df28286ddcf2d4e607740eed95089b4d80a6e2a7a858e37af2e521a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__15f0eb8f96a555ab850e02c78f1d5319de15607de2d6cecc5449543f8a58d24d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9caafe6d9a16db2e71e0d35514c7cc53b1f7f3b30806cee494691748e49625f2(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b5e07984d6cb568abac54dca9143f32081c21cefa3f9f57283a87b6c35a1fd90(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__544be01c589611e04faed808433966307bb111627f81a689fb735a3a6ff28a47(
    *,
    content: typing.Any,
    name: builtins.str,
    type: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    target_ids: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9208421dfafb85e674bb3b797871f578fa0566480e15ed57d8dbc67fd20d87f(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    content: typing.Any,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3580a73dde22a778909b428073f1b84b8c546326b9e40056a8a6853799683bf(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba3e9444ffb4b11756c647f1666a242a0bb6d1c2dbb0fd52752f94205ac09af2(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1a62f3cef96b84d09856779bec28b78a1d418f3c268511a050c8b1af032a00bc(
    value: typing.Any,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__164d77bb0e3c4701ced04ca47a3969c95a5eff28be165197ce2e498bf32cedd1(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37cd3de3e4908cd34c5eb0c9d1d4d248a5bbe3e921f6d262efcfbc7acdd5bf4d(
    *,
    content: typing.Any,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass
