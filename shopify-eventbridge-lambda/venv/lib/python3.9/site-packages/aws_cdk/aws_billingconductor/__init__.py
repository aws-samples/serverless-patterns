'''
# AWS::BillingConductor Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_billingconductor as billingconductor
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for BillingConductor construct libraries](https://constructs.dev/search?q=billingconductor)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::BillingConductor resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BillingConductor.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::BillingConductor](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_BillingConductor.html).

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
class CfnBillingGroup(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroup",
):
    '''Creates a billing group that resembles a consolidated billing family that AWS charges, based off of the predefined pricing plan computation.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html
    :cloudformationResource: AWS::BillingConductor::BillingGroup
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_billing_group = billingconductor.CfnBillingGroup(self, "MyCfnBillingGroup",
            account_grouping=billingconductor.CfnBillingGroup.AccountGroupingProperty(
                linked_account_ids=["linkedAccountIds"],
        
                # the properties below are optional
                auto_associate=False
            ),
            computation_preference=billingconductor.CfnBillingGroup.ComputationPreferenceProperty(
                pricing_plan_arn="pricingPlanArn"
            ),
            name="name",
            primary_account_id="primaryAccountId",
        
            # the properties below are optional
            description="description",
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
        account_grouping: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBillingGroup.AccountGroupingProperty", typing.Dict[builtins.str, typing.Any]]],
        computation_preference: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBillingGroup.ComputationPreferenceProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        primary_account_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param account_grouping: The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family.
        :param computation_preference: The preferences and settings that will be used to compute the AWS charges for a billing group.
        :param name: The billing group's name.
        :param primary_account_id: The account ID that serves as the main account in a billing group.
        :param description: The description of the billing group.
        :param tags: A map that contains tag keys and tag values that are attached to a billing group.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__34db7ef1df00bd83f1d6bc7787b13169d6053ecbe4f7a96747e98db547bcfa17)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBillingGroupProps(
            account_grouping=account_grouping,
            computation_preference=computation_preference,
            name=name,
            primary_account_id=primary_account_id,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a507333709cfb3aa5833139ad157de60af6d4fe1d56b93b8ffd9a4fd53641d3f)
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
            type_hints = typing.get_type_hints(_typecheckingstub__b017205194e3316c5a3b5b35d22fe320f283f813f358b9276e7d7baf9c9ea826)
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
        '''The Amazon Resource Name (ARN) of the created billing group.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time the billing group was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the billing group was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSize")
    def attr_size(self) -> jsii.Number:
        '''The number of accounts in the particular billing group.

        :cloudformationAttribute: Size
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSize"))

    @builtins.property
    @jsii.member(jsii_name="attrStatus")
    def attr_status(self) -> builtins.str:
        '''The billing group status.

        Only one of the valid values can be used.

        :cloudformationAttribute: Status
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatus"))

    @builtins.property
    @jsii.member(jsii_name="attrStatusReason")
    def attr_status_reason(self) -> builtins.str:
        '''The reason why the billing group is in its current status.

        :cloudformationAttribute: StatusReason
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrStatusReason"))

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
    @jsii.member(jsii_name="accountGrouping")
    def account_grouping(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBillingGroup.AccountGroupingProperty"]:
        '''The set of accounts that will be under the billing group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBillingGroup.AccountGroupingProperty"], jsii.get(self, "accountGrouping"))

    @account_grouping.setter
    def account_grouping(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBillingGroup.AccountGroupingProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f9c708fbe7d54cdef59ed3204494cecda18538e1eec10d86fd8f55ae7daf752)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountGrouping", value)

    @builtins.property
    @jsii.member(jsii_name="computationPreference")
    def computation_preference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBillingGroup.ComputationPreferenceProperty"]:
        '''The preferences and settings that will be used to compute the AWS charges for a billing group.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBillingGroup.ComputationPreferenceProperty"], jsii.get(self, "computationPreference"))

    @computation_preference.setter
    def computation_preference(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBillingGroup.ComputationPreferenceProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41f3295fe992f9cb25a58aec6654eb24d1e80cbee0cd3de14d958df63c247d19)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "computationPreference", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The billing group's name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b8ed4a5183989c6d90d5d14a8b43461549c879acf7cb150cd90684591ebd43ab)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="primaryAccountId")
    def primary_account_id(self) -> builtins.str:
        '''The account ID that serves as the main account in a billing group.'''
        return typing.cast(builtins.str, jsii.get(self, "primaryAccountId"))

    @primary_account_id.setter
    def primary_account_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__646e42b3eea2692844d00bd93cbeba06bbc5856813d7c83f651e58c4b732edb1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "primaryAccountId", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the billing group.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4fc1781db3881f01d158fbbb578c5ea178837f7c8778e4d3e24edfbbb0f4a04d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a billing group.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b79940f00b13b42629eb04481540a4b5f0ae2c81a08ba0818cb87b23aa91dbcd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroup.AccountGroupingProperty",
        jsii_struct_bases=[],
        name_mapping={
            "linked_account_ids": "linkedAccountIds",
            "auto_associate": "autoAssociate",
        },
    )
    class AccountGroupingProperty:
        def __init__(
            self,
            *,
            linked_account_ids: typing.Sequence[builtins.str],
            auto_associate: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The set of accounts that will be under the billing group.

            The set of accounts resemble the linked accounts in a consolidated billing family.

            :param linked_account_ids: The account IDs that make up the billing group. Account IDs must be a part of the consolidated billing family, and not associated with another billing group.
            :param auto_associate: Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                account_grouping_property = billingconductor.CfnBillingGroup.AccountGroupingProperty(
                    linked_account_ids=["linkedAccountIds"],
                
                    # the properties below are optional
                    auto_associate=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f49e139e00b0b5c04a1b1b546023b83549fcc6843b2bc7fa73b39fd6736ee578)
                check_type(argname="argument linked_account_ids", value=linked_account_ids, expected_type=type_hints["linked_account_ids"])
                check_type(argname="argument auto_associate", value=auto_associate, expected_type=type_hints["auto_associate"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "linked_account_ids": linked_account_ids,
            }
            if auto_associate is not None:
                self._values["auto_associate"] = auto_associate

        @builtins.property
        def linked_account_ids(self) -> typing.List[builtins.str]:
            '''The account IDs that make up the billing group.

            Account IDs must be a part of the consolidated billing family, and not associated with another billing group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html#cfn-billingconductor-billinggroup-accountgrouping-linkedaccountids
            '''
            result = self._values.get("linked_account_ids")
            assert result is not None, "Required property 'linked_account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def auto_associate(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-accountgrouping.html#cfn-billingconductor-billinggroup-accountgrouping-autoassociate
            '''
            result = self._values.get("auto_associate")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AccountGroupingProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroup.ComputationPreferenceProperty",
        jsii_struct_bases=[],
        name_mapping={"pricing_plan_arn": "pricingPlanArn"},
    )
    class ComputationPreferenceProperty:
        def __init__(self, *, pricing_plan_arn: builtins.str) -> None:
            '''The preferences and settings that will be used to compute the AWS charges for a billing group.

            :param pricing_plan_arn: The Amazon Resource Name (ARN) of the pricing plan used to compute the AWS charges for a billing group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                computation_preference_property = billingconductor.CfnBillingGroup.ComputationPreferenceProperty(
                    pricing_plan_arn="pricingPlanArn"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__03d110017851f76b580f2a5cc19924dea2d85571ea604024b2f8bf6bf499de02)
                check_type(argname="argument pricing_plan_arn", value=pricing_plan_arn, expected_type=type_hints["pricing_plan_arn"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "pricing_plan_arn": pricing_plan_arn,
            }

        @builtins.property
        def pricing_plan_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the pricing plan used to compute the AWS charges for a billing group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-billinggroup-computationpreference.html#cfn-billingconductor-billinggroup-computationpreference-pricingplanarn
            '''
            result = self._values.get("pricing_plan_arn")
            assert result is not None, "Required property 'pricing_plan_arn' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ComputationPreferenceProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnBillingGroupProps",
    jsii_struct_bases=[],
    name_mapping={
        "account_grouping": "accountGrouping",
        "computation_preference": "computationPreference",
        "name": "name",
        "primary_account_id": "primaryAccountId",
        "description": "description",
        "tags": "tags",
    },
)
class CfnBillingGroupProps:
    def __init__(
        self,
        *,
        account_grouping: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBillingGroup.AccountGroupingProperty, typing.Dict[builtins.str, typing.Any]]],
        computation_preference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBillingGroup.ComputationPreferenceProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        primary_account_id: builtins.str,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBillingGroup``.

        :param account_grouping: The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family.
        :param computation_preference: The preferences and settings that will be used to compute the AWS charges for a billing group.
        :param name: The billing group's name.
        :param primary_account_id: The account ID that serves as the main account in a billing group.
        :param description: The description of the billing group.
        :param tags: A map that contains tag keys and tag values that are attached to a billing group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_billing_group_props = billingconductor.CfnBillingGroupProps(
                account_grouping=billingconductor.CfnBillingGroup.AccountGroupingProperty(
                    linked_account_ids=["linkedAccountIds"],
            
                    # the properties below are optional
                    auto_associate=False
                ),
                computation_preference=billingconductor.CfnBillingGroup.ComputationPreferenceProperty(
                    pricing_plan_arn="pricingPlanArn"
                ),
                name="name",
                primary_account_id="primaryAccountId",
            
                # the properties below are optional
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5a5043cf89961ee1d8d0ec8cc20920f3427a03234cc6ae7ee74c77dcacf5641b)
            check_type(argname="argument account_grouping", value=account_grouping, expected_type=type_hints["account_grouping"])
            check_type(argname="argument computation_preference", value=computation_preference, expected_type=type_hints["computation_preference"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument primary_account_id", value=primary_account_id, expected_type=type_hints["primary_account_id"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "account_grouping": account_grouping,
            "computation_preference": computation_preference,
            "name": name,
            "primary_account_id": primary_account_id,
        }
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def account_grouping(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBillingGroup.AccountGroupingProperty]:
        '''The set of accounts that will be under the billing group.

        The set of accounts resemble the linked accounts in a consolidated billing family.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-accountgrouping
        '''
        result = self._values.get("account_grouping")
        assert result is not None, "Required property 'account_grouping' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBillingGroup.AccountGroupingProperty], result)

    @builtins.property
    def computation_preference(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBillingGroup.ComputationPreferenceProperty]:
        '''The preferences and settings that will be used to compute the AWS charges for a billing group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-computationpreference
        '''
        result = self._values.get("computation_preference")
        assert result is not None, "Required property 'computation_preference' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBillingGroup.ComputationPreferenceProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The billing group's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def primary_account_id(self) -> builtins.str:
        '''The account ID that serves as the main account in a billing group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-primaryaccountid
        '''
        result = self._values.get("primary_account_id")
        assert result is not None, "Required property 'primary_account_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The description of the billing group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a billing group.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-billinggroup.html#cfn-billingconductor-billinggroup-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBillingGroupProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnCustomLineItem(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem",
):
    '''Creates a custom line item that can be used to create a one-time or recurring, fixed or percentage-based charge that you can apply to a single billing group.

    You can apply custom line items to the current or previous billing period. You can create either a fee or a discount custom line item.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html
    :cloudformationResource: AWS::BillingConductor::CustomLineItem
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_custom_line_item = billingconductor.CfnCustomLineItem(self, "MyCfnCustomLineItem",
            billing_group_arn="billingGroupArn",
            name="name",
        
            # the properties below are optional
            account_id="accountId",
            billing_period_range=billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty(
                exclusive_end_billing_period="exclusiveEndBillingPeriod",
                inclusive_start_billing_period="inclusiveStartBillingPeriod"
            ),
            custom_line_item_charge_details=billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty(
                type="type",
        
                # the properties below are optional
                flat=billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                    charge_value=123
                ),
                line_item_filters=[billingconductor.CfnCustomLineItem.LineItemFilterProperty(
                    attribute="attribute",
                    match_option="matchOption",
                    values=["values"]
                )],
                percentage=billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                    percentage_value=123,
        
                    # the properties below are optional
                    child_associated_resources=["childAssociatedResources"]
                )
            ),
            description="description",
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
        billing_group_arn: builtins.str,
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        billing_period_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomLineItem.BillingPeriodRangeProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_line_item_charge_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomLineItem.CustomLineItemChargeDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param billing_group_arn: The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
        :param name: The custom line item's name.
        :param account_id: The AWS account in which this custom line item will be applied to.
        :param billing_period_range: A time range for which the custom line item is effective.
        :param custom_line_item_charge_details: The charge details of a custom line item. It should contain only one of ``Flat`` or ``Percentage`` .
        :param description: The custom line item's description. This is shown on the Bills page in association with the charge value.
        :param tags: A map that contains tag keys and tag values that are attached to a custom line item.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6c43da03f91fab487cb7b12443aac4a35ef34bfe36c0ce02a150eca1ab38512d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCustomLineItemProps(
            billing_group_arn=billing_group_arn,
            name=name,
            account_id=account_id,
            billing_period_range=billing_period_range,
            custom_line_item_charge_details=custom_line_item_charge_details,
            description=description,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cfcf661747b793b0d650045547ffc3ca4b57fc2b134a9b94da8423be2bb98d8c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__887096829aab23f12fa2a80cc56dfeb88061cdb0ef063c2e10abfb628c970840)
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
        '''The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociationSize")
    def attr_association_size(self) -> jsii.Number:
        '''The number of resources that are associated to the custom line item.

        :cloudformationAttribute: AssociationSize
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociationSize"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrCurrencyCode")
    def attr_currency_code(self) -> builtins.str:
        '''The custom line item's charge value currency.

        Only one of the valid values can be used.

        :cloudformationAttribute: CurrencyCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrCurrencyCode"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the custom line item was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrProductCode")
    def attr_product_code(self) -> builtins.str:
        '''The product code associated with the custom line item.

        :cloudformationAttribute: ProductCode
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrProductCode"))

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
    @jsii.member(jsii_name="billingGroupArn")
    def billing_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.'''
        return typing.cast(builtins.str, jsii.get(self, "billingGroupArn"))

    @billing_group_arn.setter
    def billing_group_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c3eb243d705caaf896e75795468936ff421a580587ebc80fd352abbf0b7b793e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingGroupArn", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The custom line item's name.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__199c4dc41e71d5adccf791ecf26d6b120bd52ba567a7e0882e3d5247e04aa8b7)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="accountId")
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account in which this custom line item will be applied to.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "accountId"))

    @account_id.setter
    def account_id(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__485a08cb6e43ed7a5b52fa253797377db356b8fe1ea1d3001a00d7a9b422d441)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "accountId", value)

    @builtins.property
    @jsii.member(jsii_name="billingPeriodRange")
    def billing_period_range(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.BillingPeriodRangeProperty"]]:
        '''A time range for which the custom line item is effective.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.BillingPeriodRangeProperty"]], jsii.get(self, "billingPeriodRange"))

    @billing_period_range.setter
    def billing_period_range(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.BillingPeriodRangeProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__4c5735856393235c9af0411ca8b7a8879608ebdefed633e1a33f50f454aac347)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingPeriodRange", value)

    @builtins.property
    @jsii.member(jsii_name="customLineItemChargeDetails")
    def custom_line_item_charge_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemChargeDetailsProperty"]]:
        '''The charge details of a custom line item.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemChargeDetailsProperty"]], jsii.get(self, "customLineItemChargeDetails"))

    @custom_line_item_charge_details.setter
    def custom_line_item_charge_details(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemChargeDetailsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d9dcde3b5032942c5c0db649ffe03d9f28478316ee33c4e6c60e10f14100a1f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "customLineItemChargeDetails", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom line item's description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__66dd00cf48245d48f64a76715433404bd203befdf24fdeac8e43d67e3528c1b5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a custom line item.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fa592de606b3d5a71ae8db1a73d086b2ca9f2b304f221694b72a7d7dbb74b841)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty",
        jsii_struct_bases=[],
        name_mapping={
            "exclusive_end_billing_period": "exclusiveEndBillingPeriod",
            "inclusive_start_billing_period": "inclusiveStartBillingPeriod",
        },
    )
    class BillingPeriodRangeProperty:
        def __init__(
            self,
            *,
            exclusive_end_billing_period: typing.Optional[builtins.str] = None,
            inclusive_start_billing_period: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The billing period range in which the custom line item request will be applied.

            :param exclusive_end_billing_period: The exclusive end billing period that defines a billing period range where a custom line is applied.
            :param inclusive_start_billing_period: The inclusive start billing period that defines a billing period range where a custom line is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                billing_period_range_property = billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty(
                    exclusive_end_billing_period="exclusiveEndBillingPeriod",
                    inclusive_start_billing_period="inclusiveStartBillingPeriod"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__7f0340ce72acb9f55083063edeae2412aaef1276e032edf20d1c4c04fadbcb4b)
                check_type(argname="argument exclusive_end_billing_period", value=exclusive_end_billing_period, expected_type=type_hints["exclusive_end_billing_period"])
                check_type(argname="argument inclusive_start_billing_period", value=inclusive_start_billing_period, expected_type=type_hints["inclusive_start_billing_period"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if exclusive_end_billing_period is not None:
                self._values["exclusive_end_billing_period"] = exclusive_end_billing_period
            if inclusive_start_billing_period is not None:
                self._values["inclusive_start_billing_period"] = inclusive_start_billing_period

        @builtins.property
        def exclusive_end_billing_period(self) -> typing.Optional[builtins.str]:
            '''The exclusive end billing period that defines a billing period range where a custom line is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html#cfn-billingconductor-customlineitem-billingperiodrange-exclusiveendbillingperiod
            '''
            result = self._values.get("exclusive_end_billing_period")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def inclusive_start_billing_period(self) -> typing.Optional[builtins.str]:
            '''The inclusive start billing period that defines a billing period range where a custom line is applied.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-billingperiodrange.html#cfn-billingconductor-customlineitem-billingperiodrange-inclusivestartbillingperiod
            '''
            result = self._values.get("inclusive_start_billing_period")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BillingPeriodRangeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "type": "type",
            "flat": "flat",
            "line_item_filters": "lineItemFilters",
            "percentage": "percentage",
        },
    )
    class CustomLineItemChargeDetailsProperty:
        def __init__(
            self,
            *,
            type: builtins.str,
            flat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            line_item_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomLineItem.LineItemFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            percentage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The charge details of a custom line item.

            It should contain only one of ``Flat`` or ``Percentage`` .

            :param type: The type of the custom line item that indicates whether the charge is a fee or credit.
            :param flat: A ``CustomLineItemFlatChargeDetails`` that describes the charge details of a flat custom line item.
            :param line_item_filters: A representation of the line item filter.
            :param percentage: A ``CustomLineItemPercentageChargeDetails`` that describes the charge details of a percentage custom line item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                custom_line_item_charge_details_property = billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty(
                    type="type",
                
                    # the properties below are optional
                    flat=billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                        charge_value=123
                    ),
                    line_item_filters=[billingconductor.CfnCustomLineItem.LineItemFilterProperty(
                        attribute="attribute",
                        match_option="matchOption",
                        values=["values"]
                    )],
                    percentage=billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                        percentage_value=123,
                
                        # the properties below are optional
                        child_associated_resources=["childAssociatedResources"]
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5d39d3a637475f4077ab769b05ae9d99ef31e0038d41087c4d8aa32837489e83)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument flat", value=flat, expected_type=type_hints["flat"])
                check_type(argname="argument line_item_filters", value=line_item_filters, expected_type=type_hints["line_item_filters"])
                check_type(argname="argument percentage", value=percentage, expected_type=type_hints["percentage"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
            }
            if flat is not None:
                self._values["flat"] = flat
            if line_item_filters is not None:
                self._values["line_item_filters"] = line_item_filters
            if percentage is not None:
                self._values["percentage"] = percentage

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of the custom line item that indicates whether the charge is a fee or credit.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def flat(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty"]]:
            '''A ``CustomLineItemFlatChargeDetails`` that describes the charge details of a flat custom line item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-flat
            '''
            result = self._values.get("flat")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty"]], result)

        @builtins.property
        def line_item_filters(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.LineItemFilterProperty"]]]]:
            '''A representation of the line item filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-lineitemfilters
            '''
            result = self._values.get("line_item_filters")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.LineItemFilterProperty"]]]], result)

        @builtins.property
        def percentage(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty"]]:
            '''A ``CustomLineItemPercentageChargeDetails`` that describes the charge details of a percentage custom line item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemchargedetails.html#cfn-billingconductor-customlineitem-customlineitemchargedetails-percentage
            '''
            result = self._values.get("percentage")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLineItemChargeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={"charge_value": "chargeValue"},
    )
    class CustomLineItemFlatChargeDetailsProperty:
        def __init__(self, *, charge_value: jsii.Number) -> None:
            '''The charge details of a custom line item.

            It should contain only one of ``Flat`` or ``Percentage`` .

            :param charge_value: The custom line item's fixed charge value in USD.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                custom_line_item_flat_charge_details_property = billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                    charge_value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b726e4b16dcd288cd3a1b8f64ca2a34fe91a6ed3af2a4b6ed9cd1a152e0f1626)
                check_type(argname="argument charge_value", value=charge_value, expected_type=type_hints["charge_value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "charge_value": charge_value,
            }

        @builtins.property
        def charge_value(self) -> jsii.Number:
            '''The custom line item's fixed charge value in USD.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitemflatchargedetails.html#cfn-billingconductor-customlineitem-customlineitemflatchargedetails-chargevalue
            '''
            result = self._values.get("charge_value")
            assert result is not None, "Required property 'charge_value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLineItemFlatChargeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "percentage_value": "percentageValue",
            "child_associated_resources": "childAssociatedResources",
        },
    )
    class CustomLineItemPercentageChargeDetailsProperty:
        def __init__(
            self,
            *,
            percentage_value: jsii.Number,
            child_associated_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''A representation of the charge details associated with a percentage custom line item.

            :param percentage_value: The custom line item's percentage value. This will be multiplied against the combined value of its associated resources to determine its charge value.
            :param child_associated_resources: A list of resource ARNs to associate to the percentage custom line item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                custom_line_item_percentage_charge_details_property = billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                    percentage_value=123,
                
                    # the properties below are optional
                    child_associated_resources=["childAssociatedResources"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__70a100ff1f6e7f50a04a566e9271338762ef27b2df9198ea25f76ee75dbba852)
                check_type(argname="argument percentage_value", value=percentage_value, expected_type=type_hints["percentage_value"])
                check_type(argname="argument child_associated_resources", value=child_associated_resources, expected_type=type_hints["child_associated_resources"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "percentage_value": percentage_value,
            }
            if child_associated_resources is not None:
                self._values["child_associated_resources"] = child_associated_resources

        @builtins.property
        def percentage_value(self) -> jsii.Number:
            '''The custom line item's percentage value.

            This will be multiplied against the combined value of its associated resources to determine its charge value.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html#cfn-billingconductor-customlineitem-customlineitempercentagechargedetails-percentagevalue
            '''
            result = self._values.get("percentage_value")
            assert result is not None, "Required property 'percentage_value' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def child_associated_resources(
            self,
        ) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of resource ARNs to associate to the percentage custom line item.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-customlineitempercentagechargedetails.html#cfn-billingconductor-customlineitem-customlineitempercentagechargedetails-childassociatedresources
            '''
            result = self._values.get("child_associated_resources")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CustomLineItemPercentageChargeDetailsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItem.LineItemFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "attribute": "attribute",
            "match_option": "matchOption",
            "values": "values",
        },
    )
    class LineItemFilterProperty:
        def __init__(
            self,
            *,
            attribute: builtins.str,
            match_option: builtins.str,
            values: typing.Sequence[builtins.str],
        ) -> None:
            '''A representation of the line item filter for your custom line item.

            You can use line item filters to include or exclude specific resource values from the billing group's total cost. For example, if you create a custom line item and you want to filter out a value, such as Savings Plan discounts, you can update ``LineItemFilter`` to exclude it.

            :param attribute: The attribute of the line item filter. This specifies what attribute that you can filter on.
            :param match_option: The match criteria of the line item filter. This parameter specifies whether not to include the resource value from the billing group total cost.
            :param values: The values of the line item filter. This specifies the values to filter on. Currently, you can only exclude Savings Plan discounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                line_item_filter_property = billingconductor.CfnCustomLineItem.LineItemFilterProperty(
                    attribute="attribute",
                    match_option="matchOption",
                    values=["values"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b18020b11e9da0d6827e72c5f07b3b822dfc78578e5de5d6bb554c27cdb13c82)
                check_type(argname="argument attribute", value=attribute, expected_type=type_hints["attribute"])
                check_type(argname="argument match_option", value=match_option, expected_type=type_hints["match_option"])
                check_type(argname="argument values", value=values, expected_type=type_hints["values"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "attribute": attribute,
                "match_option": match_option,
                "values": values,
            }

        @builtins.property
        def attribute(self) -> builtins.str:
            '''The attribute of the line item filter.

            This specifies what attribute that you can filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html#cfn-billingconductor-customlineitem-lineitemfilter-attribute
            '''
            result = self._values.get("attribute")
            assert result is not None, "Required property 'attribute' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def match_option(self) -> builtins.str:
            '''The match criteria of the line item filter.

            This parameter specifies whether not to include the resource value from the billing group total cost.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html#cfn-billingconductor-customlineitem-lineitemfilter-matchoption
            '''
            result = self._values.get("match_option")
            assert result is not None, "Required property 'match_option' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def values(self) -> typing.List[builtins.str]:
            '''The values of the line item filter.

            This specifies the values to filter on. Currently, you can only exclude Savings Plan discounts.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-customlineitem-lineitemfilter.html#cfn-billingconductor-customlineitem-lineitemfilter-values
            '''
            result = self._values.get("values")
            assert result is not None, "Required property 'values' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "LineItemFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnCustomLineItemProps",
    jsii_struct_bases=[],
    name_mapping={
        "billing_group_arn": "billingGroupArn",
        "name": "name",
        "account_id": "accountId",
        "billing_period_range": "billingPeriodRange",
        "custom_line_item_charge_details": "customLineItemChargeDetails",
        "description": "description",
        "tags": "tags",
    },
)
class CfnCustomLineItemProps:
    def __init__(
        self,
        *,
        billing_group_arn: builtins.str,
        name: builtins.str,
        account_id: typing.Optional[builtins.str] = None,
        billing_period_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.BillingPeriodRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        custom_line_item_charge_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.CustomLineItemChargeDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        description: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCustomLineItem``.

        :param billing_group_arn: The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.
        :param name: The custom line item's name.
        :param account_id: The AWS account in which this custom line item will be applied to.
        :param billing_period_range: A time range for which the custom line item is effective.
        :param custom_line_item_charge_details: The charge details of a custom line item. It should contain only one of ``Flat`` or ``Percentage`` .
        :param description: The custom line item's description. This is shown on the Bills page in association with the charge value.
        :param tags: A map that contains tag keys and tag values that are attached to a custom line item.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_custom_line_item_props = billingconductor.CfnCustomLineItemProps(
                billing_group_arn="billingGroupArn",
                name="name",
            
                # the properties below are optional
                account_id="accountId",
                billing_period_range=billingconductor.CfnCustomLineItem.BillingPeriodRangeProperty(
                    exclusive_end_billing_period="exclusiveEndBillingPeriod",
                    inclusive_start_billing_period="inclusiveStartBillingPeriod"
                ),
                custom_line_item_charge_details=billingconductor.CfnCustomLineItem.CustomLineItemChargeDetailsProperty(
                    type="type",
            
                    # the properties below are optional
                    flat=billingconductor.CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty(
                        charge_value=123
                    ),
                    line_item_filters=[billingconductor.CfnCustomLineItem.LineItemFilterProperty(
                        attribute="attribute",
                        match_option="matchOption",
                        values=["values"]
                    )],
                    percentage=billingconductor.CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty(
                        percentage_value=123,
            
                        # the properties below are optional
                        child_associated_resources=["childAssociatedResources"]
                    )
                ),
                description="description",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a7b2e875d39abe8a3c0b572bc75c4dac4bd0fc7005579ba31e1612f811f06c3)
            check_type(argname="argument billing_group_arn", value=billing_group_arn, expected_type=type_hints["billing_group_arn"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument account_id", value=account_id, expected_type=type_hints["account_id"])
            check_type(argname="argument billing_period_range", value=billing_period_range, expected_type=type_hints["billing_period_range"])
            check_type(argname="argument custom_line_item_charge_details", value=custom_line_item_charge_details, expected_type=type_hints["custom_line_item_charge_details"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "billing_group_arn": billing_group_arn,
            "name": name,
        }
        if account_id is not None:
            self._values["account_id"] = account_id
        if billing_period_range is not None:
            self._values["billing_period_range"] = billing_period_range
        if custom_line_item_charge_details is not None:
            self._values["custom_line_item_charge_details"] = custom_line_item_charge_details
        if description is not None:
            self._values["description"] = description
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def billing_group_arn(self) -> builtins.str:
        '''The Amazon Resource Name (ARN) that references the billing group where the custom line item applies to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billinggrouparn
        '''
        result = self._values.get("billing_group_arn")
        assert result is not None, "Required property 'billing_group_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The custom line item's name.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def account_id(self) -> typing.Optional[builtins.str]:
        '''The AWS account in which this custom line item will be applied to.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-accountid
        '''
        result = self._values.get("account_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def billing_period_range(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCustomLineItem.BillingPeriodRangeProperty]]:
        '''A time range for which the custom line item is effective.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-billingperiodrange
        '''
        result = self._values.get("billing_period_range")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCustomLineItem.BillingPeriodRangeProperty]], result)

    @builtins.property
    def custom_line_item_charge_details(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCustomLineItem.CustomLineItemChargeDetailsProperty]]:
        '''The charge details of a custom line item.

        It should contain only one of ``Flat`` or ``Percentage`` .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-customlineitemchargedetails
        '''
        result = self._values.get("custom_line_item_charge_details")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCustomLineItem.CustomLineItemChargeDetailsProperty]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The custom line item's description.

        This is shown on the Bills page in association with the charge value.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a custom line item.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-customlineitem.html#cfn-billingconductor-customlineitem-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCustomLineItemProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPricingPlan(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingPlan",
):
    '''Creates a pricing plan that is used for computing AWS charges for billing groups.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html
    :cloudformationResource: AWS::BillingConductor::PricingPlan
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_pricing_plan = billingconductor.CfnPricingPlan(self, "MyCfnPricingPlan",
            name="name",
        
            # the properties below are optional
            description="description",
            pricing_rule_arns=["pricingRuleArns"],
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
        description: typing.Optional[builtins.str] = None,
        pricing_rule_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of a pricing plan.
        :param description: The pricing plan description.
        :param pricing_rule_arns: The ``PricingRuleArns`` that are associated with the Pricing Plan.
        :param tags: A map that contains tag keys and tag values that are attached to a pricing plan.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5d0ad9e961729ad9fd5da8d3aced4288d20cd531e9ef7f77cb628016cf09c53e)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPricingPlanProps(
            name=name,
            description=description,
            pricing_rule_arns=pricing_rule_arns,
            tags=tags,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7ccc28b9652afce0100da6c48f0f841a4f01d03482cad5f13db27c4c6977cc8b)
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
            type_hints = typing.get_type_hints(_typecheckingstub__519c15a5e5c01d48960c856793b2c7ce85ee9854ef467008314abcb242d727cf)
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
        '''The Amazon Resource Name (ARN) of the created pricing plan.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time the pricing plan was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the pricing plan was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="attrSize")
    def attr_size(self) -> jsii.Number:
        '''The pricing rules count currently associated with this pricing plan list element.

        :cloudformationAttribute: Size
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrSize"))

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
        '''The name of a pricing plan.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__41e41d7b10b271443fa6aef0e38fea3a019d91e0812404846ce03c90c12d10cd)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing plan description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__85c231f6aa09dcdabd60d46d2de7a2ab0cdd8d2887b1e9e02743c4570bfd4f2f)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="pricingRuleArns")
    def pricing_rule_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ``PricingRuleArns`` that are associated with the Pricing Plan.'''
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pricingRuleArns"))

    @pricing_rule_arns.setter
    def pricing_rule_arns(
        self,
        value: typing.Optional[typing.List[builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__bb0c6a89bda77170ae2feda7aa8a342c0d3b465d274fbffaa9e26639dc7e9b06)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pricingRuleArns", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a pricing plan.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__13df144317e29f0d4607aebf7ab331e5ce6b9d66d406f1e7f703e3b979bee860)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingPlanProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "description": "description",
        "pricing_rule_arns": "pricingRuleArns",
        "tags": "tags",
    },
)
class CfnPricingPlanProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
        pricing_rule_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnPricingPlan``.

        :param name: The name of a pricing plan.
        :param description: The pricing plan description.
        :param pricing_rule_arns: The ``PricingRuleArns`` that are associated with the Pricing Plan.
        :param tags: A map that contains tag keys and tag values that are attached to a pricing plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_pricing_plan_props = billingconductor.CfnPricingPlanProps(
                name="name",
            
                # the properties below are optional
                description="description",
                pricing_rule_arns=["pricingRuleArns"],
                tags=[CfnTag(
                    key="key",
                    value="value"
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__98be78e385077b0ad00dbb126832cd4945f0fff6a024a4d8ad0bca813b09a348)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument pricing_rule_arns", value=pricing_rule_arns, expected_type=type_hints["pricing_rule_arns"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
        }
        if description is not None:
            self._values["description"] = description
        if pricing_rule_arns is not None:
            self._values["pricing_rule_arns"] = pricing_rule_arns
        if tags is not None:
            self._values["tags"] = tags

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a pricing plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing plan description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pricing_rule_arns(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The ``PricingRuleArns`` that are associated with the Pricing Plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-pricingrulearns
        '''
        result = self._values.get("pricing_rule_arns")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a pricing plan.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingplan.html#cfn-billingconductor-pricingplan-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPricingPlanProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556, _ITaggable_36806126)
class CfnPricingRule(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingRule",
):
    '''Creates a pricing rule which can be associated with a pricing plan, or a set of pricing plans.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html
    :cloudformationResource: AWS::BillingConductor::PricingRule
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_billingconductor as billingconductor
        
        cfn_pricing_rule = billingconductor.CfnPricingRule(self, "MyCfnPricingRule",
            name="name",
            scope="scope",
            type="type",
        
            # the properties below are optional
            billing_entity="billingEntity",
            description="description",
            modifier_percentage=123,
            operation="operation",
            service="service",
            tags=[CfnTag(
                key="key",
                value="value"
            )],
            tiering=billingconductor.CfnPricingRule.TieringProperty(
                free_tier=billingconductor.CfnPricingRule.FreeTierProperty(
                    activated=False
                )
            ),
            usage_type="usageType"
        )
    '''

    def __init__(
        self,
        scope_: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        name: builtins.str,
        scope: builtins.str,
        type: builtins.str,
        billing_entity: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        modifier_percentage: typing.Optional[jsii.Number] = None,
        operation: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        tiering: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPricingRule.TieringProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        usage_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope_: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param name: The name of a pricing rule.
        :param scope: The scope of pricing rule that indicates if it's globally applicable or service-specific.
        :param type: The type of pricing rule.
        :param billing_entity: The seller of services provided by AWS , their affiliates, or third-party providers selling services via AWS Marketplace .
        :param description: The pricing rule description.
        :param modifier_percentage: A percentage modifier applied on the public pricing rates.
        :param operation: Operation is the specific AWS action covered by this line item. This describes the specific usage of the line item. If the ``Scope`` attribute is set to ``SKU`` , this attribute indicates which operation the ``PricingRule`` is modifying. For example, a value of ``RunInstances:0202`` indicates the operation of running an Amazon EC2 instance.
        :param service: If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.
        :param tags: A map that contains tag keys and tag values that are attached to a pricing rule.
        :param tiering: The set of tiering configurations for the pricing rule.
        :param usage_type: Usage Type is the unit that each service uses to measure the usage of a specific type of resource.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__44900bb3a1f7831b3596ad895c7741866b619bfcbfa011b93a64dfccfe2f12dd)
            check_type(argname="argument scope_", value=scope_, expected_type=type_hints["scope_"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnPricingRuleProps(
            name=name,
            scope=scope,
            type=type,
            billing_entity=billing_entity,
            description=description,
            modifier_percentage=modifier_percentage,
            operation=operation,
            service=service,
            tags=tags,
            tiering=tiering,
            usage_type=usage_type,
        )

        jsii.create(self.__class__, self, [scope_, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__54f6a06227d0409aad15c03aabb80d10da84e9e4565906a6f637b7d0afbde8df)
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
            type_hints = typing.get_type_hints(_typecheckingstub__435bd0c3172b60b0e799ea02ab824cfcf99d08f564e94d81374374dac94b2c46)
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
        '''The Amazon Resource Name (ARN) used to uniquely identify a pricing rule.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="attrAssociatedPricingPlanCount")
    def attr_associated_pricing_plan_count(self) -> jsii.Number:
        '''The pricing plans count that this pricing rule is associated with.

        :cloudformationAttribute: AssociatedPricingPlanCount
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrAssociatedPricingPlanCount"))

    @builtins.property
    @jsii.member(jsii_name="attrCreationTime")
    def attr_creation_time(self) -> jsii.Number:
        '''The time the pricing rule was created.

        :cloudformationAttribute: CreationTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrCreationTime"))

    @builtins.property
    @jsii.member(jsii_name="attrLastModifiedTime")
    def attr_last_modified_time(self) -> jsii.Number:
        '''The most recent time the pricing rule was modified.

        :cloudformationAttribute: LastModifiedTime
        '''
        return typing.cast(jsii.Number, jsii.get(self, "attrLastModifiedTime"))

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
        '''The name of a pricing rule.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__3039a172a4634682aedec441346560ef397babef403555ad72234e1e5d769b94)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="scope")
    def scope(self) -> builtins.str:
        '''The scope of pricing rule that indicates if it's globally applicable or service-specific.'''
        return typing.cast(builtins.str, jsii.get(self, "scope"))

    @scope.setter
    def scope(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6a1c5307af8aa5caa43dca553d8d447af3178ab0e4a3ac26cec65752ec05f15a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scope", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        '''The type of pricing rule.'''
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7a50180ae9094b0615b9db3f9c8ef636dec978b56761a020d89c1307a4675919)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="billingEntity")
    def billing_entity(self) -> typing.Optional[builtins.str]:
        '''The seller of services provided by AWS , their affiliates, or third-party providers selling services via AWS Marketplace .'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "billingEntity"))

    @billing_entity.setter
    def billing_entity(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8804f523dd249bb75a1dbb95fc266bc031a17586d02e8ad390deb7d9cf69d95d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "billingEntity", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing rule description.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f6eae3ec411610683aa6f10c0c852a611cf583b2fae601d172fe4a30b49c019a)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="modifierPercentage")
    def modifier_percentage(self) -> typing.Optional[jsii.Number]:
        '''A percentage modifier applied on the public pricing rates.'''
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "modifierPercentage"))

    @modifier_percentage.setter
    def modifier_percentage(self, value: typing.Optional[jsii.Number]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__771d90964eec9268175f160032d7ea8291ba035a3544be4d3a230d2ab0a0e14e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modifierPercentage", value)

    @builtins.property
    @jsii.member(jsii_name="operation")
    def operation(self) -> typing.Optional[builtins.str]:
        '''Operation is the specific AWS action covered by this line item.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "operation"))

    @operation.setter
    def operation(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__7d68ebc2133e621366d444cdeb72c7d3573c57e8a969d73d5914cf5e6ec240c1)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "operation", value)

    @builtins.property
    @jsii.member(jsii_name="service")
    def service(self) -> typing.Optional[builtins.str]:
        '''If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "service"))

    @service.setter
    def service(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__37203a91eeadb3b5fb67c1340ae6aee4a1c64983cd50f0deb31484b24f20a3f9)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "service", value)

    @builtins.property
    @jsii.member(jsii_name="tagsRaw")
    def tags_raw(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a pricing rule.'''
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], jsii.get(self, "tagsRaw"))

    @tags_raw.setter
    def tags_raw(self, value: typing.Optional[typing.List[_CfnTag_f6864754]]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__74aa4f5ff17ac08d7ca00b5728574783a055d9af8627efe28321973e6be1f235)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tagsRaw", value)

    @builtins.property
    @jsii.member(jsii_name="tiering")
    def tiering(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPricingRule.TieringProperty"]]:
        '''The set of tiering configurations for the pricing rule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPricingRule.TieringProperty"]], jsii.get(self, "tiering"))

    @tiering.setter
    def tiering(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPricingRule.TieringProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8fe55809e6cb1b74a3bfa69e7578e482e14e7ff52be1b0106d1bcca12ff71b9d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tiering", value)

    @builtins.property
    @jsii.member(jsii_name="usageType")
    def usage_type(self) -> typing.Optional[builtins.str]:
        '''Usage Type is the unit that each service uses to measure the usage of a specific type of resource.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "usageType"))

    @usage_type.setter
    def usage_type(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__baf93d2b8fd207bde20614839c395d563684be63797e50c8d823f9277a364722)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "usageType", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingRule.FreeTierProperty",
        jsii_struct_bases=[],
        name_mapping={"activated": "activated"},
    )
    class FreeTierProperty:
        def __init__(
            self,
            *,
            activated: typing.Union[builtins.bool, _IResolvable_da3f097b],
        ) -> None:
            '''The possible AWS Free Tier configurations.

            :param activated: Activate or deactivate AWS Free Tier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-freetier.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                free_tier_property = billingconductor.CfnPricingRule.FreeTierProperty(
                    activated=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__c45d1c415857793db226459664e7a94bd5dd1a825a10fc6bae37cda80b69fde4)
                check_type(argname="argument activated", value=activated, expected_type=type_hints["activated"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "activated": activated,
            }

        @builtins.property
        def activated(self) -> typing.Union[builtins.bool, _IResolvable_da3f097b]:
            '''Activate or deactivate AWS Free Tier.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-freetier.html#cfn-billingconductor-pricingrule-freetier-activated
            '''
            result = self._values.get("activated")
            assert result is not None, "Required property 'activated' is missing"
            return typing.cast(typing.Union[builtins.bool, _IResolvable_da3f097b], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FreeTierProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingRule.TieringProperty",
        jsii_struct_bases=[],
        name_mapping={"free_tier": "freeTier"},
    )
    class TieringProperty:
        def __init__(
            self,
            *,
            free_tier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnPricingRule.FreeTierProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The set of tiering configurations for the pricing rule.

            :param free_tier: The possible AWS Free Tier configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-tiering.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_billingconductor as billingconductor
                
                tiering_property = billingconductor.CfnPricingRule.TieringProperty(
                    free_tier=billingconductor.CfnPricingRule.FreeTierProperty(
                        activated=False
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__0f3be0f4100fb92bfec0156ed2357fb7eb28b01d7081db0419a1583b15b33511)
                check_type(argname="argument free_tier", value=free_tier, expected_type=type_hints["free_tier"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if free_tier is not None:
                self._values["free_tier"] = free_tier

        @builtins.property
        def free_tier(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPricingRule.FreeTierProperty"]]:
            '''The possible AWS Free Tier configurations.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-billingconductor-pricingrule-tiering.html#cfn-billingconductor-pricingrule-tiering-freetier
            '''
            result = self._values.get("free_tier")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnPricingRule.FreeTierProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TieringProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_billingconductor.CfnPricingRuleProps",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "scope": "scope",
        "type": "type",
        "billing_entity": "billingEntity",
        "description": "description",
        "modifier_percentage": "modifierPercentage",
        "operation": "operation",
        "service": "service",
        "tags": "tags",
        "tiering": "tiering",
        "usage_type": "usageType",
    },
)
class CfnPricingRuleProps:
    def __init__(
        self,
        *,
        name: builtins.str,
        scope: builtins.str,
        type: builtins.str,
        billing_entity: typing.Optional[builtins.str] = None,
        description: typing.Optional[builtins.str] = None,
        modifier_percentage: typing.Optional[jsii.Number] = None,
        operation: typing.Optional[builtins.str] = None,
        service: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
        tiering: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPricingRule.TieringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        usage_type: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnPricingRule``.

        :param name: The name of a pricing rule.
        :param scope: The scope of pricing rule that indicates if it's globally applicable or service-specific.
        :param type: The type of pricing rule.
        :param billing_entity: The seller of services provided by AWS , their affiliates, or third-party providers selling services via AWS Marketplace .
        :param description: The pricing rule description.
        :param modifier_percentage: A percentage modifier applied on the public pricing rates.
        :param operation: Operation is the specific AWS action covered by this line item. This describes the specific usage of the line item. If the ``Scope`` attribute is set to ``SKU`` , this attribute indicates which operation the ``PricingRule`` is modifying. For example, a value of ``RunInstances:0202`` indicates the operation of running an Amazon EC2 instance.
        :param service: If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.
        :param tags: A map that contains tag keys and tag values that are attached to a pricing rule.
        :param tiering: The set of tiering configurations for the pricing rule.
        :param usage_type: Usage Type is the unit that each service uses to measure the usage of a specific type of resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_billingconductor as billingconductor
            
            cfn_pricing_rule_props = billingconductor.CfnPricingRuleProps(
                name="name",
                scope="scope",
                type="type",
            
                # the properties below are optional
                billing_entity="billingEntity",
                description="description",
                modifier_percentage=123,
                operation="operation",
                service="service",
                tags=[CfnTag(
                    key="key",
                    value="value"
                )],
                tiering=billingconductor.CfnPricingRule.TieringProperty(
                    free_tier=billingconductor.CfnPricingRule.FreeTierProperty(
                        activated=False
                    )
                ),
                usage_type="usageType"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__f17b7b061ea7b1cd3c448b9e95c4d41fd90828bb0cb9f8ce32836006c96e65af)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument billing_entity", value=billing_entity, expected_type=type_hints["billing_entity"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument modifier_percentage", value=modifier_percentage, expected_type=type_hints["modifier_percentage"])
            check_type(argname="argument operation", value=operation, expected_type=type_hints["operation"])
            check_type(argname="argument service", value=service, expected_type=type_hints["service"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument tiering", value=tiering, expected_type=type_hints["tiering"])
            check_type(argname="argument usage_type", value=usage_type, expected_type=type_hints["usage_type"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "name": name,
            "scope": scope,
            "type": type,
        }
        if billing_entity is not None:
            self._values["billing_entity"] = billing_entity
        if description is not None:
            self._values["description"] = description
        if modifier_percentage is not None:
            self._values["modifier_percentage"] = modifier_percentage
        if operation is not None:
            self._values["operation"] = operation
        if service is not None:
            self._values["service"] = service
        if tags is not None:
            self._values["tags"] = tags
        if tiering is not None:
            self._values["tiering"] = tiering
        if usage_type is not None:
            self._values["usage_type"] = usage_type

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of a pricing rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def scope(self) -> builtins.str:
        '''The scope of pricing rule that indicates if it's globally applicable or service-specific.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-scope
        '''
        result = self._values.get("scope")
        assert result is not None, "Required property 'scope' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''The type of pricing rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-type
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def billing_entity(self) -> typing.Optional[builtins.str]:
        '''The seller of services provided by AWS , their affiliates, or third-party providers selling services via AWS Marketplace .

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-billingentity
        '''
        result = self._values.get("billing_entity")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The pricing rule description.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def modifier_percentage(self) -> typing.Optional[jsii.Number]:
        '''A percentage modifier applied on the public pricing rates.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-modifierpercentage
        '''
        result = self._values.get("modifier_percentage")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def operation(self) -> typing.Optional[builtins.str]:
        '''Operation is the specific AWS action covered by this line item.

        This describes the specific usage of the line item.

        If the ``Scope`` attribute is set to ``SKU`` , this attribute indicates which operation the ``PricingRule`` is modifying. For example, a value of ``RunInstances:0202`` indicates the operation of running an Amazon EC2 instance.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-operation
        '''
        result = self._values.get("operation")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def service(self) -> typing.Optional[builtins.str]:
        '''If the ``Scope`` attribute is ``SERVICE`` , this attribute indicates which service the ``PricingRule`` is applicable for.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-service
        '''
        result = self._values.get("service")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.List[_CfnTag_f6864754]]:
        '''A map that contains tag keys and tag values that are attached to a pricing rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.List[_CfnTag_f6864754]], result)

    @builtins.property
    def tiering(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPricingRule.TieringProperty]]:
        '''The set of tiering configurations for the pricing rule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-tiering
        '''
        result = self._values.get("tiering")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPricingRule.TieringProperty]], result)

    @builtins.property
    def usage_type(self) -> typing.Optional[builtins.str]:
        '''Usage Type is the unit that each service uses to measure the usage of a specific type of resource.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-billingconductor-pricingrule.html#cfn-billingconductor-pricingrule-usagetype
        '''
        result = self._values.get("usage_type")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnPricingRuleProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBillingGroup",
    "CfnBillingGroupProps",
    "CfnCustomLineItem",
    "CfnCustomLineItemProps",
    "CfnPricingPlan",
    "CfnPricingPlanProps",
    "CfnPricingRule",
    "CfnPricingRuleProps",
]

publication.publish()

def _typecheckingstub__34db7ef1df00bd83f1d6bc7787b13169d6053ecbe4f7a96747e98db547bcfa17(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    account_grouping: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBillingGroup.AccountGroupingProperty, typing.Dict[builtins.str, typing.Any]]],
    computation_preference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBillingGroup.ComputationPreferenceProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    primary_account_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a507333709cfb3aa5833139ad157de60af6d4fe1d56b93b8ffd9a4fd53641d3f(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b017205194e3316c5a3b5b35d22fe320f283f813f358b9276e7d7baf9c9ea826(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f9c708fbe7d54cdef59ed3204494cecda18538e1eec10d86fd8f55ae7daf752(
    value: typing.Union[_IResolvable_da3f097b, CfnBillingGroup.AccountGroupingProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41f3295fe992f9cb25a58aec6654eb24d1e80cbee0cd3de14d958df63c247d19(
    value: typing.Union[_IResolvable_da3f097b, CfnBillingGroup.ComputationPreferenceProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b8ed4a5183989c6d90d5d14a8b43461549c879acf7cb150cd90684591ebd43ab(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__646e42b3eea2692844d00bd93cbeba06bbc5856813d7c83f651e58c4b732edb1(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4fc1781db3881f01d158fbbb578c5ea178837f7c8778e4d3e24edfbbb0f4a04d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b79940f00b13b42629eb04481540a4b5f0ae2c81a08ba0818cb87b23aa91dbcd(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f49e139e00b0b5c04a1b1b546023b83549fcc6843b2bc7fa73b39fd6736ee578(
    *,
    linked_account_ids: typing.Sequence[builtins.str],
    auto_associate: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__03d110017851f76b580f2a5cc19924dea2d85571ea604024b2f8bf6bf499de02(
    *,
    pricing_plan_arn: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a5043cf89961ee1d8d0ec8cc20920f3427a03234cc6ae7ee74c77dcacf5641b(
    *,
    account_grouping: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBillingGroup.AccountGroupingProperty, typing.Dict[builtins.str, typing.Any]]],
    computation_preference: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBillingGroup.ComputationPreferenceProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    primary_account_id: builtins.str,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6c43da03f91fab487cb7b12443aac4a35ef34bfe36c0ce02a150eca1ab38512d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    billing_group_arn: builtins.str,
    name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    billing_period_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.BillingPeriodRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_line_item_charge_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.CustomLineItemChargeDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cfcf661747b793b0d650045547ffc3ca4b57fc2b134a9b94da8423be2bb98d8c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__887096829aab23f12fa2a80cc56dfeb88061cdb0ef063c2e10abfb628c970840(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c3eb243d705caaf896e75795468936ff421a580587ebc80fd352abbf0b7b793e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__199c4dc41e71d5adccf791ecf26d6b120bd52ba567a7e0882e3d5247e04aa8b7(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__485a08cb6e43ed7a5b52fa253797377db356b8fe1ea1d3001a00d7a9b422d441(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4c5735856393235c9af0411ca8b7a8879608ebdefed633e1a33f50f454aac347(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCustomLineItem.BillingPeriodRangeProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d9dcde3b5032942c5c0db649ffe03d9f28478316ee33c4e6c60e10f14100a1f9(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCustomLineItem.CustomLineItemChargeDetailsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__66dd00cf48245d48f64a76715433404bd203befdf24fdeac8e43d67e3528c1b5(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__fa592de606b3d5a71ae8db1a73d086b2ca9f2b304f221694b72a7d7dbb74b841(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7f0340ce72acb9f55083063edeae2412aaef1276e032edf20d1c4c04fadbcb4b(
    *,
    exclusive_end_billing_period: typing.Optional[builtins.str] = None,
    inclusive_start_billing_period: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d39d3a637475f4077ab769b05ae9d99ef31e0038d41087c4d8aa32837489e83(
    *,
    type: builtins.str,
    flat: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.CustomLineItemFlatChargeDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    line_item_filters: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.LineItemFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    percentage: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.CustomLineItemPercentageChargeDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b726e4b16dcd288cd3a1b8f64ca2a34fe91a6ed3af2a4b6ed9cd1a152e0f1626(
    *,
    charge_value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__70a100ff1f6e7f50a04a566e9271338762ef27b2df9198ea25f76ee75dbba852(
    *,
    percentage_value: jsii.Number,
    child_associated_resources: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b18020b11e9da0d6827e72c5f07b3b822dfc78578e5de5d6bb554c27cdb13c82(
    *,
    attribute: builtins.str,
    match_option: builtins.str,
    values: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a7b2e875d39abe8a3c0b572bc75c4dac4bd0fc7005579ba31e1612f811f06c3(
    *,
    billing_group_arn: builtins.str,
    name: builtins.str,
    account_id: typing.Optional[builtins.str] = None,
    billing_period_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.BillingPeriodRangeProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    custom_line_item_charge_details: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCustomLineItem.CustomLineItemChargeDetailsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    description: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5d0ad9e961729ad9fd5da8d3aced4288d20cd531e9ef7f77cb628016cf09c53e(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pricing_rule_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7ccc28b9652afce0100da6c48f0f841a4f01d03482cad5f13db27c4c6977cc8b(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__519c15a5e5c01d48960c856793b2c7ce85ee9854ef467008314abcb242d727cf(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__41e41d7b10b271443fa6aef0e38fea3a019d91e0812404846ce03c90c12d10cd(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__85c231f6aa09dcdabd60d46d2de7a2ab0cdd8d2887b1e9e02743c4570bfd4f2f(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bb0c6a89bda77170ae2feda7aa8a342c0d3b465d274fbffaa9e26639dc7e9b06(
    value: typing.Optional[typing.List[builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__13df144317e29f0d4607aebf7ab331e5ce6b9d66d406f1e7f703e3b979bee860(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__98be78e385077b0ad00dbb126832cd4945f0fff6a024a4d8ad0bca813b09a348(
    *,
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
    pricing_rule_arns: typing.Optional[typing.Sequence[builtins.str]] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__44900bb3a1f7831b3596ad895c7741866b619bfcbfa011b93a64dfccfe2f12dd(
    scope_: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    name: builtins.str,
    scope: builtins.str,
    type: builtins.str,
    billing_entity: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    modifier_percentage: typing.Optional[jsii.Number] = None,
    operation: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    tiering: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPricingRule.TieringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    usage_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__54f6a06227d0409aad15c03aabb80d10da84e9e4565906a6f637b7d0afbde8df(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__435bd0c3172b60b0e799ea02ab824cfcf99d08f564e94d81374374dac94b2c46(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__3039a172a4634682aedec441346560ef397babef403555ad72234e1e5d769b94(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6a1c5307af8aa5caa43dca553d8d447af3178ab0e4a3ac26cec65752ec05f15a(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7a50180ae9094b0615b9db3f9c8ef636dec978b56761a020d89c1307a4675919(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8804f523dd249bb75a1dbb95fc266bc031a17586d02e8ad390deb7d9cf69d95d(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f6eae3ec411610683aa6f10c0c852a611cf583b2fae601d172fe4a30b49c019a(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__771d90964eec9268175f160032d7ea8291ba035a3544be4d3a230d2ab0a0e14e(
    value: typing.Optional[jsii.Number],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__7d68ebc2133e621366d444cdeb72c7d3573c57e8a969d73d5914cf5e6ec240c1(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37203a91eeadb3b5fb67c1340ae6aee4a1c64983cd50f0deb31484b24f20a3f9(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__74aa4f5ff17ac08d7ca00b5728574783a055d9af8627efe28321973e6be1f235(
    value: typing.Optional[typing.List[_CfnTag_f6864754]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8fe55809e6cb1b74a3bfa69e7578e482e14e7ff52be1b0106d1bcca12ff71b9d(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnPricingRule.TieringProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__baf93d2b8fd207bde20614839c395d563684be63797e50c8d823f9277a364722(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c45d1c415857793db226459664e7a94bd5dd1a825a10fc6bae37cda80b69fde4(
    *,
    activated: typing.Union[builtins.bool, _IResolvable_da3f097b],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0f3be0f4100fb92bfec0156ed2357fb7eb28b01d7081db0419a1583b15b33511(
    *,
    free_tier: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPricingRule.FreeTierProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f17b7b061ea7b1cd3c448b9e95c4d41fd90828bb0cb9f8ce32836006c96e65af(
    *,
    name: builtins.str,
    scope: builtins.str,
    type: builtins.str,
    billing_entity: typing.Optional[builtins.str] = None,
    description: typing.Optional[builtins.str] = None,
    modifier_percentage: typing.Optional[jsii.Number] = None,
    operation: typing.Optional[builtins.str] = None,
    service: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Sequence[typing.Union[_CfnTag_f6864754, typing.Dict[builtins.str, typing.Any]]]] = None,
    tiering: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnPricingRule.TieringProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    usage_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
