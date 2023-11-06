'''
# AWS Budgets Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_budgets as budgets
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for Budgets construct libraries](https://constructs.dev/search?q=budgets)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::Budgets resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Budgets.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::Budgets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Budgets.html).

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
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556)
class CfnBudget(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_budgets.CfnBudget",
):
    '''The ``AWS::Budgets::Budget`` resource allows customers to take pre-defined actions that will trigger once a budget threshold has been exceeded.

    creates, replaces, or deletes budgets for Billing and Cost Management. For more information, see `Managing Your Costs with Budgets <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html>`_ in the *AWS Billing and Cost Management User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_budgets as budgets
        
        # cost_filters: Any
        # planned_budget_limits: Any
        
        cfn_budget = budgets.CfnBudget(self, "MyCfnBudget",
            budget=budgets.CfnBudget.BudgetDataProperty(
                budget_type="budgetType",
                time_unit="timeUnit",
        
                # the properties below are optional
                auto_adjust_data=budgets.CfnBudget.AutoAdjustDataProperty(
                    auto_adjust_type="autoAdjustType",
        
                    # the properties below are optional
                    historical_options=budgets.CfnBudget.HistoricalOptionsProperty(
                        budget_adjustment_period=123
                    )
                ),
                budget_limit=budgets.CfnBudget.SpendProperty(
                    amount=123,
                    unit="unit"
                ),
                budget_name="budgetName",
                cost_filters=cost_filters,
                cost_types=budgets.CfnBudget.CostTypesProperty(
                    include_credit=False,
                    include_discount=False,
                    include_other_subscription=False,
                    include_recurring=False,
                    include_refund=False,
                    include_subscription=False,
                    include_support=False,
                    include_tax=False,
                    include_upfront=False,
                    use_amortized=False,
                    use_blended=False
                ),
                planned_budget_limits=planned_budget_limits,
                time_period=budgets.CfnBudget.TimePeriodProperty(
                    end="end",
                    start="start"
                )
            ),
        
            # the properties below are optional
            notifications_with_subscribers=[budgets.CfnBudget.NotificationWithSubscribersProperty(
                notification=budgets.CfnBudget.NotificationProperty(
                    comparison_operator="comparisonOperator",
                    notification_type="notificationType",
                    threshold=123,
        
                    # the properties below are optional
                    threshold_type="thresholdType"
                ),
                subscribers=[budgets.CfnBudget.SubscriberProperty(
                    address="address",
                    subscription_type="subscriptionType"
                )]
            )]
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        budget: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.BudgetDataProperty", typing.Dict[builtins.str, typing.Any]]],
        notifications_with_subscribers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.NotificationWithSubscribersProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param budget: The budget object that you want to create.
        :param notifications_with_subscribers: A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your ``CreateBudget`` call, AWS creates the notifications and subscribers for you.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__fcf9a7d2538a7b213b0959a8dca9ebac8bd9adbb67b3989e4ad2e983d215ccb6)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBudgetProps(
            budget=budget,
            notifications_with_subscribers=notifications_with_subscribers,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e48291da0e0d52b22d4094e08b1071a9eb7e9781ef841ed60fbf1c118c7db23c)
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
            type_hints = typing.get_type_hints(_typecheckingstub__9be790a4c777b9d846ffd5e29641d5e3c1e0001a4faf20e8512e5ee5dc73a48f)
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
    @jsii.member(jsii_name="budget")
    def budget(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBudget.BudgetDataProperty"]:
        '''The budget object that you want to create.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBudget.BudgetDataProperty"], jsii.get(self, "budget"))

    @budget.setter
    def budget(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBudget.BudgetDataProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__c95887cba36441131745a708716d40542977a1478eafb13e3649b0bddc03c19c)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "budget", value)

    @builtins.property
    @jsii.member(jsii_name="notificationsWithSubscribers")
    def notifications_with_subscribers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudget.NotificationWithSubscribersProperty"]]]]:
        '''A notification that you want to associate with a budget.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudget.NotificationWithSubscribersProperty"]]]], jsii.get(self, "notificationsWithSubscribers"))

    @notifications_with_subscribers.setter
    def notifications_with_subscribers(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudget.NotificationWithSubscribersProperty"]]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__338a591d66627dac6d0524a4af3df9ae2f64ac27737f12b95bc7243a4566a5e3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationsWithSubscribers", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.AutoAdjustDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "auto_adjust_type": "autoAdjustType",
            "historical_options": "historicalOptions",
        },
    )
    class AutoAdjustDataProperty:
        def __init__(
            self,
            *,
            auto_adjust_type: builtins.str,
            historical_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.HistoricalOptionsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Determine the budget amount for an auto-adjusting budget.

            :param auto_adjust_type: The string that defines whether your budget auto-adjusts based on historical or forecasted data.
            :param historical_options: The parameters that define or describe the historical data that your auto-adjusting budget is based on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                auto_adjust_data_property = budgets.CfnBudget.AutoAdjustDataProperty(
                    auto_adjust_type="autoAdjustType",
                
                    # the properties below are optional
                    historical_options=budgets.CfnBudget.HistoricalOptionsProperty(
                        budget_adjustment_period=123
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ed95504d1222347c1591bd33e0256ea9c7cfabe8856c857ffa5ee97b56e6455f)
                check_type(argname="argument auto_adjust_type", value=auto_adjust_type, expected_type=type_hints["auto_adjust_type"])
                check_type(argname="argument historical_options", value=historical_options, expected_type=type_hints["historical_options"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "auto_adjust_type": auto_adjust_type,
            }
            if historical_options is not None:
                self._values["historical_options"] = historical_options

        @builtins.property
        def auto_adjust_type(self) -> builtins.str:
            '''The string that defines whether your budget auto-adjusts based on historical or forecasted data.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html#cfn-budgets-budget-autoadjustdata-autoadjusttype
            '''
            result = self._values.get("auto_adjust_type")
            assert result is not None, "Required property 'auto_adjust_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def historical_options(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.HistoricalOptionsProperty"]]:
            '''The parameters that define or describe the historical data that your auto-adjusting budget is based on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-autoadjustdata.html#cfn-budgets-budget-autoadjustdata-historicaloptions
            '''
            result = self._values.get("historical_options")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.HistoricalOptionsProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "AutoAdjustDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.BudgetDataProperty",
        jsii_struct_bases=[],
        name_mapping={
            "budget_type": "budgetType",
            "time_unit": "timeUnit",
            "auto_adjust_data": "autoAdjustData",
            "budget_limit": "budgetLimit",
            "budget_name": "budgetName",
            "cost_filters": "costFilters",
            "cost_types": "costTypes",
            "planned_budget_limits": "plannedBudgetLimits",
            "time_period": "timePeriod",
        },
    )
    class BudgetDataProperty:
        def __init__(
            self,
            *,
            budget_type: builtins.str,
            time_unit: builtins.str,
            auto_adjust_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.AutoAdjustDataProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            budget_limit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.SpendProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            budget_name: typing.Optional[builtins.str] = None,
            cost_filters: typing.Any = None,
            cost_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.CostTypesProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            planned_budget_limits: typing.Any = None,
            time_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.TimePeriodProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Represents the output of the ``CreateBudget`` operation.

            The content consists of the detailed metadata and data file information, and the current status of the ``budget`` object.

            This is the Amazon Resource Name (ARN) pattern for a budget:

            ``arn:aws:budgets::AccountId:budget/budgetName``

            :param budget_type: Specifies whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.
            :param time_unit: The length of time until a budget resets the actual and forecasted spend. ``DAILY`` is available only for ``RI_UTILIZATION`` and ``RI_COVERAGE`` budgets.
            :param auto_adjust_data: Determine the budget amount for an auto-adjusting budget.
            :param budget_limit: The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget. ``BudgetLimit`` is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to ``100`` . This is the only valid value for RI or Savings Plans utilization or coverage budgets. You can't use ``BudgetLimit`` with ``PlannedBudgetLimits`` for ``CreateBudget`` and ``UpdateBudget`` actions.
            :param budget_name: The name of a budget. The value must be unique within an account. ``BudgetName`` can't include ``:`` and ``\\`` characters. If you don't include value for ``BudgetName`` in the template, Billing and Cost Management assigns your budget a randomly generated name.
            :param cost_filters: The cost filters, such as ``Region`` , ``Service`` , ``member account`` , ``Tag`` , or ``Cost Category`` , that are applied to a budget. AWS Budgets supports the following services as a ``Service`` filter for RI budgets: - Amazon EC2 - Amazon Redshift - Amazon Relational Database Service - Amazon ElastiCache - Amazon OpenSearch Service
            :param cost_types: The types of costs that are included in this ``COST`` budget. ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``SAVINGS_PLANS_UTILIZATION`` , and ``SAVINGS_PLANS_COVERAGE`` budgets do not have ``CostTypes`` .
            :param planned_budget_limits: A map containing multiple ``BudgetLimit`` , including current or future limits. ``PlannedBudgetLimits`` is available for cost or usage budget and supports both monthly and quarterly ``TimeUnit`` . For monthly budgets, provide 12 months of ``PlannedBudgetLimits`` values. This must start from the current month and include the next 11 months. The ``key`` is the start of the month, ``UTC`` in epoch seconds. For quarterly budgets, provide four quarters of ``PlannedBudgetLimits`` value entries in standard calendar quarter increments. This must start from the current quarter and include the next three quarters. The ``key`` is the start of the quarter, ``UTC`` in epoch seconds. If the planned budget expires before 12 months for monthly or four quarters for quarterly, provide the ``PlannedBudgetLimits`` values only for the remaining periods. If the budget begins at a date in the future, provide ``PlannedBudgetLimits`` values from the start date of the budget. After all of the ``BudgetLimit`` values in ``PlannedBudgetLimits`` are used, the budget continues to use the last limit as the ``BudgetLimit`` . At that point, the planned budget provides the same experience as a fixed budget. ``DescribeBudget`` and ``DescribeBudgets`` response along with ``PlannedBudgetLimits`` also contain ``BudgetLimit`` representing the current month or quarter limit present in ``PlannedBudgetLimits`` . This only applies to budgets that are created with ``PlannedBudgetLimits`` . Budgets that are created without ``PlannedBudgetLimits`` only contain ``BudgetLimit`` . They don't contain ``PlannedBudgetLimits`` .
            :param time_period: The period of time that is covered by a budget. The period has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date. The start date for a budget. If you created your budget and didn't specify a start date, the start date defaults to the start of the chosen time period (MONTHLY, QUARTERLY, or ANNUALLY). For example, if you create your budget on January 24, 2019, choose ``MONTHLY`` , and don't set a start date, the start date defaults to ``01/01/19 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API. You can change your start date with the ``UpdateBudget`` operation. After the end date, AWS deletes the budget and all associated notifications and subscribers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                # cost_filters: Any
                # planned_budget_limits: Any
                
                budget_data_property = budgets.CfnBudget.BudgetDataProperty(
                    budget_type="budgetType",
                    time_unit="timeUnit",
                
                    # the properties below are optional
                    auto_adjust_data=budgets.CfnBudget.AutoAdjustDataProperty(
                        auto_adjust_type="autoAdjustType",
                
                        # the properties below are optional
                        historical_options=budgets.CfnBudget.HistoricalOptionsProperty(
                            budget_adjustment_period=123
                        )
                    ),
                    budget_limit=budgets.CfnBudget.SpendProperty(
                        amount=123,
                        unit="unit"
                    ),
                    budget_name="budgetName",
                    cost_filters=cost_filters,
                    cost_types=budgets.CfnBudget.CostTypesProperty(
                        include_credit=False,
                        include_discount=False,
                        include_other_subscription=False,
                        include_recurring=False,
                        include_refund=False,
                        include_subscription=False,
                        include_support=False,
                        include_tax=False,
                        include_upfront=False,
                        use_amortized=False,
                        use_blended=False
                    ),
                    planned_budget_limits=planned_budget_limits,
                    time_period=budgets.CfnBudget.TimePeriodProperty(
                        end="end",
                        start="start"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b2c7f5c59209a2623bf116ca3a20b23835ececd0df52736e4f148622f483afb2)
                check_type(argname="argument budget_type", value=budget_type, expected_type=type_hints["budget_type"])
                check_type(argname="argument time_unit", value=time_unit, expected_type=type_hints["time_unit"])
                check_type(argname="argument auto_adjust_data", value=auto_adjust_data, expected_type=type_hints["auto_adjust_data"])
                check_type(argname="argument budget_limit", value=budget_limit, expected_type=type_hints["budget_limit"])
                check_type(argname="argument budget_name", value=budget_name, expected_type=type_hints["budget_name"])
                check_type(argname="argument cost_filters", value=cost_filters, expected_type=type_hints["cost_filters"])
                check_type(argname="argument cost_types", value=cost_types, expected_type=type_hints["cost_types"])
                check_type(argname="argument planned_budget_limits", value=planned_budget_limits, expected_type=type_hints["planned_budget_limits"])
                check_type(argname="argument time_period", value=time_period, expected_type=type_hints["time_period"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "budget_type": budget_type,
                "time_unit": time_unit,
            }
            if auto_adjust_data is not None:
                self._values["auto_adjust_data"] = auto_adjust_data
            if budget_limit is not None:
                self._values["budget_limit"] = budget_limit
            if budget_name is not None:
                self._values["budget_name"] = budget_name
            if cost_filters is not None:
                self._values["cost_filters"] = cost_filters
            if cost_types is not None:
                self._values["cost_types"] = cost_types
            if planned_budget_limits is not None:
                self._values["planned_budget_limits"] = planned_budget_limits
            if time_period is not None:
                self._values["time_period"] = time_period

        @builtins.property
        def budget_type(self) -> builtins.str:
            '''Specifies whether this budget tracks costs, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgettype
            '''
            result = self._values.get("budget_type")
            assert result is not None, "Required property 'budget_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_unit(self) -> builtins.str:
            '''The length of time until a budget resets the actual and forecasted spend.

            ``DAILY`` is available only for ``RI_UTILIZATION`` and ``RI_COVERAGE`` budgets.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeunit
            '''
            result = self._values.get("time_unit")
            assert result is not None, "Required property 'time_unit' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def auto_adjust_data(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.AutoAdjustDataProperty"]]:
            '''Determine the budget amount for an auto-adjusting budget.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-autoadjustdata
            '''
            result = self._values.get("auto_adjust_data")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.AutoAdjustDataProperty"]], result)

        @builtins.property
        def budget_limit(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.SpendProperty"]]:
            '''The total amount of cost, usage, RI utilization, RI coverage, Savings Plans utilization, or Savings Plans coverage that you want to track with your budget.

            ``BudgetLimit`` is required for cost or usage budgets, but optional for RI or Savings Plans utilization or coverage budgets. RI and Savings Plans utilization or coverage budgets default to ``100`` . This is the only valid value for RI or Savings Plans utilization or coverage budgets. You can't use ``BudgetLimit`` with ``PlannedBudgetLimits`` for ``CreateBudget`` and ``UpdateBudget`` actions.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetlimit
            '''
            result = self._values.get("budget_limit")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.SpendProperty"]], result)

        @builtins.property
        def budget_name(self) -> typing.Optional[builtins.str]:
            '''The name of a budget.

            The value must be unique within an account. ``BudgetName`` can't include ``:`` and ``\\`` characters. If you don't include value for ``BudgetName`` in the template, Billing and Cost Management assigns your budget a randomly generated name.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-budgetname
            '''
            result = self._values.get("budget_name")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def cost_filters(self) -> typing.Any:
            '''The cost filters, such as ``Region`` , ``Service`` , ``member account`` , ``Tag`` , or ``Cost Category`` , that are applied to a budget.

            AWS Budgets supports the following services as a ``Service`` filter for RI budgets:

            - Amazon EC2
            - Amazon Redshift
            - Amazon Relational Database Service
            - Amazon ElastiCache
            - Amazon OpenSearch Service

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costfilters
            '''
            result = self._values.get("cost_filters")
            return typing.cast(typing.Any, result)

        @builtins.property
        def cost_types(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.CostTypesProperty"]]:
            '''The types of costs that are included in this ``COST`` budget.

            ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``SAVINGS_PLANS_UTILIZATION`` , and ``SAVINGS_PLANS_COVERAGE`` budgets do not have ``CostTypes`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-costtypes
            '''
            result = self._values.get("cost_types")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.CostTypesProperty"]], result)

        @builtins.property
        def planned_budget_limits(self) -> typing.Any:
            '''A map containing multiple ``BudgetLimit`` , including current or future limits.

            ``PlannedBudgetLimits`` is available for cost or usage budget and supports both monthly and quarterly ``TimeUnit`` .

            For monthly budgets, provide 12 months of ``PlannedBudgetLimits`` values. This must start from the current month and include the next 11 months. The ``key`` is the start of the month, ``UTC`` in epoch seconds.

            For quarterly budgets, provide four quarters of ``PlannedBudgetLimits`` value entries in standard calendar quarter increments. This must start from the current quarter and include the next three quarters. The ``key`` is the start of the quarter, ``UTC`` in epoch seconds.

            If the planned budget expires before 12 months for monthly or four quarters for quarterly, provide the ``PlannedBudgetLimits`` values only for the remaining periods.

            If the budget begins at a date in the future, provide ``PlannedBudgetLimits`` values from the start date of the budget.

            After all of the ``BudgetLimit`` values in ``PlannedBudgetLimits`` are used, the budget continues to use the last limit as the ``BudgetLimit`` . At that point, the planned budget provides the same experience as a fixed budget.

            ``DescribeBudget`` and ``DescribeBudgets`` response along with ``PlannedBudgetLimits`` also contain ``BudgetLimit`` representing the current month or quarter limit present in ``PlannedBudgetLimits`` . This only applies to budgets that are created with ``PlannedBudgetLimits`` . Budgets that are created without ``PlannedBudgetLimits`` only contain ``BudgetLimit`` . They don't contain ``PlannedBudgetLimits`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-plannedbudgetlimits
            '''
            result = self._values.get("planned_budget_limits")
            return typing.cast(typing.Any, result)

        @builtins.property
        def time_period(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.TimePeriodProperty"]]:
            '''The period of time that is covered by a budget.

            The period has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date.

            The start date for a budget. If you created your budget and didn't specify a start date, the start date defaults to the start of the chosen time period (MONTHLY, QUARTERLY, or ANNUALLY). For example, if you create your budget on January 24, 2019, choose ``MONTHLY`` , and don't set a start date, the start date defaults to ``01/01/19 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API.

            You can change your start date with the ``UpdateBudget`` operation.

            After the end date, AWS deletes the budget and all associated notifications and subscribers.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-budgetdata.html#cfn-budgets-budget-budgetdata-timeperiod
            '''
            result = self._values.get("time_period")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudget.TimePeriodProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "BudgetDataProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.CostTypesProperty",
        jsii_struct_bases=[],
        name_mapping={
            "include_credit": "includeCredit",
            "include_discount": "includeDiscount",
            "include_other_subscription": "includeOtherSubscription",
            "include_recurring": "includeRecurring",
            "include_refund": "includeRefund",
            "include_subscription": "includeSubscription",
            "include_support": "includeSupport",
            "include_tax": "includeTax",
            "include_upfront": "includeUpfront",
            "use_amortized": "useAmortized",
            "use_blended": "useBlended",
        },
    )
    class CostTypesProperty:
        def __init__(
            self,
            *,
            include_credit: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_discount: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_other_subscription: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_recurring: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_refund: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_subscription: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_tax: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            include_upfront: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_amortized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
            use_blended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
        ) -> None:
            '''The types of cost that are included in a ``COST`` budget, such as tax and subscriptions.

            ``USAGE`` , ``RI_UTILIZATION`` , ``RI_COVERAGE`` , ``SAVINGS_PLANS_UTILIZATION`` , and ``SAVINGS_PLANS_COVERAGE`` budgets don't have ``CostTypes`` .

            :param include_credit: Specifies whether a budget includes credits. The default value is ``true`` .
            :param include_discount: Specifies whether a budget includes discounts. The default value is ``true`` .
            :param include_other_subscription: Specifies whether a budget includes non-RI subscription costs. The default value is ``true`` .
            :param include_recurring: Specifies whether a budget includes recurring fees such as monthly RI fees. The default value is ``true`` .
            :param include_refund: Specifies whether a budget includes refunds. The default value is ``true`` .
            :param include_subscription: Specifies whether a budget includes subscriptions. The default value is ``true`` .
            :param include_support: Specifies whether a budget includes support subscription fees. The default value is ``true`` .
            :param include_tax: Specifies whether a budget includes taxes. The default value is ``true`` .
            :param include_upfront: Specifies whether a budget includes upfront RI costs. The default value is ``true`` .
            :param use_amortized: Specifies whether a budget uses the amortized rate. The default value is ``false`` .
            :param use_blended: Specifies whether a budget uses a blended rate. The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                cost_types_property = budgets.CfnBudget.CostTypesProperty(
                    include_credit=False,
                    include_discount=False,
                    include_other_subscription=False,
                    include_recurring=False,
                    include_refund=False,
                    include_subscription=False,
                    include_support=False,
                    include_tax=False,
                    include_upfront=False,
                    use_amortized=False,
                    use_blended=False
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ca892e141a9adeb986265203927fc16b8a26091edacd45cbc9ebe6689e4857bb)
                check_type(argname="argument include_credit", value=include_credit, expected_type=type_hints["include_credit"])
                check_type(argname="argument include_discount", value=include_discount, expected_type=type_hints["include_discount"])
                check_type(argname="argument include_other_subscription", value=include_other_subscription, expected_type=type_hints["include_other_subscription"])
                check_type(argname="argument include_recurring", value=include_recurring, expected_type=type_hints["include_recurring"])
                check_type(argname="argument include_refund", value=include_refund, expected_type=type_hints["include_refund"])
                check_type(argname="argument include_subscription", value=include_subscription, expected_type=type_hints["include_subscription"])
                check_type(argname="argument include_support", value=include_support, expected_type=type_hints["include_support"])
                check_type(argname="argument include_tax", value=include_tax, expected_type=type_hints["include_tax"])
                check_type(argname="argument include_upfront", value=include_upfront, expected_type=type_hints["include_upfront"])
                check_type(argname="argument use_amortized", value=use_amortized, expected_type=type_hints["use_amortized"])
                check_type(argname="argument use_blended", value=use_blended, expected_type=type_hints["use_blended"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if include_credit is not None:
                self._values["include_credit"] = include_credit
            if include_discount is not None:
                self._values["include_discount"] = include_discount
            if include_other_subscription is not None:
                self._values["include_other_subscription"] = include_other_subscription
            if include_recurring is not None:
                self._values["include_recurring"] = include_recurring
            if include_refund is not None:
                self._values["include_refund"] = include_refund
            if include_subscription is not None:
                self._values["include_subscription"] = include_subscription
            if include_support is not None:
                self._values["include_support"] = include_support
            if include_tax is not None:
                self._values["include_tax"] = include_tax
            if include_upfront is not None:
                self._values["include_upfront"] = include_upfront
            if use_amortized is not None:
                self._values["use_amortized"] = use_amortized
            if use_blended is not None:
                self._values["use_blended"] = use_blended

        @builtins.property
        def include_credit(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes credits.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includecredit
            '''
            result = self._values.get("include_credit")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_discount(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes discounts.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includediscount
            '''
            result = self._values.get("include_discount")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_other_subscription(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes non-RI subscription costs.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeothersubscription
            '''
            result = self._values.get("include_other_subscription")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_recurring(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes recurring fees such as monthly RI fees.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerecurring
            '''
            result = self._values.get("include_recurring")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_refund(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes refunds.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includerefund
            '''
            result = self._values.get("include_refund")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_subscription(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes subscriptions.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesubscription
            '''
            result = self._values.get("include_subscription")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_support(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes support subscription fees.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includesupport
            '''
            result = self._values.get("include_support")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_tax(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes taxes.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includetax
            '''
            result = self._values.get("include_tax")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def include_upfront(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget includes upfront RI costs.

            The default value is ``true`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-includeupfront
            '''
            result = self._values.get("include_upfront")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_amortized(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget uses the amortized rate.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useamortized
            '''
            result = self._values.get("use_amortized")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        @builtins.property
        def use_blended(
            self,
        ) -> typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]]:
            '''Specifies whether a budget uses a blended rate.

            The default value is ``false`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-costtypes.html#cfn-budgets-budget-costtypes-useblended
            '''
            result = self._values.get("use_blended")
            return typing.cast(typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CostTypesProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.HistoricalOptionsProperty",
        jsii_struct_bases=[],
        name_mapping={"budget_adjustment_period": "budgetAdjustmentPeriod"},
    )
    class HistoricalOptionsProperty:
        def __init__(self, *, budget_adjustment_period: jsii.Number) -> None:
            '''The parameters that define or describe the historical data that your auto-adjusting budget is based on.

            :param budget_adjustment_period: The number of budget periods included in the moving-average calculation that determines your auto-adjusted budget amount. The maximum value depends on the ``TimeUnit`` granularity of the budget: - For the ``DAILY`` granularity, the maximum value is ``60`` . - For the ``MONTHLY`` granularity, the maximum value is ``12`` . - For the ``QUARTERLY`` granularity, the maximum value is ``4`` . - For the ``ANNUALLY`` granularity, the maximum value is ``1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-historicaloptions.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                historical_options_property = budgets.CfnBudget.HistoricalOptionsProperty(
                    budget_adjustment_period=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ba7bd7cc2be23305dffbf6031c061df699ccd87872fbd4ec418a99be7cf81185)
                check_type(argname="argument budget_adjustment_period", value=budget_adjustment_period, expected_type=type_hints["budget_adjustment_period"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "budget_adjustment_period": budget_adjustment_period,
            }

        @builtins.property
        def budget_adjustment_period(self) -> jsii.Number:
            '''The number of budget periods included in the moving-average calculation that determines your auto-adjusted budget amount.

            The maximum value depends on the ``TimeUnit`` granularity of the budget:

            - For the ``DAILY`` granularity, the maximum value is ``60`` .
            - For the ``MONTHLY`` granularity, the maximum value is ``12`` .
            - For the ``QUARTERLY`` granularity, the maximum value is ``4`` .
            - For the ``ANNUALLY`` granularity, the maximum value is ``1`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-historicaloptions.html#cfn-budgets-budget-historicaloptions-budgetadjustmentperiod
            '''
            result = self._values.get("budget_adjustment_period")
            assert result is not None, "Required property 'budget_adjustment_period' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "HistoricalOptionsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.NotificationProperty",
        jsii_struct_bases=[],
        name_mapping={
            "comparison_operator": "comparisonOperator",
            "notification_type": "notificationType",
            "threshold": "threshold",
            "threshold_type": "thresholdType",
        },
    )
    class NotificationProperty:
        def __init__(
            self,
            *,
            comparison_operator: builtins.str,
            notification_type: builtins.str,
            threshold: jsii.Number,
            threshold_type: typing.Optional[builtins.str] = None,
        ) -> None:
            '''A notification that's associated with a budget. A budget can have up to ten notifications.

            Each notification must have at least one subscriber. A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

            For example, if you have a budget for 200 dollars and you want to be notified when you go over 160 dollars, create a notification with the following parameters:

            - A notificationType of ``ACTUAL``
            - A ``thresholdType`` of ``PERCENTAGE``
            - A ``comparisonOperator`` of ``GREATER_THAN``
            - A notification ``threshold`` of ``80``

            :param comparison_operator: The comparison that's used for this notification.
            :param notification_type: Specifies whether the notification is for how much you have spent ( ``ACTUAL`` ) or for how much that you're forecasted to spend ( ``FORECASTED`` ).
            :param threshold: The threshold that's associated with a notification. Thresholds are always a percentage, and many customers find value being alerted between 50% - 200% of the budgeted amount. The maximum limit for your threshold is 1,000,000% above the budgeted amount.
            :param threshold_type: The type of threshold for a notification. For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE`` thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                notification_property = budgets.CfnBudget.NotificationProperty(
                    comparison_operator="comparisonOperator",
                    notification_type="notificationType",
                    threshold=123,
                
                    # the properties below are optional
                    threshold_type="thresholdType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__ea30c5d87897db387daaab29d498d54bb0b490643c5fbb8fb1a5b9a125603de5)
                check_type(argname="argument comparison_operator", value=comparison_operator, expected_type=type_hints["comparison_operator"])
                check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
                check_type(argname="argument threshold", value=threshold, expected_type=type_hints["threshold"])
                check_type(argname="argument threshold_type", value=threshold_type, expected_type=type_hints["threshold_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison_operator": comparison_operator,
                "notification_type": notification_type,
                "threshold": threshold,
            }
            if threshold_type is not None:
                self._values["threshold_type"] = threshold_type

        @builtins.property
        def comparison_operator(self) -> builtins.str:
            '''The comparison that's used for this notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-comparisonoperator
            '''
            result = self._values.get("comparison_operator")
            assert result is not None, "Required property 'comparison_operator' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def notification_type(self) -> builtins.str:
            '''Specifies whether the notification is for how much you have spent ( ``ACTUAL`` ) or for how much that you're forecasted to spend ( ``FORECASTED`` ).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-notificationtype
            '''
            result = self._values.get("notification_type")
            assert result is not None, "Required property 'notification_type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def threshold(self) -> jsii.Number:
            '''The threshold that's associated with a notification.

            Thresholds are always a percentage, and many customers find value being alerted between 50% - 200% of the budgeted amount. The maximum limit for your threshold is 1,000,000% above the budgeted amount.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-threshold
            '''
            result = self._values.get("threshold")
            assert result is not None, "Required property 'threshold' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def threshold_type(self) -> typing.Optional[builtins.str]:
            '''The type of threshold for a notification.

            For ``ABSOLUTE_VALUE`` thresholds, AWS notifies you when you go over or are forecasted to go over your total cost threshold. For ``PERCENTAGE`` thresholds, AWS notifies you when you go over or are forecasted to go over a certain percentage of your forecasted spend. For example, if you have a budget for 200 dollars and you have a ``PERCENTAGE`` threshold of 80%, AWS notifies you when you go over 160 dollars.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notification.html#cfn-budgets-budget-notification-thresholdtype
            '''
            result = self._values.get("threshold_type")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.NotificationWithSubscribersProperty",
        jsii_struct_bases=[],
        name_mapping={"notification": "notification", "subscribers": "subscribers"},
    )
    class NotificationWithSubscribersProperty:
        def __init__(
            self,
            *,
            notification: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.NotificationProperty", typing.Dict[builtins.str, typing.Any]]],
            subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudget.SubscriberProperty", typing.Dict[builtins.str, typing.Any]]]]],
        ) -> None:
            '''A notification with subscribers.

            A notification can have one SNS subscriber and up to 10 email subscribers, for a total of 11 subscribers.

            :param notification: The notification that's associated with a budget.
            :param subscribers: A list of subscribers who are subscribed to this notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                notification_with_subscribers_property = budgets.CfnBudget.NotificationWithSubscribersProperty(
                    notification=budgets.CfnBudget.NotificationProperty(
                        comparison_operator="comparisonOperator",
                        notification_type="notificationType",
                        threshold=123,
                
                        # the properties below are optional
                        threshold_type="thresholdType"
                    ),
                    subscribers=[budgets.CfnBudget.SubscriberProperty(
                        address="address",
                        subscription_type="subscriptionType"
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__07866499303a1a9ab70a645ecbda245fb51598e896b81d4f01f9cffeeac17bf1)
                check_type(argname="argument notification", value=notification, expected_type=type_hints["notification"])
                check_type(argname="argument subscribers", value=subscribers, expected_type=type_hints["subscribers"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "notification": notification,
                "subscribers": subscribers,
            }

        @builtins.property
        def notification(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnBudget.NotificationProperty"]:
            '''The notification that's associated with a budget.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-notification
            '''
            result = self._values.get("notification")
            assert result is not None, "Required property 'notification' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBudget.NotificationProperty"], result)

        @builtins.property
        def subscribers(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudget.SubscriberProperty"]]]:
            '''A list of subscribers who are subscribed to this notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-notificationwithsubscribers.html#cfn-budgets-budget-notificationwithsubscribers-subscribers
            '''
            result = self._values.get("subscribers")
            assert result is not None, "Required property 'subscribers' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudget.SubscriberProperty"]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NotificationWithSubscribersProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.SpendProperty",
        jsii_struct_bases=[],
        name_mapping={"amount": "amount", "unit": "unit"},
    )
    class SpendProperty:
        def __init__(self, *, amount: jsii.Number, unit: builtins.str) -> None:
            '''The amount of cost or usage that's measured for a budget.

            For example, a ``Spend`` for ``3 GB`` of S3 usage has the following parameters:

            - An ``Amount`` of ``3``
            - A ``unit`` of ``GB``

            :param amount: The cost or usage amount that's associated with a budget forecast, actual spend, or budget threshold.
            :param unit: The unit of measurement that's used for the budget forecast, actual spend, or budget threshold, such as USD or GBP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                spend_property = budgets.CfnBudget.SpendProperty(
                    amount=123,
                    unit="unit"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__5a81264d854f3d578cfafd932e1a5385f5f235b0b2fd9984ec61d7cd42705c9d)
                check_type(argname="argument amount", value=amount, expected_type=type_hints["amount"])
                check_type(argname="argument unit", value=unit, expected_type=type_hints["unit"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "amount": amount,
                "unit": unit,
            }

        @builtins.property
        def amount(self) -> jsii.Number:
            '''The cost or usage amount that's associated with a budget forecast, actual spend, or budget threshold.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-amount
            '''
            result = self._values.get("amount")
            assert result is not None, "Required property 'amount' is missing"
            return typing.cast(jsii.Number, result)

        @builtins.property
        def unit(self) -> builtins.str:
            '''The unit of measurement that's used for the budget forecast, actual spend, or budget threshold, such as USD or GBP.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-spend.html#cfn-budgets-budget-spend-unit
            '''
            result = self._values.get("unit")
            assert result is not None, "Required property 'unit' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SpendProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.SubscriberProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "subscription_type": "subscriptionType"},
    )
    class SubscriberProperty:
        def __init__(
            self,
            *,
            address: builtins.str,
            subscription_type: builtins.str,
        ) -> None:
            '''The ``Subscriber`` property type specifies who to notify for a Billing and Cost Management budget notification.

            The subscriber consists of a subscription type, and either an Amazon SNS topic or an email address.

            For example, an email subscriber would have the following parameters:

            - A ``subscriptionType`` of ``EMAIL``
            - An ``address`` of ``example@example.com``

            :param address: The address that AWS sends budget notifications to, either an SNS topic or an email. When you create a subscriber, the value of ``Address`` can't contain line breaks.
            :param subscription_type: The type of notification that AWS sends to a subscriber.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                subscriber_property = budgets.CfnBudget.SubscriberProperty(
                    address="address",
                    subscription_type="subscriptionType"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__e5d0b208f458ade09c3843fe83aba0d6db3ddb09a594e82cdd14537ffc0e26f0)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument subscription_type", value=subscription_type, expected_type=type_hints["subscription_type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address": address,
                "subscription_type": subscription_type,
            }

        @builtins.property
        def address(self) -> builtins.str:
            '''The address that AWS sends budget notifications to, either an SNS topic or an email.

            When you create a subscriber, the value of ``Address`` can't contain line breaks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-address
            '''
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subscription_type(self) -> builtins.str:
            '''The type of notification that AWS sends to a subscriber.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-subscriber.html#cfn-budgets-budget-subscriber-subscriptiontype
            '''
            result = self._values.get("subscription_type")
            assert result is not None, "Required property 'subscription_type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudget.TimePeriodProperty",
        jsii_struct_bases=[],
        name_mapping={"end": "end", "start": "start"},
    )
    class TimePeriodProperty:
        def __init__(
            self,
            *,
            end: typing.Optional[builtins.str] = None,
            start: typing.Optional[builtins.str] = None,
        ) -> None:
            '''The period of time that is covered by a budget.

            The period has a start date and an end date. The start date must come before the end date. There are no restrictions on the end date.

            :param end: The end date for a budget. If you didn't specify an end date, AWS set your end date to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API. After the end date, AWS deletes the budget and all the associated notifications and subscribers. You can change your end date with the ``UpdateBudget`` operation.
            :param start: The start date for a budget. If you created your budget and didn't specify a start date, the start date defaults to the start of the chosen time period (MONTHLY, QUARTERLY, or ANNUALLY). For example, if you create your budget on January 24, 2019, choose ``MONTHLY`` , and don't set a start date, the start date defaults to ``01/01/19 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API. You can change your start date with the ``UpdateBudget`` operation. Valid values depend on the value of ``BudgetType`` : - If ``BudgetType`` is ``COST`` or ``USAGE`` : Valid values are ``MONTHLY`` , ``QUARTERLY`` , and ``ANNUALLY`` . - If ``BudgetType`` is ``RI_UTILIZATION`` or ``RI_COVERAGE`` : Valid values are ``DAILY`` , ``MONTHLY`` , ``QUARTERLY`` , and ``ANNUALLY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                time_period_property = budgets.CfnBudget.TimePeriodProperty(
                    end="end",
                    start="start"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__77f51cb94a1e5a0ae65deee87b45596400f57823b1add7660a12635b0a091886)
                check_type(argname="argument end", value=end, expected_type=type_hints["end"])
                check_type(argname="argument start", value=start, expected_type=type_hints["start"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end is not None:
                self._values["end"] = end
            if start is not None:
                self._values["start"] = start

        @builtins.property
        def end(self) -> typing.Optional[builtins.str]:
            '''The end date for a budget.

            If you didn't specify an end date, AWS set your end date to ``06/15/87 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API.

            After the end date, AWS deletes the budget and all the associated notifications and subscribers. You can change your end date with the ``UpdateBudget`` operation.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-end
            '''
            result = self._values.get("end")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def start(self) -> typing.Optional[builtins.str]:
            '''The start date for a budget.

            If you created your budget and didn't specify a start date, the start date defaults to the start of the chosen time period (MONTHLY, QUARTERLY, or ANNUALLY). For example, if you create your budget on January 24, 2019, choose ``MONTHLY`` , and don't set a start date, the start date defaults to ``01/01/19 00:00 UTC`` . The defaults are the same for the AWS Billing and Cost Management console and the API.

            You can change your start date with the ``UpdateBudget`` operation.

            Valid values depend on the value of ``BudgetType`` :

            - If ``BudgetType`` is ``COST`` or ``USAGE`` : Valid values are ``MONTHLY`` , ``QUARTERLY`` , and ``ANNUALLY`` .
            - If ``BudgetType`` is ``RI_UTILIZATION`` or ``RI_COVERAGE`` : Valid values are ``DAILY`` , ``MONTHLY`` , ``QUARTERLY`` , and ``ANNUALLY`` .

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budget-timeperiod.html#cfn-budgets-budget-timeperiod-start
            '''
            result = self._values.get("start")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimePeriodProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetProps",
    jsii_struct_bases=[],
    name_mapping={
        "budget": "budget",
        "notifications_with_subscribers": "notificationsWithSubscribers",
    },
)
class CfnBudgetProps:
    def __init__(
        self,
        *,
        budget: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.BudgetDataProperty, typing.Dict[builtins.str, typing.Any]]],
        notifications_with_subscribers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.NotificationWithSubscribersProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnBudget``.

        :param budget: The budget object that you want to create.
        :param notifications_with_subscribers: A notification that you want to associate with a budget. A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your ``CreateBudget`` call, AWS creates the notifications and subscribers for you.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_budgets as budgets
            
            # cost_filters: Any
            # planned_budget_limits: Any
            
            cfn_budget_props = budgets.CfnBudgetProps(
                budget=budgets.CfnBudget.BudgetDataProperty(
                    budget_type="budgetType",
                    time_unit="timeUnit",
            
                    # the properties below are optional
                    auto_adjust_data=budgets.CfnBudget.AutoAdjustDataProperty(
                        auto_adjust_type="autoAdjustType",
            
                        # the properties below are optional
                        historical_options=budgets.CfnBudget.HistoricalOptionsProperty(
                            budget_adjustment_period=123
                        )
                    ),
                    budget_limit=budgets.CfnBudget.SpendProperty(
                        amount=123,
                        unit="unit"
                    ),
                    budget_name="budgetName",
                    cost_filters=cost_filters,
                    cost_types=budgets.CfnBudget.CostTypesProperty(
                        include_credit=False,
                        include_discount=False,
                        include_other_subscription=False,
                        include_recurring=False,
                        include_refund=False,
                        include_subscription=False,
                        include_support=False,
                        include_tax=False,
                        include_upfront=False,
                        use_amortized=False,
                        use_blended=False
                    ),
                    planned_budget_limits=planned_budget_limits,
                    time_period=budgets.CfnBudget.TimePeriodProperty(
                        end="end",
                        start="start"
                    )
                ),
            
                # the properties below are optional
                notifications_with_subscribers=[budgets.CfnBudget.NotificationWithSubscribersProperty(
                    notification=budgets.CfnBudget.NotificationProperty(
                        comparison_operator="comparisonOperator",
                        notification_type="notificationType",
                        threshold=123,
            
                        # the properties below are optional
                        threshold_type="thresholdType"
                    ),
                    subscribers=[budgets.CfnBudget.SubscriberProperty(
                        address="address",
                        subscription_type="subscriptionType"
                    )]
                )]
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__0bce15b7b8b999a87f796c503372a075fb7e77b171e9e458dd4b05e88e303d02)
            check_type(argname="argument budget", value=budget, expected_type=type_hints["budget"])
            check_type(argname="argument notifications_with_subscribers", value=notifications_with_subscribers, expected_type=type_hints["notifications_with_subscribers"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "budget": budget,
        }
        if notifications_with_subscribers is not None:
            self._values["notifications_with_subscribers"] = notifications_with_subscribers

    @builtins.property
    def budget(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBudget.BudgetDataProperty]:
        '''The budget object that you want to create.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-budget
        '''
        result = self._values.get("budget")
        assert result is not None, "Required property 'budget' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBudget.BudgetDataProperty], result)

    @builtins.property
    def notifications_with_subscribers(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBudget.NotificationWithSubscribersProperty]]]]:
        '''A notification that you want to associate with a budget.

        A budget can have up to five notifications, and each notification can have one SNS subscriber and up to 10 email subscribers. If you include notifications and subscribers in your ``CreateBudget`` call, AWS creates the notifications and subscribers for you.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budget.html#cfn-budgets-budget-notificationswithsubscribers
        '''
        result = self._values.get("notifications_with_subscribers")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBudget.NotificationWithSubscribersProperty]]]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBudgetProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnBudgetsAction(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction",
):
    '''The ``AWS::Budgets::BudgetsAction`` resource enables you to take predefined actions that are initiated when a budget threshold has been exceeded.

    For more information, see `Managing Your Costs with Budgets <https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-managing-costs.html>`_ in the *AWS Billing and Cost Management User Guide* .

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_budgets as budgets
        
        cfn_budgets_action = budgets.CfnBudgetsAction(self, "MyCfnBudgetsAction",
            action_threshold=budgets.CfnBudgetsAction.ActionThresholdProperty(
                type="type",
                value=123
            ),
            action_type="actionType",
            budget_name="budgetName",
            definition=budgets.CfnBudgetsAction.DefinitionProperty(
                iam_action_definition=budgets.CfnBudgetsAction.IamActionDefinitionProperty(
                    policy_arn="policyArn",
        
                    # the properties below are optional
                    groups=["groups"],
                    roles=["roles"],
                    users=["users"]
                ),
                scp_action_definition=budgets.CfnBudgetsAction.ScpActionDefinitionProperty(
                    policy_id="policyId",
                    target_ids=["targetIds"]
                ),
                ssm_action_definition=budgets.CfnBudgetsAction.SsmActionDefinitionProperty(
                    instance_ids=["instanceIds"],
                    region="region",
                    subtype="subtype"
                )
            ),
            execution_role_arn="executionRoleArn",
            notification_type="notificationType",
            subscribers=[budgets.CfnBudgetsAction.SubscriberProperty(
                address="address",
                type="type"
            )],
        
            # the properties below are optional
            approval_model="approvalModel"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        action_threshold: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudgetsAction.ActionThresholdProperty", typing.Dict[builtins.str, typing.Any]]],
        action_type: builtins.str,
        budget_name: builtins.str,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudgetsAction.DefinitionProperty", typing.Dict[builtins.str, typing.Any]]],
        execution_role_arn: builtins.str,
        notification_type: builtins.str,
        subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudgetsAction.SubscriberProperty", typing.Dict[builtins.str, typing.Any]]]]],
        approval_model: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param action_threshold: The trigger threshold of the action.
        :param action_type: The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.
        :param budget_name: A string that represents the budget name. ":" and "" characters aren't allowed.
        :param definition: Specifies all of the type-specific parameters.
        :param execution_role_arn: The role passed for action execution and reversion. Roles and actions must be in the same account.
        :param notification_type: The type of a notification.
        :param subscribers: A list of subscribers.
        :param approval_model: This specifies if the action needs manual or automatic approval.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5feaf1ccce7286d2cae539317638953135d21b7e897f0ded2f3a275d0516a886)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnBudgetsActionProps(
            action_threshold=action_threshold,
            action_type=action_type,
            budget_name=budget_name,
            definition=definition,
            execution_role_arn=execution_role_arn,
            notification_type=notification_type,
            subscribers=subscribers,
            approval_model=approval_model,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5e4d5fcd5b6fa47f421ce5a934095661754d1490e6d5622d679c21d056e2339d)
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
            type_hints = typing.get_type_hints(_typecheckingstub__37f0f35c0901b3170a2a787f6b136e6de796aa9287397d112b1716e76cfdf2fa)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrActionId")
    def attr_action_id(self) -> builtins.str:
        '''A system-generated universally unique identifier (UUID) for the action.

        :cloudformationAttribute: ActionId
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrActionId"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="actionThreshold")
    def action_threshold(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.ActionThresholdProperty"]:
        '''The trigger threshold of the action.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.ActionThresholdProperty"], jsii.get(self, "actionThreshold"))

    @action_threshold.setter
    def action_threshold(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.ActionThresholdProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__6444694cd4e1cfe409941297d12b4f71c45625cb1357bf1a3b12f86d4a288f85)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionThreshold", value)

    @builtins.property
    @jsii.member(jsii_name="actionType")
    def action_type(self) -> builtins.str:
        '''The type of action.'''
        return typing.cast(builtins.str, jsii.get(self, "actionType"))

    @action_type.setter
    def action_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__93ee3f487b114766988c6712b16108f0a81084444e5dcb38f58aa6ca5c1ac0eb)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "actionType", value)

    @builtins.property
    @jsii.member(jsii_name="budgetName")
    def budget_name(self) -> builtins.str:
        '''A string that represents the budget name.'''
        return typing.cast(builtins.str, jsii.get(self, "budgetName"))

    @budget_name.setter
    def budget_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__886294fdca463440eacd919c52ef223cd761321b3e92068ed0e10930b6c45bd8)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "budgetName", value)

    @builtins.property
    @jsii.member(jsii_name="definition")
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.DefinitionProperty"]:
        '''Specifies all of the type-specific parameters.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.DefinitionProperty"], jsii.get(self, "definition"))

    @definition.setter
    def definition(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.DefinitionProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__af7c0aaf6be25381fc5e59a606f980f8beb020b05d0d1b4e00097df9b213d1f4)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "definition", value)

    @builtins.property
    @jsii.member(jsii_name="executionRoleArn")
    def execution_role_arn(self) -> builtins.str:
        '''The role passed for action execution and reversion.'''
        return typing.cast(builtins.str, jsii.get(self, "executionRoleArn"))

    @execution_role_arn.setter
    def execution_role_arn(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__20f3acfbe196dceebb62052bc3a9709ca03c3cd1385bd0b8f47b14ebe24baea6)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "executionRoleArn", value)

    @builtins.property
    @jsii.member(jsii_name="notificationType")
    def notification_type(self) -> builtins.str:
        '''The type of a notification.'''
        return typing.cast(builtins.str, jsii.get(self, "notificationType"))

    @notification_type.setter
    def notification_type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53476f930c7990ef6a398f9ead465189ebfbebc41a5d5d7cb519d5ad1e21440e)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "notificationType", value)

    @builtins.property
    @jsii.member(jsii_name="subscribers")
    def subscribers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.SubscriberProperty"]]]:
        '''A list of subscribers.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.SubscriberProperty"]]], jsii.get(self, "subscribers"))

    @subscribers.setter
    def subscribers(
        self,
        value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.SubscriberProperty"]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__d139b5f0aab0780aebc710ff294cf4038924446db4e70d8dd7ceaf018b79e653)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "subscribers", value)

    @builtins.property
    @jsii.member(jsii_name="approvalModel")
    def approval_model(self) -> typing.Optional[builtins.str]:
        '''This specifies if the action needs manual or automatic approval.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "approvalModel"))

    @approval_model.setter
    def approval_model(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__cc9b0ed2b1fd2266f52e8858e29800b46ee5d46db67048e5fcafb370fe1d7fc3)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "approvalModel", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction.ActionThresholdProperty",
        jsii_struct_bases=[],
        name_mapping={"type": "type", "value": "value"},
    )
    class ActionThresholdProperty:
        def __init__(self, *, type: builtins.str, value: jsii.Number) -> None:
            '''The trigger threshold of the action.

            :param type: The type of threshold for a notification.
            :param value: The threshold of a notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                action_threshold_property = budgets.CfnBudgetsAction.ActionThresholdProperty(
                    type="type",
                    value=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__652e2954f340271681973613d60d4049ebd81a75c8987611d889045de156b8b3)
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "type": type,
                "value": value,
            }

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of threshold for a notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> jsii.Number:
            '''The threshold of a notification.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-actionthreshold.html#cfn-budgets-budgetsaction-actionthreshold-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(jsii.Number, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ActionThresholdProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction.DefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "iam_action_definition": "iamActionDefinition",
            "scp_action_definition": "scpActionDefinition",
            "ssm_action_definition": "ssmActionDefinition",
        },
    )
    class DefinitionProperty:
        def __init__(
            self,
            *,
            iam_action_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudgetsAction.IamActionDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            scp_action_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudgetsAction.ScpActionDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            ssm_action_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnBudgetsAction.SsmActionDefinitionProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The definition is where you specify all of the type-specific parameters.

            :param iam_action_definition: The AWS Identity and Access Management ( IAM ) action definition details.
            :param scp_action_definition: The service control policies (SCP) action definition details.
            :param ssm_action_definition: The Amazon EC2 Systems Manager ( SSM ) action definition details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                definition_property = budgets.CfnBudgetsAction.DefinitionProperty(
                    iam_action_definition=budgets.CfnBudgetsAction.IamActionDefinitionProperty(
                        policy_arn="policyArn",
                
                        # the properties below are optional
                        groups=["groups"],
                        roles=["roles"],
                        users=["users"]
                    ),
                    scp_action_definition=budgets.CfnBudgetsAction.ScpActionDefinitionProperty(
                        policy_id="policyId",
                        target_ids=["targetIds"]
                    ),
                    ssm_action_definition=budgets.CfnBudgetsAction.SsmActionDefinitionProperty(
                        instance_ids=["instanceIds"],
                        region="region",
                        subtype="subtype"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__96306621a1aae8f106a12b9134576206e8e4754361a681338ac6381f2e0940b2)
                check_type(argname="argument iam_action_definition", value=iam_action_definition, expected_type=type_hints["iam_action_definition"])
                check_type(argname="argument scp_action_definition", value=scp_action_definition, expected_type=type_hints["scp_action_definition"])
                check_type(argname="argument ssm_action_definition", value=ssm_action_definition, expected_type=type_hints["ssm_action_definition"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if iam_action_definition is not None:
                self._values["iam_action_definition"] = iam_action_definition
            if scp_action_definition is not None:
                self._values["scp_action_definition"] = scp_action_definition
            if ssm_action_definition is not None:
                self._values["ssm_action_definition"] = ssm_action_definition

        @builtins.property
        def iam_action_definition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.IamActionDefinitionProperty"]]:
            '''The AWS Identity and Access Management ( IAM ) action definition details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-iamactiondefinition
            '''
            result = self._values.get("iam_action_definition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.IamActionDefinitionProperty"]], result)

        @builtins.property
        def scp_action_definition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.ScpActionDefinitionProperty"]]:
            '''The service control policies (SCP) action definition details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-scpactiondefinition
            '''
            result = self._values.get("scp_action_definition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.ScpActionDefinitionProperty"]], result)

        @builtins.property
        def ssm_action_definition(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.SsmActionDefinitionProperty"]]:
            '''The Amazon EC2 Systems Manager ( SSM ) action definition details.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-definition.html#cfn-budgets-budgetsaction-definition-ssmactiondefinition
            '''
            result = self._values.get("ssm_action_definition")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnBudgetsAction.SsmActionDefinitionProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction.IamActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "policy_arn": "policyArn",
            "groups": "groups",
            "roles": "roles",
            "users": "users",
        },
    )
    class IamActionDefinitionProperty:
        def __init__(
            self,
            *,
            policy_arn: builtins.str,
            groups: typing.Optional[typing.Sequence[builtins.str]] = None,
            roles: typing.Optional[typing.Sequence[builtins.str]] = None,
            users: typing.Optional[typing.Sequence[builtins.str]] = None,
        ) -> None:
            '''The AWS Identity and Access Management ( IAM ) action definition details.

            :param policy_arn: The Amazon Resource Name (ARN) of the policy to be attached.
            :param groups: A list of groups to be attached. There must be at least one group.
            :param roles: A list of roles to be attached. There must be at least one role.
            :param users: A list of users to be attached. There must be at least one user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                iam_action_definition_property = budgets.CfnBudgetsAction.IamActionDefinitionProperty(
                    policy_arn="policyArn",
                
                    # the properties below are optional
                    groups=["groups"],
                    roles=["roles"],
                    users=["users"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__22f7bad74675d504f2471ac5656611eebbc86ce649e820a38f5961c5ae990704)
                check_type(argname="argument policy_arn", value=policy_arn, expected_type=type_hints["policy_arn"])
                check_type(argname="argument groups", value=groups, expected_type=type_hints["groups"])
                check_type(argname="argument roles", value=roles, expected_type=type_hints["roles"])
                check_type(argname="argument users", value=users, expected_type=type_hints["users"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_arn": policy_arn,
            }
            if groups is not None:
                self._values["groups"] = groups
            if roles is not None:
                self._values["roles"] = roles
            if users is not None:
                self._values["users"] = users

        @builtins.property
        def policy_arn(self) -> builtins.str:
            '''The Amazon Resource Name (ARN) of the policy to be attached.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-policyarn
            '''
            result = self._values.get("policy_arn")
            assert result is not None, "Required property 'policy_arn' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def groups(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of groups to be attached.

            There must be at least one group.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-groups
            '''
            result = self._values.get("groups")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def roles(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of roles to be attached.

            There must be at least one role.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-roles
            '''
            result = self._values.get("roles")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        @builtins.property
        def users(self) -> typing.Optional[typing.List[builtins.str]]:
            '''A list of users to be attached.

            There must be at least one user.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-iamactiondefinition.html#cfn-budgets-budgetsaction-iamactiondefinition-users
            '''
            result = self._values.get("users")
            return typing.cast(typing.Optional[typing.List[builtins.str]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "IamActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction.ScpActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={"policy_id": "policyId", "target_ids": "targetIds"},
    )
    class ScpActionDefinitionProperty:
        def __init__(
            self,
            *,
            policy_id: builtins.str,
            target_ids: typing.Sequence[builtins.str],
        ) -> None:
            '''The service control policies (SCP) action definition details.

            :param policy_id: The policy ID attached.
            :param target_ids: A list of target IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                scp_action_definition_property = budgets.CfnBudgetsAction.ScpActionDefinitionProperty(
                    policy_id="policyId",
                    target_ids=["targetIds"]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__31fd74b3c2a89d6419f8ea513fe7d522d39278beb5f299a80f1ee727475e6777)
                check_type(argname="argument policy_id", value=policy_id, expected_type=type_hints["policy_id"])
                check_type(argname="argument target_ids", value=target_ids, expected_type=type_hints["target_ids"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "policy_id": policy_id,
                "target_ids": target_ids,
            }

        @builtins.property
        def policy_id(self) -> builtins.str:
            '''The policy ID attached.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-policyid
            '''
            result = self._values.get("policy_id")
            assert result is not None, "Required property 'policy_id' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def target_ids(self) -> typing.List[builtins.str]:
            '''A list of target IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-scpactiondefinition.html#cfn-budgets-budgetsaction-scpactiondefinition-targetids
            '''
            result = self._values.get("target_ids")
            assert result is not None, "Required property 'target_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScpActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction.SsmActionDefinitionProperty",
        jsii_struct_bases=[],
        name_mapping={
            "instance_ids": "instanceIds",
            "region": "region",
            "subtype": "subtype",
        },
    )
    class SsmActionDefinitionProperty:
        def __init__(
            self,
            *,
            instance_ids: typing.Sequence[builtins.str],
            region: builtins.str,
            subtype: builtins.str,
        ) -> None:
            '''The Amazon EC2 Systems Manager ( SSM ) action definition details.

            :param instance_ids: The EC2 and RDS instance IDs.
            :param region: The Region to run the ( SSM ) document.
            :param subtype: The action subType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                ssm_action_definition_property = budgets.CfnBudgetsAction.SsmActionDefinitionProperty(
                    instance_ids=["instanceIds"],
                    region="region",
                    subtype="subtype"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__4e936943168730bfe281e6f6adccb2fafe8a803ed858a444a60decfc26cc38f7)
                check_type(argname="argument instance_ids", value=instance_ids, expected_type=type_hints["instance_ids"])
                check_type(argname="argument region", value=region, expected_type=type_hints["region"])
                check_type(argname="argument subtype", value=subtype, expected_type=type_hints["subtype"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "instance_ids": instance_ids,
                "region": region,
                "subtype": subtype,
            }

        @builtins.property
        def instance_ids(self) -> typing.List[builtins.str]:
            '''The EC2 and RDS instance IDs.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-instanceids
            '''
            result = self._values.get("instance_ids")
            assert result is not None, "Required property 'instance_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def region(self) -> builtins.str:
            '''The Region to run the ( SSM ) document.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-region
            '''
            result = self._values.get("region")
            assert result is not None, "Required property 'region' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def subtype(self) -> builtins.str:
            '''The action subType.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-ssmactiondefinition.html#cfn-budgets-budgetsaction-ssmactiondefinition-subtype
            '''
            result = self._values.get("subtype")
            assert result is not None, "Required property 'subtype' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SsmActionDefinitionProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsAction.SubscriberProperty",
        jsii_struct_bases=[],
        name_mapping={"address": "address", "type": "type"},
    )
    class SubscriberProperty:
        def __init__(self, *, address: builtins.str, type: builtins.str) -> None:
            '''The subscriber to a budget notification.

            The subscriber consists of a subscription type and either an Amazon SNS topic or an email address.

            For example, an email subscriber has the following parameters:

            - A ``subscriptionType`` of ``EMAIL``
            - An ``address`` of ``example@example.com``

            :param address: The address that AWS sends budget notifications to, either an SNS topic or an email. When you create a subscriber, the value of ``Address`` can't contain line breaks.
            :param type: The type of notification that AWS sends to a subscriber.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_budgets as budgets
                
                subscriber_property = budgets.CfnBudgetsAction.SubscriberProperty(
                    address="address",
                    type="type"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__53b54f7e3522aacd600ff090e6221f615565664782c185bdcb801f95f68daf7f)
                check_type(argname="argument address", value=address, expected_type=type_hints["address"])
                check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "address": address,
                "type": type,
            }

        @builtins.property
        def address(self) -> builtins.str:
            '''The address that AWS sends budget notifications to, either an SNS topic or an email.

            When you create a subscriber, the value of ``Address`` can't contain line breaks.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-address
            '''
            result = self._values.get("address")
            assert result is not None, "Required property 'address' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def type(self) -> builtins.str:
            '''The type of notification that AWS sends to a subscriber.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-budgets-budgetsaction-subscriber.html#cfn-budgets-budgetsaction-subscriber-type
            '''
            result = self._values.get("type")
            assert result is not None, "Required property 'type' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "SubscriberProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_budgets.CfnBudgetsActionProps",
    jsii_struct_bases=[],
    name_mapping={
        "action_threshold": "actionThreshold",
        "action_type": "actionType",
        "budget_name": "budgetName",
        "definition": "definition",
        "execution_role_arn": "executionRoleArn",
        "notification_type": "notificationType",
        "subscribers": "subscribers",
        "approval_model": "approvalModel",
    },
)
class CfnBudgetsActionProps:
    def __init__(
        self,
        *,
        action_threshold: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.ActionThresholdProperty, typing.Dict[builtins.str, typing.Any]]],
        action_type: builtins.str,
        budget_name: builtins.str,
        definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.DefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
        execution_role_arn: builtins.str,
        notification_type: builtins.str,
        subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
        approval_model: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnBudgetsAction``.

        :param action_threshold: The trigger threshold of the action.
        :param action_type: The type of action. This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.
        :param budget_name: A string that represents the budget name. ":" and "" characters aren't allowed.
        :param definition: Specifies all of the type-specific parameters.
        :param execution_role_arn: The role passed for action execution and reversion. Roles and actions must be in the same account.
        :param notification_type: The type of a notification.
        :param subscribers: A list of subscribers.
        :param approval_model: This specifies if the action needs manual or automatic approval.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_budgets as budgets
            
            cfn_budgets_action_props = budgets.CfnBudgetsActionProps(
                action_threshold=budgets.CfnBudgetsAction.ActionThresholdProperty(
                    type="type",
                    value=123
                ),
                action_type="actionType",
                budget_name="budgetName",
                definition=budgets.CfnBudgetsAction.DefinitionProperty(
                    iam_action_definition=budgets.CfnBudgetsAction.IamActionDefinitionProperty(
                        policy_arn="policyArn",
            
                        # the properties below are optional
                        groups=["groups"],
                        roles=["roles"],
                        users=["users"]
                    ),
                    scp_action_definition=budgets.CfnBudgetsAction.ScpActionDefinitionProperty(
                        policy_id="policyId",
                        target_ids=["targetIds"]
                    ),
                    ssm_action_definition=budgets.CfnBudgetsAction.SsmActionDefinitionProperty(
                        instance_ids=["instanceIds"],
                        region="region",
                        subtype="subtype"
                    )
                ),
                execution_role_arn="executionRoleArn",
                notification_type="notificationType",
                subscribers=[budgets.CfnBudgetsAction.SubscriberProperty(
                    address="address",
                    type="type"
                )],
            
                # the properties below are optional
                approval_model="approvalModel"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__2bf8a3fb960018ac6b97a0b01c3bd29dd4bf1acba7443236249ad39f7ced10a5)
            check_type(argname="argument action_threshold", value=action_threshold, expected_type=type_hints["action_threshold"])
            check_type(argname="argument action_type", value=action_type, expected_type=type_hints["action_type"])
            check_type(argname="argument budget_name", value=budget_name, expected_type=type_hints["budget_name"])
            check_type(argname="argument definition", value=definition, expected_type=type_hints["definition"])
            check_type(argname="argument execution_role_arn", value=execution_role_arn, expected_type=type_hints["execution_role_arn"])
            check_type(argname="argument notification_type", value=notification_type, expected_type=type_hints["notification_type"])
            check_type(argname="argument subscribers", value=subscribers, expected_type=type_hints["subscribers"])
            check_type(argname="argument approval_model", value=approval_model, expected_type=type_hints["approval_model"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "action_threshold": action_threshold,
            "action_type": action_type,
            "budget_name": budget_name,
            "definition": definition,
            "execution_role_arn": execution_role_arn,
            "notification_type": notification_type,
            "subscribers": subscribers,
        }
        if approval_model is not None:
            self._values["approval_model"] = approval_model

    @builtins.property
    def action_threshold(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.ActionThresholdProperty]:
        '''The trigger threshold of the action.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actionthreshold
        '''
        result = self._values.get("action_threshold")
        assert result is not None, "Required property 'action_threshold' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.ActionThresholdProperty], result)

    @builtins.property
    def action_type(self) -> builtins.str:
        '''The type of action.

        This defines the type of tasks that can be carried out by this action. This field also determines the format for definition.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-actiontype
        '''
        result = self._values.get("action_type")
        assert result is not None, "Required property 'action_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def budget_name(self) -> builtins.str:
        '''A string that represents the budget name.

        ":" and "" characters aren't allowed.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-budgetname
        '''
        result = self._values.get("budget_name")
        assert result is not None, "Required property 'budget_name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def definition(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.DefinitionProperty]:
        '''Specifies all of the type-specific parameters.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-definition
        '''
        result = self._values.get("definition")
        assert result is not None, "Required property 'definition' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.DefinitionProperty], result)

    @builtins.property
    def execution_role_arn(self) -> builtins.str:
        '''The role passed for action execution and reversion.

        Roles and actions must be in the same account.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-executionrolearn
        '''
        result = self._values.get("execution_role_arn")
        assert result is not None, "Required property 'execution_role_arn' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def notification_type(self) -> builtins.str:
        '''The type of a notification.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-notificationtype
        '''
        result = self._values.get("notification_type")
        assert result is not None, "Required property 'notification_type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def subscribers(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.SubscriberProperty]]]:
        '''A list of subscribers.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-subscribers
        '''
        result = self._values.get("subscribers")
        assert result is not None, "Required property 'subscribers' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.SubscriberProperty]]], result)

    @builtins.property
    def approval_model(self) -> typing.Optional[builtins.str]:
        '''This specifies if the action needs manual or automatic approval.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-budgets-budgetsaction.html#cfn-budgets-budgetsaction-approvalmodel
        '''
        result = self._values.get("approval_model")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnBudgetsActionProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnBudget",
    "CfnBudgetProps",
    "CfnBudgetsAction",
    "CfnBudgetsActionProps",
]

publication.publish()

def _typecheckingstub__fcf9a7d2538a7b213b0959a8dca9ebac8bd9adbb67b3989e4ad2e983d215ccb6(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    budget: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.BudgetDataProperty, typing.Dict[builtins.str, typing.Any]]],
    notifications_with_subscribers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.NotificationWithSubscribersProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e48291da0e0d52b22d4094e08b1071a9eb7e9781ef841ed60fbf1c118c7db23c(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__9be790a4c777b9d846ffd5e29641d5e3c1e0001a4faf20e8512e5ee5dc73a48f(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__c95887cba36441131745a708716d40542977a1478eafb13e3649b0bddc03c19c(
    value: typing.Union[_IResolvable_da3f097b, CfnBudget.BudgetDataProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__338a591d66627dac6d0524a4af3df9ae2f64ac27737f12b95bc7243a4566a5e3(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBudget.NotificationWithSubscribersProperty]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ed95504d1222347c1591bd33e0256ea9c7cfabe8856c857ffa5ee97b56e6455f(
    *,
    auto_adjust_type: builtins.str,
    historical_options: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.HistoricalOptionsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b2c7f5c59209a2623bf116ca3a20b23835ececd0df52736e4f148622f483afb2(
    *,
    budget_type: builtins.str,
    time_unit: builtins.str,
    auto_adjust_data: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.AutoAdjustDataProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    budget_limit: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.SpendProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    budget_name: typing.Optional[builtins.str] = None,
    cost_filters: typing.Any = None,
    cost_types: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.CostTypesProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    planned_budget_limits: typing.Any = None,
    time_period: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.TimePeriodProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ca892e141a9adeb986265203927fc16b8a26091edacd45cbc9ebe6689e4857bb(
    *,
    include_credit: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_discount: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_other_subscription: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_recurring: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_refund: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_subscription: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_support: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_tax: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    include_upfront: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_amortized: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
    use_blended: typing.Optional[typing.Union[builtins.bool, _IResolvable_da3f097b]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ba7bd7cc2be23305dffbf6031c061df699ccd87872fbd4ec418a99be7cf81185(
    *,
    budget_adjustment_period: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__ea30c5d87897db387daaab29d498d54bb0b490643c5fbb8fb1a5b9a125603de5(
    *,
    comparison_operator: builtins.str,
    notification_type: builtins.str,
    threshold: jsii.Number,
    threshold_type: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__07866499303a1a9ab70a645ecbda245fb51598e896b81d4f01f9cffeeac17bf1(
    *,
    notification: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.NotificationProperty, typing.Dict[builtins.str, typing.Any]]],
    subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5a81264d854f3d578cfafd932e1a5385f5f235b0b2fd9984ec61d7cd42705c9d(
    *,
    amount: jsii.Number,
    unit: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e5d0b208f458ade09c3843fe83aba0d6db3ddb09a594e82cdd14537ffc0e26f0(
    *,
    address: builtins.str,
    subscription_type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__77f51cb94a1e5a0ae65deee87b45596400f57823b1add7660a12635b0a091886(
    *,
    end: typing.Optional[builtins.str] = None,
    start: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__0bce15b7b8b999a87f796c503372a075fb7e77b171e9e458dd4b05e88e303d02(
    *,
    budget: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.BudgetDataProperty, typing.Dict[builtins.str, typing.Any]]],
    notifications_with_subscribers: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudget.NotificationWithSubscribersProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5feaf1ccce7286d2cae539317638953135d21b7e897f0ded2f3a275d0516a886(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    action_threshold: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.ActionThresholdProperty, typing.Dict[builtins.str, typing.Any]]],
    action_type: builtins.str,
    budget_name: builtins.str,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.DefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_role_arn: builtins.str,
    notification_type: builtins.str,
    subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
    approval_model: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5e4d5fcd5b6fa47f421ce5a934095661754d1490e6d5622d679c21d056e2339d(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__37f0f35c0901b3170a2a787f6b136e6de796aa9287397d112b1716e76cfdf2fa(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__6444694cd4e1cfe409941297d12b4f71c45625cb1357bf1a3b12f86d4a288f85(
    value: typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.ActionThresholdProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__93ee3f487b114766988c6712b16108f0a81084444e5dcb38f58aa6ca5c1ac0eb(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__886294fdca463440eacd919c52ef223cd761321b3e92068ed0e10930b6c45bd8(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__af7c0aaf6be25381fc5e59a606f980f8beb020b05d0d1b4e00097df9b213d1f4(
    value: typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.DefinitionProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__20f3acfbe196dceebb62052bc3a9709ca03c3cd1385bd0b8f47b14ebe24baea6(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53476f930c7990ef6a398f9ead465189ebfbebc41a5d5d7cb519d5ad1e21440e(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d139b5f0aab0780aebc710ff294cf4038924446db4e70d8dd7ceaf018b79e653(
    value: typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, CfnBudgetsAction.SubscriberProperty]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__cc9b0ed2b1fd2266f52e8858e29800b46ee5d46db67048e5fcafb370fe1d7fc3(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__652e2954f340271681973613d60d4049ebd81a75c8987611d889045de156b8b3(
    *,
    type: builtins.str,
    value: jsii.Number,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__96306621a1aae8f106a12b9134576206e8e4754361a681338ac6381f2e0940b2(
    *,
    iam_action_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.IamActionDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    scp_action_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.ScpActionDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ssm_action_definition: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.SsmActionDefinitionProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__22f7bad74675d504f2471ac5656611eebbc86ce649e820a38f5961c5ae990704(
    *,
    policy_arn: builtins.str,
    groups: typing.Optional[typing.Sequence[builtins.str]] = None,
    roles: typing.Optional[typing.Sequence[builtins.str]] = None,
    users: typing.Optional[typing.Sequence[builtins.str]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__31fd74b3c2a89d6419f8ea513fe7d522d39278beb5f299a80f1ee727475e6777(
    *,
    policy_id: builtins.str,
    target_ids: typing.Sequence[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__4e936943168730bfe281e6f6adccb2fafe8a803ed858a444a60decfc26cc38f7(
    *,
    instance_ids: typing.Sequence[builtins.str],
    region: builtins.str,
    subtype: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53b54f7e3522aacd600ff090e6221f615565664782c185bdcb801f95f68daf7f(
    *,
    address: builtins.str,
    type: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__2bf8a3fb960018ac6b97a0b01c3bd29dd4bf1acba7443236249ad39f7ced10a5(
    *,
    action_threshold: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.ActionThresholdProperty, typing.Dict[builtins.str, typing.Any]]],
    action_type: builtins.str,
    budget_name: builtins.str,
    definition: typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.DefinitionProperty, typing.Dict[builtins.str, typing.Any]]],
    execution_role_arn: builtins.str,
    notification_type: builtins.str,
    subscribers: typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnBudgetsAction.SubscriberProperty, typing.Dict[builtins.str, typing.Any]]]]],
    approval_model: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass
